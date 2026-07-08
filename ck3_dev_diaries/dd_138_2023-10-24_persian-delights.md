---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1603428/"
forum_thread_id: 1603428
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 138
title: "Dev Diary #138 - Persian Delights"
dd_date: 2023-10-24
author_handle: Trin Tragula
expansion: Legacy of Persia
patch: Patch 1.11
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2163
inline_image_count: 13
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1603428'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2642.jpg?1698139511
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_142_to_144
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_262_to_266
    action: preserved_and_flagged
    counts:
      Like: 138
      Love: 63
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_274_to_384
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_385_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2642.jpg?1698139511)
<!-- artifact:thread_banner:end -->

# Dev Diary #138 - Persian Delights

<!-- artifact:thread_metadata:start -->
- Thread starter [Trin Tragula](https://forum.paradoxplaza.com/forum/members/trin-tragula.18587/)
- Start date [Oct 24, 2023](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-138-persian-delights.1603428/)
<!-- artifact:thread_metadata:end -->

Hello and welcome to this development diary about flavor additions to the greater Iran area. That means in this diary you will get a test of many things that, while individually small, aim to increase the overall authenticity and uniqueness in this part of the world.  
I will also begin with a shout out to [@Vaniljkaka](https://forum.paradoxplaza.com/forum/members/1630093/) who worked on the first draft of this DD and did a lot of the event and research work for Legacy of Persia.  

---

**Historical Flavor**  

One way to significantly improve the state of the game in a given start date is to look into what unresolved issues were ongoing in a specific location at the time. To a large degree that is the thinking behind the struggle system itself but and as already described in a [previous development diary](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-136-our-vision-for-persia.1601384/) there is now both a new 867 bookmark start, and a struggle called the Iranian Intermezzo to achieve this.  

But the struggle alone cannot cover everything that was important for a ruler in medieval Iran in 867 or 1066. We have therefore taken the opportunity to more thoroughly research the starting situation for both starts, adding new rulers, dynasties, rivalries, as well as less politically influential characters such as scholars or artists active in our time period. Existing family trees have also been significantly expanded in many cases and should also now make use of a new set of coat-of-arms using Iranian or Islamic elements.  

Additionally, there has been a general go-over of the cultural and religious setup of the entire region, with adjustments here and there aiming to better reflect the political realities of the time.  

![image 01.png](https://forumcontent.paradoxplaza.com/public/1021976/image 01.png "image 01.png")



The biggest changes are to certain religious groups or sects that were important in 9th century Iran - the Mu’tazila, the Khurramites, the Azariqa. The rebellious, egalitarian Khurramites would be particularly suited for underdog playthroughs though none are landed at the start, whereas the fanatic Azariqa stand ready to unleash a terrifying wave of assassinations, to avenge the Battle of Nahrawan and the many slights they believe that they’ve suffered since. Both these faiths have been given new tenets to portray their unique worldviews. At game start in 867 there is also an ongoing Azariqa rebellion, which you can partake in if you want to attempt to form an Azariqan Caliphate.  

![An image of the Azariqa faith and its three tenets, highlighting the Fedayeen tenet and its new art](https://forumcontent.paradoxplaza.com/public/1021977/image 02.png "An image of the Azariqa faith and its three tenets, highlighting the Fedayeen tenet and its new art")


*[The Fedayeen tenet is shared by the Azariqa and the Nizari, and allows you to recruit and utilize fearsome assassins - fanatics devoted to slaying the unbelievers.]*  


![An image of the Khurramite faith and some of its counties in 867.](https://forumcontent.paradoxplaza.com/public/1021978/image 03.png "An image of the Khurramite faith and some of its counties in 867.")


*[The rural, rebellious Khurramites are present in pockets all over Iran, though their great rebellions of the mid-9th century have long since been suppressed. Also featured in the screenshot is the new geographic special location of Mount Damavand. One of multiple new special buildings in the update.]*  


![An image of the culture map of the greater Iranian area in 867, showing the new Brahui culture in much of modern Balochistan.](https://forumcontent.paradoxplaza.com/public/1021979/image 04.png "An image of the culture map of the greater Iranian area in 867, showing the new Brahui culture in much of modern Balochistan.")


*[The cultural map should be largely familiar, with some notable exceptions like 1066 and 867 now having differing setups in the region of Balochistan.]*  

When it comes to cultures, we have added a number of new cultural traditions, some of which add new gameplay elements such as the Qanat building line (from the Irrigation Experts cultural tradition which replaces Dryland Dwellers) or the new Court Scholar court position (from the new Beacon of Learning tradition) which can be sponsored to unlock new innovations.  

![An image of three of the Cultural Traditions that Persians have, featuring icons portraying a water wheel, and a scholar looking at an upside-down earth globe - and indeed, medieval Islamic cartography would seem upside-down to us.](https://forumcontent.paradoxplaza.com/public/1021980/image 05.png "An image of three of the Cultural Traditions that Persians have, featuring icons portraying a water wheel, and a scholar looking at an upside-down earth globe - and indeed, medieval Islamic cartography would seem upside-down to us.")


*[The Persians in particular have been given three new traditions to reflect all the refinement and enlightenment that made them so admired by Arabs and Turks alike.]*  

For the greater region covered by the update we now also have Jirga (for the Afghan, Baloch and Brahui cultures) which among other things unlock the Tribal Elective Succession form as well as new regional traditions that unlock unique Man-at-Arms types such as the Zupin (Pragmatic Creed) Spearmen or the Tarkhans (Frontier Warriors).  

![image 06.png](https://forumcontent.paradoxplaza.com/public/1021981/image 06.png "image 06.png")



We are also adding historically inspired decisions and events to the region, with the aim of opening up the same possibilities to rulers in our game that historical rulers of the era would have had. This also means that some previously unlikely historical scenarios are now encouraged, for instance Turkic conquerors in general and the Seljuks in particular are more likely to show up and make a new home for themselves in the Iranian plateau, and as a rising ruler in Iran you have new ways of promoting alternate Islamic faiths in the region that are not as present yet at game start (such as the Maturidi denomination of Sunni Islam or Shia Imamism).  

For the Seljuk arrival in the late 900s there is also a game rule to make their entrance more random or to turn it off entirely.  
Last but not least the chaotic setup in 867 is now further improved by an early event chain about the Zanj rebellion which should add even more uncertainty and dynamism to an already quite open starting situation.  

![image 07.png](https://forumcontent.paradoxplaza.com/public/1021982/image 07.png "image 07.png")



---

**Viziers**  

A new type of diarchy coming in Legacy of Persia, viziers were historically many things. They were powerful private landholders, vital linchpins of the civil service, some of the most corrupt people in the world, and extravagantly dramatic party-hosts.  

![image 08.png](https://forumcontent.paradoxplaza.com/public/1021983/image 08.png "image 08.png")



Mechanically, Viziers may be appointed by duke-tier or higher clan-government characters. Whilst incumbent, they grant you extra tax jurisdictions (scaled to their stewardship) and add a portion of their own tax collector aptitude directly to all of your tax collectors’ aptitudes, providing a powerful direct modifier on how much gold you get per month. How large a portion of aptitude they grant scales with how heavily the Scales of Power are swung towards them, so a more empowered vizier offers both benefits and drawbacks to their liege.  

![image 09.png](https://forumcontent.paradoxplaza.com/public/1021984/image 09.png "image 09.png")



Unlike regents, being a vizier isn’t a prestigious position for a noble — you are, after all, merely a civil servant, and what’s worse one with actual *work* you’re expected to do — instead, landless courtiers and minor barons from your faith’s dominant gender compete for the post. Having the vizier in your pocket is still desirable, though, so prospective viziers at court will politick behind the scenes, gaining friendships and rivals with other prospective candidates, their liege’s spouses, and their liege’s stay-at-home adult children.  

These relations in turn directly contribute to vizier succession score, so a candidate who’s friends with the current vizier will see themselves climb the ranking, whereas one who’s made an enemy of their liege’s spouse will see their score fall. For the same reason, prospective viziers will often learn their liege’s language, seeking to further their prospects for promotion.  

As civil servants, viziers don’t have access to *quite* as many powers as regents. Predominantly they’ll embezzle and try to give negative county modifiers to vassals in exchange for gold, though a complacent liege who lets the Scales creep too far towards their supposedly-loyal vizier will find that they’re still capable of launching coups. Viziers are also usable in the new-ish confidant council position, which allows you to substitute them in instead of your spouse for spousal council tasks (your choice of which, naturally).  

Though such functionaries can be fired at any time, removing the vizierate regardless of the status of the Scales of Power, a vizier with high swing is one who’s enmeshed themselves thoroughly, and who cannot be removed *completely* without consequence. Above a certain Scale swing threshold, firing your vizier will give you a severe negative economic modifier that harms your monthly income. This scales to how much swing the vizier had — so sure, you can fire them at 80+ swing if you like, but don’t think they won’t have arranged a little job security for just such an occasion.  

![image 10.png](https://forumcontent.paradoxplaza.com/public/1021985/image 10.png "image 10.png")



An easier way to remove civil servants is to kick them upstairs: giving your vizier a county (or, if the Scales are really swung in their favor, a duchy) will also end the vizierate, this time without any economic fallout. Everyone loves a promotion, after all.  

Finally, you may recall that I mentioned viziers were legendarily corrupt: though not always strictly true, this was generally the case, and actually a feature of the position rather than a bug. The role of a corrupt vizier was to run the realm’s finances, and it was generally understood that they’d enrich themselves in the process. It was fairly common for viziers to pay significant bribes straight to the liege to get the position — that and to capture and audit the last vizier for undeclared revenue.  

The advantage to this for the liege was that, when they needed money in a pinch, rather than have to collect a special tax from the realm as a whole, force powerful vassals and governors to cough up more cash, or individually audit every petty tax collector, there was one person in the realm they could generally guarantee not only had money but had more money than they should have. Minimal overhead, maximum convenience. At least, for the liege.  

![image 11.png](https://forumcontent.paradoxplaza.com/public/1021986/image 11.png "image 11.png")



In-game, we represent this through your vizier’s income and extravagance modifiers. They receive an income from positional corruption proportional to your own income (this doesn’t count towards the embezzlement secret, as it’s technically part of their official remuneration). Every so often, they’ll spend this money on character modifiers for treasure, activities, properties, or charity. Once they have one modifier of each type, they’ll begin again, spending more money on more expensive extra types of each modifier, up to four tiers.  

![image 12.png](https://forumcontent.paradoxplaza.com/public/1021987/image 12.png "image 12.png")



Lieges can then mulct their viziers via interaction, fining them for their excesses. This deletes a rank of the vizier’s extravagance modifiers, liquidating them and transferring gold to the ruler that increases with the tier (and number!) of modifiers liquidated. Naturally, viziers aren’t generally too happy with this, even if the process further enmeshes them as the most important state official, but there’s not much they can do about it other than rebuild their losses. Which, naturally, makes them more attractive to mulct again down the line…  

![image 13.png](https://forumcontent.paradoxplaza.com/public/1021988/image 13.png "image 13.png")



We’ve included about ~160 different modifier descriptions for what viziers are spending their money on, of which about half are explicitly historically attested (comments in the script file for anyone particularly interested in which), and another quarter reasonably probable. The remaining quarter is us trying to keep up with the lavish standards for extravagances set by history’s actual vizierates. These do vary vizier by vizier, so you should see your viziers purchasing extravagance modifiers relevant to their traits and interests.  

---

That was all for this diary! I hope it has given a general idea of the type of flavor content that you can expect in Legacy of Persia, without spoiling all of what there is to discover.

<!-- artifact:reactions:start -->
- 138 Like
- 63 Love
- 7 (unlabeled — rendered as base64 data URI)
- 6 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Trin Tragula](https://forum.paradoxplaza.com/forum/members/trin-tragula.18587/)**
Role: Game Designer - Crusader Kings 3
Badges: 36
Reaction score: 16,644

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
