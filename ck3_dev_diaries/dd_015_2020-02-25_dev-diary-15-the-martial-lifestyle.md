---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1339978/"
forum_thread_id: 1339978
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 15
title: "CK3 Dev Diary #15 - The Martial Lifestyle"
dd_date: 2020-02-25
author_handle: Heptopus
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1805
inline_image_count: 29
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1339978'
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
    location: raw_lines_391_to_393
    action: preserved_and_flagged
    counts:
      Like: 3
      Love: 2
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 2 of 3 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_401_to_450
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_451_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #15 - The Martial Lifestyle

<!-- artifact:thread_metadata:start -->
- Thread starter [Heptopus](https://forum.paradoxplaza.com/forum/members/heptopus.1269016/)
- Start date [Feb 25, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-15-the-martial-lifestyle.1339978/)
<!-- artifact:thread_metadata:end -->

Welcome back to the final installment of our breakdown of the different Lifestyles!  

Your host today will be me, [@Heptopus](https://forum.paradoxplaza.com/forum/members/1269016/), just to spice things up a little, and I am here to guide you through Warfare. But, before I do, I want to remind you that armies and battles themselves are very different from CK2, so if you want a refresher, have a look at good ol’ [Dev Diary 3](https://forum.paradoxplaza.com/forum/index.php?threads/ck3-dev-diary-3-war.1279641/).  

Without further ado, let’s have a look at the Focuses!  

![martial_lifestyle.png](https://forumcontent.paradoxplaza.com/public/535306/martial_lifestyle.png "martial_lifestyle.png")


[Strategy - Martial: +3]  
[Authority - Martial: +1, Control Growth: +0.3/month]  
[Chivalry - Prowess: +3, Attraction: +10, Advantage: +5]  

**Strategy** - Makes sense if you want to win, or even just wage, wars.  

**Authority** - Perfect for when you want to keep your realm under absolute control and cement your rule.  

**Chivalry** - The Code of Chivalry is good for lowering your chances to die on a battlefield, and heightening your chances to attract the people around you. Treating people with respect pays off, it turns out.  

The trees themselves are very varied and offer some interesting bonuses. There’s also a couple of Schemes that I’m really excited to tell you about at the end!  

![martial_lifestyle.png](https://forumcontent.paradoxplaza.com/public/535316/martial_lifestyle.png "martial_lifestyle.png")



**Strategist**  

This tree is, as one might expect, all about warfare. Some perks are fairly straightforward, such as improvements to your Men-at-Arms:  

![strategy_parthian_tactics.png](https://forumcontent.paradoxplaza.com/public/535294/strategy_parthian_tactics.png "strategy_parthian_tactics.png")


[Parthian Tactics - Light Cavalry Toughness: +30%, Light Cavalry Pursuit: +30%, Heavy Cavalry Toughness: +30%, Heavy Cavalry Pursuit: +30%, Skirmisher Damage: +20%, Skirmisher Toughness: +20%]  

![strategy_envelopment.png](https://forumcontent.paradoxplaza.com/public/535314/strategy_envelopment.png "strategy_envelopment.png")


[Envelopment - Men-at-Arms Counter efficiency: +25%]  

![strategy_hit_and_run.png](https://forumcontent.paradoxplaza.com/public/535312/strategy_hit_and_run.png "strategy_hit_and_run.png")

  
[Hit and Run - Retreat Losses: -25%, Heavy Infantry Damage: +15%, Heavy Infantry Toughness: +15%, Pikeman Toughness: +30%, Archer Damage: +30%]  

Mitigating retreat losses can be really useful if you are unlucky in a battle (and we all know it is ONLY down to bad luck), so that you can bounce back faster and show the enemy what you’re really made of.  

![strategy_organized_march.png](https://forumcontent.paradoxplaza.com/public/535293/strategy_organized_march.png "strategy_organized_march.png")


[Organized March - Movement Speed: +15%, Heavy Infantry Screen: +5, Pikeman Screen: +5, Archer Screen: +5, Skirmisher Screen: +5]  

Whether you’re fleeing or attacking, this perk will make sure you do so in an organized manner. Useful when you want to hunt down the remnants of an enemy army, or protect the remnants of your own!  

It’s also not the only perk that can speed up a conquest:  


![strategy_engineered_for_destruction.png](https://forumcontent.paradoxplaza.com/public/535311/strategy_engineered_for_destruction.png "strategy_engineered_for_destruction.png")


[Engineered for Destruction - Naval Speed: +25%, Siege Weapon effectiveness: +40%]  

So now that you have the speed, and you have the siege weapons, what more could you possibly need for a successful offense? Well, if you’re more inclined to go for the drive-through approach (some people call it raiding), or if you often find yourself losing soldiers due to hunger, we have the solution for you!  


![strategy_living_of_the_land.png](https://forumcontent.paradoxplaza.com/public/535300/strategy_living_of_the_land.png "strategy_living_of_the_land.png")


[Living Off the Land - Raid Speed: +25%, Supply Capacity: +200%]  

And if that’s still not enough you can improve your army even further by making your MaAs bring shovels to the campaign:  


![strategy_sappers.png](https://forumcontent.paradoxplaza.com/public/535313/strategy_sappers.png "strategy_sappers.png")


[Sappers - Heavy Infantry Siege Progress: +0.1, Pikeman Siege Progress: +0.1, Archer Siege Progress: +0.1, Skirmisher Siege Progress: +0.1]  

With an army this good, it would be a waste to only wage wars when you absolutely had to, wouldn’t it? That’s why we’re making CBs easier to use than ever before:  


![strategy_bellum_justum.png](https://forumcontent.paradoxplaza.com/public/535291/strategy_bellum_justum.png "strategy_bellum_justum.png")


[Bellum Justum - Casus Belli Cost: -50%]  

At the end of the tree we find the Strategist trait. It gives a boost in both Diplomacy and Martial, allows you to cross water freely, AND increases the number of dead soldiers your enemy suffers when facing you in battle. In other words, this tree will make you unstoppable on the battlefield and rightfully feared across the land!  


**Overseer**  

If you want to focus on your own realm more, and make sure it’s completely under your control, then this is the tree for you. To start it off we have some perks that will give you more stable ground to stand on, such as:  


![overseer_strict_organization.png](https://forumcontent.paradoxplaza.com/public/535301/overseer_strict_organization.png "overseer_strict_organization.png")


[Strict Organization - Increase Control in County Progress Gain: +20%]  

![overseer_serve_the_crown.png](https://forumcontent.paradoxplaza.com/public/535310/overseer_serve_the_crown.png "overseer_serve_the_crown.png")

  
[Serve the Crown - Control Growth: +0.3/month]  

And if you’re going for real stability you can tighten your grip on the population of a county so hard that you squeeze out benefits in the form of both gold and levies!  


![overseer_absolute_control.png](https://forumcontent.paradoxplaza.com/public/535308/overseer_absolute_control.png "overseer_absolute_control.png")


[Absolute Control - Enables Absolute Control for Counties]  

Absolute Control means that all of the counties you have full control over will give you 10% more taxes and levies as long as you maintain your iron grip on the populace.  

![overseer_hard_rule.png](https://forumcontent.paradoxplaza.com/public/535307/overseer_hard_rule.png "overseer_hard_rule.png")


[Hard Rule - Siege Progress against Revolts: +50%, Independence and Liberty Faction Discontent: -50]  

And when vassals, or peasants, try to turn against you… Well, let’s just say that you will make it harder for them to succeed.  

But what if the threat isn’t coming from within your own realm, but from outside it? Don’t worry, we’ve got your back:  


![overseer_a_mans_home.png](https://forumcontent.paradoxplaza.com/public/535305/overseer_a_mans_home.png "overseer_a_mans_home.png")


[A Man’s Home/A Woman’s Home - Controlled Territory Defender Advantage: +5]  

![overseer_enduring_hardships.png](https://forumcontent.paradoxplaza.com/public/535309/overseer_enduring_hardships.png "overseer_enduring_hardships.png")

  
[Enduring Hardships - Fort Level: +1, Enemy Occupations do not lower Control]  

![overseer_prepared_conscription.png](https://forumcontent.paradoxplaza.com/public/535299/overseer_prepared_conscription.png "overseer_prepared_conscription.png")

  
[Prepared Conscription - Army Maintenance: -15%, Friendly Territory Levy Reinforcement rate: +100%]  

If you need an extra push to push out an insistent enemy, you can always trade gold for swords:  


![overseer_soldiers_of_lesser_fortune.png](https://forumcontent.paradoxplaza.com/public/535304/overseer_soldiers_of_lesser_fortune.png "overseer_soldiers_of_lesser_fortune.png")


[Soldiers of Lesser Fortune - Mercenary Hire Cost: -30%]  

And, to top it all off, we have the trait Overseer. It grants you a boost in Martial, Stewardship, and Control Growth Factor, so the hold you have over your realm will be cemented for decades to come!  


**Gallant**  

Romance, prowess, and bravery… ah, the marks of a true charmer! This is the tree for those of you who want to focus on the more “elegant” side of warfare, while still giving your war efforts a boost:  


![gallant_chivalric_dominance.png](https://forumcontent.paradoxplaza.com/public/535296/gallant_chivalric_dominance.png "gallant_chivalric_dominance.png")


[Chivalric Dominance - Knight Effectiveness: +100%]  

![gallant_stalwart_leader.png](https://forumcontent.paradoxplaza.com/public/535290/gallant_stalwart_leader.png "gallant_stalwart_leader.png")

  
[Stalwart Leader - Prowess: +4, Reduces the risk of Commanding Armies]  

![gallant_kingsguard.png](https://forumcontent.paradoxplaza.com/public/535303/gallant_kingsguard.png "gallant_kingsguard.png")

  
[Kingsguard - Number of Knights: +4]  

![gallant_never_back_down.png](https://forumcontent.paradoxplaza.com/public/535295/gallant_never_back_down.png "gallant_never_back_down.png")

  
[Never back Down - Friendly Fatal Casualties: -20%, Advantage: +5]  

When you tire of fighting and it’s time to negotiate for peace you will be more persuasive than ever:  


![gallant_peacemaker.png](https://forumcontent.paradoxplaza.com/public/535302/gallant_peacemaker.png "gallant_peacemaker.png")


[Peacemaker - Peace Acceptance: +10]  

![gallant_promising_prospects.png](https://forumcontent.paradoxplaza.com/public/535297/gallant_promising_prospects.png "gallant_promising_prospects.png")

  
[Promising Prospects - Marriage Acceptance for yourself: +50, Marriage Acceptance for your Extended Family: +25]  

For friendlier times your gallant behavior attracts suitors for both you and your family, suddenly making those ridiculously good alliances possible!  

Even your own spouse isn’t immune to your charms:  


![gallant_loyalty_and_respect.png](https://forumcontent.paradoxplaza.com/public/535298/gallant_loyalty_and_respect.png "gallant_loyalty_and_respect.png")


[Loyalty and Respect - Spouse Opinion: +50, Skills from Spouse Council task: +25%]  

Of course, love is not always found in an arranged marriage, and the rumors about your gallant behavior aren’t limited to just your own court. If your dearly beloved needs to be charmed, or if you just can’t wait for permission to marry them, you can get some help along the way:  


![gallant_courtship.png](https://forumcontent.paradoxplaza.com/public/535292/gallant_courtship.png "gallant_courtship.png")


[Courtship - Romance Scheme Power: +30%, Elope Scheme Power: +30%, Romance Scheme Success Chance: +30%, Elope Scheme Success Chance: +30%]  

I think this is the first time we mention these schemes? They’re a real treat!  

The Romance Scheme finally lets you enter a chivalric romance with a character, seducing them in a court-approved manner. Just imagine a knight pining after his lady, his heart full of longing, neither of them acknowledging the smoldering feelings between them... Now that can be you! If you succeed in this scheme, and resist the temptations of the flesh (at least in public), you and your beloved become Soulmates, a more powerful version of the Lover relationship.  

And if you cannot bear to be apart, even though her liege will never approve of a marriage between you, do not fear! I bring you: Elope, marriage without any pesky relatives or lieges involved. However, in contrast to marriage, your partner actually has to like you for the union to work out, so you still have some work ahead of you. And make sure you're not caught...  


![elope_scheme.png](https://forumcontent.paradoxplaza.com/public/535315/elope_scheme.png "elope_scheme.png")



This tree culminates in the Gallant trait. It affords you extra monthly Prestige, as well as some Attraction Opinion, and of course a healthy boost to both Martial and Prowess. With all this helping you along, neither foe nor maiden will stand a chance!  


So… that’s it. Both for Martial and for our series of dev diaries focusing on Lifestyles; we made it through. I hope you’ve found something you’re looking forward to exploring and playing around with, and that you’re as excited as I am to see what kind of characters you will create with this!  

Next week we'll delve into interface, tooltips, and the tutorial, so keep your eyes peeled!

 

#### Attachments

- [![martial_lifestyle.png](https://forumcontent.paradoxplaza.com/thumbnail/public/535288/martial_lifestyle.png)](https://forum.paradoxplaza.com/forum/attachments/martial_lifestyle-png.547933/)
  
  martial_lifestyle.png
  227,6 KB

 · Views: 109

- [![martial_lifestyle.png](https://forumcontent.paradoxplaza.com/thumbnail/public/535289/martial_lifestyle.png)](https://forum.paradoxplaza.com/forum/attachments/martial_lifestyle-png.547934/)
  
  martial_lifestyle.png
  241,1 KB

 · Views: 123

<!-- artifact:reactions:start -->
- 3 Like
- 2 Love
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Heptopus](https://forum.paradoxplaza.com/forum/members/heptopus.1269016/)**
Role: Content Designer
Badges: 2
Messages: 47
Reaction score: 917
<!-- artifact:op_signature:end -->
