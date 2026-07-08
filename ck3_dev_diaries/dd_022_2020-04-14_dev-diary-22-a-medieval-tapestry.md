---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1377711/"
forum_thread_id: 1377711
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 22
title: "CK3 - Dev Diary #22 - A Medieval Tapestry"
dd_date: 2020-04-14
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
body_word_count: 1778
inline_image_count: 9
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1377711'
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
    location: raw_lines_~28_to_140
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_142_to_144
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_245_to_249
    action: preserved_and_flagged
    counts:
      Love: 12
      Like: 9
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_257_to_328
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_329_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 - Dev Diary #22 - A Medieval Tapestry

<!-- artifact:thread_metadata:start -->
- Thread starter [Heptopus](https://forum.paradoxplaza.com/forum/members/heptopus.1269016/)
- Start date [Apr 14, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-22-a-medieval-tapestry.1377711/)
<!-- artifact:thread_metadata:end -->

Hello everyone! Today Virvatuli and I are bringing you a Development Diary about how we’re catering to different player fantasies in CK3. We will also showcase some of the content and gameplay you’ll encounter!  

We are huge believers in allowing players as much freedom as possible to shape the game world in their image, which is reflected in the Paradox slogan “We make the games, you create the stories.” Of course, when trying to model history reasonably accurately as we do in CK3, your starting environment might be a far cry from the just and equal Realm you wish to rule, but determined players should be able to change the mores of their society over time - if that is their fantasy.  

As you might suspect, the CK3 team consists of some very nerdy, passionate and compassionate people. Some of the things we’re outlining in this Dev Diary were part of the regular development process, and some have been passion projects. It has been very important for us to represent our players, the team behind the game, and the people who don’t feature heavily in most history books and media. We want everyone to feel welcome and to empower you to play your fantasy.  

CK3 truly is a diverse game; it spans a map of nearly half the world and almost six centuries of history. This world is inhabited by a myriad of titles, cultures, faiths, and characters. It’s been our goal to represent all of these things with a great level of detail and accuracy to give you all a deeply immersive experience with more dynamic elements and player choice than ever before. Will you recreate history, build a brand new world, or something in between? It is all in your hands.  

But we haven’t just added more diversity; that variety is also much more readily available than it was in CK2. For example, all Faiths and Cultures on the map are playable on release, and the dynamic Faith system will give you much greater power to change the world. We’ve also added many different Game Rules which allow you to tailor your CK3 experience. If you would rather play as a Queen than a King from day one, the Game Rules let you do that, without having to create a custom Faith during your campaign. There are other challenges out there to conquer and stories to explore!  

We are incredibly proud of all the stuff we’ve made for you, so without any further ado, let’s jump into the juicy, juicy details!  


**Gender Options**  

All gender-related restrictions in CK3 are controlled by the Faiths, either directly or indirectly. As we have an awesome dynamic Faith system, all such restrictions can be changed during a playthrough. Our design philosophy for Faith Tenets related to gender has been to have the exact same options available for men and women. For example, the “View on Gender” Tenet has the settings “Male Dominated”, “Equal” and “Female Dominated”. All the restrictions for women in Male Dominated Faiths are applied to men instead in Female Dominated Faiths.  

![genderviewtenet.png](https://forumcontent.paradoxplaza.com/public/554004/genderviewtenet.png "genderviewtenet.png")

  

Even when men historically held the highest titles and womens’ rights were limited, women still had a vital impact on the world around them. In many parts of the medieval world, it was not uncommon for women to rule in their husbands’ absence, they were often advisors and took care of estates. We have chosen to represent this with the Spouse Council Position. Your Spouse’s skills have a direct impact on your realm and you will see events about your Spouse handling all sorts of duties, from negotiating with factions to raising additional troops.  

![the_guard_1.png](https://forumcontent.paradoxplaza.com/public/554005/the_guard_1.png "the_guard_1.png")

  

Like in CK2, we have a Gender Equality Game Rule, but with some improvements and added variation. The “Equal” setting (corresponding to “All” in CK2) covers more areas and has fewer exceptions than it did in CK2, largely thanks to our dynamic Faith system and the design philosophy mentioned above. It also comes with an “Inverted” setting where the historical gender statuses are turned on their head and women become the dominant gender in most religions.  

![Diversity_female_rules.png](https://forumcontent.paradoxplaza.com/public/554006/Diversity_female_rules.png "Diversity_female_rules.png")

  

Women are also more visually present in Crusader Kings than ever before. We have some awesome loading screens with a diverse bunch of characters, for example, but the biggest impact comes from the new event window. In CK2 we had lovely event illustrations, but the drawback was the lack of variation when it came to characters. In CK3 we use our gorgeous character models to bring the events to life, which will showcase the rich diversity of the cast of your playthrough in the event windows.  

![far_from_home_1.png](https://forumcontent.paradoxplaza.com/public/554008/far_from_home_1.png "far_from_home_1.png")




**Sexuality**  

Sexuality provides added spice to character behavior and motivations, both in real life and in CK3, and it will also affect what is considered sinful or even criminal in a Faith in the game. It’s great for drama and intrigue, and in CK3 we’ve given sexualities more granularity. In addition to heterosexuality and homosexuality from CK2, characters can also be bisexual and asexual. Sexuality is no longer defined by a trait, but has its own system, which makes it easier to handle for us and more visible in the interface for you. It also means that we do not frame heterosexuality as the default in CK3, which was also important for us.  

Children develop their sexualities around the age of 10 and once set, it will not change. It’s worth noting that we don’t model sexual and romantic attraction separately in the game, so a character’s sexuality sets both their sexual and romantic preferences.  

![budding_attraction.png](https://forumcontent.paradoxplaza.com/public/554009/budding_attraction.png "budding_attraction.png")

  

We do however differentiate between sexual preference and sexual behavior in-game. A character’s sexuality in and of itself can never be criminal, but certain sexual acts can be. For example, if a Faith’s “View on Same-Sex Relations” is not set to “Accepted”, two men who have sex will get the “Sodomite” Secret (no matter their sexuality). While the AI doesn’t pursue romance or sex with someone they’re not attracted to, the player can sometimes choose to act against their sexual preference (albeit with a penalty, and it can never lead to a lover relationship). This means a player’s heterosexual male character could get the “Sodomite” Secret if they seduce a homosexual or bisexual man.  

We have two Game Rules related to sexuality: “View on Same-Sex Relations” and “Sexuality Distribution”. The former is very similar to the “View on Gender” rule I mentioned above; it can change all Faith’s “View on Same-Sex Relations” from their historical defaults to “Accepted”. The latter can change how common each sexuality is. The settings are “Default” which means Heterosexuality is the most common sexuality, “Equal” which makes all four sexualities equally common, and one setting each for Homosexuality, Bisexuality, and Asexuality which makes them the most common sexuality instead of Heterosexuality.  

![accepted_same_sex_relationships.png](https://forumcontent.paradoxplaza.com/public/554010/accepted_same_sex_relationships.png "accepted_same_sex_relationships.png")

  


**Faiths**  

As the dev diaries of the last couple of weeks have shown we have given Faiths a lot of attention, and as you might already know, all Faiths will be unlocked at game start. The dynamic Faith system has allowed us to add plenty of variation at release; we hope you’ll find that each Faith has its own flavor and quirks.  

Even better, we now have more distinctions between different non-Christian Faiths, especially in Africa and India! African Paganism from CK2 has been replaced with at least six new Faiths; Roog, Bori, Siguism, Akom, Waaqism, and Kushitism, all with their own Tenets and flavor. For example, the Bori have a long history of matriarchs and worship the spirits. As they believe in spirit possession and that spirits can be either feminine or masculine, they are accepting of same-sex relations. The Siguics, on the other hand, worship their ancestors and believe that twins are blessed.  

![religion.png](https://forumcontent.paradoxplaza.com/public/554011/religion.png "religion.png")

  

Hinduism has been split into seven different Faiths. In addition to expanding upon and fleshing out the four main traditions of Hinduism (Vaishnavism, Shaivism, Shaktism and Smartism), CK3 also sees the addition of less well-known Hindu traditions such as Krishnaism and Advaitism. Buddhism has five Faiths, Jainism three, and many Religions across the map have received similar diversification. We have also added a Dualism Religion with seven different Faiths, for example Manicheanism, Mandeanism, and Sabianism.  

![india.png](https://forumcontent.paradoxplaza.com/public/554012/india.png "india.png")

  

And as you can create your own Faiths, you will be able to create the kind of society you want to play in. As I have mentioned, some things can be preset through Game Rules, but the challenge of changing the world to your liking can be a really satisfying experience.  

For example, we have the Game Rules “Faith Acceptance” which makes religious wars and disagreements a thing of the past, and “Randomized Faiths” which gives everyone in the world a random Faith. For those of you who are sensitive to border gore, please proceed with caution as the following screenshot contains graphic imagery. For the rest, how many Faiths can you spot in the screenshot?  

![how_many_faiths.png](https://forumcontent.paradoxplaza.com/public/554013/how_many_faiths.png "how_many_faiths.png")

  


**Ethnicities and Cultures**  

We have expanded the amount of portrait asset sets from the two in the CK2 base game to a grand total of seven in CK3! On release, there will be a visual distinction between Western Europe, Northern Pagans, the Middle East/North Africa, Byzantium, the Steppe, Sub-Saharan Africa, and India. We will also have an even greater number of ethnicities, so you will see variations within these seven groups.  

Thanks to the new portrait system, ethnicities now blend seamlessly. When two characters of different ethnicities have a child, the children will look a bit like both parents. More on this in a later Development Diary!  


**The End**  

That’s all for this week, friends! Unfortunately, Virvatuli will not be around to answer your questions this time, as she has set out on a new adventure after four years at Paradox. But the rest of the team will be around, of course, so ask away!  

Take care of yourselves and each other <3

<!-- artifact:reactions:start -->
- 12 Love
- 9 Like
- 5 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Heptopus](https://forum.paradoxplaza.com/forum/members/heptopus.1269016/)**
Role: Content Designer
Badges: 2
Messages: 47
Reaction score: 917

*[Full game-badge icon list of 11 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
