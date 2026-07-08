---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1292549/"
forum_thread_id: 1292549
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 6
title: "CK3 Dev Diary #06 - Council, Powerful Vassals, & Spouse Councillor"
dd_date: 2019-12-03
author_handle: Wokeg
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1695
inline_image_count: 6
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1292549'
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
    location: raw_lines_~28_to_144
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_146_to_148
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_251_to_252
    action: preserved_and_flagged
    counts:
      Like: 7
      (unlabeled — rendered as base64 data URI): 4
    note: Reactions block parsed; 1 of 2 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_260_to_323
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_324_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #06 - Council, Powerful Vassals, & Spouse Councillor

<!-- artifact:thread_metadata:start -->
- Thread starter [Wokeg](https://forum.paradoxplaza.com/forum/members/wokeg.1325927/)
- Start date [Dec 3, 2019](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-06-council-powerful-vassals-spouse-councillor.1292549/)
<!-- artifact:thread_metadata:end -->

Greetings, friends!  

I’m Wokeg, and I’m the juniorest of the content designers on CK3. Unless you like anarcho-communist insect people, you almost certainly haven’t heard of me: mostly I scuttle around the office mumbling about the West Country and obscure cultural features, but I’m here to talk to you today about your council, your powerful vassals, and the role of your spouse in the realm.  

Let’s start with the basics: what have we carried over from CK2?  

Your council still has five primary positions: a chancellor, steward, marshal, spymaster, and court chaplain, each relying on a particular skill (respectively, diplomacy, stewardship, martial, intrigue, and learning). Every councillor is either a vassal or a courtier of yours, and you are (mostly) able to hire and fire for these roles at will. Each of these council positions can be given different tasks, relying on an appropriate skill, which help your realm to survive and thrive. Theoretically.  

![001.jpg](https://forumcontent.paradoxplaza.com/public/517127/001.jpg "001.jpg")

  

Ok, so that should be pretty familiar to most of you. So, what’s actually *changed*?  

Firstly, state skills are gone. While they weren’t the worst thing in the world, you tended to forget they existed unless they were utterly abysmal, which was incredibly rare. Plus, personally, I could never get the mental image of your chancellor leaping in front of the king and clamping a hand over his mouth every time he thought of another dirty joke about the King of France out of my head.  

Instead of affecting your character’s skill in certain interactions, councillor skills now *dramatically* affect their efficacy at the tasks you set them. A skilled steward not only yanks coins from the hands of undeserving peasants as fast as the peasants earn ‘em, they’ll also be much more likely to receive positive minor events while doing it. Similarly, a terrible steward is not just slow, they’ll actively bungle things and make a mess of your accounts as they go. Choosing between the politically-powerful idiot and the adroit courtier has never been quite so difficult.  

![002.png](https://forumcontent.paradoxplaza.com/public/517128/002.png "002.png")

  

To compensate for this a little, merely being on your liege’s council will give you a very minor bonus to the appropriate skill for your position. Even a truly terrible councillor has at least *some* assistants helping them out.  

Further, tasks now do not reset when changing councillors. If you tell your steward to keep increasing the development in a particular county, they’ll stick at it until told to stop, pausing if you have no steward at all. Council tasks in specific counties will only stop if the county stops being a valid place to perform that task, such as because a time-locked action (e.g., religious conversion) was completed, or because you lost the county in a war.  

Instead of listing all the possible tasks each councillor can take, let’s keep things light and just have the most interesting/newest task each councillor can perform:  


- *Chancellor:* **Integrate Title**, speeds de jure drift of a valid title into your realm.
- *Marshal:* **Increase Control in County**, increase control gain per month in a specific county.
- *Steward:* **Increase Development in County**, reduce building & holding construction time in a specific county. Boost development growth per month in the same.
- *Spymaster:* **Find Secrets**, attempt to learn of secrets in a given court, including your own.
- *Court Chaplain:* **Fabricate Claim on County**, gain opportunities to acquire claims on a specific county.

Ok, that was a lot of information on non-dramatic differences. Are there any really *big* changes we’ve got stored up?  

Well now, that depends. Are you single and outside the reach of that meddlesome Pope? Then life might seem pretty smooth, at least for a while. On the other hand, if you’re a married Catholic…  

![003.jpg](https://forumcontent.paradoxplaza.com/public/517133/003.jpg "003.jpg")

  

The first part of this is marriage, and, as you may have guessed from the title of this dev diary, the five classic slots are now joined by your primary spouse! Historically, spouses were often vital assistants in running the realm, providing counsel and advice even when they, strictly speaking, were not supposed to.  

We model this by giving them a variety of council tasks, each one boosting your stats directly by taking some of the weight of leadership off of your shoulders. The default is a generic “assist ruler” task, simply helping out here and there, and providing a minor flat boost to all skills, for those rulers who feel like they can pretty much tackle the world unassisted. Discounting vassals as assistance, because, y’know, obviously.  

If you need more specialised help, you can also have them boost a specific stat directly. This adds a large portion of their skill directly to yours, as you offload an immense amount of power and responsibility onto your spouse, lending them your authority in exchange for their skill. While focusing in this manner, they’ll only boost their assigned skill, so you’ll need to choose how they support you carefully.  

Don’t have a spouse? Well, that’s ok, single feudal heirs are out there just waiting to meet you.  

Have a spouse and they’re landed? I’m afraid they’ve got better things to do than finish your lordly homework for you.  

![004.png](https://forumcontent.paradoxplaza.com/public/517134/004.png "004.png")

  

Now, for the second of our two major differences: have you ever heard the phrase “Will no one will rid me of this turbulent priest”?  

Well, have we got some turbulent priests for you.  

Certain faiths (details on which, other than Catholicism, to follow in a later diary) replace the court chaplain with a bishop. If you still have a court chaplain, then they’ll behave much like other councillors, though some faiths may still have a harder time firing them.  

Bishops use a mechanic called leasing (though they’re not the only ones to do so), whereby they control all levies and receive all taxes from every temple holding in your personal domain. Additionally, your bishop will receive a fraction of the taxes and levies generated by all of your vassals’ bishops. All told, that’s a ***lot*** of ducats the Church seems to be getting, isn’t it?  

Of course, as loyal subjects of the crown, your bishop will be very happy to hand over taxes and troops to you, scaling with quite how happy they are. A loyal bishop is a huge boon for your economy and military, and can make the difference between unstoppable royal might and economic ruin.  

A recalcitrant bishop, by contrast, is an utter pain. If they do not approve of you at least a little, they’ll hold back taxes and levies until you meet their standards again, and if they actively hate you, may even begin conspiring with others to replace you with a more pious monarch.  

Of course, you’re probably asking what stops you from firing your bishop and replacing them with, say, a good friend of yours?  

Around these parts, that’s what we call ***heresy***. And you’ll have to wait till the religious dev diary for details on exactly what your options are for legally sacking your bishop. As for illegally, well, no Pope can stop a knife to the base of the spine...  

Turbulent priests indeed.  

![005.png](https://forumcontent.paradoxplaza.com/public/517135/005.png "005.png")

  

Our final talking point for today is the subject of powerful vassals.  

These should be familiar to many of you from CK2’s Conclave expansion: powerful vassals are the wealthiest lords with the highest levy counts in the realm. They’re powerful, influential, and unruly, and you ignore them at your peril. The higher your tier, the more of them you’ll have to contend with, and eventually you’re going to have to pick who you want to snub rather than how you want to please everyone.  

As in Conclave, powerful vassals always expect a seat on your council. They’re the greatest magnates of their day, damn it, and they demand to be heard! Leaving one out in the political cold will give you a huge opinion penalty with that character, since a council seat is theirs by right of might.  

Not any particular seat, mind you, and just because they might not be able to organise an army to save their life, that’s no reason for you not to give them the role of marshal. Power is basically the same as competence, right?  

So, what do you actually directly *get* out of acquiescing to these uppity lords? Well, there’s one very important function that powerful vassals tie into directly: changing your succession. CK2 required you to have all vassals who both de jure and de facto belong to one of your titles approve of you before you could change your succession. In CK3, that veto belongs to your powerful vassals alone, and they very much know it.  

Finally, powerful vassals are also hooked into a number of other systems in little ways, some of which may be talked about in later dev diaries, some of which we can talk about here. In elective successions, they usually receive more votes, as they have more sway over the realm’s processes. When recruiting for schemes, powerful vassals make better agents, provided you can persuade them, and since they know this, they’re also harder to use the sway scheme on. And, lastly, an unhappy powerful vassal in a faction is a far more worrisome prospect (more on factions later down the line).  

![006.png](https://forumcontent.paradoxplaza.com/public/517136/006.png "006.png")

  

Well, that’s all we have to say on your council’s functions for now. I hope that this has answered some of your burning questions and got you excited to manage the governance of your realm.  

Next week, I believe we have some notes on characters, portraits, and traits...

<!-- artifact:reactions:start -->
- 7 Like
- 4 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Wokeg](https://forum.paradoxplaza.com/forum/members/wokeg.1325927/)**
Role: Former CK3 Experienced Game Designer
Badges: 5
Messages: 528
Reaction score: 15,169

*[Full game-badge icon list of 5 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
