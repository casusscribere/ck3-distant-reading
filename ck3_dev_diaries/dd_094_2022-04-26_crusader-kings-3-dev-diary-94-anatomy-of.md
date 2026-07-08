---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1522115/"
forum_thread_id: 1522115
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 94
title: "Crusader Kings 3 Dev Diary #94 - Anatomy of a Struggle"
dd_date: 2022-04-26
author_handle: Wokeg
expansion: Fate of Iberia
patch: Patch 1.6 (Castle)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 5141
inline_image_count: 6
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1522115'
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
    location: raw_lines_~28_to_117
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_119_to_120
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_451_to_455
    action: preserved_and_flagged
    counts:
      Like: 78
      Love: 18
      (unlabeled — rendered as base64 data URI): 1
      Haha: 1
    note: Reactions block parsed; 3 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_532_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Crusader Kings 3 Dev Diary #94 - Anatomy of a Struggle

<!-- artifact:thread_metadata:start -->
- Thread starter [Wokeg](https://forum.paradoxplaza.com/forum/members/wokeg.1325927/)
- Start date [Apr 26, 2022](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-94-anatomy-of-a-struggle.1522115/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-94-anatomy-of-a-struggle.1522115/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-94-anatomy-of-a-struggle.1522115/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-94-anatomy-of-a-struggle.1522115/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22941](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-93-turmoil-in-the-peninsula.1521199/ "CK3 Dev Diary #93 - Turmoil in the Peninsula") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-95-flavor-of-iberia.1522983/ "Crusader Kings 3 Dev Diary #95 - Flavor of Iberia")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-94-anatomy-of-a-struggle.1522115/?prdxDevPosts=1)

- [Apr 26, 2022](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-94-anatomy-of-a-struggle.1522115/post-28234612)
- [Replies: 227](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-94-anatomy-of-a-struggle.1522115/#posts)


- [/forum/developer-diary/crusader-kings-3-dev-diary-94-anatomy-of-a-struggle.1522115/post-28234612](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-94-anatomy-of-a-struggle.1522115/post-28234612)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/28234612/bookmark "Bookmark")

## **Crusader Kings 3 Dev Diary #94 - Anatomy of a Struggle**​

Welcome comrades, to a dev diary I’ve been champing at the bit to write for months! Today, we’re going to be talking about the new struggle feature - what it is, how we’ve used it, and how it all *works*.  

## The Basic Pitch​

A struggle is a long-form conflict (generally not just a war, though they likely include them) covering a particular chunk of the map. They have different phases, each of which have different variant gameplay rules (e.g., “holy wars are disabled”, “characters of different religions may marry without”, or “Jerusalem can’t declare or be declared war on”).  

Phases progress between each other by way of catalysts, specific gameplay actions (“declare war on an involved character”, “two involved characters become soulmates”, etc.) that accrue points towards a future phase. When enough points are accrued, the phase changes to the new one.  

Struggles can be resolved, permanently affecting their area in some way, through dramatic and difficult ending decisions.  

They are assumed to last at least a couple of centuries: a conqueror carving out a new realm from the ruins of an old giant wouldn’t be a struggle by itself, but if it includes dramatic aftershocks that last for generations, then it just might be.  

## Philosophy​

So why are we introducing this mechanic attached to a flavour pack? Well, simply put, we didn’t think we could do the historical realities of Iberia justice without *something* like this.  

The changing moods and temperaments of the peninsula over different decades, the way particular activities fluctuated between oddly permissive (by the standards of much of the rest of the world) and intensely strict, the role of notable characters and their policies in shaping the shifting tides of public opinion whether intentionally or not…  

Medieval Iberia is just such a fascinating smorgasbord of mercurial special rules that we had to create a system that would allow us to model them, one that guided roleplay whilst giving it consequences, and provided default end goals for players other than just conquering all of Hispania.  

Though Iberia badly needed such a thing, it would have been a waste to create a system tailored for *only* Iberia. Complex and shifting local circumstances and long-form conflicts that don’t always take the form of actively-prosecuted warfare are things seen in many parts of the world, and a setting-agnostic system that catered to the peninsula but could be easily repurposed elsewhere seemed like a very worthwhile project to spend time on.  

So let’s get into how it works!  

## Involvement​

Struggles are, first and foremost, local things. Local to large areas (Iberia, for instance, is a decently sized little peninsula), but still local. The most basic thing that defines them, then, is the struggle region - a predefined group of titles that the rules of the struggle apply within.  

For FoI’s struggle, we’ve used the ol’ reliable world_europe_west_iberia region that’s been in the title since launch, but any region or combination of regions can be defined in the appropriate parameter. At the moment, these are static and only take regions, but we’re considering other options (e.g., titles, regions selected as part of the starting effect, etc.) for the future.  

![0000.PNG](https://forumcontent.paradoxplaza.com/public/820106/0000.PNG "0000.PNG")



Cultures and faiths are regarded as either involved or not. This defines whether a specific culture or faith is seen as being a part of the “in-group” for the region, even when members of that in-group may occasionally (or frequently) be very hostile to each other. For the Iberian Struggle, for instance, a Castilian and an Andalusian both understand the changing nature of the peninsula instinctively in a way that an Anglo-Saxon would struggle to acclimate to.  

Cultures become involved either on first starting a struggle, manually via script, or automatically when a certain percentage of their total counties are within the struggle region (the number is set per struggle, currently at 80% for the Iberian Struggle).  

Hybrids and divergent cultures automatically become involved if they convert at least one county within the region on creation.  

Neither cultures nor faiths lose their involvement automatically. Once they’re in, they’re in permanently, unless manually removed via script. For Fate of Iberia, this is necessary to keep the ruling class of al-Andalus, predominantly culturally insular families of Arabs or Berbers, involved, but it’s generally there to prevent wonky behaviour with struggles incorporating cultures and faiths from *beyond* their region who don’t actually have county within it.  

A simpler example would be a hypothetical Anglo-Norman struggle for after the Conquest. We’d probably want to set Norman up as an involved culture, and wouldn’t want them to immediately become uninvolved because there are no Norman counties in the British Isles.  

### But Characters Tho?​

Within the region, characters are defined by their *personal* involvement: the degree to which they’re considered part of the ongoing medley of social and cultural fluctuations that define an active struggle, and so how other characters (and counties) treat them. There are three levels to involvement:  


- Involved
- Interloper
- Uninvolved

Involved characters are those who are wholeheartedly engaged in the unique power dynamics of the struggle, and seen as insiders within the region. They may differ *wildly* from other involved characters, but involved characters are generally considered to appreciate the minutiae that make a struggle play differently from the rest of the world. Both their culture and faith must be flagged as being involved in the struggle, and either their capital is located within the struggle region or, if they’re unlanded, they’re physically there.  

Interlopers are active within a struggle’s region but don’t *quite* grasp exactly how or why people from the region act the way they do. They generally don’t benefit from variant struggle rules as much as involved characters, but also aren’t as heavily restricted by them. Either their culture, their faith, or both are not flagged as being involved in the struggle, but their capital (or physical location if landless) is located within the region.  

Uninvolved characters are outsiders and outlanders. Their concerns are remote to the struggle region, and even if they’re originally from that region, their isolation from it makes them lose touch with its subtleties and current events. Regardless of culture or faith, if their capital is located outside of the struggle region (or if they’re landless and physically not there), a character is considered uninvolved in that struggle. Uninvolved characters are generally expected to take penalties for holding counties within a struggle region, encouraging them to either delegate to vassals with a better level of involvement, or else getting more involved themselves.  

![0001.PNG](https://forumcontent.paradoxplaza.com/public/820107/0001.PNG "0001.PNG")



## Phases​

Alright, so we know how a struggle covers an area, and how people are divided up into categories within that area. What do these categories and this area actually *do*?  

For that, we need to look to phases.  

Each phase reflects a sort of mood or temperament within a struggle region specific to that struggle, the outcome of many prior actions leading to a shifting tide of general opinion about what is and isn’t acceptable. Maybe some things that were taboo become mainstream for a time, and things otherwise considered acceptable are baulked at by even very conservative characters.  

Though we’ll talk about how exactly you transition between phases a bit more in a moment, it’s worth noting that each phase has at least one (and usually more) *future* phase predefined for it, a phase that actions take in the course of play will gradually move the region’s “mood” towards.  

Within the Iberian Struggle, phases are on a loosely even cycle: though there’s some lateral movement and backtracking possible, they mostly move evenly in a circle. This is purely a design choice, and more esoteric flows are entirely scriptable.  

### Manifesting the Mood​

The actual effects of each phase can be split into three broad categories - parameters, character modifiers, and county modifiers. These are then further split by the involvement of different characters.  

Parameters work similarly to doctrine parameters in faiths, or tradition parameters for cultures. They’re special rules, entirely defined within script (and so fully moddable) that can be referred to elsewhere in script to unlock unique content, provide special exemptions, or block off specific actions.  

For example: in one phase, involved characters might be able to intermarry between faiths, in another, interlopers might receive cheaper holy wars whilst involved characters have them blocked entirely, and in both uninvolved characters may be blocked from culture converting involved cultures.  

![0002.PNG](https://forumcontent.paradoxplaza.com/public/820108/0002.PNG "0002.PNG")



As with other breeds of parameter, struggle parameters are identified purely by their exact spelling and can thus be reused simply by duplicating them, either within a struggle or in other struggles, making them very versatile rules.  

Character modifiers can be applied directly to involved or interloper characters. This generally chiefly affects involved characters, making some things easier and others harder, but we also use it to let interlopers occasionally have an easier time of bending or breaking local rules. Though these are our current guidelines, since these are all entirely scriptable, they can be changed according to the tonal needs of any given struggle.  

Uninvolved characters do not have a character modifier slot - we don’t want characters in India getting negative modifiers for not being involved or interlopers in a struggle in Iberia!  

Finally, we have county modifiers. These are applied to any county in the struggle region according to the direct holder of each county and their involvement; they generally have situational variables depending on phase for involved characters, mild to moderate debuffs for interlopers, and moderate to heavy debuffs for uninvolved characters.  

## Catalysts​

Transitioning from a phase to any of its future phases requires the activation of *catalysts*: notable events, gameplay actions, and consequences to existing mechanics that drive the current phase towards a specific future phase.  

Catalysts themselves can be anything. A war being declared, a type of character being seduced, a certain type of scheme failing, and so on. They’re set inside a phase’s future phase block, and, as with other elements of struggles, are entirely scriptable. Virtually any effect block in the entire title can be made into a catalyst with a bit of thought.  

Whenever a catalyst is activated, meaning that the thing that sets them happens, the current phase gains points towards the future phase that that catalyst was tied to (for instance, a notable interfaith marriage might help an uncertainty-focused phase gain points towards a tolerance-focused phase). Catalysts themselves are repeatable and the points they give vary with the difficulty of the catalyst in question - two notable characters becoming soulmates might well be worth more points than a notable character being executed, for instance.  

Points for put into simple tallies: when one tally for a future phase is met, that future phase becomes the new current phase, though there’s a grace period of a month before the actual switch.  

On the off chance that all of the dozens or hundreds of characters involved in a struggle are being *incomprehensibly* boring, we should note the existence of one special catalyst: the passage of time. Every phase has a default future phase, and receives a single point per year towards that phase’s tally, representing the natural trend of public discourse towards particular conclusions. This can (and essentially always will) be overridden or exacerbated by more dramatic catalysts being activated, but even in very calm struggle, change is *always* coming.  

## Ending Decisions​

A core part of the identity of struggles is that they’re not things that can be solved just by painting the map - after all, if they were, then the Iberian Struggle would’ve ended in its first decade when Musa ibn Nusayr had essentially subjugated the entire peninsula.  

We wanted to provide more difficult and interesting goals for ending a struggle than just conquering the whole struggle region. After all, it really doesn’t matter if you’ve conquered everyone if that hasn’t dealt with the underlying societal causes besetting a struggle locale.  

Ending decisions are our solution to this, being major, demanding decisions with consequences for the entire struggle region when taken and usually pretty intricate requirements.  

In order for a struggle to be endable through the usual flow, at least one phase must have an ending decision defined, though they can be ended manually through script also. The Iberian Struggle has three ending decisions, each tied (both mechanically and thematically) to a different phase).  

## The Iberian Struggle​

To finish up, let’s take a look at the new Iberian Struggle’s design (though I’ll put an obligatory reminder that this stuff isn’t final and that we generally continue to adjust things as we balance and playtest).  

The Iberian Struggle’s phases are Opportunity, Hostility, Compromise, and Conciliation. Opportunity can lead to either Hostility or Conciliation, depending on how the peninsula’s leaders treat each other, whilst both Hostility and Conciliation respectively build or degrade towards Compromise, which in turn decays into Opportunity, starting the cycle again.  

In Opportunity, Iberia is approaching a stage of uncertainty after notable spikes (hostile or friendly) in prior relations between faiths and cultures have abated. Struggle modifiers and parameters make war easier and cheaper, changing cultures and faiths easier and cheaper, but also unlock interfaith marriages and block off holy wars. Friendly interrelations between disparate characters activate catalysts guiding it towards Conciliation, whilst violent ones do the same for Hostility.  

For Hostility, aggressive actors have brought tensions to a simmering fever pitch, and even the slightest differences may be cause for aggressive persecution. The phase’s effects make wars cheaper and more brutal for all involved, reduce economic and technological progress, and increase the capacity of many characters for hostile schemes. Violence can’t persist forever though, and either efforts at building bridges or simple exhaustion will eventually bring even the most violent Hostility phase towards Compromise.  

Standing opposite Hostility is Conciliation, where pragmatic politicking builds bridges between even very disparate realms. Characters in this phase aren’t really tolerant by the modern meaning of the word, but many of the harsher biases of their time are temporarily dropped or ignored in the name of expediency. Wars become more expensive and truces longer, but there’s opportunity to unite against outsiders intervening in Iberian matters, and ruling over more multicultural and multifaith realms becomes easier and more beneficial.  

Periods of interreliance like this don’t generally last. Granted privileges decay, ignored biases relapse, and power-hungry nobles tear down bridges for short-term gain. Even the most wholeheartedly supported Conciliation phase decays towards Compromise eventually.  

Finally, Compromise. In this phase, Iberia has reached a point of equilibrium. Wars are less likely and most costly, but economic investment and other forms of passive stability are easier and better, whilst interfaith marriages flourish. The exhausted pragmatism of Compromise isn’t permanent, and will someday give rise to the cynical dynamism of Opportunity. The cycle begins anew.  

Naturally we’ve peppered all of this with phase-specific events, decisions, interactions, the odd CB, and so on. Most phases also add variant unlocking criteria to existing pieces of content, adjusting the circumstances under which things like the Claim Throne scheme or Found Holy Order decision can be used - most commonly temporarily extending them to characters who’d usually not have access.  

Say you don’t want to move on from a phase, though. Maybe you think Hostility’s the place for you, or you’d prefer a more permanent Conciliation, and want to break the endless cycle of social transmutation - well, unless you wanted permanent Opportunity, you’re in luck, because we’ve got ending decisions for Hostility, Compromise, and Conciliation.  

![0003.PNG](https://forumcontent.paradoxplaza.com/public/820109/0003.PNG "0003.PNG")



Hostility’s ending decision is *Dominance*, reflecting the final ascension of one of Iberia’s warring states to a position of not just military dominance, but social and spiritual hegemony.  

This gives your house an incredibly powerful modifier, making county and faith conversion within Iberia markedly faster, improving relations with those who share your faith or culture but markedly worsening them with other involved cultures or faiths, and making Holy Wars and Conquests cheaper and easier to access. It requires holding several important duchies, having a monocultural, monofaith primary kingdom, and being the only major player independent ruler in Iberia.  

![0004.PNG](https://forumcontent.paradoxplaza.com/public/820110/0004.PNG "0004.PNG")



Conciliation’s ending decision is *Détente*, making temporary accommodations into more permanent ones.  

Involved cultures gain a huge amount of cultural acceptance with each other, a house modifier that improves the opinion of different faiths and cultures, and several signature mechanics of the Conciliation phase become permanent for involved culture characters within Iberia: namely, interfaith marriage and disabled holy wars. Additionally, Iberian characters may join defensive wars for targets within Iberia against *any* aggressor from outside of Iberia.  

It requires a certain level of fame, being allied to *every* other independent involved Iberian ruler, and completely controlling an Iberian kingdom without controlling more than a certain fraction of Iberian territory.  

![0005.PNG](https://forumcontent.paradoxplaza.com/public/820111/0005.PNG "0005.PNG")



Compromise’s ending decision is *Status Quo*. Where Dominance is enforcing will and Détente finding accommodation, Status Quo is accepting that times have changed, that attempts to unite the peninsula are futile, and that its peoples and realms should go their separate ways and leave their neighbours be.  

Status Quo balkanises Iberia, transferring duchies to connected kingdoms if appropriate and making every kingdom within Iberia its own de jure empire whilst *permanently* destroying Hispania. Ruling houses across the former struggle region gain a modifier for two centuries making them better at fighting in lands of their own cultural heritage, whilst the capital counties of all independent rulers become strongholds for the next century. Some CBs within Iberia become more expensive.  

The requirements for Status Quo are a bit byzantine, essentially because it functions as the opt out decision if Dominance or Détente prove too difficult to work towards. If Iberia can’t be subjugated or coerced into cooperation then, in extremis, it can always be *destroyed*.  

## Future Use​

The Iberian Struggle is our first go at a struggle system, and it’s one we’re fairly pleased with. That said, we’ve certainly taken note of how the feature seems to have caught the popular imagination over the last week or so, and we’re very interested to hear your thoughts now that there’s a bit more information available. Needless to say, modders will be able to utilise this mechanic and share their creations from the release of 1.6 onwards.  

So, are there parts of the system you’d like to see refined and made more flexible? What are the struggles *you’d* like to see made in future? What’s your jankiest idea for hope for how to use the struggle system?  

As ever, I’ll be around in the thread for the next hour or so to answer your queries.

 

[Reply](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-94-anatomy-of-a-struggle.1522115/add-reply "Reply, quoting this message")

[Report](https://forum.paradoxplaza.com/forum/posts/28234612/report)

Click to expand...

[![Wokeg](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/dev/m/stellaris_dev_avatar_arthropoid_11.png)](https://forum.paradoxplaza.com/forum/members/wokeg.1325927/)

Written by

### [Wokeg](https://forum.paradoxplaza.com/forum/members/wokeg.1325927/)

Former CK3 Experienced Game Designer

-

Messages
528

-

Reaction score
15.169

- [1](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-94-anatomy-of-a-struggle.1522115/)
- [2](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-94-anatomy-of-a-struggle.1522115/page-2#posts)
- [3](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-94-anatomy-of-a-struggle.1522115/page-3#posts)
- …
  
  #### Go to page
  
  Go

- [12](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-94-anatomy-of-a-struggle.1522115/page-12#posts)
[Next](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-94-anatomy-of-a-struggle.1522115/page-2#posts)

1 of 12

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-94-anatomy-of-a-struggle.1522115/page-2#posts) [Last](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-94-anatomy-of-a-struggle.1522115/page-12#posts "Last")

[Sort by date](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-94-anatomy-of-a-struggle.1522115/) [Sort by reaction score](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-94-anatomy-of-a-struggle.1522115/?order=prdx_dd_reaction_score)

[![Trunting](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/majesty2_avatars/Heroes/s/majesty2_avatar_63.png)](https://forum.paradoxplaza.com/forum/members/trunting.476240/)

#### [Trunting](https://forum.paradoxplaza.com/forum/members/trunting.476240/)

##### General

**95 Badges**

Apr 14, 2012

1.943

4.742

- ![Crusader Kings II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_forumicon.png "Crusader Kings II")
- ![Semper Fi](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/sefi.png "Semper Fi")
- ![Rome Gold](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/RomeGold.png "Rome Gold")
- ![Hearts of Iron III Collection](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/hoi3col_medal.png "Hearts of Iron III Collection")
- ![Hearts of Iron III: Their Finest Hour](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/TFH_forumicon.png "Hearts of Iron III: Their Finest Hour")
- ![For the Motherland](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/FTM1.png "For the Motherland")
- ![Hearts of Iron III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/hoi3_forum_icon.gif "Hearts of Iron III")
- ![Stellaris: Ancient Relics](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellarisrelics.png "Stellaris: Ancient Relics")
- ![Age of Wonders: Planetfall - Revelations](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/AoWrevelationsicon.png "Age of Wonders: Planetfall - Revelations")
- ![Imperator: Rome Sign Up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Imperatorsignup.png "Imperator: Rome Sign Up")
- ![Crusader Kings II: Holy Fury](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/holy_fury_nonPO.png "Crusader Kings II: Holy Fury")
- ![Europa Universalis IV: Dharma](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/dharmaicon.png "Europa Universalis IV: Dharma")
- ![Europa Universalis IV: Rule Britannia](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/rule_britania_icon.png "Europa Universalis IV: Rule Britannia")
- ![Stellaris: Apocalypse](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/apocalypse_forum_icon2.png "Stellaris: Apocalypse")
- ![Stellaris: Humanoids Species Pack](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/humanoid_forumicon.png "Stellaris: Humanoids Species Pack")
- ![Hearts of Iron IV: Expansion Pass](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/hoi_tiger_forum_icon.png "Hearts of Iron IV: Expansion Pass")
- ![Europa Universalis IV: Cradle of Civilization](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/EUIV_CoC.png "Europa Universalis IV: Cradle of Civilization")
- ![Age of Wonders II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/AoW2_forum_badge.png "Age of Wonders II")
- ![Age of Wonders](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/AoW1_forum_badge.png "Age of Wonders")
- ![Age of Wonders III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/AoW3_forum_badge.png "Age of Wonders III")
- ![Tyranny - Bastards Wound](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Tyr_bw.png "Tyranny - Bastards Wound")
- ![Hearts of Iron IV: Death or Dishonor](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/HoI4DoD.png "Hearts of Iron IV: Death or Dishonor")
- ![Europa Universalis IV: Mandate of Heaven](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/moh_forum_icon.png "Europa Universalis IV: Mandate of Heaven")
- ![Crusader Kings II: Monks and Mystics](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/monksandmystics.png "Crusader Kings II: Monks and Mystics")
- ![Hearts of Iron IV: Together for Victory](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/HoI4Tfv.png "Hearts of Iron IV: Together for Victory")
- ![Stellaris: Leviathans Story Pack](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/leviathans.png "Stellaris: Leviathans Story Pack")
- ![Hearts of Iron IV: Battle for the Bosporus](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/bftb.png "Hearts of Iron IV: Battle for the Bosporus")
- ![Hearts of Iron IV: No Compromise No Surrender](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/NCNS.png "Hearts of Iron IV: No Compromise No Surrender")
- ![Hearts of Iron IV: Graveyard of Empires](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/goe_forum_icon.png "Hearts of Iron IV: Graveyard of Empires")
- ![Hearts of Iron IV: Götterdämmerung](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/gtd.png "Hearts of Iron IV: Götterdämmerung")
- ![Hearts of Iron IV: Arms Against Tyranny](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/AAT_forum_icon_16x16.png "Hearts of Iron IV: Arms Against Tyranny")
- ![Hearts of Iron IV: No Step Back](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/NSB_forum_icon_16x16.png "Hearts of Iron IV: No Step Back")
- ![Hearts of Iron IV: By Blood Alone](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/BBA_forum_icon_16x16.png "Hearts of Iron IV: By Blood Alone")
- ![Victoria 3 Sign Up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/v3_signup_forum_icon.png "Victoria 3 Sign Up")
- ![Stellaris: Nemesis](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/nemesis.png "Stellaris: Nemesis")
- ![Stellaris: Necroids](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellaris_forumicon_necroids.png "Stellaris: Necroids")
- ![Age of Wonders: Planetfall](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/aowstandard.png "Age of Wonders: Planetfall")
- ![Crusader Kings III: Royal Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3-royal.png "Crusader Kings III: Royal Edition")
- ![Crusader Kings III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3.png "Crusader Kings III")
- ![Imperator: Rome - Magna Graecia](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/MagnGraeciaIcon.png "Imperator: Rome - Magna Graecia")
- ![Stellaris: Federations](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/FederationsIcon.png "Stellaris: Federations")
- ![Hearts of Iron IV: La Resistance](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/HoILRicon.png "Hearts of Iron IV: La Resistance")
- ![Tyranny: Archon Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/tyr_arc.png "Tyranny: Archon Edition")
- ![Stellaris: Lithoids](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/lithoids_forum_badge.png "Stellaris: Lithoids")
- ![Age of Wonders: Planetfall Sign Up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/planetfallsignup.png "Age of Wonders: Planetfall Sign Up")
- ![Tyranny: Gold Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/tyr_ove.png "Tyranny: Gold Edition")
- ![Darkest Hour](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/DHicon.gif "Darkest Hour")
- ![Europa Universalis IV](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_forumicon.png "Europa Universalis IV")
- ![Victoria 2](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/vic2.png "Victoria 2")
- ![Warlock 2: The Exiled](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/warlock2_forum_icon.png "Warlock 2: The Exiled")

[](javascript:;)

- [Apr 26, 2022](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-94-anatomy-of-a-struggle.1522115/post-28234845)


- [/forum/developer-diary/crusader-kings-3-dev-diary-94-anatomy-of-a-struggle.1522115/post-28234845](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-94-anatomy-of-a-struggle.1522115/post-28234845)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/28234845/bookmark "Bookmark")
- [#2](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-94-anatomy-of-a-struggle.1522115/post-28234845)

I would like to see an investiture struggle.

<!-- artifact:reactions:start -->
- 78 Like
- 18 Love
- 17 (unlabeled — rendered as base64 data URI)
- 1 Haha
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
