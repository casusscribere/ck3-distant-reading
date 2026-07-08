---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1522115/"
forum_thread_id: 1522115
content_type: reply_thread
parent_dd_file: dd_094_2022-04-26_crusader-kings-3-dev-diary-94-anatomy-of.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 94
title: "Crusader Kings 3 Dev Diary #94 - Anatomy of a Struggle"
dd_date: 2022-04-26
expansion: Fate of Iberia
patch: Patch 1.6 (Castle)
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 12
reply_count: 228
participant_count: 170
reply_date_first: 2022-04-26
reply_date_last: 2022-05-16
body_word_count: 22118
inline_image_count: 0
quoted_span_count: 121
extraction_rationale: |
  Full reply thread captured live via Claude in Chrome (article.message bodies).
  Quote blocks split into artifact:quote spans and excluded from word counts.
  Usernames replaced by stable per-thread participant ids; the dev-diary OP is
  excluded (see parent_dd_file).
notes_for_analyst: |
  Community-voice counterpart to the linked dev diary. Strip YAML + artifact
  comments before tokenizing, exactly as for dd_*.md.
---

# Reply thread — Crusader Kings 3 Dev Diary #94 - Anatomy of a Struggle

*228 replies from 170 participants across 12 pages*

## Reply 1 — participant_001 · 2022-04-26 · post-28234612

Crusader Kings 3 Dev Diary #94 - Anatomy of a Struggle​Welcome comrades, to a dev diary I’ve been champing at the bit to write for months! Today, we’re going to be talking about the new struggle feature - what it is, how we’ve used it, and how it all works. The Basic Pitch​A struggle is a long-form conflict (generally not just a war, though they likely include them) covering a particular chunk of the map. They have different phases, each of which have different variant gameplay rules (e.g., “holy wars are disabled”, “characters of different religions may marry without”, or “Jerusalem can’t declare or be declared war on”). Phases progress between each other by way of catalysts, specific gameplay actions (“declare war on an involved character”, “two involved characters become soulmates”, etc.) that accrue points towards a future phase. When enough points are accrued, the phase changes to the new one. Struggles can be resolved, permanently affecting their area in some way, through dramatic and difficult ending decisions. They are assumed to last at least a couple of centuries: a conqueror carving out a new realm from the ruins of an old giant wouldn’t be a struggle by itself, but if it includes dramatic aftershocks that last for generations, then it just might be. Philosophy​So why are we introducing this mechanic attached to a flavour pack? Well, simply put, we didn’t think we could do the historical realities of Iberia justice without something like this. The changing moods and temperaments of the peninsula over different decades, the way particular activities fluctuated between oddly permissive (by the standards of much of the rest of the world) and intensely strict, the role of notable characters and their policies in shaping the shifting tides of public opinion whether intentionally or not… Medieval Iberia is just such a fascinating smorgasbord of mercurial special rules that we had to create a system that would allow us to model them, one that guided roleplay whilst giving it consequences, and provided default end goals for players other than just conquering all of Hispania. Though Iberia badly needed such a thing, it would have been a waste to create a system tailored for only Iberia. Complex and shifting local circumstances and long-form conflicts that don’t always take the form of actively-prosecuted warfare are things seen in many parts of the world, and a setting-agnostic system that catered to the peninsula but could be easily repurposed elsewhere seemed like a very worthwhile project to spend time on. So let’s get into how it works! Involvement​Struggles are, first and foremost, local things. Local to large areas (Iberia, for instance, is a decently sized little peninsula), but still local. The most basic thing that defines them, then, is the struggle region - a predefined group of titles that the rules of the struggle apply within. For FoI’s struggle, we’ve used the ol’ reliable world_europe_west_iberia region that’s been in the title since launch, but any region or combination of regions can be defined in the appropriate parameter. At the moment, these are static and only take regions, but we’re considering other options (e.g., titles, regions selected as part of the starting effect, etc.) for the future. { "lightbox_close": "Close", "lightbox_next": "Next", "lightbox_previous": "Previous", "lightbox_error": "The requested content cannot be loaded. Please try again later.", "lightbox_start_slideshow": "Start slideshow", "lightbox_stop_slideshow": "Stop slideshow", "lightbox_full_screen": "Full screen", "lightbox_thumbnails": "Thumbnails", "lightbox_download": "Download", "lightbox_share": "Share", "lightbox_zoom": "Zoom", "lightbox_new_window": "New window", "lightbox_toggle_sidebar": "Toggle sidebar" } Cultures and faiths are regarded as either involved or not. This defines whether a specific culture or faith is seen as being a part of the “in-group” for the region, even when members of that in-group may occasionally (or frequently) be very hostile to each other. For the Iberian Struggle, for instance, a Castilian and an Andalusian both understand the changing nature of the peninsula instinctively in a way that an Anglo-Saxon would struggle to acclimate to. Cultures become involved either on first starting a struggle, manually via script, or automatically when a certain percentage of their total counties are within the struggle region (the number is set per struggle, currently at 80% for the Iberian Struggle). Hybrids and divergent cultures automatically become involved if they convert at least one county within the region on creation. Neither cultures nor faiths lose their involvement automatically. Once they’re in, they’re in permanently, unless manually removed via script. For Fate of Iberia, this is necessary to keep the ruling class of al-Andalus, predominantly culturally insular families of Arabs or Berbers, involved, but it’s generally there to prevent wonky behaviour with struggles incorporating cultures and faiths from beyond their region who don’t actually have county within it. A simpler example would be a hypothetical Anglo-Norman struggle for after the Conquest. We’d probably want to set Norman up as an involved culture, and wouldn’t want them to immediately become uninvolved because there are no Norman counties in the British Isles. But Characters Tho?​Within the region, characters are defined by their personal involvement: the degree to which they’re considered part of the ongoing medley of social and cultural fluctuations that define an active struggle, and so how other characters (and counties) treat them. There are three levels to involvement: Involved Interloper Uninvolved Involved characters are those who are wholeheartedly engaged in the unique power dynamics of the struggle, and seen as insiders within the region. They may differ wildly from other involved characters, but involved characters are generally considered to appreciate the minutiae that make a struggle play differently from the rest of the world. Both their culture and faith must be flagged as being involved in the struggle, and either their capital is located within the struggle region or, if they’re unlanded, they’re physically there. Interlopers are active within a struggle’s region but don’t quite grasp exactly how or why people from the region act the way they do. They generally don’t benefit from variant struggle rules as much as involved characters, but also aren’t as heavily restricted by them. Either their culture, their faith, or both are not flagged as being involved in the struggle, but their capital (or physical location if landless) is located within the region. Uninvolved characters are outsiders and outlanders. Their concerns are remote to the struggle region, and even if they’re originally from that region, their isolation from it makes them lose touch with its subtleties and current events. Regardless of culture or faith, if their capital is located outside of the struggle region (or if they’re landless and physically not there), a character is considered uninvolved in that struggle. Uninvolved characters are generally expected to take penalties for holding counties within a struggle region, encouraging them to either delegate to vassals with a better level of involvement, or else getting more involved themselves. Phases​Alright, so we know how a struggle covers an area, and how people are divided up into categories within that area. What do these categories and this area actually do? For that, we need to look to phases. Each phase reflects a sort of mood or temperament within a struggle region specific to that struggle, the outcome of many prior actions leading to a shifting tide of general opinion about what is and isn’t acceptable. Maybe some things that were taboo become mainstream for a time, and things otherwise considered acceptable are baulked at by even very conservative characters. Though we’ll talk about how exactly you transition between phases a bit more in a moment, it’s worth noting that each phase has at least one (and usually more) future phase predefined for it, a phase that actions take in the course of play will gradually move the region’s “mood” towards. Within the Iberian Struggle, phases are on a loosely even cycle: though there’s some lateral movement and backtracking possible, they mostly move evenly in a circle. This is purely a design choice, and more esoteric flows are entirely scriptable. Manifesting the Mood​The actual effects of each phase can be split into three broad categories - parameters, character modifiers, and county modifiers. These are then further split by the involvement of different characters. Parameters work similarly to doctrine parameters in faiths, or tradition parameters for cultures. They’re special rules, entirely defined within script (and so fully moddable) that can be referred to elsewhere in script to unlock unique content, provide special exemptions, or block off specific actions. For example: in one phase, involved characters might be able to intermarry between faiths, in another, interlopers might receive cheaper holy wars whilst involved characters have them blocked entirely, and in both uninvolved characters may be blocked from culture converting involved cultures. As with other breeds of parameter, struggle parameters are identified purely by their exact spelling and can thus be reused simply by duplicating them, either within a struggle or in other struggles, making them very versatile rules. Character modifiers can be applied directly to involved or interloper characters. This generally chiefly affects involved characters, making some things easier and others harder, but we also use it to let interlopers occasionally have an easier time of bending or breaking local rules. Though these are our current guidelines, since these are all entirely scriptable, they can be changed according to the tonal needs of any given struggle. Uninvolved characters do not have a character modifier slot - we don’t want characters in India getting negative modifiers for not being involved or interlopers in a struggle in Iberia! Finally, we have county modifiers. These are applied to any county in the struggle region according to the direct holder of each county and their involvement; they generally have situational variables depending on phase for involved characters, mild to moderate debuffs for interlopers, and moderate to heavy debuffs for uninvolved characters. Catalysts​Transitioning from a phase to any of its future phases requires the activation of catalysts: notable events, gameplay actions, and consequences to existing mechanics that drive the current phase towards a specific future phase. Catalysts themselves can be anything. A war being declared, a type of character being seduced, a certain type of scheme failing, and so on. They’re set inside a phase’s future phase block, and, as with other elements of struggles, are entirely scriptable. Virtually any effect block in the entire title can be made into a catalyst with a bit of thought. Whenever a catalyst is activated, meaning that the thing that sets them happens, the current phase gains points towards the future phase that that catalyst was tied to (for instance, a notable interfaith marriage might help an uncertainty-focused phase gain points towards a tolerance-focused phase). Catalysts themselves are repeatable and the points they give vary with the difficulty of the catalyst in question - two notable characters becoming soulmates might well be worth more points than a notable character being executed, for instance. Points for put into simple tallies: when one tally for a future phase is met, that future phase becomes the new current phase, though there’s a grace period of a month before the actual switch. On the off chance that all of the dozens or hundreds of characters involved in a struggle are being incomprehensibly boring, we should note the existence of one special catalyst: the passage of time. Every phase has a default future phase, and receives a single point per year towards that phase’s tally, representing the natural trend of public discourse towards particular conclusions. This can (and essentially always will) be overridden or exacerbated by more dramatic catalysts being activated, but even in very calm struggle, change is always coming. Ending Decisions​A core part of the identity of struggles is that they’re not things that can be solved just by painting the map - after all, if they were, then the Iberian Struggle would’ve ended in its first decade when Musa ibn Nusayr had essentially subjugated the entire peninsula. We wanted to provide more difficult and interesting goals for ending a struggle than just conquering the whole struggle region. After all, it really doesn’t matter if you’ve conquered everyone if that hasn’t dealt with the underlying societal causes besetting a struggle locale. Ending decisions are our solution to this, being major, demanding decisions with consequences for the entire struggle region when taken and usually pretty intricate requirements. In order for a struggle to be endable through the usual flow, at least one phase must have an ending decision defined, though they can be ended manually through script also. The Iberian Struggle has three ending decisions, each tied (both mechanically and thematically) to a different phase). The Iberian Struggle​To finish up, let’s take a look at the new Iberian Struggle’s design (though I’ll put an obligatory reminder that this stuff isn’t final and that we generally continue to adjust things as we balance and playtest). The Iberian Struggle’s phases are Opportunity, Hostility, Compromise, and Conciliation. Opportunity can lead to either Hostility or Conciliation, depending on how the peninsula’s leaders treat each other, whilst both Hostility and Conciliation respectively build or degrade towards Compromise, which in turn decays into Opportunity, starting the cycle again. In Opportunity, Iberia is approaching a stage of uncertainty after notable spikes (hostile or friendly) in prior relations between faiths and cultures have abated. Struggle modifiers and parameters make war easier and cheaper, changing cultures and faiths easier and cheaper, but also unlock interfaith marriages and block off holy wars. Friendly interrelations between disparate characters activate catalysts guiding it towards Conciliation, whilst violent ones do the same for Hostility. For Hostility, aggressive actors have brought tensions to a simmering fever pitch, and even the slightest differences may be cause for aggressive persecution. The phase’s effects make wars cheaper and more brutal for all involved, reduce economic and technological progress, and increase the capacity of many characters for hostile schemes. Violence can’t persist forever though, and either efforts at building bridges or simple exhaustion will eventually bring even the most violent Hostility phase towards Compromise. Standing opposite Hostility is Conciliation, where pragmatic politicking builds bridges between even very disparate realms. Characters in this phase aren’t really tolerant by the modern meaning of the word, but many of the harsher biases of their time are temporarily dropped or ignored in the name of expediency. Wars become more expensive and truces longer, but there’s opportunity to unite against outsiders intervening in Iberian matters, and ruling over more multicultural and multifaith realms becomes easier and more beneficial. Periods of interreliance like this don’t generally last. Granted privileges decay, ignored biases relapse, and power-hungry nobles tear down bridges for short-term gain. Even the most wholeheartedly supported Conciliation phase decays towards Compromise eventually. Finally, Compromise. In this phase, Iberia has reached a point of equilibrium. Wars are less likely and most costly, but economic investment and other forms of passive stability are easier and better, whilst interfaith marriages flourish. The exhausted pragmatism of Compromise isn’t permanent, and will someday give rise to the cynical dynamism of Opportunity. The cycle begins anew. Naturally we’ve peppered all of this with phase-specific events, decisions, interactions, the odd CB, and so on. Most phases also add variant unlocking criteria to existing pieces of content, adjusting the circumstances under which things like the Claim Throne scheme or Found Holy Order decision can be used - most commonly temporarily extending them to characters who’d usually not have access. Say you don’t want to move on from a phase, though. Maybe you think Hostility’s the place for you, or you’d prefer a more permanent Conciliation, and want to break the endless cycle of social transmutation - well, unless you wanted permanent Opportunity, you’re in luck, because we’ve got ending decisions for Hostility, Compromise, and Conciliation. Hostility’s ending decision is Dominance, reflecting the final ascension of one of Iberia’s warring states to a position of not just military dominance, but social and spiritual hegemony. This gives your house an incredibly powerful modifier, making county and faith conversion within Iberia markedly faster, improving relations with those who share your faith or culture but markedly worsening them with other involved cultures or faiths, and making Holy Wars and Conquests cheaper and easier to access. It requires holding several important duchies, having a monocultural, monofaith primary kingdom, and being the only major player independent ruler in Iberia. Conciliation’s ending decision is Détente, making temporary accommodations into more permanent ones. Involved cultures gain a huge amount of cultural acceptance with each other, a house modifier that improves the opinion of different faiths and cultures, and several signature mechanics of the Conciliation phase become permanent for involved culture characters within Iberia: namely, interfaith marriage and disabled holy wars. Additionally, Iberian characters may join defensive wars for targets within Iberia against any aggressor from outside of Iberia. It requires a certain level of fame, being allied to every other independent involved Iberian ruler, and completely controlling an Iberian kingdom without controlling more than a certain fraction of Iberian territory. Compromise’s ending decision is Status Quo. Where Dominance is enforcing will and Détente finding accommodation, Status Quo is accepting that times have changed, that attempts to unite the peninsula are futile, and that its peoples and realms should go their separate ways and leave their neighbours be. Status Quo balkanises Iberia, transferring duchies to connected kingdoms if appropriate and making every kingdom within Iberia its own de jure empire whilst permanently destroying Hispania. Ruling houses across the former struggle region gain a modifier for two centuries making them better at fighting in lands of their own cultural heritage, whilst the capital counties of all independent rulers become strongholds for the next century. Some CBs within Iberia become more expensive. The requirements for Status Quo are a bit byzantine, essentially because it functions as the opt out decision if Dominance or Détente prove too difficult to work towards. If Iberia can’t be subjugated or coerced into cooperation then, in extremis, it can always be destroyed. Future Use​The Iberian Struggle is our first go at a struggle system, and it’s one we’re fairly pleased with. That said, we’ve certainly taken note of how the feature seems to have caught the popular imagination over the last week or so, and we’re very interested to hear your thoughts now that there’s a bit more information available. Needless to say, modders will be able to utilise this mechanic and share their creations from the release of 1.6 onwards. So, are there parts of the system you’d like to see refined and made more flexible? What are the struggles you’d like to see made in future? What’s your jankiest idea for hope for how to use the struggle system? As ever, I’ll be around in the thread for the next hour or so to answer your queries.

## Reply 2 — participant_002 · 2022-04-26 · post-28234845

I would like to see an investiture struggle.

## Reply 3 — participant_003 · 2022-04-26 · post-28234850

Could the struggle system be implemented to England during the Norse invasions?

## Reply 4 — participant_004 · 2022-04-26 · post-28234853

Is this like border conflicts but taken to the extreme?

## Reply 5 — participant_005 · 2022-04-26 · post-28234855

Very informative, thank you!

## Reply 6 — participant_006 · 2022-04-26 · post-28234865

Definitely would love to see some sort of struggle implemented for England, trying to swing it for the Anglo-Saxons/Normans/Norwegians. Perhaps if you're going from the earlier start one for the Norse Invasions would make more sense where it can end similar to Iberia with a status quo of smaller kingdoms.

## Reply 7 — participant_007 · 2022-04-26 · post-28234868

Ooooh, this is pretty great! Also, good to hear that this is gonna be a general mechanic

## Reply 8 — participant_008 · 2022-04-26 · post-28234877

Could you give some more examples of regions where the struggle system will be implemented in the 867 start date?

## Reply 9 — participant_009 · 2022-04-26 · post-28234878

This is quite fascinating! I look forward to seeing how this system can be adapted to other regions, and I feel that this is a relatively simple way to add alot of familiarity and flavour to any otherwise foreign region and time.

## Reply 10 — participant_010 · 2022-04-26 · post-28234890

Has something been done to make the Almohads and Almoravids intervene in the peninsula as they historically did?

## Reply 11 — participant_011 · 2022-04-26 · post-28234894

Well, I think the Danelaw/Anglo-Saxon struggle is something fans would like to see in the future, perhaps retrofitted into the Northern Lords pack. It wouldn't make sense to make a whole new Norse themed DLC just for that, unless it heavily focuses on the Anglo-Saxons and other cultures in England. Other than that, the struggle mechanic would fit literally anywhere where there are big groups of cultures and religions clashing. It's good stuff. As a side note, I haven't seen any new cloaks in any of the new screenshots, which I find just a tiny bit disappointing. I see a lot of them in the various new artworks though, which just makes me want them all the more. Are we not getting any?

## Reply 12 — participant_001 · 2022-04-26 · post-28234895

<!-- artifact:quote:start -->
> Trunting said: I would like to see an investiture struggle. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Skidofly said: Could the struggle system be implemented to England during the Norse invasions? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> X1Armor said: Is this like border conflicts but taken to the extreme? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Conor_GG said: Definitely would love to see some sort of struggle implemented for England, trying to swing it for the Anglo-Saxons/Normans/Norwegians. Perhaps if you're going from the earlier start one for the Norse Invasions would make more sense where it can end similar to Iberia with a status quo of smaller kingdoms. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> guglik0 said: Could you give some more examples of regions where the struggle system will be implemented in the 867 start date? Click to expand...
<!-- artifact:quote:end -->
Interesting choice! It's not at the moment, but it certainly could be. Personally I think the timeframe there is a little short for it, but it would depend on implementation. There's elements of that in the Iberian Struggle, but it doesn't, strictly speaking, have to be. I've seen this one crop up a lot in various public forums! Strictly speaking, no. At the moment there are no other regions where the struggle system will be implemented - Iberia is our first struggle. I've got a handful of personal favourites that I know I'd like to try and which those unfortunate enough to be within rambling distance of me are very well aware of, but I don't think I'm allowed to share those.

## Reply 13 — participant_012 · 2022-04-26 · post-28234896

Looks cool, have wanted something like this for ages.

## Reply 14 — participant_013 · 2022-04-26 · post-28234897

First off, I love the idea. I'd like to see it implemented for England in 1066, and the British Isles in 867. I think that would better channel the chaos of the Viking invasions, because right now it is too easy. Unless you have bad luck, you can always dominate and form the Kingdom of England before anyone dies, except maybe Aethelred. Second, I'd really love to see you guys work on a version, that can be triggerable. Like whenever the power balances in a region is massive messed up. Like if you conquer and form an empire where there wasn't one. Or if you remove the only powerful neighbor, and leave yourself as 10+ times stronger (at max troop capacity) than any of your neighbors. Beyond that, I think this would be a base to use to work on a mini crisis within Kingdoms and Empires for Female/Male inheritance (in one sex favored systems Ag/cognat preferences), regencies, and even bankruptcy. I could also, see a potential for succession struggles, since these were common, and could last years with people often ruling for months before being deposed by siblings or other relatives (To make these more dynamic, you could give the player an option to play as the winner of a succession struggle, similar to appointees for crusades).

## Reply 15 — participant_014 · 2022-04-26 · post-28234900

This looks incredible. Do struggles have the potential to naturally develop or will they be the result of fixed conditions simulating historical events. Are there any struggles outside of Iberia to begin with or are they too intensive to code? Might we expect a struggle to be a standard component of a Flavor Pack moving forward?

## Reply 16 — participant_015 · 2022-04-26 · post-28234901

I really like the concept and can't wait to see how it works out. Maybe if it works out quite well and could be expanded as a general feature for Empire under a dispute rather than an Iberia-specific one. However there is one thing, I might be a minority but this could be split into multiple DDs, and started the introduction a few weeks earlier. With more screenshots perhaps.

## Reply 17 — participant_012 · 2022-04-26 · post-28234906

<!-- artifact:quote:start -->
> Wokeg said: It's not at the moment, but it certainly could be. Personally I think the timeframe there is a little short for it, but it would depend on implementation. Click to expand...
<!-- artifact:quote:end -->
Maybe in a future expansion you could have a more explosive version of a struggle called a crisis?

## Reply 18 — participant_016 · 2022-04-26 · post-28234909

So... It seems to me that the most noticeable difference will be periods of no Holy Wars in Iberia. I wonder how that goes. BTW, we're not forced to become an Empire after dominating the peninsula, are we? I rather like being a King instead of an Emperor.

## Reply 19 — participant_017 · 2022-04-26 · post-28234912

Not sure if it's a good fit for the system, but maybe an adapted struggle system lends itself for southern France. Catharism and the Albigensian crusade were an important episode deciding the future of that region, but the integration of the Languedoc into France had a lot of interesting aspects to it (including family ties to the Kings of France and Aragon), and I'd love to see this complexity reflected in game mechanics that go beyond "me adopting Catharism, getting roflstomped by the pope".

## Reply 20 — participant_018 · 2022-04-26 · post-28234913

<!-- artifact:quote:start -->
> Wokeg said: Cultures and faiths are regarded as either involved or not. This defines whether a specific culture or faith is seen as being a part of the “in-group” for the region, even when members of that in-group may occasionally (or frequently) be very hostile to each other. For the Iberian Struggle, for instance, a Castilian and an Andalusian both understand the changing nature of the peninsula instinctively in a way that an Anglo-Saxon would struggle to acclimate to. Cultures become involved either on first starting a struggle, manually via script, or automatically when a certain percentage of their total counties are within the struggle region (the number is set per struggle, currently at 80% for the Iberian Struggle). Hybrids and divergent cultures automatically become involved if they convert at least one county within the region on creation. Neither cultures nor faiths lose their involvement automatically. Once they’re in, they’re in permanently, unless manually removed via script. For Fate of Iberia, this is necessary to keep the ruling class of al-Andalus, predominantly culturally insular families of Arabs or Berbers, involved, but it’s generally there to prevent wonky behaviour with struggles incorporating cultures and faiths from beyond their region who don’t actually have county within it. A simpler example would be a hypothetical Anglo-Norman struggle for after the Conquest. We’d probably want to set Norman up as an involved culture, and wouldn’t want them to immediately become uninvolved because there are no Norman counties in the British Isles. Click to expand...
<!-- artifact:quote:end -->
Hold on a second, you've explained how cultures can become involved later on in a struggle, but how can another *faith* become involved in a struggle after the struggle has begun? For example, if Haesteinn decides to invade Galicia in the Iberian Struggle, what does it take for Norse to become an involved faith?

## Reply 21 — participant_019 · 2022-04-26 · post-28234916

Feels like the Byzantines should be stuck in a permanent struggle!

## Reply 22 — participant_001 · 2022-04-26 · post-28234924

<!-- artifact:quote:start -->
> krissuyx said: Well, I think the Danelaw/Anglo-Saxon struggle is something fans would like to see in the future, perhaps retrofitted into the Northern Lords pack. It wouldn't make sense to make a whole new Norse themed DLC just for that, unless it heavily focuses on the Anglo-Saxons and other cultures in England. Other than that, the struggle mechanic would fit literally anywhere where there are big groups of cultures and religions clashing. It's good stuff. As a side note, I haven't seen any new cloaks in any of the new screenshots, which I find just a tiny bit disappointing. I see a lot of them in the various new artworks though, which just makes me want them all the more. Are we not getting any? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> oreopirate said: Second, I'd really love to see you guys work on a version, that can be triggerable. Like whenever the power balances in a region is massive messed up. Like if you conquer and form an empire where there wasn't one. Or if you remove the only powerful neighbor, and leave yourself as 10+ times stronger (at max troop capacity) than any of your neighbors. Beyond that, I think this would be a base to use to work on a mini crisis within Kingdoms and Empires for Female/Male inheritance (in one sex favored systems Ag/cognat preferences), regencies, and even bankruptcy. I could also, see a potential for succession struggles, since these were common, and could last years with people often ruling for months before being deposed by siblings or other relatives (To make these more dynamic, you could give the player an option to play as the winner of a succession struggle, similar to appointees for crusades). Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Stormbound5 said: This looks incredible. Do struggles have the potential to naturally develop or will they be the result of fixed conditions simulating historical events. Are there any struggles outside of Iberia to begin with or are they too intensive to code? Might we expect a struggle to be a standard component of a Flavor Pack moving forward? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> RhoxOS said: I really like the concept and can't wait to see how it works out. Maybe if it works out quite well and could be expanded as a general feature for Empire under a dispute rather than an Iberia-specific one. However there is one thing, I might be a minority but this could be split into multiple DDs, and started the introduction a few weeks earlier. With more screenshots perhaps. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> TheDungen said: Maybe in a future expansion you could have a more explosive version of a struggle called a crisis? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Magnificate said: BTW, we're not forced to become an Empire after dominating the peninsula, are we? I rather like being a King instead of an Emperor. Click to expand...
<!-- artifact:quote:end -->
I'm very sorry to say that Art tells me we do not have any cloaks planned for this DLC - we do, however, have some of the biggest and fanciest hats yet added to the title. Yeah, I'm rather interested in the possibilities of a more dynamically triggered region-agnostic struggle like this. We'd need to make the region variable, but that's doable... worth some thought on our part, at least. At the moment, it's just the Iberian Struggle. We may well see struggles in future flavour packs or expansions, but they're not a standard component for every DLC. Our first struggle is very much a result of fixed conditions (it technically starts in the history files in... I think 719?), but there's nothing stopping struggles from being set up to happen more naturalistically except for the preset region. Valid feedback, thank you! Well, we only just got struggles, so lets see how these pan out before we go talking about anything like that. You are not! Creating Hispania is locked behind resolving the struggle (to keep things a bit more interesting), but resolving the struggle does not automatically create Hispania.

## Reply 23 — participant_020 · 2022-04-26 · post-28234928

<!-- artifact:quote:start -->
> pardaloco said: Has something been done to make the Almohads and Almoravids intervene in the peninsula as they historically did? Click to expand...
<!-- artifact:quote:end -->
^This. Would be nice to make those invasions more likely (I think one of those already has an event in CK3), to shake things up. If it's too railroady, could be easily turned off by the game rules. Maybe make it similar to something like Turkic adventurers in CK2?

## Reply 24 — participant_021 · 2022-04-26 · post-28234929

Maybe a Catholic/Orthodox struggle?

## Reply 25 — participant_022 · 2022-04-26 · post-28234930

Maybe a struggle for a year or two for realms under partitions after previous ruler died? And where there will be three endings "dominance" where one person gets go rule all, "status quo" where everything remains the same just like after partition and "kinship" where you get alliances made with your siblings against outside threats?

## Reply 26 — participant_023 · 2022-04-26 · post-28234932

Do regions = empire level? I'd certainly like a struggle for the High Kingship mechanic for Ireland given that the provinces and even dynasties fighting for dominance in 867 are the same as those fighting in 1066. The ebb and flow of struggle could be altered by region specific activities such as hostage taking, making tributaries, dividing duchies amongst rivals (could be region specific for a certain phase), supporting certain churches against each other and perhaps in a later phase, the church in Rome. Other elements like placing your favoured candidates on rival thrones as well as forming grand alliances to keep other members in check could also work. Throw in feudalisation, Norse cities, and in a later stage, the English and you could have a struggle that could last 300 years.

## Reply 27 — participant_024 · 2022-04-26 · post-28234933

Are there mixed catalysts? Say, two characters of diferent faiths eloping together could both be seen as a positive act of overcoming differences at the same time that could be seen as a hostile action by one house head losing control over who their house members are marrying

## Reply 28 — participant_012 · 2022-04-26 · post-28234936

<!-- artifact:quote:start -->
> Wokeg said: Well, we only just got struggles, so lets see how these pan out before we go talking about anything like that. Click to expand...
<!-- artifact:quote:end -->
That's sort of my point. I like the concept and think that if it works well it's basic premisse could be useful in a lot of scenarios.

## Reply 29 — participant_025 · 2022-04-26 · post-28234938

Apart from the England - Normal struggle that everyone mentions, I would love to see a Norsemen - Slavic struggle. Also, a struggle in the holy land would be interesting. I hope that as time goes on, these struggles will be implemented and of course, some from the other parts of the world as India or Africa. I have no ideas for those regions tho.

## Reply 30 — participant_020 · 2022-04-26 · post-28234940

For the struggle examples, I think that post-4th crusade Byzantium is an easy fit for a mid/late game struggle appearing.

## Reply 31 — participant_012 · 2022-04-26 · post-28234946

<!-- artifact:quote:start -->
> Crusader_SVK_287 said: Apart from the England - Normal struggle that everyone mentions, I would love to see a Norsemen - Slavic struggle. Also, a struggle in the holy land would be interesting. I hope that as time goes on, these struggles will be implemented and of course, some from the other parts of the world as India or Africa. I have no ideas for those regions tho. Click to expand...
<!-- artifact:quote:end -->
What norsemen slavic struggle?

## Reply 32 — participant_026 · 2022-04-26 · post-28234955

I crave to have the struggle mechanic pop up In France, Germany and France after a foreign culture/religion (Islam) conquers these Christian areas. It'd be much more interesting than just blobbing all the area, or at least have some special mechanics caused by such a blob!

## Reply 33 — participant_027 · 2022-04-26 · post-28234956

Seems great! Keep up the good work! I agree with the guy who suggested the investiture struggle, but should be along with a rework with... well... investiture. About England, it seems a way too short timeframe to me, but I don't know. I'd like to see an Italian peninsula struggle, between all the duchies there.

## Reply 34 — participant_028 · 2022-04-26 · post-28234957

Looking forward to this! Is there a plan to use the struggle mechanism for more general events e.g. in case of a succession crisis?

## Reply 35 — participant_022 · 2022-04-26 · post-28234958

Also other struggles I can think of: - Jerusalem is a must tbh; - India - Central Europe can be either Christians Vs Pagans or Pagans Vs other Pagans. Especially for the Prussian region.

## Reply 36 — participant_029 · 2022-04-26 · post-28234964

Interesting. How easy will it be for the player to influence the Struggle? It feels like it will make playing Iberia easier. At the moment if you start off as Christian, you are constantly fighting holy wars. With the struggle, it feels like the tactic is go conciliation until you can build enough military power and then go hostile and holy war.

## Reply 37 — participant_013 · 2022-04-26 · post-28234967

<!-- artifact:quote:start -->
> Wokeg said: It's not at the moment, but it certainly could be. Personally I think the timeframe there is a little short for it, but it would depend on implementation. Click to expand...
<!-- artifact:quote:end -->
Just to toss my five cents at this, I would argue that such a struggle would extend up to 1085, when King Knut of Denmark basically gives up his claim to England. With a period of Compromise, with the Danelaw being Conciliation and Compromise from 884 until 1002 with the St Brice's day Massacre. Which followed by the two cultures more or less alternating control. And periods of hostility from 865-884, and 1002 to 1085, with maybe an ending as Dominance.

## Reply 38 — participant_029 · 2022-04-26 · post-28234968

Also will the AI in the region actively try to influence the struggle?

## Reply 39 — participant_026 · 2022-04-26 · post-28234969

Can there be a struggle between just two cultures, rather than faiths? It would be fun to use that technique to simulate the Hundred Years' War

## Reply 40 — participant_030 · 2022-04-26 · post-28234972

The Byzantine-Turkic struggle for first the Anatolian plateau (when the Turks were still mostly pastoralists) and then second for the Byzantine heartland comes to mind. It did span historically several centuries (pre Manzikert 1071 till 1453) and involved a whole region.

## Reply 41 — participant_031 · 2022-04-26 · post-28234979

<!-- artifact:quote:start -->
> Wokeg said: “Jerusalem can’t declare or be declared war on” Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Wokeg said: It's not at the moment, but it certainly could be. Personally I think the timeframe there is a little short for it, but it would depend on implementation. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Wokeg said: At the moment, it's just the Iberian Struggle. We may well see struggles in future flavour packs or expansions, but they're not a standard component for every DLC. Our first struggle is very much a result of fixed conditions (it technically starts in the history files in... I think 719?), but there's nothing stopping struggles from being set up to happen more naturalistically except for the preset region. Click to expand...
<!-- artifact:quote:end -->
I thought for a moment that was a hint to another struggle. It's 200 played years when you take into account the Norse/Danish/Norwegian kings of England even after it's been formed - and more if you count the possibility of Hardrada winning the Hasting scenario, or count the Normans as an extension of the Norse invasion. Hardrada and William would be interlopers at first (unless they're grandfathered in as hybrid/variant cultures of Norse), but once one of them wins and shifts their capital to England, they'd be potentially be involved. Might we see some of them being set up outside of DLC if they're appropriate to be struggles, but don't fit the themes of a given DLC? For example, Britain 867 - 1066; something modelling struggles like the war of the roses (very late in CK3's period, but plausible to happen anywhere, anywhen); the Hundred Years War; the Crusades even (although this is *probably* more suited to a major DLC, say one on religion...); maybe the formation of Russia?

## Reply 42 — participant_032 · 2022-04-26 · post-28234980

What is the reasoning behind making every independent ruler an Emperor if deciding for status quo? I get the reasoning behind destroying Hispania. I don't get making Kings into Emperors.

## Reply 43 — participant_033 · 2022-04-26 · post-28234987

<!-- artifact:quote:start -->
> Wokeg said: Cultures become involved either on first starting a struggle, manually via script, or automatically when a certain percentage of their total counties are within the struggle region (the number is set per struggle, currently at 80% for the Iberian Struggle). Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Wokeg said: Future Use​The Iberian Struggle is our first go at a struggle system, and it’s one we’re fairly pleased with. That said, we’ve certainly taken note of how the feature seems to have caught the popular imagination over the last week or so, and we’re very interested to hear your thoughts now that there’s a bit more information available. Needless to say, modders will be able to utilise this mechanic and share their creations from the release of 1.6 onwards. So, are there parts of the system you’d like to see refined and made more flexible? What are the struggles you’d like to see made in future? What’s your jankiest idea for hope for how to use the struggle system? As ever, I’ll be around in the thread for the next hour or so to answer your queries. Click to expand...
<!-- artifact:quote:end -->
Wouldn't that prevent empires like the Almohads from getting involved. Something for the Byzantine Empire (Struggle for Constantinople) to simulate internal politics, periods of strength, stability, decay, foreign invasions. Also something for the Karling Realms, with a clear endgoal towards establishing the Holy Roman Empire. Maybe too short, though.

## Reply 44 — participant_021 · 2022-04-26 · post-28234988

Can a character join two struggles at the same time? Also, with Status Quo, if a foreign interloper managed to reunite the peninsula,will there be a decision for him to bring Hispania back?

## Reply 45 — participant_034 · 2022-04-26 · post-28234990

<!-- artifact:quote:start -->
> Wokeg said: A core part of the identity of struggles is that they’re not things that can be solved just by painting the map - after all, if they were, then the Iberian Struggle would’ve ended in its first decade when Musa ibn Nusayr had essentially subjugated the entire peninsula. We wanted to provide more difficult and interesting goals for ending a struggle than just conquering the whole struggle region. Click to expand...
<!-- artifact:quote:end -->
I want to kiss you on the mouth. I can't believe this is a flavour pack, this looks so awesome.

## Reply 46 — participant_035 · 2022-04-26 · post-28234992

<!-- artifact:quote:start -->
> Wokeg said: Future Use​The Iberian Struggle is our first go at a struggle system, and it’s one we’re fairly pleased with. That said, we’ve certainly taken note of how the feature seems to have caught the popular imagination over the last week or so, and we’re very interested to hear your thoughts now that there’s a bit more information available. Needless to say, modders will be able to utilise this mechanic and share their creations from the release of 1.6 onwards. So, are there parts of the system you’d like to see refined and made more flexible? What are the struggles you’d like to see made in future? What’s your jankiest idea for hope for how to use the struggle system? As ever, I’ll be around in the thread for the next hour or so to answer your queries. Click to expand...
<!-- artifact:quote:end -->
Awesome DD! I can't stress this enough. Greater flexibility in how to set the struggle region will of course be great, although that's not the most limiting factor for things I have in mind. My two top most-wanted things now are definitely: - a game rule to determine who's a legit raid target, for anyone allowed to raid: we can determine who gets to raid, but not who they get to raid. - a way to call in temporary war allies, either through a scripted rule, or through an additional parameter in CBs I will use the Viking invasions of England as an example for both. Let's say the Danelaw gets reworked as a Struggle. One phase could prevent Norse rulers in the Struggle region from raiding Christian rulers. Another phase could allow for any ruler in the target region to call neighbours to their defense against Northern invasions - even if they're not proper allies. The possibilities would be awesome. I'm hoping to use Struggles in my Tribal Trouble mod as a way to rework the Feudalization process, and both of those would be the greatest things I could hope for to make it happen.

## Reply 47 — participant_036 · 2022-04-26 · post-28234997

Italy would certainly be another good place for struggles, given the political situation and the number of invasions it experienced

## Reply 48 — participant_037 · 2022-04-26 · post-28234999

Good evening,very interesting mechanic but question; Is this struggle system fully moddable and scriptable or some cannot be modded because it's hardcoded,i.e,can we create new struggle ,phases and so on through modding or not? Thanks for any replies about this.

## Reply 49 — participant_038 · 2022-04-26 · post-28235001

Are "sub-struggles" possible with the new system? E. g. would it be possible, to have the Iberian struggle being a part of an even bigger struggle with it's own conditions and can struggles overlap?

## Reply 50 — participant_039 · 2022-04-26 · post-28235005

<!-- artifact:quote:start -->
> [...] we’re very interested to hear your thoughts Click to expand...
<!-- artifact:quote:end -->
They should've sent a poet... this is amazing!

## Reply 51 — participant_024 · 2022-04-26 · post-28235006

I'd love to see something like a Carolingian struggle with a focus on dynasties/houses that could end with a renewed Carolingian Empire or the formation of France and the HRE (the game really needs a way for the AI to form the HRE) as separate entities with involved characters being Karlings, Capets and other famed houses of the era while you can also get to participate through marriages or raising your dynastic splendor.

## Reply 52 — participant_040 · 2022-04-26 · post-28235012

I would love to see Struggle about muslim conquest of India.

## Reply 53 — participant_001 · 2022-04-26 · post-28235015

<!-- artifact:quote:start -->
> anbeck said: Not sure if it's a good fit for the system, but maybe an adapted struggle system lends itself for southern France. Catharism and the Albigensian crusade were an important episode deciding the future of that region, but the integration of the Languedoc into France had a lot of interesting aspects to it (including family ties to the Kings of France and Aragon), and I'd love to see this complexity reflected in game mechanics that go beyond "me adopting Catharism, getting roflstomped by the pope". Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Spaninq said: Hold on a second, you've explained how cultures can become involved later on in a struggle, but how can another *faith* become involved in a struggle after the struggle has begun? For example, if Haesteinn decides to invade Galicia in the Iberian Struggle, what does it take for Norse to become an involved faith? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> tribnia said: Maybe a Catholic/Orthodox struggle? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Anonim97 said: Maybe a struggle for a year or two for realms under partitions after previous ruler died? And where there will be three endings "dominance" where one person gets go rule all, "status quo" where everything remains the same just like after partition and "kinship" where you get alliances made with your siblings against outside threats? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> riadach said: Do regions = empire level? I'd certainly like a struggle for the High Kingship mechanic for Ireland given that the provinces and even dynasties fighting for dominance in 867 are the same as those fighting in 1066. The ebb and flow of struggle could be altered by region specific activities such as hostage taking, making tributaries, dividing duchies amongst rivals (could be region specific for a certain phase), supporting certain churches against each other and perhaps in a later phase, the church in Rome. Other elements like placing your favoured candidates on rival thrones as well as forming grand alliances to keep other members in check could also work. Throw in feudalisation, Norse cities, and in a later stage, the English and you could have a struggle that could last 300 years. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Coplantor said: Are there mixed catalysts? Say, two characters of diferent faiths eloping together could both be seen as a positive act of overcoming differences at the same time that could be seen as a hostile action by one house head losing control over who their house members are marrying Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Crusader_SVK_287 said: Apart from the England - Normal struggle that everyone mentions, I would love to see a Norsemen - Slavic struggle. Also, a struggle in the holy land would be interesting. I hope that as time goes on, these struggles will be implemented and of course, some from the other parts of the world as India or Africa. I have no ideas for those regions tho. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Furleppe said: For the struggle examples, I think that post-4th crusade Byzantium is an easy fit for a mid/late game struggle appearing. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> PabloSugo1991 said: I crave to have the struggle mechanic pop up In France, Germany and France after a foreign culture/religion (Islam) conquers these Christian areas. It'd be much more interesting than just blobbing all the area, or at least have some special mechanics caused by such a blob! Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> TheMind said: Seems great! Keep up the good work! I agree with the guy who suggested the investiture struggle, but should be along with a rework with... well... investiture. About England, it seems a way too short timeframe to me, but I don't know. I'd like to see an Italian peninsula struggle, between all the duchies there. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> boorkie said: Looking forward to this! Is there a plan to use the struggle mechanism for more general events e.g. in case of a succession crisis? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Anonim97 said: Also other struggles I can think of: - Jerusalem is a must tbh; - India - Central Europe can be either Christians Vs Pagans or Pagans Vs other Pagans. Especially for the Prussian region. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Loderingo said: Interesting. How easy will it be for the player to influence the Struggle? It feels like it will make playing Iberia easier. At the moment if you start off as Christian, you are constantly fighting holy wars. With the struggle, it feels like the tactic is go conciliation until you can build enough military power and then go hostile and holy war. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> oreopirate said: Just to toss my five cents at this, I would argue that such a struggle would extend up to 1085, when King Knut of Denmark basically gives up his claim to England. With a period of Compromise, with the Danelaw being Conciliation and Compromise from 884 until 1002 with the St Brice's day Massacre. Which followed by the two cultures more or less alternating control. And periods of hostility from 865-884, and 1002 to 1085, with maybe an ending as Dominance. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Loderingo said: Also will the AI in the region actively try to influence the struggle? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> PabloSugo1991 said: Can there be a struggle between just two cultures, rather than faiths? It would be fun to use that technique to simulate the Hundred Years' War Click to expand...
<!-- artifact:quote:end -->
Oooh, the Cathars, not seen that one yet! Same mechanic, I'm afraid, so new smaller faiths can get in, but most larger ones practically won't be able to. ^^' That might be a mite bit too large! I think this is something we'd really like to explore at some point. Technically, a region can be as small as a one-barony county, whilst the largest literally includes the entire map. Ahhhh, that's a tasteful concept! Not in the Iberian Struggle, but there's nothing stopping that from being scripted. ^^' Funnily enough, it's something I considered early on, but we tried to focus on clear fundamentals for the first time folks'd be interacting with the system. Norse-Slavic, that's an uncommon pick! Music to my ears. Ahhh, like a more dynamic version of the core idea here? That's a cool one. Something in Italy, and something for investiture, are both excellent ideas. I do agree that I think the Norse invasions in the British Isles are a bit too short term, but it's still fun to see what folks're interested in. Not specifically, but we're keeping our options open. A Central European struggle? Neat! Depends who you're playing and the phase, but relatively easy to influence, relatively hard to completely control. Worth pointing out that these phases and ending decisions are Iberia specific - future struggles would be expected to have their own phases and ending decisions. Generally yes! Many catalysts are things they'll look to do anyway, though some are a bit more player-focused. Faith is a required component at the moment, but there's nothing stopping someone from only adding the one involved faith.

## Reply 54 — participant_026 · 2022-04-26 · post-28235019

Can we please have the possibility of Making Portugal separated from Hispania, like it was historically? A player-dominated Portugal should have the possibility of being separated from Hispania, and if the AI does so, the player, who's about to form Hispania, should have the ability to either accept this and and remain as just King of Hispania/Spain, rather than Emperor, or go to war against Portugal to claim the Imperial crown.

## Reply 55 — participant_041 · 2022-04-26 · post-28235021

Quick Ideas for other struggles: -> The abbasid empire in 867 was much less religiously unified than the game portrays it as, and there could be a struggle between many different variations of islam there. -> The muslim conquest of india could maybe also be represented as a struggle? -> The founding of the HRE could be represented as a struggle, maybe less focused on different cultures and religions, and more on the relation between the nobility and the church. Though I mostly just want the HRE being founded in 867.

## Reply 56 — participant_042 · 2022-04-26 · post-28235026

What are some cool Parameters not yet advertised in the DD you want to share with us?

## Reply 57 — participant_043 · 2022-04-26 · post-28235027

You mention Jerusalem a few times, is that a hint that the middle east is confirmed to have some sort of struggle implemented for crusader jerusalem? If so, I think that the Byzantines should be involved in some way or have some sort of struggle system with the Seljuks to reflect the constant losses/gains that both achieved after manzikert and the centuries following. HRE definitely need some sort of struggle system with the papacy to reflect the investiture conflict and the struggles with nobles in northern italy, right now HRE plays as a giant blob when it was constantly afflicted with internal conflicts for most of its history. Dev diary looks awesome, looking forward to an iberia playthrough when it comes out.

## Reply 58 — participant_044 · 2022-04-26 · post-28235028

<!-- artifact:quote:start -->
> magriboy0750 said: Is this struggle system fully moddable and scriptable or some cannot be modded because it's hardcoded,i.e,can we create new struggle ,phases and so on through modding or not? Click to expand...
<!-- artifact:quote:end -->
Fully moddable! New struggles, phases, the works!

## Reply 59 — participant_016 · 2022-04-26 · post-28235031

Is the decision to create Portugal integrated into the Iberian Struggle? Was it modified in any way?

## Reply 60 — participant_045 · 2022-04-26 · post-28235032

For future struggles: I think that when you will work on the Mongol Empire and its legacy in for example the Golden Horde, a dynamic struggle system that would apply to regions conquered by mongols would be a good starting point.

## Reply 61 — participant_046 · 2022-04-26 · post-28235038

Ethiopia seems like the perfect place for a struggle. From the 10th to 13th century, the region was in permanent struggle between Islam, Christianity and paganism. Their neighbours were also involved, including the Fatimids, which had their own issues with religious stance at the moment, and of course there's the role played by the jewish populations of the regions). One of the possible outcomes would be a new baqṭ forced on Nubians and Ethiopians by the Fatimids (who did build mosques in Nubia in the 11th century), another could be christian emancipation - total independance of Ethiopia and Nubia from muslim domination, and something to protect the patriarchate of Alexandria under Fatimid rule, and yet another could be muslim domination... Maybe there could even be a third way of the pagans manage to win the struggle. More generally, the struggle mechanic could be adapted to fit with all major conversion campaigns, especially in Mali. Maybe in Scandinavia too but I'm not knowledgeable enough about that area to know if there's enough "material" for a struggle.

## Reply 62 — participant_047 · 2022-04-26 · post-28235039

Some cool struggles could be: - the Hundred Years' War - the conflict between the HRE and the Italian states - the aftermath of Abbasid collapse in Iran has some great potential as well Also, I second the investiture controversy, post 4th crusade Aegean world, and Ireland

## Reply 63 — participant_048 · 2022-04-26 · post-28235047

Wow i'm actually very impressed. You've stopped, taken a deep breath and delivered us something serious, thoughtful, granular and complex, instead of more fart jokes and simplifications (which seemed to be the general view here at times and i sort of agreed with it). This is a really strong schema/framework for making CK3 the best damn game it can be. 10/10.

## Reply 64 — participant_001 · 2022-04-26 · post-28235048

<!-- artifact:quote:start -->
> Farbolo said: The Byzantine-Turkic struggle for first the Anatolian plateau (when the Turks were still mostly pastoralists) and then second for the Byzantine heartland comes to mind. It did span historically several centuries (pre Manzikert 1071 till 1453) and involved a whole region. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> DreadLindwyrm said: Might we see some of them being set up outside of DLC if they're appropriate to be struggles, but don't fit the themes of a given DLC? For example, Britain 867 - 1066; something modelling struggles like the war of the roses (very late in CK3's period, but plausible to happen anywhere, anywhen); the Hundred Years War; the Crusades even (although this is *probably* more suited to a major DLC, say one on religion...); maybe the formation of Russia? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> $ilent_$trider said: What is the reasoning behind making every independent ruler an Emperor if deciding for status quo? I get the reasoning behind destroying Hispania. I don't get making Kings into Emperors. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Arcvalons said: Wouldn't that prevent empires like the Almohads from getting involved. Something for the Byzantine Empire (Struggle for Constantinople) to simulate internal politics, periods of strength, stability, decay, foreign invasions. Also something for the Karling Realms, with a clear endgoal towards establishing the Holy Roman Empire. Maybe too short, though. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> tribnia said: Can a character join two struggles at the same time? Also, with Status Quo, if a foreign interloper managed to reunite the peninsula,will there be a decision for him to bring Hispania back? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> WeeLittleSpoon said: I want to kiss you on the mouth. I can't believe this is a flavour pack, this looks so awesome. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Chatoustikmou said: Awesome DD! I can't stress this enough. Greater flexibility in how to set the struggle region will of course be great, although that's not the most limiting factor for things I have in mind. My two top most-wanted things now are definitely: - a game rule to determine who's a legit raid target, for anyone allowed to raid: we can determine who gets to raid, but not who they get to raid. - a way to call in temporary war allies, either through a scripted rule, or through an additional parameter in CBs I will use the Viking invasions of England as an example for both. Let's say the Danelaw gets reworked as a Struggle. One phase could prevent Norse rulers in the Struggle region from raiding Christian rulers. Another phase could allow for any ruler in the target region to call neighbours to their defense against Northern invasions - even if they're not proper allies. The possibilities would be awesome. I'm hoping to use Struggles in my Tribal Trouble mod as a way to rework the Feudalization process, and both of those would be the greatest things I could hope for to make it happen. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> DarkPeppix said: Italy would certainly be another good place for struggles, given the political situation and the number of invasions it experienced Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> magriboy0750 said: Good evening,very interesting mechanic but question; Is this struggle system fully moddable and scriptable or some cannot be modded because it's hardcoded,i.e,can we create new struggle ,phases and so on through modding or not? Thanks for any replies about this. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> The_F said: Are "sub-struggles" possible with the new system? E. g. would it be possible, to have the Iberian struggle being a part of an even bigger struggle with it's own conditions and can struggles overlap? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Vivs said: They should've sent a poet... this is amazing! Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Coplantor said: I'd love to see something like a Carolingian struggle with a focus on dynasties/houses that could end with a renewed Carolingian Empire or the formation of France and the HRE (the game really needs a way for the AI to form the HRE) as separate entities with involved characters being Karlings, Capets and other famed houses of the era while you can also get to participate through marriages or raising your dynastic splendor. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Ksiendzu said: I would love to see Struggle about muslim conquest of India. Click to expand...
<!-- artifact:quote:end -->
[subtle-unsubtle scribbling] I'd certainly like to personally, but per the usual, no promises, I'm afraid. As an Englishman I am obliged to both thumbs up any mention of the Hundred Years War and point out that the Wars of the Roses are, sadly, technically outside of our time period - they started in 1455 and our last year is 1453. Certainly some interesting choices, though! To be clear: kingdoms become empire titles, every independent ruler doesn't become an emperor. Though they would then have an easier time creating those titles. Nope - a good deal of Arabic and Berber cultures that were ruling class members for al-Andalus are pre-emptively involved. The Almohads themselves would simply remain interlopers (which they, at least at first, sorta were) till they convert enough counties within Iberia. You hypothetically could but we'd generally recommend against that as a default - it'd be very easy to end up in situations where you've got +X% of Y modifier from one struggle and -Z% of Y modifier from another. We hope to address some of this in the future with some clever modifier shenaniganery. I take cash or card or alcohol. More seriously, though, glad you're hyped! Many, many people have touched the design and implementation of this system, it's been through a lot of revisions, and especially our UX designers have worked absolute miracles taking a really high concept design and making it into something not only parseable but actively intuitive. Interesting. Thanks for the notes! Yeah, intriguing how many people seem after that... There are some elements that can't be decided on the fly (region being the biggest at the moment). New struggles, struggle phases, struggle catalysts, and struggle parameters are all scriptable. I suppose you technically could but I'd strongly advise against it. Overlapping struggles invite weird behaviour where modifiers and parameters conflict. ^^' Glad you like it. Ooph, what an excellent idea! That could certainly be fun.

## Reply 65 — participant_049 · 2022-04-26 · post-28235057

I wonder if the conflict between pagans and christian in the Nordics could be adopted to this, which makes it a bit of a shame you already did our DLC!

## Reply 66 — participant_050 · 2022-04-26 · post-28235058

I'm going to be honest, I find the struggle mechanic WAY more interesting than the Royal Court expansion. This is amazing! While RC is a lot more flashy and seems to ''deepen'' the game, the struggles lay the foundations for very interesting organic stories in the game. Assassinating someone, promoting a marriage, educating a child in this or that culture... these are all options that could lead to completely different development in the struggle of a region. And yes, for now this is limited to Iberia, but everyone is already mentioning the British isles and even the Holy Land is name dropped in the post! That is so exciting! Also, reading about the Status Quo ending, I find that very interesting. All the petty kings becoming ACTUAL kings, new empires being created, even for the AI, changes to the De jure land... That would result in a curious map, with less wars being warred because X character owns Z county, and meanwhile, integrating land and De jure drift would be more important. I only hope that this doesn't lead to a bit of a stagnation when it comes to conflict. I'll keep following these diaries, I want to see what else they have in store for the DLC. As a final note, I hope they don't forget about events. One of my biggest disappointments when I first played the game was reclaiming Toledo and getting... nothing. Not even a message. Please, add at least something recognising how important it was for the christian iberians. Also, I'd love some kind of event regarding the bells of Santiago if a muslim (or non christian Iberian) captures it. Also also, some flavour for the Camino de Santiago too. I mean, come ooooon...

## Reply 67 — participant_051 · 2022-04-26 · post-28235059

A generic struggle system for kingdom titles taken by foreigners as the newcomers have to deal with any local vassals and their previous vassals try and take advantage of the new opportunities. It could be used to model things like Norman castle-building and importing foreign nobility.

## Reply 68 — participant_052 · 2022-04-26 · post-28235068

<!-- artifact:quote:start -->
> Wokeg said: Catalysts themselves can be anything. A war being declared, a type of character being seduced, Click to expand...
<!-- artifact:quote:end -->
So, you're saying you're also working on a Trojan Cycle spin-off game, or just you want the community to make a Trojan Cycle mod?

## Reply 69 — participant_053 · 2022-04-26 · post-28235070

Even though it takes place in the back end of the game where most people do not play to, the Hundred Years War would be an excellent struggle that would not only make the conclusion of the game very exciting, but also provide reason for a late game bookmark. Furthermore, you could combine this with a 1066 Norman struggle to make an English-French themed succession flavor pack. The Deli Sultans of India would also do well, with the Ghazni and Tughlug. The advent of Islam to India and the emergence of an Indo-Islamic civilization would work really well alongside Royal Court mechanics and combined with a struggle. Trying to find to find accommodation and balance between the different faiths and cultures is just ripe for opportunity, with Dhimmi status, Iconoclasm, and state policy to conversion, the role of intermarriage, and egalitarianism. There were times of indian-muslim accommodation alongside periods of stringent dogmatic Islamic adherence and demands. While there is no official word on there being an East Asia (China to Japan) DLC, this new mechanic combined with the Royal Court is helping develop the mechanical stage to allow for really dynamic and interesting potential gameplay within the Middle Kingdom, where a tech monolith is able to provide very interesting gameplay that is not all about conquering neighbors (unless the Mandate is lost and China fractures )

## Reply 70 — participant_024 · 2022-04-26 · post-28235082

From a purely narrative/RP reason it would be neat to include in the change of phase a reference to the final act that triggered. It could lead to very interesting AARs with things like the marriage that unified Hispania or the execution that lead to a century of uninterrupted violence

## Reply 71 — participant_052 · 2022-04-26 · post-28235090

So, obviously we're looking deeply forward to the Iberian Struggle and also hope to eventually see other scripted Struggles modelling other big historical events, I am wondering if it would be possible and if it would even make sense to script a kind of "generic dynamic Struggle" that could trigger in any region if the right criteria were met, just to make sure that any place could potentially be the site of a Struggle in any playthrough? Obviously something like that could never be as interesting as a Struggle written specifically for a particular occurence, but it would allow anyone to witness/participate in a Struggle in their homeland under the right circumstances even without living in the specific places with scripted Struggles.

## Reply 72 — participant_054 · 2022-04-26 · post-28235091

hope we will have a struggle for the kigdom of jerusalem after creation by a successfull crusade

## Reply 73 — participant_055 · 2022-04-26 · post-28235098

Have you considered adding decisions to form León and Castilla for the 867 starting date like the ones for Aragón and Portugal?

## Reply 74 — participant_056 · 2022-04-26 · post-28235102

<!-- artifact:quote:start -->
> Wokeg said: They are assumed to last at least a couple of centuries: a conqueror carving out a new realm from the ruins of an old giant wouldn’t be a struggle by itself, but if it includes dramatic aftershocks that last for generations, then it just might be. Click to expand...
<!-- artifact:quote:end -->
It's fairly typical for Iberian Muslim rulers to expand into France. How will that work with regards to the struggle? Does it suddenly stop at the Pyrenees mountains? It's basically an extension of the Iberian struggle, this time between French catholic rulers instead of Iberian ones. Good vision on paper, however it's currently so easy to expand in CK3 that after a few centuries the player (even starting from a count position) will already have carved an intercontinental empire and the struggle will be long forgotten.

## Reply 75 — participant_057 · 2022-04-26 · post-28235106

I would go for an East-African Struggle. Espescially the Empire of Abyssinia (and maybe including Egypt). Why? You have a relatively instable realm with Coptics, Muslims, Jews and 2 Pagan Faiths and various Cultures intermingling with each other. The only thing that would be necessary is for the Duchy of Makuria and the Sultanate of Egypt to have some vassals. They have to land them so or so.

## Reply 76 — participant_032 · 2022-04-26 · post-28235107

<!-- artifact:quote:start -->
> Wokeg said: To be clear: kingdoms become empire titles, every independent ruler doesn't become an emperor. Though they would then have an easier time creating those titles. Click to expand...
<!-- artifact:quote:end -->
Oh, okay, slightly different then, but still, sorry, my question wasn't answered. What is the reasoning behind that? To make it Kingdom now an Empire-tier and thus preventing de jure wars to accelerate the conquest of the region? That's the only thing I can think of and might actually be the motivation.

## Reply 77 — participant_058 · 2022-04-26 · post-28235109

As someone who likes playing further towards the east of the map, something about the rise of the Islamic sultanates in the Indian subcontinent would be cool for a future struggle!

## Reply 78 — participant_059 · 2022-04-26 · post-28235111

Carolingian Struggle is the best idea I've heard so far. Something to focus the AI and player on the conflict over Charlemagnes empire, with potential for outcomes depending on who comes out on top would be awesome.

## Reply 79 — participant_060 · 2022-04-26 · post-28235114

Would it be possible to have a 'sub-national' stuggle within sufficiently large empires? say for an example the Holy Roman statelets, having a struggle that would nudge the game toward a cycle of consolidation and fragmentation of rule, jousting for control of the throne? But really, you could probably make an argument that any large empire (that aren't at high enough authority) should have a low-boil struggle among it's vassals

## Reply 80 — participant_061 · 2022-04-26 · post-28235115

This looks better than what i could ever imagine or come up with myself! I love that we can take the historical route or other ones. I'm so excited for future Iberia play, i think I'll do a lot of different playthroughs in the area (or from outside, TO Iberia!) It's an obvious interest of mine and I feel super lucky to be in the first region affected by this mechanic, but also share the enthusiasm shown by everyone for it to flourish and be applied to different conflicts throughout the game map. Congrats Paradox, you really outdid yourselves with this one!

## Reply 81 — participant_062 · 2022-04-26 · post-28235120

This is more interesting than I expected. I'm looking forward to the system being deployed elsewhere, e.g. the Hundred Years War. I could also see this used to represent the Rome/Constantinople conflict, culminating in either reconciliation or the Great Schism (although from the comment above the system would need modification to support multiple struggles impacting characters at once).

## Reply 82 — participant_063 · 2022-04-26 · post-28235121

<!-- artifact:quote:start -->
> Farbolo said: The Byzantine-Turkic struggle for first the Anatolian plateau (when the Turks were still mostly pastoralists) and then second for the Byzantine heartland comes to mind. It did span historically several centuries (pre Manzikert 1071 till 1453) and involved a whole region. Click to expand...
<!-- artifact:quote:end -->
Interesting idea. This struggle was a catalyst for the First Crusade, so it would have some interesting involvement of characters. Also, in the final stages the BYZ Emperor negotiated for Western military assistance in exchange for, among others things, converting to Catholicism.

## Reply 83 — participant_064 · 2022-04-26 · post-28235136

I think the struggle system should be a dynamic thing that happens when two religions contest a region. Examples include the Crusades in the Middle East obviously The northern crusader conflicts between the Baltic pagans and Christian holy orders Anatolia after manzikert between Byzantines and Turkic beys And the Muslim invasions of India all of these cases would work much better with the struggle system laid out than the normal holy war system honestly I’m more in favor of getting rid of the holy war Cb altogether and making religious struggles more like what’s been presented here as the struggle system

## Reply 84 — participant_031 · 2022-04-26 · post-28235138

<!-- artifact:quote:start -->
> Wokeg said: As an Englishman I am obliged to both thumbs up any mention of the Hundred Years War and point out that the Wars of the Roses are, sadly, technically outside of our time period - they started in 1455 and our last year is 1453. Certainly some interesting choices, though! Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Keslier said: Even though it takes place in the back end of the game where most people do not play to, the Hundred Years War would be an excellent struggle that would not only make the conclusion of the game very exciting, but also provide reason for a late game bookmark. Furthermore, you could combine this with a 1066 Norman struggle to make an English-French themed succession flavor pack. Click to expand...
<!-- artifact:quote:end -->
Although the wars of the roses are technically outside the period, they're the sort of conflict that might work well as a model if you have a "generalised" struggle becomes possible (say if there's a kingdom/empire claimant war between two houses of the same dynasty and some conditions are met then you target as a region the involved titles?). It's the sort of thing I could certainly appreciate in various places, under various names. It's also the sort of conflict that could arise at any point, not just as a late game scenario.

## Reply 85 — participant_065 · 2022-04-26 · post-28235141

Thank you for the amazing DD!! Really looking forward to play FOI! I would very much like see a Struggle involving Rus, Ruthenia and in in general all Russian Grand Principalities (and it would be really great to actually have them named "(Velikoe) Knyazhestvo" as you do with other regional title names), the states of Cumans and Pechenegs in the 1066 start, and Khazaria and the Norse states in the 867 start, and also Baltic (Lithuania, Teutonic Order) and Western states, and the Mongols. I think there are a lot of interesting possibilities and opportunities there, because it's a really interesting region, with many cultures and faiths involved (for example, the interfaith marriage mechanic could reflect the actual historical marriages between children of Russian and Cuman rulers), a lot of tension, intrigue, alliances and wars between Russian Knyazyas themselves and other rulers, and, in general, this region would be a great idea for a Flavor Pack!

## Reply 86 — participant_066 · 2022-04-26 · post-28235166

Some ideas: - Ibn Khaldun struggle, involving the islamic faith in maghreb, misr, mashrek and Persia. Phases would be "carve out an empire and blob among muslims" then "more and more vassals become independent" until either you recreate the Caliphate (unification) or the muslim world remains divided and the caliph title disapears. - Steppe nomadic struggle: a peaceful phase where the people of the steppe have many trade-related events with the outsiders, which can transition to either directly a steppe-focused wartime phase (destroying old empires and making new ones, changing power balance) or a shorter migration phase where varangian-like CBs could be launched by small tribes (and be easy to succeed) before shifting to a wartime phase to integrate post-migration divided counties into bigger realms. The conclusion could be allowing mega blobbing (the Mongol Empire) or a pacification of the steppe, making it easier to feudalize. - Imperial division or unity in China if it ever gets added - Some that other people already described (Latin States, 4th crusade, Baltic Crusades, Cathar Crusade...) and of course a Karling/setting the HRE struggle

## Reply 87 — participant_067 · 2022-04-26 · post-28235186

West slavic state forming struggle? This struggle mechanic could be fitted for the nation forming and unification of relatively recently settled and formed semitribal western slavic states and their resistance towards frankish/HRE meddling. I say "unification" but it was more of a securing of trade around Moravia (meant the region, not state) and back then west slavs practically still spoke the same language (even liguists think that difference between Polish and Czech was definite only in 12th century) during 9th century it was the Great Moravia during 10th century it was Bohemia during 10-11th century split it was Poland under Boleslaw the Brave and it ended in failure (or status quo you could say) Bohemia+Moravia+Meissen+Lusatia became part of HRE but Bohemia eventually stabilised and kept Moravia Nitra(Slovakia) became part of Hungary but never played an important role compared to the rest ever since Poland was independent but dynastically fractured and, with breaks, constantly arguing with Bohemia over Silesia from late 11th century onward you only had 3 kingdoms which interacted with each other more or less dynastically or over border skirmishes (like the mentioned Silesia) ... edit: to note I didn't mention Pommerania because it was "in a way" kept out almost separate issue more closely related to the Baltics

## Reply 88 — participant_068 · 2022-04-26 · post-28235191

<!-- artifact:quote:start -->
> Creating Hispania is locked behind resolving the struggle (to keep things a bit more interesting), but resolving the struggle does not automatically create Hispania. Click to expand...
<!-- artifact:quote:end -->
God, this looks dope. Really excited for this pack to eat several weeks of my life. This prompted a thought: when it's time to expand this mechanic into other areas of the map, what about locking every de jure Empire behind a Struggle? It would make empires feel really special, an achievement of generations that can't be accomplished just by map-painting and conquest. Start dates could have an in-progress Struggle for the already existing empires, and then for all the others, if nothing else has yet happened to trigger a regional Struggle it could automatically kick off as soon as a ruler meets the other requirements for Empire creation. I don't know if a 1:1 Struggle : Empire relationship is exactly right; you have some historical conflicts that feel right for a Struggle but are either conflicts between regions mapped as different de jure empires (any French-English conflict, for example) or involve smaller territorial regions within the same de jure Empire but not comprising all of it (lots of stuff that happened within the de jure HRE). But I think it might be a good starting point, and then you could evaluate region by region whether multiple Empires could be locked behind the same Struggle, multiple Struggles could be a gateway to the same Empire, and which Struggles could pit two or more de jure Empires against each other. Hell, maybe even have kind of a default Struggle template that the player touches off when they meet the requirements for creating a custom Empire. "Imperial Ambitions" or something; checks the region's the most powerful vassals, most troublesome counties, and most dangerous neighbors and uses the cultures and religions involved to generate an appropriate set of Phases and Catalysts.

## Reply 89 — participant_069 · 2022-04-26 · post-28235196

A successful Crusade/Jihad could begin a struggle in the region where it happened.

## Reply 90 — participant_070 · 2022-04-26 · post-28235203

Verry hyped for the mechanics and so far everything looks great! Still sorta distressed Vimara Peres is nowhere to be seen

## Reply 91 — participant_071 · 2022-04-26 · post-28235208

Does the struggle kick off when you start the game, or does it have conditions required to begin it?

## Reply 92 — participant_072 · 2022-04-26 · post-28235213

Hot take: give every empire its own internal struggle. With Expansion, Competition, Prosperity, Decline phases.

## Reply 93 — participant_073 · 2022-04-26 · post-28235239

<!-- artifact:quote:start -->
> Agamidae said: Hot take: give every empire its own internal struggle. With Expansion, Competition, Prosperity, Decline phases. Click to expand...
<!-- artifact:quote:end -->
As long as Decline isn't forced upon the player "Just because"...

## Reply 94 — participant_074 · 2022-04-26 · post-28235243

The struggle concept could be interesting for creating special title like the Outremer Empire / Roman Empire or during the Mongol Invasion. It could even create or modify an existing religion (remove or add a Syncretism tenet).

## Reply 95 — participant_075 · 2022-04-26 · post-28235252

As someone who lives in the Catalonia area I am curious to know several things: 1- The Catalan counties belong to Aquitaine in 867, how will this be reflected in the fighting system? 2- Will there be events/decisions for the Catalan counties to become independent and join the kingdom of Aragon? 3- Will the AI be able to evolve the kingdoms of 867 to how they are in 1066? examples: Asturias can become the kingdom of León? Can the crown of Aragon be created? Can the Taifa kingdoms appear? thanks for any answer

## Reply 96 — participant_076 · 2022-04-26 · post-28235253

First would like to say I'm super excited about struggles! Not something the community was expecting, but you all really delivered on coming up with a new system we would love. My big question is whether the AI will be more aggressive towards the player in a struggle? In the base game I've had war declared on me like 5 times out of hundreds of hours of play and would be looking forward to some real challenge with the struggle. I have a couple ideas that I don't think have been touched on below. Mongolia 1179: This is a great point in time for a struggle in Mongolia. Many interesting participants you could start as. Ong Khan of the Kereyid tribe has just declared war against the Merkid on behalf of his vassal Temujin (future Genghis Khan) and his other vassal Jamukha (Temujin's blood brother and eventual biggest rival). All this to rescue Temujin's wife Borte (could be a new CB "abduction). The other two main tribal leaders are Tayang Khan ruling the Naiman in the West and Altan Khan in the east as vassals of the Jurched of Northern China. Struggle would be great for this as you could go for unification with multi-culture and multi-religion like Genghis Khan, a unification with one of the cultures or religions dominating, status quo to keep the tribes warring like China wants so they're too busy to attack them. Interesting religions in the area that might conflict like Tengrism, Nestorian Christianity, Islam, and Buddhism. Aristocrats versus individuality could be a big part of the struggle historically as Genghis was against the traditional aristocracy. Italian Republic: I don't know how historical this is, but I love the major decision in Sicily to form a Parliament of the three estates. I would love to have a struggle that involves Italy forming a parliament, restoring the senate, parliamentary monarchy, resisting republicanism, restoring the old religions. We've got tons of different Latin heritages, North African Muslims, Orthodox Greeks, the Byzantines next door, HRE above, and the pope involved in it all just makes it way more interesting. The Karlings 867: Not much to say about this. It's already one of the most interesting starts in the game with the chaos of several kingdoms with claims on each other that goes different every play through. To have the struggle system placed on top would be great. Struggles could end in separate kingdoms, reforming Charlemagne's empire, or constant struggle.

## Reply 97 — participant_077 · 2022-04-26 · post-28235283

I would love a struggle between the Shia and Sunni sects in the Muslim regions. They are just so . . . barren compared to the rest of Europe even though they are a huge part of history.

## Reply 98 — participant_078 · 2022-04-26 · post-28235295

Will Christian and Muslim feudals be able to raid (razia, or ghazah) each other during the Hostility phase? This is something that I've always wanted to see in the games and this seems like the perfect opportunity to do it. Minor raiding was a big part of the Reconquista that sadly never actually happens in CK2 or CK3. *Edited because I originally wrote "non-feudals", which actually don't exist in the Peninsula during the time period.

## Reply 99 — participant_079 · 2022-04-26 · post-28235319

As a Spanish player, and after the well-known disasters affecting our community, it is only fair to recognise that this DLC looks amazing. Congratulations. However, let me beg you to be ESPECIALLY careful with the bad or missing translation this time. I'm looking forward to this.

## Reply 100 — participant_080 · 2022-04-26 · post-28235354

I'm curious about how the struggle responds to interlopers conquering the entire region (say the Almohads, France, or a player reforming the Roman Empire). Can the interloper enforce one of the endings or can only an involved character? Do interlopers get any benefit for ending the struggle? Or does the struggle keep going on, just now inside the interlopers realm? Alternatively will the struggle respond to interlopers conquering of the region, maybe ending the struggle prematurely if a certain amount is taken by the interlopers so the local can focus on responding to the interlopers? Edit: re-reading the dev diary, my example would I guess be uninvolved characters as their capitals are outside the region (though they might have interloper or involved vassals). So are any of the answers to these questions different if the realm conquering Iberia is uninvolved in the struggle?

## Reply 101 — participant_081 · 2022-04-26 · post-28235372

<!-- artifact:quote:start -->
> Wokeg said: Catalysts​Transitioning from a phase to any of its future phases requires the activation of catalysts: notable events, gameplay actions, and consequences to existing mechanics that drive the current phase towards a specific future phase. Catalysts themselves can be anything. A war being declared, a type of character being seduced, a certain type of scheme failing, and so on. They’re set inside a phase’s future phase block, and, as with other elements of struggles, are entirely scriptable. Virtually any effect block in the entire title can be made into a catalyst with a bit of thought. Whenever a catalyst is activated, meaning that the thing that sets them happens, the current phase gains points towards the future phase that that catalyst was tied to (for instance, a notable interfaith marriage might help an uncertainty-focused phase gain points towards a tolerance-focused phase). Catalysts themselves are repeatable and the points they give vary with the difficulty of the catalyst in question - two notable characters becoming soulmates might well be worth more points than a notable character being executed, for instance. Points for put into simple tallies: when one tally for a future phase is met, that future phase becomes the new current phase, though there’s a grace period of a month before the actual switch. On the off chance that all of the dozens or hundreds of characters involved in a struggle are being incomprehensibly boring, we should note the existence of one special catalyst: the passage of time. Every phase has a default future phase, and receives a single point per year towards that phase’s tally, representing the natural trend of public discourse towards particular conclusions. This can (and essentially always will) be overridden or exacerbated by more dramatic catalysts being activated, but even in very calm struggle, change is always coming. Click to expand...
<!-- artifact:quote:end -->
Most of this looks great, but I have some concerns about the above. This is worryingly similar to Fervor - a system in which a quantity increases and decreases according to character actions. So far, this type of system has not worked well. Fervor doesn't feel like it increases and decreases in a natural manner, and I'm concerned that catalysts will feel the same. It's especially concerning that catalysts include things like seduction - the current AI seduction is a complete disaster. Characters seduce one another for seemingly no reason (other than poorly coded event logic). Is building Struggles on such a shaky foundation a good idea? If Struggle progress is balanced around the current broken AI behavior, will that become an obstacle to making the AI behave more reasonably, since now any such changes will break the balance of Struggles? It just feels like if I were going to build something that depends on how the AI seduces, schemes, etc., I would want to make sure those ducks were in a row before I started depending on them.

## Reply 102 — participant_082 · 2022-04-26 · post-28235387

could a struggle commence upon the creation of any custom empire? i.e. 'hang on! you can't do that!'

## Reply 103 — participant_083 · 2022-04-26 · post-28235407

I really like the Struggle system! It feels like it could do a lot to give different areas an overarching regional flavor while not having too much railroading. Especially if there's a way to make the start of Struggles a bit more dynamic, so a Struggle could trigger in a region under certain conditions (like, since Jerusalem was mentioned in the diary, being started by the Crusades happening). One area I think the Struggle system could be useful in future is in Italy either for the Guelphs and Ghibelines or in late game the rise of the Italian city states. The latter would be especially interesting if/when republics become playable and you have a Struggle over whether Italy should be dominated by feudal, republic, or theocratic governments.

## Reply 104 — participant_084 · 2022-04-26 · post-28235410

As a Spaniard myself, I can only say three letters: W O W.

## Reply 105 — participant_083 · 2022-04-26 · post-28235418

I also wonder if the system might be useful for the spread of Islam in West Africa. I'm not as familiar with that particular area of history, but it could be a good way to give the region some more flavor content.

## Reply 106 — participant_085 · 2022-04-26 · post-28235421

What an awesome DD! The mechanic is very promising, can't wait to see it used in other regions. Some ideas: Struggle for North Sea/Danelaw. It might not last very long, but given the open-ended nature of CK history, I can see some potential in aggressive raiding, settling, conquest, defensive efforts and a struggle between Asatru vs. Christianity. Struggle for Italy/Rome, which included the Investiture Controversy with the HRE and which saw the Pope deciding it in his favor. But what if it ended the other way around? Or what if it lasted longer, if the Emperor had more support from his vassals? Also, as someone mentioned, the Carolingian Struggle to restore the glory of their old empire. Of course, it would be at the expense of the HRE and France, so both would make good involved parties. Then there's the Struggle between the ERE and the Abbasids/Fatimids/Seljuks (and then Turks). And we know that once the Crusaders got involved, Saladin (Egypt) became also a major player. Things were messy, ideal for a Struggle full of backstabbing. Another Struggle could be within the ERE itself, as it wasn't very stable. Times of unrest, times of internal stability, times of civil war... everything's possible here. And if someone manages to bring everything together, maybe they can prevent the ERE from certain death? And what about the Mongols? Their later conquests under Dschingis Khan are too big for the mechanic, but the time before that? Parts of Mongolia are on the map, but the region isn't that interesting at the moment. Having a Struggle to unite the warring tribes, securing support or destroying opposition, or accepting the fragmented status quo... and then the ultimate prize: becoming Khan and leading the tribes west. I'd take that!

## Reply 107 — participant_086 · 2022-04-26 · post-28235423

Is there a way for an uninvolved power to overcome a Struggle through intervention? Say, if the Iberian struggle is unresolved but the resurgent Roman Empire rolls in and holds the peninsula for decades, would they eventually be able to overcome the local pressures or would the struggle remain active indefinitely, draining any outside invader? This is a general concern that only increases as more regions get their appropriate Struggles. Yes, map painting is not the playstyle that is being supported here and that's good, but it also creates a railroading situation where some cultures and faiths are easier to displace than others based on the Struggles involving them.

## Reply 108 — participant_087 · 2022-04-26 · post-28235430

This seems amazing. Truly unique and refreshing. If this is well implement.... oooowwwwmahGod... gonna be sweet. Should we start making a list of the most popular struggle locations we are all proposing? So many good ideas too, it's hard to choose I wanna add my voice to those that have proposed Italy as a great location for potential struggle(ssss). We don't just have a very similar situation to that of Iberia between Christians and Muslism to the south (and let's not forget the Byzantines wanting back), but we also have the investiture controversy, Carolingians fighting Lombards, rampaging Normans making a name for the Hautevilles, the crucible of cultures that Sicily becomes -giving way to personalities as interesting as Frederick II Hohenstaufen-, the Aragonese conquest later on... there is just so much flavour in it you can practically see it oozing out.

## Reply 109 — participant_088 · 2022-04-26 · post-28235436

If the "Struggle system" is as good in-game as it appears on paper, if it's implemented into the game in an intelligent way, and it is quickly added to regions of the world beyond being confined to the Iberian peninsula (not that Spain isn't important, but this is too good to not be a universal tool) this will be what CK3 needed to elevate it from "really good" to "genre-defining" There is potential in this system to check off so many boxes that players have requested over the years. I've seen people with requests as large as "I want a fundamental change to CK3 that makes painting the map not mean game over" to requests as small as my recent plea to make dueling have more purpose The Struggle can do these things, and more. With a system like this, and a little creativity, you really do have a catch-all system in place. This isn't the magic fix, but it's certainly one of them - if utilized correctly. Good job, the whole concept looks great.

## Reply 110 — participant_048 · 2022-04-26 · post-28235439

As other people have mentioned the Karlings, something loosely fitting into the struggle schema would be great for that arena literally just to set the stage/clear the board for the actual medieval age to begin and the late dark ages end. Unless you turn matri-marriage off the Karlings always just hang around most games and keep you in this semi dark age state forever. Would be great to have a system that makes it more definitive they either rise back to glory with a second Carolingian renaissance, all die out/purged horribly, or I don't know successfully merge into new dynasties. Certain parts of said struggle could have matri-marriage off and make Karlings really picky about marriage options, Anything to rid me of these buggers.

## Reply 111 — participant_089 · 2022-04-26 · post-28235455

Sicily would be perfect for a Struggle region except it might be too small. If culture can be used exclusively instead of religion+culture then Italy in the HRE could be a struggle region too. I'd put forward India as a struggle region not just between Dharmic religions and Islam, but as a concluded struggle region between the Dharmic faiths. Maybe they went the conciliatory ending. Armenia/the caucuses in general can be a three-way struggle between the ERE, the Seljuks, and the native Armenians desperately trying to maintain independence.

## Reply 112 — participant_066 · 2022-04-26 · post-28235467

On the topic of overlapping modifiers in case of large area struggles, @Wokeg , may I suggest to simply add little to no modifiers to large scale struggles (which would focus on other features for each phase)? Modifiers could be confined to the smaller struggles only.

## Reply 113 — participant_059 · 2022-04-26 · post-28235477

<!-- artifact:quote:start -->
> Caeserion said: Sicily would be perfect for a Struggle region except it might be too small. If culture can be used exclusively instead of religion+culture then Italy in the HRE could be a struggle region too. I'd put forward India as a struggle region not just between Dharmic religions and Islam, but as a concluded struggle region between the Dharmic faiths. Maybe they went the conciliatory ending. Armenia/the caucuses in general can be a three-way struggle between the ERE, the Seljuks, and the native Armenians desperately trying to maintain independence. Click to expand...
<!-- artifact:quote:end -->
Yeah, Sicily, and even Southern Italy, is just too small for a struggle region IMO. With India Buddhism would also probably be heavily involved, as it's in this time that Buddhism falls put of favor in India in favor of Hinduism and Islam. Not sure how much that involved warfare though.

## Reply 114 — participant_090 · 2022-04-26 · post-28235504

<!-- artifact:quote:start -->
> Wokeg said: Interesting choice! It's not at the moment, but it certainly could be. Personally I think the timeframe there is a little short for it, but it would depend on implementation. There's elements of that in the Iberian Struggle, but it doesn't, strictly speaking, have to be. I've seen this one crop up a lot in various public forums! Strictly speaking, no. At the moment there are no other regions where the struggle system will be implemented - Iberia is our first struggle. I've got a handful of personal favourites that I know I'd like to try and which those unfortunate enough to be within rambling distance of me are very well aware of, but I don't think I'm allowed to share those. Click to expand...
<!-- artifact:quote:end -->
Have you considered a religious struggle as a type? Like Conversion of Rus to Islamic, Orthodox or Catholic faith made into a competition between those 3?

## Reply 115 — participant_091 · 2022-04-26 · post-28235508

Beautiful. That's going to be really fun to play. Will inject much needed dynamism and roleplaying.

## Reply 116 — participant_092 · 2022-04-26 · post-28235526

Everything for this next flavor pack sounds good so far, and I am looking forward to what is possible when people begin modding with this system. One of the possible modable uses I am curious about for this system would be creating special "kingdoms"/"empires". Could it be possible to create impromptu "kingdoms" or "empires" where the involved characters act like "vassals" to another character who holds a specific title (assuming the system is changed to allow the struggle region to include specific de jure kingdom/empire titles, and be dynamic)? For example, a struggle system could be setup after the 1066 wars for England, like William wins and gets the Kingdom of England. Then, his vassals are released and added as involved characters. From reading the dev diary, the possible effects on characters both during the struggle and after it ends seems to vary a lot and has a lot of potential, and seems like it could simulate vassalage, like how it is mentioned that during the detente ending, the Iberian characters could defend any other Iberian character from outside attackers could simulate a liege protecting his vassal's land. Maybe it is possible to do some complex checks on the involved characters so that characters that don't own the specified title (Kingdom of England in this case) could lose gold, or have lowered levies, while the character that has the title would gain those, to simulate the taxes. If these sort of options are possible, it could create some unique, dynamic realms that may have special mechanics compared to others.

## Reply 117 — participant_093 · 2022-04-26 · post-28235536

Iberia has a lot of replayability potential, and this system seems to further exarcebate this. I'm looking forward to this flavor pack! P.S: Please buff de jure Portugal

## Reply 118 — participant_094 · 2022-04-26 · post-28235548

Could the empire of Hispania have an alternate name if it is held by an Arabic speaking character, i.e. Al-Andalus

## Reply 119 — participant_095 · 2022-04-26 · post-28235599

<!-- artifact:quote:start -->
> Tiax said: Most of this looks great, but I have some concerns about the above. This is worryingly similar to Fervor - a system in which a quantity increases and decreases according to character actions. So far, this type of system has not worked well. Fervor doesn't feel like it increases and decreases in a natural manner, and I'm concerned that catalysts will feel the same. It's especially concerning that catalysts include things like seduction - the current AI seduction is a complete disaster. Characters seduce one another for seemingly no reason (other than poorly coded event logic). Is building Struggles on such a shaky foundation a good idea? If Struggle progress is balanced around the current broken AI behavior, will that become an obstacle to making the AI behave more reasonably, since now any such changes will break the balance of Struggles? It just feels like if I were going to build something that depends on how the AI seduces, schemes, etc., I would want to make sure those ducks were in a row before I started depending on them. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Illusive_Mike said: Is there a way for an uninvolved power to overcome a Struggle through intervention? Say, if the Iberian struggle is unresolved but the resurgent Roman Empire rolls in and holds the peninsula for decades, would they eventually be able to overcome the local pressures or would the struggle remain active indefinitely, draining any outside invader? This is a general concern that only increases as more regions get their appropriate Struggles. Yes, map painting is not the playstyle that is being supported here and that's good, but it also creates a railroading situation where some cultures and faiths are easier to displace than others based on the Struggles involving them. Click to expand...
<!-- artifact:quote:end -->
The progress towards a phase is never reduced. It's more of a race between the two potential future phases. We also adjusted the AI intent for characters within the Iberian Struggle to pursue catalysts. When a character joins the Struggle, they receive an agenda and will act accordingly. This agenda is hidden however, but might be deduced by observing how they behave. We have indeed a fourth way of ending the Struggle, but only for non-Involved characters

## Reply 120 — participant_096 · 2022-04-26 · post-28235612

<!-- artifact:quote:start -->
> Wokeg said: What are the struggles you’d like to see made in future? Click to expand...
<!-- artifact:quote:end -->
Byzantines vs Seljuqs in the struggle for Anatolia!

## Reply 121 — participant_097 · 2022-04-26 · post-28235617

You'd think that the Status Quo ending would make more sense if, instead of turning every single local kingdom into a de jure empire, you'd split the former de jure empire of Hispania between the neighbouring de jure empires of Francia and Maghreb, since the concept of a unified peninsula is no more and the border between the Muslim and Christian half is solidified. In any case, looking at the suggestions here we can already guess what the expansion after this is gonna be called: "Oops! All Struggles."

## Reply 122 — participant_098 · 2022-04-26 · post-28235622

<!-- artifact:quote:start -->
> Wokeg said: Technically, a region can be as small as a one-barony county, whilst the largest literally includes the entire map. Click to expand...
<!-- artifact:quote:end -->
Haha that stretches my imagination. For a world level struggle the Mongols could really become one in the late game. Maybe the region involved in the struggle is simply any the Mongols are next to If they conquer most of the map then maybe the whole world will be in the Mongol struggle! As for a barony struggle level struggle. Maybe Socotra is struggling not to be invaded lol. Struggles I'd like to see: Struggle for India between incoming Muslims and the native Indian religions. I can picture special tolerance and intolerance phases, expansions, claims to the Delhi Sultanate, trade relations and conversions etc. Struggle in China, probably better off if china is ever added but the Jade Dragon mechanics have some similarities to the phases of the struggle and areas like Tibet, the Steppe, and the Guiyi Circuit especially could all be involved in the current situation in China. Broken, Unified, Expanding, etc Struggle for Indochina, probably would also be better with a map expansion but similar to Muslim adventurers entering India there's a long history of Hindu adventurer kings entering Indochina and making special adjustments to their faith and building great cities! Struggle for the Steppe. Living in the Steppe is a struggle within itself. Unifying under a great Khan is an obvious end state. The steppe could have huge resistances to uninvolved parties interloping, they'd also have Migration periods and special CBs. New cultures could perpetually be moving in from the east to west leading to periods of great pressure for those involved in the struggle for the steppe to attack outsiders, or unite in confederacy. Struggle for East Africa. A very slow burning struggle shifting between long periods of peace or conquest between the Muslim rulers of Egypt, their christian subjects, and the christian lands to the south. News of Crusades could quickly shift this struggle from a long period of detent to a period of holy war and conquest. Struggle for Anatolia, others have said it better than me but there really needs to be a long dynamic unfolding situation of the Turks entering Anatolia Struggle for Jerusalem, the Crusades really could use some systems that actually makes them more historical. Right now after installing a kingdom of jerusalem they're pretty left to be devoured by all their angry neighbours. Plus the Crusades might be genuinely more fun with some narrative adventures and events. Struggle for Ireland. Internally it's really hard to forma. proper high kingdom of Ireland, rather instead it's more common to go through many cycles of disunified high kingships passing along. It could also give Ireland a bit more defensiveness to outsiders invading, slowing down it's conquest by England. Maybe even an outsider can be declared the King of Ireland only for them to struggle to actually unify and control the land. The Struggle for the HRE is a must in the 867 start date to have some kind of system to actually make anything mildly historical happen there. Refounding a big old HRE should be one of the possible outcomes with others splintering or remaining seperated in the carolingian de jures. A separate but similar , religious conflict system would be really really good for this game I think. You could have the Sunni/Shia conflict with ways for Shia's to pop up more often. The Great Schism between Catholic and Orthodox with rulers on the border getting options who to deal with. 'conflict' between the Indian religions allowing them to flow more into each other, etc.

## Reply 123 — participant_099 · 2022-04-26 · post-28235627

<!-- artifact:quote:start -->
> Wokeg said: Status Quo balkanises Iberia, transferring duchies to connected kingdoms if appropriate and making every kingdom within Iberia its own de jure empire whilst permanently destroying Hispania. Ruling houses across the former struggle region gain a modifier for two centuries making them better at fighting in lands of their own cultural heritage, whilst the capital counties of all independent rulers become strongholds for the next century. Some CBs within Iberia become more expensive. Click to expand...
<!-- artifact:quote:end -->
What is the Pourpose to make unhistoric little empires of the small kingdoms in Iberia which pop up en masse by succession on the muslim and Christian Kingdoms. The only way to get a recognised empire in the middle ages is either get it handed by the Pope, the ecumenical Patriarch (as a Christian) or by conquering everything, not by a conciliatory mechanic, regardless how difficult to achieve. It makes little historical sense to have a 2 Province empire of Navara, kingdom of Coimbra and etc. Imagine the following being done as succession after Status Quo: All Hail Kaiser Ludwig of Navarra in his capital Aargau - emperor of Navarra, king of Barcelona, one county holder (in todays Switzerland) and brother to the Holy Roman emperor.

## Reply 124 — participant_045 · 2022-04-26 · post-28235649

Could you tell us what the next Diary will be about like? Victoria 3 allways does that and i guess that you have every DD planned out allready for this DLC

## Reply 125 — participant_100 · 2022-04-26 · post-28235684

I'd definitely love a Papal/Imperial conflict, ("investiture controversy" feels a bit too limiting, I think?) Guelf-Ghibelline struggle? It's something that is at least on the back burner for most of the period.

## Reply 126 — participant_101 · 2022-04-26 · post-28235701

<!-- artifact:quote:start -->
> Wokeg said: Something in Italy, and something for investiture, are both excellent ideas. Click to expand...
<!-- artifact:quote:end -->
In my humble opinion, this should be one and the same struggle involving the Guelphs and the Ghibellines. Have you considered giving government type a role in struggles? I think it could be used to model the rise of Italian city states or the struggle between holy orders and tribes in the Baltics. Republics and theocracies will of course not be playable but could be interesting mid-game adversaries of players. If you ever decide to add a nomadic government type, I think there could be an interesting struggle on the steppes between different nomadic tribes, between nomads who want to settle and nomads who want to keep to the old ways, and with their feudal and tribal neighbors. Writing that all out, I realize that might become too confusing. I would really like to see the Struggle system used in a way that captures the dynamism of steppe culture, but I... uh... struggle to visualize the exact possibilities.

## Reply 127 — participant_102 · 2022-04-27 · post-28235740

Let's go for a 2-counties Corsica struggle. We've been struggling since the beginning of time to this day.

## Reply 128 — participant_103 · 2022-04-27 · post-28235754

Firstly - this sounds great, really looking forward to this flavour pack. Secondly - this genuinely sounds like it was built for Anglo-French conflict. People have already mentioned the Hundred Years war in this thread, but everything about Anglo/English - French relations post William the conqueror is perfectly described as a struggle. Just look at the angevin kings, who controlled more of France than the French throne.

## Reply 129 — participant_081 · 2022-04-27 · post-28235779

<!-- artifact:quote:start -->
> Pdx_Meedoc said: The progress towards a phase is never reduced. It's more of a race between the two potential future phases. We also adjusted the AI intent for characters within the Iberian Struggle to pursue catalysts. When a character joins the Struggle, they receive an agenda and will act accordingly. This agenda is hidden however, but might be deduced by observing how they behave. Click to expand...
<!-- artifact:quote:end -->
On the one hand, that sounds very promising. On the other hand, I shudder to imagine the adultery rate in courts where characters have an agenda that pushes them even further towards seduction.

## Reply 130 — participant_032 · 2022-04-27 · post-28235787

<!-- artifact:quote:start -->
> Antimonum said: What is the Pourpose to make unhistoric little empires of the small kingdoms in Iberia which pop up en masse by succession on the muslim and Christian Kingdoms. The only way to get a recognised empire in the middle ages is either get it handed by the Pope, the ecumenical Patriarch (as a Christian) or by conquering everything, not by a conciliatory mechanic, regardless how difficult to achieve. It makes little historical sense to have a 2 Province empire of Navara, kingdom of Coimbra and etc. Imagine the following being done as succession after Status Quo: All Hail Kaiser Ludwig of Navarra in his capital Aargau - emperor of Navarra, king of Barcelona, one county holder (in todays Switzerland) and brother to the Holy Roman emperor. Click to expand...
<!-- artifact:quote:end -->
I am trying to understand the reasoning here. I think it might have to do with avoiding Empire de jure CBs once it gets balkanized. I get destroying the Empire of Hispania title. I don't get making these kingdoms into empires.

## Reply 131 — participant_032 · 2022-04-27 · post-28235790

<!-- artifact:quote:start -->
> Juncoril said: Let's go for a 2-counties Corsica struggle. We've been struggling since the beginning of time to this day. Click to expand...
<!-- artifact:quote:end -->
It has to do with your cheese.

## Reply 132 — participant_104 · 2022-04-27 · post-28235794

Seeing all that talk about culture conversion, does the AI actually pick that councillor option? I have a feeling that they never ever do that currently and provinces only switch cultures via events.

## Reply 133 — participant_081 · 2022-04-27 · post-28235796

<!-- artifact:quote:start -->
> $ilent_$trider said: I am trying to understand the reasoning here. I think it might have to do with avoiding Empire de jure CBs once it gets balkanized. I get destroying the Empire of Hispania title. I don't get making these kingdoms into empires. Click to expand...
<!-- artifact:quote:end -->
Maybe it's just an engine limitation. There has to be an empire, so the only way to destroy Hispania is to replace it with other empires.

## Reply 134 — participant_032 · 2022-04-27 · post-28235805

Ah, yeah, now that you mention it, yeah... That totally makes sense. In that case, I just hope status quo also gives a prestige/renown penalty to the Empire titles in Hispania so they are, mechanically speaking, an Empire, but don't get the perks of being one,

## Reply 135 — participant_105 · 2022-04-27 · post-28235839

A perfect example of a Struggle would be after the establishment of the crusader states, 1099-1187 from their foundation to their fall, we don't have a crusader states start date yet but there should also be a dynamic one formed immediately after the establishment of a crusader kingdom, with the (forced) establishment of a new religious kingdom in foreign lands there will naturally be a struggle that follows, with stages of tension, temporary peace and a lot of hostility.

## Reply 136 — participant_106 · 2022-04-27 · post-28235843

This looks fantastic. Easily worth spending money on future flavor packs if this is the kind of quality we'll be getting out of them. The place that comes to mind for first for this system are easily the British Isles. Lots of cultures and religions there that interact.

## Reply 137 — participant_107 · 2022-04-27 · post-28235853

This system looks like it might have great potential. I highly approve the general design direction of creating agnostic systems that could be applied to a variety of different regions and different topics. Hopefully you can eventually fill the map with a huge variety of pre-set and dynamic struggles. Can struggles overlap? For example a north italian struggle against german imperial dominance and an overlapping investiture struggle amongst all catholic rulers across western europe/western schism. Can the struggle regions change dynamically? For example if I were to create dynamic struggle that forms to the boundaries of a collapsed empire. Say the empire gets destroyed via the struggles starting event releasing all subjects and the struggle is reforming the empire. (Maybe smth like this could be a post 4th crusade byzantine struggle?) Could I have a decision that lets a now independent kingdom remove itself from the struggle, such that that kingdom is no longer involved without ending the struggle? I would love to see a struggle that would focus on christianization and settling of central europe. Especially with the german Ostsiedelung and the northern crusades. The region being the Baltics, West Slavic region and Pannonia, possibly the southern Rus Kingdoms. Christians Local christian rulers could invite german settlers, granting tax and levy benefits, help towards feudalization, founding new city holdings over time that could turn the counties culture german or invite them to help christianize pagan lands This in turn could spawn hybrid eastern german cultures, such as (new) prussian, (german) pommeranian, upper saxon etc. german characters actively culture converting in the area would rather spawn a hybrid than their own culture spread of Magdeburg rights in new established cities in the east mechanics to organize coordinate holy wars, invite holy orders to conquer, possibly leading to Teutonic State to form ending when the whole region is christianized Pagan for Pagans it could be ways of uniting against christianity or intermarrying into christian families and giving minor concession to keep christians at bay or playing off catholics and orthodox against each other in their attempts of conversion like the Lithuanians did for a while. ending if a feudal pagan realm can dominate the region.

## Reply 138 — participant_108 · 2022-04-27 · post-28235861

<!-- artifact:quote:start -->
> Cultures become involved either on first starting a struggle, manually via script, or automatically when a certain percentage of their total counties are within the struggle region (the number is set per struggle, currently at 80% for the Iberian Struggle). Click to expand...
<!-- artifact:quote:end -->
Would it be possible to make this triggered not just by percentage of the overall culture, but also by percentage of the culture within the region? If say, something really strange happens, and we end up with a strong Norse presence on the Iberian peninsula, then we might end up with a scenario where Norse culture is widespread and the Iberian peninsula does not hit the 80% majority, yet still, within the peninsula, Norse culture is one of the most dominant cultures present. It seems to me it would make sense to make them relevant to the struggle A similar mechanic could work for religions

## Reply 139 — participant_109 · 2022-04-27 · post-28235900

Guelphs and Ghibellines / Swabian Sicily vs Papacy

## Reply 140 — participant_110 · 2022-04-27 · post-28235937

Hmmm. I'll probably need somewhere in the ballpark of 5 to 10 mods to be happy with this system, but I'm a fan of "just conquer it" problem solving and grinding conquered regions under my heel, heh heh

## Reply 141 — participant_111 · 2022-04-27 · post-28235964

<!-- artifact:quote:start -->
> Wokeg said: What are the struggles you’d like to see made in future? Click to expand...
<!-- artifact:quote:end -->
*cough* Hussites and the road to Reformation? *cough*

## Reply 142 — participant_112 · 2022-04-27 · post-28235971

Oh the possibilites of this new system!

## Reply 143 — participant_113 · 2022-04-27 · post-28235974

I really don't want pre-defined struggles in the game to be the focus. I think if this system is to be implemented it should be able to arise through natural gameplay in different areas. I have no idea how that would be even remotely achievable but I would personally not enjoy the system if it was exclusive to specific areas and time periods.

## Reply 144 — participant_114 · 2022-04-27 · post-28235994

The investiture controversy between the pope and the emperor with the guelphs and Ghibellines on either side seem like a natural place for the struggle mechanic to be used

## Reply 145 — participant_115 · 2022-04-27 · post-28235997

Seems like a great system that could be implemented in some way to represent events with Byzantium vs The Arabs/Turks.

## Reply 146 — participant_116 · 2022-04-27 · post-28236051

Sounds a very interesting system. Could work really well in East Africa, specifically the long struggle between the Christian Nubians and the Muslim Egyptians that started before the game and continued on until just after the end of the game. The relationship waxed and waned depending on who was ruling over Egypt - generally decent under the Fatamids but deteriorated under later ones. The Christian Nubians also championed the cause of the Copts in Egypt (who in game disappear very fast), so that could be caught up in the struggle as well.

## Reply 147 — participant_117 · 2022-04-27 · post-28236056

I don't know if this has been mentioned yet, but I personally wish for Tripartite Struggle, where three Indian Empires fight over Kanauj (and dominance over India as a whole).

## Reply 148 — participant_118 · 2022-04-27 · post-28236059

Rus/Finno-Ugric struggle Germans/West Slavs + Balts struggle Norse/English struggle Byzantine/Turkic struggle Maybe something in Persia and India with steppe folk

## Reply 149 — participant_030 · 2022-04-27 · post-28236089

The longer I think about it, the more I suspect myself finally coming back to play CK3 on a regular with this "Flavour Pack". As others have said, the struggle-mechanism has me way more excited than Royal Court ever did. People had both complained that the specific regions lacked distinction and that the world's events more often than not lacked 'relatedness', for lack of a better word, meaning that the events seemed not to be interwoven into the bigger context of a great, over-arching narrative/conflict. Seems to me that you attempt to address both these issues, to which I applaud. Just asking myself, how many struggles will already be implemented mod-wise until you come around with your next 'official' struggle Hopefully the mutual compatability of these differing struggles can be ensured by the modding-community... Oh, and thanks btw for both the lengthy and detailed character of this DD and your very open communication afterwards. I suppose this is something we direly missed here sometimes in the past months.

## Reply 150 — participant_119 · 2022-04-27 · post-28236106

<!-- artifact:quote:start -->
> Wokeg said: What are the struggles you’d like to see made in future? Click to expand...
<!-- artifact:quote:end -->
Bulgarians, Seljuks/Rûm and Byzantium!

## Reply 151 — participant_120 · 2022-04-27 · post-28236142

Another excellent idea for a Struggle is between the Byzantines and Bulgarians which historically lasted from the 5th century all the way to the 14th century when Bulgaria was annexed by the Ottomans. During this massive period, there were many times of brutal wars but also cultural exchanges, with the Bulgarians Christianizing and creating a Slavic alphabet and having their own patriarch. Some cool mechanics could be made based on these historical events. Also, there should be some triggers for a Bulgarian independence uprising after the 1066 start date because we never see Bulgaria again, while historically, they made an uprising and created the Second Bulgarian Empire. Another cool idea is some Struggle system for Kievan Rus because it's a large mix of Norse and Slavic cultures and pagan and Christian religions, also mixed with arriving steppe Tengri tribes and bordering the Islamic Volga Bolgars. The end of the struggle could be the creation of the Rus culture. Will there be some new Royal Court 3D or artifacts? Or just new headgears?

## Reply 152 — participant_121 · 2022-04-27 · post-28236236

Modder here, was initially planning on starting work on an Anarchy at Samarra/Zanj Rebellion/Qarmatian uprising event chain with Royal Court, but this seems like the dream DLC for it. One question though, will we be able to add progress to phases via something like custom court events? Considering how much of the Anarchy at Samarra was based around court politics, it'd definitely be nice to have them hold a lot of weight. Keen as a bean for this though.

## Reply 153 — participant_122 · 2022-04-27 · post-28236248

@Wokeg This all looks amazing; what an excellent read, I truly can't wait to see this in action. I know I'm late to the party but I'd like to throw my hat in the ring and advocate for dynamic struggles borne out of disruption to the status quo. e.g - northmen pushing into central europe - heresy in a region has become more widespread than expected (>20% cathar in french region) - could be tied into the above point but when reforming an unreformed religion there should be a struggle between those stuck in the old way vs the new. This could divide the empire into two (or more) conflicting empires. the reason i feel there should be dynamic struggles alongside the scripted ones is that whilst it won't have much/any beautiful scripted flavour it would make playing in regions that don't have a lot of interesting things happening (such as Persia/Indian region) feel unique in each playthrough depending on how you roleplay it. perhaps you have brought zoroastrianism back from its downward trajectory, a dynamic struggle between islamic and zoroastrians would ensue. anyway I can't wait to see what you guys and gals come up with; much love from australia.

## Reply 154 — participant_123 · 2022-04-27 · post-28236253

I woud love to see a Struggle mechanic in a flavor pack for Poland and it's "Rozbicie dzielnicowe" (basically a fragmentation of the country) that lasted from 1138 to 1320 which would include the rise of the Teutonic Order and the long lasting fights for the reunification of the country.

## Reply 155 — participant_124 · 2022-04-27 · post-28236302

Maybe we will see this in the next devdiaries, but I'm disappointed we still see no way to manage minorities yet. Converting a county is a handy gamey concept, but what does it mean? That you conviced everyone? That you convinced the elites? That you brought in new settlers from your religion and outnumbered (or out-importance-d) the previous majority? Same goes for cultural conversion (moreso even). The way it's set, cultural and religious conversion are tedious button clicking activities with almost no interaction with it. No RPG elements in our RPG game are involved here. 1. Settlers Royal Court introduced the decision "petition settlers to liege" or some such title, where you ask your liege to grant you settlers for extra development. This is a good idea, and it could be further used to spice up cultural and religious conversion. I the Middle Ages, lords of frontier lands would usually create towns and grant them "charters of freedom" or "charta populationis" the freedom form serfdom would attract peasants. But it has tradeoffs. Less taxes for future development, increased prosperity and cultural and religious conversion? Sounds like an interesting choice. Furthermore, your inland neighbors don't appreciate that a great deal of these new settlers are escaped serfs from their lands. And usually charter towns were created by the King or equivalent, with the marcher lords themselves opposed to them existing in their vicinity (for the same reasons, a drain in their serfs and in their trade revenue). 2. Policy You could set, through your councillors, a policy of "forced resettlement" (Byzantine style), of incentive (like the charters above) or a policy of conciliation (do not attempt to change culture or religion, wichever you choose, but I can't think of the benefits. No loss in development but increased bad events where people enter into conflict with one another? Conciliation really was not the common approach anyone ever had. Cultural, maybe, when a culture that was less developed came into contact with one that was, like Arabs and Persians after the conquest of Mesopotamia, or Alexander in Babylon trusting Bagoas and his Persian advisors...) Precisely, Alexander gives us an example of the kinds of conflicts that might arise from conciliation. Your old guard feels you are soft or misguided, they resent your acceptance of the new culture and they despise the new advisors, the satraps... meanwhile the new culture is very suspicious of the old. You need to choose one, or create a melting pot quickly and set up your heirs to be as tolerant as you, or the empire will break. 3. Cult Will you accept other religion's existing in your empire? Will you convert their temples, or allow their continued existence? Will you impose taxes on the believers, or allow them free practice? Will you save yourself the trouble and befriend the heads of faith (something that is pretty much impossible with the current way CK3 handles religion, with religious leaders often being picked out of thin air with no previous existence or history, so you can't anticipate their rise) or promote their division with the funding of heresies through a fun learning and diplo minigame where you debate the heads of faith until, years or decades later, new heresies pop up and the reigious unity of your new subjects is broken. Now you can get to work and appear to be the conciliating lord you want others to see yourself as. These are simply some ideas I'd like to see in my game. More RPG and interaction between systems is always good.

## Reply 156 — participant_015 · 2022-04-27 · post-28236348

Will there be some event or CB reflecting the Siege of Lisbon (1147)? Diverting some of the crusaders into Iberia for their own greed could be differentiated from full Crusade and become part of the Opportunity or Hostility phase IMO. Also, I think this is different from 'encouraging uninvolved characters to delegate Iberian lands to vassals with a better level of involvement'

## Reply 157 — participant_125 · 2022-04-27 · post-28236354

Will there be a "parias" system for iberian struggle? Making muslim or christians tributaries of your realm intead of conquering them.

## Reply 158 — participant_126 · 2022-04-27 · post-28236419

I would love to see the following two struggles. - The Christianization of Scandinavia (Maybe give the Norse bonuses to reformation if they manages to resist?) - The (culutural) Germanization of slavic lands (Maybe in combination with Baltic Crusades)

## Reply 159 — participant_127 · 2022-04-27 · post-28236497

Time to Tizona

## Reply 160 — participant_128 · 2022-04-27 · post-28236538

I am really loving this system. It sounds extremely fun to play with, but I especially can't wait to see what modders can do with it.

## Reply 161 — participant_129 · 2022-04-27 · post-28236571

<!-- artifact:quote:start -->
> Wokeg said: It's not at the moment, but it certainly could be. Personally I think the timeframe there is a little short for it, but it would depend on implementation. Click to expand...
<!-- artifact:quote:end -->
How about a longer term struggle for England/Britain that starts with the Norsemen and ends with the Normans?

## Reply 162 — participant_130 · 2022-04-27 · post-28236589

Struggle seems to me the most innovative thing PDS has done for a very long time: kudos! On the supposition that it's positioned as a standard mechanic, it offers many new content opportunities for both PDS and modders. For example: "small" Struggles could be included within free updates or "easy" mods, while "large" ones could be released as content DLCs at whim. This seems a logical progression. Why? Because, while most Struggles will be of interest only to particular segments; it's balanced in development cost terms by not having to worry about testing new mechanics; only having to balance the newly drafted content. For example, I'd primarily be interested in Iberia, Britons v Danes, Angevins v Capetians, Normans v Saxons (if the latter is feasible length-wise - not letting ourselves be distracted by William I's choice of a quick and ruthless "Domination"-type path!). But I certainly could be tempted toward say a partly-internal ERE feudalism v imperial "centralize/decentralize system of government" Struggle (eg the creation of the theme system being a significant episode); while not so interested in say a Crusaders v Marches/Baltic Pagans one - despite the latter starting with Charlemagne and continuing through almost the entire period.

## Reply 163 — participant_131 · 2022-04-27 · post-28236593

I would like to see the struggle between Muslims and Pagans in West Africa over control of gold, salt, and slaves.

## Reply 164 — participant_031 · 2022-04-27 · post-28236614

<!-- artifact:quote:start -->
> Kapitalisti said: How about a longer term struggle for England/Britain that starts with the Norsemen and ends with the Normans? Click to expand...
<!-- artifact:quote:end -->
Harald Hardrada *is* often considered the last Viking claimant to England, although the post-Hastings attacks by Sweyn (1070) and the planned attack by Cnut IV of Denmark (1085/6) may also count here.

## Reply 165 — participant_132 · 2022-04-27 · post-28236623

<!-- artifact:quote:start -->
> PabloSugo1991 said: Portugal separated from Hispania, like it was historically? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> PabloSugo1991 said: just King of Hispania/Spain Click to expand...
<!-- artifact:quote:end -->
No it wasn't? The Kingdom of Hispania was the Visigothic kingdom, which encompassed all of the peninsula. The Kingdom of Hispania is not the Kingdom of Spain. The Kingdom of Hispania predates the game's timeframe, and the Kingdom of Spain lays outside of the timeframe. The Empire of Hispania is an alt-history imperial formable.

## Reply 166 — participant_133 · 2022-04-27 · post-28236748

Can you finally remove the muwalladi thing please now that you can simulate the Andalusian behaviour without the need to split the Sunni Muslims please please please

## Reply 167 — participant_134 · 2022-04-27 · post-28236763

Great DD. I can't wait to play around the struggle feature.

## Reply 168 — participant_031 · 2022-04-27 · post-28236764

<!-- artifact:quote:start -->
> Mo_Fleet said: Can you finally remove the muwalladi thing please now that you can simulate the Andalusian behaviour without the need to split the Sunni Muslims please please please Click to expand...
<!-- artifact:quote:end -->
We're more likely to see *more* variant faiths sharing heads of faith rather than less to be honest. Now we can get more regional variants and hopefully have them all play nicely with each other.

## Reply 169 — participant_048 · 2022-04-27 · post-28236795

<!-- artifact:quote:start -->
> DreadLindwyrm said: We're more likely to see *more* variant faiths sharing heads of faith rather than less to be honest. Now we can get more regional variants and hopefully have them all play nicely with each other. Click to expand...
<!-- artifact:quote:end -->
Have they given any info anywhere yet how that will work (shared heads of faith) or just stated it will be a thing?

## Reply 170 — participant_031 · 2022-04-27 · post-28236812

<!-- artifact:quote:start -->
> The Shacks said: Have they given any info anywhere yet how that will work (shared heads of faith) or just stated it will be a thing? Click to expand...
<!-- artifact:quote:end -->
It's mentioned as a thing in one of the press releases - and we haven't been corrected on it when it was brought up. But I don't think we've seen anything beyond "it's happening" yet. Hopefully @Wokeg is planning for it to be a dev diary, or part of one? Possibly alongside what Mozarabic will have as doctrines and tenets.

## Reply 171 — participant_135 · 2022-04-27 · post-28236820

On paper, very well thought out mechanic that seems to be a brilliant add-on to the game and solely more than worth the price of admission for the flavour pack. Fortunately the game seems to deviate further and further from mindlessly painting the map, fully contextualizing wars and this is a solid step in the right direction. Together with this new design I would turn simple map painting impossible, softly forcing huge polities to brake under their own weight after some decades or a generation of full power using other more subtle mechanics than partition. As far as future struggles, I believe the map could be all split into many different regions, each one with its own kind of struggle. Think about mission trees for each country in EU4 and establish a parallel with regions here. Hopefully, Paradox will continue developing new struggles over each free patch and paid add-on as the area to cover is huge. Modding capabilities are also a big plus too. All in all, it seems the designers are to be heartily congratulated for the mechanic their minds conjured!

## Reply 172 — participant_103 · 2022-04-27 · post-28236831

<!-- artifact:quote:start -->
> Kapitalisti said: How about a longer term struggle for England/Britain that starts with the Norsemen and ends with the Normans? Click to expand...
<!-- artifact:quote:end -->
If the struggle mechanic is limited so that it can only do before or after William the Conqueror instead of including the invasion and extending beyond it, then it makes more sense to do after. You have the English kings from William through to Henry III fighting with the French throne over their continental possessions. In particular the Angevin kings like Richard the Lionheart owned more of France than the French king at the time. Following this you have Edward I and his campaign of subjugating Wales and Scotland, sowing the seeds for political discourse between England and Scotland for the next 500 years. Then Finally you've got Edward III beginning the Hundred Years War with France, arguably the definitive conflict of the medieval period, which takes us all the way up to 1453. In reality though the British Isles are probably one of few regions on the map that would be appropriate to have a struggle which runs from 867 all the way to 1453.

## Reply 173 — participant_136 · 2022-04-27 · post-28236853

<!-- artifact:quote:start -->
> Dracupuncture said: @Wokeg This all looks amazing; what an excellent read, I truly can't wait to see this in action. I know I'm late to the party but I'd like to throw my hat in the ring and advocate for dynamic struggles borne out of disruption to the status quo. e.g - northmen pushing into central europe - heresy in a region has become more widespread than expected (>20% cathar in french region) - could be tied into the above point but when reforming an unreformed religion there should be a struggle between those stuck in the old way vs the new. This could divide the empire into two (or more) conflicting empires. the reason i feel there should be dynamic struggles alongside the scripted ones is that whilst it won't have much/any beautiful scripted flavour it would make playing in regions that don't have a lot of interesting things happening (such as Persia/Indian region) feel unique in each playthrough depending on how you roleplay it. perhaps you have brought zoroastrianism back from its downward trajectory, a dynamic struggle between islamic and zoroastrians would ensue. anyway I can't wait to see what you guys and gals come up with; much love from australia. Click to expand...
<!-- artifact:quote:end -->
I like the idea of smaller scale dynamic struggles that can be triggered by events and player actions alongside the larger, scripted, and more detailed regional struggles.

## Reply 174 — participant_130 · 2022-04-27 · post-28236854

<!-- artifact:quote:start -->
> Wokeg said: A simpler example would be a hypothetical Anglo-Norman struggle for after the Conquest. We’d probably want to set Norman up as an involved culture, and wouldn’t want them to immediately become uninvolved because there are no Norman counties in the British Isles. Click to expand...
<!-- artifact:quote:end -->
A quick heads-up on something you probably already know (or not!) as evidence of the massive ethnic cleansing following the Conquest. Take a look at the original document that (utterly wrongly!!!) has been described by moderns as Magna Carta. This is the 1215 Runnymede peace treaty, i.e. one and a half centuries post-Conquest. There are many named individuals in it (IIRC well over 30): either as signatories or objects of complaint, or otherwise material for mention. There are names from many parts of Europe. These predominantly appear to be French names, but not just Normans (or, at least, obviously holding their primary power bases in parts other than Normandy). There are also names (French or otherwise) whose power bases obviously are in Scotland, Ireland, and Italy. But there is not a single English forename. Not a trace of an Aethelred, an Edgar, an Aelfred, or anything else starting with anything traceable to an Anglo-Saxon name! Further, the document naturally focuses on grievances and about (allegedly) restoring (or sometimes creating!) specific feudal rights: narrowly scoping most of these to the rights of "free men" in the realm (which often meant much more than just England). Only rarely does it mention "men" by itself. English men are (conspicuous;y!) not mentioned. Again contrary to modern popular belief, to believe "free men" includes English men is a category mistake. Because the English were serfs and thus by definition unfree, being legally bound to land belonging to the local (non-English) free men. The only exceptions to that being those that (literally) escaped peonage and made it as far as sanctuary in either the Church (low ranks only) or the very few royal chartered towns (such as London). "Free men" thus essentially is shorthand for Normans, foreigners, and clerks / churchmen (most of whom were Normans or foreigners anyway). My source of the original text is the appendix to Dan Jones' book "In the Reign of King John: A Year in the Life of Plantagenet England" (available in hardback or e-book), which focuses on the background to 1215: a political / economic / cultural analysis of England in that "snapshot" year. It's also the book that brought home to me how the gradual expansion of the "forests", meaning the Crown land / Royal demesnes carved out by royal decree at whim since the Conquest (thus not just by John!), had systemically wrecked the English economy (circa half of the land whether arable or not being owned directly by the monarch and turned over to bailiffs aka "foresters" to manage either inefficiently, corruptly, or not at all) to the point that revolution became objectively necessary. [EU4 Crown Land enthusiasts take note! ] [Whence Magna Carta, then? In the third "issue" (1217), the second to be promulgated not by John but by his son's regent William Marshal, the already edited document was split in two. About 40% of it was removed, expanded and placed into a separate primarily economic document titled the Charter of the Forest. The balance was miscellaneous but remained larger in length, so for convenience of reference / differentiation became known simply as the Great(er) Charter! Oddly, three Articles (1, 9, and 29) of the 37 articles in the 1297 promulgation remain good law in England (the other 34 Articles having been purged periodically over the last two centuries): these can be read in modern translation here. They're substantially different to the original, but you can sense the flavor! Note the original 1297 text (appended to the translation) is Latin, whereas iirc its 1215 peace-treaty ancestor was written in Norman French - my point being that neither law was accessible even to those few serfs (meaning the English) able to read. ] Separately: it could be argued that any cultural Struggle based on the Conquest could easily extend until such "decision" points as when the Norman overlords finally took up English as a language to use among themselves; and as a language of statute; etc. In combination, such constraints might imply resolution only at the end of the Angevin period: after the loss of all the monarch's and nobility's mainland Angevin possessions (French becoming superfluous). I give you the Wars of the Roses. Any errors in the above are, of course, my errors only. HTH

## Reply 175 — participant_137 · 2022-04-27 · post-28236858

Some specific struggle concepts: Gaelic Ireland and the English/Normans/other invader (possibly and probably the Norse given how Ireland is the first start date) - with alternating phases of Submission and Rebellion, and possibly of hybrid cultures switching sides due to Gaelicisation. The Wars of the Guelphs and Ghibellines - people have already mentioned the Investiture Controversy, but the conflicts and divisions between the two factions continued for centuries after the Papacy and the Emperor had resolved the issue. It would be interesting to explore a struggle that began as one between the Emperor and the Papacy, then into one between two dynasties, until it was effectively between two prototypes of modern political parties. Instead of cultures being involved, families and realms are assigned sides depending on whether a ruler or dynasty head has a Guelph or Ghubelline trait, which is passed down to children unless they are reeducated by someone from the other side. A causal decision made at the beginning of the struggle will have consequences for many generations until it either ends with one sides final victory or burns out with no clear winner. The Mandate of Heaven - well, you haven't announced China yet, but if/when you do, "the phases" of the Struggle system could be used to represent the board cycles of Chinese dynastic history, Stability, Stagnation, Corruption, Rebellion, Chaos - Stability is when all is well, Stagnation is when a certain inertia sets in, Corruption is when a Dynasty becomes perceived as having become tyrannical and Rebellion is when a great civil war becomes inevitable. Chaos is a sort of temporary fail state, where no Emperor exists, but everyone has a cheap CB on everyone else. With the main difference being that the "ending decisions" merely reset the clock. Have you overthrown the old Dynasty and built a new one? Congratulations, you have returned to the Stability phase, or possibly even the Stagnation or Corruption phase, depending on the nature and morality of the new dynasty. Has the Empire collapsed in warring states? Welcome back to the Chaos phase. The Northern Crusades - probably an obvious choice, but the complexity of the Northern Crusades really isn't represented by the current Crusade system, in particular how the Teutonic Knights were fighting pretty much entirely Christian enemies by the end of it. It would also be nice, given how the Teutonic Knights are themselves unplayable and will very, very rarely become an independent state like they were in the game as it stands - to make a Struggle that encourages the HRE (AI or player) to hand over territories it would otherwise be blobbing into to the Teutonic Order States, which could have various interesting interactions with playable characters. The Frankokratia/Latinokratia - the conflict between the Eastern Roman Greeks and the Italian and Frankish Crusader States set up after the Fourth Crusade. A bit too late game, and bit specific a scenario perhaps, but it certainly scans as a candidate. Some concepts for dynamic struggles, that can occur anywhere on the map under certain conditions and would potentially spice up mid to late game content after a player has built a strong realm: Independence War - instead of being a simple faction rebellion amongst many, under some conditions an Independence War could trigger a generic Independence struggle that continues even after the original revolt is crushed. Church and State - the increasing conflict between church and state is a recurring theme of medieval history, especially of the late Middle Ages. Under certain circumstances a realms secular rulers might find themselves in a protracted struggle against the influence of the Church. Dynastic Struggle - claimants come and claimants go, once you've mastered the game you can usually either defeat or break up rival claimant factions easily enough - but what if this time, the division in your society goes beyond one war and one claimant? What if the everyone in the realm is offered the chance to take sides, and like in the Guelphs and Ghibellines idea above, this decision becomes an inheritable trait. Your realm gets split 50-50 between vassals and dynasties that have chosen x or y character; they hate each other now, almost as much as they'd hate people with a different culture or religion. In some phases of the struggle they won't even marry, in others they can try to make peace again. It doesn't even have to be about a claimant as such, the struggle could pick one of the vassals in your realm who is a "Powerful Vassal" and decide their dynasty is now your dynasties rivals, and will be until the Struggle ends. Crown and Estates - a conflict between the King and their Court and their more independent minded vassals, ending in either absolutism, parliamentary government or some manner of compromise.

## Reply 176 — participant_138 · 2022-04-27 · post-28236863

The system itself seems to be quite complicated for me in theory, so I'm waiting to see what it looks like in practice. And as for the events to which I would see him, there is the issue of fights for the heritage of Carolingians on the starting date 872. It is quite rare to see that new monarchies of Germany and France arise in Western Europe, and the descendants of Charlemagne do not rebuild the power of their great ancestor or create a place For the new nations, therefore, such a system, which in its own way forces them to choose a certain path for history, seems to be a good solution for the Franks. Such an event could be focused on all the countries under the control of the Carolingian dynasty, making the Carolingian subjects, in the absence of their expansion, have an ever worse relationship with their suzerain, and the most powerful vassals would enjoy the special Casus Belli, or if a worthy successor to Charlemagne were found, this one would receive bonuses to accelerate its expansion and to recreate the Frankish Empire as a single domain linking the empires of France, Italy and Germany. I sincerely apologize in case of linguistic mistakes

## Reply 177 — participant_139 · 2022-04-27 · post-28236871

<!-- artifact:quote:start -->
> Wokeg said: Crusader Kings 3 Dev Diary #94 - Anatomy of a Struggle​Welcome comrades, to a dev diary I’ve been champing at the bit to write for months! Today, we’re going to be talking about the new struggle feature - what it is, how we’ve used it, and how it all works. The Basic Pitch​A struggle is a long-form conflict (generally not just a war, though they likely include them) covering a particular chunk of the map. They have different phases, each of which have different variant gameplay rules (e.g., “holy wars are disabled”, “characters of different religions may marry without”, or “Jerusalem can’t declare or be declared war on”). Phases progress between each other by way of catalysts, specific gameplay actions (“declare war on an involved character”, “two involved characters become soulmates”, etc.) that accrue points towards a future phase. When enough points are accrued, the phase changes to the new one. Struggles can be resolved, permanently affecting their area in some way, through dramatic and difficult ending decisions. They are assumed to last at least a couple of centuries: a conqueror carving out a new realm from the ruins of an old giant wouldn’t be a struggle by itself, but if it includes dramatic aftershocks that last for generations, then it just might be. Philosophy​So why are we introducing this mechanic attached to a flavour pack? Well, simply put, we didn’t think we could do the historical realities of Iberia justice without something like this. The changing moods and temperaments of the peninsula over different decades, the way particular activities fluctuated between oddly permissive (by the standards of much of the rest of the world) and intensely strict, the role of notable characters and their policies in shaping the shifting tides of public opinion whether intentionally or not… Medieval Iberia is just such a fascinating smorgasbord of mercurial special rules that we had to create a system that would allow us to model them, one that guided roleplay whilst giving it consequences, and provided default end goals for players other than just conquering all of Hispania. Though Iberia badly needed such a thing, it would have been a waste to create a system tailored for only Iberia. Complex and shifting local circumstances and long-form conflicts that don’t always take the form of actively-prosecuted warfare are things seen in many parts of the world, and a setting-agnostic system that catered to the peninsula but could be easily repurposed elsewhere seemed like a very worthwhile project to spend time on. So let’s get into how it works! Involvement​Struggles are, first and foremost, local things. Local to large areas (Iberia, for instance, is a decently sized little peninsula), but still local. The most basic thing that defines them, then, is the struggle region - a predefined group of titles that the rules of the struggle apply within. For FoI’s struggle, we’ve used the ol’ reliable world_europe_west_iberia region that’s been in the title since launch, but any region or combination of regions can be defined in the appropriate parameter. At the moment, these are static and only take regions, but we’re considering other options (e.g., titles, regions selected as part of the starting effect, etc.) for the future. View attachment 832624 Cultures and faiths are regarded as either involved or not. This defines whether a specific culture or faith is seen as being a part of the “in-group” for the region, even when members of that in-group may occasionally (or frequently) be very hostile to each other. For the Iberian Struggle, for instance, a Castilian and an Andalusian both understand the changing nature of the peninsula instinctively in a way that an Anglo-Saxon would struggle to acclimate to. Cultures become involved either on first starting a struggle, manually via script, or automatically when a certain percentage of their total counties are within the struggle region (the number is set per struggle, currently at 80% for the Iberian Struggle). Hybrids and divergent cultures automatically become involved if they convert at least one county within the region on creation. Neither cultures nor faiths lose their involvement automatically. Once they’re in, they’re in permanently, unless manually removed via script. For Fate of Iberia, this is necessary to keep the ruling class of al-Andalus, predominantly culturally insular families of Arabs or Berbers, involved, but it’s generally there to prevent wonky behaviour with struggles incorporating cultures and faiths from beyond their region who don’t actually have county within it. A simpler example would be a hypothetical Anglo-Norman struggle for after the Conquest. We’d probably want to set Norman up as an involved culture, and wouldn’t want them to immediately become uninvolved because there are no Norman counties in the British Isles. But Characters Tho?​Within the region, characters are defined by their personal involvement: the degree to which they’re considered part of the ongoing medley of social and cultural fluctuations that define an active struggle, and so how other characters (and counties) treat them. There are three levels to involvement: Involved Interloper Uninvolved Involved characters are those who are wholeheartedly engaged in the unique power dynamics of the struggle, and seen as insiders within the region. They may differ wildly from other involved characters, but involved characters are generally considered to appreciate the minutiae that make a struggle play differently from the rest of the world. Both their culture and faith must be flagged as being involved in the struggle, and either their capital is located within the struggle region or, if they’re unlanded, they’re physically there. Interlopers are active within a struggle’s region but don’t quite grasp exactly how or why people from the region act the way they do. They generally don’t benefit from variant struggle rules as much as involved characters, but also aren’t as heavily restricted by them. Either their culture, their faith, or both are not flagged as being involved in the struggle, but their capital (or physical location if landless) is located within the region. Uninvolved characters are outsiders and outlanders. Their concerns are remote to the struggle region, and even if they’re originally from that region, their isolation from it makes them lose touch with its subtleties and current events. Regardless of culture or faith, if their capital is located outside of the struggle region (or if they’re landless and physically not there), a character is considered uninvolved in that struggle. Uninvolved characters are generally expected to take penalties for holding counties within a struggle region, encouraging them to either delegate to vassals with a better level of involvement, or else getting more involved themselves. View attachment 832625 Phases​Alright, so we know how a struggle covers an area, and how people are divided up into categories within that area. What do these categories and this area actually do? For that, we need to look to phases. Each phase reflects a sort of mood or temperament within a struggle region specific to that struggle, the outcome of many prior actions leading to a shifting tide of general opinion about what is and isn’t acceptable. Maybe some things that were taboo become mainstream for a time, and things otherwise considered acceptable are baulked at by even very conservative characters. Though we’ll talk about how exactly you transition between phases a bit more in a moment, it’s worth noting that each phase has at least one (and usually more) future phase predefined for it, a phase that actions take in the course of play will gradually move the region’s “mood” towards. Within the Iberian Struggle, phases are on a loosely even cycle: though there’s some lateral movement and backtracking possible, they mostly move evenly in a circle. This is purely a design choice, and more esoteric flows are entirely scriptable. Manifesting the Mood​The actual effects of each phase can be split into three broad categories - parameters, character modifiers, and county modifiers. These are then further split by the involvement of different characters. Parameters work similarly to doctrine parameters in faiths, or tradition parameters for cultures. They’re special rules, entirely defined within script (and so fully moddable) that can be referred to elsewhere in script to unlock unique content, provide special exemptions, or block off specific actions. For example: in one phase, involved characters might be able to intermarry between faiths, in another, interlopers might receive cheaper holy wars whilst involved characters have them blocked entirely, and in both uninvolved characters may be blocked from culture converting involved cultures. View attachment 832626 As with other breeds of parameter, struggle parameters are identified purely by their exact spelling and can thus be reused simply by duplicating them, either within a struggle or in other struggles, making them very versatile rules. Character modifiers can be applied directly to involved or interloper characters. This generally chiefly affects involved characters, making some things easier and others harder, but we also use it to let interlopers occasionally have an easier time of bending or breaking local rules. Though these are our current guidelines, since these are all entirely scriptable, they can be changed according to the tonal needs of any given struggle. Uninvolved characters do not have a character modifier slot - we don’t want characters in India getting negative modifiers for not being involved or interlopers in a struggle in Iberia! Finally, we have county modifiers. These are applied to any county in the struggle region according to the direct holder of each county and their involvement; they generally have situational variables depending on phase for involved characters, mild to moderate debuffs for interlopers, and moderate to heavy debuffs for uninvolved characters. Catalysts​Transitioning from a phase to any of its future phases requires the activation of catalysts: notable events, gameplay actions, and consequences to existing mechanics that drive the current phase towards a specific future phase. Catalysts themselves can be anything. A war being declared, a type of character being seduced, a certain type of scheme failing, and so on. They’re set inside a phase’s future phase block, and, as with other elements of struggles, are entirely scriptable. Virtually any effect block in the entire title can be made into a catalyst with a bit of thought. Whenever a catalyst is activated, meaning that the thing that sets them happens, the current phase gains points towards the future phase that that catalyst was tied to (for instance, a notable interfaith marriage might help an uncertainty-focused phase gain points towards a tolerance-focused phase). Catalysts themselves are repeatable and the points they give vary with the difficulty of the catalyst in question - two notable characters becoming soulmates might well be worth more points than a notable character being executed, for instance. Points for put into simple tallies: when one tally for a future phase is met, that future phase becomes the new current phase, though there’s a grace period of a month before the actual switch. On the off chance that all of the dozens or hundreds of characters involved in a struggle are being incomprehensibly boring, we should note the existence of one special catalyst: the passage of time. Every phase has a default future phase, and receives a single point per year towards that phase’s tally, representing the natural trend of public discourse towards particular conclusions. This can (and essentially always will) be overridden or exacerbated by more dramatic catalysts being activated, but even in very calm struggle, change is always coming. Ending Decisions​A core part of the identity of struggles is that they’re not things that can be solved just by painting the map - after all, if they were, then the Iberian Struggle would’ve ended in its first decade when Musa ibn Nusayr had essentially subjugated the entire peninsula. We wanted to provide more difficult and interesting goals for ending a struggle than just conquering the whole struggle region. After all, it really doesn’t matter if you’ve conquered everyone if that hasn’t dealt with the underlying societal causes besetting a struggle locale. Ending decisions are our solution to this, being major, demanding decisions with consequences for the entire struggle region when taken and usually pretty intricate requirements. In order for a struggle to be endable through the usual flow, at least one phase must have an ending decision defined, though they can be ended manually through script also. The Iberian Struggle has three ending decisions, each tied (both mechanically and thematically) to a different phase). The Iberian Struggle​To finish up, let’s take a look at the new Iberian Struggle’s design (though I’ll put an obligatory reminder that this stuff isn’t final and that we generally continue to adjust things as we balance and playtest). The Iberian Struggle’s phases are Opportunity, Hostility, Compromise, and Conciliation. Opportunity can lead to either Hostility or Conciliation, depending on how the peninsula’s leaders treat each other, whilst both Hostility and Conciliation respectively build or degrade towards Compromise, which in turn decays into Opportunity, starting the cycle again. In Opportunity, Iberia is approaching a stage of uncertainty after notable spikes (hostile or friendly) in prior relations between faiths and cultures have abated. Struggle modifiers and parameters make war easier and cheaper, changing cultures and faiths easier and cheaper, but also unlock interfaith marriages and block off holy wars. Friendly interrelations between disparate characters activate catalysts guiding it towards Conciliation, whilst violent ones do the same for Hostility. For Hostility, aggressive actors have brought tensions to a simmering fever pitch, and even the slightest differences may be cause for aggressive persecution. The phase’s effects make wars cheaper and more brutal for all involved, reduce economic and technological progress, and increase the capacity of many characters for hostile schemes. Violence can’t persist forever though, and either efforts at building bridges or simple exhaustion will eventually bring even the most violent Hostility phase towards Compromise. Standing opposite Hostility is Conciliation, where pragmatic politicking builds bridges between even very disparate realms. Characters in this phase aren’t really tolerant by the modern meaning of the word, but many of the harsher biases of their time are temporarily dropped or ignored in the name of expediency. Wars become more expensive and truces longer, but there’s opportunity to unite against outsiders intervening in Iberian matters, and ruling over more multicultural and multifaith realms becomes easier and more beneficial. Periods of interreliance like this don’t generally last. Granted privileges decay, ignored biases relapse, and power-hungry nobles tear down bridges for short-term gain. Even the most wholeheartedly supported Conciliation phase decays towards Compromise eventually. Finally, Compromise. In this phase, Iberia has reached a point of equilibrium. Wars are less likely and most costly, but economic investment and other forms of passive stability are easier and better, whilst interfaith marriages flourish. The exhausted pragmatism of Compromise isn’t permanent, and will someday give rise to the cynical dynamism of Opportunity. The cycle begins anew. Naturally we’ve peppered all of this with phase-specific events, decisions, interactions, the odd CB, and so on. Most phases also add variant unlocking criteria to existing pieces of content, adjusting the circumstances under which things like the Claim Throne scheme or Found Holy Order decision can be used - most commonly temporarily extending them to characters who’d usually not have access. Say you don’t want to move on from a phase, though. Maybe you think Hostility’s the place for you, or you’d prefer a more permanent Conciliation, and want to break the endless cycle of social transmutation - well, unless you wanted permanent Opportunity, you’re in luck, because we’ve got ending decisions for Hostility, Compromise, and Conciliation. View attachment 832627 Hostility’s ending decision is Dominance, reflecting the final ascension of one of Iberia’s warring states to a position of not just military dominance, but social and spiritual hegemony. This gives your house an incredibly powerful modifier, making county and faith conversion within Iberia markedly faster, improving relations with those who share your faith or culture but markedly worsening them with other involved cultures or faiths, and making Holy Wars and Conquests cheaper and easier to access. It requires holding several important duchies, having a monocultural, monofaith primary kingdom, and being the only major player independent ruler in Iberia. View attachment 832628 Conciliation’s ending decision is Détente, making temporary accommodations into more permanent ones. Involved cultures gain a huge amount of cultural acceptance with each other, a house modifier that improves the opinion of different faiths and cultures, and several signature mechanics of the Conciliation phase become permanent for involved culture characters within Iberia: namely, interfaith marriage and disabled holy wars. Additionally, Iberian characters may join defensive wars for targets within Iberia against any aggressor from outside of Iberia. It requires a certain level of fame, being allied to every other independent involved Iberian ruler, and completely controlling an Iberian kingdom without controlling more than a certain fraction of Iberian territory. View attachment 832629 Compromise’s ending decision is Status Quo. Where Dominance is enforcing will and Détente finding accommodation, Status Quo is accepting that times have changed, that attempts to unite the peninsula are futile, and that its peoples and realms should go their separate ways and leave their neighbours be. Status Quo balkanises Iberia, transferring duchies to connected kingdoms if appropriate and making every kingdom within Iberia its own de jure empire whilst permanently destroying Hispania. Ruling houses across the former struggle region gain a modifier for two centuries making them better at fighting in lands of their own cultural heritage, whilst the capital counties of all independent rulers become strongholds for the next century. Some CBs within Iberia become more expensive. The requirements for Status Quo are a bit byzantine, essentially because it functions as the opt out decision if Dominance or Détente prove too difficult to work towards. If Iberia can’t be subjugated or coerced into cooperation then, in extremis, it can always be destroyed. Future Use​The Iberian Struggle is our first go at a struggle system, and it’s one we’re fairly pleased with. That said, we’ve certainly taken note of how the feature seems to have caught the popular imagination over the last week or so, and we’re very interested to hear your thoughts now that there’s a bit more information available. Needless to say, modders will be able to utilise this mechanic and share their creations from the release of 1.6 onwards. So, are there parts of the system you’d like to see refined and made more flexible? What are the struggles you’d like to see made in future? What’s your jankiest idea for hope for how to use the struggle system? As ever, I’ll be around in the thread for the next hour or so to answer your queries. Click to expand...
<!-- artifact:quote:end -->
a struggle system in finland would be nice. the dynamic powers of the norse, finnish tribes and other opportunistic conquerors Finns could unify, or norse take finland, or estonians take finland ?

## Reply 178 — participant_140 · 2022-04-27 · post-28236914

<!-- artifact:quote:start -->
> Agamidae said: Hot take: give every empire its own internal struggle. With Expansion, Competition, Prosperity, Decline phases. Click to expand...
<!-- artifact:quote:end -->
Agreed but it would need to be handled carefully. I would love more challenge to an empire because at that point the game becomes too easy/map painty and more instability for empires for the challenge is desirable (and fairly historical, ruling a large empire with a diverse population especially before all the advanced communications we have now should be challenging but rewarding when you do it right!)

## Reply 179 — participant_103 · 2022-04-27 · post-28236968

<!-- artifact:quote:start -->
> kuvetelxo said: The system itself seems to be quite complicated for me in theory, so I'm waiting to see what it looks like in practice. And as for the events to which I would see him, there is the issue of fights for the heritage of Carolingians on the starting date 872. It is quite rare to see that new monarchies of Germany and France arise in Western Europe, and the descendants of Charlemagne do not rebuild the power of their great ancestor or create a place For the new nations, therefore, such a system, which in its own way forces them to choose a certain path for history, seems to be a good solution for the Franks. Such an event could be focused on all the countries under the control of the Carolingian dynasty, making the Carolingian subjects, in the absence of their expansion, have an ever worse relationship with their suzerain, and the most powerful vassals would enjoy the special Casus Belli, or if a worthy successor to Charlemagne were found, this one would receive bonuses to accelerate its expansion and to recreate the Frankish Empire as a single domain linking the empires of France, Italy and Germany. I sincerely apologize in case of linguistic mistakes Click to expand...
<!-- artifact:quote:end -->
I agree that it's quite difficult to visualise without seeing examples, but I'm sure we will see much more over the coming weeks.

## Reply 180 — participant_141 · 2022-04-27 · post-28237059

This seems interesting and fun if implemented in a good way Is the idea in the future that players will be able to create struggles and/or that they can show up naturally due to for example the player taking over large amount of an empire from another culture and/or faith? I could see the system be used in some way of having feuds between dynasties if the relationship of the dynasty heads ever get too bad leading to negative opinion between members of the two dynasties. If I'm part of dynasty X I can see the consequences being it harder to sway someone from dynasty Y, marry them, making it harder to invite someone from dynasty Y to my plots but also whether I'm from dynasty X or a uninvolved dynasty it's easier to invite someone from dynasty X in a plot against a member from dynasty Y. The dynasty heads could also be permanent rivals. The end goals could be something like eliminating the other dynasty giving me a certain amount of splendor and prestige or to "bury the hatchet" giving both dynasties splendor and prestige but also maybe faith if both are from the same religion.

## Reply 181 — participant_142 · 2022-04-27 · post-28237109

I could see this struggle system used to represent the struggles within religions leading to new faiths. It could be used to to model the Christian schisms, to reform a Pagan religion, or the struggle between different schools of Islamic law.

## Reply 182 — participant_143 · 2022-04-27 · post-28237215

Please tell me that Sephardic Jewish courtiers in Iberia are automatically coded in as involved. So that if we decide to land one to switch characters and play them, they will automatically be involved in the struggle and your Muslim liege doesn’t automatically demand your conversion. Or if never landed, the AI has incentives to not immediately convert them into extinction. It is like minority religions in specific regions are always wiped out in a flash by the AI even when historically inaccurate (examples include Ethiopia or the historically very multireligious Khazaria, where all the pagans are immediately converted — both places I would love to see the struggle system added). Anyway, I think for representation it would be good for them to be coded in as involved from the beginning, regardless of whether they are landed.

## Reply 183 — participant_144 · 2022-04-27 · post-28237227

This almost seems to be tailor-made to represent the cycle of conquest, acceptance, and chafing under HRE rule in Italy, to be honest - from Charlemagne's conquest of Lombardy to the Italian Wars.

## Reply 184 — participant_145 · 2022-04-27 · post-28237343

<!-- artifact:quote:start -->
> Wokeg said: Though Iberia badly needed such a thing, it would have been a waste to create a system tailored for only Iberia. Complex and shifting local circumstances and long-form conflicts that don’t always take the form of actively-prosecuted warfare are things seen in many parts of the world, and a setting-agnostic system that catered to the peninsula but could be easily repurposed elsewhere seemed like a very worthwhile project to spend time on. Click to expand...
<!-- artifact:quote:end -->
This is the exact sort of creativity/initiative I think a lot of players including myself have been wishing for from various PDX titles for a while, and I'm so happy to see the development thought process head in this direction. I'm still quite sore about the various gripes caused by Royal Court regarding implementation of certain features, render lag on 3d simulations that seem unnecessary, and event bugs such as being asked to adopt your own child. But this is great, and I hope it sets a precedent for future patches and other teams (I don't mean to slander other teams, just that it feels as though a couple of titles have become... very samey/repetitive when it comes to flavour packs or reskinning old mechanics)

## Reply 185 — participant_146 · 2022-04-27 · post-28237454

It would be interesting if there could be dynamic struggle systems that could start to form over generations in an area. Right now its predefined due to mimic the events in history. But, what if the game could detect certain events in a region and create dynamic rules that would apply to that region due to generational occupation that lead to internal religious/cultural strife.

## Reply 186 — participant_147 · 2022-04-27 · post-28237465

I think it looks like a good system for the Hundred Years' War - could give some direction to the often anarchic mid/late game, and would resolve nicely to either English/French victory or a status quo.

## Reply 187 — participant_148 · 2022-04-27 · post-28237691

If I modded Sunset Invasion as a Western European Struggle, would Iberia have two Struggles at game start? Does the UI support that?

## Reply 188 — participant_149 · 2022-04-27 · post-28237831

Great work! In reply to ideas for Italy, I would love to see the struggle between republic vs feudal government systems (like peasant revolt results in republic instead of peasant leaders). Alternatively the struggle between Guelfi (papal supporters) vs Ghibellini (Emperor supporters) and maybe an enhanced papal mechanics linked to it

## Reply 189 — participant_150 · 2022-04-28 · post-28237952

<!-- artifact:quote:start -->
> ulriquinho said: Please tell me that Sephardic Jewish courtiers in Iberia are automatically coded in as involved. So that if we decide to land one to switch characters and play them, they will automatically be involved in the struggle and your Muslim liege doesn’t automatically demand your conversion. Or if never landed, the AI has incentives to not immediately convert them into extinction. It is like minority religions in specific regions are always wiped out in a flash by the AI even when historically inaccurate (examples include Ethiopia or the historically very multireligious Khazaria, where all the pagans are immediately converted — both places I would love to see the struggle system added). Anyway, I think for representation it would be good for them to be coded in as involved from the beginning, regardless of whether they are landed. Click to expand...
<!-- artifact:quote:end -->
I strongly agree

## Reply 190 — participant_150 · 2022-04-28 · post-28237956

I think the Sephardic culture although no county exists for it should be an involved culture, because Sephardic culture (Iberian jewish culture) is by its very definition linked to iberia. Sephardic Jews went through periods of prominence and repression during this period. I think the stage system should influence the prominence of Iberias jews, for example in the compromise phase when interfaith marriages become more common you should have a higher chance of getting Sephardic jews in your court (particularly in Muslim realms), while in the Hostile phase you should have more Sephardic Conversos in your court (mainly in Christian realms) this would reflect how in tolerant times the jews enjoyed a "golden age", but in tough times they were often forced to convert.

## Reply 191 — participant_151 · 2022-04-28 · post-28237978

Oh god this system would be sooooo cool with the Northern Crusades. It was such a complex and interesting conflict involving a ton of different facets (migrations, interfaith relations, colonization etc.) that really cant be done justice by the current Crusade system would absolutely love something like that. Oh also the conflict between England and France with the Angevin Empire leading into the hundred years war sounds amazing. The struggle feature might be one of the best additions to Crusader Kings yet! Cant wait to see it in action

## Reply 192 — participant_152 · 2022-04-28 · post-28238033

What is Batalawys? Never heard of it.

## Reply 193 — participant_031 · 2022-04-28 · post-28238035

<!-- artifact:quote:start -->
> Bshepp said: I think the Sephardic culture although no county exists for it should be an involved culture, because Sephardic culture (Iberian jewish culture) is by its very definition linked to iberia. Sephardic Jews went through periods of prominence and repression during this period. I think the stage system should influence the prominence of Iberias jews, for example in the compromise phase when interfaith marriages become more common you should have a higher chance of getting Sephardic jews in your court (particularly in Muslim realms), while in the Hostile phase you should have more Sephardic Conversos in your court (mainly in Christian realms) this would reflect how in tolerant times the jews enjoyed a "golden age", but in tough times they were often forced to convert. Click to expand...
<!-- artifact:quote:end -->
If we're lucky, whichever brand of Judaism is involved in Spain is the fourth religion that's involved in the earlier screenshots (making it Catholic, Mozarabic, Muwalladi, and the type of Judaism). I however suspect it's one of the neighbouring brands of Islam that is involved. If it *is* a Jewish branch, then all it would take would be including Sephardi as an involved culture, and Sephardi jews in the area would be involved if unlanded, and of course if they became landed somehow.

## Reply 194 — participant_031 · 2022-04-28 · post-28238037

<!-- artifact:quote:start -->
> EarlKonrad said: What is Batalawys? Never heard of it. Click to expand...
<!-- artifact:quote:end -->
Probably a dynasty, since Muslim realms seem to be named for the owning dynasty. Looking back at a CK2 thread, it could be one of the duchies (Extremadura) under a different name. (Under the Marwanids according to that thread). Andalusian suggestions I have some problems when playing in Andalusia in the 867 stardate, the dinasty of the duchy of Batalwys or Extremadura, the marwanids or Al-marwani, they are badawi, when in history they were a muladi family coming from the north of iberia, and... forum.paradoxplaza.com

## Reply 195 — participant_150 · 2022-04-28 · post-28238043

<!-- artifact:quote:start -->
> DreadLindwyrm said: If we're lucky, whichever brand of Judaism is involved in Spain is the fourth religion that's involved in the earlier screenshots (making it Catholic, Mozarabic, Muwalladi, and the type of Judaism). I however suspect it's one of the neighbouring brands of Islam that is involved. If it *is* a Jewish branch, then all it would take would be including Sephardi as an involved culture, and Sephardi jews in the area would be involved if unlanded, and of course if they became landed somehow. Click to expand...
<!-- artifact:quote:end -->
It's Rabbinism

## Reply 196 — participant_031 · 2022-04-28 · post-28238060

<!-- artifact:quote:start -->
> Bshepp said: It's Rabbinism Click to expand...
<!-- artifact:quote:end -->
Thanks. I wasn't going to risk starting up the game to try to check, only to get sucked into another all night session.

## Reply 197 — participant_153 · 2022-04-28 · post-28238099

If the Struggle system can be used to simulate Interregnum/Succession Crises then 867 Tibet can benefit. Last time I played there there 2 claimants to the Empire of Tibet and no good way to recreate the title that was any different from creating it from scratch

## Reply 198 — participant_143 · 2022-04-28 · post-28238318

<!-- artifact:quote:start -->
> Bshepp said: I think the Sephardic culture although no county exists for it should be an involved culture, because Sephardic culture (Iberian jewish culture) is by its very definition linked to iberia. Sephardic Jews went through periods of prominence and repression during this period. I think the stage system should influence the prominence of Iberias jews, for example in the compromise phase when interfaith marriages become more common you should have a higher chance of getting Sephardic jews in your court (particularly in Muslim realms), while in the Hostile phase you should have more Sephardic Conversos in your court (mainly in Christian realms) this would reflect how in tolerant times the jews enjoyed a "golden age", but in tough times they were often forced to convert. Click to expand...
<!-- artifact:quote:end -->
This is an excellent suggestion. And yeah even if it is an oversight that they didn’t include Rabbinism as the fourth religion or Sephardic as one of the involved cultures, it is not too late to add them in. And this isn’t something that should have to be modded in. Specifically because I think this is important both re: representation and historical accuracy. By the way, this probably my own major concern (I also hope/am concerned about whether the AI takes to heart incentives to not convert involved courtiers/vassals during the more peaceful phases). Otherwise, I think this sounds like a solid solid solid dlc. If I had a harsh tone in my first post on the subject, it is because I feel strongly about including representation when such a solid opportunity like this presents itself. Oversights are easy, especially when we are just talking about a handful of courtiers. But adding last minute little details, like your suggestion, to the courtiers can make a dlc that much better! So I really hope the devs listen to this discussion! And if there was an oversight, please devs, don’t take it as a calling out, but rather as a strong suggestion to correct the oversight before release! And if it was included, good job!

## Reply 199 — participant_154 · 2022-04-28 · post-28238625

<!-- artifact:quote:start -->
> Wokeg said: they generally have situational variables depending on phase for involved characters, mild to moderate debuffs for interlopers, and moderate to heavy debuffs for uninvolved characters. Click to expand...
<!-- artifact:quote:end -->
Does this mean that conquering within the struggle region as a foreign power is very difficult? So i can't swoop in as a foreign empire and just take over all of the territory, because the conflict has the people to involved in their own struggle than to bother with my foreign rule? Or what exactly is meant by "moderate to heavy debuffs for uninvolved characters"?

## Reply 200 — participant_155 · 2022-04-28 · post-28238665

The struggle system can be used on a smaller scale? For example a struggle between dynasties, two characters or a personal struggle?

## Reply 201 — participant_152 · 2022-04-28 · post-28238800

<!-- artifact:quote:start -->
> DreadLindwyrm said: Probably a dynasty, since Muslim realms seem to be named for the owning dynasty. Looking back at a CK2 thread, it could be one of the duchies (Extremadura) under a different name. (Under the Marwanids according to that thread). Andalusian suggestions I have some problems when playing in Andalusia in the 867 stardate, the dinasty of the duchy of Batalwys or Extremadura, the marwanids or Al-marwani, they are badawi, when in history they were a muladi family coming from the north of iberia, and... forum.paradoxplaza.com Click to expand...
<!-- artifact:quote:end -->
I can't find any mention of Google of it outside of said DD and a single posting in Spain. One would think that that type of information wouldn't be this obscure which, to me, raises a question of its validity. I do know of a municipality in Brazil called Batataus, but as far as I know it's name has nothing to do with Iberia.

## Reply 202 — participant_156 · 2022-04-28 · post-28238878

Investiture, conflict of primacy over religion (historically between Kaiser of the HRE and Pope), but maybe could be adopted to different secular ruler or different religion (with hierocratic leadership) altogether. Also some struggles for unions of Kingdoms with different cultures could be interesting as well. Let's say Poland and Bohemia in union under one ruler (which have different cultures) have problems with compatibility and it could be overcomed by one of the cultures in the region including divergent and especially hybrid ones becoming the majority culture.

## Reply 203 — participant_050 · 2022-04-28 · post-28238911

<!-- artifact:quote:start -->
> EarlKonrad said: What is Batalawys? Never heard of it. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> EarlKonrad said: I can't find any mention of Google of it outside of said DD and a single posting in Spain. One would think that that type of information wouldn't be this obscure which, to me, raises a question of its validity. I do know of a municipality in Brazil called Batataus, but as far as I know it's name has nothing to do with Iberia. Click to expand...
<!-- artifact:quote:end -->
Badajoz. I don't know if it means the city of Badajoz or the region/kingdom in CK3, since that is called ''Badajoz'' too. I live in the region, so is pretty funny seeing all this. Try Batalyaws. Paradox misspelled it.

## Reply 204 — participant_154 · 2022-04-28 · post-28239049

<!-- artifact:quote:start -->
> $ilent_$trider said: What is the reasoning behind making every independent ruler an Emperor if deciding for status quo? I get the reasoning behind destroying Hispania. I don't get making Kings into Emperors. Click to expand...
<!-- artifact:quote:end -->
it is probably to break up existing De Jure structures and truly have settled what belongs where in this status quo.

## Reply 205 — participant_152 · 2022-04-28 · post-28239123

<!-- artifact:quote:start -->
> Monalba said: Badajoz. I don't know if it means the city of Badajoz or the region/kingdom in CK3, since that is called ''Badajoz'' too. I live in the region, so is pretty funny seeing all this. Try Batalyaws. Paradox misspelled it. Click to expand...
<!-- artifact:quote:end -->
Oh, that makes sense. Batalawys and Badaloz are phonetically a bit similar. Can see the confusion there. That you for clarifying that.

## Reply 206 — participant_157 · 2022-04-28 · post-28239361

<!-- artifact:quote:start -->
> EarlKonrad said: Oh, that makes sense. Batalawys and Badaloz are phonetically a bit similar. Can see the confusion there. That you for clarifying that. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Monalba said: Badajoz. I don't know if it means the city of Badajoz or the region/kingdom in CK3, since that is called ''Badajoz'' too. I live in the region, so is pretty funny seeing all this. Try Batalyaws. Paradox misspelled it. Click to expand...
<!-- artifact:quote:end -->
I can't wait for fate of iberia to launch so I can make butr-portugese hybrid (Butrgese) Oh no, an intern is probably being whipped now

## Reply 207 — participant_158 · 2022-04-29 · post-28240465

<!-- artifact:quote:start -->
> Skidofly said: Could the struggle system be implemented to England during the Norse invasions? Click to expand...
<!-- artifact:quote:end -->
Or Southern Italy during the battles between the Lombards, the Papacy, the Normans, the Greeks, the HRE and the Muslims. Shifting alliances. Shifting warfare. Lord knows the Hautevilles sure are popular to play as. Doesn't hurt that they are neighbors of Matilda the Much Simped.

## Reply 208 — participant_157 · 2022-04-29 · post-28240693

<!-- artifact:quote:start -->
> Brian Bóruma said: Or Southern Italy during the battles between the Lombards, the Papacy, the Normans, the Greeks, the HRE and the Muslims. Shifting alliances. Shifting warfare. Lord knows the Hautevilles sure are popular to play as. Doesn't hurt that they are neighbors of Matilda the Much Simped. Click to expand...
<!-- artifact:quote:end -->
Or just italy in general, is sicily forever lost or is the hre able to reclaim the southern lombard princes holding, railroad collapse of Central power in wake of matilda's death, occilate between extremes of independent Italian republics and centralised hre. Could also interact with general investiture controversy, for if papal states sans rome prefer loyalty to emperor or not, as did in late 18th; if pope so weak he's not able to bequeath the kingdom of sicily to the hautevilles so they're stuck at being the 3 counts (dukes) until emperor or pope strong enough to make titles, like how fate of iberia is going to turn small kings into emperors and shatter e_iberia

## Reply 209 — participant_159 · 2022-04-29 · post-28241318

looking forward!

## Reply 210 — participant_158 · 2022-04-29 · post-28241610

<!-- artifact:quote:start -->
> YellowPress said: Or just italy in general, is sicily forever lost or is the hre able to reclaim the southern lombard princes holding, railroad collapse of Central power in wake of matilda's death, occilate between extremes of independent Italian republics and centralised hre. Could also interact with general investiture controversy, for if papal states sans rome prefer loyalty to emperor or not, as did in late 18th; if pope so weak he's not able to bequeath the kingdom of sicily to the hautevilles so they're stuck at being the 3 counts (dukes) until emperor or pope strong enough to make titles, like how fate of iberia is going to turn small kings into emperors and shatter e_iberia Click to expand...
<!-- artifact:quote:end -->
Not just Sicily but also Sardinia. Cagliari has silver mines, is the capital of the duchy and kingdom, and is one of the most (hypothetically) valuable provinces in the game. Also a fairly easy kingdom to create.

## Reply 211 — participant_160 · 2022-04-30 · post-28241729

So, I would love to see a way for someone to be invited into a crisis, probably during period of hostility, to simulate how at times people in the region would invite interlopers in to a conflict to try and decide it (The almovarids for example). If they fail, then they revert back to ininvolved. If they succeed, well they now have land in the region and it depends on what they do with it.

## Reply 212 — participant_161 · 2022-04-30 · post-28242099

This in Anatolia and the Balkans for a challanging Byz campaign, fighting on two fronts

## Reply 213 — participant_157 · 2022-04-30 · post-28242453

<!-- artifact:quote:start -->
> stratigo said: So, I would love to see a way for someone to be invited into a crisis, probably during period of hostility, to simulate how at times people in the region would invite interlopers in to a conflict to try and decide it (The almovarids for example). If they fail, then they revert back to ininvolved. If they succeed, well they now have land in the region and it depends on what they do with it. Click to expand...
<!-- artifact:quote:end -->
I can guarantee you they'll be invitations

## Reply 214 — participant_162 · 2022-05-01 · post-28243383

I mean I'm parroting everyone else everywhere. But the easiest fit is certainly England and the Norse invasion. It fits almost prefectly and would make that area even more interesting than it already is from the last flavour pack. My issue is that I'd like to not play as the norse or england for a while. I love that we're getting iberia. That area always felt weird, playing as either of the 3 brothers always felt a bit stale, just capture everything and convert everything. There was no spice...now it seems we're getting it. I dont know much about India or Africa, and perhaps introducing struggles within those area would encourage people to learn about and play those areas. I'm sure struggles would introduce a lot of flavour in India since there are a number of conflicts between traditional Bhuddists, "modern" Hinduism, and the Islamic invasions all throughout the years available to us in game.

## Reply 215 — participant_163 · 2022-05-01 · post-28243532

Certainly looks promising. However reading through this thread, now literally every single piece of the map been suggested for this mechanic. Now why don't we all just wait for the DLC, play like 2-3 runs in iberia from different angles. After that everyone will be in a better spot judging if there is a need for a struggle mechanic anywhere and everywhere.

## Reply 216 — participant_164 · 2022-05-01 · post-28243835

The fact that the team feels like they need to implement struggles shows that there was an initial, basegame level failure in the design of the sandbox. If the sandbox was better prepared, a struggle system wouldn't be necessary or would be much different. So far it just seems like it's there to force something to happen on the map that could have been happening already if Casus Bellis and war systems had been further improved from ck2. Struggles look like they will artificially force a historic situation/environment into the sandbox instead of setting the sandbox up in a way that encourages such situations "naturally". Buut well, it's too late to make engine/basegame level changes at this point, I assume, so this will have to do. Will probably be fun anyway. Edit: Since it's a common sentiment, I should clarify I'm not saying I think this content should have been in the basegame release, or that it was withheld. I'm saying that if the basegame design was done properly, this content would not have been necessitated at all.

## Reply 217 — participant_165 · 2022-05-01 · post-28243850

<!-- artifact:quote:start -->
> ZeDango said: The fact that the team feels like they need to implement struggles shows that there was an initial, basegame level failure in the design of the sandbox Click to expand...
<!-- artifact:quote:end -->
The struggle system at it's core is a system that permit to change the global systems of the game based on location and past event. In my opinion, it is a really nice addition that can, if well designed give us a changing world, more fluid and that feel more personal. As such, the struggle system doesn't correct a mistake so it doesn't show failure. Also, because it is not scripted event, it will not be less sandboxy, more like different types of sands in a big sandbox.

## Reply 218 — participant_164 · 2022-05-01 · post-28243858

<!-- artifact:quote:start -->
> Fovéa said: The struggle system at it's core is a system that permit to change the global systems of the game based on location and past event. In my opinion, it is a really nice addition that can, if well designed give us a changing world, more fluid and that feel more personal. As such, the struggle system doesn't correct a mistake so it doesn't show failure Click to expand...
<!-- artifact:quote:end -->
That's the point. It's an additional system and mechanic that permits things to happen where the sandbox already should be allowing such or similar things to occur.

## Reply 219 — participant_119 · 2022-05-01 · post-28244281

<!-- artifact:quote:start -->
> Sphem said: Bulgarians, Seljuks/Rûm and Byzantium! Click to expand...
<!-- artifact:quote:end -->
Oh and Russian princes squabbling!

## Reply 220 — participant_166 · 2022-05-02 · post-28244775

<!-- artifact:quote:start -->
> ZeDango said: That's the point. It's an additional system and mechanic that permits things to happen where the sandbox already should be allowing such or similar things to occur. Click to expand...
<!-- artifact:quote:end -->
yes, maybe, if the "sandbox" were a perfect simulation of reality and medieval politics. but that's a pipe dream anyway, so who cares?

## Reply 221 — participant_132 · 2022-05-02 · post-28244837

<!-- artifact:quote:start -->
> Pistike said: reading through this thread, now literally every single piece of the map been suggested for this mechanic. Click to expand...
<!-- artifact:quote:end -->
Lmao this

## Reply 222 — participant_013 · 2022-05-02 · post-28245502

<!-- artifact:quote:start -->
> ZeDango said: That's the point. It's an additional system and mechanic that permits things to happen where the sandbox already should be allowing such or similar things to occur. Click to expand...
<!-- artifact:quote:end -->
It's impossible for it to have been set up in such a way. Think about how many things have to go just right for these kind of situations to have arisen in the real world. That means that in order to be "Properly set up" the devs have to be able to take every single possible situation into account. Especially the Player who can literally do anything, and plan towards a long term goal. The devs have no way, shape or form to take the player into account. How do you account for a Duke of Sardinia or Corsica who converts to Hellensim in the mid 900's and forms a Kingdom with Siciliy, Sardinia, and the Mallorcas?

## Reply 223 — participant_167 · 2022-05-02 · post-28245666

One thought I had on the rules for involved, uninvolved and interloper characters was that theses mechanics, or ones closely related, could be used to represent smaller regions that were difficult to conquer and control from the outside, or that were notably independent or troublesome even while part of another realm. Any character whose capital wouldn't be in the region would be an uninvolved character, so if lording over that region, would be under different rules than any characters in that region, while any invader into the region who settled there would likely be an interloper. There's a lot of potential in mechanics like this for remote and inhospitable regions to play in interesting ways that make them trouble for outsiders going in there, but without making the rulers in that region overpowered.

## Reply 224 — participant_168 · 2022-05-03 · post-28246458

<!-- artifact:quote:start -->
> Tuo said: One thought I had on the rules for involved, uninvolved and interloper characters was that theses mechanics, or ones closely related, could be used to represent smaller regions that were difficult to conquer and control from the outside, or that were notably independent or troublesome even while part of another realm. Any character whose capital wouldn't be in the region would be an uninvolved character, so if lording over that region, would be under different rules than any characters in that region, while any invader into the region who settled there would likely be an interloper. There's a lot of potential in mechanics like this for remote and inhospitable regions to play in interesting ways that make them trouble for outsiders going in there, but without making the rulers in that region overpowered. Click to expand...
<!-- artifact:quote:end -->
It would also make a lot of historical scenarios more balanced, where a small power held out against a larger power for a very long time. In the game right now, those smaller powers tend to just... get steamrolled.

## Reply 225 — participant_169 · 2022-05-03 · post-28246478

Not sure if this has already been suggested, but could the struggle system be used for feuds between houses and dynasties?

## Reply 226 — participant_111 · 2022-05-09 · post-28257658

<!-- artifact:quote:start -->
> Wokeg said: Involved characters are those who are wholeheartedly engaged in the unique power dynamics of the struggle, and seen as insiders within the region. They may differ wildly from other involved characters, but involved characters are generally considered to appreciate the minutiae that make a struggle play differently from the rest of the world. Both their culture and faith must be flagged as being involved in the struggle, and either their capital is located within the struggle region or, if they’re unlanded, they’re physically there. Click to expand...
<!-- artifact:quote:end -->
After a little thinking, I'm not entirely sold on the requirement to be within the region in order to be considered involved. This makes it very easy for important but unlanded, and even some landed characters, to fall out of the loop. Let me provide two examples: 1 - the Catholic queen regnant of Castile is deposed in a civil war, has her Iberian holdings revoked and eventually finds shelter at her husband the duke of Poitou's court. From there, she schemes and arranges marriages all over the peninsula to get her line back on the throne. She still has friends and followers back home, but from the Struggle's perspective whatever she does doesn't matter. 2 - let's say that the county of Carcassonne, located just outside of the Iberian region, has been converted to an Iberian culture early in the game. Say that it's ruled by the duke of Barcelona, who is in all respects involved in the struggle against Al-Andalus. Yet for some reason the culturally Iberian barons of Carcassonne are not considered involved in the same fight that their brethren in the neighboring Rosselló are fighting. Perhaps if a character's religion and culture match the struggle, then they should be considered involved even when they're outside of the region, provided that their place of residence shares their culture and is physically connected to the region by a string of same-culture counties?

## Reply 227 — participant_164 · 2022-05-12 · post-28263473

<!-- artifact:quote:start -->
> Zhetone said: yes, maybe, if the "sandbox" were a perfect simulation of reality and medieval politics. but that's a pipe dream anyway, so who cares? Click to expand...
<!-- artifact:quote:end -->
Wow, amazing, your asinine sarcasm added a lot to this debate. My viewpoint has been entirely shifted and I am truly glad I had this conversation.

## Reply 228 — participant_170 · 2022-05-16 · post-28272815

<!-- artifact:quote:start -->
> Wokeg said: Needless to say, modders will be able to utilise this mechanic and share their creations from the release of 1.6 onwards Click to expand...
<!-- artifact:quote:end -->
To clarify: would it be possible to mod a custom Struggle without requiring players to own the flavor pack?

