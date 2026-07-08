---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1856175/"
forum_thread_id: 1856175
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 180
title: "Dev Diary #180 - How a Crown is Earned"
dd_date: 2025-08-21
author_handle: PDX-Trinexx
expansion: Coronations
patch: Patch 1.17
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2915
inline_image_count: 36
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1856175'
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
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_428_to_432
    action: preserved_and_flagged
    counts:
      Like: 79
      Love: 25
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_440_to_500
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_501_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Dev Diary #180 - How a Crown is Earned

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)
- Start date [Aug 21, 2025](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-180-how-a-crown-is-earned.1856175/)
<!-- artifact:thread_metadata:end -->

*(CM's note: Today's dev diary is brought to us by one of our designers lacking a forum account; please politely shame them in the comments for this)*  

Hello again, my good players, modders, friends, enemies, mum and dad! I am (yet again) Jason, and I’m here to give you more details about Coronations, the central feature of our similarly named event pack.  

I think we should just run through a particular character's Coronation experience from beginning to end. Afterwards, perhaps have a quick discussion of the possible choices our protagonist didn't make, and get into a Coronation guest's perspective and possibilities.  
Please note that everything shown in this dev diary is a work in progress, and the numbers you see here today are liable to change before the release of Coronations  

## Coronations: From Crownless to Becrowned-Upon​

Please meet our hero: young King Ailill of Scotland. He’s just taken the throne and he’s facing some rather tough circumstances. Not exactly hated throughout the realm, but certainly not liked by all. A strong faction stands in opposition to our sweet boy Ailill, and his little two-county demesne leaves him little strength with which to dissuade them.  

![image_01.png](https://forumcontent.paradoxplaza.com/public/1345045/image_01.png "image_01.png")


*[But hey… he’s a nice guy.]*  

Notice his head is a little bare? As a king yet to hold a Coronation, the Uncrowned law has been set on King Ailill upon his succession: he’s losing vassal opinion, and his Legitimacy is being both drained and its gain neutered. This needs to be sorted.  

![image_02.png](https://forumcontent.paradoxplaza.com/public/1345046/image_02.png "image_02.png")


*[The principal reminder to hold a Coronation, but there are a few others in suitable places]*  

Fortunately (or because a certain guardian angel interfered on his behalf), King Ailill has enough gold to hold a Coronation right away. This is a doubly good choice because it’ll keep the mighty Liberty Faction off his back temporarily… although whether the Coronation will weaken or swell that Faction remains to be seen.  

![image_03.png](https://forumcontent.paradoxplaza.com/public/1345047/image_03.png "image_03.png")



Ailill may only hold a regular Coronation; as a Catholic king, he cannot hold a papal Anointment, which is a rite reserved for emperors alone. He will be crowned in his capital, St. Johnston. As the site of other coronations of the past, this barony boosts his activity’s chance of success. The middling options for ceremony and celebrations are all he can afford, but they should serve well enough.  

![image_04.png](https://forumcontent.paradoxplaza.com/public/1345048/image_04.png "image_04.png")



The Intent our boy selects will have a significant impact on the outcome of this pricey endeavor. Some suit his precarious situation well, while others represent a bit of a strategic miscalculation.  

Exalt the Crown is great for when you’re in a safe situation. Rather than striving to please attendees, you’ll strive towards bonuses for your Dynasty and Coronation artifacts, as well as tack additional rewards onto the Oath you will hopefully manage to complete.  

![image_05.png](https://forumcontent.paradoxplaza.com/public/1345049/image_05.png "image_05.png")


*[Note that all these Intents let you gain Opinion with a certain subset of your vassals]*  

Weaken Detractors could help Ailill against the Faction opposing him: he may get opportunities to peel off its members or lower its discontent. Sadly, Ailill is a compassionate feller and he’s not interested in bullying his attendees or entrenching the hatred of his enemies.  

![image_06.png](https://forumcontent.paradoxplaza.com/public/1345050/image_06.png "image_06.png")



Embrace Supporters could be a useful Intent, as King Ailill has some important friendly vassals whom he could further strengthen and please.  

![image_07.png](https://forumcontent.paradoxplaza.com/public/1345051/image_07.png "image_07.png")



Impress Attendees is a reliable fallback, particularly for those facing unpopularity. It will give Ailill the most opportunities to boost his general image and counteract losses to Magnificence (the Coronation’s success metric). He’s going to go with this Intent.  

![image_08.png](https://forumcontent.paradoxplaza.com/public/1345052/image_08.png "image_08.png")



The Activity is announced, and invitations go out. The king’s guests choose their own Intents: some are helpful to their host, some are hostile, and others - pure self-interest.  

And so, it begins! Note, on the right, that the most powerful of Ailill’s supporters and detractors - those who can affect the course of his Coronation - are shown, with their Activity Intents. The Coronation’s Magnificence is currently extremely low, and likely to spawn negative events or effects for King Ailill. It was damaged by the existence of the strong Liberty Faction, and wasn’t particularly high to begin with.  

![image_09.png](https://forumcontent.paradoxplaza.com/public/1345053/image_09.png "image_09.png")



If you’re a member of a culture or faith that practiced Coronations involving a priest placing the crown, you get the event below - and a choice between having the crown put on you and crowning yourself. The latter practice was surprisingly common in, say, medieval Iberia. This event obviously does not trigger if your Coronation is an Anointment, and is all about being recognized by the Pope.  

Ailill will crown himself king without the church’s intercession… because I showed off the “you are crowned by a priest” event in last week’s [dev diary](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-178-a-vision-in-gold.1855069/).  

![image_10.png](https://forumcontent.paradoxplaza.com/public/1345054/image_10.png "image_10.png")



The Prelude phase of the Coronation has begun: in its random events, the host and guests begin to meet, to engage in politics, and discuss the ceremony to come.  

![image_11.png](https://forumcontent.paradoxplaza.com/public/1345055/image_11.png "image_11.png")


*[An opportunity to unleash supporters against detractors; a faction leader, no less!]*  

Throughout the Coronation, its host will receive Petition events from groups of guests who all hold the same Intent. Most of these are largely beneficial, and the Host may choose between accepting the petition (to increase Cultural Acceptance, etc.) and disappointing the petitioners in exchange for some Magnificence.  

King Ailill’s guests do not all have friendly Intents, and those intending to Disrupt Loyalists confront him in order to strengthen their faction. They are only able to do so because the unfriendly Detractors at the Coronation outnumber, or outmatch, Ailill’s present Supporters.  

![image_12.png](https://forumcontent.paradoxplaza.com/public/1345056/image_12.png "image_12.png")


![image_13.png](https://forumcontent.paradoxplaza.com/public/1345057/image_13.png "image_13.png")



With his focus on impressing everyone during the Prelude (at the expense of gaining pretty much anything else), Ailill has increased Magnificence up to an appreciable 63/100 for the beginning of the Ceremony. The people of St. Johnston are pleased with the regal spectacle!  

![image_14.png](https://forumcontent.paradoxplaza.com/public/1345059/image_14.png "image_14.png")


![image_15.png](https://forumcontent.paradoxplaza.com/public/1345060/image_15.png "image_15.png")



The ceremony proceeds, with Ailill gaining or losing some currency based on his popularity among each of the Three Estates: the nobility, the clergy, and the common people.  

![image_16.png](https://forumcontent.paradoxplaza.com/public/1345061/image_16.png "image_16.png")


*[The common people get a say about their king… sort of]*  

The time comes for Ailill to crown himself! If he had any zealous vassals, they would now be displeased along with his realm priest.  

![image_17.png](https://forumcontent.paradoxplaza.com/public/1345062/image_17.png "image_17.png")



When all the ceremonial events are complete and an Oath is chosen, or all possible Oaths are turned down (more on this below), it’s time for the celebratory feast!  

![image_18.png](https://forumcontent.paradoxplaza.com/public/1345063/image_18.png "image_18.png")



This final phase of the Coronation can still play host to politics, but now also presents chances to lose accumulated stress, and more opportunities to gain positive relations.  

![image_19.png](https://forumcontent.paradoxplaza.com/public/1345064/image_19.png "image_19.png")


*[This is actually an Exalt the Crown option - but I couldn’t resist showing it off]*  

If the host is true to the Intent they began the Coronation with (that is, if they never switch it out) they may claim an additional reward at the activity’s end. Our guy Ailill was utterly focused on Impressing his Attendees.  

![image_20.png](https://forumcontent.paradoxplaza.com/public/1345065/image_20.png "image_20.png")



And, well, you’ve all seen Activity Conclusions before! So I think this wraps up Ailill’s Coronation.  

To summarize how it went: as I mentioned earlier, Ailill incurred significant opportunity cost to choose options that improved Magnificence, but it furnished him with more Prestige and Legitimacy at the close of his Coronation. He achieved those ends pretty well; he made his most powerful vassal into a new friend/best bro, swayed most attendees into liking him more, made it to the next level of legitimacy, and gained a good chunk of prestige. But he spent a bunch of gold on this, and he’s still likely to face a civil war now that festivities are over. What’s more, Ailill’s realm has been sort of torn by the divide between his supporters and detractors… who, at the Coronation’s end, lose opinion of one another and get closer to becoming rivals.  

So yeah, this new Coronation activity is a hive of drama, wherein I’d say we got acquainted with young King Ailill ( #1 goodestboy of Alba) and his particular crop of vassals and contemporaries pretty well.  

Now, let’s take a look at how the activity plays out for a guest.  

## The Guest Perspective​

Attending Coronations as a guest is highly encouraged, particularly if it happens to be your liege’s Coronation! AI vassals are basically required to attend. And if you disinvite them for being haters - they send you a snarky letter inviting themselves back.  

Guests come not to murder and seduce and all those usual things: they come to figure out where they stand with this new ruler, to find opportunities for personal gain… or just to be nice and have a good time. We really wanted to allow guests agency through Intents, and thereby lend attending Coronations a tangible purpose, expanding your expected outcomes beyond the usual stress loss and opinion gains with random attendees.  

Here are the Guest Intents, some of which are available only to vassals:  

Bear Witness, the default Intent, is for those simply into having a good time… or maybe those specifically interested in cultural acceptance with attendee cultures, piety, or legitimacy. The latter is a pretty juicy gain from just attending someone else’s activity!  

![image_21.png](https://forumcontent.paradoxplaza.com/public/1345066/image_21.png "image_21.png")


*[The default Guest Intent]*  

Offer Support is a great choice when you favor the crowned sovereign, want their goodwill, and intend to help secure their position. This is a particularly handy Intent when you’re setting up your dynasty in other realms, and looking for opportunities to help them succeed.  

![image_22.png](https://forumcontent.paradoxplaza.com/public/1345067/image_22.png "image_22.png")



Advocate Domain is a vassal-only Intent, and pretty nifty for those intensely interested in their little corner of the realm. In their time of fresh uncertainty, a new liege might prove quite generous in inducements and concessions towards your lands’ prosperity.  

![image_23.png](https://forumcontent.paradoxplaza.com/public/1345068/image_23.png "image_23.png")



Vassals interested in getting their contracts changed may pick Profess Rights and hope for a major boon from their liege. With such a narrow focus, you may see fewer rewards… but we all know how big it is if you do get the treasure of all treasures: reduced vassal taxes.  

![image_24.png](https://forumcontent.paradoxplaza.com/public/1345069/image_24.png "image_24.png")



The Seize Advantages Intent yields prestige, gold, or claims on titles in or near the host’s realm; expect opinion hits though, as it’s not the friendliest Intent.  

![image_25.png](https://forumcontent.paradoxplaza.com/public/1345070/image_25.png "image_25.png")



Definitely not the friendliest of Intents, Disrupt Loyalists is your path to reducing the Magnificence of the Coronation, and thereby costing the host Prestige, Legitimacy, and Opinion. It’s particularly useful for faction members, and those with rivalries against the host and their supporters. A terrible foe with Disrupt Loyalists may even critically succeed… and get the chance to coup their despised host.  

But be warned: this Intent will create ill will with the sovereign being crowned, and with those who love them.  

![image_26.png](https://forumcontent.paradoxplaza.com/public/1345071/image_26.png "image_26.png")



As you can see, there is a good selection of Intents for guests - Intents that should prove relevant to your gameplay interests.  

Some answers to potential questions: you can attend the Coronation of your spouse, and you will be recognized as consort. You can’t be the officiant at a Coronation. You can only attend as a full-grown adult (although the ruler getting crowned has a minimum age of 12. We want waiting for adulthood to be a little punishing… not too punishing).  

Below is a guest-facing petition event, the culmination of their Intent. In this instance, the guest has the Advocate Domain Intent and is the only attending vassal who has selected it. Nice guy Ailill chooses to accept.  

![image_27.png](https://forumcontent.paradoxplaza.com/public/1345072/image_27.png "image_27.png")



As the Coronation progresses, the guests get random flavor events in the Prelude and Feast phase. They receive some events in the Ceremony phase where they bear witness to the host becoming a proper sovereign.  

For instance, if you’re a vassal and receive the event below, this is a big opportunity to speak out and either voice contempt or total support (or do neither of these things). Being a sufficiently devoted detractor can lead to rivalries, be warned.  

![image_28.png](https://forumcontent.paradoxplaza.com/public/1345073/image_28.png "image_28.png")



There are plenty more random and systemic events I could include in this, but I think y’all get the idea.  

---

## Oaths​

Hello there, this is Joachim, better known around these parts as [@Snow Crystal](https://forum.paradoxplaza.com/forum/members/1280952/), with a small section on Oaths. Oaths are a new mini-feature we added to the Coronations as a part of the middle phase of the activity. You will be able to choose an Oath to open up a special decision and set yourself a long-term goal for the crowned ruler in question.  

Our aim in making these Oaths is to give the player some tangible goals to choose from, to give their rule a more substantial focus, in addition to your regular decisions.  

![image_29.png](https://forumcontent.paradoxplaza.com/public/1345074/image_29.png "image_29.png")



We have changed the event screen for the occasion to show you more options at once and give you more alternatives. Hopefully, this will enable the player to find something that fits their interests for their next ruler. Of course, if none do, you can refrain from taking an Oath if you are uninterested.  

Now, let’s have a look at some of the options here, so we can take a better look at exactly what the Oaths are like.  

![image_30.png](https://forumcontent.paradoxplaza.com/public/1345075/image_30.png "image_30.png")



Each Oath comes with a time restriction, some requirements, and rewards. Some of the Oaths are a tad more simplistic and more likely to be available, as they are almost always relevant, like the conquest Oath we have a picture of here, whereas others will be a bit more involved.  

The exact rewards you get will be affected by the Coronation Magnificence, so a higher Magnificence will provide a higher amount of legitimacy and prestige.  

![image_31.png](https://forumcontent.paradoxplaza.com/public/1345076/image_31.png "image_31.png")



![image_32.png](https://forumcontent.paradoxplaza.com/public/1345077/image_32.png "image_32.png")



The Oath decision will be available at the top of the decision screen in a new special Oath category, as well as in the Current Situation screen, both of them showing the amount of time remaining. Those who fail to uphold their Oath in time will lose legitimacy and prestige as they lose face among peers, vassals, and peasants.  

![image_33.png](https://forumcontent.paradoxplaza.com/public/1345078/image_33.png "image_33.png")



After that, it functionally works like most decisions do. You fulfill some requirements, and you get some (occasionally spicy) rewards for your actions. With all that said, let’s take a look at a handful of the Oaths we have added.  

![image_34.png](https://forumcontent.paradoxplaza.com/public/1345079/image_34.png "image_34.png")



![image_35.png](https://forumcontent.paradoxplaza.com/public/1345081/image_35.png "image_35.png")



![image_36.png](https://forumcontent.paradoxplaza.com/public/1345082/image_36.png "image_36.png")



So these come in many different forms, really. They are still a work in progress, but hopefully some of these have piqued your interest.  

---

## Bye!​

Jason again. Thanks for reading! It’s been a personal pleasure to explore the long-awaited possibilities of coronations in Crusader Kings III, to expand on what our in-game Activities can be, and to write y’all some of my most fanciest events yet.  

I truly hope you enjoy our event pack. If there’s anything you’re exceptionally interested in or hopeful for with this new Activity, then please let us know below!

<!-- artifact:reactions:start -->
- 79 Like
- 25 Love
- 7 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)**
Role: Community Manager
Badges: 102
Messages: 642
Reaction score: 17,753

*[Full game-badge icon list of 1 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
