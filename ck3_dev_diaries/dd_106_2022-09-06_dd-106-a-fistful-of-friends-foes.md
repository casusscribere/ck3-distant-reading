---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1540926/"
forum_thread_id: 1540926
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 106
title: "DD #106: A Fistful Of Friends & Foes"
dd_date: 2022-09-06
author_handle: PDS_Noodle
expansion: Friends and Foes
patch: Patch 1.7 (Bastion)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 3446
inline_image_count: 26
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1540926'
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
    location: raw_lines_~28_to_120
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_122_to_123
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_382_to_386
    action: preserved_and_flagged
    counts:
      Like: 113
      Love: 25
      (unlabeled — rendered as base64 data URI): 8
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_394_to_451
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_452_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# DD #106: A Fistful Of Friends & Foes

<!-- artifact:thread_metadata:start -->
- Thread starter [PDS_Noodle](https://forum.paradoxplaza.com/forum/members/pds_noodle.1394234/)
- Start date [Sep 6, 2022](https://forum.paradoxplaza.com/forum/developer-diary/dd-106-a-fistful-of-friends-foes.1540926/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/dd-106-a-fistful-of-friends-foes.1540926/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/dd-106-a-fistful-of-friends-foes.1540926/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/dd-106-a-fistful-of-friends-foes.1540926/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22941](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/development-diary-105-1-7-bastion-update.1540182/ "Development Diary #105: 1.7 &quot;Bastion&quot; Update") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/development-diary-107-1-7-0-bastion-update-notes.1541141/ "Development Diary #107: 1.7.0 &quot;Bastion&quot; Update Notes")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/dd-106-a-fistful-of-friends-foes.1540926/?prdxDevPosts=1)

![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2052.jpg?1662558444)

# DD #106: A Fistful Of Friends & Foes

- Thread starter [PDS_Noodle](https://forum.paradoxplaza.com/forum/members/pds_noodle.1394234/)
- Start date [Sep 6, 2022](https://forum.paradoxplaza.com/forum/developer-diary/dd-106-a-fistful-of-friends-foes.1540926/)

Hello everyone!  

Nice to meet all of you! A little background on me: I am Noodle, a Game Designer on CK3. I’ve been on this project since before the release of the game, but for most of its life I’ve been some delicious flavour of QA. Anyway, enough about me, I know you’re all here for more on our Event Pack!  

Last time out Trin took you through some of the more mechanical changes, such as the memory system and viewer, the loyalty traits and some of our childhood event changes. Today I’ll walk you all through some of the flavour-driven content you can expect to find in the Event Pack, though we’ll also look at a neat little system we’ve mentioned in passing before towards the end.  

We’ve been hard at work creating over 100 new standalone events for this pack, and at this point it probably behooves me to explain that when we say ‘over 100’ we mean something a little different than just counting out each individual event we’ve made. To avoid any grey areas, we count both big event chains and small, one-off events exactly the same. No matter if you’re counting a singular event or a behemoth 14-event long chain: as Gimli would put it, it still only counts as one. As such, whilst we’ve bandied around a figure of 100, you’ll all be getting quite a bit more than that!  

All of the new events pertain to the relationships between characters in some fashion, meaning that all relationships - from lieges to vassals, from friends to spouses, from lovers to foes to… lover-foes - have new events tied to them, to greater or lesser degrees. I’m going to take you through some of the joyful and jocular, the serious and the sad, and of course the weird and the wacky of this pack.  

Let’s begin by addressing an event or two that could bring your character happier times, shall we?  

### The Good​


You should always be able to rely on your friends to support you not only in good times, but also in bad. Moreover, a true friend is one who will have difficult talks with you because they truly care about your wellbeing. Perhaps even an intervention, should the actions you take to deal with stress so completely consume your life:  

![A friendly Intervention.png](https://forumcontent.paradoxplaza.com/public/861443/A friendly Intervention.png "A friendly Intervention.png")


*[picture of A Friendly Intervention]*  

Despite the name, it’s not just friends who come into the spotlight in this pack. Your family are an active part of your life at court. Your parents offer sage advice, your children chances to bond, and your siblings are solid confidants - when they’re not trying to take your throne for themselves, of course. Even your beloved darling spouse also has the opportunity to raise you up, praise you, and, er, ask if you’d maybe consider sponsoring his mum to make you a lovely set of jewellery:  

![Family Craft.png](https://forumcontent.paradoxplaza.com/public/861444/Family Craft.png "Family Craft.png")


*[picture of The Family Craft]*  

Still, trusting your mother-in-law could have its upsides. It might turn out the old girl is quite the metalsmith!  

![Inspiration Realised.png](https://forumcontent.paradoxplaza.com/public/861445/Inspiration Realised.png "Inspiration Realised.png")


*[picture of Inspiration Realised]*  

Even when you’re looking after your family and all is seemingly well, intrigue is never too far away. The demands of a multiple-spouse marriage becomes a little more unique in Friends & Foes, as now you might be getting a few eyebrow-raising requests:  

![Great Expectations.png](https://forumcontent.paradoxplaza.com/public/861446/Great Expectations.png "Great Expectations.png")


*[picture of Great Expectations event]*  

Every mother wants to see her son get ahead in life, so it’s no wonder Tamrust here is so eager to please. In my case, however, I’m more interested in getting a-head in a rather different way: seeing my rival Sholah get their comeuppance would be a mighty fine way to do a deal.  

![All Hail The High Chieftain.png](https://forumcontent.paradoxplaza.com/public/861447/All Hail The High Chieftain.png "All Hail The High Chieftain.png")


*[picture of All Hail The High Chieftain event]*  

Ah, Tamrust, you shouldn’t have!  

### The Sad​


In the game’s time period, as it is today, the death of a loved one can leave the bereaved with so many conflicting feelings. Regret over lost time together, sadness at the knowledge that the departed will no longer be around, perhaps even relief at their suffering finally ending.  

In one of our new events, a visit from one person to their friend’s deathbed can go a few different ways. Perhaps you are the one bedridden, simply waiting for death. What would you desire from your friend? Or maybe you are the one visiting them, your lifelong friend, with whom you have forged so many memories and shared so much of your life with. What would you do when faced with this scene?  

![A Friend till the End.png](https://forumcontent.paradoxplaza.com/public/861448/A Friend till the End.png "A Friend till the End.png")


*[picture of A Friend till the End]*  

The possibilities here are rather wide. That third option you see is somewhat randomised and based on the bedridden person’s personality. Sometimes you won’t have a third option at all. Sometimes, as you can see above, you may even have to do your beloved friend the ultimate favour. Sometimes, as seen below, you’ll come into possession of a small gift.  

![Receiving the Pendant.png](https://forumcontent.paradoxplaza.com/public/861450/Receiving the Pendant.png "Receiving the Pendant.png")


*[picture of receiving the pendant]*  

![Lavender Jade Pendant.png](https://forumcontent.paradoxplaza.com/public/861451/Lavender Jade Pendant.png "Lavender Jade Pendant.png")


*[picture of the pendant itself]*  

Whilst seeing your friend breathe their last is desperately sad, there’s also something to be said for the brutal moments when a sibling rivalry gets way out of hand. Ambition and envy drives the closest of brothers and sisters to do the most heinous of things.  

![Night Terrors.png](https://forumcontent.paradoxplaza.com/public/861452/Night Terrors.png "Night Terrors.png")


*[picture of Night Terrors event]*  

This rare event may fire if your sibling doesn’t like you, and happens to have a trait that might cause them to view you as dispensable in the pursuit of their wider ambitions. Of course, you’re not going down without a fight; the throne is yours and as the saying goes, might does indeed make right:  

![Night Terrors Denied Ambitions.png](https://forumcontent.paradoxplaza.com/public/861453/Night Terrors Denied Ambitions.png "Night Terrors Denied Ambitions.png")


*[picture of Night Terrors Denied Ambitions event]*  

The young king survives this particular attempt from their sibling, but their relationship is irreparably damaged. Suffice to say, however, much nastier outcomes could well have arisen. Luck and wits will save many a monarch, but sooner or later your wits fade and your luck runs thin…  

### The Zany​


Like the glorious sprinkles on this Medieval doughnut (which were actually a thing: there’s references in The Forme of Cury to honeyed fried dough ‘Cryspels’ which were essentially the precursors to modern doughnuts!) we of course have some of the slightly more unusual events that you can stumble across during your rule.  

The subject of this DLC made for fertile grounds for such events. Interpersonal relationships are at the heart of CK3, and how you interact with others depends often on whether they’re your foe or your friend. In order for you to have a friend, of course, you must first have a person to be friends with. I know, I know, it sounds obvious, but they do say the real miracle Jesus performed was having 12 close friends in his thirties. Well, that, and also the following:  

![The Face of Jesus.png](https://forumcontent.paradoxplaza.com/public/861454/The Face of Jesus.png "The Face of Jesus.png")


*[picture of The Face of Jesus event]*  

If you take your religious leader’s excitement and fervour at face value, you’ll not just acquire a friend, but also a Delicious Face of Jesus artifact:  

![Delicious Face of Jesus.png](https://forumcontent.paradoxplaza.com/public/861455/Delicious Face of Jesus.png "Delicious Face of Jesus.png")


*[picture of Delicious Face of Jesus]*  

Of course, if you dare to doubt their obviously-correct opinion on divinely-shaped confectionery, you’re dead certain to make a rival of them. Or, as you can see in the third option, there’s an even more dramatic decision to be made. What price do you put on friendship versus the chance to literally eat Jesus’ face?  

Mind you, there’s some things you can find that shouldn’t be eaten. Bog bodies are known worldwide, but are particularly prevalent in Northwestern Europe. Such findings continue to intrigue archeologists, but I suspect finding one would be rather more of an unpleasant surprise for your average Medieval child:  

![The Body in the Bog.png](https://forumcontent.paradoxplaza.com/public/861456/The Body in the Bog.png "The Body in the Bog.png")


*[picture of Bog Body event]*  

This event ties nicely in with the new memory system; sometimes if someone in your realm dies in that particular county, they have a chance of turning up here! Now I won’t spoil any particular outcomes to this small event chain, but naturally all is always exactly as it seems.  

You just found a body in a bog. These things do happen. It’s perfectly normal.  

### For a Feud Dollars More​


Petty rivalries are an inextricable part of any Crusader Kings game. I’ve been a CK player for years, and I know exactly what I - and all of you - get up to when someone wrongs you. After all, who amongst us has not exterminated an entire dynasty for the vicious crime of their grandfather once having accidentally tripped over your dog?  

![A Damnable House.png](https://forumcontent.paradoxplaza.com/public/861457/A Damnable House.png "A Damnable House.png")


*[picture of A Damnable House event]*  

Thankfully, you now have the opportunity to codify your hatred for those hated dog-trippers! House Feuds are a new system that can be triggered by a wide range of sources. It could be as simple as your House Head sharing a mutual dislike of each other with another House Head and those embers sputtering into the flames of true conflict. It could be as serious as a family member of your House being killed by a member of the other House, or as complicated as the two having competing Claims.  

These Feuds can be inherited between generations, ebbing and flowing, each party exacting a toll from the other. These squabbles can escalate to horrific ends if all parties continue to seek revenge upon the other, and only the actions of calm heads can end it; but even then, often only once the debt has been repaid or one family has suffered so horribly under the other that they will surely never recover.  

I was going to give you a runthrough of some of the 31 events (remember: for us, it still only counts as one!) that comprise House Feuds, but when I was playing around with Friends and Foes this last Sunday on a post-PDXCon rest day, I happened to hit upon a perfect mini-AAR to show you to illustrate exactly how these can generate organically. You join me on the steppes of modern-day Ukraine and Kazakhstan, where I am waging a war against a neighbour to expand my territory.  

*(A small note: I am playing with some custom gamerules including equal genders and majority-bisexual, hence why things might seem a little unusual with who is leading armies and the like. Or, if you’re one of those super cool and wonderfully attractive people who also play with those rules, high five, consider your ruleset officially dev-approved)*  

![Fallen Daughter.png](https://forumcontent.paradoxplaza.com/public/861458/Fallen Daughter.png "Fallen Daughter.png")


*[Picture of Fallen Daughter]*  

As battle concludes, it is with no small amount of grief that I receive the news that my knight, daughter and heir Princess Sarantay has fallen in battle at the hands of the vile and base Chieftain Malyy. And we know him to be vile and base, for who else but a true monster would snatch away my daughter’s life from the world so cruelly?  

I try to put it out of my head - as much as any parent can do so with the death of their beloved child - but the flames of hatred still lick balefully at my heart. During the day it is all I can think about, and at night dreams of vengeance and retaliation poison my mind. Try as I might, I can’t bring myself to move on and let Allah enact retribution: I must pursue this myself.  

![lure-of-vendetta-png.873969](https://forum.paradoxplaza.com/forum/attachments/lure-of-vendetta-png.873969/?hash=ba5083f8fa1fa38df17b6ee701087ff7 "")


*[Picture of House Feud 1]*  

![Brutal Feud.png](https://forumcontent.paradoxplaza.com/public/861461/Brutal Feud.png "Brutal Feud.png")


*[Picture of House Feud 2]*  

![Ongoing House Feud.png](https://forumcontent.paradoxplaza.com/public/861462/Ongoing House Feud.png "Ongoing House Feud.png")


*[Picture of House Feud 3]*  

Now, I won’t go too in-depth on what exactly transpired in the years this feud went on for. One such action involved seducing the enemy head of house’s wife - a fairly impressive feat, despite how sprightly I am at 68 years old - and revealing him for the cuckold he was. This disrespect was met with bared knives, and a minor member of my dynasty was struck down from the shadows.  

It was an escalation I would not - could not! - ignore. House Kurgani were all too ready to unsheathe blades, but they soon found themselves on the wrong end of them. Three murders, one after the other, left them without the flower of their youth. The feud was clearly in our favour, the rival house a shadow of what they once were, and it even left me considering whether it was worth continuing. After all, Malyy was a mere chieftain, and I a mighty Khan. Surely it was time to let bygones be bygones?  

![Outclassed Adversaries.png](https://forumcontent.paradoxplaza.com/public/861463/Outclassed Adversaries.png "Outclassed Adversaries.png")


*[Picture of House Feud 4]*  

Yet every time I considered it, all I could think of in my mind’s eye was my precious daughter. The feud would continue until the damnable Malyy was dead. I called my trustiest cutthroat and sent him on one final mission…  

It is strange how fate works. The hired knife was drawing closer and closer still to Malyy, aided by no less than his own wife - who it seemed had grown rather fond of me, not that that’s surprising - but it appeared someone else had got there first. Perhaps he had many enemies. Perhaps, even, a member of my own house had enacted their own revenge. Either way, he now lies in the cold ground.  

![Life in Color.png](https://forumcontent.paradoxplaza.com/public/861464/Life in Color.png "Life in Color.png")


*[Picture of House Feud 5]  

(Another note: This event isn’t actually part of the House Feud ones, but instead is part of a reworked couple of events when Best Friends or Nemeses die and can happen to anyone lucky enough to have their worst antagonist die on them. Suffice to say, that Vengeful option there does some fun stuff…)*  

The blood has been spilt, the eye has been taken for the eye. There is no longer any reason to prolong this blood feud. House Dulo has conclusively proven the dominance of our bloodline and emerges triumphant from the crucible of intra-house conflict.  

![The Next Enemy.png](https://forumcontent.paradoxplaza.com/public/861465/The Next Enemy.png "The Next Enemy.png")


*[Picture of House Feud 6]*  

I’ll leave you to discover most of the rest of the peaks and troughs of the cycle of ceaseless vengeance that signify House Feuds, but I do want to leave on one particularly interesting note. Malyy’s son, Tyueykezhut, was grateful that the bloodshed had ended, even if House Kurgani were crushed underneath our boot heel. He didn’t let go of the past, though, and the fire that once consumed my heart no doubt now consumes his; a grim reminder of how he spent his childhood raised to hate anyone who bears the name Dulo. And so the flames of open conflict die away to smouldering embers, all too ready for the right person to come along and nurse them back into a roaring crescendo once more…  

![Gained Nemesis.png](https://forumcontent.paradoxplaza.com/public/861466/Gained Nemesis.png "Gained Nemesis.png")


*[Picture of House Feud 7]*  

That will be all from me for today! Thank you very much for reading this, my very first dev diary! Friends & Foes releases this week on the 8th of September, and I hope you enjoy your time with it.  

![Nick-name.png](https://forumcontent.paradoxplaza.com/public/861414/Nick-name.png "Nick-name.png")

 

#### Attachments

- [![Lavender Jade Pendant.png](https://forumcontent.paradoxplaza.com/thumbnail/public/861449/Lavender Jade Pendant.png)](https://forum.paradoxplaza.com/forum/attachments/lavender-jade-pendant-png.873959/)
  
  Lavender Jade Pendant.png
  203,3 KB

 · Views: 0

- [![Lure of Vendetta.png](https://forumcontent.paradoxplaza.com/thumbnail/public/861459/Lure of Vendetta.png)](https://forum.paradoxplaza.com/forum/attachments/lure-of-vendetta-png.873969/)
  
  Lure of Vendetta.png
  796,4 KB

 · Views: 0

- [![Ongoing House Feud.png](https://forumcontent.paradoxplaza.com/thumbnail/public/861460/Ongoing House Feud.png)](https://forum.paradoxplaza.com/forum/attachments/ongoing-house-feud-png.873970/)
  
  Ongoing House Feud.png
  118,6 KB

 · Views: 0

<!-- artifact:reactions:start -->
- 113 Like
- 25 Love
- 14 (unlabeled — rendered as base64 data URI)
- 13 (unlabeled — rendered as base64 data URI)
- 8 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDS_Noodle](https://forum.paradoxplaza.com/forum/members/pds_noodle.1394234/)**
Role: CKIII Designer
Badges: 8
Messages: 217
Reaction score: 4,857
<!-- artifact:op_signature:end -->
