---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1576961/"
forum_thread_id: 1576961
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 122
title: "Dev Diary #122: Regencies and Elegance of the Empire"
dd_date: 2023-04-04
author_handle: Paradoksalny Kierownik
expansion: Tours and Tournaments
patch: Patch 1.9
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 8324
inline_image_count: 71
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1576961'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2277.jpg?1680617327
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_142_to_144
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_879_to_882
    action: preserved_and_flagged
    counts:
      Love: 225
      Like: 107
      (unlabeled — rendered as base64 data URI): 3
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_890_to_992
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_993_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2277.jpg?1680617327)
<!-- artifact:thread_banner:end -->

# Dev Diary #122: Regencies and Elegance of the Empire

<!-- artifact:thread_metadata:start -->
- Thread starter [Paradoksalny Kierownik](https://forum.paradoxplaza.com/forum/members/paradoksalny-kierownik.1725641/)
- Start date [Apr 4, 2023](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-122-regencies-and-elegance-of-the-empire.1576961/)
<!-- artifact:thread_metadata:end -->

Welcome, comrades! First up today we’ll be talking about a subject _very_ dear to my heart, and that’s regencies — what happens when you can’t effectively rule your realm, either because you’re out travelling or because you are a small baby with lacking social skills.  

## Design Ethos​

First up, I’d like to go over a little of what was in our minds when we were designing this system, what we were trying to achieve, and what parameters we set ourselves. If you’re after strict in-game stuff, you can spin on to the next section.  

A regent, or an expected regent, was a figure of huge importance and subject to plenty of political intrigue — not to mention being one of the more prominent ways for unlanded women to exert soft power on behalf of family members. Their job was to shepherd the realm when the actual ruler was otherwise indisposed, giving them a tremendous amount of power and authority but a fairly precarious base for such.  

Capturing the full scope and scale of the power wielded by someone essentially appointed as a stand-in for the liege was a big ask, and something we tried to frame as about providing interesting obstacles to overcome whilst trying to model some of the importance attached to the position.  

At the same time, this expansion’s shining stars are activities, so we needed regencies to be interesting and engaging _without_ making the player afraid to ever leave home for fear of a coup, or distracting too much from whatever urgent business called them away from their realm to begin with. Unless, of course, they’re a child or incapable, in which case… yeah, that needs to be a bit more important (and, perhaps, threatening).  

From the regent’s POV, we wanted to give you more opportunity to use and abuse your power. There’s a few core player fantasies we tried to keep in mind here, giving each mechanics and a chance to shine:  


- The scheming regent, greedy for power.
- The loyal regent, serving the throne as best they can.
- The laissez faire regent, skimming off the top but not too much.
So those were the rough goals we set ourselves. Regencies needed to be fun for the regent, offering plenty of interactivity and options on how to play, interesting for the liege without being too punishing or distracting most of the time, and allow escalation to more serious levels when a regent is given time to flourish and solidify their power.  

![diarchies_001.PNG](https://forumcontent.paradoxplaza.com/public/951492/diarchies_001.PNG "diarchies_001.PNG")



### What is a Regency?​

Simply put, when a character needs help to manage the day-to-day running of their realm, they get a regent.  

Historically, this happened for all kinds of reasons — maybe the king was off on pilgrimage to the Holy Land, maybe they were imprisoned far from home, maybe they were too young or ill to deal with all the petty tasks and vigorous travails entailed by ruling a realm.  

A regent was the go-to person for questions that would usually go to a healthy, adult ruler. This position inherently gave them access to no small amount of the liege’s power: when the regent spoke, they could speak with their liege’s authority meaning that, de facto, many regencies amounted to a degree of power sharing between the two.  

The thing is, this is sort of an unstable arrangement. Monarchic power does not like being shared like this, especially in such an awkward, unofficial fashion. Generally, a regency wouldn’t last long enough for this to be much of a problem, but when they did… well, no one enjoys quite as excellent an opportunity to slowly take control of an entire realm as someone who already nominally controls it.  

### Swinging the Scales of Power​

In-game, we represent this tug-of-war between regent and liege with the Scales of Power.  

![diarchies_002.PNG](https://forumcontent.paradoxplaza.com/public/951493/diarchies_002.PNG "diarchies_002.PNG")



The lower this bar, the more titular the regent is — they’re nominally the liege’s second in command, but in practice, they’re more or less a figurehead able to do little more than their basic job.  

The higher this bar, the more power the regent actually has — they’re not just a reference point for the realm, they’re considered an increasingly-legitimate source of authority in and of themselves. A dangerous position for the liege to get into…  

Along the bar we have different levels — each level unlocks different interactions or effects. Generally, as the bar increases, the regent gets more abilities that allow them to imitate powers their liege has (we’ll talk more about those in a bit), whilst adding prestige costs to actions that would otherwise be free — representing the political divisions in the realm and the liege needing to spend political capital in order to just administer their lands.  

![diarchies_003.PNG](https://forumcontent.paradoxplaza.com/public/951494/diarchies_003.PNG "diarchies_003.PNG")



Most regents will thus want to keep this bar as high as possible, whilst lieges will want it nice and low.  

In order to actually affect it, both liege and regent have an interaction allowing them to trade various currencies (gold, prestige, piety) for a bit more authority in the realm, using the influence they’ve accrued elsewhere to sway people to their side of the aisle.  

![diarchies_004.PNG](https://forumcontent.paradoxplaza.com/public/951495/diarchies_004.PNG "diarchies_004.PNG")



The Scales of Power always have a natural resting point that they’ll slowly drift towards over time, so things’ll usually trend one way or else equalise, but where this resting point lies is situational: for instance, if the liege is a recently-grown adult trying to shake off an overbearing regent from their childhood, then the resting point will strongly favour the liege.  

### Mandates & Strife​

For the liege, that covers things. Their best ways to affect the Scales are to influence them directly and to put themselves in a position where a regency would no longer be necessary.  

For their regent, though, there’s a few more options…  


![diarchies_005.PNG](https://forumcontent.paradoxplaza.com/public/951496/diarchies_005.PNG "diarchies_005.PNG")



Mandates are generalised tasks the liege can set for their regent. Think of them as a bit like council tasks — someone has a job, you tell them what you’d like to focus on in their job, but then how they do that is at their discretion.  

On the regent’s end, you’ll receive events related to your mandate, generally giving you the option to serve the realm dutifully, split a benefit with your liege (or even steal it entirely), or bunk off and ignore the important job you were given. Particular skills and traits play into both how good any given character is at this, and how their AI will react to events.  

Splitting a benefit gives you an appropriate short term boost, bunking off means you don’t have to worry about potential costs or challenges, but serving dutifully reinforces the connection between you and the realm in the minds of your fellow vassals _generally_ at some personal cost to yourself. The upside is that this, in turn, swings the Scales of Power in your direction a little bit more.  

This means that even a self-serving regent is of some use to their liege — they need to do the job well to increase their own power, after all. At least, up to a point.  

Fulfilling a mandate isn’t without its perils, though, as using your liege’s power (even on their behalf) when you’re _not_ the liege can cause a lot of friction with your fellow vassals. Ultimately, to them, you might be regent but your job isn’t to over-step and boss them around, it’s to mind things quietly and leave them alone till the liege can resume control.  

Thus, strife opinion.  

![diarchies_006.PNG](https://forumcontent.paradoxplaza.com/public/951500/diarchies_006.PNG "diarchies_006.PNG")




Strife operates a bit like tyranny, but, per the image, affects your fellow vassals’ opinion of you rather than your subjects. Whenever a regent abuses their position (or even _uses_ their position), they generate strife.  

Unlike tyranny, though, strife doesn’t go hand-in-hand with generating a huge amount of fear in people. You might hate a tyrannical liege but be too scared to do anything to them, but if something were to _happen_ to an unpopular regent, well, any other vassal could be up next, right?  

To that end, strife affects how likely other vassals are to start or join schemes against a character more than many types of opinion. A regent who acts too much has a lot of unique opportunities, but may test the patience of their colleagues.  

### A Throne Fit for Two​

Most commonly, you’ll enter a regency when you leave your portion of the realm for some reason. Maybe it’s a feast in a neighbouring realm, maybe you’ve been kidnapped by a foreign power. “Your portion” is defined as your domain and the lands of your vassals: so if the King of Bavaria goes to a feast in Bohemia, that’d still trigger a regency, but if the Holy Roman Emperor does, it wouldn’t.  

These regencies aren’t too dramatic and don’t offer the regent too much opportunity for shenanigans — sort of akin to house-sitting. The regent’s job is to keep an eye on things, proverbially watering the plants, feed the pets (see: vassals), etc, till their liege returns in short order.  

The regent can try their hand at embezzlement, maybe imprison some rival vassals that annoy them, or justify some trumped-up claims to a few titles, depending on how much they can swing the Scales in their favour. As soon as the liege is back in their realm, they can dismiss the regent at any time (and it’ll generally even happen automatically).  

Thus the liege knows that they’ll be able to spend some time away from home without the entire realm catching fire immediately, and the regent gets a bit of meaningful agency. A nice, even trade.  

But what if things don’t shake out like that? What if the liege is waylaid on the route home, or some foreign power refuses to let them return to their realm? If they take too long, they give the regent time to grow, to not just cement their power, but expand it. If this persists for too long, and the Scales of Power get high enough, the regent can expand their power significantly: they can entrench themselves.  

![diarchies_007.PNG](https://forumcontent.paradoxplaza.com/public/951502/diarchies_007.PNG "diarchies_007.PNG")



### Entrenched Regencies​

Once a regent entrenches, they, the liege, and everyone else have to recognise that they’ve got a lot of power at their fingertips. The Scales shift back down to around the mid-point, and in exchange, the regent unlocks a whole raft of potential new abilities letting them act almost as though they are the liege (revoking titles from fellow vassals, retracting vassals, imprisoning people they don’t have direct control over, and so on), whilst the liege starts paying prestige costs on some things that were formerly free.  

Were you wondering why I didn’t mention children or incapable characters earlier when talking about how you enter a regency? That’s because, when a regent is called to serve for such characters, everyone knows that they’re intended to be in it for the long haul. When a child inherits, or a character becomes incapable, they _immediately_ enter an entrenched regency.  

If an ordinary regency is akin to house-sitting, then an entrenched regency is more like having a housemate you’re having problems with. You’re both sharing the same space, and even if you’d otherwise get on, them being constantly around can really grate on the nerves. Worryingly for most lieges, an entrenched regent cannot be as easily unilaterally dismissed — they’re going to have to work for it.  

### Borrowed Powers & You​

Alright, so you’ve got a regent. Maybe they’re entrenched, maybe they’re not. Either way, as they continue to swing the Scales of Power in their favour, they’ll unlock more and more interactions. Each unlock is about either replicating powers usually only a liege would have, exploiting the regent’s dual-role as vassal and executor of their liege’s authority, or exploiting the trust placed in them by their liege.  

We loosely group these interactions together as Borrowed Powers, abilities contingent on the regent’s role as an actor on their liege’s behalf.  

These interactions can model relatively minor or benign forms of corruption, or some things as severe as title revocation from co-vassals. That… might sound like it could be a smidgeon problematic for their liege, depending on who their regent tries to have a go at.  

![diarchies_008.PNG](https://forumcontent.paradoxplaza.com/public/951503/diarchies_008.PNG "diarchies_008.PNG")



Well, fortunately for the liege, because they are the ultimate source of authority here, many of the more serious interactions still have to go through them first. This allows them a chance to veto serious power abuses by their regent — _if_ the liege has the prestige to spare.  

If both the liege and the recipient accept, then the interaction goes through as usual. If the liege accepts but the recipient refuses, then the regent generally gets a choice on whether to back their claim in war or back-down whilst generating a criminal reason on the recipient for both them and the liege, their punishment for disobeying the laws of the land. This lets even a landless regent cause some trouble in the realm.  

The intention here is to give lieges some agency over what their regent can do, without letting them hard-block everything, whilst requiring vassals to make a harder choice on whether to give in to this type of political blackmail or stand strong and hope. In politics, as in war, you have to pick your battles.  

Ok, so the regent has access to new character interactions for the duration of their stay, but what specifically can they actually do?  

## Core Loop​

### Regent Revoke Title​

The most important tool in the arsenal of any regent is the ability to revoke titles from co-vassals. Naturally, the liege gets a veto, but an important additional hurdle for the regent here is that the regent also requires a claim in order to even select a target.  

![diarchies_009.PNG](https://forumcontent.paradoxplaza.com/public/951507/diarchies_009.PNG "diarchies_009.PNG")



Regent Revoke Title is only available around the mid-point of the Scales of Power in an entrenched regency, so there’s no need to worry about the realm’s boundaries getting redrawn every time you pop over the border for a feast.  

The intention here is to empower regents to act on dynastic claims and so gerrymander the realm a bit according to their liking, but only when appropriate. And, of course, if a regent is landless and wants to move up in the world…  

### Legal Meddling​

That said, when you’re both one of the realm’s great magnates _and_ its temporary head (with a convenient scapegoat above you you can vaguely pin the blame on), there’s a lot you can do to forge claims a little faster than usual.  

Enter, Legal Meddling.  

![diarchies_010.PNG](https://forumcontent.paradoxplaza.com/public/951508/diarchies_010.PNG "diarchies_010.PNG")



![diarchies_011.PNG](https://forumcontent.paradoxplaza.com/public/951509/diarchies_011.PNG "diarchies_011.PNG")



With this interaction, regents can either use their learning or spend prestige (again, leveraging that political capital - regentry is power-hungry work) in order to generate claims on the counties of their fellow vassals.  

Using learning is free, whilst prestige can be spent in two increments. A moderate amount for a straight 50:50 shot of forging the claim or failing, or a larger amount to simply automatically obtain a claim.  

![diarchies_012.PNG](https://forumcontent.paradoxplaza.com/public/951511/diarchies_012.PNG "diarchies_012.PNG")



This makes a regent with a lot of prestige to spare something of a potential problem. If they have the power, they’ll try to grab what they’re entitled to, and if they’re not entitled to anything, they’ll try to _make_ those entitlements.  

### Regent Retract Vassal​

When the Scales tip a bit further towards them, regents can even try to retract whole vassals, providing said-vassals would be de jure theirs. In kingdoms, at most, this likely means shuffling a few counts around. In empires with king-tier regents, though, this can mean trying to grab entire duchies that should, rightfully, be theirs.  

![diarchies_013.PNG](https://forumcontent.paradoxplaza.com/public/951512/diarchies_013.PNG "diarchies_013.PNG")



## Bells’n’Whistles​

### Regent Imprison​

Alongside the main Revoke-Meddle-Retract cycle, regents also have sundry other powers to make use of. One of these is the ability to imprison characters in their liege’s realm: this includes fellow vassals, but also the courtiers of those vassals, guests passing through, etc.  

![diarchies_014.PNG](https://forumcontent.paradoxplaza.com/public/951514/diarchies_014.PNG "diarchies_014.PNG")



Perfect for when someone is so, so close to being within your grasp. And if they’re landed and refuse, since you’d imprison them in the resulting war anyway, you can recoup some of your war costs as reparations.  

![diarchies_015.PNG](https://forumcontent.paradoxplaza.com/public/951515/diarchies_015.PNG "diarchies_015.PNG")



### Shift Privileges​

This interaction consists of a regent selling knowingly-duplicated certificates, titles, monopolies, and other administrative bric-a-brac to the subjects of a fellow vassal. A liege, who needs to maintain their status as lord and arbitrator, couldn’t get away with such tricks, but a regent knows that they won’t be around forever and doesn’t need to keep hold of such a facade.  

As with Legal Meddling, the regent can spend prestige to gamble or win, or test a skill to do it for free (in this case, diplomacy). The regent gets a lump sum of gold and some garnered strife. The unfortunate target vassal gets a powerful negative county modifier to pair neatly with their newfound grudge.  

![diarchies_016.PNG](https://forumcontent.paradoxplaza.com/public/951516/diarchies_016.PNG "diarchies_016.PNG")



### Syphon Treasury​

One thing almost any regent is capable of, given their access to their liege’s authority, is a little bit of casual embezzlement from the royal treasury. The funds are, after all, merely resting in their account.  

Embezzlement takes the form of a stewardship challenge, with the difficulty going up the more you try to steal at any one time. This type of white tunic crime is a bit subtler than merely stealing bags of silver, though, so they don’t _directly_ take the money from their liege’s treasury — their master would surely notice that.  

Instead, depending on the regent’s stewardship, they’ll steal increasingly difficult-to-track intangibles from their liege’s realm.  

Characters with low stewardship will apply visible negative county modifiers to their liege’s domain, something a canny player can easily notice if they’re paying attention. Characters with medium stewardship syphon lots of control from one county in their liege’s domain, whilst those with high stewardship spread the amount out over a few counties to be slightly harder to catch, and if the embezzling regent has excellent stewardship, then they’ll steal small amounts of development progress from multiple counties instead.  

Naturally, the more a character tries to steal, the harder it gets and the worse the modifiers applied to their poor, trusting liege.  

![diarchies_017.PNG](https://forumcontent.paradoxplaza.com/public/951521/diarchies_017.PNG "diarchies_017.PNG")



Once a character has embezzled, they generate an embezzlement secret. Each embezzlement secret tracks how much that character has embezzled from the target in total. Small amounts can be blackmailed for a hook, but very high amounts may result in a strong hook.  

But, you may well be asking, why? What’s the worst that can happen if you’re discovered embezzling?  

Well, unlike many secrets, you can definitely put a price on the harm caused by embezzlement. A handy, convenient price. So, if a liege catches their regent stealing from them, they can demand restitution.  

In full.  

![diarchies_018.PNG](https://forumcontent.paradoxplaza.com/public/951522/diarchies_018.PNG "diarchies_018.PNG")



Maybe there’s been a war, a rebellion, or just some preemptive partition, though. Maybe the embezzler is under a new liege, and thinks they’re safe from the old one. Well, regrettably, a nice lump sum of reparations money can be a _very_ enticing offer to split with a new liege.  

![diarchies_0018_2.PNG](https://forumcontent.paradoxplaza.com/public/951523/diarchies_0018_2.PNG "diarchies_0018_2.PNG")



Of course, an independent embezzler has no one to fear. If they can manage independence.  

### Subsidise Liege Authority​

Borrowed Powers are all about using a liege’s authority to benefit the regent — that is, assuming the liege actually has any authority. After all, if the king can’t revoke a title, how can his regent hope to?  

Regents desperate for power can thus offer to help subsidise their liege’s efforts at centralisation, paying prestige to help them increase their Crown Authority whilst taking the social hit of being the realm’s stooge.  

![diarchies_019.PNG](https://forumcontent.paradoxplaza.com/public/951524/diarchies_019.PNG "diarchies_019.PNG")



![diarchies_020.PNG](https://forumcontent.paradoxplaza.com/public/951525/diarchies_020.PNG "diarchies_020.PNG")



### Own Vassal Contract​

Last but by no means least, any regent with a shred of dignity to their name has some degree of power over their own vassal contract, making countersigning a few extra changes a simple matter.  

![diarchies_021.PNG](https://forumcontent.paradoxplaza.com/public/951526/diarchies_021.PNG "diarchies_021.PNG")




### Ending Regencies​

All good things must come to an end, and so too it is with regencies.  

Most regencies are nice’n’easy to remove. Providing you’re an adult within your own realm not currently travelling, you can remove them at any time for free. When you return from travel, they’ll generally be dismissed automatically, even, though there’s still a manual dismissal button for things like being released from a foreign prison.  

Entrenched regencies, though, have had more time to coil themselves around the levers of power. Administrators, clerics, staff in the royal household, the nobility — some from all of these classes support the regent’s access to executive authority, and removing them is not quite as simple as writing a thank you letter.  

At the uppermost levels of the Scales of Power, the regent is so influential that their liege can’t even broach the subject seriously, and drastic actions may have to be taken to regain control.  

![diarchies_022.PNG](https://forumcontent.paradoxplaza.com/public/951528/diarchies_022.PNG "diarchies_022.PNG")



Below this, the liege can attempt to offer their regent various gifts to speed their parting. Depending on the regent, they may prefer different types of gift, or even be happy with none at all, but if they decline, they’re merely delaying the inevitable. The mere act of a liege trying to enforce their authority on a realm is deeply corrosive to a regent’s control, and will start to swing the Scales against them.  

![diarchies_023.PNG](https://forumcontent.paradoxplaza.com/public/951529/diarchies_023.PNG "diarchies_023.PNG")



In turn, if the regent isn’t careful, eventually they’ll completely lose the ability to resist and risk getting nothing.  

![diarchies_024.PNG](https://forumcontent.paradoxplaza.com/public/951531/diarchies_024.PNG "diarchies_024.PNG")



![diarchies_025.PNG](https://forumcontent.paradoxplaza.com/public/951532/diarchies_025.PNG "diarchies_025.PNG")




Regencies give a lot of power to the regent, but in the end, no matter how they try to cling on, the liege will always win. Unless...  

## Coups​

The threat of a coup by your regent is, in essence, something you’ll always see coming. You can see who your regent is, you can see what they think about you (though we’ll get to regent loyalty in juuuuuust another couple of sections), you can see them working their way up the Scales of Power towards the point where they can give this a try.  

It’s less of a sudden shock and more about rising dread.  

### Anatomy of a Coup​

To start preparing a coup, the regent will need to _almost_ max out their Scales of Power. This unlocks access to all the resulting content, giving the liege a solid way to fight back against even a very incipient coup. Unfortunately for the liege, ticking below this value doesn’t invalidate the prep-work a regent needs to do to proceed, so as long as the regent is persistent enough, they’ll find a way.  

![diarchies_026.PNG](https://forumcontent.paradoxplaza.com/public/951533/diarchies_026.PNG "diarchies_026.PNG")




Once the final Scale node is hit, the regent gains access to a character interaction and a decision. The character interaction allows them to contact powerful vassals around the realm, offering various promises in return for support. A simple majority of the realm’s powerful vassals must support the coup for it to proceed any further.  

![diarchies_027.PNG](https://forumcontent.paradoxplaza.com/public/951534/diarchies_027.PNG "diarchies_027.PNG")



AI regents have a slightly more streamlined flow for this section. The requirements are broadly similar, but sanded back a little and forced to be a bit more active than they’d usually be, so that they actually pull off the odd coup without needing to manage human-tier planning.  

Once the conspirators are gathered, the decision comes into play.  

![diarchies_028.PNG](https://forumcontent.paradoxplaza.com/public/951535/diarchies_028.PNG "diarchies_028.PNG")



![diarchies_029.PNG](https://forumcontent.paradoxplaza.com/public/951536/diarchies_029.PNG "diarchies_029.PNG")



![diarchies_030.PNG](https://forumcontent.paradoxplaza.com/public/951537/diarchies_030.PNG "diarchies_030.PNG")



With these requirements fulfilled, the regent selects how they want to frame their coup: one focusing on diplomacy, intrigue, or prowess. The skill they choose reflects the skill duel that their liege must reply to, and which (if any) councillor they can call on to defend them. Assuming, of course, that said-councillor isn’t in the conspiracy too.  

![diarchies_031.PNG](https://forumcontent.paradoxplaza.com/public/951538/diarchies_031.PNG "diarchies_031.PNG")



If the liege gives in, then their life and freedom are assured, though their realm is forefeit. If they choose to challenge their traitorous regent, depending on the framing, they might be imprisoned or killed on loss, but may also fend off the conspirators. If a suitable councillor or court position holder is available, then they can be called in to act as a proxy, taking the conspirators on in the liege’s stead.  

Needless to say, failure for the regent means certain imprisonment at best and a quick traitor’s death at worst.  

![diarchies_032.PNG](https://forumcontent.paradoxplaza.com/public/951539/diarchies_032.PNG "diarchies_032.PNG")



For regents, success means a massive victory. After all, coups take a lot of investment and risk to pay off, and need rewards suitably larger than what can be done in a simple, cheap war. The regent takes every top-tier title their former liege possessed, the realm’s capital and capital duchy (if applicable), and, if the deposed liege was an emperor, the usurper also takes the kingdom title the liege held with the most de facto land in the realm (e.g., in the Holy Roman Empire, that’d be Germany).  

The price for this, other than any blood on their hands, is the cost of their promises to their co-conspirators and a rather high chance of an unpleasant nickname. A worthwhile trade indeed.  

![diarchies_033.PNG](https://forumcontent.paradoxplaza.com/public/951540/diarchies_033.PNG "diarchies_033.PNG")



### Nitty-Gritty​

Alright, let’s go over a few of the remaining systems I’m sure some of you have been champing at the bit to talk about since the first screenshot in the DD.  

### Loyalty​

Rather than just checking their opinion of their liege, regents have a special loyalty value, affected by a whole range of factors, with three bands to it. Traits, relationships, cultural traditions, opinion, and even certain court positions can all play into this.  

Regents with high loyalty are considered selfless: they’ll select mandate event options that benefit their liege, mostly refrain from using their Borrowed Powers, and are much more willing to give up power when asked to even in entrenched regencies. They’ll also generally not swing the Scales very much, if at all.  

![diarchies_034.PNG](https://forumcontent.paradoxplaza.com/public/951541/diarchies_034.PNG "diarchies_034.PNG")



Regents with low loyalty are listed as self-interested: these characters aren’t _necessarily_ hostile to their liege, they may even quite like them, but they want power and the benefits of power and are willing to go to some lengths to get it.  

Self-interested regents will use their Borrowed Powers liberally, swing the Scales whenever they can, resist attempts to dismiss them, and select beneficial options for the liege in mandate events not because they want to help them, but because it swings the Scales towards them.  

Self-interested regents are the only regents who will ever seriously contemplate a coup.  

![diarchies_035.PNG](https://forumcontent.paradoxplaza.com/public/951542/diarchies_035.PNG "diarchies_035.PNG")



Finally, those regents in the middle are considered situational. They likely enjoy their access to power, but aren’t committed to taking advantage of it at any cost. Situational characters use Borrowed Powers on occasion, sometimes swing the Scales, and will generally nab benefits for themselves during mandate events.  

## Succession​

Unlike titles, regents don’t really have a clear line of succession, at least not as such. Like loyalty, a range of factors go into determining who the realm expects the next regent to be, but, whereas loyalty generally takes into account the personal aspects of a character and their relationship to their liege, succession calculates a sort of rough social proximity.  

Things like sharing faith and culture give a little bump, as does being a powerful vassal or a councillor. Family, especially close family, will generally dominate the top rankings, though lieges with royal courts also give significant weighting to things like having a good skill related to the court type or speaking the court language effectively, and characters who can’t speak their liege’s main tongue can expect to take a significant dip.  

![diarchies_036.PNG](https://forumcontent.paradoxplaza.com/public/951544/diarchies_036.PNG "diarchies_036.PNG")



Whoever has the highest score takes the role of regent when the time comes.  

### Designation​

That said, the title of regent isn’t a true _title_ per se, it’s an office, and one to whom a liege can technically appoint anyone they like. Designating a future regent is as simple as using an interaction from the power sharing window.  

Of course, people higher up the rankings won’t exactly be happy about this…  

![diarchies_037.PNG](https://forumcontent.paradoxplaza.com/public/951545/diarchies_037.PNG "diarchies_037.PNG")



… and maybe your lowborn mate Geoff of Monmouth you met on tour _will_ be loyal to a fault, but he’s a bit coarse and not everyone in the realm takes kindly to that…  

![diarchies_038.PNG](https://forumcontent.paradoxplaza.com/public/951546/diarchies_038.PNG "diarchies_038.PNG")



… or even your bastard half-brother, who’s certainly better but not exactly the right stuff.  


![diarchies_039.PNG](https://forumcontent.paradoxplaza.com/public/951548/diarchies_039.PNG "diarchies_039.PNG")



In addition to securing the throne for yourself, though, there’s one other major reason you might want to designate an official future regent: succession. If you die with an underage heir and a loyal designated regent, your heir will receive a strong hook on them (expiring on their 21st birthday) that compels the regent to remain loyal. For your sakes. It was, after all, your dying wish.  

![diarchies_040.PNG](https://forumcontent.paradoxplaza.com/public/951549/diarchies_040.PNG "diarchies_040.PNG")



## Becoming Regent as a Vassal​

Humble vassals can also proactively seek future status as regent - in addition to actively working for it by bettering their succession score (whether that be through murder or an intense regime of linguistics), they can directly ask the liege to nominate them officially via interaction.  

![diarchies_041.PNG](https://forumcontent.paradoxplaza.com/public/951551/diarchies_041.PNG "diarchies_041.PNG")



Sadly for vassals everywhere, the liege can’t designate a new regent whilst the old one is still in power, and thus during an active regency they may have to take matters into their own hands. Fast-moving and very risky, the Overthrow Regent scheme allows characters to attempt to stage an altered kidnapping, effectively couping the regent and installing themselves in their stead.  

Failure naturally invites imprisonment, but even in success, this is an overturning of their liege’s laws, and is still a crime. Whether it’s one the liege feels like enforcing likely rests on the relationship between the liege and their new would-be regent.  

![diarchies_042.PNG](https://forumcontent.paradoxplaza.com/public/951552/diarchies_042.PNG "diarchies_042.PNG")




### Power Sharing Modifiers​

Regencies also provide some slight modifiers to both parties: generally speaking, regents take more stress due to the extra job (including taking more when entrenched), whilst lieges gain a bit of extra stress loss in unentrenched regencies due to being away from the hustle-and-bustle of rule for a bit.  

Probably more interestingly to many of you, inside entrenched regencies, lieges gain some extra domain cap depending on their regent’s stewardship. If you plan forward, this lets you account for lost stewardship on future children or should you get conked on the noggin at a tournament, smoothing out some of those transitions in rule. Providing, of course, that your regent still likes you well enough not to get ideas when called to serve…  

### Modding Info & Behind the Scenes Systems​

Maybe you’re not just here for the gameplay, though. I’m sure some of you reading either work on or play total conversions, overhauls, or expanded content mods, and perhaps you’re wondering how the hell these mechanics’ll map onto your preferred fantasy/post-apocalyptic/science fiction/specific area setting?  

Welp, good news for you. Remember when I said this dev diary was about regencies? _*I lied*_. This dev diary is actually about _diarchies_!  

A diarchy is a system in which two people share power between them (think: monarchy, one ruler, diarchy, two rulers), and it’s the term for the script system we built regencies into. We didn’t just build a mechanic that could only reflect the role and responsibilities of feudal regents, we built an underlying system allowing you to script & tailor your own diarchies for your own settings.  

### Diarchies & Scales of Power Parameters​

In vanilla, there are presently two types of diarchy — regencies and entrenched regencies. These are held entirely in script, and thus can be modified, tweaked, or reworked wholesale (though code does require something called “regency” to refer to). The only major restriction is that you can only have one diarch at a time — you might be eligible for different types of diarchy and diarchies can be made to transform into different types, but you can’t have a regent and another type of diarch at the same time.  

Because the nature, start, and end conditions of diarchies are all scripted, it is entirely supported to add new types of diarchy. They’re as moddable as cultures, faiths, or governments. I certainly know there’s some… natural extensions of the system that I’ve got my eye on adding to vanilla in the future.  

The Scales of Power themselves take scriptable parameters for each node in much the same way as cultural traditions and faith tenets, meaning that new powers can be created and hooked in with extreme ease. Since they’re parameters, they can also be shared between diarchies easily.  

![diarchies_043.PNG](https://forumcontent.paradoxplaza.com/public/951553/diarchies_043.PNG "diarchies_043.PNG")



### Loyalty, Succession, & Balancing Point​

You know what I love? Script values. They’re fun, they’re powerful, and they’re easy to use.  

So easy in fact that we’re using them directly to govern diarch loyalty, diarch succession, and the balancing point for different diarchies. This means you can effortlessly sync with (or tweak, or add to without otherwise altering) vanilla or use your own values hygienically for any/all of these.  

Determining what a character’s loyalty would be, where they place in the succession, or changing where the Scales of Power balance out according to actual circumstances are all easy, no-fuss, no-muss operations.  

### Incapability​

Perhaps you like incapability, but it’s not super thematic for your mod — maybe someone’s actually in a temporary coma, or they’ve got a specific fantastical disease, or you just really want syphilis to take you down an extra peg. You want a diarchy to pop up there, but you’re dreading the thought of winding through all the vanilla use-cases for “has_trait = incapable”.  

Never fear, it’s been accounted for. Rather than referring specifically to the incapable trait, vanilla now uses an “is_incapable = yes” parameter, something set on the incapable trait but which can be added to _any_ trait, making hooking your traits into the system deliciously easy.  

### Conclusion​

Finally, re![:D](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Big Grin    :D")D #116, we had some good guesses, but the main shoutout has to go to  
[@TheGib770](https://forum.paradoxplaza.com/forum/members/963270/) for getting _all_ of the possible historical regents (Rasad for her son Caliph al-Mustansir of Egypt, Kol Sverker for his son Duke Sven of Ostergotland, and, most obscurely, Guy de Bachaumont for his nephew Count Bouchard of Vendome) in near-record time.  

For those of you who were curious, here’s the uncensored list from DD #116:  


![116_List.PNG](https://forumcontent.paradoxplaza.com/public/951594/116_List.PNG "116_List.PNG")



… and that about sums up everything, I think. Regencies is part of the free update that comes together with Tours & Tournaments. It’s a core part of how travel works so it’s intended to be a core part of the title going forward.  

And now on to part 2 of our double-DD.  


### Elegance of the Empire​


Hi everyone, I’m Nils, Principal Character artist on CK3.  

Ewan’s act will be a tough one to follow for sure, but to round this week's dev diary off, I'm here to write about the new set of clothes we're adding for the Chapter II Expansion Pass! That's right, you will get access to these unbelievably fashionable outfits on top of all the other good stuff we'll be releasing for everyone joining in on Chapter II, the next season of content for Crusader Kings III!  

### Dressed to Impress​

The theme this time is really the fanciest of the fancy; garments worthy of emperors and empresses. We have given this pack what we considered a fitting name: Elegance of the Empire.  

![Dress to impress.jpg](https://forumcontent.paradoxplaza.com/public/951562/Dress to impress.jpg "Dress to impress.jpg")


*Characters dressed in Elegance of the Empire assets. Look at all that Bling!*  

As with previous sets, we aimed to stay close to historical accuracy and, as usual, we did our due diligence when it came to research. This meant trawling the internet and our bookshelves for fitting examples of historical dress. The ambition was to create a wardrobe for an emperor and an empress similar to what it might have looked in the 11th century - in other words, around the later start date of CK3.  

## Take on the Mantle​

Somewhat amazingly if you think about it, there are a number of garments surviving from medieval times to this day. Among those are the thousand-odd years old mantles of Emperor - and later Saint - Henry II (973-1024) and his spouse the Empress - also later Saint - Cunigunde (975-1033). Of course, extant items are hard to beat as source material so these provided an excellent reference for our new mantles and a direction to follow for the rest of the clothes set.  

![Henry II Mantle.jpg](https://forumcontent.paradoxplaza.com/public/951563/Henry II Mantle.jpg "Henry II Mantle.jpg")


*The “Star-mantle” of Henry II*  

Although it is a little bit unclear if this garment was ever worn by the Emperor himself and, admittedly, if it should even be considered a mantle at all (it might have been originally worn as a chasuble) it has a distinct and interesting design and served as a great base for a new mantle design. The embroidered pattern depicts various religious and astrological motifs and the Latin text along the bottom hem (which is simplified in our version) translates to something like: “May good luck be with you, Emperor Henry, treasure of Europe, may your empire grow larger, you ruler for all time”. But you all probably got that already.  


![Mantle of Cunigunde.jpg](https://forumcontent.paradoxplaza.com/public/951564/Mantle of Cunigunde.jpg "Mantle of Cunigunde.jpg")


*The Great Mantle of St. Cunigunde*  

Cunigunde’s mantle is adorned with framed figures representing scenes from the lives of Christ and the saints Peter and Paul. The design also incorporates decorative patterns and many small religious inscriptions. We recreated this design for the new female mantle.  

![In game mantles.jpg](https://forumcontent.paradoxplaza.com/public/951565/In game mantles.jpg "In game mantles.jpg")


*Our in-game mantles. Made by Joakim and Oskar.*  


## The Crown(s)​

Fortunately for us, the mantles are not the only regalia to survive from this imperial couple. No less spectacular is the Crown of Cunigunde, possibly made for her coronation in 1002. This beautiful and heavily gem-adorned crown in the romanesque style was an obvious choice for the new female royalty-tier headgear in the set.  

![crown_of_cunigunde comparison.jpg](https://forumcontent.paradoxplaza.com/public/951566/crown_of_cunigunde comparison.jpg "crown_of_cunigunde comparison.jpg")


*The Crown of Cunigunde real life vs in-game version*  

Interestingly, a crown known as the crown of Henry II also exists. However, this impressive piece is actually a reliquary crown of a much later date and was not made anywhere close to Henry's lifetime. On top of that, it in fact already exists in the game as the “Jewel-encrusted Crown” released with the Garments of the Holy Roman Empire!  

![Reliquiary crown of Henry.jpg](https://forumcontent.paradoxplaza.com/public/951568/Reliquiary crown of Henry.jpg "Reliquiary crown of Henry.jpg")


*The Reliquary Crown of Henry II*  

So we had to look for inspiration elsewhere for the new male imperial crown. We ended up going for another reliquary crown known as the Crown of Hildesheim. It is in the right style and most likely from the right time and area, so it seems close to something Heinrich, or another sovereign of the time, might have worn. As any good medieval crown should, this design certainly adheres to the “more is more” aesthetic…  

![Crown_of_hildesheim.jpg](https://forumcontent.paradoxplaza.com/public/951585/Crown_of_hildesheim.jpg "Crown_of_hildesheim.jpg")


*The Crown of Hildesheim real life vs in-game version. This beautiful asset was made by our artist Joakim (as was the female one as well)*  

*Today, the crown is kept at Hildesheim Cathedral Museum in Germany. It sits on top of a reliquary statue of Saint Oswald, if you fancy a real life look at the original!*  

## Attired you out yet?​

As unlikely as it seems, another garment of Henry II has also been preserved to this day. That is his tunic or dalmatic, which provided the foundation for the new male emperor-tier clothes that we are adding in the pack.  

To be precise, only the decorative trims of this tunic are actually from the original clothes. But we can get a good sense of how it looked by adding the trims to a garment construction typical of the time.  

![Tunic of Henry II.jpg](https://forumcontent.paradoxplaza.com/public/951587/Tunic of Henry II.jpg "Tunic of Henry II.jpg")


*Tunic of Henry II. Some sources suggest the decorative trims and cuffs might in fact have been part of a garment belonging to his wife Cunigunde. It was hard to find a definitive answer, but we decided to use this as a base for the new male clothes.*  

To emphasize the regal feel of this outfit, we added a very fancy (if impractical) looking sword and sword belt. The sword is closely based on the so-called Sword of Saints Cosmas and Damian, also known as the Sword of Essen, which was gifted by the Emperor Otto III (Henry II’s cousin and predecessor) to the Essen Abbey in 993. So we can say with some confidence that if you were looking for the most impressive sword money could buy in Europe in the late 10th or early 11th century - it would have looked something like this.  

![Sword_of_essen.jpg](https://forumcontent.paradoxplaza.com/public/951572/Sword_of_essen.jpg "Sword_of_essen.jpg")


*The Sword of Saints Cosmas and Damian, real life vs our version*  

For the female outfit, we did not find a suitable extant garment to base it on, so we had to turn to secondary sources. There are a number of contemporary depictions of the empress Cunigunde which provided a direction for the clothes.  

![Henry_And_Cunigunde_Bamberg.jpg](https://forumcontent.paradoxplaza.com/public/951573/Henry_And_Cunigunde_Bamberg.jpg "Henry_And_Cunigunde_Bamberg.jpg")


*Henry II and Cunigunde founding the Bamberg Cathedral, 11th century*  

The outfit also features a bag which was based on a German reliquary bag of the 11th century. While not technically a lady’s purse, it has a lot of similarities with girdle pouches and purses of slightly later dates, so it seems reasonable that a fancy purse of the 11th century might have looked similar to this.  


![Reliquiary bag.jpg](https://forumcontent.paradoxplaza.com/public/951590/Reliquiary bag.jpg "Reliquiary bag.jpg")


*German Reliquary bag,11th century*  

![sp2_clothes.jpg](https://forumcontent.paradoxplaza.com/public/951592/sp2_clothes.jpg "sp2_clothes.jpg")


*In-game male and female outfits*  

## Something for the rabble​

In addition to the imperial-tier garments and headgear, the Elegance of the Empire set also contains new High Nobility headgear. These will add some nice visual variety to dukes and duchesses in Europe.  

The male one is based on a type of hat seen in some manuscript illustrations and an extant “cloth crown” belonging to none other than Hildegard von Bingen, the famous German composer/writer/philosopher/etc. abbess of the 12th century. So apparently, this was a style of head covering worn by both men and women of high stature.  


![sp2_nobility_headgear.jpg](https://forumcontent.paradoxplaza.com/public/951580/sp2_nobility_headgear.jpg "sp2_nobility_headgear.jpg")


*Manuscript illustrations, the Crown of Hildegard von Bingen*  

For the ladies, we have added a new circlet based on the 12th century funeral crown of queen Anna of Antioch.  

![sp2_nobility_headgear_ingame.jpg](https://forumcontent.paradoxplaza.com/public/951581/sp2_nobility_headgear_ingame.jpg "sp2_nobility_headgear_ingame.jpg")


*The new male and female High Nobility headgear*  

## It’s a Must(ache)​

Saving the best for last, we have also added a glorious new mustache! I think, in this case, I’ll just let the screenshots speak for themselves.  


![sp2_mustache.jpg](https://forumcontent.paradoxplaza.com/public/951582/sp2_mustache.jpg "sp2_mustache.jpg")


*The new Regal Mustache*  


That’s it for me this time!  

## A few words on the roadmap from our Game Director​

We want to provide a clear view of our current plan for 2023. Today we’re excited to reveal that Crusader Kings III: Tours & Tournaments is releasing on the 11th of May 2023. And we’re also sharing the roadmap of what will come:, all part of what we are calling Chapter II:  


![16_9 (1).png](https://forumcontent.paradoxplaza.com/public/951583/16_9 (1).png "16_9 (1).png")



If you purchase Chapter II already today, you get access to Elegance of the Empire instantly. Next up is of course Tours & Tournaments on the 11th of May - mark your calendars and check out Chapter II here:  

[Chapter II on Steam](https://store.steampowered.com/bundle/31178/Crusader_Kings_III_Chapter_II/)  

[Chapter II on Microsoft Store](https://www.microsoft.com/store/productid/9nfjz5747nb4)  

Next week, we will have a deep dive into Tournaments - until then!

 

#### Attachments

- [![diarchies_001.PNG](https://forumcontent.paradoxplaza.com/thumbnail/public/951490/diarchies_001.PNG)](https://forum.paradoxplaza.com/forum/attachments/diarchies_001-png.963989/)
  
  diarchies_001.PNG
  1,4 MB

 · Views: 0

- [![diarchies_001.PNG](https://forumcontent.paradoxplaza.com/thumbnail/public/951491/diarchies_001.PNG)](https://forum.paradoxplaza.com/forum/attachments/diarchies_001-png.963990/)
  
  diarchies_001.PNG
  1,4 MB

 · Views: 0

- [![diarchies_009.PNG](https://forumcontent.paradoxplaza.com/thumbnail/public/951506/diarchies_009.PNG)](https://forum.paradoxplaza.com/forum/attachments/diarchies_009-png.964005/)
  
  diarchies_009.PNG
  2,3 MB

 · Views: 0

- [![diarchies_038.PNG](https://forumcontent.paradoxplaza.com/thumbnail/public/951547/diarchies_038.PNG)](https://forum.paradoxplaza.com/forum/attachments/diarchies_038-png.964046/)
  
  diarchies_038.PNG
  335,7 KB

 · Views: 0

- [![116_List.PNG](https://forumcontent.paradoxplaza.com/thumbnail/public/951555/116_List.PNG)](https://forum.paradoxplaza.com/forum/attachments/116_list-png.964054/)
  
  116_List.PNG
  345,2 KB

 · Views: 0

- [![Crown_of_hildesheim.jpg](https://forumcontent.paradoxplaza.com/thumbnail/public/951569/Crown_of_hildesheim.jpg)](https://forum.paradoxplaza.com/forum/attachments/crown_of_hildesheim-jpg.964068/)
  
  Crown_of_hildesheim.jpg
  605,9 KB

 · Views: 0

- [![Tunic of Henry II.jpg](https://forumcontent.paradoxplaza.com/thumbnail/public/951571/Tunic of Henry II.jpg)](https://forum.paradoxplaza.com/forum/attachments/tunic-of-henry-ii-jpg.964070/)
  
  Tunic of Henry II.jpg
  22,2 KB

 · Views: 0

- [![Reliquiary bag.jpg](https://forumcontent.paradoxplaza.com/thumbnail/public/951574/Reliquiary bag.jpg)](https://forum.paradoxplaza.com/forum/attachments/reliquiary-bag-jpg.964073/)
  
  Reliquiary bag.jpg
  354,7 KB

 · Views: 0

- [![sp2_clothes.jpg](https://forumcontent.paradoxplaza.com/thumbnail/public/951576/sp2_clothes.jpg)](https://forum.paradoxplaza.com/forum/attachments/sp2_clothes-jpg.964075/)
  
  sp2_clothes.jpg
  831,9 KB

 · Views: 0

- [![diarchies_043.PNG](https://forumcontent.paradoxplaza.com/thumbnail/public/951593/diarchies_043.PNG)](https://forum.paradoxplaza.com/forum/attachments/diarchies_043-png.964092/)
  
  diarchies_043.PNG
  50,2 KB

 · Views: 0

<!-- artifact:reactions:start -->
- 225 Love
- 107 Like
- 10 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Paradoksalny Kierownik](https://forum.paradoxplaza.com/forum/members/paradoksalny-kierownik.1725641/)**
Role: Corporal
Badges: 44
Messages: 27
Reaction score: 1,566

*[Full game-badge icon list of 44 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
