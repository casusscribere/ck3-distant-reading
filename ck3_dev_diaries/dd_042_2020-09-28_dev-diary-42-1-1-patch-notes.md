---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1428193/"
forum_thread_id: 1428193
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 42
title: "CK3 Dev Diary #42 - 1.1 Patch Notes"
dd_date: 2020-09-28
author_handle: rageair
expansion: Post-release patches
patch: Patch 1.1 (Chevron)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 15471
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1428193'
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
    location: raw_lines_~28_to_120
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_122_to_123
    action: preserved_and_flagged
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #42 - 1.1 Patch Notes

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Sep 28, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-42-1-1-patch-notes.1428193/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-42-1-1-patch-notes.1428193/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-42-1-1-patch-notes.1428193/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-42-1-1-patch-notes.1428193/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-41-a-grand-thank-you.1420381/ "CK3 Dev Diary #41 - A Grand Thank You!") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-43-a-ruler-of-your-own.1441657/ "CK3 Dev Diary 43 - A Ruler of Your Own")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-42-1-1-patch-notes.1428193/?prdxDevPosts=1)

[Threadmarks](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-42-1-1-patch-notes.1428193/threadmarks "Threadmarks")

[View all 1 threadmarks](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-42-1-1-patch-notes.1428193/threadmarks)

---
[Reader mode](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-42-1-1-patch-notes.1428193/reader/)

---


#### Recent threadmarks

[1601296162,1601296162](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-42-1-1-patch-notes.1428193/#post-26961271 "Threadmark created by rageair on Sep 28, 2020")

[Reader mode](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-42-1-1-patch-notes.1428193/reader/)

- [Sep 28, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-42-1-1-patch-notes.1428193/post-26961188)
- [Replies: 915](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-42-1-1-patch-notes.1428193/#posts)


- [/forum/developer-diary/ck3-dev-diary-42-1-1-patch-notes.1428193/post-26961188](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-42-1-1-patch-notes.1428193/post-26961188)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/26961188/bookmark "Bookmark")

Greetings!  

Tomorrow is the day when patch 1.1 will drop, and we’re very excited to share it with you! We've made a variety of UI improvements, fixed a whole bunch of bugs, and addressed many common issues players have run into. Using the standard Paradox unit of measurement, the changelog comes in at 5.3 [@Groogy](https://forum.paradoxplaza.com/forum/members/162573/) in length. Without further ado, here’s the changelog in all its glory!  

WARNING: It is really long, so only open the Spoiler Block if you want to see the entire changelog:  

(No really, it is MASSIVE.)  

Spoiler: 1.1 Patch Notes

#########################################  
#########################################  
################ 1.1.0 ####################  
#########################################  
#########################################  

###################  
# Game Balance  
###################  
- A woman being close to the fertility cutoff cap (3 years) now gives the 'Low Fertility' marriage penalty.  
- Being unable to inherit titles no longer blocks claim inheritance. The Castrated, Bastard, and Disinherited traits still block claim inheritance. Only from within your dynasty for Disinherited  
- Building a new Temple now gives much more piety, you can't do it too often anyways  
- Cities and Temples now follow the same cost scale as Castles  
- Clan rulers now desire fewer spouses the lower their tier is. The Piety penalty only triggers if they are below desired spouses. The numbers are: Baron/Count wants one, Dukes two, Kings three, and Emperors four.  
- The Piety hit from being below desired spouses has been doubled.  
- Confederate Partition now ignores land held by vassals with title allegiance when there's titles with their own separate succession (E.G., elective titles, titles with their own gender laws). This means no more creating a kingdom where all the vassals will go with another title  
- Courtiers you have a kid with are now slightly more likely to stick around  
- Creating a title will now cause vassals dejure under it to lose title allegiance if their allegiance is to a title of the same tier. E.G., creating the empire of Italia as the HRE will cause the Italian vassals to lose allegiance to the HRE  
- Denying Call to Arms now costs Fame, potentially reducing your Level of Fame. Denying offensive wars has a small impact, but denying defensive calls have a massive impact.  
- Denying a defensive war now reduces opinion with your ally by -50 for 25 years (decaying)  
- Denying an offensive war now reduces opinion with your ally by -20 for 5 years (decaying)  
- Slashed the opinion modifier from Diplomacy by half  
- Diplomacy skill now gives a prestige mult % (with offset)  
- Electors should now be less inclined to form or join independence factions, unless they're another faith than their liege  
- Fixed pregnancy chance remaining unchanged for significant fertility spans before dropping drastically. Now the reduction in pregnancy chance is gradual instead. E.G., before the couple's fertility dropping from 53% to 52% would cause the chance of pregnancy to drop from 3% to 2% per month, while now it'll go from 2.52% to 2.47%  
- For player cultures, the culture head now updates within a month when one ruler becomes bigger than another  
- For player dynasties, the dynast now takes at most one month to update when someone else becomes more than 10% stronger, rather than up to a year  
- Giving away a holding of the wrong type as an ambitious or greedy character will no longer incur stress  
- Greedy gift-receivers now no longer demand insane amounts of additional gold  
- The AI is now much more likely to demand the conversion of heretical vassals, if their refusal would result in them being marked as criminals. This should make the AI less likely to collapse to heresy.  
- Heresiarchs will no longer accept demands of conversion.  
- Denying a conversion request now gives the liege a revoke reason, in addition to the imprisonment reason they already got.  
- Outbreaks of heresy now increase the Fervor of the affected Faith much more positively. This means that large faiths are more likely to bounce back to max Fervor after a Heresy outbreak.  
- If a vassal asks for something in return for you asking them to convert faith, denying their request no longer gives you an imprisonment/revoke reason on them (you're being impious by not parting with simple material wealth!)  
- If you have Partition and your primary title has a special election form, the heir to that title will be the primary heir for your Partition and get a share as long as they're a valid player heir, even if they otherwise wouldn't have been part of the Partition, or later in the Partition order  
- Increased cooldown on asking vassal to convert faith to 15 years  
- Inheritance succession can now go up to 6 generations upwards to find a distant relative rather than just 3  
- It is now harder to murder someone you're at war with, or murder their vassals/courtiers  
- The maximum success chance/secrecy of Abduct Schemes are now 85% (down from 95%).  
- It is now practically impossible to abduct someone you're at war with, with a lesser penalty to their vassals/courtiers  
- It's now much harder to scheme to abduct Rulers (especially Foreign Rulers) and subjects of a foreign court.  
- Knights will more often gain prowess and blademaster traits in battle  
- Large realms are now unlikely to convert religion in wars  
- Lowered the attack stat of Pikemen  
- Lowered the recruitment costs of MaA  
- Made a number of interactions unavailable if you're at war with the target (E.G., it makes no sense to ask the Pope for money while you're at war with her)  
- Made diplomacy affect the opinion gained from gifts much more (x3)  
- Military prestige/piety maintenance costs no longer reduce you Fame/Devotion gain  
- Opinion from multiple elective titles no longer stacks for each title with the law, it happens once per vassal based on their title allegiance's law.  
- Outnumbering the enemy now further increases the survivability of your knights  
- The Pechenegs are now a bit more stable at game start  
- Rebalanced debt so that it now comes in levels. The higher the level, the harsher the penalties. Penalties include levy reductions, to make severely indebted realms collapse easier.  
- Reclusive characters will no longer host feasts  
- Removed the stress loss for lustful characters when renouncing celibacy, as it could lead to free stress loss  
- Significantly nerfed the 'resurging saoshyant' modifier  
- Slightly reduced the cost of Main holdings  
- Vastly empowered the Mongol Empire's armies. Now you will truly learn to fear the horsemen of the steppe!  
- Temujin & co now starts off with substantial prowess scores.  
- Temujin now starts with a full roster of knights, as well as a few Han siege engineers.  
- The Mongol Empire is now much more aggressive, and will attack several times per year, if opportunity arises.  
- Weak realms are now much more likely to agree to subjugation by the Mongol Empire.  
- The Borjigin Dynasty is no longer obscure, and starts with a few Warfare legacies unlocked.  
- Ask to Take the Vows cooldown increased to 10 years.  
- Ask to Take the Vows now costs piety to use, rather than giving you piety.  
- Ask to Take the Vows improves the opinion of your Court Chaplain and Head of Faith when used.  
- The 'Take the Vows' interaction can now be used on characters of 10 years or older (used to be only Adults).  
- The 'Take the Vows' interaction can now be used on characters that are married or betrothed.  
- The 'Take the Vows' interaction can now be used on characters that stand to inherit titles, this means that it's possible to prune your partition inheritance by disinheriting children using this tool.  
- The AI acceptance values of Ask to Take the Vows have been massively reworked to take many things into account. Most notably having a Learning Education makes children much more likely to want to go to church.  
- Using Ask to Take the Vows on someone now moves them away from your court, into the court of a theocrat in the realm (if there's one) or into the pool.  
- You can not force characters married/betrothed in the incorrect lineality to Take the Vows (i.e. Women in a Patrilineal Marriage).  
- You now need a Strong Hook to force acceptance of Ask to Take the Vows. Weak Hooks give a bit of acceptance instead.  
- The AI is now more inclined to buy certain MaA based on their culture  
- The AI is now more inclined to recruit their cultural MaA  
- The AI is now much more likely to request money from their Head of Faith, especially if their HoF is very rich  
- The AI is now reluctant to betroth boys to old women, regardless of them sharing their dynasty or not.  
- The AI now only wants to spend money on recruiting guest claimants that have claims on bordering realms  
- The AI (primarily War Defenders) will now consider White Peace more often, to avoid dragging wars on needlessly. They'll look at how long the war has lasted for, and compare that to their current War Score. This should reduce the number of extremely drawn-out wars.  
- The AI will now account for Bankruptcy when considering White Peace. Starting at -100 gold, the AI will then progressively pursue White Peace more as they fall deeper into debt (-2 years of income, and -4 years of income), offsetting this by how close they are to winning (at 80 or above War Score, the AI will try to 'toughen it out' as the winnings from the war is more likely to outweigh the expenses of maintaining their army).  
- The AI will now only demand conversion from vassals if they have the money to pay their demands, if the vassal is unlikely to simply accept straight-up.  
- The AI will now take age and fertility into account when marrying away any character of a reputable house, not only their own. This should make it less likely for interesting characters to end up in fruitless marriages.  
- The Exclave Independence game rule now triggers closer to succession for AI rulers  
- The Inbred trait is now much less likely to be inherited, but further reduces fertility  
- The Renown gain from alive dynasty members is now capped at 2/month (100 alive members)  
- The Strong Blood dynasty modifier now only improves the chance of characters with no inherited genetic traits getting a positive one by 400%, rather than 40 000%. +400% means that the chance of getting Comely for instance is 2.5% instead of 0.5%  
- The holder of Jerusalem is now unlikely to accept Populist demands  
- The opinion hit from being unallied as a Clan vassal has been increased to 15 for non-powerful vassals, and 30 for powerful vassals.  
- Titles automatically destroyed due to a ruler getting unlanded now gives that rulers claims if they received claims on the counties they lost  
- Turks are now more likely to assimilate to local cultures than they were  
- Under Partition, higher-tier titles no longer reduce the number of counties you get. In practice what this tends to mean is that in some (but not all) cases where your primary heir would get only one or two counties, they get one more  
- Very non-zealous characters will now revoke titles from other-faith vassals if that'd be the best for the realm, presuming that there's no tyranny loss.  
- Viking vassals are now more restricted when it comes to overseas conquests  
- Wandering characters who decide to marry will now prefer to marry a character traveling with them, rather than creating a spouse  
- Winning a Great Holy War as the attacker now refills all the levies and garrisons in the counties taken  
- Wounded Knights are now less likely to die in battle  
- You can now manage the focus of your children even if they're landed, as long as you're their liege  
- You may now revoke the last county of someone who holds a duchy or higher that is impossible to revoke (E.G., a head of faith title). That will lead to that higher title getting destroyed  
- You must be at peace to create a new faith.  
- Your liege now gets "opinion of predecessor" towards your heir when you die, if they end up your heir's liege and your heir had no liege or a different liege  
- wandering characters with absurd amounts of gold will now tend to spend it all on improving themselves (no more inviting wanderers with 7000 gold and banishing them!)  
- Added more restrictions to the check for if characters are willing to cheat on their partners  
- Alan culture now starts with Compound Bows researched in 867 as well as 1066.  
- Germania can no longer be created by spiritually-headed Christians, who must create the HRE instead.  
- Increased the Level of Splendor gain from the "Dynasty of Many Crowns" decision from 75 to 1000  
- Increased the area for Stammesherzogtum to include parts of Bavaria and northern Germany, so all German cultures are able to gain the innovation.  
- Increased the base fortifications slightly for castle holding upgrades.  
- Indimitated vassals are now slightly-less-deterred from joining factions  
- Jarl Haestinn now starts at Fame Level 5 instead of 6  
- Made the 'Religious Construction' county modifier focus more on bonuses for temple holdings specifically instead of development in general.  
- Nerfed the 'Supplies' siege event to grant a total of 20% Siege progress, down from 40%.  
- Peasant Leaders now get a discount on raised levy maintenance, making popular revolts less likely to succumb to crippling debt  
- Peasant and Populist Faction Leaders now gain gold contributions from faction members when war is declared, so that they can pay army maintenance. The gold is removed once the war has ended.  
- Reduced the chance of children reincarnating with an ancestor's sinful personality traits  
- Removed claimants with pressed claims from the pool of potential court physicians  
- Removed extra 6th holy site of Alexandria from Waaqism  
- Removed extra 6th holy sites of Wadan and Kisi from the Siguic and Bidaic faiths, respectively  
- Restricted the Intrigue(Scheming) event "Confused Heritage" to players only, as the AI was going a bit wild with it and turning everyone into bastards unnecessarily  
- The AI is now less likely to want to spend gold on Guests during war, and when their coffers are running low  
- The AI should now be more inclined to build Castle holding upgrades  
- The regional innovation Stammesherzogtum now also reduces the likelihood that vassals will join Independence Factions  
- There is now a 5-10 year grace period on game start before Populist Factions will form  
- Vassals are now increasingly likely to join factions the more in debt their liege is  
- Zbrojnosh Men-At-Arms now counter Pikemen in addition to Archers.  
- restoring the HRE is now easier & more rewarding, whilst still requiring a decent amount of prestige, realm size, & controlled kingdoms.  
- Independence faction now has domains of all faction members as war goal  
- When you successfully ask a vassal to end an offensive war, the defender now gets a small opinion bonus towards you.  
- The maximum penalty for being over your domain limit is now -100% taxes/levies, increased from -90%.  
- If you vastly exceed your Domain Limit for more than one year (the grace period for new inheritances/conquests), all buildings will deactivate until your domain limit is lowered.  

###################  
# AI  
###################  
- Discouraged the AI from doing naval invasions when land invasions are feasible  
- Gave the AI dancing lessons  
- Gave the AI some self-confidence lessons. Just because its liege is a complete coward, that doesn't mean it should avoid making or joining factions. It should only do so if they themselves are cowed  
- Increased the AI willingness to spend on Duchy Capital buildings  
- Informed the AI of the existence of the player when it is trying to spread out to avoid attrition  
- Informed the AI that if it has nothing else to do in a war, it might as well defend the wargoal  
- Russian Vikings are now much more unlikely to conquer overseas  
- Should now be better at merging small army stacks  
- Sternly told the AI that when it's trying to support the player, it shouldn't try to retreat just because the enemy is coming right at it (except if it hasn't yet arrived at the player's location)  
- Taught the AI how to count. It will now when deciding whether to raise its troops consider all its troops, not just its levies. So it won't refrain from raising its troops just because its levies alone would be pointless to raise  
- Taught the AI to be a bit better at avoiding pushing 3rd party claims that'll lead to the claimant going independent. It's still happy to push such claims for close family members  
- The AI is more likely to acquiesce to a faction demand when they're deep in debt  
- The AI is no longer more eager to join a claimant faction if the claimant is close to death, but instead less likely  
- The AI is now more likely to create holy orders, but gets less likely to do so the more holy orders a faith has  
- The AI no longer minds matrilineal marriages for men and patrilineal marriages for women in most cases when those marriages are within the same dynasty  
- The AI now wants to recruit guests that they have a positive relation with, for example Friends or Lovers  
- The AI should no longer attempt to call the player in against their own heir or spouse (they wouldn't accept, so they should presume the player wouldn't either)  
- The AI should no longer bother the player with offensive call-to-arms if they're the primary defender in a war.  
- The AI will now properly revoke Holy Order leases if they're of another faith  
- The AI will now use Ask to Take the Vows under certain circumstances.  
- The AI will now wait longer to send a new ransom request to the player after they previously denied one.  
- The distance the AI is willing to raid is now based on its tier  
- Told the AI it might as well support the player if there's no enemies around as long as there's enemies *somewhere*, rather than running off on its own to go siege something  
- Told the AI that considering the threat of enemies when you're at sea makes some sense even if they can't get to you while you remain at sea  
- Told the AI that counting the player's enemies twice if they're movement locked and trying to decide if the player needs help or not might lead to some silly decisions  
- Told the AI that hunting down enemy armies in enemy territory is a good idea if it is safe to do so, even if it is currently in a defensive mode  
- Told the AI that it is a good idea to raise more troops when it already has troops raised  
- Told the AI that it might actually be a good idea to try to avoid running into enemy units while raiding  
- Told the AI that it really doesn't make any sense to try to retreat from a dangerous enemy while at sea  
- Told the AI that it shouldn't bother sending support to the player while the player is just moving around at sea. Only once the player is standing still or making landfall does support make much sense  
- Told the AI that it's fine to hunt down enemy armies that aren't in either the attacker or defender's territory  
- Told the AI that just because it thinks a battle's about equal, that doesn't mean it should refrain from piling more troops into it to be 100% sure  
- Told the AI that maybe it shouldn't pretend it can't see your units when it actually can due to you being in or on the border of its liege's territory  
- Told the AI that when deciding where to raid, it might make sense to measure the distance by sea, not as the crow flies  
- Told the AI that when it has decided to either retreat or stand on fight, there's no point doing other things like hunting nearby enemy units, or trying to merge with a friendly stack  
- Told the AI that when supporting the player while the player is at sea, it makes sense for it to go to the same province, rather than stay on land  
- Told the AI to not bother pushing the claims of vassals of vassals. Its own, its direct vassals, and its courtiers should be plenty  
- Vikings should now mostly prefer to conquer contiguous areas overseas (their vassals can still go their own way though)  
- When granting titles, the AI now has a small preference for giving away titles it more recently acquired, instead keeping its older titles  

###################  
# Interface  
###################  
- Add a situation warning you of when a vassal may leave your realm due to inheriting a foreign title.  
- Add character list filters for: not my faith, not my religion, not my culture, not my culture group, has no claims, has claims on me, and not player dynasty.  
- Add developer easter egg character portraits to the credits view  
- Added a Current Situation item for Vassals that could be granted to their Rightful Liege  
- Added a descriptive text in the Dynasty View that tells how you pan it  
- Added a game concept for Gifts  
- Added a warning/suggestion in the current situation list for when having too few wives  
- Added an alert for when your primary heir is of another dynasty and you don't have any members of yours in the (current) succession line  
- Added game concept for the Unreformed Pagan Combat Bonus, making it clear that it only applies in counties of one's own faith  
- Added missing "+" sign in tooltips about "X's opinion of you: 50"  
- Added shortcut listings for the encyclopedia and character finder  
- Added war start date to war tooltip  
- Added warnings to the take vows interactions about kicking out potentially useful people  
- Allow left mouse drag in dynasty tree  
- Changed the name of the vassal contract modification confirmation interaction from "modify" to "modify vassal contract"  
- Clicking a region in a cultural innovation tooltip now highlights it on the map  
- Clicking on the checkbox or label will now also register the allow marriage button  
- Contribution scores are no longer shown for GHW participants who can't have them.  
- Crown authority tooltip only shows cost of locked levels  
- Deceased rulers no longer shown an heir in the character window  
- Directed GHWs now have a more accurate victory message  
- Disallow wasting a hook use on a feudal contract negotiation if its already fair or in favor of the vassal.  
- Display text in the realm view when the player has no vassals  
- Don't show rally map icons on water, they are never valid there.  
- Faith doctrine names should now be tooltippable in far more cases  
- Fix borders not always being cleared when they could be.  
- Fix the rally point icon when placing or moving rally points from blocking the click to actually move them if not hitting the map.  
- Fix weak hooks suggesting you can force someone into a faction when the interaction requires a strong one.  
- Fixed "Opinion of Liege" in character list entries not providing a breakdown when tooltipped  
- Fixed "kinswoman" and "kinsman" in some cases being swapped  
- Fixed Call to War and Offer to Join War interfaces in some cases selecting wars that cannot be selected. Now only auto-selects if there's only one war and it can be selected  
- Fixed a handful of cases where localization would treat other players in MP as if they are you  
- Fixed a misplaced space in the scheme success chance breakdown  
- Fixed a number of cases where coats of arms could end up blank  
- Fixed a superfluous Education Trait entry in the Encyclopedia  
- Fixed a variety of interface functionality treating sessions where people can hotjoin but there's just one player, as if they're an actual multiplayer session. Could cause things like the "Player" mapmode to appear  
- Fixed baronies showing up in the Ask For Claim interaction  
- Fixed broken tooltips in the battle events list in the battle summary  
- Fixed dead Popes being called king-bishops  
- Fixed deleting a rally point not fully deselecting it, leading to clicking another rally point in the military view in some cases simply panning to that rally point without opening the rally point window  
- Fixed directed GHWs (e.g. Jihads) showing incorrect war chest shares and scores for the person winning  
- Fixed directed GHWs showing warscore share rather than rank  
- Fixed doctrine tooltips in the faith view linking the doctrine itself, leading to pointless recursion  
- Fixed dynasty modifier icons sticking around in the dynasty window after the modifier has been removed  
- Fixed education focus icons in their tooltip lighting up on hover as if they were buttons  
- Fixed faith doctrines in the encyclopedia and similar on the main menu sometimes saying "All <blank>:" rather than "All Adherents:"  
- Fixed faith hostility descriptions "Evil" and "Hostile" not being tooltippable in some places  
- Fixed it not being possible to filter by traits in the spouse interface that aren't shown (E.G., filtering by a specific education)  
- Fixed links being unclickable in some tooltips  
- Fixed links in the console output being unclickable  
- Fixed mercenary troops not getting accounted for in a number of military strength breakdowns  
- Fixed missing culture names in Guardian/Ward interactions  
- Fixed pushing the claim of a courtier saying they "stay" your vassal rather than "become" your vassal  
- Fixed regnal numbering failing in some cases when names contain non-ASCII characters  
- Fixed some of the things that can block changing a focus not showing up in red with a warning symbol  
- Fixed succession UI saying "From Realm's <blank>" rather than "From Realm's Partition Succession"  
- Fixed the "<child> has no reason to stay at court" message claiming the child is your stepbrother or sister rather than child  
- Fixed the "Realm will lose land when Vassal dies" alert showing up in some cases where the land won't actually leave the realm since the heir will become your vassal  
- Fixed the "powerful vassal" text in the vassals list not having a tooltip  
- Fixed the Allow Marriage checkbox  
- Fixed the Claimants list for titles in some cases including people who don't actually have a claim on the title  
- Fixed the Expose Secret interaction showing the effects of the Blackmail interaction  
- Fixed the Find Concubine window in some cases showing someone who is already your concubine  
- Fixed the Select Beneficiary having a game concept on the send interaction button, making it hard to click. Fixed the effects description *not* having a game concept for "Beneficiary"  
- Fixed the achievements box in the Game Rules window only having a tooltip on the "Achievements (Not) Available" text rather than the whole area  
- Fixed the center of the Resign from Council button not being clickable  
- Fixed the character portrait in the Load Game window highlighting when you put your mouse over it, as if it were a button  
- Fixed the character window strength breakdown listing "Attacker's/Defenders' Allies' Military Strength" rather than simply "Allies' Military Strength"  
- Fixed the combat predictor in some cases ignoring some of your armies, thus predicting far worse odds than reality  
- Fixed the declare war tooltip in the war declaration screen telling you about things blocking the war declaration twice  
- Fixed the election candidate view showing the health icon twice on candidates  
- Fixed the game pretending you could swap councillors (and then doing nothing when you clicked the button) in cases where the current councillor isn't eligible for the other's council position. Now it'll say Reassign instead, and lead to the current councillor being fired  
- Fixed the game sometimes claiming a marriage has no chance of children despite both parties being fertile  
- Fixed the game sometimes saying that the development progress will "change by x" when it'll actually "decrease by x"  
- Fixed the hotkeys for the mapmodes hidden under "additional mapmodes" not working in the lobby  
- Fixed the math sometimes overflowing for combat predictions for large battles, leading to it just saying the odds are even despite them being anything but  
- Fixed the prestige icon in the Arrange Marriage view causing the prestige tooltip rather than the prestige gain breakdown tooltip  
- Fixed the progress bar under "total soldiers" in the military view not having a tooltip; now gives the same tooltip as the label above it  
- Fixed the rally point progress bar occasionally going offscreen  
- Fixed the realm name of dead rulers being misplaced  
- Fixed the religion filters and similar for character lists not always working. Was for instance broken in the election window  
- Fixed the tooltip for the achievements icon in character selection covering the ironman checkbox  
- Fixed the unit banner for stationary units turning invisible when you have the war overview window open  
- Fixed the victory screen of Directed GHWs saying you didn't participate enough rather than showing your participation rank  
- Fixed titles sometimes showing up twice in the title finder  
- Fixed traits with gendered names such as "Pretty" having their names based on the target rather than schemer in romance schemes  
- Fixed troop counts being massively wrong until you unpause. Now they'll only be a little bit off (since a lot of things can change on the first day)  
- Fixed unpause tooltip in single-player sometimes saying "Game is Paused by UNKNOWN"  
- Fixed word salad in the Level of Splendor toasts  
- Fixed you in some cases getting a "your child can marry" notification for someone you have no power to marry off  
- Fixed your heir display taking a day to update after your heir dies. Now instant for player heirs  
- Got rid of strange glow on the "no character selected" portrait when creating a claimant faction  
- Hovering over options in the dropdowns in the Barber Shop will now show the resulting change on your character model. No more having to click through the options one by one  
- Improved consistency between Call to War and Offer to Join War interfaces  
- Improved the look of faction entries when the faction is at war to push its demands  
- Improved tooltip placement in the title window for the titles in the "De Jure Part of" list and the De Jure Hierarchy list in the holding view  
- In the character view, hovering over the military strength of the character will now list knights with their cultural name rather than yours  
- Invalid savegames can be toggled on or off when the save window is up  
- Knights no longer have such a disproportionate effect on army quality levels. This has no impact on gameplay; just makes the quality level more representative of the actual effectiveness of the army  
- Level of Splendor triggers now correctly show their name rather than just a number  
- Made it clear in the Knight game concept that Knights represent both the character *and* their retinue of troops; a Knight isn't single-handedly causing 30 casualties  
- Make sure absolute control is displayed correctly in the domain tab  
- Make sure the friends panel can be expanded if at 8 or more  
- Make sure the page number and close button are not drawn over each other in tutorial windows  
- Make sure the right mouse button is registered when clicked to pan to the army from the outliner  
- Make sure the views on a faith are not shown when the player hasn't selected a character yet  
- Make sure to switch between click to show/hide on the tooltip for notifications  
- Minor GHW layout improvement  
- Only show the click to unlock text in lifestyle perks if it's available  
- Only show the continue button if the credits list is still scrolling  
- Only show the map icon and progress bar for tasks that have a councillor appointed to it  
- Only show the select button in the MP lobby if the game has not been started yet  
- Opening a dynasty tree now pans to you (if you're in it). Otherwise it pans to the dynast, or the founder if it is a dead dynasty  
- Outdated information should no longer stick around in the character window  
- Peasant and Populist revolts will no longer get dynasty-based names for governments that use such names  
- Potential scheme agents with positive acceptance score are now listed as "Will join" rather than "Can be convinced"  
- Remove double toast when a dynasty member makes a cadet house.  
- Remove starting fervor info from the faith creation screen, it does not vary so it is unnecessary information.  
- Remove the description for secondary characters on the bookmarks screen  
- Removed dagger icon next to scheme start effects to make the less awkward when used with personal schemes  
- Scheme Agent acceptance tooltip now shows the full breakdown directly in the list.  
- Select the correct text flavorization when a title can't be granted  
- Shift+F11 will now generate a picture of your current map mode and put it in your screenshots folder  
- Show a message in the window when you have no vassals and are about to convert to a new faith  
- Sort by name for Knights in the battle result window now uses first names instead of titled names.  
- Stopped showing the opinion of players of the faction target when creating a claimant faction  
- Successful conversion is now sent as a message rather than a toast  
- The "Allow Marriage" button in the interaction list now looks far less out of place, and the full button is tooltippable  
- The "Pending Crusade Participation" alert now only shows up if the head of faith would actually be upset at you for not participating  
- The "will not accept" icon and tooltip now only shows up on interactions where there's no combination of options that'll lead to the recipient accepting. No more "will not accept" on ransom when they'll gladly accept as long as you're willing to pay  
- The 'Alliance Expired' message now shows clickable links for the character names.  
- The AI trying to ransom itself from your prison will no longer be called "Ransom Yourself"  
- The Appoint a Councillor window now no longer appears under other windows until clicked  
- The Great Holy War interface now tells you how much of the war chest you'll get when the war begins  
- The Hajjaj version of the Pilgrim trait now has unique art  
- The Muslim caliphates are now named "Sunni Caliphate" and such, rather than "Abbasid"  
- The Romance interaction now uses the correct notification header  
- The Success Chance and Secrecy modifiers are now not shown for Discovered schemes, to prevent being able to deduce who's scheming against you (only total chance is shown)  
- The army tooltip now shows commander advantage rather than martial  
- The automatic pausing from having died no longer gets unpaused when you dismiss the succession screen; you now have to manually unpause instead  
- The battle predictor is no longer as pessimistic about your odds. Now a predicted 50% edge is enough to get "you'll probably win", while before you needed a 133% edge. The other categories have had their thresholds tweaked as well  
- The breach siege event pictures now have the correct aspect ratio and properly updates to show the different breach levels.  
- The character relation description will now include spouses and concubines of landed rulers.  
- The concubine and blackmail interactions now show all their effects  
- The faction interface now clearly shows who has been blocked temporarily from joining a faction, and until when  
- The game will no longer claim that your guest's claim on a title that's already in your realm, or which has no holder, is useful  
- The house & dynasty view now looks nicer for houses and dynasties with no living members  
- The lost titles section in the ruler transition window is no longer shown where there's no lost titles and is expanded by default.  
- The on-map council task icons are now always shown when you have the council window open  
- The raid loot info now shows up in province tooltips when you have a raid selected rather than a raid army  
- Tracked decisions now show as alerts instead of in the suggestion dropdown  
- Unit movement arrows are more visible when moving through heavily-forested provinces  
- When a war goal has multiple options (E.G., claim wars, holy wars), those are now sorted by tier then roughly by distance from your realm, rather than in arbitrary order  
- When looking at the list of knights and potential knights, potential knights only have their portrait darkened rather than their entire entry, so it no longer looks as if buttons like "Recruit to Court" are grayed out  
- When revoking a title, the new domain size is shown correctly now  
- When viewing a battle you're not involved in, it'll no longer say it's "your" commander and "your" realm  
- You can now hover over innovations in modifier breakdowns (E.G., "Manoralism" in the building cost breakdown) to see the full info on the innovation  
- You can now queue movement waypoints for gathering armies using shift, rather than being limited to just the shortest available path  
- You no longer get the Dangerous Faction alert for a faction that's at war with you. The ongoing war is presumably enough of a tell  
- You now get a notification in the lower-right corner when a part of your realm gets sieged by someone you're hostile to  
- Improved Bookmarks screen scaling on different aspect ratios  
- Fixed missing description in Secret Exposed notification  
- Don't show the cost of removing a title law if there is no cost.  
- New Stress indicator look and placement  
- Fixed various text overflow issues with localized text  
- Added visible "close" button to Toasts  
- More info for pinned characters in Outliner  
- Fixed an issue where Sinful and Virtuous traits were not highlighted in the Character Window  
- Clearer state of army in Army View  
- More feedback on pause/unpause  

###################  
# Art  
###################  
- Added ethnicities for East African, South Indian and Slavic, and Arctic/Circumpolar  
- Added lighting for Corridor Night event background.  
- Fixed a CoA that was showing debug pink  
- Large map names look better, at a small cost to tiny map names.  
- Tweak to Knights Templar coat of arms  
- Updated some character portraits in the credits list  
- Fixed a large amount of portrait clipping issues between clothing, headgear and hair.  
- Lowered some headgears to better rest on a character heads rather than floating.  
- Improved teenager animations to not be neutral but also show more personality like adults.  
- Adjusted animations to cause less intersections.  
- Increased map readability by changing the colour slightly for titles that had similar, or the same, colour.  
- Visual Map improvements in the African region.  
- Fixed a number of lakes floating around.  
- Added FXAA as an anti aliasing option  
- Improved visuals of Bookmarks screen (New Game) and Main Menu  
- Fixed some errors on the Bookmarks map  
- Frontend menus have been tidied up  
- New Siege Window layout and art  
- Improved HUD visuals  
- Color coded Education Trait Icons  
- Increased contrast of character portraits  
- Cleaned up file structure  
- War Overview now looks cooler  
- Culture Window looks cooler too  
- Great Holy War is actually great  
- Culture icons are now unified to always display as a candle  
- Added Easter Egg DNA for Henrik Fåhreaus, Debbie Lane, Hanna Löhman, Maximilian Olbers, Bianca Savazzi  

###################  
# Localization  
###################  
- A more flavourful description added for when murder by hunting "accident"  
- Added Vote Strength to game concepts  
- Added a first person present tense text for the "join faction" effect  
- Added an alternative text for holy war if one has the pluralist doctrine  
- Added clarification on the modifier text for the Condottieri innovation  
- Added description for Parliament Special Building  
- Added dynasty names  
- Added localization for Yazidi bishops and theocracies  
- Added missing character name to bastardry reveal event  
- Added missing whitespace in Fabricate Hook event titles  
- Added some missing perspectives for effects  
- Added some uppercase loc commands for cases where a 'you' is displayed instead of a name  
- Added text for the first-person version of losing one's guardian  
- Added the alternate localization 'Ritual Suicide' for non-Christian Faiths with the 'Consolamentum' tenet  
- Children who reincarnate as an ancestor with sinful traits now acknowledge that isn't actually a good thing  
- Clarified some of the information in the reactive advice about education  
- Clarified the effect of the perks 'Sound Foundations' and 'Friendly Counsel'  
- Clarified the effects of the "Found new Kingdom/Empire" decisions  
- Correct loc command for seduction tooltip if you're already friends  
- Corrected a few befriend events that did not start with an uppercase letter  
- Dynasty prefixes in effects and decisions are now more consistent  
- Fixed a broken game concept in the Pluralist doctrine tooltip in German  
- Fixed a bunch of grammar and typos  
- Fixed a capitalization error in one of the female south slavic names  
- Fixed a number of typos and grammar issues  
- Fixed a recursive 'MAX_RECURSION_DEPTH' recursion bug in the event No Time For Myself  
- Fixed a scope mis-match in the lover reveal event which caused the event to describe people having affairs with themselves  
- Fixed an error that caused rulers to use their own name instead of the name of the potential spouse on some marriage acceptance breakdowns  
- Fixed an error that caused the Consecrate Bloodline decision to refer to "The Papacy Himself"  
- Fixed error that would occasionally cause titles to be presented as " 's Primary Title"  
- Fixed grammatical error in Great Holy War victory desc  
- Fixed several minor grammatical errors.  
- Fixed the missing text for polyamory tenet compatibility  
- Fixed the tooltip for the war chest distribution  
- Fixed typo in "Shunned" game concept text  
- Improved the text of the 'Secret Revealed!' event for lovers  
- Learning requirement for temporal condemnation is now shown as an int  
- Re-named the 'West African' culture group to 'Guinean'  
- Reduced the fowl feast event texts so no scroll is required in the English version  
- Removed the tooltip link in GHW dynamic titles  
- Removed unused strings from hastings bookmark  
- Renamed the 'Initiate Consolamentum' decision to 'Initiate Endura' to be more correct  
- Renamed the Temporal Condemnation interaction to Condemn Sins so it's a verb like other interactions  
- Renamed the Wendish Empire to the Southern Baltic Empire  
- The greeting in the secret documents letter is now more mysterious  
- The tooltip for candidates in an elective succession now correctly displays the name of the candidate instead of the person who nominated them  
- Updated Tutorial text  
- Updated loc for using a strong hook on someone  
- Updated the building localization so that the text colours are consistent among all building entries in the encyclopedia  
- Updated the confirmation button name for the "Dynasty of Many Crowns" decision  
- Updated the cultural titles for Iranian culture-group rulers, including unique titles for Muslim and non-Muslim rulers  
- Updated the description for bastard secrets to fix possible grammatical issues for certain scopes  
- Updated the description for bastard secrets to fix possible grammatical issues for certain scopes "  
- Updated the error messages for incompatible tenets when creating a new faith  
- Updated the event text for "Earned Responsibility" to accurately use the player character's gender  
- Updated the event text for "Twist of Fate" for when your dead heir was already an equal or higher tier ruler than your current character  
- Updated the explanation for Fervor's impact on Popular Opinion  
- Updated the name of Tengriism's religious group from 'Shamanic' to 'Steppe' to be more consistent with the naming scheme of other religions  
- Updated the name of the 'Crusader King' trait for Muslims  
- Updated the names for 'c_hordalandi' and 'b_sunnhordalandi'  
- Updated the tooltip for Divine Marriage to clarify how it works  
- Updated the tooltip for when powerful vassals block a succession law change  
- Various typos and grammar issues fixed  
- Various typos fixed in traits and interactions  
- Added localization to some triggers that were missing it  

###################  
# Game Content  
###################  
- Add define for the desired number of spouses in polygamous faiths - allows to specify the value per primary title tier level  
- Added a new "Ayyar" cultural Men-at-Arms for Iranian cultures  
- Added a new Suggestion to recruit men-at-arms when a player has fewer regiments than expected for their rank  
- Added a notification toast when your liege changes to inform you who your new liege is and why they became your new liege.  
- Added animations, AI balancing, localization, and other small things to martial events  
- Added more mythological names for warhorses and added animations to events  
- Removed traits that were unused  
- Reviving Taltosism now allows you to choose between vanilla Taltosism & swapping out one tenet for a scripted alternative whilst promulgating the restoration.  
- Reviving Taltosism will now convert Magyar Group counties more generously, especially in Mogyer areas with less German influence.  
- Updated the 'Establish Batrican Supremacy' to have more accurate and easier to understand requirements  
- Updated the martial lifestyle event "Under Siege"  
- added "the Apostate" nickname when reviving Taltosism.  
- made Reviving Taltosism more visible, flexible, & meaningfully challenging.  

###################  
# User Modding  
###################  
- "image = blah" now works in combat effects  
- Add can_declare_war trigger to see if a character can attack another character for a set of titles using a CB with an optional claimant.  
- Add console command to dump out landed title hierarchy from barons up their de jure liege's.  
- Add current_day trigger  
- Add current_month trigger  
- Add holder_ignore_head_of_faith_requirement which will suppress the head of faith warnings in history when giving someone a title, useful to represent a historical person holding a head of faith title due to conversion or other representation but not affecting actual gameplay.  
- Add player_heir order of succession type, it will always grab the player heir of the person evaluating the succession.  
- Add set_mother effect to change the mother of a character.  
- Added FaithDoctrine.GetNameNoTooltip; GetName now is tooltippable  
- Added add_piety_no_experience and add_prestige_no_experience effects to add/lose to them whilst not changing the persistent experience gain.  
- Added console command print_naval_distance, to find the naval distance between two provinces  
- Added console commands pause_on, save_on, and pause_and_save_on. These force the game to pause and/or save at a specific date, or when a specific event triggers (for any character in the game)  
- Added define AI_USE_VASSAL_OF_VASSAL_CLAIMS  
- Added define DEBT_MODIFIER_THRESHOLDS. Debt now gives a character modifier based on this, as well as a combat modifier  
- Added define MARRIAGE_OWNER_IS_MATCHMAKER that lets the AI logic for marrying skip the interaction redirect logic when figuring out who it can marry off. As long as that matches the actual redirect logic for the actor, the result is the same but faster  
- Added define MAX_HEIRS_IN_LINE_OF_SUCCESSION_TOOLTIP  
- Added define MAX_MONTHLY_PRESTIGE_GAIN_FROM_ALIVE_MEMBERS  
- Added define MAX_QUALITY_POWER_MULT  
- Added effect generate_building  
- Added effect set_can_be_named_after_dynasty = no to suppress such naming for titles. You can also put can_be_named_after_dynasty = no in the title definition for historical titles  
- Added global data system promote GetGeographicalRegion. E.G., GetGeographicalRegion( 'world_europe_west_iberia' ).GetName  
- Added graphics defines PRESTIGE_LEVEL_PATH, DYNASTY_PRESTIGE_LEVEL_PATH, and PIETY_LEVEL_PATH  
- Added link "activity" for getting the activity a character is participating in  
- Added link "house_founder". Added link "last_house_head"; same as "house_head" if there is one, but if the house is dead it'll give you the last person to be head of it  
- Added on-action on_concubinage_end  
- Added on_vassal_gained on-action  
- Added tab-complete for virtually every console command where that makes sense (E.G., add_trait, show_title, change_culture)  
- Added title transfer type swear_fealty  
- Added trait flag blocks_from_claim_inheritance = yes and blocks_from_claim_inheritance_from_dynasty. Being unable to inherit titles no longer blocks claim inheritance  
- Added trigger debt_level  
- Added trigger has_relation_to, matching the data function HasRelationTo  
- Added triggers ai_reserved_gold and ai_war_chest  
- Allow title laws to define if they are shown in the title law UI or not.  
- Allow title laws to define when they can be removed or not.  
- Disabled the use of the "inheritance" and "abdication" title transfer reasons, as using them could break a variety of things  
- Dynamic descriptions now log when they make use of loc that does not exist  
- Eliminated "break" effect  
- Enable the AI to use scripted guis based on the ai_is_valid and ai_chance in definitions. By default a scripted gui will not be used.  
- Fix copying coat of arms only working across the same scope types. Can now correctly copy from a title to a title, a title to a dynasty, etc.  
- Fix set_title_name and reset_title_name not updating the name on the map instantly.  
- Fix some in game coat of arms not refreshing the shown texture when given a new coat of arms by effect.  
- Fixed adding an is_shown to a council task not actually hiding it in the council window when not fulfilled  
- Fixed grant_titles_interaction's effects being applied after the titles are given out, rather than before  
- Fixed the game crashing or presenting other issues if you tried to create a title with no tier, barony tier, or county tier. This creation will now get outright blocked  
- Fixed the vassal_count trigger having the behavior of the domain_size trigger rather than actually checking the vassal count  
- Fixed title_will_leave_sub_realm_on_succession not properly accounting for heirs changing liege due to inheriting a higher tier title  
- Gaining a title you have an explicit claim on no longer causes the on_explicit_claim_lost on-action  
- Important actions now support "icon = blah"  
- Improved performance of *_character_to_title_neighboring_*, *_character_to_title_neighboring_and_across_water_county_*, *_neighboring_realm_same_rank_owner, and *_neighboring_and_across_water_realm_same_rank_owner  
- Remove court physician as being a required cached scripted relation.  
- Remove friend and lover as being required cached scripted relations.  
- Removed set_title_and_vassal_change_type and set_add_claim_on_loss, integrating them into create_title_and_vassal_change instead. This lets us ensure that all title and vassal changes are properly set up, and log errors at read-time if you forget to set the transfer type  
- Removed unused desc system from doctrine groups  
- Scripted Guis used by the AI can have an ai_frequency in months defined for how often they will be evaluated like character interactions.  
- The "character:history_id" link now no longer logs an error on runtime if the character doesn't exist (when used in a event target comparison); it will instead error during load time if referencing someone who isn't in the history database at all  
- The AI values tooltip in debug mode now shows which rough budget categories the AI has put its money into  
- The ai_will_do of call_ally_interaction is now respected by the AI  
- The on-actions in title_on_actions.txt (except on_title_destroyed) now provide scope:transfer_type so you can determine how the title/vassal change happened  
- To make the above optimization possible, none of them work with barons or baronies any more  
- You can now use "==" in place_in_line_of_succession for when you really do want to check equality (since "=" will throw an error since usually it makes little sense )  
- do_ghw_title_handout now also handles dejure vassalization  
- x_traveling_family_member now includes adult children too  
- The trigger_event effect now supports delayed = yes/no  
- Updated the info doc for character interactions  
- The AI desire for matrilineal marriages is now scriptable through the ai_wants_matrilineal_marriage scripted rule  
- Added trigger domain_size_excluding_grace_period  
- Map Editor - Map Object Editor - UX improvements (grouped by layer, more compact)  
- Map Editor - Map Object Editor - can create/edit/delete map objects types in editor  
- Map Editor - Export & Import tool added for merging map changes by area  
- Map Editor - Starts up faster  
- Map Editor - Claims less memory  
- Map Editor - Cursor change while editor is saving  
- Map Editor - Height map can be reloaded while in editor  




###################  
# Databases  
###################  
- Added Saka culture to the Tarim Basin.  
- Added additional rulers in Sapmi for both bookmarks. Both to add more variety with independent tribes, as well as splitting up the large realm of the Finnish ruler in Oulu.  
- Added the Guiyi Circuit as an independent realm in 867 to better represent the history of the area in and surrounding Xia.  
- Afar and Somali cultures now start the game with their Men-at-Arms innovation unlocked.  
- Aquitaine now has Salic law (male only title-specific succession) in 867.  
- Changed Andrew the Apostle's culture from Scots to Greek  
- Changed a few Prussian dynasty names to sound less German.  
- Changed a few additional counties in eastern Cumania to be of Kipchak culture.  
- Changed the names for a couple of duchies in eastern Germany. Ostmark is now named Nordmark, while previous Nordmark is named Mecklenburg (the Billung Mark).  
- Connected the Benin dynasty to its founder, to avoid a disconnected dynasty tree.  
- Ekundayo of the Benin dynasty no longer lives to be more than 200 years old (causing her to still be alive in 1066!). She now passes away at a more reasonable age.  
- Fixed the count of Grisons accidentally being independent in 867.  
- Fixed two Dukes of Poland being presented as full Kings between 1031 and 1058  
- House of Wittelsbach is now playable in 1066. Otto I (count of Scheyern) has been granted the county of Rothenburg, which encompases the area of Scheyern Castle.  
- Improved the historical setup for Mosul in 867.  
- Improvements to Cumania in 1066. A couple of fictional vassals was added to reduce the Khan's domain size and avoid vassals with a disjointed realm.  
- Kashmiri culture no longer starts with Elephantry unlocked, since they are mostly situated outside the sub-continent of India.  
- Kirati culture now start the game with the Elephantry innovation unlocked.  
- Luticia is now independent in 1066, to represent the Slavic uprising.  
- Made several changes to the De Jure setup in Sub-Saharan Africa.  
- Made several government updates to the Russian principalities and their vassals. They are now consistently feudal, with occasional tribal vassals to represent recent (or semirecent) conquests.  
- Made sure that Khazar still has counties of their culture in 1066 within the kingdom of Caucasus.  
- Made the island of Socotra de jure to the duchy of Socotra.  
- Members of the Contarini dynasty are now Cisalpine.  
- Ostyak and Permian cultures now have their Men-at-Arms innovation Forest Warden unlocked in 1066  
- Prince Ibrahim Aghlabid of the Sultanate of Africa is now a vassal under his father.  
- Rhodri the Great's dad, Merfyn, is now suitably oppressive.  
- Ruler of Naissus is no longer tribal in 1066.  
- Saint Peter now keeps the name "Petrus" upon becoming the first Pope instead of getting a random papal name.  
- Sami culture now starts with their cultural Men-at-Arms unlocked in 867, and two additional innovations in 1066.  
- Tangut characters Xingge Pochou and Fuyun Ezangquhuai are no longer both married and betrothed.  
- The dynamically-named Child of Concubine/Consort trait has been split into separate "Child of Concubine" and "Child of Consort" traits  
- The ruler of Magdeburg is now a Theocracy in 1066.  
- Updated and fixed several holding types within Tibet.  
- Updated and fixed the names of Popes Eugenius II and III.  
- Updated and improved the Polabian setup, mainly in 867, and added a number of Polabian names for the area to have less German names under Polabian rule.  
- Updated history for Rethel and it's historical rulers.  
- Updated the culture setup in the Steppes slightly.  
- Updated the history and setup for the Karakhanids.  
- Various improvements and changes have been made to the history of the western half of Byzantium in 1066, to more accurately represent the themes used at the time.  
- Volga Bulgaria is now feudal in 1066, to represent the fact that they were more sedentary than not. Especially when compared to their nomadic neighbors.  
- corrected the date of birth of Alfred's youngest daughter so that she is no longer his eldest.  
- gave the House of Wessex a fixed motto.  
- slightly adjusted Insularist setup in 867 Scotland  
- Updated the kingdom of Sao's coat of arms.  
- Corrected the Saffarid-Tahirid war to make the Saffarid the attacker, rather than defender. If the Saffarid successfully win the war, they will gain the duchies of Herat and Nishapur.  
- Daju culture no longer has the Early Medieval era unlocked in 1066.  
- Split up the much too big viking count north of Sweden in 1066 into smaller realms  
- Updated a number of holdings in Bohemia, 867, to have the holding type match the ruler's government.  
- Updated several holdings in east Africa to be tribal if held by tribal rulers at game start.  
- The province of Zeeland now begins under the control of the HRE in 1066  

###################  
# Bugfixes  
###################  
- AI will ignore unit targets in attrition areas  
- Cancelling construction that costs prestige or piety no longer gives you Fame or Devotion; just the prestige/piety cost back  
- Don't count the court physician in the relationship tab as a relation.  
- Fix not being able to reform your faith with the same doctrines, entirely different doctrines is only required if creating a new faith instead of reforming one.  
- Fix temporal head of faith titles not following the player heir if the realm heir differs from the player heir from an elective primary title.  
- Fix the mass ransom button being usable when the person we ransom to cannot pay the gold.  
- Fix the player heir not always being the passed on house head if the player heir and realm heir differed due to a primary title being elective.  
- Fix the prisoner action buttons not always matching up to if the interaction could be done.  
- Fixed the special contracts, march etc, having the incorrect name until you had the right innovations for them.  
- Fix unnecessarily handling controller input and rotating/zooming the camera. This will avoid some issues with black maps after loading into the game, if a connected controller constantly sent unexpected inputs.  
- Fix war participant tooltip not listing the number of knights but just repeating the word knight.  
- Fixed Divorce not being available if your faith requires divorce approval by the spiritual head of faith, but you don't have a spiritual head of faith (no head, or temporal head)  
- Fixed GHWs in some cases resulting in the Crusader King unlanding another beneficiary to get the capital, rather than just directly getting the capital in the first place  
- Fixed an issue where a modifier for elector voting would not print text properly  
- Fixed characters of the non-dominant gender of a faith getting claims on their dying parent's titles. E.G., now men won't get such claims in a Female Dominated faith  
- Fixed characters who change liege not always getting properly updated. This could for instance lead to their liege's vassal limit usage not updating  
- Fixed excommunication being available for faiths with Communion but non-spiritual heads  
- Fixed factions not disbanding when they lose or white peace their faction war  
- Fixed granting an unlanded character titles in rare cases causing them to become independent  
- Fixed house and dynasty modifiers never expiring when they have an expiry date  
- Fixed it being possible to give your primary heir titles they won't get in partition by first giving them a title that they will get in the partition  
- Fixed it in some cases being possible to on your death continue playing as someone who didn't actually inherit any titles from you  
- Fixed it in some cases being possible to revoke a character's last county while they still hold a higher-tier title  
- Fixed it in some cases not being possible to revoke a character's last duchy or higher  
- Fixed merging units together ignoring knights for the purpose of supplies, leading to merging armies of just knights causing them to lose all supplies  
- Fixed newly created and historical characters that start with a focus being considered to already have changed it once, preventing you from changing it again in the case of childhood focuses  
- Fixed people who lose land in a war sometimes erroneously ending up as the vassal of the conqueror  
- Fixed prestige gain from alive house and dynasty members getting the "Monthly Prestige Gain" modifier applied twice  
- Fixed several issues of text overflowing in the UI in some languages  
- Fixed siege phase time and morale loss modifiers applying via the owner of the holding. E.G., the owner having the Military Engineer trait would make it faster for others to siege their holdings  
- Fixed sieges not immediately starting if a hostile army is standing in a holding that ceases to be occupied (E.G., due to a 3rd party war resolving)  
- Fixed taking someone's primary title sometimes unlanding them entirely even though they should still have vassals to steal a county from  
- Fixed taking the last physical land of a spiritual head of faith causing the head of faith title to be destroyed  
- Fixed the game in some cases (like the "Disallow Marriage" checkbox) thinking people have been rulers for far longer than they actually have been  
- Fixed the game in some cases blocking interactions saying "You is already considering a proposal from you" after interacting with yourself  
- Fixed the game in some cases releasing people from prison when it shouldn't, such as when they become rulers  
- Fixed vassals in some cases going independent or becoming a vassal of your liege if your primary title has its own succession laws and doesn't go to the same heir as the rest of your realm  
- Giving out a title while above your domain limit will no longer give you stress. Previously it'd give you stress without warning you  
- Guests with claims will no longer accept staying if you promise to press a claim that you cannot declare a war for.  
- It is no longer possible for the county capital's fort level to go below 1, which would render it unsiegeable  
- Made the Crusader helmet show up in the barbershop  
- Remove incorrect warning about adjacent vassal contract levels if its display method is a radio button, they are unique picks already.  
- The Promote Christian Settlements decision now gives Hungarian culture all innovations and innovation progress of Mogyer culture  
- The Reclaim Britannia decision no longer changes effects based on dejure drift  
- Titles with title-specific succession laws (E.G., Male Preference) that match your realm law are no longer considered separate when calculating partition splits, so they'll no longer always go to your primary heir unless the law is actually distinct from your realm laws  
- Vassals of vassals are now able to declare war on vassals of their liege's liege  
- When your spouse is also your heir in your latest save, we don't clone them to show them twice in the main menu  
- Your children will no longer leave your court just because they're bold. So daughters won't run off in male-dominated society, and sons won't run off in female-dominated society  
- A Head of Faith will no longer forsake their religion if your spouse is charming enough  
- A bastard born to a landed woman and a landed man will now get her house as default  
- A betrothal in your own court will no longer be talked about as a marriage  
- A faction will no longer courteously greet you before calling you a tyrant  
- A zealous character will now sweat a bit about committing adultery  
- Added a 10 year cooldown to childhood events if the child decides to kill the animal instead of adopting it. You monsters.  
- Added a cooldown to the "Know Thyself" upcoming death event to reduce the level of spam telling you about being at death's door  
- Added a text variant for placing a vassal under house arrest  
- Added a trigger in one of the options for clan.1201 so that rulers can't give away their only title in the name of diversity  
- Added an alert for when you have no player heir to your titles but there's someone in your dynasty who can inherit  
- Added encyclopedia link for attrition in a tooltip  
- Added grandparent checks to scheme modifiers  
- Added in events about upgrading relationships  
- Updated conditions for rival in seduction events so they don't bonk you in the head while imprisoned  
- Added missing background to the event Domain of Debauchery  
- Added missing error icon next to 'Holy War for County' when Piety Level is Sinner  
- Added missing perspectives to effect loc  
- Added missing tooltip about prestige loss in rival upgrade event  
- Added prisoner and jailor to custom loc key and trigger  
- Added triggers to notifications so that marshal vassals don't gain opinion of themselves when they do something good  
- Agent in scheme is now properly exposed  
- Alawites & Qarmatians may no longer go on Hajj, though they have access to pilgrimages as usual  
- All Hajj events now have the pilgrimage activity theme  
- An imprisoned vassal will no longer scream about rebellion  
- Apply army maintenance modifier to unraised MaA reinforcement cost  
- Assyrians no longer have access to cataphracts  
- Austria & Switzerland will now be correctly drifted into a restored Carolingian Empire  
- Babies will no longer be assigned commander traits through a yearly event  
- Barons married to other landed characters will no longer be naked  
- Bastards can no longer create Cadet Branches  
- Betrothal toast will now trigger if either participant isn't an adult  
- Blocked Vlach rulers from taking the Unite the Slavs and Unite the Southern Slavs decisions  
- Blocked the “Making Acquaintances” event and its options if the child already has all the traits/opposites that they can get from the event  
- Blocked the seduction of characters who are imbeciles or incapable  
- Butr culture now starts with Mubarizun unlocked in 1066  
- Byzantine characters now use royal headgear instead of ducal headgear  
- Calm doesn't like impatient  
- Capital duchy modifiers are now correctly recalculated after moving the capital or destroying the duchy  
- Character modifiers coming from difficulty settings are now applied correctly when loading save games and starting multiplayer games.  
- Characters are now more reluctant, or outright forbidden, from leaving their partners behind  
- Characters can no longer get different tiers of the same congenital trait  
- Characters that should be naked no longer wear cloaks  
- Characters using the northern portrait set no longer toss away their crown when they become emperors.  
- Characters will no longer be as desperate for your friendship in foreign special diplomacy event  
- Characters will no longer be doubly motivated to murder to move up the succession  
- Child preacher in event must be of age 4 or older  
- Children are no longer allowed to partake in an Intrigue challenge event  
- Children are no longer encouraged to pick up more spouses  
- Children can no longer be educated by hardened criminals  
- Children can no longer be granted a bishopric as they are too young to handle both managerial tasks and religious duties  
- Children can no longer start a literalist debate  
- Children, imprisoned, and incapable vassals can no longer demand that you host a feast  
- Clarified the development growth modifier from the terrain in the county capital to specify the capital holding name, instead of simply the county name.  
- Clarified the name for the different culture group opinion penalty by making it say "Foreign Culture Group", rather than "Culture".  
- Cleaned up cooldown for the befriend scheme  
- Clicking the Too Few Spouses issue now opens the Find Spouse interaction  
- Compassionate character are now told that blackmailing people is stressful  
- Corrected several holding names in Europe.  
- County task icon tooltip no longer shows big empty are when there's no councillor for that task.  
- Courtiers can now marry even if they're out and about  
- Courtiers of Theocracies and Mercenaries will no longer wear inappropriate clothes  
- Crusader Helmets will now always show up when appropriate  
- Devouring people will now have a clearer impact on your stress level  
- Don't apply army maintenance modifier to prestige cost  
- Dukes now understand that an Emperor can be their Rightful Liege when they're deciding if they want to join an Independence Faction  
- Dynasty Heads/House Heads can now only use their special calls to war for conflicts where they are a primary participant and the target is not already involved  
- Enabled the Nowruz festival event for all Iranian culture group characters, instead of only Persians.  
- Establish Norman Culture decision now have the effects displayed  
- Event childhood.1002 no longer triggers if child has both traits that the event can give  
- Excommunicated characters can no longer Take the Vows.  
- Family members of a prisoner will now be miffed if you snatch the prisoner up as your concubine/consort  
- Feudal Elective nominations now check the title holder's lieges' laws when determining eligible candidates  
- First Marriage event is not blocked from triggering multiple times for divorcees  
- Fix court bishop income tooltip when using theocratic lease  
- Fixed AI's caving to populist demands when they really shouldn't  
- Fixed Scalloway using incorrect cultural names.  
- Fixed Unify the Burgundies preventing culture conversion if the character was already Occitain  
- Fixed a bug sometimes preventing concubines from being shown properly in the marriage window.  
- Fixed a bug that caused the ransom prisoner event to occasionally display the payer's current gold total instead of the actual amount of gold they paid in ransom  
- Fixed a bug that prevented Counties from joining Claimant Factions  
- Fixed a bug where the faith of an attacker in a holy war did not lose Fervor when that attacker was defeated  
- Fixed a bug where there would be a small gap between neck and torso at lower levels of body fat  
- Fixed a bunch of errors popping during runtime  
- Fixed a couple of Decisions not refunding their Prestige cost properly if the player opts out  
- Fixed a couple of Scheme events for landed characters firing for unlanded characters  
- Fixed a localization error in the Holy War Casus Belli effects that referred to the attacker's vassals as 'your vassals' even when you were the defender  
- Fixed a typo in the A Spain United event  
- Fixed an error which caused the event 'Differences in Faith' to trigger for counties of your own religion  
- Fixed an error with the Unite the Slavs decision that prevented the De Jure drift effect from working correctly  
- Fixed an event stating that your lover revealed your secret when you in fact did it yourself, by claiming a bastard as your own  
- Fixed an inverted value that caused children with a 'bad' education affinity to do better at their education than children with a 'good' affinity  
- Fixed an issue with the CB cost breakdown not showing properly for the Independence CB.  
- Fixed behavior in the achievements window  
- Fixed being able to send multiple Blackmail interactions to the same character while waiting for their first response  
- Fixed broken capitalization in house and dynasty tooltips when you are the house or dynasty head  
- Fixed broken god reference in a death transition text  
- Fixed children with preexisting Guardians not being selected by default when using 'Offer Guardianship' on them  
- Fixed embracing English culture sometimes converting landed spouses or family members without their consent  
- Fixed faulty gender of a Roman  
- Fixed imprisoned characters sometimes being chosen to be mercenary captains or Holy Order Grandmasters  
- Fixed loc in seduction event  
- Fixed lowborns getting kinslayer traits when murdering other lowborns  
- Fixed perspectives for a number of Interaction triggers  
- Fixed runtime errors in script  
- Fixed some errors with tutorial concepts in the encyclopedia  
- Fixed some rank/tier game concept confusion  
- Fixed some siege logic that was causing infinite sieges in allied land when it was a part of the enemy realm.  
- Fixed sorting knights by name in the battle overview window.  
- Fixed the AI recruiting guests because they themselves had a good claim, rather than the guest  
- Fixed the kingdom of Pontus capital being set outside its de jure area. The capital is now set as Trebizond.  
- Fixed the mixed usage of possessive pronouns in the notification for Allied Combatants Captured  
- Fixed the revoke title interaction so it shows titles properly in the interface.  
- Fixed the show/hide invalid savegames logic  
- Fixed typo the name for the County of Padua, which was incorrectly named Paduan.  
- Fixed up some grammar when exposing Secrets  
- GHW title recipients who own the target title will no longer conquer it from themselves  
- Gnosticism's stress loss for granting titles now scales correctly  
- Guardian remove themselves from guardianship if their ward is imprisoned  
- Guardians will no longer keep teaching your kids after fleeing the realm  
- Guests with claims on your vassal's vassal's titles will no longer arrive due to these claims  
- Hajj decision has unique text to distinguish itself from the normal pilgrimage decision  
- Head of Faith looks at incest as a divorce reason based on faith's doctrines  
- Highborn people will now be more skeptical about marrying lowborns  
- Hindu Shahis are correctly feudal now  
- Historical characters will no longer be their own parent  
- Holstein moved to Saxony/Germany, due to being pre-Danish union (mostly)  
- If people start to murder your courtiers the experience will now be much smoother  
- If you instantly regret romancing someone the game will now accept that you've moved on  
- If you promise a vassal to educate their child they will now be miffed if you try to return the child  
- If you're trying to elect a kinslayer as your heir you will now get a functional tooltip  
- If your liege declares war on your war-target your war is invalidated  
- Imprisoned AI rulers will now attempt to ransom themselves  
- Imprisoning someone for having a Secret Lover when it's criminal does not cause tyranny when done via the secret exposed event  
- Infertile spouses will now no longer wish each other 'a long life and many children'  
- Intended achievements where you need to start as a particular can now also be accomplished after that character's death  
- Interaction-acceptance now considers personality ONCE  
- Intrigue event about zealous agent now exposes the scheme as well as the agent if you fail the duel  
- It's now possible to negotiate an alliance even if your family is very inbred  
- Khotan & Dzungaria now start entirely feudalised, rather than partially clan  
- Knights that kill or wound commanders now have a chance to increase their prowess/gain prestige  
- Korosten is now appropriately vassalised to Turov, the local tribal power  
- Landless nuns now wear habits  
- Level of splendor will no longer give 0 acceptance in marriages  
- Losing a Liberty War now only gives the attacking faction members a hook on their liege, instead of everyone attacking the liege (which included participants of completely different wars).  
- Lovers exposed during feasts have a trigger to ensure none of them are imprisoned at the time  
- Lowborn bastards no longer try to belong to a House  
- Lowered the amount of gold the recipient needs to have to unlock the Demand Payment interaction  
- Lowered the penalty for negotiating an alliance with your primary heir  
- Made sure effects are applied to the correct scope in rival upgrade events  
- Made sure marriage action looks for consort instead of concubine  
- Made sure reformed faiths get a new shiny icon  
- Made sure that all loc strings in the game are localized  
- Make a sieging standing army use proper siege animation. Also play victory animation when winning a siege  
- Married couples will no longer be exposed as if they have an affair if they're also lovers  
- Mercenary and holy order captains will now abdicate from those positions when getting titles  
- Milete faith's have Same-Sex Relations set to Shunned by default  
- More events now take place at the proper location  
- More information given if a new religious movement is founded  
- Moved blocking traits from Declare Bloodline Holy decision to be stress impacts instead  
- Moved the effects of the Convert County Task conclusion event into the immediate block to stop the event script from overwriting player changes between the event firing and resolving  
- Mystic will no longer stick their nose in religious matters that are of no concern to them  
- Naughty children go straight to jail with no education  
- Negative opinions for concubine or polygamous marriages now specifically checks for number of spouses and concubines  
- Neighboring ruler war resolution message will now name the war  
- Newly made nuns/monks are only sent to monastery of their faiths or to their liege's pool  
- Nikephoros Palaiologos is no longer Duke of Bulgaria in 1066  
- No more distance education  
- Non-relevant mercenaries should no longer use the Palace Guards cultural Men-at-Arms.  
- Now check for the correct scope when blocking attempts on joining one's ally in a war against one's liege  
- Now show the correct name when offering an opportunity to ransom a character that's not landed  
- Now showing the culture or religion trigger for Restoring the Roman Empire decision as it didn't print correctly as a tooltip  
- Only the Byzantine Emperor now wears the Imperial Crown  
- Order members can not be asked to (re)join a holy order  
- Outremer culture no longer discovers up to 7 new innovations every time a new ruler adopts it  
- Outremer culture now correctly retains all Innovations that its parent culture has discovered instead of only some of them.  
- Pecheneg ruling dynasty now relates to Khan Kura  
- People are now less eager to marry people they are terrified off  
- People that are terrified of you are now more likely to agree to marriage, as long as they don't have to marry you  
- People will no longer judge you harshly for breaking a betrothal to an Eunuch  
- Physicians are no longer in two places at once when sick  
- Pilgrimage decision preview will now give the correct minimum sum you will have to pay  
- Player now gets notifications about their right-hand person  
- Player unit graphics are now prioritized over other unit graphics when they occupy the same position.  
- Player's reaction to someone recovering from illness is now based on their relationship with the character and the previous sick person's opinion of the player  
- Populist uprising wars no longer invalidate on succession if the new liege does not personally hold the target title  
- Prevent CTD when loading save with some incorrect landed state  
- Prioritized what "Call To War" interaction and action to show  
- Properly clear occupations when liege invalidates vassal's war by attacking the same target  
- Rebuffing the advances of a romantic interest now correctly ends their scheme instead of forcing you to become soulmates anyway  
- Reforming to feudal now grants the same amount of random buildings as previously built in the province  
- Refusing to attend a feast when faith has 'Ritual Celebrations' tenet now results in loss of piety, rather than devotion  
- Relocated an oddly-positioned tooltip when refusing a blackmail threat from another player in an MP game  
- Removed an outdated reference to an old button in the 'Fabricating Claims' reactive advice  
- Removed anachronistic Mogyers from Pannonia in 867  
- Removed excess slaughtering from Iberian mercenary names  
- Removed excessive warning in Take Stewardship of the Sacred River decision  
- Removed incorrect holy sites of Jerusalem, Mosul, and Mecca from Yazidism. Replaced them with more suitable unique Holy Sites of Sinjar, Baalbek, and Lalish.  
- Removed incorrect info about fabricating claims from the title integration council task tooltip.  
- Removed redundant tooltip when offering to join a war you're already fighting in  
- Removed some game log spam in multiplayer  
- Removed the 'is diplomatically available' from the is_shown trigger for Temporal Condemnation so that it's failed conditions are only shown when failed  
- Removed the multiple message and variations of the same condition for attempting to join or create a faction when underage  
- Replaced fake Mogy├½r names  
- Required baronies in befriending events are now checked for in the event trigger  
- Reshaped the Thar Desert slightly for a better setup and to connect the counties of Ludrava and Vikramapura to one another.  
- Restructured how bastard secrets are exposed to ensure that the piety loss/opinion loss from adultery only happens once  
- Reworked and clarified a condition for Faith Reformation and Head of Faith title creation ΓÇö holy sites must be within your realm, and held by you or vassals of your faith  
- Right trait is now referenced in elections  
- Rum now no longer takes dynasty names, always retaining its title name regardless of the holder's culture  
- Saladin's Helmet (DDE) will now appear for marshals of duke+ rank and duke+ rulers leading an army, as it's too opulent and fancy for common knights  
- Same Faith only has one entry in the Laws section of the encyclopedia  
- Secret exposure notification now removes the correct hook  
- Show both siege weapon and standing unit during siege if army has siege weapons  
- Show maximum possible tax and levies for bishop in the endorsement tooltip  
- Sick characters now dress the part  
- Sneaky people will now wear sneaky clothes  
- Socotra & its historical rulers are Yemeni instead of Bedouin  
- Splendor levels are no longer over-explained in the encyclopedia  
- Split the Take Vows decision into two, one for asking someone to a go to a holy order, the other to a monastery  
- Spouse will no longer reveal their own scheme or a scheme they're part of  
- Spread Assyrian culture a little  
- Spymasters will no longer try to dig up dirt on themselves  
- Steward can no longer target themselves when discovering a claim for their liege  
- Stopped swearing fealty to the Mongol Khan ending the wrong wars  
- Stress gain/loss from deceased siblings is now calculated before friendship/lover/rivalry/opinion modifiers are deleted  
- Stricter checks on titles so that one does not give away their primary title in an event in the name of diversity  
- Svend II of Denmark now spawns as either bisexual or heterosexual  
- Temujin's kids will no longer be educated child prodigies  
- The "Form the Swiss Confederation" decision can now be undertaken even if the HRE doesn't exist  
- The "New Cultural Era" toast will now show the correct culture's cultural head character.  
- The " Cannibalism" decision can now only be taken once per Faith.  
- The 'Form Outremer' decision now correctly transfers all Innovations known by your former culture to the new Outremer culture.  
- The 'I'm not done with you yet' option in Torture events will now apply the correct effects  
- The 'Pacifism' and 'Dharmic Pacifism' tenets now correctly provide +1 Domain Limit to all adherents.  
- The 'Too Few Knights' warning will now only appear when you have too few knights, not when you have too many!  
- The 'Unrepresented' event now only fires for clans, and cannot poach lands from player characters  
- The AI will now shy further away from old marriage-partners  
- The Arrange Marriage screen now allows you to toggle the 'matrilineal' checkbox prior to selecting a recipient.  
- The Catholic Pope now wears the correct clothes  
- The Consecrate bloodline decision now gives the bloodline trait to descendants even if the family tree has dead members  
- The Decision to unify Iberia now displays the condition that you must have an Iberian Kingdom as your primary title  
- The Domestic Affairs task now correctly gives an opinion boost of your direct vassals if you're a vassal yourself  
- The Embracing/Abandoning Celibacy and Searching for Physician decisions are now available even when commanding an army  
- The Exclave Independence game rule no longer fails if the heir of a dead character is at war for 5+ years  
- The Head of Faith can no longer Excommunicate themselves  
- The Jewish Head of Faith now wears the correct clothes  
- The Mongol Empire will no longer destroy itself when winning a war  
- The Mongol Empire will now always declare the correct wars when arriving  
- The Pope can no longer publicly accept cannibalism  
- The Pope will now always wear the correct clothes  
- The council window resets to the player council tab when opened so the empty council position works correctly.  
- The death notification toasts now show death reasons properly. They are always delayed to the next event tick after the death happens now, it was inconsistent before.  
- The decision to Create the Kingdom of Israel can only be done once per campaign  
- The declare war window will no longer show claimant CBs for characters whose claims can't actually be used  
- The distance check for joining Holy Wars now checks realmborder-to-wartarget distance instead of capital-to-capital distance  
- The duration of the Private Army from your spouse is now determined by their martial skill rating  
- The elope scheme will now run smoother  
- The enabled criteria for Special Buildings will now always show up  
- The event 'Faction Organizing' no longer fires for factions you're already at war with  
- The event for discovering bastard secret now mentions the bastard by name and shows their portrait in the bottom left  
- The game will no longer tell you to take more concubines when you've had enough  
- The potential guardian to a ward who's a courtier now checks if the ward or requester is of interest to them. To educate the courtier of a count is of no interest to a foreign emperor.  
- The tutorial widget in the bookmark window will no longer show up for a fraction of a second when opening that window for the first time  
- Toast about one's foreign guest enjoying the dance is now displayed properly  
- Tooltip cleanup for  
- Two players having a child together will no longer have a screaming competition about the name  
- Tyranny now also gets added even if the vassal declines the title revocation  
- Unlanded characters will no longer have random dungeons  
- Updated Reclaim Britannia decision  
- Updated loc for a councillor being blocked from being fired from the council  
- Updated loc for culture innovations effects  
- Updated localization for culture promotion modifier  
- Updated requirements for creating the Empire of Germania to give correct tooltip  
- Updated the event loc for An Insulting Accusation to imply that the character's believes in their vassal's innocence  
- Updated the location triggers for befriend outcomes so that the correct location can be fetched when trying to befriend unlanded characters as an independent ruler  
- Vassals and Lieges no longer receive a penalty to Negotiate Alliance when you're already at war  
- Vassals can no longer call their liege into their own wars  
- War important actions and suggestions will no longer show up when the player is in debt.  
- Warning about your realm priest not endorsing you will no longer lie about levies  
- West Slavic cultures are now easier to differentiate on the map  
- When being courted by a pregnant woman, the option to bring you a wolf pelt is unavailable unless your religion allows for women combatants  
- Fixed an issue when opening the marriage window for the 1st time and the player would get the wrong default sort order.  
- When requesting gold in exchange for ending a war at the behest of your liege, the shown gold amount now correctly corresponds with what you actually receive.  
- When setting title color from another title, shift it more, so gradient border is always present  
- When the 'Generate Families' game rule is on, rulers who had a spouse and children generated will no longer receive the wedding event after game start  
- Witches can now host a Grand Rite  
- Women will now be punished for having too few consorts  
- You are no longer malnourished and obese for life  
- You can no longer Demand Conversion from imprisoned foreign rulers  
- You can no longer ask your house head to approve your divorce if you are the house head (just do it)  
- You can no longer attempt to find dead people's secrets  
- You can no longer be tortured to confess a secret you don't know  
- You can no longer demand liberty from a chill liege  
- You can no longer grant a vassal who's at war with the recipient  
- You can no longer lose a friend you didn't have  
- You can no longer owe a favor to yourself because of a necklace  
- You can no longer remove your vassal's guardians all nilly willy  
- You can now condemn your vassals for their sins even if you're pious  
- You can now declare war for your claims while imprisoned  
- You can now help your allies in religious wars they start  
- You can now marry your concubines/consorts without having to dismiss them first  
- You can now only call people of the "right" faith to Great Holy Wars  
- You can now scheme to claim thrones even while feasting  
- You can now take other ruler's concubines as your concubines if you've imprisoned them  
- You no longer is the real father, you ARE the real father!  
- You now kick hostile Holy Orders from your holdings with a few choice words  
- You wife will now leave your kids behind if she flees your tyranny  
- You will no longer be encouraged to give away your last county  
- You will no longer be stressed out if a spouse you dislike dies  
- You will no longer be told twice about your ransom offer being accepted  
- You will no longer call newly independent rulers your vassal  
- You will no longer get a broken event if your liege declares war against someone you're already warring with  
- You will no longer have to spend the rest of your life fabricating one hook  
- You will no longer refer to someone else's claims as your own  
- You will no longer think less or more of yourself depending on how good you are at romancing someone else  
- You will now be told only once that you've successfully blackmailed someone  
- You will now be told why you can't debate people 24/7  
- You will now only be notified of the establishment of Norman culture if you're in Europe  
- You'll no longer get events in third person about how virtuous you are  
- Your de jure liege is no longer called your de jure vassal  
- Your mentor will no longer ditch you in the middle of your education  
- Zealous people are no longer more likely to say goodby to their religion  
- Adaptive tenet now correctly requires you to have a pluralist religious attitude  
- Added Welsh/Cumbrian cultural names for Hereford & Herefordshire.  
- Added an extremely minor piety cost for changing to a different version of Mohammad's Succe
