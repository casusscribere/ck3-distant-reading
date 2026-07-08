---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1333592/"
forum_thread_id: 1333592
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 14
title: "CK3 Dev Diary #14 - The Diplomacy Lifestyle"
dd_date: 2020-02-18
author_handle: Voffvoffhunden
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2916
inline_image_count: 30
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1333592'
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
    location: raw_lines_~28_to_138
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_140_to_142
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_449_to_450
    action: preserved_and_flagged
    counts:
      Like: 3
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 1 of 2 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_458_to_512
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_513_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #14 - The Diplomacy Lifestyle

<!-- artifact:thread_metadata:start -->
- Thread starter [Voffvoffhunden](https://forum.paradoxplaza.com/forum/members/voffvoffhunden.246161/)
- Start date [Feb 18, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-14-the-diplomacy-lifestyle.1333592/)
<!-- artifact:thread_metadata:end -->

Welcome back everyone! It’s Tuesday, and that means I’m here to talk about Lifestyles once again. Oh come on, I can hear you at the back there, groaning! In my day we would have felt *lucky* to get such an in-depth rundown of a new system. Don’t worry though, we’re through the Lifestyles soon.  
Now, where was I? Ah, yes. This time we’re going into detail on the Diplomacy Lifestyle!  

It should require little introduction. We’ve all been there, trying to befriend our neighbors while sending gifts to our vassals to keep them from being too annoyed. We’ll also be looking at the flip side, of course. Considering the name of Paradox’s engine, we are all too familiar with the aphorism that “war is the continuation of the Diplomacy Lifestyle by other means.”  

Diplomacy contains the following focuses:  

![Diplomacy focuses.JPG](https://forumcontent.paradoxplaza.com/public/533633/Diplomacy focuses.JPG "Diplomacy focuses.JPG")


[Foreign Affairs - Diplomacy: +3]  
[Majesty - Diplomacy: +1, Monthly Prestige: +1/month]  
[Family - Diplomacy: +2, Fertility: +25%]  

**Foreign Affairs** - For when you need that kick to your Diplomacy Skill to prevent your neighbour, vassals, liege and/or your own sons from declaring war on you.  
**Majesty** - When you need a little more Prestige to keep you going.  
**Family** - Diplomacy skill to keep the peace at home, as well as a fertility boost to make sure your home keeps growing.  

We might as well get diving straight into the trees that come with the Lifestyle:  


![Diplomacy Lifestyle traits.png](https://forumcontent.paradoxplaza.com/public/533634/Diplomacy Lifestyle traits.png "Diplomacy Lifestyle traits.png")




**Family Hierarch**  

Of all the trees, I want to start with this one, because it starts off so strong.  


![Family Hierarch - Befriend.JPG](https://forumcontent.paradoxplaza.com/public/533660/Family Hierarch - Befriend.JPG "Family Hierarch - Befriend.JPG")


[Befriend - You can use the Befriend Scheme]  

Indeed, yet another Scheme unlocked by a perk, and this one can come in very handy. Not only does it seek to improve your target’s opinion of you, but to make them your Friend!  

It is a Personal Scheme that does not use Agents, which will (quite like Seduce) rely a fair bit on your target’s personality. Your Diplomacy skill is also an important factor, of course. While there are many ways to end up with Friends, the Befriend Scheme might be the most reliable one of them all. As long as you’re able to build your Success Chance high enough, of course.  

You’re all familiar with the Friend relationship, but in CK3 it will feel more present than ever. In addition to being a lot more present in events, they also offer a few mechanical bonuses, such as being better Councillors.  


![Fabricate Claim preview edited.jpg](https://forumcontent.paradoxplaza.com/public/533661/Fabricate Claim preview edited.jpg "Fabricate Claim preview edited.jpg")



Of course, not only does the tree make it easier to make Friends, it helps them offer even more bonuses!  


![Family Hierarch - Confidants.JPG](https://forumcontent.paradoxplaza.com/public/533658/Family Hierarch - Confidants.JPG "Family Hierarch - Confidants.JPG")


[Confidants - Each Friend adds: -15% Stress Gain]  

![Family Hierarch - Friendly Counsel.JPG](https://forumcontent.paradoxplaza.com/public/533656/Family Hierarch - Friendly Counsel.JPG "Family Hierarch - Friendly Counsel.JPG")


[Friendly Counsel - Each Friend gives 2 random Skill points]  
(Be sure not to lose them again, or they won’t be able to advise you anymore!)  

The tree itself offers ways of ensuring that you find more success with your Befriend Scheme, too.  


![Family Hierarch - Flatterer.JPG](https://forumcontent.paradoxplaza.com/public/533659/Family Hierarch - Flatterer.JPG "Family Hierarch - Flatterer.JPG")


[Flatterer - Befriend Scheme Power: +30%]  

![Family Hierarch - Thicker than Water.JPG](https://forumcontent.paradoxplaza.com/public/533657/Family Hierarch - Thicker than Water.JPG "Family Hierarch - Thicker than Water.JPG")


[Thicker Than Water - Personal Scheme Success Chance: +50% against family members]  

Now that I’ve mentioned family, I can hear you shouting again… "Isn’t this tree called 'Family Hierarch'? This is all about Friends!"  

Well, my - dare I say - friends, is your true family not who you choose?  

Actually, in CK3, the answer is absolutely “no”. You’re stuck with the good-for-nothing lowlives you get. What better, then, than to make them less likely to poison your wine?  


![Family Hierarch - Heart of the Family.JPG](https://forumcontent.paradoxplaza.com/public/533654/Family Hierarch - Heart of the Family.JPG "Family Hierarch - Heart of the Family.JPG")


[Heart of the Family - Close Family Opinion: +20]  

Even better, what about ensuring that future generations contain fewer of those lowlives than your current one does?  


![Family Hierarch - Groomed to Rule.JPG](https://forumcontent.paradoxplaza.com/public/533653/Family Hierarch - Groomed to Rule.JPG "Family Hierarch - Groomed to Rule.JPG")


[Groomed to Rule - Children receive 1 to 3 extra Skill points]  

But all these useless children, just lying around… what did they ever do for you? Well:  


![Family Hierarch - Sound Foundations.JPG](https://forumcontent.paradoxplaza.com/public/533655/Family Hierarch - Sound Foundations.JPG "Family Hierarch - Sound Foundations.JPG")


[Sound Foundations - Each living Child give 1 random Skill point]  

It all culminates in the Family Hierarch trait - Patriarch for men and Matriarch for women. It comes with Diplomacy bonuses, further increased Fertility, Stress Gain reductions, and even more Close Family Opinion bonuses. It’ll be a rare occasion when a family member betrays a Family Hierarch!  


To move on, maybe family is not your main priority. I get it. It can get tough at times. The same goes for friends, honestly. Sometimes anyone can get lonely. Anyways, I recommend heading over to the official [Crusader Kings Discord](https://discord.gg/ck3) to meet up with people who share some of your interests. It’s full of lovely people, so just join up, say hi, and be nice. Hang out for a while.  

Anyways, I just thought it was suitable to throw in a mention there, while also using it as a segue to the next tree!  

**Diplomat**  

The Diplomat tree looks outwards, to a much greater degree, but one thing that is good with everyone is improving the quality of your gifts:  


![Diplomat - Thoughtful.JPG](https://forumcontent.paradoxplaza.com/public/533650/Diplomat - Thoughtful.JPG "Diplomat - Thoughtful.JPG")


[Thoughtful - Opinion Gain from Send Gift: +100%]  

As for those outwards-looking perks I promised...  


![Diplomat - Defensive Negotiations.JPG](https://forumcontent.paradoxplaza.com/public/533644/Diplomat - Defensive Negotiations.JPG "Diplomat - Defensive Negotiations.JPG")


[Defensive Negotiations - Fellow Vassal Opinion: +15, Independent Ruler Opinion: +15, Can propose one Alliance without a Marriage]  

You read that right. You can straight up ask someone if they want an Alliance, and then expect the promise to be held, even if none of your family members are married! Crazy, I know. There are still a lot of restrictions on who you can enter an extra alliance with, but it gives you a little extra space to maneuver when your ratio of sons to daughters doesn’t work out perfectly.  

Alliances themselves also come with a little extra bonus now, to further sweeten the deal:  


![Diplomat - Embassies.JPG](https://forumcontent.paradoxplaza.com/public/533645/Diplomat - Embassies.JPG "Diplomat - Embassies.JPG")


[Embassies - Each Alliance grants: +1 Diplomacy Skill]  

If you still need better relations abroad after all that, there’s a perk that helps your Chancellor do their job a little better:  


![Diplomat - Adaptive Traditions.JPG](https://forumcontent.paradoxplaza.com/public/533648/Diplomat - Adaptive Traditions.JPG "Diplomat - Adaptive Traditions.JPG")


[Adaptive Traditions - Foreign Affairs effectiveness: +25%]  

It’s not the only Councillor you can improve, either. And I know this one is likely to be appreciated:  


![Diplomat - Accomplished Forger.JPG](https://forumcontent.paradoxplaza.com/public/533647/Diplomat - Accomplished Forger.JPG "Diplomat - Accomplished Forger.JPG")


[Accomplished Forger - Fabricate Claim on County Speed: +75%]  

And here we’re heading straight down into the less pleasant aspect of Diplomacy. This might be a bit of a surprise, but there are perks that unlock entirely new Casus Bellis:  


![Diplomat - Ducal Conquest.JPG](https://forumcontent.paradoxplaza.com/public/533646/Diplomat - Ducal Conquest.JPG "Diplomat - Ducal Conquest.JPG")


[Ducal Conquest - You are able to use the Ducal Conquest Casus Belli]  


![Diplomat - Forced Vassalage.JPG](https://forumcontent.paradoxplaza.com/public/533651/Diplomat - Forced Vassalage.JPG "Diplomat - Forced Vassalage.JPG")


[Forced Vassalage - You are able to use the Vassalize Casus Belli]  

Ducal Conquest lets you go to war to seize Counties required to create an as-yet Uncreated Duchy Title. Vassalize lets you… forcibly vassalise an independent ruler of lower rank. Be warned, they might not make for the happiest vassal afterwards, but that’s what your dungeons are for, right?  
There are limits on how often these CBs can be used, and they’re not the most universally useful ones, but in the right situations they can absolutely turn a realm around.  

But what’s the worst part of going to war and taking what you want? Having to “wait for truces” afterwards, of course.  


![Diplomat - Flexible Truces.JPG](https://forumcontent.paradoxplaza.com/public/533649/Diplomat - Flexible Truces.JPG "Diplomat - Flexible Truces.JPG")


[Flexible Truces - Shorter Truces and no Prestige penalty for breaking them]  

Pretty neat, huh? Remember that there will be other penalties, though, such as how willing others are to trust your word. This perk does not mean that Truce breaking is “free”.  

Finally, the trait unlocked at the end of the tree is Diplomat. It gives a hefty boost to Diplomacy, of course, but it also gives a nice little boost to Independent Ruler Opinion. That’s how respected you can get.  


**August**  

Our last tree for today is for those who want to be respected and honored for their rule. Indeed, one of the key perks will help your fame precede you.  


![August - A Life of Glory.JPG](https://forumcontent.paradoxplaza.com/public/533635/August - A Life of Glory.JPG "August - A Life of Glory.JPG")


[A Life of Glory - Level of Fame impact: +100%]  

As I’m sure you’ve all noted down in your textbooks, Levels of Fame are the levels you acquire by gathering Prestige throughout your life.  
And speaking of gathering prestige throughout your life:  


![August - Dignitas.JPG](https://forumcontent.paradoxplaza.com/public/533640/August - Dignitas.JPG "August - Dignitas.JPG")


[Dignitas - Diplomacy per Level of Fame: +1]  

Of course, living a famously powerful and honored life comes with benefits. People are more inclined to believe that you have honorable intentions, for example.  


![August - Benevolent Intent.JPG](https://forumcontent.paradoxplaza.com/public/533637/August - Benevolent Intent.JPG "August - Benevolent Intent.JPG")


[Benevolent Intent - Sway Scheme Power: +30%]  

![August - Firm Hand.JPG](https://forumcontent.paradoxplaza.com/public/533639/August - Firm Hand.JPG "August - Firm Hand.JPG")


[Firm Hand - Monthly Prestige per Dread: +1%]  

No one says you cannot be both honored and a little feared.  

With the August perk tree, those who serve you will also serve you better...  


![August - Praetorian Guard.JPG](https://forumcontent.paradoxplaza.com/public/533643/August - Praetorian Guard.JPG "August - Praetorian Guard.JPG")


[Praetorian Guard - Monthly Prestige per Knight: +2%]  
… and bring you greater benefits.  


![August - Inspiring Rule.JPG](https://forumcontent.paradoxplaza.com/public/533642/August - Inspiring Rule.JPG "August - Inspiring Rule.JPG")


[Inspiring Rule - Monthly Prestige per Adult Powerful Vassal on the Council: +5%]  

It even offers way of getting more people to serve you.  


![August - True Ruler.JPG](https://forumcontent.paradoxplaza.com/public/533641/August - True Ruler.JPG "August - True Ruler.JPG")


[True Ruler - Offer Vassalization acceptance: +25]  

Just imagine that, people willingly bending the knee to join your realm. We all know you’re the best ruler, of course, but who would have thought *they* knew?  

Finally, here is one of my personal favourites, as a little extra at the end here. Who’s better to direct the chronicle of you and your ancestors’ lives than you?  


![August - Writing History.JPG](https://forumcontent.paradoxplaza.com/public/533638/August - Writing History.JPG "August - Writing History.JPG")


[Writing History - You can take the Commission Epic Decision]  

Commission Epic starts a lengthy event chain where you can (in exchange for varying amounts of gold) commission a writer to write your family chronicle. There’s quite a few different possible paths the the effort can take, but you’ll have plenty of choice when it comes to who authors it.  


![events2_02.jpg](https://forumcontent.paradoxplaza.com/public/533662/events2_02.jpg "events2_02.jpg")



Depending on the quality of the composition, you will be able to acquire a lot of Prestige in the long run, once enough people have read it. Or at least when they keep it in their libraries.  

Sometimes I ask myself why I felt so inspired when making events about the process of creating a massive piece of creative historical fiction on an unparalleled scale under impossible deadlines. I’m sure there’s nothing deeper to examine, there, though.  

Lastly, the perk tree offers up its trait, August. Uniquely, it does not only offer a Diplomacy boost, but also a tiny bump to Martial. Its great benefit, however, lies in the increase to monthly Prestige you get, ensuring that you can make the most of your Prestigious life.  

**Events**  

I want to mention a little about the Diplomacy Lifestyle events, because they contain some very unusual events in that they offer opportunities for slightly unusual ways of getting to know people. Several event chains are quite involved, and outcomes are not merely reliant on your stats, but also on the other person’s personality.  

![events2_01.jpg](https://forumcontent.paradoxplaza.com/public/533663/events2_01.jpg "events2_01.jpg")


In this example, the outcome is not determined by chance, but by the Duke’s traits. And since he’s Gluttonous, it’s fair to assume that he’ll appreciate the effort...  
Not all the events in the lifestyle are like this, but you'll see more of them than you will in the other lifestyles. They encourage a certain insight into your friends, vassals, and neighbours that will hopefully keep them feeling fresh time and again.  


That’s all for this week! A new Lifestyle, a new Scheme, Decision and CBs. Diplomacy has a lot to offer, and I suspect that a many of you are already considering how to make friends and influence people.  

I’ll repeat the mention of the [CK Discord](https://discord.gg/ck3) as well. It’s a really lovely place, so be nice on there, and go make some friends!  

Next week we’ll be wrapping this Lifestyle journey up with the Martial Lifestyle, and I am already now willing to say that we're going to be looking at some crazy - and hopefully unexpected - stuff. I know it’s been a long time of only talking about Lifestyles, but we’re weathering it together.  


**Bonus dev story - no new info about the game below here!**  

Speaking of weathering it together, after last week there were a few questions about life as a CK dev, possibly related to the fact that I said it was a lot of work. One example of how it can get really hard is when stuff goes wrong, but it’s all buried deep in script or code, with no one knowing why.  

Last summer, I spent weeks looking for a single, humble error, somewhere in the script. Something you should know is that part of our testing process involves running “overnights”, where we let the game play itself every evening, and then we look at the results the next morning. There’s usually a bunch of errors (the game is unfinished, after all, and even a released game is rarely perfect…), and for a while, every overnight was haunted by dozens of the same error, localised on line 307 of the “contract_disease_effect”.  

Now, crucial to fixing a bug in a game is that you’re able to reproduce it. You have to know how to make it fire to check what is actually wrong, and to check that it’s fixed once you think you have fixed it. The problem was that none of us managed to reproduce it.  

Cue a mad chase where coder Matthew ( [@blackninja9939](https://forum.paradoxplaza.com/forum/members/795679/) ) and I spent days trying to track it down in ever more elaborate ways. Every time it breached the surface, we thought we had it, only for it to slip away into the deep again. But we refused to give up. ***I*** refused to give up. No error message was going to do this to me and get away with it!  
I had this illustration commissioned to immortalise the occasion:  


![contract disease effect chase.png](https://forumcontent.paradoxplaza.com/public/533666/contract disease effect chase.png "contract disease effect chase.png")



I am happy to announce that we did find the issue in the end. I won’t bother you with the boring technical details*, but it was pretty much the equivalent of hunting a white stag or some other mythical beast. All over a minor technical issue.  

Anyways, that’s just a little story from the trenches to give you some slight insight into the creation of this… thing. See you next week!  

*[Boring technical details: Turns out a destroyed title would still keep characters in line to inherit, which meant the game was trying to send notifications to the holder of the destroyed title to tell them that their heir had contracted a disease. Naturally it didn’t find any holder, since the title no longer existed, and started complaining instead.]

<!-- artifact:reactions:start -->
- 3 Like
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Voffvoffhunden](https://forum.paradoxplaza.com/forum/members/voffvoffhunden.246161/)**
Role: Rouge Game Dev - Former CK3 Content Designer
Badges: 74
Messages: 261
Reaction score: 1,286
<!-- artifact:op_signature:end -->
