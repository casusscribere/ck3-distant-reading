---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1411956/"
forum_thread_id: 1411956
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 38
title: "CK3 Dev Diary #38 - Legacy Showcase"
dd_date: 2020-08-18
author_handle: rageair
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2540
inline_image_count: 7
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1411956'
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
    location: raw_lines_~28_to_156
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_155
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1438.jpg?1597753937
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_158_to_160
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_318_to_323
    action: preserved_and_flagged
    counts:
      Like: 147
      Love: 84
      (unlabeled — rendered as base64 data URI): 6
      Haha: 1
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_331_to_409
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_410_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1438.jpg?1597753937)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #38 - Legacy Showcase

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Aug 18, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-38-legacy-showcase.1411956/)
<!-- artifact:thread_metadata:end -->

Greetings! It’s been a while since the Dev Diary about Dynasties, and we’re thinking that you might be interested in what the other Dynasty Legacies have in store. That way you have some time to plan which Legacies you’d like to play with first, and perhaps even theorycraft a bit!  

As mentioned in the Dynasty Dev Diary, you have to carefully choose between using your powers as Dynast or saving up for Legacies (or strike a careful balance). Unlocking Legacies are a very long-term goal, but can radically alter the way you play the game. Because Legacies are permanent, the bonuses they convery are generally not as powerful as those you get from Lifestyles - on the other hand you can count on them for the rest of the game! And they apply to every member of your dynasty.  

Depending on how you play, you’ll unlock varying amounts of Legacies each game. If you carefully plan every child’s marriage it’s possible to complete several tracks - but even so, the first one you choose is usually the one that will truly define your Dynasty, as you struggle your way to the top!  

The cost of Legacies is static, and each step in a track gets progressively more expensive. The first step costs 1000 renown, and the last one costs 5000. While most tend to unlock one full track before moving on (as the bonuses get progressively more powerful) it’s a legitimate strategy to pick up some of the cheaper ones first.  

Let’s briefly go through each track.  

**Warfare**  


![Warfare.png](https://forumcontent.paradoxplaza.com/public/597894/Warfare.png "Warfare.png")


The Warfare legacies mold your Dynasty members into competent knights and powerful commanders. The ideal choice for a true warmonger, or someone who wants to stalwartly defend their rightful lands.  

Personally, I find that the Warfare Legacy track does really well when playing in an area where you’re likely to get attacked, such as when playing Tribal, or in the crossroads between India and the Middle East.  

The first Legacy, **House of Warriors**, makes every Dynasty member have additional +2 Prowess skill, as well as increasing the effectiveness of Knights by 15% for landed members. A very powerful early-game Legacy, and the only one that objectively increases your military might.  

**Generational Belligerence** reduces the cost of going to war by 20%, primarily making conquest and third-party Claim wars easier to declare (warring for your own Claims is always cheap, but declaring wars for someone else’s is expensive). A good Legacy for those that want to grow their realm early.  

**Squire Traditions** makes all members gain 10% more Martial lifestyle experience. You’ll see similar bonuses in other trees for other Lifestyles. All of these are generally great to have, and stack with the bonuses you get from education.  

**Inherited Tactics** is a fantastic Legacy for winning wars, as it gives your dynasty members +5 Advantage while leading armies. As you’ll eventually experience, Advantage is the main deciding factor in wars. Having an extra +5 is truly huge, but of course - your enemies could always recruit your family members and use them as commanders against you…  

Finally, the **Private Army** Legacy unlocks an additional slot for Men-at-Arms. This is not to be underestimated, as there are no other sources of additional Men-at-Arms slots except for increasing your tier. Additionally, it also gives you access to the ‘House Guard’ regiment - a special regiment of Heavy Infantry MaA that is free, but takes up one MaA slot and can’t have its size increased. This makes even a lowly Count of your Dynasty able to field quite a formidable force, while you as a mighty Emperor might instead opt to use the extra MaA slot for an additional unit of Armored Horsemen!  

**Law**  


![Law.png](https://forumcontent.paradoxplaza.com/public/597895/Law.png "Law.png")


The Law legacies focus on stability and consolidation, making members of your Dynasty exceptionally good vassals and reducing the chance of revolts.  

I personally enjoy using these Legacies when running a larger realm, especially one containing multiple Cultures. I usually go for it when playing a vassal in the Holy Roman Empire or the Seljuk Empire, as the subjects you have are quite diverse.  

The first Legacy, **Mostly Fair**, increases popular opinion in your domain by 5. This is quite powerful, and even offsets the entire penalty for being the wrong culture in the same culture group. A great Legacy to have if your domain is mostly made up of other cultures or faiths.  

**Faithful Magistrates** increases passive Control Growth by 0.2/month in your entire Domain. Getting control up after conquest or revocation is a challenge, and your Marshal can only be assigned to one County at a time. This also makes your Dynasty members excellent vassal candidates for newly conquered lands.  

**Power and Prosperity** boosts Stewardship lifestyle experience by 10%.  

**Delegated Authority** increases your Powerful Vassal’s opinion of you by 5, which isn’t insignificant seeing how hard they can be to please. Especially when you’re an Emperor, and simply can’t have all of your Powerful Vassals on the Council…  

Finally, **Home Estates** increases your Domain Limit by 1, which is a fantastic bonus to have - especially if you’re not playing a line of high-stewardship characters. This means that it’s easier to preserve your domain throughout the generations.  

**Guile**  


![Guile.png](https://forumcontent.paradoxplaza.com/public/597896/Guile.png "Guile.png")


The Guile Legacies are optimal for those that want to rule as dreaded tyrants, and/or murder their way to the top.  

If I know that keeping my realm together peacefully isn’t an option, then this is what I’d pick. The increase in Dread gain is invaluable when starting off, especially if I need to get my plans going quickly. In Spain, for example, there’s just no time to waste in uniting the lands, so ruling through fear while removing my brothers one-by-one is a legitimately good way to play. Generally, I’d avoid picking these Legacies if I was planning to have a lot of Dynastic vassals, as some legacies can be double-edged...  

The first Legacy, **Ominous Reputation**, increases Dread gain by 20%, a fantastic starting Legacy when you want to rule through fear throughout the generations.  

**Long Reach** increases Hostile Scheme Success Chance by 10%, which is excellent as it applies not only to murders, but to Hook Fabrication, Abduction and all other hostile schemes too. It is a double edged sword though, if your kinsmen want to see you dead…  

**Natural Schemers** boosts Intrigue lifestyle experience by 10%.  

**Venial** makes Tyranny decay 20% faster, which is great in combination with Dread for quickly reorganizing your realm through revocations and retractions.  

Finally, the **Family Connections** legacy gives each Dynasty member a major chance of avoiding one successful murder scheme targeting them. When playing as a Dreadful ruler, being murdered is really the only constant threat hanging above your head. It’s calming to know that you have at least some protection, but remember, your devious brother will have the same...  

**Blood**  


![Blood.png](https://forumcontent.paradoxplaza.com/public/597897/Blood.png "Blood.png")


The Blood legacies were briefly covered in the previous Dev Diary, and remain my personal favorites. They affect the inheritance of traits, and can even make your Dynasty known for showing certain traits!  

This legacy track is optimal for those wanting to play the breeding game, trying to get the best possible rulers to succeed them.  

**Noble Veins** has two bonuses; firstly it improves the chance of inheriting good congenital traits by 30%, and then it adds 30% to the (admittedly small) chance for new good genetic traits to randomly appear. Quite a good starting Legacy, allowing you to kickstart the breeding game.  

**Convergent Blood** increases the chance of reinforcing genetic traits by 30%. This means that the offspring of a character with the first level strength genetic trait would have that much more chance of getting the second level genetic strength trait, and so on. Naturally, this chance is still mostly dependent on both parents having the traits.  

**Resilient Bloodline** is much like Noble Veins, but it reduces the chance of bad genetic traits appearing randomly or propagating, also by 30%.  

**Architected Ancestry** allows you to select one of the following traits to more commonly appear among your Dynasty Members: Beauty (Tier 1), Physique (Tier 1), Intelligence (Tier 1), Fecund (50% more fertility), Giant, Dwarf, Scaly or Albino. This one is fantastic for roleplaying, as having a dynasty of, for example, Giants makes for a very interesting story. Historically there were definitely families known for sharing a specific ‘trait’, flattering or not, this legacy represents that. The chance for each newborn child to get the trait is roughly ~2%, so you’ll still have to put in some work if you want the trait to be truly common.  

**Octogenarians** increase Life Expectancy by 5 years. Unlike a flat health boost, this also makes women able to carry children for 5 more years, and makes character portraits visually age slower.  

**Erudition**  


![Erudition.png](https://forumcontent.paradoxplaza.com/public/597898/Erudition.png "Erudition.png")


The Erudition legacies are more powerful than they might seem at a glance, with a strong focus on piety and the clergy - but the final legacy is possibly the strongest of them all, if you keep a skilled council.  

I personally enjoy the Erudition legacies when playing in the middle of a vast Feudal sphere, such as the HRE or anywhere in India, as the guests you get are much more vital to your expansion than in Clan/Tribal areas like the Middle East or Africa.  

**Vibrant Court** increases your Court and Guest opinion by +10, and makes your Court attract better Guests. The opinion is very useful, as it makes your court less likely to scheme against you, but the true power of this legacy lies in the attraction of better guests. When choosing where to travel, Claimants and exceptionally good commanders/knights are significantly more likely to visit you, should you be within their range. If you plan to expand early using foreign Claimants, this is the legacy for you.  

**Ordained Rulership** increases your Piety gain by 10%, providing one of the few sources of unconditional Piety increase in the game. This is obviously a great legacy if you’re aiming for creating your own Faith, or just want the Pope to love your Dynasty.  

**Treasured Knowledge** boosts learning lifestyle experience by 10%.  

**True Believers** give your Dynasty a +5 Clergy opinion, which will help you earn the favor of both realm priest and Head of Faith. If you’re of a faith with no Clergy, you will instead gain a +3 flat increase in opinion for characters of your faith.  

**Bureaucrats** increase the base progress and impact from Councillor skill on Council Tasks by 10%. Yes, this means that every single Council task is 10% faster. Of course, this effect is more useful the more skilled your council is - but with the better guests attracted by Vibrant Court you’ll rarely find yourself without suitable candidates!  

**Glory**  


![Glory.png](https://forumcontent.paradoxplaza.com/public/597899/Glory.png "Glory.png")


The Glory legacies are all about the name of your dynasty, and how far you can get it to travel across the known world. Prestige and opinion, fame and glory!  

Naturally, this is a great track for those in need of prestige - which includes all Tribal rulers. This is not to say that the legacies aren’t useful for others, as they make it easier to arrange beneficial marriages and get the aid you need.  

**Desirable Match** increases marriage acceptance by 30. Now, how much is that really? There are many factors that determine the acceptance of a marriage, but having an extra 30 essentially means that you’re able to marry one step above your current position (marrying the child of a Duke as a Count, for example). Now, this truly shines when combined with the Gallantry Lifestyle Tree Perk, for a total of 80 extra acceptance… Essentially a must-have for anyone planning to play an extended marriage game.  

**Renowned Name** increases Prestige gain by 10%, providing one of the few sources of unconditional Prestige increase in the game. You can never have too much prestige, as it helps both with increasing your Level of Fame (opinion) and as a resource for declaring war!  

**Earning Respect** boosts diplomacy lifestyle experience by 10%.  

**Assertive Rulers** reduces the Short Reign penalty by 20%, providing a much needed boost to stability on succession.  

**Righteousness** increases general opinion by 10, yes, that’s with everyone. A massively helpful legacy for keeping your realm faction-free! Essentially, a Dynasty with a completed Glory legacy track will have no troubles keeping even large realms together.  

**Kin**  


![Kin.png](https://forumcontent.paradoxplaza.com/public/597900/Kin.png "Kin.png")


Finally, the Kin legacies are tailored for those that want a truly vast Dynasty, where members help each other and rarely quarrel.  

Now, there’s no better legacy for those that want a big realm where most vassals are of your own Dynasty. Your kin will tend to be well educated, and keeping the peace is easier when you can use schemes such as Sway or Befriend (or even Seduce…) against your kin with ease. I really enjoy this legacy track when playing a polygamous faith, for example when playing as a Clan ruler in the Middle East, as then you’re motivated to keep a large dynasty regardless.  

**Bounteous Loins** increase fertility by 10% for your entire Dynasty, this means that it’s much easier to get over the early-game ‘hump’ where you’re establishing your dynasty, as well as make your dynasty larger in the long run.  

**Studious Youth** makes it much more likely for members of your dynasty to get good Education traits, offsetting the need for finding a high-learning guardian.  

**Constant Care** increases spousal opinion by +10, and lowers the chance of complications during pregnancy. Again, in the long run this means that your Dynasty will grow much larger than those without these legacies.  

**Close Bonds** gives a Dynasty opinion bonus of +5, which means that everyone in the entire dynasty likes each other much more than they already do (essentially doubling the bonus). It also provides one of the most fun bonuses of any legacy; 30% increased success chance of Personal Schemes against Dynasty Members. This means every personal scheme, from Sway to Elope. Use with care...  

**Graceful Aging** makes it so that your Dynasty members do NOT lose prowess with age. Normally, older characters lose prowess with time, making a once-great knight easily bestable by a young upstart in personal combat. It also gives Dynasty members a chance to randomly gain skills when growing older, making the elder members of the dynasty truly wise, and very useful as commanders, knights and councillors!  

---  

That’s it for this Dev Diary! I hope you have fun figuring out what you want to go for first!

<!-- artifact:reactions:start -->
- 147 Like
- 84 Love
- 22 (unlabeled — rendered as base64 data URI)
- 18 (unlabeled — rendered as base64 data URI)
- 6 (unlabeled — rendered as base64 data URI)
- 1 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)**
Role: CK3 Game Director
Badges: 43
Reaction score: 11,829

*[Full game-badge icon list of 16 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
