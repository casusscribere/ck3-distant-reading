---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1326963/"
forum_thread_id: 1326963
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 13
title: "CK3 Dev Diary #13 - The Learning Lifestyle"
dd_date: 2020-02-11
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
body_word_count: 3999
inline_image_count: 61
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1326963'
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
    location: raw_lines_683_to_684
    action: preserved_and_flagged
    counts:
      Like: 4
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 1 of 2 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_692_to_759
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_760_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #13 - The Learning Lifestyle

<!-- artifact:thread_metadata:start -->
- Thread starter [Voffvoffhunden](https://forum.paradoxplaza.com/forum/members/voffvoffhunden.246161/)
- Start date [Feb 11, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-13-the-learning-lifestyle.1326963/)
<!-- artifact:thread_metadata:end -->

Oh, it’s Tuesday already! Time to take off my Developer Hat and put on my Developer Who Talks About the Game Hat.  

I hope all these dev diaries have been showing off my erudition, deep knowledge and, uh, healthy living? Because it’s time for the Learning Lifestyle!  

Seeking out information, acquiring knowledge, and reading everything you can get your hands on should resonate with a lot of you, seeing as that’s more or less what you’re doing right now. You might even have a theological bent and be praying for a release date announcement!  
But your prayers will go unanswered for some time yet.  

Here are the focuses that the Learning Lifestyle allows for:  


![Learning Focuses.JPG](https://forumcontent.paradoxplaza.com/public/531828/Learning Focuses.JPG "Learning Focuses.JPG")


[Medicine Focus - Learning: +1, Health: Small Boost]  
[Scholarship Focus - Learning: +3]  
[Theology Focus - Learning: +1, Piety: +1/month]  

**Medicine** is the focus for those of you who want to shield yourself and your court from the vagaries of Medieval life. Life is short enough as it stands, and far more so if smallpox decides to take up residence in your castle, or if you’re of the easily-stressed persuasion for that matter.  

**Scholarship** is a good one for those who love to seek knowledge and understand the weirdness and wonder out there. It’s effects are about knowing how to improve your own abilities, and how to improve the realm.  

**Theology** is about the great questions. Who are, and what is the divine? Why does the divine want me specifically to rule the entire world? Its perks offer numerous bonuses to your interactions with your faith and the clergy.  

The perk trees themselves match these themes fairly well, but provide you with more detailed options.  

![Learning Lifestyle Traits.png](https://forumcontent.paradoxplaza.com/public/531851/Learning Lifestyle Traits.png "Learning Lifestyle Traits.png")



**Theologian**  

I would like us to dive in head first into the realm of theology. Some of the perks here are the straightforward fare you might expect, making others of your faith like you more for being such a staunch practicioner:  

Editors note: I started out strong by getting the screenshots wrong, didn't I. Faithful is now corrected, whereas for Church and State, the value in the comment is the currently correct one, not the one in the screenshot. Oh well! (And yes, I am *also* the editor. Sue me.)  

![Theologian - Faithful.JPG](https://forumcontent.paradoxplaza.com/public/531830/Theologian - Faithful.JPG "Theologian - Faithful.JPG")


[Faithful - Clergy Opinion: +10]  

![Theologian - Church and State.JPG](https://forumcontent.paradoxplaza.com/public/531840/Theologian - Church and State.JPG "Theologian - Church and State.JPG")


[Church and State - Realm Priest opinion: +30]  

From the Council dev diary, you might remember the Realm Priest, who is appointed to give their approval or disapproval to the way you behave. You know, just so the gods can be absolutely certain that you deserve those sweet, sweet church taxes.  

It is clear that this is a very powerful perk, but I can already hear you all shout out for answers: “Will this be useless if my religion doesn’t use Realm Priests???”  

Fear not, there is a variant of the perk for all those out there who prefer that approach:  


![Church and State 2.PNG](https://forumcontent.paradoxplaza.com/public/531844/Church and State 2.PNG "Church and State 2.PNG")


[Church and State - Monthly Piety from Buildings: +100%]  

Of course, whether your Realm Priest/Court Chaplain likes you or not is irrelevant to the fact that you can improve the way they build your religious relations by being equally good at all this god-stuff as they are:  


![Theologian - Clerical Justifications.JPG](https://forumcontent.paradoxplaza.com/public/531846/Theologian - Clerical Justifications.JPG "Theologian - Clerical Justifications.JPG")


[Clerical Justifications - Religious Relations efficiency: +20%]  

Religious Relations is a Council Task, so check the Council DD for that one!  

Once you’re considered pious and a brilliant, shining example of an adherent of your faith… wouldn’t you want even more acknowledgement?  

![Theologian - Radiant.JPG](https://forumcontent.paradoxplaza.com/public/531841/Theologian - Radiant.JPG "Theologian - Radiant.JPG")


[Radiant - Level of Devotion impact: +100%]  

Now, Level of Devotion reflects how good of a believer others think you are. As with other similar values, it is increased by gaining Piety, but your “Devotion Experience” does not fall when you spend Piety, so it’s an ever-growing measure of your life’s accomplishments. Well, ever-growing as long as you do nothing to upset the church, important members of the clergy, or your god(s). At least while anyone’s watching.  

Theology isn’t just about your own faith, however. It’s also about how much better it is than every other faith. If you’re going to be doing a lot of conversion, give the Theologian tree a look:  

![Theologian - Zealous Proselytizer.JPG](https://forumcontent.paradoxplaza.com/public/531833/Theologian - Zealous Proselytizer.JPG "Theologian - Zealous Proselytizer.JPG")


[Zealous Proselytizer - Convert Faith in County progress speed: +25%]  

![Theologian - Religious Icon.JPG](https://forumcontent.paradoxplaza.com/public/531845/Theologian - Religious Icon.JPG "Theologian - Religious Icon.JPG")


[Religious Icon - Convert Faith in County: The Fervor modifier never goes below 0]  

Since the Fervor modifier can be so powerful, it can be an immense benefit to prevent it from ever being negative.  

Now, it’s really good that we have definitely told you everything about how religions and fervor and all those things work in CK3, otherwise I’d be telling you guys way too much right now.  

Especially with perks such as this:  [Prophet - ![:p](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Stick Out Tongue    :p")![:p](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Stick Out Tongue    :p")![:p](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Stick Out Tongue    :p")]  
NOTE: Ooops, turns out I finally reached the end of the line, here. There’s some things I can’t say as much as I want about, apparently. I can’t wait for you guys to get your hands on the religion DD...  

Now, back to the perk tree! Towards the end you can get skilled enough to make some very convincing arguments for why imprisoning your vassals and revoking all their titles is exactly what your god(s) would want you to do!  

![Theologian - Defender of the Faith.JPG](https://forumcontent.paradoxplaza.com/public/531836/Theologian - Defender of the Faith.JPG "Theologian - Defender of the Faith.JPG")


[Defender of the Faith - Tyranny Gain: -25%, Same Faith Opinion: +5]  

Interestingly enough, this perk changes depending on how tolerant your faith is of others. There’s multiple variations, but here’s one:  

![Defender of the faith 2.PNG](https://forumcontent.paradoxplaza.com/public/531850/Defender of the faith 2.PNG "Defender of the faith 2.PNG")


[Defender of the Faith - Diplomacy per Level of Devotion: +1, Monthly Piety: +20%]  

At the very end, you’ll get the Theologian trait, which will help provide all the Learning and Piety you could ever wish for. As befits someone who is in such close communion with the divine.  


**Whole of Body**  

So, maybe an eternal afterlife isn’t your thing? Maybe you’re more of an eternal current-life kind of person? Then the Whole of Body tree is for you! (Note that it does not confer actual immortality. That would just be a silly thing to have in a game like this, wouldn’t it?)  

First, happy news is that a familiar face is going to make a return in CK3: the Court Physician! (Pretend that was a completely new, surprising detail that you never could have guessed.) They work a lot like in CK2, but you can now do something to actually improve them:  


![Whole of Body - Anatomical Studies.JPG](https://forumcontent.paradoxplaza.com/public/531835/Whole of Body - Anatomical Studies.JPG "Whole of Body - Anatomical Studies.JPG")


[Anatomical Studies - Court Physician costs less to hire, Court Physician treatments have better outcomes]  

Of course, who needs a Court Physician, isn’t it better to just avoid getting sick in the first place?  

![Whole of Body - Wash Your Hands.JPG](https://forumcontent.paradoxplaza.com/public/531834/Whole of Body - Wash Your Hands.JPG "Whole of Body - Wash Your Hands.JPG")


[Wash Your Hands - Reduced chance of contracting Illnesses, Reduced chance for Courtiers to contract Illnesses]  

Never mind the confused looks as you’re constantly cleaning your hands, and never mind the fact that your pox-ridden ancestors are turning in their graves at your foolishness. It’ll actually help. At least it... might?  

There’s a couple other perks that improve your endurance as well.  


![Whole of Body - Iron Constitution.JPG](https://forumcontent.paradoxplaza.com/public/531843/Whole of Body - Iron Constitution.JPG "Whole of Body - Iron Constitution.JPG")


[Iron Constitution - Disease Resistance (Fertility): +30%, Disease Resistance (Health): Massive Boost]  

Disease Resistance refers to values that are only applied as offsets from disease modifiers. So they won’t have any impact until you get sick, but once you do get sick, it won’t keep you from running around and leaving children everywhere you go. And illnesses won’t drag you into the grave so fast, either.  

Lastly, if you want to improve your survivability even when you’re healthy, just be Healthy!  

![Whole of Body - Healthy.JPG](https://forumcontent.paradoxplaza.com/public/531848/Whole of Body - Healthy.JPG "Whole of Body - Healthy.JPG")


[Healthy - Health: Significant Boost]  

Sometimes the simplest solution is the best.  

Health is not only about the body, however, but also about the mind. I know you guys are really excited to hear more about the details of the Stress system, so... we’re going to leave you wanting for a few more weeks!  

But there are perks that affect that as well:  


![Whole of Body - Carefree.JPG](https://forumcontent.paradoxplaza.com/public/531838/Whole of Body - Carefree.JPG "Whole of Body - Carefree.JPG")


[Carefree - Stress Gain: -25%]  

![Whole of Body - Mental Resilience.JPG](https://forumcontent.paradoxplaza.com/public/531842/Whole of Body - Mental Resilience.JPG "Whole of Body - Mental Resilience.JPG")


[Mental Resilience - Time between Mental Breaks: +3 years]  
“Agh, not knowing what it means is going to give *me* a mental break!!”  

Then, there are two very cool perks, that both come in handy in a more active fashion. The first is:  


![Whole of Body - Restraint.JPG](https://forumcontent.paradoxplaza.com/public/531837/Whole of Body - Restraint.JPG "Whole of Body - Restraint.JPG")


[Restraint - You can take the Embrace Celibacy and Abandon Celibacy Decisions]  

Just imagine! Once your children are starting to amass, you might want to start limiting the pool of competing claimants in the inevitable inheritance dispute, and if a few of your Strong, Genius heirs accidentally get thrown off a roof, you can get started on some new ones again!  

And finally:  


![Whole of Body - Know Thyself.JPG](https://forumcontent.paradoxplaza.com/public/531847/Whole of Body - Know Thyself.JPG "Whole of Body - Know Thyself.JPG")


[Know Thyself - When Death of natural causes is 1 year away, you will receive a warning]  

Yup, you read that correctly. It is actually possible to feel it when your time is approaching. I want to emphasise the “natural causes”, though. Disease and cold steel might still take you by surprise, but if you can survive those, then you can be well-prepared by the time you kick the bucket, precisely to avoid the worst of those aforementioned inheritance disputes.  

The perk from this tree, Whole of Body, is unusual in that it does not affect your skills at all. Instead, it improves your fertility, your health, and reduces stress gain. Let’s just say that someone who finishes the tree will have a hard time getting killed by anything. (Except for murders and executions. Murders and executions are still pretty deadly.)  


**Scholar**  

At long last, the most sophisticated of the perk trees. The one about knowledge and answers, and wisdom for the sake of wisdom. Come with me on this journey into the unknown, where I will reveal to you… more perks?!?  

In the Middle Ages, scholarship was undeniably tied to theology, and that means that being a good believer can aid you in being a good learner.  

![Scholar - Scholarly Circles.JPG](https://forumcontent.paradoxplaza.com/public/531849/Scholar - Scholarly Circles.JPG "Scholar - Scholarly Circles.JPG")


[Scholarly Circles - Learning per Level of Devotion: +2]  

True wisdom is shown in who you surround yourself with, though. So you should surround yourself with servants who are smarter than you are:  


![Scholar - Learn on the Job.JPG](https://forumcontent.paradoxplaza.com/public/531825/Scholar - Learn on the Job.JPG "Scholar - Learn on the Job.JPG")


[Learn on the Job - 20% of Councillors’ primary Skill is added to your own]  

It’s not only your own skills which can benefit from your focus, either:  


![Scholar - Pedagogy.JPG](https://forumcontent.paradoxplaza.com/public/531826/Scholar - Pedagogy.JPG "Scholar - Pedagogy.JPG")


[Pedagogy - Your wards can get additional Skills, and can become your Friends]  

Just imagine taking your neighbor’s child hostage educating your neighbour’s child, and ending up friends instead of enemies!  

There are perks that help you more efficiently develop your realm:  


![Scholar - Planned Cultivation.JPG](https://forumcontent.paradoxplaza.com/public/531829/Scholar - Planned Cultivation.JPG "Scholar - Planned Cultivation.JPG")


[Planned Cultivation - Increase Development in County efficiency: 20%]  

And there are other ways the tree helps you improve as well:  


![Scholar - Scientific.JPG](https://forumcontent.paradoxplaza.com/public/531839/Scholar - Scientific.JPG "Scholar - Scientific.JPG")


[Scientific - Cultural Fascination progress: +100%]  

You’re going to have to wait a while before you get to hear about any of what that modifier means, though. Sorry!  

Other perks are good for making friends outside of your own circles:  


![Scholar - Open Minded.JPG](https://forumcontent.paradoxplaza.com/public/531827/Scholar - Open Minded.JPG "Scholar - Open Minded.JPG")


[Open-minded - Ignore Negative Culture Opinion]  

![apostate.JPG](https://forumcontent.paradoxplaza.com/public/531855/apostate.JPG "apostate.JPG")


[Apostate - Different Faith Opinion: +10, Faith Conversion Cost: -75%]  

Wow, those are some cheap conversions, for when your studious research helps you discover a faith you like better than your own!  

Once you’re an insufferable know-it-all, you can even talk your way into making religious authorities grant you claims in exchange for your hard-earned Piety.  

![Scholar - Sanctioned Loopholes.JPG](https://forumcontent.paradoxplaza.com/public/531832/Scholar - Sanctioned Loopholes.JPG "Scholar - Sanctioned Loopholes.JPG")


[Sanctioned Loopholes - You can use the Buy Claim interaction]  

It doesn’t come cheap, but with this much Piety (and your well-formulated arguments), it doesn’t matter what the Pope says.  

Lastly we have the Scholar trait, which grants a solid boost to Learning, small boosts to Hostile and Personal Scheme power, as well as a modifier to Development Growth in your Counties.  

Knowing stuff comes in handy in a wide variety of ways.  



That’s it for today! Knowledge, religion and long lives-  

Exactly *how* long, you ask? **sigh**  


**Modding: Fine, let’s talk about immortality**  

What follows here is about modding, and is not used by the vanilla game!  

Today I’ve been talking a lot about long lives, but not about eternal lives. Some people really enjoy seeing what their cruel tyrant-queen might get up to age after immortal age, or total conversion mods where magical creatures literally live forever. Well, we haven’t left you out in the cold. We’ve added a simple means for mods to make traits grant immortality, by simply toggling a parameter.  

![immortal parameter.JPG](https://forumcontent.paradoxplaza.com/public/531824/immortal parameter.JPG "immortal parameter.JPG")



Immortality will come out of the box with convenient functionality such as value triggers for "effective age" and "real age", and ways of setting those.  

To be clear, this will not be active for any traits in the vanilla game, but it makes it easy for mods to add it, should they want to.  

Don’t say we never did anything for you!  

Especially not when I return next week with the Diplomacy Lifestyle, and some more tidbits about various related things. We’re almost through our massive Lifestyle rundown, and the next DD will bring some of the most impactful perks seen thus far.  

Until then!  


**PS:**  
A lot of people ask what life as a game developer is. It’s pretty much constant hard work, as you try to fit together an impossibly complicated piece of art on an impossibly tight deadline. But occasionally the game hiccups in fun ways that you’re lucky to get to see. When the character animations started reacting oddly the other day, Peter, one of our UX Designers, saw one of the most important relationships in his life reflected in his in-game marriage:  


![alarm.png](https://forumcontent.paradoxplaza.com/public/531858/alarm.png "alarm.png")


Rest well, everyone!

 

#### Attachments

- [![Whole of Body - Restraint.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531791/Whole of Body - Restraint.JPG)](https://forum.paradoxplaza.com/forum/attachments/whole-of-body-restraint-jpg.544436/)
  
  Whole of Body - Restraint.JPG
  34,7 KB

 · Views: 175

- [![Whole of Body - Mental Resilience.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531790/Whole of Body - Mental Resilience.JPG)](https://forum.paradoxplaza.com/forum/attachments/whole-of-body-mental-resilience-jpg.544435/)
  
  Whole of Body - Mental Resilience.JPG
  32,4 KB

 · Views: 227

- [![immortal parameter.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531792/immortal parameter.JPG)](https://forum.paradoxplaza.com/forum/attachments/immortal-parameter-jpg.544437/)
  
  immortal parameter.JPG
  8,9 KB

 · Views: 182

- [![Whole of Body - Wash Your Hands.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531793/Whole of Body - Wash Your Hands.JPG)](https://forum.paradoxplaza.com/forum/attachments/whole-of-body-wash-your-hands-jpg.544438/)
  
  Whole of Body - Wash Your Hands.JPG
  36,3 KB

 · Views: 177

- [![Theologian - Church and State.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531794/Theologian - Church and State.JPG)](https://forum.paradoxplaza.com/forum/attachments/theologian-church-and-state-jpg.544439/)
  
  Theologian - Church and State.JPG
  28,3 KB

 · Views: 172

- [![Theologian - Faithful.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531795/Theologian - Faithful.JPG)](https://forum.paradoxplaza.com/forum/attachments/theologian-faithful-jpg.544440/)
  
  Theologian - Faithful.JPG
  26,2 KB

 · Views: 173

- [![Theologian - Defender of the Faith.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531796/Theologian - Defender of the Faith.JPG)](https://forum.paradoxplaza.com/forum/attachments/theologian-defender-of-the-faith-jpg.544441/)
  
  Theologian - Defender of the Faith.JPG
  29,1 KB

 · Views: 171

- [![Scholar - Scientific.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531798/Scholar - Scientific.JPG)](https://forum.paradoxplaza.com/forum/attachments/scholar-scientific-jpg.544443/)
  
  Scholar - Scientific.JPG
  28,2 KB

 · Views: 174

- [![Theologian - Apostate.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531799/Theologian - Apostate.JPG)](https://forum.paradoxplaza.com/forum/attachments/theologian-apostate-jpg.544444/)
  
  Theologian - Apostate.JPG
  27,3 KB

 · Views: 178

- [![Theologian - Zealous Proselytizer.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531810/Theologian - Zealous Proselytizer.JPG)](https://forum.paradoxplaza.com/forum/attachments/theologian-zealous-proselytizer-jpg.544455/)
  
  Theologian - Zealous Proselytizer.JPG
  31 KB

 · Views: 167

- [![Scholar - Scholarly Circles.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531806/Scholar - Scholarly Circles.JPG)](https://forum.paradoxplaza.com/forum/attachments/scholar-scholarly-circles-jpg.544451/)
  
  Scholar - Scholarly Circles.JPG
  32,8 KB

 · Views: 166

- [![Whole of Body - Iron Constitution.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531811/Whole of Body - Iron Constitution.JPG)](https://forum.paradoxplaza.com/forum/attachments/whole-of-body-iron-constitution-jpg.544456/)
  
  Whole of Body - Iron Constitution.JPG
  33,9 KB

 · Views: 161

- [![Theologian - Religious Icon.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531812/Theologian - Religious Icon.JPG)](https://forum.paradoxplaza.com/forum/attachments/theologian-religious-icon-jpg.544457/)
  
  Theologian - Religious Icon.JPG
  31,3 KB

 · Views: 170

- [![Scholar - Open Minded.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531813/Scholar - Open Minded.JPG)](https://forum.paradoxplaza.com/forum/attachments/scholar-open-minded-jpg.544458/)
  
  Scholar - Open Minded.JPG
  32,8 KB

 · Views: 166

- [![Whole of Body - Know Thyself.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531814/Whole of Body - Know Thyself.JPG)](https://forum.paradoxplaza.com/forum/attachments/whole-of-body-know-thyself-jpg.544459/)
  
  Whole of Body - Know Thyself.JPG
  35,6 KB

 · Views: 185

- [![Scholar - Pedagogy.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531815/Scholar - Pedagogy.JPG)](https://forum.paradoxplaza.com/forum/attachments/scholar-pedagogy-jpg.544460/)
  
  Scholar - Pedagogy.JPG
  32,2 KB

 · Views: 169

- [![Scholar - Learn on the Job.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531816/Scholar - Learn on the Job.JPG)](https://forum.paradoxplaza.com/forum/attachments/scholar-learn-on-the-job-jpg.544461/)
  
  Scholar - Learn on the Job.JPG
  30,6 KB

 · Views: 166

- [![Fearful Troops.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531817/Fearful Troops.JPG)](https://forum.paradoxplaza.com/forum/attachments/fearful-troops-jpg.544462/)
  
  Fearful Troops.JPG
  32,1 KB

 · Views: 172

- [![Learning Focuses.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531818/Learning Focuses.JPG)](https://forum.paradoxplaza.com/forum/attachments/learning-focuses-jpg.544463/)
  
  Learning Focuses.JPG
  74,2 KB

 · Views: 165

- [![Church and State 2.PNG](https://forumcontent.paradoxplaza.com/thumbnail/public/531808/Church and State 2.PNG)](https://forum.paradoxplaza.com/forum/attachments/church-and-state-2-png.544453/)
  
  Church and State 2.PNG
  101,8 KB

 · Views: 169

- [![Whole of Body - Anatomical Studies.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531807/Whole of Body - Anatomical Studies.JPG)](https://forum.paradoxplaza.com/forum/attachments/whole-of-body-anatomical-studies-jpg.544452/)
  
  Whole of Body - Anatomical Studies.JPG
  33 KB

 · Views: 170

- [![Whole of Body - Carefree.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531805/Whole of Body - Carefree.JPG)](https://forum.paradoxplaza.com/forum/attachments/whole-of-body-carefree-jpg.544450/)
  
  Whole of Body - Carefree.JPG
  30,4 KB

 · Views: 167

- [![Scholar - Planned Cultivation.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531804/Scholar - Planned Cultivation.JPG)](https://forum.paradoxplaza.com/forum/attachments/scholar-planned-cultivation-jpg.544449/)
  
  Scholar - Planned Cultivation.JPG
  34,4 KB

 · Views: 173

- [![Theologian - Clerical Justifications.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531803/Theologian - Clerical Justifications.JPG)](https://forum.paradoxplaza.com/forum/attachments/theologian-clerical-justifications-jpg.544448/)
  
  Theologian - Clerical Justifications.JPG
  30 KB

 · Views: 177

- [![Church and State - No Realm Priest.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531802/Church and State - No Realm Priest.JPG)](https://forum.paradoxplaza.com/forum/attachments/church-and-state-no-realm-priest-jpg.544447/)
  
  Church and State - No Realm Priest.JPG
  29,7 KB

 · Views: 176

- [![Whole of Body - Healthy.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531801/Whole of Body - Healthy.JPG)](https://forum.paradoxplaza.com/forum/attachments/whole-of-body-healthy-jpg.544446/)
  
  Whole of Body - Healthy.JPG
  27,7 KB

 · Views: 174

- [![Scholar - Sanctioned Loopholes.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531800/Scholar - Sanctioned Loopholes.JPG)](https://forum.paradoxplaza.com/forum/attachments/scholar-sanctioned-loopholes-jpg.544445/)
  
  Scholar - Sanctioned Loopholes.JPG
  31,1 KB

 · Views: 173

- [![Theologian - Radiant.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531797/Theologian - Radiant.JPG)](https://forum.paradoxplaza.com/forum/attachments/theologian-radiant-jpg.544442/)
  
  Theologian - Radiant.JPG
  28,7 KB

 · Views: 176

- [![Learning Lifestyle Traits.png](https://forumcontent.paradoxplaza.com/thumbnail/public/531819/Learning Lifestyle Traits.png)](https://forum.paradoxplaza.com/forum/attachments/learning-lifestyle-traits-png.544464/)
  
  Learning Lifestyle Traits.png
  241,9 KB

 · Views: 191

- [![Church and State - No Realm Priest.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531822/Church and State - No Realm Priest.JPG)](https://forum.paradoxplaza.com/forum/attachments/church-and-state-no-realm-priest-jpg.544467/)
  
  Church and State - No Realm Priest.JPG
  29,7 KB

 · Views: 176

- [![Fearful Troops.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531823/Fearful Troops.JPG)](https://forum.paradoxplaza.com/forum/attachments/fearful-troops-jpg.544468/)
  
  Fearful Troops.JPG
  32,1 KB

 · Views: 195

- [![Theologian - Apostate.JPG](https://forumcontent.paradoxplaza.com/thumbnail/public/531831/Theologian - Apostate.JPG)](https://forum.paradoxplaza.com/forum/attachments/theologian-apostate-jpg.544476/)
  
  Theologian - Apostate.JPG
  27,3 KB

 · Views: 195

Last edited: Feb 11, 2020

<!-- artifact:reactions:start -->
- 4 Like
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Voffvoffhunden](https://forum.paradoxplaza.com/forum/members/voffvoffhunden.246161/)**
Role: Rouge Game Dev - Former CK3 Content Designer
Badges: 74
Messages: 261
Reaction score: 1,286

*[Full game-badge icon list of 2 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
