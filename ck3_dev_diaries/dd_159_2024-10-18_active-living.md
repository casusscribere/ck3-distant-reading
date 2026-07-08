---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1710659/"
forum_thread_id: 1710659
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 159
title: "Dev Diary #159 - Active Living"
dd_date: 2024-10-18
author_handle: Snow Crystal
expansion: Wandering Nobles
patch: Patch 1.14
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 5496
inline_image_count: 66
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1710659'
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
    location: raw_lines_~28_to_149
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_148
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3340.jpg?1729255765
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_151_to_153
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_703_to_707
    action: preserved_and_flagged
    counts:
      Like: 49
      Love: 26
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_715_to_784
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_785_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3340.jpg?1729255765)
<!-- artifact:thread_banner:end -->

# Dev Diary #159 - Active Living

<!-- artifact:thread_metadata:start -->
- Thread starter [Snow Crystal](https://forum.paradoxplaza.com/forum/members/snow-crystal.1280952/)
- Start date [Oct 18, 2024](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-159-active-living.1710659/)
<!-- artifact:thread_metadata:end -->

Hello there!  

Last week, we got a glimpse of what we are adding to the Wandering Nobles DLC. Today, we are back to discuss the new Wandering lifestyle and the new activities it unlocks in more depth.  

## New Lifestyle​

As mentioned last week, it is set up like all the other lifestyles in the game, with 27 perks spread across 3 lifestyle trees, 3 new traits, and 3 attached focuses. Unlike our other lifestyles in the game, it is not connected to an education trait but to the Traveler trait. Now, you will gain a 10% monthly gain from the base Traveler trait and an additional 20% for every level in the Wanderer trait path.  

![Picture 1.jpg](https://forumcontent.paradoxplaza.com/public/1195116/Picture 1.jpg "Picture 1.jpg")



![Picture 2.jpg](https://forumcontent.paradoxplaza.com/public/1195117/Picture 2.jpg "Picture 2.jpg")



The way we see this lifestyle is that for some characters, it might be something to go for right away to use some of its bonuses. For many others, however, it would rather be a natural step after finishing a tree in another lifestyle and having had time to travel around to build up their Traveler trait.  

Last week, we looked at the whole tree to see what it looked like for a landed character, whereas this time, I will show what it looks like for a landless character. The two rightmost trees have minor variations, whereas the Inspection tree had to be almost entirely recreated for the new play style.  

![Picture 3.jpg](https://forumcontent.paradoxplaza.com/public/1195118/Picture 3.jpg "Picture 3.jpg")



As we start looking through each perk, I will show variations of each perk, if any, and talk a bit about each. That said, it’s only natural to start with the first tree we made for the new lifestyle.  

## Wayfarer​


When explaining the fantasy of the tree to people, I often used my father as an example. This is not the person who goes out in the forest for the sake of going anywhere, but rather someone who enjoys the journey itself. They enjoy traveling, and exactly where they end up is less important.  

Before we start, one last thing to say is a bit about lifestyle philosophy when we created these new lifestyle trees:  


- We wanted each tree's first perk (intro perk) to be generally suitable for anyone, so it is easy to dip into any of them and still feel like you get some kind of bonus worth taking. We believe it is easier to entice people to go further down the tree if they have invested some points.
- Then, we have a midpoint where we unlock the activity, which we wanted to be a halfway-capstone trait—it is supposed to define the tree.
- We also included one capstone perk right before the trait so you would feel it is worth finishing up the rest of the tree.
- Every tree should have at least two themes that will synergize throughout the tree.
- You should be active to gain the tree's bonuses. You engage with this lifestyle; the lifestyle does not engage with you.

So, with that in mind, what were the themes for the Wayfarer tree? We attached it to Fame (Prestige Experience) and Stress Loss. Attaching it to fame, rather than Prestige, enables us to give out some more sources without worrying about giving out an abundance of Prestige to the player. We also wanted to include a bit of a “friendly ruler traveling through their domain” kind of feel to it, so we have some perks trying to enable that fantasy.  

Now, let’s have a look at the perks for Wayfarer.  

![Picture 3-2.jpg](https://forumcontent.paradoxplaza.com/public/1195119/Picture 3-2.jpg "Picture 3-2.jpg")



### Well Prepared​

![Picture 4.jpg](https://forumcontent.paradoxplaza.com/public/1195120/Picture 4.jpg "Picture 4.jpg")



This perk was supposed to give you a simple way to make traveling safer. If you want to travel around a fair bit, which is the point of this tree, we want it to be less costly and dangerous. We also included a supply boon because it fits the name of the perk.  

### Far and Wide​

![Picture 5.jpg](https://forumcontent.paradoxplaza.com/public/1195121/Picture 5.jpg "Picture 5.jpg")



This is the first perk dipping into the fame synergy we wanted for the tree. By letting you travel around more safely (from the first perk) and now giving you a fame gain, you can start racking up fame while participating in activities or traveling to distant lands.  

### Just One More Hill​

![Picture 6.jpg](https://forumcontent.paradoxplaza.com/public/1195122/Picture 6.jpg "Picture 6.jpg")



This is inspired by the two educational perks in the game: the Pedagogy perk in the Scholar (Learning) tree and the Groomed To Rule perk in the Family Hierarch (Diplomacy) tree. I wanted a way to enable the player to prepare their heir for the tree if they wanted to dip into it with their next character and give them a solid way to pass on the Traveler trait from one character to another.  

As a fun little side note, the name is inspired by my father, who would always respond with a “Just one more hill and we’re home!” or “It’s just around the corner now!” whenever my sister or I would ask if we would be home soon when we were out walking as kids. Of course, that was a lie; it was not just one more hill or just around the corner.  

### Storyteller​

![Picture 7.jpg](https://forumcontent.paradoxplaza.com/public/1195123/Picture 7.jpg "Picture 7.jpg")



The first capstone perk of the tree enables both the fame and the stress loss synergy. It gives you fame from hikes and random travel events (particularly danger-related ones), and the activity is intended to be a very effective way of removing Stress (similar to feasts).  

### Of the People​

![Picture 8.jpg](https://forumcontent.paradoxplaza.com/public/1195124/Picture 8.jpg "Picture 8.jpg")


![Picture 9.jpg](https://forumcontent.paradoxplaza.com/public/1195125/Picture 9.jpg "Picture 9.jpg")



The first perk in this tree has two different variations, one playing into the friendly ruler fantasy and the other into the fame theme. In both cases, we wanted to inspire the character to move around often.  

### Local Hero​

![Picture 10.jpg](https://forumcontent.paradoxplaza.com/public/1195126/Picture 10.jpg "Picture 10.jpg")



For the Wayfarer tree specifically, we made the perk of both lines leading up to the trait a bit of a capstone perk. In this case, the Local Hero one is intended to be a great boon for those grabbing all that fame, giving them a decent Diplomacy boost. It also gives you access to two new travel options, one of which provides you with another way to play into fame and stress loss:  

![Picture 11.jpg](https://forumcontent.paradoxplaza.com/public/1195127/Picture 11.jpg "Picture 11.jpg")


![Picture 12.jpg](https://forumcontent.paradoxplaza.com/public/1195128/Picture 12.jpg "Picture 12.jpg")



### Travel Companion​

![Picture 13.jpg](https://forumcontent.paradoxplaza.com/public/1195129/Picture 13.jpg "Picture 13.jpg")



This is just a simple perk that increases the opinion of everyone traveling with you at any given time and improves the Caravan Master aptitude of anyone currently serving that role for you.  

### The Home Away from Home​

![Picture 14.jpg](https://forumcontent.paradoxplaza.com/public/1195130/Picture 14.jpg "Picture 14.jpg")



This is the capstone perk for stress loss. You can increase your stress while traveling and open up a new activity option: expanding the time spent on a hike. This should give you more options to lose stress or gain fame.  


### Wayfarer Trait​

![Picture 15.jpg](https://forumcontent.paradoxplaza.com/public/1195131/Picture 15.jpg "Picture 15.jpg")



Finally, for Wayfarer, the trait tries to tie together the two synergies that we have played into throughout the tree. It gives you higher stress loss the more fame you have, as well as giving you the Prowess fame bonus. It does mean, at the end of the day, that how many boons you get from these last perks matter how much fame you have managed to scrounge together, but we felt that was fine and played into one of our philosophies from earlier; you have to (most likely) be active to get fame, which in turn will give you a good boon at the end here.  

---

## Voyager​

So, on to our second tree, the Voyager tree. If the Wayfarer tree was about the one who enjoyed the journey but didn’t care about the destination, then the Voyager tree is the opposite. They don’t care about their journey but about where they are going. When explaining their fantasy, I have often described them as the tourist tree.  

The themes we have explored for this tree focus on Points of Interest and Languages. The points of interest theme was an obvious fit for it, whereas the language theme just happened as we played around with themes that might fit the tree. Of course, the tree isn’t limited to just those two things.  

![Image 15-2.jpg](https://forumcontent.paradoxplaza.com/public/1195132/Image 15-2.jpg "Image 15-2.jpg")



### Power at Home/Organized Camp​

![Picture 16.jpg](https://forumcontent.paradoxplaza.com/public/1195133/Picture 16.jpg "Picture 16.jpg")


![Picture 17.jpg](https://forumcontent.paradoxplaza.com/public/1195134/Picture 17.jpg "Picture 17.jpg")



When we originally made the perk for landed gameplay, being able to handle your regent at home would help someone who would regularly travel abroad to see things. If the idea was that you should be able to travel to distant places, we didn’t want you to get punished too hard immediately.  

That idea did not easily reflect into a landless variation, so we instead tried to dip more into our idea of having “something that is just generally good to dip into” for landless play, and that was an across-the-board boon to provisions and travel speed.  

### Mercenary Contacts​

![Picture 18.jpg](https://forumcontent.paradoxplaza.com/public/1195135/Picture 18.jpg "Picture 18.jpg")


![Picture 18-2.jpg](https://forumcontent.paradoxplaza.com/public/1195209/Picture 18-2.jpg "Picture 18-2.jpg")



We wanted to give the Voyager an easy, cheap option to provide general boosts to their travels, but taking a travel option spot. This means you can travel far with fewer dangers, presumably, but you are giving up other opportunities. Due to the name, we attached a bonus to hiring regular mercenaries.  

### Journey Planner​

![Picture 19.jpg](https://forumcontent.paradoxplaza.com/public/1195137/Picture 19.jpg "Picture 19.jpg")



Looking into opportunities to go to distant locations, we figured a boon to diplomatic range would be an exciting option. One thing to note is that it is not an easily obtainable modifier in many places in the game, giving another reason for dipping into the tree. Another thing to note is that the tree unlocks diplomatic range matters for the Monument Expedition activity, so increasing it slightly means you will have access to more locations for that activity if you so wish.  

### Finally There​

![Picture 20.jpg](https://forumcontent.paradoxplaza.com/public/1195138/Picture 20.jpg "Picture 20.jpg")



We wanted to empower the player when they finally reach their destination in a journey, to play into the core idea of the tree. Initially, we simply gave the player a prestige and stress bonus every time they reached their destination in a journey.  

However, this didn’t quite work when we looked at the tree for landless characters, as… Well… They could reach a destination every other day if they kept moving their camp about. Instead, we attached the same idea directly to Points of Interest, which synergizes surprisingly well with another perk further down the tree. We initially kept the original idea for landed gameplay, but after seeing the synergy and how much cleaner it looked, we changed it to be the same as the landless one.  

### Journey​

![Picture 22.jpg](https://forumcontent.paradoxplaza.com/public/1195139/Picture 22.jpg "Picture 22.jpg")



The mid-way capstone perk of the tree, where you unlock the Monument Expedition. The activity was strong enough that we did not need to attach many other effects to this one. The first perk that plays into the language theme, making it slightly easier to learn new languages.  

### Souvenirs Aplenty​

![Picture 23.jpg](https://forumcontent.paradoxplaza.com/public/1195140/Picture 23.jpg "Picture 23.jpg")


![Picture 24.jpg](https://forumcontent.paradoxplaza.com/public/1195141/Picture 24.jpg "Picture 24.jpg")



As part of this tree, we wanted to include at least one perk where you could effectively “bring home development,” but we wanted to ensure it couldn’t be stacked infinitely. In that sense, we figured it might be fun if you, as a, for example, slightly backward Scandinavian, traveled to Constantinople to see the sights and were inspired to improve your homeland.  

This is another one that didn’t reflect well as a landless one. We tried different variations, some decreasing building costs for a period, etc. But in the end, none of them felt quite right, so we simplified it and reimagined it as a perk where going to new places would give a (non-stacking) opinion boon with your camp.  

### Gracious Host, Impeccable Guest​

![Picture 25.jpg](https://forumcontent.paradoxplaza.com/public/1195142/Picture 25.jpg "Picture 25.jpg")


![Picture 26.jpg](https://forumcontent.paradoxplaza.com/public/1195143/Picture 26.jpg "Picture 26.jpg")



We imagined this perk as someone who has often been traveling to other cities and knows the etiquette and manners expected of you no matter where you are. Someone who can equally serve up an impressive feast for strangers on one side and attend one in an exotic court on the other.  

This is the primary payoff perk for the language theme, as you get a neat bonus for all your court positions. It’s not grand or super impactful, but it can add up if you have a lot of active court positions.  

### Been There, Done That​

![Picture 27.jpg](https://forumcontent.paradoxplaza.com/public/1195144/Picture 27.jpg "Picture 27.jpg")



This is the other perk I mentioned in the ‘Finally There’ perk. It increases almost all rewards you gain from Points of Interest by 30% (with a few exceptions, like events triggering or gaining traits). This is the absolute capstone perk of the tree, and it enables a playstyle mostly traveling around and seeing Points of Interest with Monument Expeditions and Pilgrimages while still racking up lifestyle experience points, a lot of prestige, and reducing stress.  

### Voyager Trait​

![Picture 28.jpg](https://forumcontent.paradoxplaza.com/public/1195145/Picture 28.jpg "Picture 28.jpg")



Unlike its Wayfarer equivalent, we wanted this trait to play less into the synergies of the tree but more be a composite of the tree. It bumps up the diplomatic range gain even further and increases your travel speed, giving you access to even more points of interest previously out of range.  

---

## Inspector - Landed​

The final tree of the lifestyle is the Inspector tree, and as you might notice, we will split this into two different sections altogether, rather than simply showing the variations of the perks. This was the one tree that saw a significant rework for landless gameplay due to how the tree was initially structured for landed gameplay.  

When we started making this tree, we wanted a tree that was very much built up around a managerial figure who would travel the realm regularly to make sure everything was up to scratch—the one who periodically shows up unannounced in a vassal’s domain to ensure they are doing their job correctly.  

The themes for this tree are fuzzier, and it is more playing into a specific idea of having to travel to holdings around the realm to give them a temporary boon. You go somewhere, host an activity, or make a decision somewhere, and that place is improved for a while.  

![Picture 28-5.jpg](https://forumcontent.paradoxplaza.com/public/1195146/Picture 28-5.jpg "Picture 28-5.jpg")



### Mustering​

![Picture 29.jpg](https://forumcontent.paradoxplaza.com/public/1195147/Picture 29.jpg "Picture 29.jpg")



The first one is a simple boon as you travel through holdings of your realm, improving any Stationed Men-at-Arms there by about 5-10% for 15 years. In other words, consider preparing before going to war, making sure to do the rounds and inspire your men so they get that fighting boon.  

### Know Your Land, Know Your People​

![Picture 30.jpg](https://forumcontent.paradoxplaza.com/public/1195148/Picture 30.jpg "Picture 30.jpg")



This is a mouthful but less impactful than it first seems. The parochial and minor landholder vassal bonuses should be negligible, and the importance lies in the marriage acceptance boon. It means that within your realm, you have a significantly higher chance of being able to grab any marriage you may wish, both for yourself and your extended family. Want to ally with a pesky vassal who keeps being an issue to your rule? This could push up the acceptance level enough to make it happen.  

I understand that certain players will read this as marriage acceptance with close and extended family, and technically speaking, that would also be true as long as they are within the realm.  

### No Stone Unturned​

![Picture 31.jpg](https://forumcontent.paradoxplaza.com/public/1195149/Picture 31.jpg "Picture 31.jpg")



As part of our work on this lifestyle tree, we wanted to give the player more active tools for gaining control and development, of which this perk is a key part. By hosting feasts, hunts, inspections, or other activities, you can now focus on where you want to improve something.  

Need to hold a feast, and you recently had a popular revolt ruin the control in your domain? Now, you can handle both of those at once.  

### Travel Logs​

![Picture 32.jpg](https://forumcontent.paradoxplaza.com/public/1195150/Picture 32.jpg "Picture 32.jpg")



We often noticed that many players ensured that they only traveled relatively safely, so the Seasoned Trait Track had little time to shine. As a ruler who was actively trying to make sure their realm was safe and well taken care of, it felt natural that you would be able to increase this trait track even if you didn’t directly experience the danger, simply because you were so directly working against it.  

### Inspection​

![Picture 33.jpg](https://forumcontent.paradoxplaza.com/public/1195151/Picture 33.jpg "Picture 33.jpg")



The first capstone perk of the tree opens up the inspection activity. This should open up the fantasy of traveling around your realm more appropriately, as we will see later when discussing the activity. We also attached some tax bonuses,  

### Arbitration​

![Picture 34.jpg](https://forumcontent.paradoxplaza.com/public/1195152/Picture 34.jpg "Picture 34.jpg")



This unlocks a new decision where you can stop a journey to manage the domain for a while. Effectively, you will trade some prestige and travel time to gain legitimacy and either remove corruption in that domain or gain a temporary modifier that will increase levy size, holding taxes, or development. This plays into the same logic as with ‘No Stone Unturned,’ where you can more directly manage one holding and take care of any issue it might have.  

### Charts & Itineraries​

![Picture 35.jpg](https://forumcontent.paradoxplaza.com/public/1195154/Picture 35.jpg "Picture 35.jpg")



This unlocks a new decision: You can write a book about your travels somewhere. This is a leftover from when the tree was focused more on surveying the land rather than inspecting it when we focused more on mapping out your realm, etc. We like how the decision turned out, so we kept it as is, even if things around it have changed slightly.  

### Personal Touch​

![Picture 36.jpg](https://forumcontent.paradoxplaza.com/public/1195155/Picture 36.jpg "Picture 36.jpg")



This is the proper capstone perk of this tree, binding together ‘No Stone Unturned,’ ‘Inspection,’ and ‘Arbitration’ in one, either giving you them for free or improving them. This should be a noticeable boon for those who want to simply do realm gardening and ensure their little realm runs smoothly.  

### Inspector Trait​

![Picture 37.jpg](https://forumcontent.paradoxplaza.com/public/1195156/Picture 37.jpg "Picture 37.jpg")



With a similar logic to the Voyager trait, this is supposed to, at a glance, tell a player what kind of fantasy this tree is supposed to provide to you as a player. It’s about realm management and gardening and ensuring all the little bits and bobs work as they should.  

---

## Inspector - Landless​


As we approached making a landless variant of the Inspector tree, we asked ourselves if we could keep the same logic as we did for the landed tree. After all, it was a tree focused on improving your realm, which is hard to simulate with a character that does not hold land.  

In the end, we decided to do away with the central theme of the tree and look for something that might work better for the landless playstyle instead. We landed (see what I did there?) on a theme around improving your understanding of a specific terrain. Simply put, you can become the master of a particular field or area.  

![Picture 37-2.jpg](https://forumcontent.paradoxplaza.com/public/1195157/Picture 37-2.jpg "Picture 37-2.jpg")



### Finding Your Way​

![Picture 38.jpg](https://forumcontent.paradoxplaza.com/public/1195158/Picture 38.jpg "Picture 38.jpg")



So, the very first perk of this tree is critical to setting up the rest of the tree. We unlock a new decision for you where you choose a designate a type of terrain that you would like to focus on:  


- Woodlands - Forests/Jungles/Taiga/Wetlands
- Highlands - Mountains/Hills/Desert Mountains
- Lowlands - Plains/Steppe/Farmlands/Floodplains
- Drylands - Deserts/Drylands/Oasis
For many perks following this, you will then enable bonuses to the Designated Terrain.  

### Knowing the Land​

![Picture 39.jpg](https://forumcontent.paradoxplaza.com/public/1195159/Picture 39.jpg "Picture 39.jpg")



As we looked at changing the “Knowing Your Land” perk, we still wanted to try and keep some of the same fantasy. But rather than knowing your land or its people, you know the terrain you specialize in and how you keep yourself alive as you travel through it. As a significant boon to the Gather Provisions decision, it is an even more helpful tool in getting extra provisions, particularly if you spend most of your time in your Designated Terrain.  

### Navigating the Wilds​

![Picture 40.jpg](https://forumcontent.paradoxplaza.com/public/1195160/Picture 40.jpg "Picture 40.jpg")



We knew we wanted to put a battle bonus to this one. After all, as we started playing around with the idea of specializing in a terrain, one of our first ideas was to be a renowned bandit group holed up in a mountain pass. We want you to feel like when you are fighting in your terrain, you are truly in your element.  

### Earth’s Bounty​

![Picture 41.jpg](https://forumcontent.paradoxplaza.com/public/1195161/Picture 41.jpg "Picture 41.jpg")



Replacing the Inspection trait wasn’t easy, as it was vital to the original tree. What we looked at was to continue the logic from the ‘Knowing the Land’ perk, where provisions are less of a problem as you travel through your Designated Terrain. Opening up the Quartermaster and Head Porter positions irrelevant to your buildings means you will always have effective ways of handling provisions.  

### Right-Hand Man​

![Picture 42.jpg](https://forumcontent.paradoxplaza.com/public/1195162/Picture 42.jpg "Picture 42.jpg")



After making Earth’s Bounty, we felt we had a tiny sub-theme of Officers in the tree, so we thought we could play further into that with this trait. The Second officer is the most crucial position you can have as a landless character, and this is a way to ensure they are doing their utmost for you.  

The second part of the perk was my experimentation to see if it would be interesting for the player to gain skill bonuses based on their current Camp Purpose, slightly inspired by other perks such as ‘Friendly Counsel’ in the Family Hierarch (Diplomacy) tree or ‘Learn on the Job’ in the Scholar (Learning) tree. As you might imagine, the exact skills will change depending on your camp purpose, such as Martial and Prowess for Swords-for-Hire or Learning and Stewardship for Scholars.  

### King of the Wilds​

![Picture 43.jpg](https://forumcontent.paradoxplaza.com/public/1195163/Picture 43.jpg "Picture 43.jpg")



This is the capstone perk of this lifestyle, unlocking a decision to hyper-focus on a specific terrain from the ones in your Designated Terrain. For example, if you chose Highlands the first time, you can now select between Mountains, Hills, or Desert Mountains as your terrain to master.  

The idea was that since you specialize in a particular terrain, you are likely to be often forced to take action outside of that terrain and then get 0 bonuses from this perk, so in turn, they should be extra strong when you finally get the chance to shine.  

---

## New Activities​

As we started working on the DLC, we knew we wanted to add activities so the player could open up more travel options. We already have many options across base-game activities (see Hunts, Pilgrimages, and Feasts) and DLC-locked ones (see grand activities), but we wanted to make something symbolic of each tree.  

In the end, though we had many different potential options, we ended up with three activities we wanted to go for:  


- Hikes for the Wayfarer tree, so you can travel just for the sake of traveling
- Monument Expedition for the Voyager tree so that you can get to the points of interest you want to see
- Inspection for the Inspector tree so you can improve the specific counties you want to improve

It was vital for us that each activity gave you more of what the lifestyle tree already gave you, but usually with minor tweaks or twists from the regular lifestyle. For example, the hike will give you stress loss and fame, but you might also get wise man trait XP.  

## Hikes​

Speaking of hikes, it is the first activity we will talk about.  

![Picture 44.jpg](https://forumcontent.paradoxplaza.com/public/1195164/Picture 44.jpg "Picture 44.jpg")



You can set out with your guards and up to 1 special companion to leave life at court for a short bit. If you bring a companion, the events will change slightly based on that, and you will have opportunities to build a bond with them. Or torment them if they aren’t built for hiking.  

You will set out towards a location, usually quite remote from anything. As you reach the area, the activity will start, and you will take a short hike before you start the return journey back home. You will go through several events detailing your experience in the wilderness, some rarer than others.  

Some examples:  

![Picture 45.jpg](https://forumcontent.paradoxplaza.com/public/1195165/Picture 45.jpg "Picture 45.jpg")


![Picture 46.jpg](https://forumcontent.paradoxplaza.com/public/1195166/Picture 46.jpg "Picture 46.jpg")



The “systemic” events of the activity—the start, mid-activity, and end events—don’t have options, but any randomized events in between those will. You will meet people, see sights, or experience nature's good and bad sides.  

![Picture 47.jpg](https://forumcontent.paradoxplaza.com/public/1195168/Picture 47.jpg "Picture 47.jpg")


![Picture 48.jpg](https://forumcontent.paradoxplaza.com/public/1195169/Picture 48.jpg "Picture 48.jpg")



## Monument Expeditions​

The Monument Expedition is the only one of the three that lets you travel outside your borders, which felt fitting considering the lifestyle trees and how they have been set up. You can go to any barony in the world with a special building, so it’s not just for any point of interest, but it will let you visit most of them.  

![Picture 49.jpg](https://forumcontent.paradoxplaza.com/public/1195170/Picture 49.jpg "Picture 49.jpg")



![Picture 50.jpg](https://forumcontent.paradoxplaza.com/public/1195171/Picture 50.jpg "Picture 50.jpg")



When you arrive at the activity's location, you can choose one skill to focus your efforts on as you explore the local sights. The alternatives will be based on the building and its type, and then throughout the activity, you will have opportunities to increase or decrease the chance of getting skill boons.  

![Picture 51.jpg](https://forumcontent.paradoxplaza.com/public/1195172/Picture 51.jpg "Picture 51.jpg")



Most events related to the activity will either increase your chance of getting extra skill boons or give you options for good court position holders.  

![Picture 52.jpg](https://forumcontent.paradoxplaza.com/public/1195173/Picture 52.jpg "Picture 52.jpg")



![Picture 53.jpg](https://forumcontent.paradoxplaza.com/public/1195174/Picture 53.jpg "Picture 53.jpg")



Finally, at the end of your journey, you will gain a slight skill improvement, with the possibility of a second one based on how things turned out.  

![Picture 54.jpg](https://forumcontent.paradoxplaza.com/public/1195175/Picture 54.jpg "Picture 54.jpg")



## Inspections​

Now then, to the final activity, Inspection. Similar to the hikes, this can only be done within your borders, giving you a few options based on where it is and what you want to do. One thing to note is that numbers might be higher than they should be in the following pictures (success chance and gold gain).  

![Picture 55.jpg](https://forumcontent.paradoxplaza.com/public/1195176/Picture 55.jpg "Picture 55.jpg")



![Picture 56.jpg](https://forumcontent.paradoxplaza.com/public/1195177/Picture 56.jpg "Picture 56.jpg")



As you arrive, you will have three options to choose from (the first one is only available in border counties). They are:  


- Claims/Vassalization Acceptance
- Taxes/County Control/Development
- Levies/Opinion/Popular Opinion

We made all the information easily accessible in the event, so you do not have to comb through menus to find it. In the picture, you can see that you have 325 levies from the county, 1.64 in taxes, 9 development, 10 popular opinion, and the local ruler has an opinion of 100 of you.  

The option chosen will affect the rest of the inspection and how things will turn out, and this will be the goal of the inspection. Based on your options here, many events in the rest of their activity might act slightly differently. For example, an option that would increase the chances of success for someone aiming to increase Levies/Opinion/Popular Opinion might decrease the chance of success for someone aiming to increase Taxes/Control/Development.  

Halfway through the activity, you will get a second option to specialize:  

![Picture 57.jpg](https://forumcontent.paradoxplaza.com/public/1195178/Picture 57.jpg "Picture 57.jpg")



Here, you get to choose even further. In this case, we decided on Taxes/County Control (which is invisible due to already being at a 100)/Development as our first option, and here, we get to choose between Taxes and Development to hyper-focus on. This lets us decide which will have the strongest effect in the case of a successful Inspection.  

Throughout the inspection, you will encounter a fair number of events that give you opportunities to affect the county in some way. Most of these will have opportunities to increase or decrease the chance of success, which is at the heart of the activity.  

![Picture 58.jpg](https://forumcontent.paradoxplaza.com/public/1195179/Picture 58.jpg "Picture 58.jpg")



![Picture 59.jpg](https://forumcontent.paradoxplaza.com/public/1195180/Picture 59.jpg "Picture 59.jpg")



And if things work out, you will get the rewards you sought.  

![Picture 60.jpg](https://forumcontent.paradoxplaza.com/public/1195181/Picture 60.jpg "Picture 60.jpg")



---

## Conclusion​

And that’s all for this time. Hopefully, you all enjoyed this glance at the new lifestyle and new activities. With winter soon upon us up here in the north, I figured I’d give you one last art piece to look at before I jump out. Look at it and freeze, like I do.  

![Picture 61.jpg](https://forumcontent.paradoxplaza.com/public/1195182/Picture 61.jpg "Picture 61.jpg")



Oh, and remember to leave any questions you might have about the DLC below, and I’ll happily answer them.

 

#### Attachments

- [![Picture 19.jpg](https://forumcontent.paradoxplaza.com/thumbnail/public/1195136/Picture 19.jpg)](https://forum.paradoxplaza.com/forum/attachments/picture-19-jpg.1203606/)
  
  Picture 19.jpg
  5,8 KB

 · Views: 0

<!-- artifact:reactions:start -->
- 49 Like
- 26 Love
- 7 (unlabeled — rendered as base64 data URI)
- 7 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Snow Crystal](https://forum.paradoxplaza.com/forum/members/snow-crystal.1280952/)**
Role: Game Designer - Crusader Kings 3
Badges: 63
Reaction score: 12,091

*[Full game-badge icon list of 14 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
