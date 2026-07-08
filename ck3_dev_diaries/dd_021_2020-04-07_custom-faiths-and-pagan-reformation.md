---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1372700/"
forum_thread_id: 1372700
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 21
title: "Dev Diary #21 - Custom Faiths and Pagan Reformation"
dd_date: 2020-04-07
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
body_word_count: 1151
inline_image_count: 5
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1372700'
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
    location: raw_lines_202_to_205
    action: preserved_and_flagged
    counts:
      Like: 14
      (unlabeled — rendered as base64 data URI): 3
      Love: 1
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_213_to_321
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_322_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Dev Diary #21 - Custom Faiths and Pagan Reformation

<!-- artifact:thread_metadata:start -->
- Thread starter [Baron von Shoes](https://forum.paradoxplaza.com/forum/members/baron-von-shoes.1426511/)
- Start date [Apr 7, 2020](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-21-custom-faiths-and-pagan-reformation.1372700/)
<!-- artifact:thread_metadata:end -->

Oh, hello there! Interested in becoming a heresiarch, are we? Or maybe you just want to organize your ancestor’s ancient spiritual traditions into a true reformed Faith, one that can stand up to the Crescent and Cross? Either way, you’ve come to the right place!  

To start us off, I’m going to go into how the process of creating a new Faith or reforming a pagan one works. After that, there will be a teaser of some Tenets and Doctrines that you may be interested in picking for your newly-founded Faiths ![;)](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Wink    ;)")  

**Faith Creation**  
Creating a new Faith is no easy task. Only the most pious rulers will be able to convince the clergy within their realm that they alone know the true will of the divine and, in doing so, take the first steps towards establishing a new Faith. However, with a little bit of devotion and a lot of time, you too will be able to reshape your Faith to suit your dynasty’s needs!  

When looking at your own Faith’s tenets and doctrines, you will see a button at the bottom labeled ‘Create New Faith’. Clicking this button will open the Faith Creation window, which can be viewed at any time — even long before you have acquired the means to actually create a new Faith! This will allow you to play around with the different options and get a feel for what is possible, allowing you to set long-term goals for yourself.  

![DD_CreateAFaith_WM.png](https://forumcontent.paradoxplaza.com/public/551168/DD_CreateAFaith_WM.png "DD_CreateAFaith_WM.png")

 [Screenshot of the Faith Creation window showing modified Tenets and Doctrines]  

You can change every single Tenet and Doctrine of your hypothetical new Faith on this screen, though the list of what Tenets are available to pick varies from Religion to Religion. For example, Tenets based on the concept of Dharma are exclusive to Oriental Religions, whereas Monasticism was common practice and is thus available to everyone. This means when creating a new Faith, you must first ensure you are a member of the Religion that you want to base your new Faith off of.  

Beyond simple availability, it is also easier for some Religions to accept certain Doctrines than others. For example, Islam is used to polyamory and will happily accept a new Faith espousing it. In contrast, a new Christian faith that claims God intended us to have multiple spouses will be met with a little more skepticism...  

The way this plays out in CK3 is that each Tenet and Doctrine has a Piety cost associated with it. The further you deviate from your original Faith, the more Piety you will need in order to convince the priests that yes, you actually have had a vision from the divine and yes, you actually are enforcing their will and not just trying to make some weird personal sex cult.  

![DD_Cosanguinity_WM.png](https://forumcontent.paradoxplaza.com/public/551169/DD_Cosanguinity_WM.png "DD_Cosanguinity_WM.png")


[Screenshot of the scaling costs for the Cosanguinity Doctrine]  

After you have made all the changes you want, you will be given the total amount of Piety your character needs in order to create their new Faith. This cost can get quite high, meaning that creating a new Faith or reforming a pagan one ends up being a life-long goal for most characters. It is highly recommended to attempt this with characters who have a Learning education and/or who have multiple Virtuous personality traits, and having the ability to go on frequent pilgrimages or donate gold & troops to holy causes helps too! Finally, timing your divine revelation to completely coincidentally occur when your Faith is suffering from low Fervor will make it much easier to get everyone to buy into your new canon (I will talk more about Fervor in our future Dev Diary on heresy outbreaks).  

Once you are happy with your Tenets and Doctrines and have accumulated the necessary amount of Piety, you can officially convert to your new Faith. You and your capital county will adopt it immediately, but it won’t be easy for a ruler to convince their vassals and subjects to adopt this strange new Faith — they might be more inclined to stage an uprising and depose their mad king from the throne! After all, if you die before your new Faith gains a foothold in the world, there is a good chance your Faith will die with you…  

**Pagan Reformation**  
Pagan Faiths in Crusader Kings III start out with the special ‘Unreformed’ Doctrine.  

This Doctrine grants notable bonuses to Tribal rulers early on, but it locks them into the Tribal government type and provides substantial Opinion penalties to any non-Tribal vassals they acquire. Since Tribal realms are notoriously unstable, successful chieftains will eventually want to look into either converting to a reformed religion so they can feudalize, or reforming their pagan religion into a true organized faith.  

Like with Faith Creation, rulers must earn a substantial amount of Piety to organize their Faith’s disparate shamans into a coherent clergy. In addition, they must have at least 3 of their Faith’s holy sites located within their realm.  

![DD_VidilismHolySites_WM.png](https://forumcontent.paradoxplaza.com/public/551170/DD_VidilismHolySites_WM.png "DD_VidilismHolySites_WM.png")


[Screenshot showing 3 of the Vidilist Holy Sites]  

Once you accomplish this, the process is quite similar to creating a new Faith of an existing reformed Religion. Your vassals may still be reluctant to convert to your newly reformed Faith, but because reformed Faiths gain a bonus to conversion against unreformed Faiths, you will have a much easier time convincing them to go along with your reformation than a heresiarch within in an existing Faith would have with making a new heresy.  

![DD_ReformationNew_WM.png](https://forumcontent.paradoxplaza.com/public/551416/DD_ReformationNew_WM.png "DD_ReformationNew_WM.png")

   [Screenshot showing a Vidilist reformation event]  

**Tenet and Doctrine teaser**  

To finish this off, here are a few choice tenets and doctrines which you can pick when creating a new Faith in CK3. Many of these are also used by already existing Faiths, but some are only available to custom Faiths created by players. As you can see, there is a lot of variety in the kinds of custom Faiths you can create — ultimately every kind of playstyle should have some set of Tenets and Doctrines to support it!  

![DD_Tenet_Showcase_WM.png](https://forumcontent.paradoxplaza.com/public/551173/DD_Tenet_Showcase_WM.png "DD_Tenet_Showcase_WM.png")

[Screenshot of the Tenets Warmonger, Human Sacrifice, Ritual Cannibalism, Christian Syncretism, Dharmic Pacifism, Carnal Exaltation, Divine Marriage, Sacred Childbirth, and the Doctrines Pluralism and Fundamentalist]  

That is all I have for you this week, but join us next time as my colleague [@Heptopus](https://forum.paradoxplaza.com/forum/members/1269016/) talks about the diversity across the world in CK3 and the many different ways you can tailor the game experience to match your personal preferences!

<!-- artifact:reactions:start -->
- 14 Like
- 4 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
- 1 Love
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Baron von Shoes](https://forum.paradoxplaza.com/forum/members/baron-von-shoes.1426511/)**
Role: Content Designer
Badges: 54
Messages: 65
Reaction score: 2,138

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
