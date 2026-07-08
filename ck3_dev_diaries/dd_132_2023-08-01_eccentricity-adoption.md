---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1595139/"
forum_thread_id: 1595139
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 132
title: "Dev Diary #132 – Eccentricity & Adoption"
dd_date: 2023-08-01
author_handle: Meka66
expansion: Wards and Wardens
patch: Patch 1.10
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1104
inline_image_count: 13
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1595139'
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
    location: raw_lines_~28_to_145
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_144
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2481.jpg?1690858560
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_147_to_149
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_261_to_266
    action: preserved_and_flagged
    counts:
      Like: 131
      Love: 39
      (unlabeled — rendered as base64 data URI): 8
      Haha: 2
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_274_to_339
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_340_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2481.jpg?1690858560)
<!-- artifact:thread_banner:end -->

# Dev Diary #132 – Eccentricity & Adoption

<!-- artifact:thread_metadata:start -->
- Thread starter [Meka66](https://forum.paradoxplaza.com/forum/members/meka66.1470167/)
- Start date [Aug 1, 2023](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-132-eccentricity-adoption.1595139/)
<!-- artifact:thread_metadata:end -->

### Eccentric​

Hello hello hello, welcome to another Wards and Wardens dev diary! Today I'm going to be talking you through two new features: adoption and the Eccentric trait! We'll start off with the simpler of the two features: Eccentricity.  

### Why add a new trait in Wards and Wardens?​

Friends and Foes added the Loyal and Disloyal traits, but unfortunately these came quite late in development and as a consequence they were quite under-utilized, so we decided to have the discussion around new traits quite early this time around and we went over a few different ideas including Superstitious, Silly vs Serious, but we kind of knew all along that what we really wanted was something analogous to the Wild Wasteland trait in Fallout or CK2 Lunatic.  

For those unfamiliar, Lunacy in CK2 was usually where we made our more… out there content. There are still echoes of this here and there in CK3, but for the most part, Lunacy isn't really the same as it was.  


![image-1.png](https://forumcontent.paradoxplaza.com/public/997638/image-1.png "image-1.png")


The decision was made quite early in CK3's development that the lunatic trait would be analogous to real-world mental illness so this kind of content was typically deemed inappropriate. As a result of that decision, we've not really had an easy way to gate the sillier side of things when it comes to the player character. This has been a bit of a divisive subject on the forums, so we felt we needed some way to gate the content without resorting to game rules.  

### What is Eccentric? Who is Eccentric?​

Eccentric is a *personality* trait meaning it is an essential part of a character's personality. Eccentrics are erratic and irrational, but there is a method to the madness so they may be able to see things that other characters don't.  


![image-2.png](https://forumcontent.paradoxplaza.com/public/997639/image-2.png "image-2.png")


*Numbers are subject to balancing*  

Wards and Wardens being all about children and childhood made it the perfect fit for a new Personality trait, and as with all other Personality traits in the game, Eccentric can be acquired during childhood.  


![image-3.png](https://forumcontent.paradoxplaza.com/public/997640/image-3.png "image-3.png")


![image-4.png](https://forumcontent.paradoxplaza.com/public/997641/image-4.png "image-4.png")



People have been known to lose their marbles later in life, so a particularly stressed character may have a mental break which causes them to start seeing things in a more Eccentric way.  


![image-5.png](https://forumcontent.paradoxplaza.com/public/997642/image-5.png "image-5.png")



As you can see in the below screenshot, a non-Eccentric child would just guess at the options presented to them, but an eccentric may think of something a bit more creative.  


![image-6.png](https://forumcontent.paradoxplaza.com/public/997643/image-6.png "image-6.png")


![image-7.png](https://forumcontent.paradoxplaza.com/public/997644/image-7.png "image-7.png")



There has also been an audit of some existing content to add checks for the Eccentric trait where sensible. The now-infamous Cat-apult event, for example, has now been made into an Eccentric event.  

Something I'd like to nip in the bud quite early is that the Eccentric trait is not intended to reflect any real-world disabilities, illnesses, or neurodivergence. I think it's wonderful if you are able to project some of your own experiences onto the trait, but making a direct and conscious effort to make the Lunatic trait analogous to real-world mental illnesses is the reason why we ended up making Eccentric to begin with and we'd rather not have to come up with another trait for our silly content.  

Eccentric is a free feature and will be available to everyone, but some unique content related to the trait will be exclusive for DLC-owners.  

### Adoption​

Now onto the next feature of this diary and one that's quite exciting to me personally is the Adoption interaction! Now many many patches ago we introduced the Same-Sex marriage rule and ever since then it's just kind of been there and we've yet to introduce a way to actually make same-sex play… well, playable.  

### Who can adopt?​

Under the default game rules, Adoption is available to characters who are in a same-sex marriage, the childless and elderly/infertile, and Compassionate characters. Compassionate has long been a bit of a weak trait to have, so it's nice to give them a powerful way to secure succession and bring talented orphans into the family.  


![image-8.png](https://forumcontent.paradoxplaza.com/public/997645/image-8.png "image-8.png")



### Who can be adopted?​

Children can be adopted as long as: they're not a ruler, they're not in prison or otherwise unavailable, nobody in their family is a ruler, they're not already part of your house, and they're not in the realm of someone of their dynasty. This does mean you're technically allowed to adopt noble children, and children whose parents are still alive, but they are highly reluctant to accept adoption in those circumstances.  

![image-9.png](https://forumcontent.paradoxplaza.com/public/997646/image-9.png "image-9.png")


### Noble Adoption​

If you want to role-play a culture where adoption is commonplace (as it was in some off-map and out-of-period cultures), you can take up the Noble Adoption cultural tradition!  

![image-10.png](https://forumcontent.paradoxplaza.com/public/997647/image-10.png "image-10.png")


### Hold on a minute, isn't this anachronistic?​

Sort of! While adoption amongst nobility was exceptionally rare, it wasn't completely unheard of. As such, we've restricted access to adoption quite a lot as described and the AI is quite reluctant to do it.  

### Can the restrictions be loosened?​

Absolutely! Adoption comes with three new game rules that can forbid it or make it easier!  


![image-11.png](https://forumcontent.paradoxplaza.com/public/997648/image-11.png "image-11.png")


![image-12.png](https://forumcontent.paradoxplaza.com/public/997649/image-12.png "image-12.png")


![image-13.png](https://forumcontent.paradoxplaza.com/public/997650/image-13.png "image-13.png")


### ​

Just like the Eccentric trait, Adoption is part of the free update releasing with Wards & Wardens on August 22nd. Next week we will talk about the new Court position and share more details on what to expect from this event pack. See you then!

<!-- artifact:reactions:start -->
- 131 Like
- 39 Love
- 15 (unlabeled — rendered as base64 data URI)
- 10 (unlabeled — rendered as base64 data URI)
- 8 (unlabeled — rendered as base64 data URI)
- 2 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Meka66](https://forum.paradoxplaza.com/forum/members/meka66.1470167/)**
Role: CK3 Game Design
Badges: 100
Messages: 399
Reaction score: 13,781

*[Full game-badge icon list of 5 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
