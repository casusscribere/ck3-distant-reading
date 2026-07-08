---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1924995/"
forum_thread_id: 1924995
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 3
title: "\"Silk & Silver\" Dev Diary #3 - Merchants Vision"
dd_date: 2026-05-26
author_handle: PinkAxelotl
expansion: Silk & Silver
patch: null
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2711
inline_image_count: 24
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1924995'
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
    location: raw_lines_~28_to_114
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_116_to_117
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_390_to_394
    action: preserved_and_flagged
    counts:
      Like: 81
      Love: 38
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_402_to_512
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_513_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# "Silk & Silver" Dev Diary #3 - Merchants Vision

<!-- artifact:thread_metadata:start -->
- Thread starter [PinkAxelotl](https://forum.paradoxplaza.com/forum/members/pinkaxelotl.1880684/)
- Start date [May 26, 2026](https://forum.paradoxplaza.com/forum/developer-diary/silk-silver-dev-diary-3-merchants-vision.1924995/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/silk-silver-dev-diary-3-merchants-vision.1924995/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/silk-silver-dev-diary-3-merchants-vision.1924995/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/silk-silver-dev-diary-3-merchants-vision.1924995/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22945](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/by-god-alone-dev-diary-3-puppets-theocratic-play.1923707/ "&quot;By God Alone&quot; Dev Diary #3 - Puppets &amp; Theocratic Play") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/silk-silver-dev-diary-4-republics-vision.1927392/ "&quot;Silk &amp; Silver&quot; Dev Diary #4 - Republics Vision")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/silk-silver-dev-diary-3-merchants-vision.1924995/?prdxDevPosts=1)

![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_banners/4/4531.jpg?1779793063)

# "Silk & Silver" Dev Diary #3 - Merchants Vision

- Thread starter [PinkAxelotl](https://forum.paradoxplaza.com/forum/members/pinkaxelotl.1880684/)
- Start date [May 26, 2026](https://forum.paradoxplaza.com/forum/developer-diary/silk-silver-dev-diary-3-merchants-vision.1924995/)

Hi all! I’m PinkAxelotl. Today, we’re taking a look at our vision for Merchants in *Silk & Silver*. Who are they, what is the experience they provide, which are the relationships that matters to them the most, and what specific systems are used to support their gameplay?  

For the purposes of this Development Diary, the term “Merchant” only includes the new landless Merchant government. We won’t delve into details about their administrative-focused counterparts, i.e. Patricians or Republics. That’s a topic for another time.  

Let’s get an important disclaimer out of the way: We’re right in the thick of development and all of this is subject to change.  


![1 - Trade Flows Forever On.png](https://forumcontent.paradoxplaza.com/public/1503991/1 - Trade Flows Forever On.png "1 - Trade Flows Forever On.png")

By introducing Merchants we have an unique opportunity to provide a new playstyle that covers a previously untapped historical fantasy around trade and wealth-based power dynamics. Fight other Merchant families over important Trade Goods, win the favor of your Patron, and most importantly – keep caravans moving.  

The focus of the Merchant experience is that of the family Company. This means that we’re not creating a peddler fantasy. You have family members and Associates (Courtiers) working the caravans on behalf of the Company.  

Merchant gameplay is a constant trade-off between Gold and Prestige. As a Merchant, you are highly capable at Trade, but constantly hindered by not being a noble. Throughout this document, you will see that this interplay between Prestige and Gold pervades all mechanics we introduce for this playstyle.  

Career Path  

So who exactly can be a Merchant? We’ve added the option to “Create your own Merchant” on game start, which can be done anywhere in the world. You will also be able to become a Merchant via a Decision when playing as a Duke or Count, as long as your Culture allows it. Patricians and Adventurers will also be able to take this Decision.  

As you progress your Company, you might eventually want to settle down somewhere. The problem of getting to the very top is that everyone wants a piece of the pie. Being the biggest Merchant should not mean that no one challenges you. Rather the opposite. Acquiring land and “settling down” in the traditional sense should be an appealing way to mitigate risks and “tie down” assets. You can accomplish this by either purchasing land from your Patron, or choosing to either join or form a Republic.  

Monopolies & Trade Expertise  

Building Trade Expertise in a Primary Good of your choosing and acquiring Monopolies are integral to a Merchant’s Company progression (i.e. becoming *the* wine salesman of Italy). These have been covered extensively in the latest Silk & Silver Dev Diary on Trade, so for brevity’s sake we will move right along.  

Company Size  

Your Monopolies and Trade Expertise tells the world *what* you are, while your Company Size is all about *who* you are as a Company.  

![image_01.png](https://forumcontent.paradoxplaza.com/public/1503995/image_01.png "image_01.png")


*[Available Company Sizes]*​


Your Acumen represents the amount of gold your company has accumulated through Trade. For progression, it is used to gate the different Company Sizes, which you can spend Prestige to unlock (the first being an “Aspiring Business” and the last being “Trade Empire”).  

For all intents and purposes, you can view these as your Company status. If you have a Trade Empire, most interactions will be easier for you to accomplish successfully, especially if you are looking to acquire a Trade Monopoly.  

The different Size tiers boost a Company’s Competitiveness, which helps handle trade competition. They also unlock Merchant Charters from increasingly higher-tiered characters (i.e. dukes at tier 2, kings at tier 3, and so on). We will cover these Charters later in the document.  

Company Purposes  

We can’t talk about Merchant fantasies without covering Company Purposes. Right from the get-go, we knew we wanted to put a lot of emphasis on the role-playing possibilities of playing as a Merchant, to fill the day-to-day activities of being the head of a Company, so that you’re not simply sitting around waiting for gold to trickle in. This is especially important for balancing against the number-heavy Trade feature.  

![image_02.png](https://forumcontent.paradoxplaza.com/public/1503996/image_02.png "image_02.png")


*[Company Purpose Overview]*​


Company Purposes are different paths to pursue. Will you become a skilled craftsperson, lend gold at exuberant rates, trade in weapons, or reach for distant riches?  

The different Purposes are:  


- **Reputable**: Default starting Purpose, increasing family and Patron opinion.
- **Artisan**: Focus on Artifacts and Inspiration.
- **Creditor**: Lend gold and get strong hooks.
- **War Profiteer**: Sponsor wars with either Men at Arms or Mercenaries.
- **Caravaneer**: Get strong cultural bonuses and unlock Luxury Contracts.

You can pursue many of these actions regardless of what Purpose you have. We’re not limiting the amount of tools you have to engage with while playing as a Merchant character. The goal of these Purposes is to allow you to be significantly better at a particular playstyle, not limiting you to one.  

As you will have noticed, all Purposes reference Opportunities and Contracts, and so let’s get into those next.  

![image_03.png](https://forumcontent.paradoxplaza.com/public/1503997/image_03.png "image_03.png")


*[Reputable Company Purpose]*  

![image_04.png](https://forumcontent.paradoxplaza.com/public/1503998/image_04.png "image_04.png")


*[Artisan Company Purpose]*  

![image_05.png](https://forumcontent.paradoxplaza.com/public/1503999/image_05.png "image_05.png")


*[Creditor Company Purpose]*  

![image_06.png](https://forumcontent.paradoxplaza.com/public/1504000/image_06.png "image_06.png")


*[War Profiteer Company Purpose]*  

![image_07.png](https://forumcontent.paradoxplaza.com/public/1504001/image_07.png "image_07.png")


*[Caravaneer Company Purpose]*​


Trade Contracts  

Similar to landless Adventurers, Merchants have access to a variety of contracts. The purpose of Merchant Contracts is primarily to either gain Prestige or Trade bonuses.  

![image_08.png](https://forumcontent.paradoxplaza.com/public/1504003/image_08.png "image_08.png")


*[Promote Goods Trade Opportunity]*​


When taking on a Contract, you will be required to do a bit of legwork to improve the markets along your Trade Route, travelling far abroad to secure luxury goods, and build your Prestige to eventually be able to compete with the big traders.  

![image_09.png](https://forumcontent.paradoxplaza.com/public/1504004/image_09.png "image_09.png")


*[Luxury Contract Event]*​


Our current list of Merchant Contract Types are:  


- **Trade Opportunities**:
  * Used to maintain existing Trade Routes. When going on a Trade Opportunity, you travel to a market for a variety of purposes, such as increasing the sell price of specific trade goods, and promoting your business so as to make the market more attractive.
  * Trade Opportunities are also an avenue into fighting competing Merchant Families in your markets.
- **Unity Contracts**:
  * These are urgent situations that require your immediate attention. You must address irregularities in your business dealings, or run the risk of losing face. Most often one of your family members has been accused of misconduct. Can you assuage every party involved?
- **Luxury Contracts**
- Undertake expeditions abroad and bring home wealth that significantly bolster your reputation. But the higher reward, the higher the risk. Will you be able to capture and reliably move live exotic animals back home?
- Luxury Contracts unlock Domicile Artifacts and are the only way of acquiring them.

Trade Opportunities trigger schemes that you have to complete. To make these more active and engaging, we’re adding a button that allows you to gain Advantages at an increased risk.  

On top of that, we are adding an option for you to chain Trade Opportunities, so that you don’t need to go home in-between. Or, you can choose to send a dedicated Associate to handle the situation in your place.  

![image_10.png](https://forumcontent.paradoxplaza.com/public/1504005/image_10.png "image_10.png")


*[Push for Advantages button]*​


Company Palace  

As a Merchant, your Company Palace (Domicile) is your base of operations. All your Trade Routes start here. A bigger and better Palace increases the max number of Trade Routes you can set up as well, which makes upgrading your Palace integral to progressing your Company.  

![image_11.png](https://forumcontent.paradoxplaza.com/public/1504006/image_11.png "image_11.png")


*[Wuhsha’s Domicile at Game Start]*​


One noteworthy characteristic of the Palace is that this Domicile type is fully integrated into the city where you are located. This means that if you upgrade a domicile building, you are investing in the holding at large. The main and external buildings cost Prestige in addition to Gold, since you are technically constructing in a landed ruler’s realm.  

![image_12.png](https://forumcontent.paradoxplaza.com/public/1504007/image_12.png "image_12.png")


*[Domicile Artifacts]*​


With very few steady Prestige incomes, your Palace is also a place you can show off the exotic artifacts you’ve obtained through Luxury Contracts. These can be assigned to your Palace’s own artifact inventory.  


![2 - Thicker Than Water.png](https://forumcontent.paradoxplaza.com/public/1503992/2 - Thicker Than Water.png "2 - Thicker Than Water.png")

A Merchant’s family members are key to components in managing Trade successfully. Family members will be responsible for managing specific trade routes, and have abilities that directly improve the market abilities of that route. As the House Head, you decide how far to push your family, and whether or not the individual interests must be sacrificed for the sake of the Company, which is where House Unity comes in.  

Traders  

You can assign either Family or Associates to oversee and manage Trade Routes. These characters will handle the menial tasks associated with the buying and selling of goods, so that you can focus on the bigger picture for the Company.  

The Trader tasks are:  


- Manage Competition: Raises Competitiveness
- Negotiate Deals: Improves Acumen gain
- Oversee Caravans: Gives Trade Capacity

![image_13.png](https://forumcontent.paradoxplaza.com/public/1504008/image_13.png "image_13.png")


*[Trader assigned to Trade Route]*​


House Unity  

As the Merchant government is heavily family-oriented, we also made the decision to implement House Unity for it. This offers a lot of opportunities for the tension and cohesion of family members.  

Merchant House Unity has a distinct trade off: High House Unity is all about blood ties and presenting like a Noble Family (i.e. high focus on Prestige, at the cost of a competitive trade edge). Meanwhile, low House Unity centers around profit and getting skilled characters involved in the Trade, no matter the blood ties (i.e. high focus on Competitiveness, at the cost of Prestige).  

![image_14.png](https://forumcontent.paradoxplaza.com/public/1504009/image_14.png "image_14.png")


*[Cooperative House Unity - second highest level]*  

![image_15.png](https://forumcontent.paradoxplaza.com/public/1504010/image_15.png "image_15.png")


*[Concerted House Unity - highest level]*  

![image_16.png](https://forumcontent.paradoxplaza.com/public/1504011/image_16.png "image_16.png")


*[Fractious House Unity - second lowest level]*  

![image_17.png](https://forumcontent.paradoxplaza.com/public/1504012/image_17.png "image_17.png")


*[Divided House Unity - lowest level]*  


![3 - Company Network.png](https://forumcontent.paradoxplaza.com/public/1503993/3 - Company Network.png "3 - Company Network.png")


Patron  

To manage your business, you are wholly dependent on your Patron, who is the holder of the County where your Palace is located. This character allows you to conduct trade in their land, with the expectation that you will supply the needs of their holding. The relationship between you is a new tributary type, where you become their Beneficiary.  

You have a special interaction that targets your Patron, from which you can ask for a range of favors, including marrying into low nobility. Engaging with your Patron is the primary way to spend gold to get Prestige. And Prestige, as we’ve learnt, is how to improve your Trade.  

Merchant Charter  

If you schmooze your Patron well enough, you can also request a Charter from them. This opens up a whole new level of Decisions for you, where you can either use the Charter in defiance of your Patron to vastly boost your Prestige, or reinvest some of your gold into your Patron’s lands to develop buildings and increase Prosperity. The latter of which will boost the trade output of your local market. Win win.  

![image_18.png](https://forumcontent.paradoxplaza.com/public/1504013/image_18.png "image_18.png")


*[Charter gained]*​


Any Patron can only have one active Charter at a time, while having a number of Beneficiaries vying for it at the same time.  

Working with or against your Patron has its own risks/rewards. Use the Charter to support them, and you might eventually be rewarded. Use the Charter against them, and you might eventually be punished, at the risk of imprisonment and the destruction of the artifact.  

![image_19.png](https://forumcontent.paradoxplaza.com/public/1504014/image_19.png "image_19.png")


*[Abuse Charter Authority Event]*​


Competition  

House Relations play an important part in keeping track of a Merchant’s main competition. As soon as you start creating Trade Routes, your relationship with merchants in those markets will start to deteriorate. Obtaining a Monopoly that another merchant is vying for also deteriorates the relationship. Basically, if you are competing over the same resources, the relationship between your Houses will become increasingly fraught.  

You can use the Charter and Trade Opportunities to put a real dent in the Competitiveness of your competitors, along with all the regular scheming and plotting of the regular Crusader Kings 3 experience.  


![4 - In Conclusion.png](https://forumcontent.paradoxplaza.com/public/1503994/4 - In Conclusion.png "4 - In Conclusion.png")

Here you have the Merchant experience: one where familial duty is posed against company profit, where a lowborn character might hope to rise above their station by building a lasting trade empire.

<!-- artifact:reactions:start -->
- 81 Like
- 38 Love
- 8 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PinkAxelotl](https://forum.paradoxplaza.com/forum/members/pinkaxelotl.1880684/)**
Role: Private
Badges: 59
Messages: 16
Reaction score: 659

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
