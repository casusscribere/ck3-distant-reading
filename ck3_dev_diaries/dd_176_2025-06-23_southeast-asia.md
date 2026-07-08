---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1802991/"
forum_thread_id: 1802991
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 176
title: "Dev Diary #176 - Southeast Asia"
dd_date: 2025-06-23
author_handle: Distantaziq
expansion: All Under Heaven
patch: null
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 5533
inline_image_count: 27
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1802991'
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
  - type: thread_metadata
    location: raw_lines_142_to_144
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_549_to_554
    action: preserved_and_flagged
    counts:
      Like: 99
      Love: 43
      (unlabeled — rendered as base64 data URI): 2
      Haha: 2
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_562_to_672
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_673_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Dev Diary #176 - Southeast Asia

<!-- artifact:thread_metadata:start -->
- Thread starter [Distantaziq](https://forum.paradoxplaza.com/forum/members/distantaziq.1001649/)
- Start date [Jun 23, 2025](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-176-southeast-asia.1802991/)
<!-- artifact:thread_metadata:end -->

Hello and welcome! I am [@Trin Tragula](https://forum.paradoxplaza.com/forum/members/18587/), one of the design leads at Studio Black. In this third regional feature diary for All Under Heaven, we will be covering Southeast Asia, with a special focus on the new Mandala and Wanua government types and how we will use them to highlight the unique aspects of the region itself. We will also cover the new Great Project feature, as well as how we deal with Tributaries in this expansion; while tributaries were introduced in Khans of the Steppe, they don’t work in quite the same way for these sedentary states.  

---

### The Scene: Southeast Asia in the Middle Ages​

In our timeline, this region was quite different compared to China in the north. It's extremely diverse, with a wide range of faiths and cultures within it.  

![image_01.png](https://forumcontent.paradoxplaza.com/public/1317549/image_01.png "image_01.png")


*[Screenshot of Southeast Asia in the 867 start]*  

In large parts, Southeast Asia is home to a wide range of tribal polities. These are spread over a geographic area that is just as varied, featuring deep river valleys, jungles, and high mountain ranges. In such a place, waterways (seas as well as rivers) are what links peoples to each other, but despite skilled boat builders and sailors, the region presents many challenges in keeping a larger state together.  

Realms in this region have, up until recently, tended to be much more transitory in nature than China, Europe, or even India. The norm here is a looser network of city-states bound together by personal loyalties to popular and powerful rulers; these then break apart after the death of the personality that brought them together.  

![image_02.png](https://forumcontent.paradoxplaza.com/public/1317550/image_02.png "image_02.png")


*[Screenshot of Borobudur]*  

In the Dharmic faiths of India (Buddhism and Hinduism), rulers have found the authority and unifying ideology needed to unite larger realms. They are still centered around great leaders, but with Brahman priests as their allies, they aspire to become living gods: Devarajas.  

The Devaraja concept is built upon the Indian idea of an ideal ruler, someone who rules with the gods' favor. In Southeast Asia, this morphs into the idea that a popular king is actually a god personified himself. Religious ritual and kingship blend in enormous temple cities, where subjects and remote tributaries alike all come together to fund and construct great public works. Monuments can be both religious and expressions of royal power, as giant statues of Dharmic gods carry the face of the very ruler walking among his subjects. The capital temple complex becomes the center of a Mandala, with subservient villages, cities, and tributary kings surrounding it.  

Nonetheless, even the Devaraja realms have a fleeting element. Smaller states may pay tribute to the god-king, but after one dies or a more persuasive one makes themselves known, they can reconsider their allegiance; on the periphery of the Mandala realm, loyalties change quickly.  

Southeast Asia is, as mentioned, a diverse region. Alongside the states like the ones I have described here, there is also the Viet and the Kingdom of Nanzhao (later Dali) that operate quite differently. We covered these in a previous dev diary by [@PDX_Chop](https://forum.paradoxplaza.com/forum/members/1377369/) so we will not talk about those again today, but this introduction would be incomplete without mentioning them.  

I will now hand over to [@Distantaziq](https://forum.paradoxplaza.com/forum/members/1001649/), who will discuss how we have endeavored to portray the region. They’ll detail the mechanics we’ve developed to represent the Mandala realms and the surrounding non-Dharmic tribal realms in All Under Heaven.  

---

### Mandala - the Devaraja Realm​

Greetings! I'm Distantaziq, one of the designers working on *All Under Heaven!*  

Today, we will be exploring the God-Kings and Queens of Southeast Asia -- Mandala! Historically, these governments heavily rely on religion and faith, revolving around the one Mandala ruler who stepped up with the claim to be a divine being.  

![image_03.png](https://forumcontent.paradoxplaza.com/public/1317552/image_03.png "image_03.png")


*[Map of the Kingdom of Angkor in 1066 with tributaries and vassals]*  

From a balancing perspective, the design intent with Mandalas is to present the player with a new challenge. As we will discuss below, Mandalas start out weaker, especially compared to being consistently powerful Feudal or Clan government rulers of comparable size. However, if you overcome the initial difficulties, you work over generations to reach unseen heights of power – as long as you take care not to lose your divinity, and prepare your heir accordingly…  

### Godmode?​

As mentioned, Mandala revolves around faith, and in line with this, Piety will be the Mandala’s main resource.  

Building your first Mandala Capital Temple Complex? Use (mainly) Piety.  
Designating your divine heir? Use Piety.  
Convincing your immediate surroundings that you indeed are a divine being that they should devote their life and kingdoms to? …well. Accumulate Piety.  

And Piety levels!  

![image_04.png](https://forumcontent.paradoxplaza.com/public/1317553/image_04.png "image_04.png")


*[The tooltip for Level of Devotion, featuring additional Piety levels]*  

The Mandala government, being so thoroughly intertwined with faith, religion, and divinity, has unique access to three additional Levels of Devotion: *Divine*, *Demigod* and *Godlike*.  

Now, how do you become Godlike, you might ask? Well, it's simple: It is divinity proven over generations.  

![image_05.png](https://forumcontent.paradoxplaza.com/public/1317554/image_05.png "image_05.png")


*[A truly Godlike Ruler of Angkor]*  

Or more practically put: if your character reaches one of the new Levels of Devotion, your successor gains a buff that allows them to progress to the *next* Level of Devotion, and so on. This can continue until you establish a lineage of godlike characters.  

Oh, and make sure not to die the wrong way in relation to your Aspect. Did you ever hear about that Serenity-Aspect God king who died from a local epidemic? No? I didn't think so.  

![image_06.png](https://forumcontent.paradoxplaza.com/public/1317556/image_06.png "image_06.png")


*[9 levels of devotion in a grid, ranking from Sinner to Godlike]*  

And yes, we do need to showcase some truly decadent art icon renders for this specific feature!  

### A Matter of Temples​

So, what more might a mighty God-King Devaraja possibly need in this world, you might ask? Well, how about temples?  

In All Under Heaven, we’re introducing an additional holding type: the Temple Citadel. This will be the main holding for Mandala rulers, and will also be valid as a capital for most other landed governments (alongside the Castle Holding) in order to ensure it remains viable if the area is conquered by a non-Mandala ruler.  

The Temple Citadel of your capital is the main location for your Capital Temple Complex; a temple with additional defences and a fierce focus on Levels of Devotion, and the foundation for any self-respecting God-King. These Great Buildings are built using the new Great Projects feature, which are collaborative efforts between yourself and your subjects. More on them in a future dev diary!  

The resulting Great Building, or Capital Temple Complex, supports your realm in expanding your domain limit and vassal limit within your Mandala realm, and by increasing your Radiance as a God-King (your ability to attract tributaries and vassals).  

![image_07.png](https://forumcontent.paradoxplaza.com/public/1317557/image_07.png "image_07.png")


*[The building breakdown for the Capital Temple Complex Great Building, complete with 5 levels]*  

Of course, only a Mandala may enjoy the effects of such a building. Should you stop being a Mandala or if the building should come under control of a feudal or tribal heathen, it won’t have much use other than possibly as a tourist attraction.  

![image_08.png](https://forumcontent.paradoxplaza.com/public/1317558/image_08.png "image_08.png")


*[One of the effects of completing the base tier Capital Temple Complex Great Project]*  

Did you just start off as a new Mandala and didn't get the Temple Citadel memo? Well, no Temple Citadel, no problem!  

### What's *Your* Aspect?​

Before even starting the construction of a Capital Temple Complex, the Mandala ruler needs to pick one of four Mandala Aspects. Loosely based on the Hindu god aspects, these Aspects should heavily impact the way you choose to approach your Mandala playthrough.  


- **Creation  
  * Unlocks bonuses to chaining construction and gains piety from child rearing
  * Should primarily pass on through peaceful means**
- **Serenity**
  * Unlocks bonuses to Befriending, as well as including Allies in the Request Contribution interaction
  * Should primarily pass on through peaceful means
- **Destruction  
  * Unlocks additional Casus Belli and bonuses to Military Power
  * May also pass on through combat or certain violent deaths**
- **Trickery  
  * Unlocks additional schemes like Disbelieve Mandala and provided bonuses to certain Schemes (like using Coerce Tributary against someone of a higher tier)
  * May also pass on through being murdered**

As one may note in the breakdown, as well as mentioned in a previous paragraph, you don't just get to die in any way to have your heir be able to level up to the next level of devotion -- a God of Destruction may die on the battlefield and have their existence be canonized, but a God of Trickery dying from being a drunkard? Maybe not so venerable.  

Each of the Aspects also come with their own set of requirements in order to achieve the next level of the aspect. This system, together with your Level of Devotion and Capital Temple Complex Tier feeds into…  

### Mandala Radiance​

Multiple rulers in Southeast Asia claim to be the next Devaraja, asserting their own divinity? Well, how impressive is *your* Temple Complex?  
Mandala Radiance, which indicates your attractiveness and helps you gauge your competition, is unlocked as soon as you have orchestrated the construction of your first tier Temple Complex.  

![image_09.png](https://forumcontent.paradoxplaza.com/public/1317561/image_09.png "image_09.png")


*[Work in Progress mapmode for Mandala, denoting who might accept a Tributarization offer]*  

This Radiance should heavily impact who the minor rulers of the area should want to pledge themselves to. They might even leave their current Suzerain if that ruler is perceived as impious to join a more attractive Devaraja.  

### I Decree…​

Compared to Aspects, Decrees offer a more flexible way of ruling your realm. So, what do you decree, oh Divine Ruler?  

![image_10.png](https://forumcontent.paradoxplaza.com/public/1317562/image_10.png "image_10.png")


[Image of the Mandala Laws window, depicting the Decrees]  

Choose your Decree to primarily affect the current focus of your devotees (or subjects, however you want to call them). Is your current focus Prosperity, Expansion, or Reverence right now? What do you aim to do next?  


### Tributary Status​

A Mandala's main subject will be the tributary. With faith being more relevant than cemented relations via vassalization, this system is intended to give a fairly loose realm setup.  

Mandalas hold less land directly, instead relying mainly on their tributaries. While vassals still *exist* in a Mandala realm, they are more limited here than in other governments. You can also integrate more tributaries as vassals as you expand your Capital Temple Complex. A tributary is unable to engage in factions, has less opinions about what you get up to, and can engage in Tribute Missions to their Devaraja. On the other hand, they also might break away if you turn out not to be as divine as you say or if you treat them badly.  

![image_11.png](https://forumcontent.paradoxplaza.com/public/1317563/image_11.png "image_11.png")


*[A grossly overstepped domain limit]*  

All of this is reflected in lower domain as well as vassal limit, and more tributaries on game start.  

#### War is Not the Answer?​

The emphasis in the Mandala realms is offering alternatives to simply going to war to claim new tributaries or expand your realm and divinity. Subjugation wars, for instance, will generate regular Tributaries instead of piety-granting Mandala Tributaries unless you go heavily into the Destruction Aspect.  

One of these alternatives-to-war is the new scheme Coerce Tributary, which is one of the cornerstones for Mandala play. It is a Political Scheme that looks at your chosen Mandala Aspect and associated skill, then allows you to attempt coercing another ruler to become your Tributary -- that you're the divine ruler they've been waiting for.  

![image_12.png](https://forumcontent.paradoxplaza.com/public/1317564/image_12.png "image_12.png")


*[The Mandala Ruler is anticipating the outcome of the successful Coerce Tributary scheme - events are still Work in Progress!]*  

Beware though; if the Tributary you're chatting up is already a Tributary, then their current Suzerain might incentivize them to stay, or you might even have to fight in order to defend that Tributary as they break away and join your fold.  

![image_13.png](https://forumcontent.paradoxplaza.com/public/1317565/image_13.png "image_13.png")


*[The Suzerain of the targeted Tributary gets the option to intervene in the Coerce Tributary scheme - events are still Work in Progress!]*  

Or you don't help them, which severs their Tributary status and burns your bridge with that particular Tributary.  

![image_14.png](https://forumcontent.paradoxplaza.com/public/1317566/image_14.png "image_14.png")


*[The target of Coerce Tributary was incentivized to stick around, costing the Suzerain a bunch of resources - events are still Work in Progress!]*  

Regardless, you may have gained a new Tributary, but you definitely meddled with their Suzerain's (presumably a competing Mandala ruler) plans.  

---

### Maritime Southeast Asia​

The islands are a virtual petri dish of faiths and cultures. We have very few sources of documentation from the time before larger faiths and realms significantly influenced the cultures and beliefs of the islanders.  

![image_15.png](https://forumcontent.paradoxplaza.com/public/1317567/image_15.png "image_15.png")


*[Screenshot of Maritime South East Asia in 1066]*  

In light of this, we have aimed to add the most prominent ones.  

![image_16.png](https://forumcontent.paradoxplaza.com/public/1317568/image_16.png "image_16.png")


*[Screenshots of the Philippines in 1066]*  

Including small bits of Papua, the lion's share of the maritime Southeast Asian archipelago is featured on the map.  

### Wanua​

This is a heavily sea-based government form, which historically (as mentioned) came under the subject of larger realms and religions. They are still a tribal government type, however, and as such, live under its constraints. If you want to progress further and become more advanced in terms of innovations and development, then you will want to eventually adopt a different style of government.  

As the Wanuas are in the islands of Southeast Asia, a couple of Mandala upstart kingdoms are already available (some which later morphed into more powerful historical kingdoms like Srivijaya or Majapahit after our end date). However, if one desires to embark on the journey from Wanua to a powerful Mandala God-King, then that is entirely possible.  

As long as you either have adopted a Dharmic faith (or worked hard enough to reform your own faith), it is but a simple button press away, granting you access to islands that are ripe for the picking…  

![image_17.png](https://forumcontent.paradoxplaza.com/public/1317570/image_17.png "image_17.png")


*[A screenshot of the Adopt Mandala Rule Decision for the Wanua Rulers]*  

In addition to the cultural flavor, Wanua will be able to traverse the sea and raid, naturally. We are also looking into more ways of making the Wanua feel special and fun to play; for example, being more dependent on Legitimacy (which they would receive from being Mandala Tributaries).  

---

### Great Projects​

Another addition with *All Under Heaven* is the Great Projects feature! This allows several rulers to come together and fund various parts of projects that would be very expensive or take ages to fund individually.  

![image_18.png](https://forumcontent.paradoxplaza.com/public/1317571/image_18.png "image_18.png")



### The Mandala Great Project​

For Mandala, the Capital Temple Complex is such a project; a physical manifestation of your spiritual might where your followers may come to pay tribute or simply worship you. The temple comes in 5 tiers, and once you have completed the first tier you have officially started your path towards godhood (should you manage to defend it, of course).  

#### Mandatory Contributions​

Each tier requires a specific set of contributions that you or any of your subjects may fund; depending on who funds it, that specific ruler gains the spoils of such a benevolent act, as well as the appreciation of the founder (in this case you).  

![image_19.png](https://forumcontent.paradoxplaza.com/public/1317572/image_19.png "image_19.png")


*[Work In Progress Great Project window featuring the Contributions of a Mandala Capital Upgrade]*  

#### Optional Contributions​

There are also optional contributions, for those who absolutely must have that golden dome, that yield additional rewards for the contributor.  

#### Request Contribution​

If you are just starting off on your Mandala journey or your subjects for one reason or the other needs an additional nudge in order to actually contribute those archways to your project, there's also the Request Contribution button.  
Inside, you may be able to incentivize their request via hooks, bribes, forcing them with your oppressive pious spirit - whatever might convince them to make the right call.  

Once you have completed the final tier -- an achievement likely spanning generations -- you will have proven yourself an established Devaraja ruler and will receive huge bonuses to your Mandala way of life.  

### Chinese Great Projects​

In China, the great projects are more focused on large-scale infrastructure and other improvements that require several contributors; examples include building sections of the Great Wall or improving the Grand Canals.  

These projects allow the Emperor to either contribute significantly on his own, displaying his might and benevolence as the Son of Heaven, or they present an opportunity for ambitious subjects vying for the imperial graces…  

![image_20.png](https://forumcontent.paradoxplaza.com/public/1317573/image_20.png "image_20.png")



Another opportunity for benevolent actions that improve your own standing is provided by the Great Projects that spawn from Natural Disasters. While Natural Disasters may spawn in geographically turbulent areas all over the map, only those in China will affect the Dynastic Cycle and potentially impact the Emperor’s standing, depending on how they deal with it. More on Natural Disasters and their implications for the Dynastic Cycle will be covered in a future Dev Diary.  

Needless to say, this feature opens up significant opportunities for modding and new additions; not only grand buildings, but great feats of humanity which can be showcased for generations to come!  

---

### Tribute Missions​

Both Mandala and Hegemonic tributaries may go on Tribute Missions to their Suzerain, primarily to strengthen their own Legitimacy, but also to partake in the wealth and grandeur typically associated with their Suzerain.  

### Mandala Tribute Missions​

Historically, the act of paying tribute was often both a matter for states and a very direct personal action, with one ruler acknowledging another as their better and bringing them a gift to prove this. The fact that one party considers the other their suzerain does not mean that there cannot be reciprocity however; in return for paying tribute, the tributary might gain benefits at home (they appear as a more rightful King due to being acknowledged by a more powerful Suzerain) or even receive gifts to bring back home (essentially a form of trade).  

Since the passive payment of a resource over time does not quite cover the interpersonal aspects of a relationship like this, we have added what we call Tribute Missions to be used for tributaries of the more voluntary types that you see in East Asia. To preserve these relationships, at least one such tribute needs to be undertaken per Suzerain's lifetime.  

The Pay Tribute missions start off with a Decision which allows you to determine what tribute you want to bring, and types vary depending on the Suzerain. For example, if they utilize Eunuchs (like the Chinese Admin government) you may gift a Eunuch. If they have concubines (again, like the Chinese Admin government) you may gift a concubine. Standard tributes of Gold or Herd (if you're a Nomad tributary) are always available.  

![image_21.png](https://forumcontent.paradoxplaza.com/public/1317574/image_21.png "image_21.png")


*[Image of the Select Tribute character interaction for a Hegemonic Tributary]*  

Once you’ve decided what kind of tribute you’re offering, you set off on a journey towards your Suzerain's capital! Upon arrival, you are greeted by the Suzerain (if they have a Royal Court, you are received at the Court), where you exchange gifts. First, the Suzerain receives your gift, and you may attempt to influence what the reward will be - or you leave it up to the discretion of the Suzerain.  

Similar to the type of tribute being offered, the type of reward the Suzerain may choose between vary depending on if you're a Mandala or the Emperor - a handful of options might be to:  


- Award them with additional Trade Posts that increases the development of the Tributary's capital
- Award them with an artifact for them to bring back and display to their people
- Award them with a monk, to mend their heathen ways (for Mandalas to give to their tribal tributaries who are still unreformed)

You start traveling back home once you’ve received your reward, eager to showcase the gift and enjoy the legitimacy you received from your tribute. Now I will hand the word over to [@lachek](https://forum.paradoxplaza.com/forum/members/669315/), who implemented the Hegemonic / Celestial Tributary types.  

### Hegemonic Tribute Missions​

Hello again! [@lachek](https://forum.paradoxplaza.com/forum/members/669315/) here, and I'm excited to once more discuss Tributaries with you! As mentioned above, tributaries were first introduced into Crusader Kings III to support nomadic gameplay with Khans of the Steppe, where they modeled the unique subject-overlord relationship between a tributary and their suzerain. On the vast expanse of Northern Asia, nomadic tributary relationships were mostly held together through military domination, either implied or by actual display of force. Nomadic rulers can demand that neighboring realms fall in line under them by building up a sizable horde, or simply go out and enforce it through warfare. Through a cascade of such relationships, enormous swathes of the plains can be held together under a single suzerain. However, they can collapse just as quickly due to migratory patterns or a foreign conqueror cutting off a key part of the chain.  

We also implemented a Subjugated Tributary type available outside the steppe to represent rulers dominated by more powerful neighbors and made to pay tax to their overlord.  

However, none of those types adequately represent how tributary relationships functioned in either Southeast Asia or China. Therefore, we are introducing both Mandala tributaries and the Hegemonic/Celestial types (more on the distinction later), where the relationship is more contingent on one-sided respect and a gift economy.  

#### Celestial Tributaries​

These are realms within China's sphere of influence that recognize the Emperor as the Son of Heaven and pay him a great deal of personal respect (not to speak of material wealth). In return, they are granted recognition and sovereignty by China. Unlike tributaries on the steppe, this is not primarily a military arrangement but rather a one-sided show of deference, ultimately serving both parties in the end.  

This relationship can be established by either party through character interaction, but is typically initiated by the prospective tributary themselves. Once established, the tributary has few immediate obligations: a little bit of Prestige and perhaps some Gold, in exchange for which some of China's Legitimacy is conferred upon them. It's usually a beneficial arrangement for both parties, especially since any taxes paid by the tributary goes directly into the Emperor's personal coffers rather than into the treasury. This makes it one of the few sources of direct income the Emperor has available for his own discretionary projects. Over time, the Emperor may decide to impose further standing obligations on some of their tributaries. Any increase in taxation or prestige transfer also comes with closer ties to China, however, thereby increasing legitimacy for the subject.  

However, Celestial Tributaries are also expected to Kowtow to the Son of Heaven on a regular basis, bringing immense riches and gifts with them to reaffirm their deference and respect. This is fundamentally the same kind of Tribute Mission as in Mandala realms, with a few modifications. Unlike in Mandala realms, the Chinese Emperor always has some minimum expectation regarding the size of tribute, depending on the esteem in which the tributary is already held. This is tracked by a metric we call Imperial Grace, which serves several purposes:  

- It acts as a timer on how frequently you are expected to pay tribute; if you're only able to bring the bare necessities and wait until the last moment to reaffirm your respect, the Emperor might start to demand more frequent visits. Highly successful missions give you a longer grace period until your presence is once again expected.
- It gives you an opportunity to adjust your relationship depending on what kind of tributary you want to be. Do you pay only nominal respect when absolutely required, just so China will overlook you when assessing their borders? Or are you a devoted subject looking for a closer relationship?
- The decay rate of Imperial Grace increases during unstable periods of the Dynastic Cycle, reflecting the uncertainty of these times. Will you contribute to sustaining the ruling dynasty of China's legitimacy during troubles times, or seize on this moment to break the agreement and try to claim a piece of the pie for yourself?
- As a Celestial Tributary you can quite readily adjust your own tributary contract's obligations, but changing it in your favor costs an amount of Imperial Grace.

Finally, at very high levels of Imperial Grace, the Emperor might decide to make China's relationship with its subject more permanent through the granting of a Seal of Investiture. This is an enduring artifact (regalia type, which can be reforged into a court artifact if you wish) that gives access to special privileges not usually available to subjects of China.  

**Trade Access**: This privilege grants the tributary access to the domestic markets of the Chinese capital, resulting in a gradual closing of the development gap between the two realms' capital provinces. A low-development tributary enjoying this privilege could potentially propel itself to wealth and power compared to their less privileged neighbors within a few generations.  

**Family Access**: This privilege negates the usual high acceptance maluses for marrying into the Chinese imperial dynasty, and even grants a small bonus to such dynastic intermingling.  

**Palace Access**: This privilege lets the tributary's representatives roam the palace grounds, rubbing shoulders with ministers, governors, and sages in the seat of power. Tributaries with this privilege become active participants in the Dynastic Cycle and can join political movements to shape the future of China.  

Once you have gained a Seal of Investiture, these become available as new contract privileges that you can activate in exchange for a one-time cost of Imperial Grace. This doesn't make the tribute missions redundant, however. The size of the bonuses you get from these scales with the degree of Imperial Grace you currently possess, so sustained tribute will only make your relationship with China more powerful.  

It is important to note that a Celestial Tributary contract is a formal agreement between a realm and the Chinese Emperor. The contract is inherited upon death of either the tributary or the suzerain, but if the Hegemony title is lost then the contract will break -- even if another claimant dynasty later restores it. As long as the dynastic line is unbroken, however, accumulated Imperial Grace and the privileges that the contract yields can be maintained for centuries.  

You may have noted I’ve made a distinction between Hegemonic and Celestial Tributaries above. A Celestial Tributary is a type of Hegemonic Tributary, specific to China. However, other hegemony titles (e.g. India or restored Rome) can also maintain Hegemonic Tributaries that share many similarities with Celestial ones. Instead of Imperial Grace these contracts have Subject Standing. They do not use the Seal of Investiture mechanic with its tie-ins to China-specific mechanics like difficult dynastic intermarriage or the Dynastic Cycle situation, but most other aspects of the contract work in similar ways with the same dynamics. This allows Hegemony-tier titles to use the tributary mechanic not only to expand their own de facto tracts of land, but also to accept recognition and deference from select surrounding realms they find useful to their larger strategy.  

### Moddability​

I'll conclude this with a final note to modders. The Hegemonic/Celestial variants of tributary types now marks five distinct types I've implemented in Crusader Kings III (with Mandala tributaries being a sixth variant in All Under Heaven's release). I'm continually amazed at how flexible this system truly is in allowing you to model different types of relationships between realms that look nothing like a feudal liege/vassal system.  

Anything from simple non-aggression between two specific rulers to long-standing extractive domination is possible, with the one caveat that it must always have an implied power imbalance. With the addition of Subject Standing, which tracks relationship strength over time and can theoretically be applied to any subject contract (including your typical vassal contracts, if so desired), there's a lot of fertile ground to represent entirely novel types in your own mods, be they focused on more granular historical accuracy or total conversions. So go wild!  

And here we are handing the microphone back to [@Trin Tragula](https://forum.paradoxplaza.com/forum/members/18587/), who will have another look at the map.  

---

### Map Corner​

As we did last time, we will conclude with a short overview of the map area relevant to this diary. Southeast Asia looks rather different in 867, 1066, and 1178, so for this I will be using a mix. If you are curious about anything in particular that I have not shown off feel free to ask us in the comments.  
Like everything else shown in this diary, this is a work in progress, but we would love to hear your feedback on the things we’ve covered so far.  

![image_22.png](https://forumcontent.paradoxplaza.com/public/1317575/image_22.png "image_22.png")


*[Faiths 867]*  

As was mentioned in the introduction, Southeast Asia has quite a complex mix of faiths and religions. We have tried to represent a reasonable amount of this variety, while also generalizing to avoid having overly small micro-faiths at the start.  

Already by 867, Hinduism and Buddhism in various forms are dominant in large parts of this map, but older indigenous faiths are also present both on the mainland and the islands.  

![image_23.png](https://forumcontent.paradoxplaza.com/public/1317576/image_23.png "image_23.png")



When it comes to cultures, the region is even more diverse in many ways. Notably, the Tai peoples are still found mostly in its northern parts. Historically, offshoots from this group would come to be politically dominant in many parts of the mainland, from modern Laos and Thailand, to Assam in northern India (the area labeled “Kamrupi” on this map).  

Striking a balance between having too many or too few cultures from a gameplay point of view is never easy, but in this part of the world it is perhaps particularly hard. What we show here is both more simplified and more balkanized than we usually aim for.  

![image_24.png](https://forumcontent.paradoxplaza.com/public/1317577/image_24.png "image_24.png")



This is a screenshot of the political situation in 1066, with the Song empire looming over the region in the north. The Srivijaya Empire (which was alive and well in the initial screenshot at the beginning of this diary) has been shattered by a relatively recent Chola invasion from India.  

![image_25.png](https://forumcontent.paradoxplaza.com/public/1317578/image_25.png "image_25.png")



A quick overview of the Duchy mapmode. Many of these are not yet created on game start, as small realms prevail in Southeast Asia. Where other regions have a number of powerful dukes under their Kings, this region often sees duchies divided up between individual tributaries instead.  

![image_26.png](https://forumcontent.paradoxplaza.com/public/1317579/image_26.png "image_26.png")


*[De jure kingdoms in 867.]*  

![image_27.png](https://forumcontent.paradoxplaza.com/public/1317580/image_27.png "image_27.png")



Last but not least, these are our de jure empires for the region! Nusantara may look big, but in terms of counties, it is not actually as enormous as it might seem. Not all parts of these islands are places with established states (i.e., counties) and the inland can often be impassable in places like Borneo or Papua.  

---

That was all we had this time! This diary is also the last one before our summer break, but dev diaries will resume in early August. Until then we will of course still be attentive to the feedback you have provided to our diaries so far (including this one).

 

Last edited by a moderator: Jun 24, 2025

<!-- artifact:reactions:start -->
- 99 Like
- 43 Love
- 11 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
- 2 Haha
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Distantaziq](https://forum.paradoxplaza.com/forum/members/distantaziq.1001649/)**
Role: The Godless One
Badges: 7
Messages: 190
Reaction score: 484

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
