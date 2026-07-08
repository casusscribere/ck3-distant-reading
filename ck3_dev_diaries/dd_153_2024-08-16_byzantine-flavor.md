---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1699607/"
forum_thread_id: 1699607
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 153
title: "Dev Diary #153 - Byzantine Flavor"
dd_date: 2024-08-16
author_handle: chaddling
expansion: Roads to Power
patch: Patch 1.13
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 5283
inline_image_count: 36
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1699607'
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
    location: raw_lines_~28_to_152
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_151
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3219.jpg?1723804495
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_154_to_156
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_681_to_685
    action: preserved_and_flagged
    counts:
      Like: 126
      Love: 106
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_693_to_807
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_808_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3219.jpg?1723804495)
<!-- artifact:thread_banner:end -->

# Dev Diary #153 - Byzantine Flavor

<!-- artifact:thread_metadata:start -->
- Thread starter [chaddling](https://forum.paradoxplaza.com/forum/members/chaddling.1717140/)
- Start date [Aug 16, 2024](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-153-byzantine-flavor.1699607/)
<!-- artifact:thread_metadata:end -->

*Note: You can also listen to today's Dev Diary [here on our YouTube channel!](https://www.youtube.com/watch?v=8JgCqhbn_g0)*  

---

Χαῖρε! I’m Chad, a game designer here on the CK3 team. Today, I’ll be walking you through some highlights of what we’ve added in terms of Byzantine flavor in Roads to Power.  

Some cursory but important notes to begin our discussion:  


- These images may be works in progress. We are still working away at polishing *Roads to Power* to provide the best experience possible.
- Yes, I will refer to Byzantium as Byzantium in this dev diary. I know that the endonym is more properly the Roman Empire, but it’s our policy to not use endonyms in the game. Those of you who have strong opinions about this get a special game rule to rename Byzantium with several options.

Without further ado, let’s get into it!  

---

### Flagship for Administrative Government​

Byzantium has been our main point of inspiration and the impetus for Administrative Government. We outlined this in the two previous dev diaries on Admin, but I wanted to discuss this in a bit more detail.  

Essentially, all the content we’ve made for Administrative Government has been designed with an eye towards Byzantium as the model. This doesn’t mean that this content can’t appear if playing as a different admin realm. Far from it.  

What it does mean is that all the content you encounter while playing as Byzantium should feel tailored and appropriate to the context. There is alternative text for other admin realms. So fret not, we haven’t siloed all the content to a single empire. Playing admin should generally feel different and exciting, but playing as Byzantium should feel *special*.  

---

### Improved Cultural Traditions​

We’ve revamped Greek Cultural Traditions and added special integrations with Admin Government and the other unique aspects of the DLC. In the descriptions below, you’ll undoubtedly find references to features and concepts that we haven’t yet discussed, but will be discussed either later in this or a future dev diary.  

![image-01-02.png](https://forumcontent.paradoxplaza.com/public/1166872/image-01-02.png "image-01-02.png")


*[Palace Politics & Cultural Traditions]*  

In addition to this gorgeous new art, we’ve added loads of integrations with new content exclusive to *Roads to Power*. Palace Politics is a great example. Not only does it unlock the new Varangian Guards Men-at-Arms type and the Akolouthos Court Position, but also incorporates several unique bonuses to demonstrate the Greek affinity for Administrative Government.  

Maiming and disfiguring characters was a primary way to take your political opponents out of the running in the Byzantine political milieu, and we’ve reflected that here with reduced monthly Influence.  

We’ve added unique bonuses to Greek characters for scheming. Not only do they get special bonuses to a new type of Scheme Countermeasure, but they can also execute Political Schemes faster.  

Political Schemes are a new category of Schemes that we’ve added as a central aspect to the Administrative Government experience. I’ll go into more detail about this, but suffice it to say that you can’t play in Byzantium without engaging with these new Schemes.  

And of course, your Chief Eunuch will be a major player. We’ve added a new trait, called Beardless Eunuch, to differentiate characters castrated as children from characters who were castrated as adults.  

![image-03-04.png](https://forumcontent.paradoxplaza.com/public/1166873/image-03-04.png "image-03-04.png")


*[Beardless Eunuch Trait & Eunuch Scheme Agent Type]*  

As you can see, these characters also affect Influence. They are generally disliked by other vassals in the realm because they make for *excellent* Scheme Agents in Political Schemes.  

Roman Ceremonies contains a slew of new features for Byzantium, including access to the Hold a Triumph Decision, the Chariot Race Activity and its associated Court Positions, and a new type of Diarchy called a Duumvirate.  

![image-05-06.png](https://forumcontent.paradoxplaza.com/public/1166874/image-05-06.png "image-05-06.png")


*[Imperial Tagmata & Cultivated Sophistication Cultural Traditions]*  

Imperial Tagmata unlocks the Byzantine Men-at-Arms discussed in the next section, but also provides some unique bonuses that are useful for Administrative realms.  

This Cultural Tradition allows Governors with the Frontier Administration type to borrow Title Men-at-Arms from non-Frontier neighbors in the realm. They also get an additional Title Men-at-Arms Regiment slot and a bonus to their Heavy Cavalry Regiment maximum size.  

Cultivated Sophistication provides a variety of Culture-related effects in addition to granting Development from building Estate Buildings. Moreover, it allows House Heads to adopt characters into their House.  

---

### New Men-at-Arms Types​

The Varangian Guard  


![image-07-08.png](https://forumcontent.paradoxplaza.com/public/1166875/image-07-08.png "image-07-08.png")


*[Varangian Guards Men-at-Arms and the Decision to Found the Varangian Guard]*  

The Varangian Guards Men-at-Arms type is now available to the Emperor of Byzantium as Title Men-at-Arms. This means they can only be recruited for the Byzantine Empire Title. Furthermore, you can’t recruit them right off the bat if you start in 867. You must take the Found the Varangian Guard Decision first.  

#### Akolouthos Court Position​

To head up these new Men-at-Arms is a brand new Court Position: the *Akolouthos*. Historically, this was an office in the imperial palace tasked with overseeing the Varangians. An *Akolouthos* with good Aptitude will increase Heavy Infantry Toughness of your Men-at-Arms overall and make Characters with the Varangian trait both more common and better at being Bodyguards.  

![image-09.png](https://forumcontent.paradoxplaza.com/public/1166876/image-09.png "image-09.png")


*[Akolouthos Court Position filled by Glum]*  

### Byzantine Men-at-Arms​

Aside from the Varangian Guard, we have added 3 new Men-at-Arms types for Greeks which are unlocked by the Imperial Tagmata Cultural Tradition.  

![image-10-11-12.png](https://forumcontent.paradoxplaza.com/public/1166877/image-10-11-12.png "image-10-11-12.png")


*[Akritai, Skoutatoi, and Ballistrai Men-at-Arms Types]*  

### Additional Men-at-Arms​

Additionally, we’ve added Ayrudzi for Armenians and Conrois for the Normans.  

![image-13-14.png](https://forumcontent.paradoxplaza.com/public/1166878/image-13-14.png "image-13-14.png")


*[Ayrudzi and Conrois Men-at-Arms Types]*  

---

### Bureaucracy Dynasty Legacy​

An expansion wouldn’t be complete without a new Dynasty Legacy. This time, we’ve created one specifically for characters with Administrative Government.  

![image-15.png](https://forumcontent.paradoxplaza.com/public/1166883/image-15.png "image-15.png")


*[Art for the new Bureaucracy Dynasty Legacy]*  

All of these perks buff how well you can play within an Administrative Realm. Unlocking perks will propel your family forward whether you are aiming for the imperial throne or you wish to pull strings from the shadows of your Estate.  

![image-16.png](https://forumcontent.paradoxplaza.com/public/1166885/image-16.png "image-16.png")


*[Effects of Bureaucracy Dynasty Legacy Perks]*  

You’ll notice that two of these perks unlock unique Estate upgrades, namely the Reception Hall and the Cabinet of Curiosities. These are special internal Estate upgrades that provide powerful bonuses for your House members.  

The Reception Hall provides Legitimacy to House Members who accede to the imperial throne. For every Feast or Grand Wedding that House Members host in the Barony where the House’s Estate is located, the counter on this internal building increases. Once a House Member wins the Acclamation Succession and becomes the Emperor, the counter resets.  

![image-17.png](https://forumcontent.paradoxplaza.com/public/1166886/image-17.png "image-17.png")


*[Description and Effects of the Reception Hall internal Estate upgrade]*  

Upgrading this internal building decreases the Legitimacy counter lost whenever a House Member becomes Emperor and increases monthly influence gain for the Estate owner.  

The Cabinet of Curiosities, on the other hand, provides opportunities based on how many Artifacts the Estate owner puts on display. Once an artifact has been added to the Estate, it is irretrievable and only contributes to the quality of the Cabinet of Curiosities building.  

![image-18-19.png](https://forumcontent.paradoxplaza.com/public/1166887/image-18-19.png "image-18-19.png")


*[Hall of Wonders (Cabinet of Curiosities Level 2) Effects & Contributed Artifacts Breakdown]*  

The image above shows the second level of the Cabinet of Curiosities, which is available after you have contributed enough artifacts so the quality level is 15 or higher. You can see the breakdown of scores below. Essentially, the higher quality the Artifact is, the greater it boosts the quality of the Cabinet of Curiosities.  

Upgrading this internal Estate building makes it cheaper and easier to attain higher quality Artifacts and allows you to request Artifacts from other House members. The more you upgrade this building, the more bonuses you receive to your Stewardship and Learning skills as well as your Renown and Influence gains.  

Finally Bureaucracy Dynasty Legacy unlocks the Order Mass Arrests Decision, which I’ll let you discover for yourselves upon release.  

---

### Political Schemes​

As we mentioned in the dev diaries about Administrative Government, we’ve created a new category of Schemes called Political Schemes which are available to characters with Administrative Government. Byzantium, and by extension, Administrative Realms, should be much more about Intrigue and Scheming than War. In these realms, palace politics and backhanded trickery reign supreme.  

For example, at some point you’ll want to run a smear campaign against one of your political rivals. You can do that now with the Slander Scheme.  

![image-20.png](https://forumcontent.paradoxplaza.com/public/1166888/image-20.png "image-20.png")


*[The Emperor schemes to slander the reputation of one of his vassals]*  

If successful, this Scheme lowers the Target’s Candidate Score for Acclamation (to be the Basileus) and Appointment (to be a Strategos) Successions in the Realm and lowers their Governor Efficiency by 5% for 10 years. This combo makes them a much less desirable candidate for any position.  

Another Scheme you’ll definitely want to try out is Raid Estate, in which you attempt to successfully stage a raid against another Noble Family’s Estate.  

![image-21.png](https://forumcontent.paradoxplaza.com/public/1166889/image-21.png "image-21.png")


*[A Noble Family Head schemes to raid a fellow vassal’s Estate]*  

Of course, it’s imperative that this kind of activity remains under the radar or there will be consequences. The potential rewards, on the other hand, are quite large: Gold for yourself and fewer political rivals from the other Noble Family. Disrupting your political rival’s base of operations can prove quite fruitful.  

With plenty of these new Political Schemes in addition to a veritable buffet of new Character Interactions, you’ll have all the tools you need to plot and scheme your way to power in Byzantium.  

---

### Chariot Racing Activity​

Byzantium would not be complete without a Chariot Racing Activity and beautiful new art for the Hippodrome. Period. Sure, the sport wasn’t at the peak of its popularity during the High Middle Ages, but it is part and parcel of the Byzantine experience. So we’ve added it.  


### Intents​

We’ve also added a few custom Intents for this Activity that better fit its historical and political context. The default Intent will always be to Increase Influence, but you may want to choose Appease the Populace if your Popular Opinion is low. Of course, there are a variety of traditional Intents to choose from.  

Of course, you’ll need to be wary. Activity Guests have an additional Intent option to Sow Discord which aims to reduce the Popular Opinion of the current Emperor and sabotage their County Control.  


### Place Your Bets​

At the very beginning of the Chariot Race, you’ll have the opportunity to place a wager on the Charioteers competing in that day’s competition. You’ll see representatives here in a unique interface from the four traditional teams of the Hippodrome: the *Venetoi* (Blues), the *Prasinoi* (Greens), the *Leukoi* (Whites), and the *Rhousioi* (Reds). You can easily see which character is your own Champion Charioteer from the icon next to their name.  

![image-22.png](https://forumcontent.paradoxplaza.com/public/1166890/image-22.png "image-22.png")


*[Choosing a team to place a wager on during a Chariot Race Activity]*  

You’ll be approached by the Emperor’s Bookmaker, a new Court Position added in this DLC, and they will ask if you’d like to place a wager. You then have a series of choices:  

1. Which team would you like to place your wager on?
2. Would you like to place your wager on a specific member of the team or hedge your bets and bet on the team as a whole?
3. What type of wager would you like to place?
  1. Win - The character or team will come in First Place
  2. Place - The character or team will come in First or Second Place
  3. Show - The character or team or will come in First, Second, or Third Place

You may well want to place a wager on your own Charioteer if you’ve brought them along! Be wary, though, for if they perform poorly, you’ll gain stress. There are also chances to steal another attendee’s Champion Charioteer if you do not already employ one.  


### Charioteer Court Position​

Every Landed and Landless title holder with the Roman Ceremonies Cultural Tradition has access to the new Champion Charioteer Court Position. If hired, these characters will travel with you to Chariot Races and compete on your behalf.  

![image-23-24.png](https://forumcontent.paradoxplaza.com/public/1166891/image-23-24.png "image-23-24.png")


*[Champion Charioteer Court Position & Charioteer Trait]*  

Every Charioteer is assigned a Charioteer Trait indicating which team they’re on and how much experience they have competing. The more experience they have, the better they are.  

If you want to train up your Charioteer in between races, which can happen every 10 years in game, you can work on upgrading your Stables Estate Building. It has a special track which unlocks a new Court Position Task for the Charioteer, enabling them to gain trait experience outside of the Chariot Race Activity.  

![image-25.png](https://forumcontent.paradoxplaza.com/public/1166892/image-25.png "image-25.png")


*[Charioteer Training Grounds Estate Building]*  

![image-26.png](https://forumcontent.paradoxplaza.com/public/1166893/image-26.png "image-26.png")


*[Charioteer Training Court Position Task]*  

### Politicking​

Before the race begins, you’ll have some opportunity for politicking and rubbing shoulders with other important people in the realm, depending on your stature. You only get to sit in the *kathisma*, the imperial box, if the Emperor invites you as his Guest of Honor.  

![image-27.png](https://forumcontent.paradoxplaza.com/public/1166894/image-27.png "image-27.png")


*[Event where the Emperor may decide to invite an additional guest into the kathisma]*  

### The Race​

Then begins the actual race – what everyone’s come to see. This always begins with the Emperor’s address, which provides special options based on Activity Intent and current situation.  

![image-28.png](https://forumcontent.paradoxplaza.com/public/1166895/image-28.png "image-28.png")


*[Event beginning the Chariot Race where the Emperor decides how to frame his opening address]*  

You can track the Charioteers and their place via the new UI element on the side of the Activity window. And, of course, we’ve added chariot animations complete with horses, which are also available in the Barbershop.  

![image-29.png](https://forumcontent.paradoxplaza.com/public/1166896/image-29.png "image-29.png")


*[Event in a Chariot Race where one charioteer passes another]*  

But now… an interlude on what happens when you have *two* Emperors at the helm from my beloved colleague [@Wokeg](https://forum.paradoxplaza.com/forum/members/1325927/) !  

---

### Duumvirates​

I’ll bet you thought you were safely out of the Wokeg info dump mines, didn’t you? You’re never safe. Not from my word vomit.  

Let’s talk co-emperors.  

![image-30.png](https://forumcontent.paradoxplaza.com/public/1166897/image-30.png "image-30.png")


*[Byzantium has historical co-emperors in both 1066 & 1178]*  

### Co-Emperors? The Emperor does not share power!​

You’d be surprised.  

Yes, the Roman Empire was very much an autocracy from Augustus onwards, and by the medieval period, that autocracy had decided *fairly* thoroughly that power rested entirely in and flowed exclusively from the emperor, but the key word there is “emperor”, not “the”.  

If it’s the position of emperor that is in charge, you simply appoint a second emperor. A slightly more junior emperor to the other emperor, but they’re *both* in charge. One is just a little more in charge than the other.  

This addresses who the next emperor will be (Emperor A is dead, but Emperor B is still emperor), mollifies powerful pretenders, or even just gives your child some practical experience of rule.  

It’s also an absolute recipe for petty personal conflicts, drama, civil wars, and comes with the *delightful* incentive to murder the other emperor in pursuit of indisputed power.  

If you’ve ever wondered why the Byzantines have such a reputation for civil wars and intrigue, well, personally, I’d peg this practice as a major contributor.  

### Co-Rule in CKIII​

So, the challenge here was to model something that caused Byzantium a lot of problems, but also make it fun.  

We settled on a type of diarchy focused around settling the question of your succession, grooming your heir, and farming influence. In exchange, you get a diarch that can be helpful but who may, over time, grow too big for their boots and decide to take drastic action.  

We’re introducing three new diarchies to represent this:  


- Duumvirates
- Nominal Duumvirates
- Co-Monarchies
… of these, duumvirates are a full-sized diarchy, whilst the other two are much smaller goals-focused diarchies for niche situations.  

These diarchies are grouped together as co-rulership. Co-rulers do not have diarchy inheritance — when a co-ruling diarch dies, the diarchy ends — and cannot be ended forcibly except by the death of one of the involved parties (or maiming for some, which we’ll get onto).  

Making someone your co-ruler always makes them your designated heir, provided they are of your dynasty.  

#### Loyalty​

Co-rulers take their loyalty first and foremost from how likely they are to inherit soon.  

![image-31.png](https://forumcontent.paradoxplaza.com/public/1166898/image-31.png "image-31.png")


*[A co-emperor much younger than you receives a substantial loyalty boost]*  

They’re happier the greater the age gap. Conversely, if you have a co-ruler for decades, they’ll start to get more and more annoyed with you not dying. We track both the years count for this, and how healthy you are vs. your age.  

![image-32.png](https://forumcontent.paradoxplaza.com/public/1166899/image-32.png "image-32.png")


*[Being unduly healthy, starting in your 50s and scaling up to your 90s, will cause a co-ruler to get progressively less loyal to you]*  

#### Nominal Duumvirates​

Sometimes, you’re just looking to help secure the succession. Though appointing one of your infant children co-emperor isn’t a silver (sling) bullet ensuring they’ll win the purple, it does help quite a lot. Such a child can’t really wield any *true* power, but they can start growing accustomed to the ceremonies of rule.  

Nominal co-emperors have access to no Borrowed Powers. Instead, as the Scales of Power swing towards them, they become more cost-efficient to promote for Administrative offices and earn progress towards base skill points granted when they come of age.  

![image-33.png](https://forumcontent.paradoxplaza.com/public/1166900/image-33.png "image-33.png")


*[An emperor names one of his children as nominal co-emperor]*  

Basically, the more power they have when they hit 16, the more skill bonuses they get from their apprenticeship as emperor.  

The older a nominal co-emperor gets, the more the natural resting point of the Scales of Power will swing towards them. To hurry the process, you may voluntarily cede authority to them.  

When your little partner reaches adulthood, the diarchy type is immediately converted over to a true Duumvirate.  

![image-34.png](https://forumcontent.paradoxplaza.com/public/1166901/image-34.png "image-34.png")


*[A tooltip showing the potential skill rewards on offer for a well-trained nominal co-emperor]*  

#### The Long Tail​

As long as you have them, both nominal co-emperors and full co-emperors boost your influence gain per month and give some directly to themselves.  

If you elevate and support one from a young age, they’ll be not only a fountain of influence for you, but hopefully have a ready supply of influence themselves when they inherit.  

All you have to do is keep them sweet until then.  

#### Duumvirates​

Co-emperors can be picked up in a few ways: they might be nominal co-emperors that reached adulthood, you might nominate an adult family member, or you might diffuse a faction by elevating its leader (forcibly putting truces on *everyone* in the faction).  

They carry over the passive influence gain and Administrative office promotion efficiency we talked about in the last section. Additionally, as a full co-emperor is always an adult, provided all relevant circumstances permit, their children are considered to be Born in the Purple just as those of the full emperor.  

Co-emperors have access to the standard suite of Borrowed Powers that we give most diarchs, though things like Diarch Revoke Title and Diarch Retract Vassal cannot be used against the empire’s administrative vassals. Like all diarchs, they’re also somewhat better at scheming within the realm.  

Finally, they interact with their liege’s realm law slightly differently. Co-emperors can ask to have it increased, taking the blame as diarchs usually do, but may also ask to have the Imperial Bureaucracy *reduced*.  

This reduces any strife that the co-emperor has accrued substantially, and makes co-emperors the only character other than the realm’s liege who can directly affect its primary law.  

#### Scapegoat Counterpart​

When two people hold ultimate power in an institution, petty personal spats can not only get out of hand quickly, they’re actively incentivised: you can always blame the other guy.  

One of the first Borrowed Powers a co-emperor unlocks is the ability to Scapegoat Counterpart. Fortunately/unfortunately, their senior emperor can also use it back on *them*.  

Scapegoating your fellow emperor requires you to have *either* higher diplomacy or higher intrigue than them. You receive influence and gain a little tyranny/strife to cause your target to gain even more tyranny/strife, and lose opinion with them.  

![image-35.png](https://forumcontent.paradoxplaza.com/public/1166902/image-35.png "image-35.png")


*[A senior emperor humiliates his co-emperor in order to earn influence]*  

Influence, tyranny, and strife gain (as well as opinion loss) all scale with your relative skill, and whether you are being subtle or obvious.  

#### Demand Despotate​

A powerful co-emperor demands their own slice of the realm to rule. First, they must actually have a governorate of their own, but what self-respecting co-emperor could be happy with a mere duchy-tier title?  

With this interaction, they may demand they be given a kingdom title within the empire as their own private fief. This immediately creates said kingdom if it didn’t exist, and grants it — and all of its de jure vassals — to the co-emperor. Refusing this interaction costs the senior emperor double the influence that the co-emperor paid to send it.  

There are other ways to acquire a despotate, but they generally involve more underhanded means and don’t necessarily come with an immediate grant of (potentially) many vassals.  

#### Imperial Expedition​

With two emperors, you can afford to risk one doing something a little grandiose.  

This Borrowed Power gives the co-emperor a *single* usage of a very powerful Casus Belli: an Imperial Expedition, to be launched against realms that either border the empire or have territory de jure belonging to it. They can target *all* duchies that match either of these criteria and belong to the target.  

Every governor bordering the defender is forcibly called to war as an ally. Non-bordering governors with martial Province Administrations are given the choice to join.  

Upon victory, the co-emperor is given four choices:  


- Turn the conquered lands over to their senior emperor for disbursement, reaping opinion and influence proportional to the amount of land captured.
- Keep the territories for themselves, losing proportional opinion with their senior emperor.
- Handing over *most* of the territories whilst keeping the best duchy for themselves (giving slightly reduced influence and opinion).
- Appointing local interim governors. This gives no influence or opinion with their senior emperor, but does give plenty of opinion with the newly elevated governors, as well as hooks on them. Perfect for producing a batch of loyal future supporters.

![image-36.png](https://forumcontent.paradoxplaza.com/public/1166903/image-36.png "image-36.png")


*[A co-emperor launches an expedition to reclaim lands lost to the Turks]*  

#### God’s Perfect Vessel​

God’s vice-regent on Earth understands that killing (even when justified) is a sin. It does a ruler good to show a little mercy when dispensing justice, and what is more mercifully just than sparing a usurper’s life whilst denying them the chance to look upon God’s right-hand ever again?  

Co-emperors, senior emperors, and even appropriately-cultured co-monarchs have access to the new Maim Co-Ruler interaction. This allows you to choose whether you wish to cut away their testicles, eyes, nose, a leg, or an arm.  

If a co-ruler maims their senior ruler, they then immediately usurp their top tier titles plus the entire capital duchy. If the senior ruler maims their co-ruler, then their diarchy ends and their former co-ruler is demoted back to whatever rank is granted by any titles they hold.  

The same logic is applied on execution.  

![image-37.png](https://forumcontent.paradoxplaza.com/public/1166904/image-37.png "image-37.png")


*[A co-emperor maims his father (the option to cut off the nose is obscured by the tooltip for stabbing or boiling out the eyes)]*  

#### Co-Monarchies​

Lastly, we’ve added in a reduced form of co-emperorship for feudal rulers, in the form of co-monarchies.  

These have no new Borrowed Powers, are unique to feudal kingdoms and empires, and are primarily intended as an early game mechanism.  

Since a co-ruler is your designated heir, raising one of your children as king or emperor in your lifetime allows you access to the designate heir mechanics much earlier than usual — with the advent of Choose a New Destiny and loosened restrictions on who you might play after death, this is much less of a balance concern than previous patches.  

Your new co-ruler can only be deposed by execution (or maiming if you have the appropriate cultural tradition), has the same dubious loyalty mechanics as a co-emperor, etc., so consider this a roleplay-friendly alternative for putting your preferred heir on the throne to disinheriting your three eldest children to get to the fourth you actually wanted.  

Instead of influence gain, co-monarchs give vassal opinion scaling with their diplomacy to the liege, and gain considerable monthly prestige that scales slightly up for empires.  

![image-38.png](https://forumcontent.paradoxplaza.com/public/1166905/image-38.png "image-38.png")


*[Henry the Young King is a historical co-monarch in 1178]*  

Okay, that’s all from me. *For now.* Back to your regularly scheduled dev diary host!  

---

### New Decisions​

We’ve added a bunch of new decisions with associated content to make playing in Byzantium feel more unique. I’ll highlight a few of those here.  

### Hold Triumph​

The Byzantine Emperor can now use the Hold a Triumph Decision after a major accomplishment, like winning a War. This is a chance to capitalize on your successes and reap the rewards. You may gain Legitimacy, Influence, and Prestige depending on your actions.  

![image-39.png](https://forumcontent.paradoxplaza.com/public/1166906/image-39.png "image-39.png")


*[Decide whether your Triumph should conclude at the Hagia Sophia or the Hippodrome]*  

The following events are reactive to what you’ve done most recently as the Emperor. For example, should you win the war against the Seljuks in 1066 and hold a triumph, you’ll have unique options for how to focus your speech.  

![image-40.png](https://forumcontent.paradoxplaza.com/public/1166907/image-40.png "image-40.png")


*[Decide how to craft your imperial speech while holding a triumph]*  

### Prepare Greek Fire Dromons​

We’re not adding Naval Warfare to CK3 with *Roads to Power*, so get that idea out of your minds right now. *But!* We have added some representation for Greek Fire, the famed Byzantine weapon primarily utilized in naval warfare.  

![image-41.png](https://forumcontent.paradoxplaza.com/public/1166908/image-41.png "image-41.png")


*[Prepare Greek Fire Dromons Decision]*  

Taking this Decision as the Byzantine Emperor unlocks a new Scheme that, upon completion, gives you the ability to harm or even destroy embarked armies near Byzantion.  

![image-42.png](https://forumcontent.paradoxplaza.com/public/1166910/image-42.png "image-42.png")


*[Event where the Emperor decides how to start the Scheme to construct Greek Fire Dromons]*  

### Establish Silk Production​

Taking this decision unlocks the unique Mulberry Copse Estate Building, which gives powerful bonuses. Upgrading the Building to level 4 unlocks the Commission Silk Regalia Decision, a means of acquiring a unique Artifact – one of the many perks of being Emperor.  

![image-43.png](https://forumcontent.paradoxplaza.com/public/1166911/image-43.png "image-43.png")


*[The Decision to Commission Silk Regalia alongside the Estate Building art for the Large Magnanery]*  

---

### Terrain Changes​

A while back, there was a forum post that caught our attention suggesting Terrain changes for Anatolia. With some changes, we decided to implement these suggestions. Here’s an updated Terrain map of Anatolia:  

![image-44.png](https://forumcontent.paradoxplaza.com/public/1166912/image-44.png "image-44.png")


*[New Terrain Map Mode changes in Anatolia]*  

Most noticeably, we added a bunch of Steppe Terrain, changed the Impassable Terrain layout around Cilicia, and adjusted some County boundaries in that area as well, including the Baronies of Soloi and Tarsus.  

---

### Gloss Tooltips​

One of my favorite things that we have added in Roads to Power is what we’re calling the Gloss functionality. We have always wavered about adding historically niche words or phrases to the game, especially if they wouldn’t be translated.  

To me, this expansion just wouldn’t feel right without adding some Byzantine Greek words and phrases. So to make this all work, we’ve implemented a new type of tooltip, which you can see an example of below.  

![image-45.png](https://forumcontent.paradoxplaza.com/public/1166913/image-45.png "image-45.png")


*[An example where we highlight a quotation in Ancient Greek from Homer’s Iliad]*  

We’ve added quite a few of these around the new content we have created and hope to include this more in future expansions.  

---

Alright, folks! That’s all from me for today. As I’ve said, these are but a few examples of what we’ve made so as not to spoil any surprises awaiting you in *Roads to Power*.

 

Last edited by a moderator: Aug 20, 2024

<!-- artifact:reactions:start -->
- 126 Like
- 106 Love
- 6 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [chaddling](https://forum.paradoxplaza.com/forum/members/chaddling.1717140/)**
Role: Game Designer
Badges: 102
Messages: 56
Reaction score: 2,122

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
