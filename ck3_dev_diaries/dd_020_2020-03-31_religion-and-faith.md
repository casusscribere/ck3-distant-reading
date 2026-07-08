---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1368714/"
forum_thread_id: 1368714
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 20
title: "Dev Diary #20 - Religion and Faith"
dd_date: 2020-03-31
author_handle: Baron von Shoes
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1587
inline_image_count: 8
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1368714'
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
    location: raw_lines_~28_to_142
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_144_to_146
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_270_to_274
    action: preserved_and_flagged
    counts:
      Love: 18
      Like: 7
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_282_to_377
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_378_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Dev Diary #20 - Religion and Faith

<!-- artifact:thread_metadata:start -->
- Thread starter [Baron von Shoes](https://forum.paradoxplaza.com/forum/members/baron-von-shoes.1426511/)
- Start date [Mar 31, 2020](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-20-religion-and-faith.1368714/)
<!-- artifact:thread_metadata:end -->

Come one, come all! Zealots and cynics, fundamentalists and heretics! It is time for us to finally talk about religion in Crusader Kings III, and all that it entails.  

While parts of the religion system in CK3 may seem familiar to fans of the previous games, the system itself has been completely rebuilt from the ground up. As a result, there is little point in talking about changes from CK2; instead, I will start diving into how religion works in CK3 and what that means to you as a player.  

**The Religious Hierarchy**  
The most logical place to start talking about religion in CK3 is with… Religions! As a game concept, a Religion is defined by four main things:  


- What Traits are considered Sins and Virtues (3 each by default)
- What Religion Family it belongs to (Abrahamic, Oriental, or Pagan)
- What the standard religious Doctrines are for its Faiths
- What Tenets are available to its Faiths
Individual characters and counties will never believe in a whole Religion — they believe in a Faith instead, with each Religion having several Faiths under it. For example, Catholicism and Orthodoxy are Faiths under Christianity, while Theravada and Mahayana are Faiths under Buddhism.  

![DD_WM_ChristianFaiths.png](https://forumcontent.paradoxplaza.com/public/548416/DD_WM_ChristianFaiths.png "DD_WM_ChristianFaiths.png")


[Screenshot showing a selection of either Christian Faiths, including distinct Coptic and Apostolic Faiths]  

Similar to the way that Faiths belong to a Religion, Religions belong to a Religion Family. Religion Families are little more than groups of Religions, but this does serve an important purpose, as it plays a significant part in how Faith Hostility is calculated (more on that in a later Dev Diary).  

**Anatomy of a Faith**  
So if a character believes in a Faith, what does that mean for them? Well, each Faith is based on its parent Religion and inherits those attributes, but will be differentiated from other Faiths by its Tenets, Doctrines, and Holy Sites.  

**Tenets**  
Tenets are mechanical representations of the most important rites, rituals, and traditions of a Faith. Every Faith has exactly 3, picked from a total of around 50 different Tenets in the whole game. Tenets are the things which make a Faith special and unique, the things that set it apart from the other Faiths even within the same Religion (and especially outside of it).  

![DD_WM_Catholicism.png](https://forumcontent.paradoxplaza.com/public/548407/DD_WM_Catholicism.png "DD_WM_Catholicism.png")


[Screenshot of the Catholic Faith’s 3 Tenets - Armed Pilgrimages, Communion, and Monasticism]  

Taking Catholicism as an example, we see one of their Tenets is that of Communion. This Tenet is what allows the Catholic Pope to excommunicate rulers, as well as allowing rulers to buy Indulgences from the Pope.  

![DD_WM_CommunionTenet.png](https://forumcontent.paradoxplaza.com/public/548408/DD_WM_CommunionTenet.png "DD_WM_CommunionTenet.png")


[Screenshot of the Communion Tenet, promoting values of honesty and community among adherents]  

You may notice here that Communion also modifies what traits are considered Sins and Virtues by the Faith. While every Faith inherits 3 Sins and Virtues from its parent Religion, Tenets can add, modify, or remove these.  

While some Tenets are unique to a single Faith, others are shared among multiple Faiths. For example, both Catholicism and Orthodoxy have the Communion Tenet. However, it is important to note that no two Faiths have the exact same combination of Tenets — as a result, every Faith will play at least a little differently, and some drastically so!  

![DD_WM_SacredLies.png](https://forumcontent.paradoxplaza.com/public/548409/DD_WM_SacredLies.png "DD_WM_SacredLies.png")


[Screenshot of the Sacred Lies Tenet, promoting scheming and treachery among adherents]  

**Doctrines**  
While less impactful than Tenets, Doctrines are still a crucial part of each Faith. A Faith’s Doctrines determine both its clerical structure as well as what its adherents can and cannot legally do.  

![DD_WM_Doctrines.png](https://forumcontent.paradoxplaza.com/public/548410/DD_WM_Doctrines.png "DD_WM_Doctrines.png")


[Screenshot of the Catholic Doctrines]  

Every Faith has at least 18 Doctrines, with a few extras depending on the circumstances. While every Religion has a default stance for each Doctrine, these should be considered guidelines more than actual rules; individual Faiths can and do break away from standard dogma when appropriate. The different Doctrines are broken up into 4 categories:  

- Main Doctrines
- Marriage Doctrines
- Crime Doctrines
- Clergy Doctrines

Main Doctrines cover how a Faith is organized on a fundamental level. These include things such as the traditional gender roles of a Faith, if the Faith has a Religious Head or not, how accepting (or unaccepting!) the Faith is of other Faiths and Religions, and if its priests must be part of a dedicated theocracy or if lay clergy are permitted.  

Marriage Doctrines cover who is allowed to get married and how: if rulers can have multiple spouses, if concubines are permitted, if and when divorce is permitted, if extramarital relations can result in legitimate heirs, and who can even get married in the first place.  

The Crime Doctrines cover what acts, if any, are considered immoral or even outright criminal. Characters who are publicly known to have violated these principles are Shunned, suffering an opinion penalty with all characters of that Faith, and may even be considered an outright Criminal who can be lawfully imprisoned and punished for their violations against divine law.  

Finally the Clergy Doctrines determine how priests must behave and what their primary role in society is. The Clergy Doctrines also determine what power, if any, secular rulers have over the clergy within their realm.  

**Holy Sites**  
Finally, every Faith has some number of Holy Sites that this Faith considers to be more sacred than the rest. Controlling these Holy Sites will give a bonus to all characters of that Faith; this can create a significant source of conflict in the game, as many different Faiths can share specific Holy Sites, and every one of them wants to be the one in control!  

![DD_WM_HolySites.png](https://forumcontent.paradoxplaza.com/public/548412/DD_WM_HolySites.png "DD_WM_HolySites.png")


[Screenshot showing the five Orthodox Holy Sites and their corresponding bonuses]  

**Moddability**  
I’m going to go on a quick tangent here and talk about modding Faiths and Religions in Crusader Kings III. Primarily, I want to mention that everything I have talked about so far is completely modular! This means Religion Groups, Religions, Faiths, Doctrines, Tenets, and Holy Sites can all be swapped in and out, modified, changed, or new ones added with even just a basic knowledge of scripting.  

![DD_WM_Script.png](https://forumcontent.paradoxplaza.com/public/548414/DD_WM_Script.png "DD_WM_Script.png")


[Screenshot of a script snippet showcasing the Coptic Faith’s parameters]  

This is one of the primary reasons we settled on the Faith, Tenet, and Doctrine system for CK3. Even though religion has a massive impact and touches dozens of game systems, it is easy for even new modders to dip their toes into the pool and start adding or changing things as they see fit. For experienced modders, this setup improves productivity and reduces the risk of introducing bugs. This has also had the side-effect of improving our productivity here at the office, which brings me to...  

**This is my Faith. There are many like it, but this one is mine.**  
At current count, we have 99 different Faiths in Crusader Kings III, all of which are fully playable. That more than doubles the number of playable religions we had in CK2 *after* Jade Dragon released.  

![DD_WM_EgyptNubia.png](https://forumcontent.paradoxplaza.com/public/548415/DD_WM_EgyptNubia.png "DD_WM_EgyptNubia.png")


[Screenshot of Egypt and Nubia, showing the diverse number of Faiths in the region]  

Remember what I said earlier about how no two Faiths have the same combination of Tenets, and how every Faith would play at least slightly differently?  

Yeah.  

Your options are quite extensive:  


- You can play as the good ol’ Catholics, or one of their heresies like the Cathars.
- You can play a different branch of Christianity, such as the Coptic Church or the Armenian Apostolic Church.
- You can play as a more unusual branch of Christianity like the Adamites.
- You can play not just as Sunni or Shia, but as individual religious movements or schools within them such as the Ash’ari or Maturidi, and the Isma’ili or Qarmatian.
- You can play as various Jewish movements, such as the Karaites or Rabbanists.
- You can play as a Dualist sect, such as Sabianism or Manicheanism.
- You can play as individual branches of Hinduism, such as Vaishnavism and Shaktism, or make the choice between Therevada, Mahayana, and Vajrayana Buddhism.
- You can play as one of three different schools of Confucianism, shaped by differing philosophies and focuses.  
- You can play as a distinct African pagan Faith such as Bori Animism or the Senegambian Roog Sene.
- You can play as either Tengri or Magyar steppe pagans each with their own special traditions.
- You can play as one of the Indian or Tibetan pagans as well, extending beyond Bon and into other regional and cultural Faiths.
- Finally, don't forget the old favorite pagan Faiths like Norse (now called Asatru)!
While many of these faiths will have some similarities and common elements (especially within the same Religion), none of them are identical to each other. They all differentiate themselves mechanically in at least one way, and often in many ways. But… let’s say you’ve looked at every single one of these Faiths, and none of them are quite right. What, then, is a soul-searching medieval ruler to do?  

Well, join us next week for the Dev Diary on Custom Faith Creation and Pagan Reformation!

<!-- artifact:reactions:start -->
- 18 Love
- 7 Like
- 5 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Baron von Shoes](https://forum.paradoxplaza.com/forum/members/baron-von-shoes.1426511/)**
Role: Content Designer
Badges: 114
Messages: 65
Reaction score: 2,138

*[Full game-badge icon list of 37 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
