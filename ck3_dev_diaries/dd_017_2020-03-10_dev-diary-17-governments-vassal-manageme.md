---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1352640/"
forum_thread_id: 1352640
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 17
title: "CK3 Dev Diary #17 - Governments, Vassal Management, Laws, and Raiding"
dd_date: 2020-03-10
author_handle: Meneth
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1924
inline_image_count: 7
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1352640'
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
    location: raw_lines_~28_to_138
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_140_to_142
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_255_to_257
    action: preserved_and_flagged
    counts:
      Like: 18
      (unlabeled — rendered as base64 data URI): 6
    note: Reactions block parsed; 1 of 3 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_265_to_356
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_357_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #17 - Governments, Vassal Management, Laws, and Raiding

<!-- artifact:thread_metadata:start -->
- Thread starter [Meneth](https://forum.paradoxplaza.com/forum/members/meneth.265499/)
- Start date [Mar 10, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-17-governments-vassal-management-laws-and-raiding.1352640/)
<!-- artifact:thread_metadata:end -->

Good afternoon, everyone. I’m Magne “Meneth” Skjæran. You might know me from the CK2 dev diaries or the Paradox Wikis, but for the last couple of years I’ve been working on CK3 as a programmer. Today we’re going to cover a number of topics closely related to government types: governments themselves, vassal management, laws, and raiding.  

Let's start off with a familiar concept from CK2: governments. For the player, we have three playable governments: Feudal, Tribal, and Clan, which each have some significant differences in how they play.  

The Feudal government type is based on European feudalism, and is heavily based around the idea of obligations: you owe service to your liege, and your liege owes you protection in return. It is the most common government form in the game. Feudal realms play pretty similarly to CK2, focusing on claims and inheritance more so than the other government forms.  

A new addition in CK3 is Feudal Contracts. Every feudal vassal (except barons) has an individual contract with you, rather than obligations being set realm-wide. These contracts have three levels; Low, Medium, and High, with Medium being the default. High will provide more levies and tax at the cost of an opinion hit, while Low provides less but improves opinion. Higher levels are usually better (though perhaps not if you’re at risk of your vassals revolting), but cannot be imposed unilaterally.  

You’ll need to have a hook on your vassal in order to increase their obligations unless you’re fine with all your vassals considering you a tyrant, but you can always lower them. As a result this means you can significantly increase your power if you’re able to obtain hooks on your vassals; perhaps a bit of judicious blackmail might be in order?  

![Feudal Contract.png](https://forumcontent.paradoxplaza.com/public/539711/Feudal Contract.png "Feudal Contract.png")

  
[Modifying a Feudal Contract]  

Furthermore we have the Clan government form. This government is the rough equivalent of the Iqta government in CK2, though in CK3 it does have a more Feudal bent than it did previously.  

The Clan government type is used by most Muslim realms. This government puts more emphasis on the family rather than the realm, with most vassals being members of your dynasty. Obligations are heavily based on opinion rather than being contractual, with happy vassals providing significantly more taxes and levies than unhappy ones. A happy family is a powerful family.  

Clan governments also have access to the Clan Invasion casus belli, which can be used once in a lifetime at the highest level of Fame to invade a kingdom, providing a powerful boon for a well-established clan ruler.  

Finally we have Tribal realms. Much like in CK2 these have their own Tribal holding type, providing more troops but less tax. Additionally, most tribals are able to go on raids, which you can read more about below. Tribal realms are unaffected by development, and cause non-tribal realms to have lower supply limits in their lands, making them a tougher nut to crack, but reducing their influence as the years drag on. Tribal realms also pay for men at arms using prestige rather than gold, allowing smaller realms to punch above their weight.  

Tribal rulers base their obligations on levels of Fame rather than on contracts or opinion; the more famous your ruler is, the more troops and money your vassals will be willing to provide for your pursuits.  

Finally, Tribal rulers have a once-in-a-lifetime Subjugation casus belli, allowing them to forcibly vassalize an entire realm.  

As the game goes on, you can eventually reform out of Tribalism, becoming a Clan or Feudal realm instead.  

![Vassal Overview.png](https://forumcontent.paradoxplaza.com/public/539712/Vassal Overview.png "Vassal Overview.png")

  
[The vassal management tab]  

To get an easy overview of your realm, we in CK3 have the Realm screen. Let’s start with the Vassals tab of this screen where all your vassals are shown. This gives you a clear overview of where your levies and taxes come from, who might be a threat to you, and allows you to renegotiate feudal contracts.  

This is also where you change your crown authority (or tribal authority), which I’ll talk more about later in this dev diary.  

Lastly, the screen shows your Powerful Vassals. Much like in CK2’s Conclave DLC, your realm will have some powerful vassals; these expect to be seated on the council, and will make their displeasure known if that is not the case.  

![Domain overview.png](https://forumcontent.paradoxplaza.com/public/539713/Domain overview.png "Domain overview.png")

  
[The Domain Tab]  

Then we have the Domain tab. This lets you easily inspect your domain, showing where you’re earning money and levies, and where you can build more buildings. It also shows the level of development and control in the counties you personally hold, letting you easily tell where you can make improvements.  

Finally we have the Succession tab. Due to being a bit of a work in progress, I’m afraid I can’t show you a picture of it right now. Here you can change your succession laws, see your heir(s), and check what titles, if any, you will lose when you die. If you hold any elective titles, you’ll be able to easily get to the election screen from here.  

Now with all these mentions of laws, let's go through what laws exist. We’ve trimmed down the number of laws from CK2 as much of what used to be law is handled on a more individual level now, but some still remains.  

Like in CK2, we have crown authority for Feudal and Clan realms, and tribal authority for Tribal realms. Higher levels of authority unlock mechanics like imprisonment (for tribals, the others start with it), title revocation, restrictions on internal wars, and heir designation. However, increasing these levels will make your vassals unhappy. Tribal authority is significantly less powerful than crown authority, representing how Tribal governments over time gradually got supplanted by Feudal and Clan governments.  

![Succession Laws.png](https://forumcontent.paradoxplaza.com/public/539714/Succession Laws.png "Succession Laws.png")

  
[Changing succession law]  

Then there’s succession laws. To no one’s surprise, Gavelkind is making a return, though we’ve renamed it to Partition to make it more obvious what it actually means. This is the default succession form of most realms in both 867 and 1066.  

For added fun, there’s now three variants of Partition. We’ve got regular Partition, which functions like Gavelkind in CK2; your realm gets split roughly equally between your heirs, and any heirs that end up a lower tier than your primary heir becomes a vassal.  

However, many realms start with a worse form, especially in 867. This is Confederate Partition, which will also create titles of your primary title’s tier if possible. So if you as Norway have conquered all of Sweden but destroyed the kingdom itself, it will get recreated on your death so that your second heir becomes an independent ruler. Tribals are typically locked to this succession type, with some exceptions.  

Finally we have an improved version of Partition: High Partition. Under High Partition your primary heir will always get at least half your titles, so it doesn’t matter if you’ve got 2 or 10 kids; your primary heir will get the same amount of land.  

We’ve also done a lot of tweaks to the internal logic of who gets what titles, which tends to lead to far nicer splits than in CK2; border gore will of course still happen, but to a lesser degree than before.  

Then we have the other succession forms. There’s Oldest Child Succession (replacing Primogeniture), Youngest Child Succession (replacing Ultimogeniture), and House Seniority. A notable difference from CK2’s Seniority Succession is that under House Seniority, the oldest eligible member of your house inherits, not of your entire dynasty.  

We also have a number of variants on elective succession, ranging from Feudal Elective, to Princely Elective (HRE succession), and a handful of cultural variants. Each of these have different restrictions on who can vote, who can be elected, and how the AI will select who to vote for.  

Additionally, we’ve got a full suite of gender laws, corresponding to the gender laws in CK2. These are: Male Only, Male Preference, Equal, Female Preference, and Female Only.  

Finally, we have raiding. If you’re a Norwegian like me, sometimes you feel your Viking blood coursing through your veins, the noise of it drowning out everything else. Times like this, there’s only one solution: go on a raid.  

Fans of Pagan gameplay in CK2 will be glad to hear that not only have we implemented raiding in CK3 as well, we’ve made some improvements to it to make it more fun to play with, and less unfun to be on the receiving end of.  

The core system is very similar to CK2. If you’re a Pagan or Tribal ruler, you have the ability to raid other rulers’ lands. To do so you raise a raid army, and march or sail over to your target. Only the Norse can raid across sea; other raid armies will simply be unable to embark.  

![Rally Point.png](https://forumcontent.paradoxplaza.com/public/539716/Rally Point.png "Rally Point.png")

  
[Raising a raid army]  

Once at your target your army will start looting the barony they’re in. This is a pretty quick process, but during it your army will be unable to move, preventing you from running away from any counter-raiding force. This change makes it a lot simpler to deal with raiders if you’ve got enough men and can raise them quickly enough, as the AI won’t just immediately run away.  

![Raid Lindisfarne.png](https://forumcontent.paradoxplaza.com/public/539717/Raid Lindisfarne.png "Raid Lindisfarne.png")

  
[A raid in progress]  

While in CK2 raiding was done on a county level, in CK3 it is on a barony level. Another difference is that in CK3 raiding no longer uses the siege mechanics directly, but rather a similar system where things like siege engines do not have an impact since you’re raiding the countryside, not a heavily fortified castle.  

Another significant change is that if you beat a raid army, you receive all the gold they’re carrying. This means that even if you cannot respond instantly to a raid, it is still very much worth it to beat up the raiders. Like in CK2, you also become immune to raiding by that enemy for several years.  

Just like in CK2, a raid army is limited in how much loot it can carry based on the army size. Loot is deposited once the army is back in friendly lands, after which you might either disband or go raiding once more.  

On the quality of life side, we now show on the map what provinces have already been raided when you have a raid army selected. This makes it easy to see what places to avoid. Hovering over a province will also tell you how much loot raiding it would provide.  

![Raid.png](https://forumcontent.paradoxplaza.com/public/539719/Raid.png "Raid.png")

  
[Northern England in its natural state]  

That’s all for today, folks. Tune in next week to learn more about how war functions in Crusader Kings 3.

 

Last edited: Mar 10, 2020

<!-- artifact:reactions:start -->
- 18 Like
- 9 (unlabeled — rendered as base64 data URI)
- 6 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Meneth](https://forum.paradoxplaza.com/forum/members/meneth.265499/)**
Role: Crusader Kings 3 Programmer
Badges: 153
Reaction score: 5,413

*[Full game-badge icon list of 29 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
