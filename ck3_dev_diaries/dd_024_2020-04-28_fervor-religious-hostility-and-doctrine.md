---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1386925/"
forum_thread_id: 1386925
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 24
title: "Dev Diary #24 - Fervor, Religious Hostility, and Doctrine Showcase"
dd_date: 2020-04-28
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
body_word_count: 1515
inline_image_count: 9
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1386925'
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
    location: raw_lines_~28_to_140
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_139
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1362.jpg?1588190981
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_142_to_144
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_250_to_253
    action: preserved_and_flagged
    counts:
      Like: 70
      (unlabeled — rendered as base64 data URI): 12
      Love: 2
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_261_to_369
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

<!-- artifact:thread_banner:start -->
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1362.jpg?1588190981)
<!-- artifact:thread_banner:end -->

# Dev Diary #24 - Fervor, Religious Hostility, and Doctrine Showcase

<!-- artifact:thread_metadata:start -->
- Thread starter [Baron von Shoes](https://forum.paradoxplaza.com/forum/members/baron-von-shoes.1426511/)
- Start date [Apr 28, 2020](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-24-fervor-religious-hostility-and-doctrine-showcase.1386925/)
<!-- artifact:thread_metadata:end -->

Hello everyone, and welcome back to our final Dev Diary on Religion in Crusader Kings 3! Today I will be talking about what the mysterious Fervor is, how that ties into Heresies and Heresy Outbreaks, as well as how Religious Hostility works and some of the ways that Doctrines can impact it. To wrap things up, I will show off some additional never-before seen Tenets and Doctrines!  

**Fervor**  
Every Faith has a Fervor score, which is a representation of how strongly adherents of that Faith believe in the righteousness of their religious and secular leaders. While Fervor has a slow ticking increase over time, it is primarily influenced by the virtuousness or sinfulness of that Faith’s leaders. Virtuous priests can inspire a populace and rally the people behind themselves, while sinful ones (especially religious heads) can cause massive scandals that damage the faithful’s trust in their religious institutions.  

![DD_WM_Scandal.png](https://forumcontent.paradoxplaza.com/public/559275/DD_WM_Scandal.png "DD_WM_Scandal.png")


[A screenshot of the Pope looking very guilty after being caught in flagrante]  

Adherents of a Faith with high Fervor are willing to fight and die for their beliefs. They gain bonus resistance to attempts to convert them to another faith, and both secular and religious leaders can declare Holy Wars to spread their Faith across the world. However, while these Holy Wars are ostensibly waged in the name of the divine, in practice they often tend to be little more than opportunistic land-grabs — as a result, every Holy War declared will slightly damage a Faiths’ Fervor, while losing land to hostile Holy Wars will actually increase your Faith’s Fervor as the embattled faithful dig in and fight for their way of life!  

When a Faith’s Fervor drops, adherents of that Faith become vulnerable to conversion. Characters are more willing to accept a Demand Conversion when their Faith’s Fervor is low, and the Court Chaplain’s ‘Convert County’ task gains a scaling bonus against Faiths whose Fervor is lower than their own. In addition, if Fervor drops low enough, a Faith becomes vulnerable to heresy outbreaks!  

**Heresy Outbreaks**  
A heresy outbreak is what happens when a ruler becomes disillusioned with their current Faith and is swayed to join a different one. If there is already a heretical Faith present nearby, they will convert to that one automatically. If no suitable heresies are around, they will become a heresiarch and start espousing the doctrines of a brand new Faith, which is typically (but not always), one from their Religion.  

A ruler who converts to or founds a new heretical Faith will then attempt to convince nearby rulers of their old Faith to join them, with the success rate of this being dependent on how low their old Faith’s fervor has fallen. This means that while heresy outbreaks can vary wildly in size, converts to the new heresy will tend to remain clustered together in a specific region — this both protects the burgeoning Faith while simultaneously limiting its influence in distant lands.  

![DD_WM_Heresy.png](https://forumcontent.paradoxplaza.com/public/559277/DD_WM_Heresy.png "DD_WM_Heresy.png")


[A screenshot showing an outbreak of Lollardy, originating in southern England]  

As you can imagine, heresy outbreaks are incredibly divisive events; nobody wants to sit on the fence when your immortal soul is on the line! As a result, after a heresy outbreak occurs both the old Faith and the new heretical Faith will gain a substantial increase to their Fervor score. As this is likely to encourage Holy Wars for both sides, it is not uncommon for a new period of religious violence to follow as the two Faiths fight for supremacy!  

Ultimately, the flow from scandal to heresy to zealousness and back will cause Fervor to vary wildly over the course of a game of CK3. Unlike the relatively static Mortal Authority in CK2, this means that even the big dominant religions will have periods of weakness, making them vulnerable to fractures and religious violence.  

**Religious Hostility**  
Speaking of religious violence, how does that work? With so many different Faiths and Religions in Crusader Kings III, how do they view each other? What is the difference between how an Orthodox ruler views a Catholic, a Bogomil, and an Ash’ari?  

In Crusader Kings III this is all handled by the Religious Hostility system. For characters of a given Faith, every other Faith in the game will receive one of the following rankings:  


1. Righteous
2. Astray
3. Hostile
4. Evil
Righteous is how a Faith views itself and, in a few rare circumstances, other Faiths that have certain things in common with it. Righteous Faiths have no penalties at all with each other.  

Astray is how a Faith views other Faiths that have similar goals and ideals but are just a little… wrong. For example, Orthodoxy and Catholicism consider each other to be Astray. Astray Faiths have only a minor opinion penalty with each other.  

Hostile is how most Faiths view their heresies and other significantly divergent Faiths. Opinion penalties are more substantial at this level, and rulers gain the ability to declare Holy Wars against rulers of Hostile Faiths. However, intermarriage is still common when it is politically convenient, and alliances can still be forged between rulers of Hostile Faiths.  

Evil Faiths are considered to be an anathema, and cannot be tolerated. Evil Faiths suffer the most severe opinion penalty possible, and Holy Wars against each other become commonplace. Rulers will almost never accept marriages with characters of an Evil Faith, making alliances all-but-impossible.  

So how is Religious Hostility determined? The primary factor is what Religion Family both Faiths belong to:  

![DD_Hostility.png](https://forumcontent.paradoxplaza.com/public/559280/DD_Hostility.png "DD_Hostility.png")


[A screenshot of a spreadsheet showing how base Religious Hostility is calculated, with Abrahamic Faiths being the least tolerant and Eastern Faiths being the most tolerant]  

But wait, if Abrahamic Faiths view other Faiths within the same Religion has Hostile, why do Catholicism and Orthodoxy only see each other as Astray? The answer to that, my friend, is Doctrines!  

**Doctrine & Tenet Showcase**  
Now we’re going to take some time to reveal a bunch of the various Doctrines and Tenets available for Faiths in Crusader Kings 3. For starters, the Catholic, Orthodox, Apostolic, and Coptic Faiths all have the ‘Ecumenism’ Doctrine, which changes the Hostility of any other Faith with the same Doctrine to just ‘Astray’, thus allowing these Faiths to have cordial relations with each other.  

![DD_WM_Doctrine_Ecumenism.png](https://forumcontent.paradoxplaza.com/public/559281/DD_WM_Doctrine_Ecumenism.png "DD_WM_Doctrine_Ecumenism.png")


[A screenshot showing the Ecumenism doctrine, which reduces Hostility between certain Christian Faiths]  

In a similar vein, the various Muslim Faiths all have a doctrine representing their belief in the true succession for Muhammad. The various Sunni Faiths all see each other as Astray, with the same being true for the collective Shia Faiths and the collective Muhakkima Faiths.  

The embattled minority of Gnostic Faiths have an ever stronger version of this; having always struggled to have their beliefs accepted, they see all other Gnostic Faiths as being fully ‘Righteous’. This allows us to have coalitions of Faiths within or even outside of a Religion that see some Faiths as allies and others as enemies, completely changing the dynamic of how religious relations play out in Crusader Kings III.  

![DD_WM_Doctrine_Gnositism.png](https://forumcontent.paradoxplaza.com/public/559283/DD_WM_Doctrine_Gnositism.png "DD_WM_Doctrine_Gnositism.png")


[A screenshot showing the Gnosticism Tenet, which among other things eliminates Religious Hostility between Gnostic Faiths]  

Finally there are other Tenets which can modify how your Faith sees, and is seen by, Faiths in other Religions.  

![DD_WM_Doctrine_Syncretism.png](https://forumcontent.paradoxplaza.com/public/559284/DD_WM_Doctrine_Syncretism.png "DD_WM_Doctrine_Syncretism.png")


[A screenshot showing various Syncretism Tenets, which reduce Religious Hostility across entire Religions]  

Diplomacy not your thing? Try some warfare!  

![DD_WM_Tenets_Warfare.png](https://forumcontent.paradoxplaza.com/public/559285/DD_WM_Tenets_Warfare.png "DD_WM_Tenets_Warfare.png")


[A screenshot showing various warfare-focuses Doctrines and Tenets, including Armed Pilgrimages which enables Crusades]  

Or is all of this just too secular for you? After all, isn’t religion supposed to be about spiritualism, a belief in otherworldly entities beyond our understanding? Well then maybe one of these tenets would suit you...  

![DD_WM_Tenets_Mysticism.png](https://forumcontent.paradoxplaza.com/public/559287/DD_WM_Tenets_Mysticism.png "DD_WM_Tenets_Mysticism.png")


[A screenshot showing various Tenets of a more spiritual nature: Astrology, Auspicious Birthright, Reincarnation, Sun Worship, Sky Burials, and Esotericism]  

Of course, this is just a sample of the Tenets and Doctrines that we have in Crusader Kings 3. It would take too long to go into this level of detail for all of them, but here is a teaser of some available Tenets on the Faith Creation screen, showing both some previously revealed and unrevealed Tenets.  

![DD_WM_Tenets_List.png](https://forumcontent.paradoxplaza.com/public/559288/DD_WM_Tenets_List.png "DD_WM_Tenets_List.png")


[A snippet of a handful of available Tenets from the Faith Creation screen]  

That’s all for now — hopefully this post has given you something to think about as you plan your first campaign of Crusader Kings III, and every one after that!

<!-- artifact:reactions:start -->
- 70 Like
- 14 (unlabeled — rendered as base64 data URI)
- 12 (unlabeled — rendered as base64 data URI)
- 2 Love
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Baron von Shoes](https://forum.paradoxplaza.com/forum/members/baron-von-shoes.1426511/)**
Role: Content Designer
Badges: 95
Messages: 65
Reaction score: 2,138

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
