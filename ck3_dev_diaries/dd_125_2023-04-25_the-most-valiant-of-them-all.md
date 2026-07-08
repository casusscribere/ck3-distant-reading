---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1579721/"
forum_thread_id: 1579721
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 125
title: "Dev Diary #125 – The Most Valiant of Them All"
dd_date: 2023-04-25
author_handle: PDX-Trinexx
expansion: Tours and Tournaments
patch: Patch 1.9
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 3048
inline_image_count: 27
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1579721'
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
    location: raw_lines_~28_to_159
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_158
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2313.jpg?1682419705
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_161_to_163
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_485_to_490
    action: preserved_and_flagged
    counts:
      Love: 118
      Like: 95
      (unlabeled — rendered as base64 data URI): 3
      Haha: 2
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_498_to_596
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_597_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2313.jpg?1682419705)
<!-- artifact:thread_banner:end -->

# Dev Diary #125 – The Most Valiant of Them All

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)
- Start date [Apr 25, 2023](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-125-the-most-valiant-of-them-all.1579721/)
<!-- artifact:thread_metadata:end -->

### Knights, Accolades and Glory​

Hey! We’re CK’s resident gang of big, beefy, vascular knight bannerets and we’re here to talk knights! Specifically, the brand-new Accolades feature. So slap on your jerkin, grab your bodkin, strap on your slaying-sword, and don’t you dare get distracted by any damsels in distress.  

Accolades are about adding depth and flavor to knight management, giving you cause to care about the low-ranked NPCs you’re sending to untimely deaths. This is a smaller feature, but it’s an excellent tie-in to the new Activity System, particularly Grand Tournaments. Activities are ideal less-than-lethal reasons to get your knights out of the house, and get them known as the budding warriors and leaders they are.  

### Hey, is this just adding more Knight Effectiveness?​

No. But your knights *will* probably get a few new things to offer the battlefield.  

### What’s an Accolade?​

*“In death thy glory in heaven, in victory thy glory on earth. Arise therefore, Arjuna, with thy soul ready to fight”* - The Bhagavad-Gita  

An Accolade represents the special honors - the eminent status - a liege affords to a favored knight. It represents an awe-inspiring reputation passed through generations of fighters; as Accolades improve over time (and as more storied martial deeds are done), they offer more bonuses to the knights who hold them and to their liege (you).  

![01-knights-window.png](https://forumcontent.paradoxplaza.com/public/959498/01-knights-window.png "01-knights-window.png")


[Image: Accolades reside at the top of the Knights Window]  

By spending prestige to create an Accolade on a worthy knight, you make the character your Acclaimed Knight. They serve just as normal knights do, with no additional effects but those provided by their Accolade Attributes (I’ll get to those shortly).  

Here’s what creating an Accolade looks like:  

![02-create-accolade.png](https://forumcontent.paradoxplaza.com/public/959499/02-create-accolade.png "02-create-accolade.png")


[Image: Pictured: who you can Acclaim and what’s so very praiseworthy about them]  

Note that not *all* your knights are shown as Accolade candidates here. Only unlanded and baron-rank knights can become Acclaimed Knights. Candidates must also have at least 8 prowess - nobody wants them constantly dying of incompetence. Finally, they have to be eligible for at least two Accolade Attributes.  

### Accolade Attributes​

*“He who would tell divers tales must know how to vary the tune.”* - Marie de France  

Accolade Attributes reflect the traits, skills or other qualities of your knights that make them stand out. They’re the source of Accolade bonuses, which scale as knights gain Glory (a new stat: Accolade XP).  

Every Accolade has two Attributes. The Ranks earned through Glory gain alternately provide one Attributes’ bonus and then the other’s. So, if your Accolade has a Mentor Attribute, you’ll gain the Mentor’s aid to their fellow knights only with every second increase in Rank.  

Some Attributes simply herald an element of a knight’s personality and, while they can be interesting, aren’t particularly impressive. Others (like the aforementioned Mentor) depend on the knight being exceptional and, in return, offer potent men-at-arms modifiers, lifestyle trait boosts, etc.  

Let’s check out some Attributes.  

![03-outrider.png](https://forumcontent.paradoxplaza.com/public/959501/03-outrider.png "03-outrider.png")


[Image: The lowest-level Outrider Attribute bonuses]  

The Outrider, shown above, is mostly about boosting light cavalry. Below, you can see what its effects look like when they reach their max. If you’re interested in these kinds of Men-at-Arms bonuses: there’s more on that later in the Dev Diary, including a hot scoop on special Accolade MaA units.  

![04-outrider-max.png](https://forumcontent.paradoxplaza.com/public/959502/04-outrider-max.png "04-outrider-max.png")


[Image: The highest-level Outrider Attribute bonuses]  

To be an Outrider, your knight needs the Open Terrain Expert trait or XP in the Horse track of the shiny new Hastiluder tiered trait (gained from Grand Tournament participation). Being, say, a salt-of-the-earth Thug is more common. Wrathful, Arbitrary, Impatient, Arrogant and Reaver characters all qualify.  

The Thug’s is not exactly a rich lineup of bonuses. But hey, if you’re a bad guy, you might still want a Thug on your side!  

![05-thug.png](https://forumcontent.paradoxplaza.com/public/959503/05-thug.png "05-thug.png")


[Image: the lowest-level Thug Attribute bonus]  

![06-thug-max.png](https://forumcontent.paradoxplaza.com/public/959504/06-thug-max.png "06-thug-max.png")


[Image: The highest-level Thug Attribute bonuses]  

Given knights are a liege’s military muscle, most Accolade bonuses are martial and army-focused. Nonetheless, for those more interested in singing *chansons* than cleaving skulls, there’s Acclaimed Knights like the rare Master of Revels:  

![07-revels.png](https://forumcontent.paradoxplaza.com/public/959505/07-revels.png "07-revels.png")


[Image: The lowest-level Master of Revels Attribute bonuses]  

![08-revels-max.png](https://forumcontent.paradoxplaza.com/public/959506/08-revels-max.png "08-revels-max.png")


[Image: The highest-level Master of Revels Attribute bonuses]  

If you find yourself curious about Attributes, a full list with requirements and effects are listed in the in-game Encyclopedia. Have a Marauder and Thug-led gang of bully-boys backing you up, if you wish - or get yourself a Tactician and a House Paragon!  

One thing to clear up: while it’s possible to have multiple Acclaimed Knights, you may only ever have one instance of each Accolade Attribute. Let’s keep the modifier stacking reasonable, folks.  

![09-an-accolade.png](https://forumcontent.paradoxplaza.com/public/959507/09-an-accolade.png "09-an-accolade.png")


[Image: An Accolade]  

### The Accolade View​

You’ve created an Accolade. It’s visible above your knights list. When opened, you’re faced with the Accolade’s name, its Acclaimed Knight, the Successor (if one’s been found), its Attributes, and the bonuses it provides.  

Note that your Accolades can be freely renamed, just in case the randomly-filled templates like “The Sword of Death” or “Senior Knight of the Polish Guard” don't do it for you.  

And the track in the middle is showing… Glory? That’s XP, right?  

### Glory​

*“He who does more is of greater worth”* - Geoffroi de Charny, The Book of Chivalry  

Heck yeah, XP. Glory is gained whenever something happens that might make your Acclaimed Knight and their Accolade more respected, more famed and glorious, in the eyes of loyal warrior and hateful foe alike. Accolade Rank is increased with Glory; they’re what provide you with the good stuff.  

Here’s a list of common Glory sources for an Acclaimed Knight:  


- Fighting in winning battles
- Wounding/killing other knights in battle
- Winning single combats
- Attending Activities with their liege
- Participating in/winning Tournament Contests
- Their liege winning wars against higher-ranked war targets

On that last point: indeed, the feat of besting an Emperor as a Count nets the Count’s Acclaimed Knights a tasty bit of extra Glory. This amount varies based on the size of the war target and the Casus Belli type.  

![10-glory-gain.png](https://forumcontent.paradoxplaza.com/public/959508/10-glory-gain.png "10-glory-gain.png")


[Image: Glory gain on victory… should this victory somehow happen]  

Some new events will also provide opportunities to increase your Accolade’s Glory. This may be the knight-iest one of all:  

![11-training-montage.png](https://forumcontent.paradoxplaza.com/public/959509/11-training-montage.png "11-training-montage.png")


[Image: An imminent training montage]  

![12-tooltip.png](https://forumcontent.paradoxplaza.com/public/959510/12-tooltip.png "12-tooltip.png")


[Image: Tooltip of Option A, with Accolades shown in its bottom two entries]  

Glory will not accrue endlessly; it is also sometimes lost. This happens when knights lose battles, are defeated, and on Accolade Succession. The last one might seem harsh, but can you really expect a brand-new Acclaimed Knight to command the same respect as their predecessor? Give them some time.  

![13-lolnoob.png](https://forumcontent.paradoxplaza.com/public/959511/13-lolnoob.png "13-lolnoob.png")


[Image: A n00b.]  


### ​

### Accolade Succession​

*“For I have promised to do the battle to the uttermost, by faith of my body, while me lasteth the life, and therefore I had liefer to die with honour than to live with shame”* - Malory, Le Morte d’Arthur  

Knights die. It’s a hazard of the job. If Accolades, as a system, were about the rise of an individual knight’s personal legend, it’d necessitate a lot of frustration and loss of investment. Therefore, Accolades carry on from master to pupil, from Acclaimed Knight to Successor.  

Accolade Successors are filled in automatically, but the Accolade’s liege is free to remove them and select replacements.  

![14-accolade-succession.png](https://forumcontent.paradoxplaza.com/public/959512/14-accolade-succession.png "14-accolade-succession.png")


[Image: Successor requirements and candidates]  

What if one has no valid Successors among their knights? Well, willing players can try to recruit characters who fulfill Attribute requirements, by hook (literally and otherwise) or marriage offer.  

But if poring through character lists is not your cup of tea, never fear!  

### Seek Worthy Accolade Successor​

*“Your prowess, Roland, is a curse on our heads”* - The Song of Roland  

Worried that one day your Acclaimed Knight will be dead and gone? For a nominal prestige cost, a brand new Accolade Successor can be yours!  

![15-seek-successor.png](https://forumcontent.paradoxplaza.com/public/959513/15-seek-successor.png "15-seek-successor.png")


[Image: This Interaction is available from the Successor window]  

![16-successor-found.png](https://forumcontent.paradoxplaza.com/public/959514/16-successor-found.png "16-successor-found.png")


[Image: Top-quality chivalric virtue, on demand!]  

There *is* a bit of fine print to Seek Worthy Accolade Successor, including a fair amount of cooldown. Also, Successors will not necessarily fulfill *both* of an Accolade’s Attributes, and when that happens - things get funky.  

### Primary & Secondary Attributes​

Accolades all have two Attributes. First displayed is the Primary, the core of the Accolade’s identity, which will never change. Below is the Secondary Attribute, which Successors aren’t required to qualify for. Successors must simply fulfill the Primary Attribute requirements (listed in the Successor screen) and qualify for any other Attribute.  

An example: you create an Accolade with a Politicker Primary Attribute and an Idealist Secondary Attribute. The Accolade is named something warm and fuzzy like “Most Loyal of the Banners”. Then the Acclaimed Knight dies, and guess what? His Successor is no Idealist, he’s a dang Thug! Your new knight is putting his unique unsavory spin on your Politicker Accolade.  

On the bright side, the mutability of Secondary Attributes allows you more flexibility with Accolade bonuses. This boon is offset by increased Succession Glory loss whenever an Accolade has to change over to a new Secondary Attribute.  

### Inactive Accolades​

*“Ubi sunt”*  

What if, god forbid, you fail to find a Successor for your Accolade? Fear not, sweet gamer. The Accolade isn’t destroyed, but rather it becomes Inactive. If you want to free up the slot, you can Retire the Accolade even while it’s still filled by a knight, and it’ll become Inactive.  

Clicking on the Inactive Accolades button which, when needed, appears in the Knights and Accolades window will take you here:  

![17-out-of-commission.png](https://forumcontent.paradoxplaza.com/public/959515/17-out-of-commission.png "17-out-of-commission.png")


[Image: Some out-of-commission Accolades]  

These Inactive Accolades no longer provide any effects. You may Reinstate them, choosing a knight to fill them when doing so, or delete them if you wish.  

But what if you have an Inactive Accolade and there’s no one up to the task of filling it?  

### The Restore Accolades Decision​

*“Are there such heroes among you / Whose bones would not crackle in my fingers?”* - The Epic of Jangar  

Of course, you’re free to hunt down characters who meet the requirements of your fallen Accolades manually. But this Decision exists to make things a little easier:  

![18-restore-accolades.png](https://forumcontent.paradoxplaza.com/public/959516/18-restore-accolades.png "18-restore-accolades.png")


[Image: SOUND THE HORNS, SEND THE MINSTRELS]  

Neat little aside: this Decision first looks to recruit existing characters, but if none available meet requirements, new characters are generated. The new characters’ Skills and Traits will be appropriate for your Accolade’s Primary Attribute. The individual’s culture should be both A) situated realistically near to yours, B) friendly with yours, and C) either suit the Primary Attribute or generally be well-known for exceptional knights. Basically, this just sets up Norman knights appearing as Accolade candidates all over Christendom.  

Plus, if you’re Emperor of Byzantium, there’s a decent chance the elite fighting men who show up will be Armenians or Varangians. Pretty neat.  

### Acclaimed Knights & Grand Tournaments​

Let’s switch gears and talk Tournaments. They’re an outstanding one-stop destination for all things knight. Not only do your Acclaimed Knights stand to gain Glory from competition and victory, but the Hastiluder Trait earned with the honing of warrior skills unlocks powerful Men-at-Arms Attributes. Attend equestrian contests if you’re interested in Attributes like Lancer or Camel Rider; hold dismounted combats to pursue knights like the Vanguard and the Skirmisher, and do some archery to get Archers and Crossbow Captains.  

Those particularly interested in improving their stable of knights can attend Tournaments with the Recruit Intent, and improve their odds of going home in chivalrous company.  

![19-recruit-intent.png](https://forumcontent.paradoxplaza.com/public/959517/19-recruit-intent.png "19-recruit-intent.png")


[Image: A Tournament attendee selecting the Recruit Intent]  

Interested in your own tale-worthy tournamenting knight? Want an Ulrich von Lichtenstein to dazzle the crowd with skin-tight armor and miraculous skill? Well…  

![20-out-of-control-references.png](https://forumcontent.paradoxplaza.com/public/959518/20-out-of-control-references.png "20-out-of-control-references.png")


[Image: Reference reference]  

### Accolades for Everybody! No, Wait…​

The keen-eyed among you may have noticed earlier there’s but 5 spaces for Accolades in the Knights and Accolades window. This is no mistake: 5 is the maximum number of Acclaimed Knights you’ll ever have simultaneously. And I’m afraid to say you’ll often have far less. Sometimes, even no capacity for Accolades at all.  

What gets you from no Accolades at all to a whole squad of Acclaimed Knights? These do:  


- King-tier Rank
- Emperor-tier Rank
- Bannus (Innovation)
- Knighthood (Innovation)
- Renowned Name (Dynasty Legacy Perk 2)

![21-knighthood-innovation.png](https://forumcontent.paradoxplaza.com/public/959519/21-knighthood-innovation.png "21-knighthood-innovation.png")


[Image: The Knighthood Innovation, looking pretty stronk]  

### Who is the Most Glorious of Them All?​

*“This man was very rich and very proud of his bravery, courage and conspicuous lineage; for every Frank is anxious to outdo the others”* - Anna Comnena, huge fan of the Latins  

Some cultures’ members tended to care a little more than others about glorious feats of arms, and thus we’ve given them a boost to Glory gain. Cultures with Traditions like Chanson de Geste, Royal Army, Performative Honor: those cultures’ Acclaimed Knights have the best shot at being the greatest in all the world.  

![22-futuwaa-innovation.png](https://forumcontent.paradoxplaza.com/public/959520/22-futuwaa-innovation.png "22-futuwaa-innovation.png")


[Image: Futuwaa, with its new Glory Gain modifier]  

The Chivalry lifestyle tree is a good source of Glory bonuses too.  

![23-chivalric-dominance.png](https://forumcontent.paradoxplaza.com/public/959521/23-chivalric-dominance.png "23-chivalric-dominance.png")


[Image: Chivalric Dominance: a little preview of the Gallant trait]  

### Knight Army Modifiers​

*“He has many men about him and is himself the best of fighters, and is not at a loss for wise counsel.”* - The Laxdæla Saga  

Before closing things out, let’s take a moment to explain Accolade effects, such as the new Knight Army Modifier. Wherever you see this term, it means your Acclaimed Knight will improve an army simply by being in it. There’s no requirement for the Acclaimed Knight to be the Army’s commander.  

Mouse over the Acclaimed Knight icon (helmet with the lil’ colorful scarf) on the army containing your Acclaimed Knight to see what modifiers are being applied to the army by Acclaimed Knights.  

![24-skirmishing-backup.png](https://forumcontent.paradoxplaza.com/public/959522/24-skirmishing-backup.png "24-skirmishing-backup.png")


[Image: This commander’s got a bit of skirmishing backup]  

### Everybody Loves Men-at-Arms​

When you choose a Men-at-Arms-boosting Accolade as a Primary Attribute and level it up, you’ll unlock a fun reward: special, extra-strong Men-at-Arms.  

Only one Regiment of these can be recruited and they have a limited troop count. However, their high base stats synchronize well with your Acclaimed Knight’s relevant modifiers and the new bonuses from stationing Regiments in your Holdings. Furthermore, these Retinue MaA perform better in appropriate terrains, they are *twice* as good at countering, and some of them receive stat increases as the Cultural Eras go by.  

Here’s a taste. And it’s just lowly skirmishers with bonuses from game start, because I’m an irrepressible tease.  

![25-skirmisher-no-accolade.png](https://forumcontent.paradoxplaza.com/public/959523/25-skirmisher-no-accolade.png "25-skirmisher-no-accolade.png")

![26-skirmisher-accolade.png](https://forumcontent.paradoxplaza.com/public/959524/26-skirmisher-accolade.png "26-skirmisher-accolade.png")


[Image: Left: regular skirmishers. Right: skirmishers unlocked by a high-ranked Skirmisher Accolade. Bear in mind effects from Knight Army Modifiers aren’t visible here]  

### A Knight’s Own Dev Diary of Chivalry​

That about wraps it up! I’d love to leave you with one last wise quote from de Charny, who may or may not be a greater knight than a certain Willy Marshall or Rodrigo de Vivar:  

*“Avoid quarrels.”*  

Thanks for reading!

 

#### Attachments

- [![03-outrider.png](https://forumcontent.paradoxplaza.com/thumbnail/public/959500/03-outrider.png)](https://forum.paradoxplaza.com/forum/attachments/03-outrider-png.971998/)
  
  03-outrider.png
  262,1 KB

 · Views: 0

<!-- artifact:reactions:start -->
- 118 Love
- 95 Like
- 14 (unlabeled — rendered as base64 data URI)
- 10 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
- 2 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)**
Role: Community Manager
Badges: 102
Messages: 642
Reaction score: 17,753

*[Full game-badge icon list of 36 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
