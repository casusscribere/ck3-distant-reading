---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1602548/"
forum_thread_id: 1602548
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 137
title: "Dev Diary #137 - Machinations of a Clan"
dd_date: 2023-10-17
author_handle: Servancour
expansion: Legacy of Persia
patch: Patch 1.11
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2022
inline_image_count: 17
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1602548'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2620.jpg?1697530322
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_284_to_288
    action: preserved_and_flagged
    counts:
      Like: 147
      Love: 50
      (unlabeled — rendered as base64 data URI): 8
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_296_to_386
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_387_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2620.jpg?1697530322)
<!-- artifact:thread_banner:end -->

# Dev Diary #137 - Machinations of a Clan

<!-- artifact:thread_metadata:start -->
- Thread starter [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)
- Start date [Oct 17, 2023](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-137-machinations-of-a-clan.1602548/)
<!-- artifact:thread_metadata:end -->

Salutations!  

It’s been a while since I last wrote a DD, so a quick (re)introduction might be in order. I’m Emil, aka “Servancour”, one of your resident CK3 game designers. I’ve been on the project since way before release, and tend to mostly focus a lot on game mechanics and systemic features. Which, in fact, brings me to why I’m here today. When we settled on Persia as the focus for our upcoming Flavor Pack, we soon came to realize that this would be an excellent opportunity to revisit the Clan Government and give it a much needed update.  

Clans, as you currently know them, are very similar to Feudal. There are only two real points of difference between them. Opinion is a major factor in their obligations, meaning that a vassal’s opinion of their liege affects how much taxes and levies they will give to their liege. Secondly, they have access to and utilize vassal contracts, albeit in a slightly stripped down version, with less available options than their Feudal counterparts.  

This begs the question; How can we make Clan Government stand out? We’ve already identified one aspect above, so our first action and problem to solve is this - How do (or should) Clans manage their vassals? Secondly, and perhaps much more important, is what does a *Clan* actually represent? What does the name mean for gameplay?  

But I’m getting ahead of myself. Let’s start with the first question, shall we? And have a look at Clan obligations.  

---

**Tax Jurisdictions and Tax Collectors**  

While we knew we wanted to add something new to Clan obligations, we had to ask ourselves how we wanted to make it different. As with all things Crusader Kings, adding a new element that makes use of characters felt like a natural fit, to give obligations some personality if you will. Meet the Tax Collector.  

![image01.png](https://forumcontent.paradoxplaza.com/public/1019877/image01.png "image01.png")



You’ll have access to a limited number of Tax Jurisdictions. To which you assign your Clan vassals as Taxpayers, allowing you to gain both taxes and levies from your subjects. A Jurisdiction requires a Tax Collector to function however. So before you can collect any taxes, you need to appoint one of your courtiers as a Tax Collector for each Jurisdiction.  

![image02.png](https://forumcontent.paradoxplaza.com/public/1019878/image02.png "image02.png")



With Tax Collectors, you won’t manage the obligations of your vassals directly. Instead, you manage them *through* your Tax Collector. Similar to a Court Position, a Tax Collector uses their aptitude to set the obligations of the vassals assigned to them. Higher levels of aptitude means that you’ll get more taxes and levies. Aptitude is primarily based on their skills, with Learning being the more important one, but their opinion of you also plays a significant part. To maximize the use of your Tax Collectors, you’ll want to find and appoint a skilled character, and then put the sway scheme to good use in order to squeeze as much gold from your subjects as possible.  

![image03.png](https://forumcontent.paradoxplaza.com/public/1019879/image03.png "image03.png")



While your Tax Collectors act as your intermediaries, you are still able to exact a certain degree of control of *how* they should manage your vassals. This is where Tax Decrees come into play. A Tax Decree is essentially how you want your vassals to be taxed, changing the obligations and providing an assortment of additional benefits.  

![image04.png](https://forumcontent.paradoxplaza.com/public/1019880/image04.png "image04.png")



With the introduction of Tax Decrees, it made perfect sense to move over some aspects of vassal contracts to this new system instead. For example, this is where you’ll find Iqta, Ghazi, and Jizya to use as you see fit. While you won’t have to bother with decrees if you don’t want to, they do give you opportunities to min-max in different ways. Decrees change the obligations of your vassals, either increasing or reducing them, in exchange for other boons. Take Iqta as an example. Iqta is a great option if you find yourself with vassals who are slightly upset, just enough for you to start taking notice, and if you also finds yourself being at war frequently, as Iqta provides you with increased Men-at-Arms Damage based on the number of assigned vassals alongside an opinion bonus.  

![image05.png](https://forumcontent.paradoxplaza.com/public/1019881/image05.png "image05.png")



One thing to consider is that the modifiers applied to the obligations occur on the level as set by your Tax Collector. Which makes Decrees more or less powerful depending on the Tax Collector in question. Again, looking at the effects of Iqta, -20% to both taxes and levies won’t be very noticeable if your Tax Collector has a terrible aptitude. This makes Iqta very rewarding for the price you pay, since the gained benefit is pretty good. If your Tax Collector is excellent on the other hand, you’ll feel the impact of those 20%.  

That about sums it up for how Tax Jurisdictions, Collectors, and Decrees work. With obligations out of the way, let’s go back and answer our second question!  

---

**House Unity**  

As the name suggests, Clans should be all about the clan itself and its members. Something that we really don’t represent at the moment. Nor does it have any real impact on how you play the game. To solve this, and put a significantly larger emphasis on your House when you are playing as a Clan, we are introducing House Unity.  

Unity represents the overall state of a House. Essentially the internal relationships between its members and the attitude they have towards each other. In many ways, Unity is the result of how you choose to interact with your fellow House members. We show everything regarding Unity in each Clans House view, allowing you to easily inspect your own Unity, and the Unity of other Houses.  

![image06.png](https://forumcontent.paradoxplaza.com/public/1019882/image06.png "image06.png")



We measure Unity on a scale between 0 and 200, divided up into five distinct ranges, or levels. Each level comes with a set of impactful rules and trade offs that may have a noticeable impact on how you play the game. By default, most Houses start in the middle. Essentially a “neutral” level. From there, they’ll be able to actively increase or decrease their Unity.  

The levels are as following, listed from lowest to highest level of Unity:  


- Antagonistic
- Competitive
- Impassive
- Friendly
- Harmonious

Thematically, having a high level of Unity means that you’ll enjoy internal stability and have House members that (generally speaking) adopt a friendly attitude towards each other. But you’ll pay for it with a reduced capability to wage wars as efficiently. CBs become more expensive to use, and you can no longer use the Invasion CB. A low level of Unity provides you with the opposite. You’ll gain a great deal of military might, allowing you to more easily conquer large swathes of land, but pay the price of reduced internal stability. Depending on your playstyle, you might enjoy a particular direction more than the other. Regardless of your own preference, having either low or high levels of Unity is meant to be equally viable.  

Instead of having me ramble about the effects of each level, here are some nifty screenshots showing you what they look like:  

![image07.png](https://forumcontent.paradoxplaza.com/public/1019883/image07.png "image07.png")


![image08.png](https://forumcontent.paradoxplaza.com/public/1019884/image08.png "image08.png")


![image09.png](https://forumcontent.paradoxplaza.com/public/1019887/image09.png "image09.png")


![image10_02.png](https://forumcontent.paradoxplaza.com/public/1019926/image10_02.png "image10_02.png")


![image11.png](https://forumcontent.paradoxplaza.com/public/1019889/image11.png "image11.png")



Other than the passive effects, you also gain access to a set of unique decisions. Most of which are available only to the House Head, as they provide powerful boons for the entirety of a House. The primary currency for these decisions is Piety. Since most Clans belong to an Islamic faith, this felt like a natural fit. Besides, Piety is generally more difficult to get than Prestige, making you consider where and how to spend that hard earned Piety.  

Some of these decisions make use of a completely new type of modifier; a modifier that scales on the number of landed House members. If you are like me, and like to utilize nepotism to the fullest, these modifiers can become *incredibly* powerful. Be mindful that the Piety cost will increase accordingly.  

For all you modders out there, you can use scaling modifiers in every place you use regular modifiers. You simply feed it a value for how you want it to scale.  

Let’s look at an example. If your House is Antagonistic, you can use the decision “Reinforce Army with Loyal Officers”:  

![image12.png](https://forumcontent.paradoxplaza.com/public/1019890/image12.png "image12.png")


![image13.png](https://forumcontent.paradoxplaza.com/public/1019891/image13.png "image13.png")



Last, but certainly not least, Unity directly affects the outcome of your succession. Each level has an impact on the outcome of how titles are inherited, and the succession changes automatically as your House’s Unity changes. They all maintain a variant of Partition, meaning that titles will always be split to some extent. When you are Antagonistic, all eligible children inherit equal shares. If you are Harmonious, the primary heir inherits the majority of the titles (at least two thirds). With varying degrees in-between. At worst, this means that you don’t have to deal with Confederate Partition, and at best, you have an easier time accessing a superior version of High Partition. The drawback? While you can try to get a single heir succession law, such as Primogeniture, it will be more difficult and expensive to do so.  

![image14.png](https://forumcontent.paradoxplaza.com/public/1019892/image14.png "image14.png")



Now that we know what Unity does, let’s explore how it’s impacted by gameplay. As mentioned previously, Unity is all about the members of a House and how they interact. This will become apparent as you start interacting with your family members. A lot of existing interactions have been updated to also have an impact on your Unity in different ways. Whenever you are playing as Clan that is. Taking what we call “divisive” actions, such as Revoke Title or Imprison, against fellow House members will naturally reduce your House’s Unity. Meanwhile, “unifying” actions, such as Negotiate Alliance or Offer Ward, will increase Unity. Unity is therefore really a byproduct of how you and your fellow House members interact with each other.  

With that said, the House Head enjoys a number of additional actions, giving them a greater degree of control in how they want to direct the Unity of their own House. The foremost of these is a decision in which the Head actively takes a stance and chooses a direction to steer their Unity. Then we also have two new interactions the Head can use on members of their House, both of which act as a double-edged sword and have some clear advantages and drawbacks.  

![image15.png](https://forumcontent.paradoxplaza.com/public/1019893/image15.png "image15.png")


![image16.png](https://forumcontent.paradoxplaza.com/public/1019894/image16.png "image16.png")


![image17.png](https://forumcontent.paradoxplaza.com/public/1019895/image17.png "image17.png")



There are of course many more interactions, far too many to list all of them here, which will have an impact on your Unity. Worth mentioning is that the immediate impact of these interactions is fairly small, but they stack up over time, especially when you are not the only one within your House who will be using them.  

Rest assured that you’ll have plenty to explore as you get your hands on the updated Clan Government later this year, which will be included with the free update launching alongside Legacy of Persia!

<!-- artifact:reactions:start -->
- 147 Like
- 50 Love
- 9 (unlabeled — rendered as base64 data URI)
- 9 (unlabeled — rendered as base64 data URI)
- 8 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)**
Role: Game Designer
Badges: 4
Reaction score: 9,949

*[Full game-badge icon list of 30 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
