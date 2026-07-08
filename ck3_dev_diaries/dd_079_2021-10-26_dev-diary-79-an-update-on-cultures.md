---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1495786/"
forum_thread_id: 1495786
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 79
title: "CK3 Dev Diary #79 - An Update on Cultures"
dd_date: 2021-10-26
author_handle: Servancour
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 948
inline_image_count: 4
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1495786'
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
    location: raw_lines_~28_to_162
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_161
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1754.jpg?1635253594
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_164_to_166
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_214_to_219
    action: preserved_and_flagged
    counts:
      Like: 156
      Love: 56
      (unlabeled — rendered as base64 data URI): 4
      Haha: 2
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_227_to_337
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_338_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1754.jpg?1635253594)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #79 - An Update on Cultures

<!-- artifact:thread_metadata:start -->
- Thread starter [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)
- Start date [Oct 26, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-79-an-update-on-cultures.1495786/)
<!-- artifact:thread_metadata:end -->

Greetings!  

We’ve talked plenty about cultures already at this point, but I wanted to give you a brief update on what we’ve done since the initial reveal of the culture rework. Since then, we’ve taken some time to add additional functionality based on your feedback!  

Previously, you could only add new traditions to a culture to fill out any empty tradition slots you may have. If you wanted to change anything regarding your culture, you would have to create a new one. Which begs the question. What if I want to keep the culture I already have? Or why can I not replace that one tradition to make my culture perfect? Fret not. The cultural head has gained the ability to change, or ‘reform’ if you will, their culture in order to change it without the need to create a new culture. The cultural head cannot replace everything mind you, but may change the ethos, the martial custom, and any tradition. If you want to change any of the remaining pillars you’ll have to create a new culture, either by diverging or forming a hybrid. Do note that you need to own the Royal Court expansion to reform your culture, similar to creating a culture. Even without the DLC, you can always add new traditions to fill out any empty slots.  

Reasoning for what you are able to change this way is twofold. First, changing heritage or language for an existing culture felt a bit off. While a language in reality does evolve over time, that is something we don’t really represent in the game, which makes it weird to simply “replace” a language. And you can’t really change your heritage in the same vein as, say, a tradition. Secondly, we wanted to make sure that you still have a valid reason to create a divergent culture. The two approaches are slightly similar in functionality, but it is important that both reforming and diverging a culture serves different purposes and that the distinction between the two is clear.  

![01_reform_button.jpg](https://forumcontent.paradoxplaza.com/public/755549/01_reform_button.jpg "01_reform_button.jpg")


*[Image showing the options to reform or diverge a culture]*​


The major difference is, as mentioned above, that reforming only allows you to change certain aspects about a culture, while diverging allows for additional possibilities. A second significant difference is the cost. Replacing a pillar will cost you prestige. The ethos in particular includes a rather hefty prestige cost that should make it rather difficult to repeatedly change it over the course of a campaign. You are, however, free to pick any ethos, regardless of circumstances.  

![02_replace_ethos.jpg](https://forumcontent.paradoxplaza.com/public/755550/02_replace_ethos.jpg "02_replace_ethos.jpg")


*[Image of the ethos replacement window]*​


Traditions will also be more expensive to replace. Instead of just a flat increase, replacing a tradition increases the prestige cost by 50%. The cost penalty will therefore be relative to how well your culture matches any given tradition, making the additional cost more harsh for already expensive (and less compatible) traditions.  

![03_replace_tradition_cost.jpg](https://forumcontent.paradoxplaza.com/public/755551/03_replace_tradition_cost.jpg "03_replace_tradition_cost.jpg")


*[Image showing the prestige cost for the Agrarian tradition when replacing a tradition]*​


These additional costs will make reforming or diverging your culture easier or more difficult depending on your situation. Attempting to diverge from a large and unified culture, such as Greek when playing as the Byzantine emperor, will be rather expensive and the less viable option. Especially if you only want to change a tradition or two. Reforming your culture will be cheaper, allowing you to more easily tweak your culture over time.  

If you are playing as the cultural head of a widely spread culture, such as Andalusian, diverging might instead be your preferred solution. Diverging from a culture that is spread out across multiple realms is significantly cheaper, allowing you to instead spend the prestige on replacing additional traditions or save it for something else entirely. Changing pillars is, for example, free when diverging, since you are forced to change at least one pillar in order to be able to create your new culture.  

Finally, you might have noticed the hourglass in the above screenshots. This is the establishment rate. Whenever you add or replace a tradition, or change a pillar, it will take some time before the change is applied. The time required for a change to be fully adopted mainly depends on your culture’s size. Larger cultures will logically gravitate towards a slower establishment rate. The duration is also increased whenever you replace an existing tradition. As such, adding a completely new tradition to your culture is not only cheaper, but it will go faster as well. This is important because you may only have one cultural change pending at any given time. If you replace a tradition with something else, you will have to wait until that tradition has been fully adopted before you can change your culture again. Diverging, on the other hand, still allows you to do sweeping changes and they take effect immediately as you create a new culture.  

![04_establish_time.jpg](https://forumcontent.paradoxplaza.com/public/755552/04_establish_time.jpg "04_establish_time.jpg")


*[Image of the establishment rate tooltip]*​


That about sums up all of the additional changes we’ve done. In short, the ambition here is to allow you to shape your culture more freely in the way you want, without having to always resort to doing something that might feel a bit heavy handed. On a final note, I’d like to thank you for providing us with feedback and voicing your opinions! Giving valid and constructive criticism does, at times, pay off.

<!-- artifact:reactions:start -->
- 156 Like
- 56 Love
- 24 (unlabeled — rendered as base64 data URI)
- 15 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
- 2 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)**
Role: Game Designer
Badges: 4
Reaction score: 9,949

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
