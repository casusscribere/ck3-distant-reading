---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1382730/"
forum_thread_id: 1382730
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 23
title: "CK3 - Dev Diary #23 - Holy Orders"
dd_date: 2020-04-21
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
body_word_count: 891
inline_image_count: 7
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1382730'
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
    location: raw_lines_212_to_214
    action: preserved_and_flagged
    counts:
      Like: 12
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 1 of 3 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_222_to_292
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_293_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 - Dev Diary #23 - Holy Orders

<!-- artifact:thread_metadata:start -->
- Thread starter [Heptopus](https://forum.paradoxplaza.com/forum/members/heptopus.1269016/)
- Start date [Apr 21, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-23-holy-orders.1382730/)
<!-- artifact:thread_metadata:end -->

Hello everyone, I’m back with some spicy information about Holy Orders in Crusader Kings III!  

Let’s start off with some general information: a Holy Order is an independent military organization that fights to defend and expand the influence of their faith; their first and foremost loyalty in the game will be to their god/s. If you read the [earlier dev diary about mercenaries](https://forum.paradoxplaza.com/forum/index.php?threads/ck3-dev-diary-18-men-at-arms-mercenaries-and-cbs.1357939/) you will notice that Holy Orders have a lot in common with them: succession, being a Title with a Court, etc. However, unlike mercenaries the members have dedicated their lives to a higher purpose than that of the pursuit of gold. Very noble!  

![grandmaster.png](https://forumcontent.paradoxplaza.com/public/557031/grandmaster.png "grandmaster.png")



Much like in CK2 you will be able to hire Holy Orders to help you out in religious wars, but unlike in CK2 they will fight all enemies once hired. A thing to keep in mind, however, is that Holy Orders are dismissed as soon as you’re no longer at war with someone of another faith, so make sure to really time those wars right!  

![military_view.png](https://forumcontent.paradoxplaza.com/public/557033/military_view.png "military_view.png")



Aside from ordinary levies a Holy Order also has a number of MaA regiments that are special for Holy Orders (based on Religion and not Faith), e.g. “Order Knights”. These regiments will work as regular MaAs and have a type, specified terrain effects, etc. They are truly a force fighting for the good of your faith! Or, of course, a scary opponent to face on the battlefield...  

You can only ever hire a single Holy Order, but if you are the patron of an order (more on this further down) it costs nothing to rope them into your religious conflicts. Ha, who needs mercenaries? **And**, unlike mercenaries, they will stick around with no time limit; no 3-year contracts!  

If you are a King or an Emperor, and have a pile of gold and a big chunk of piety, you can found a new Holy Order in your realm by leasing a valid Holding (Castle or City) to the order.  

![holy_order_founded.png](https://forumcontent.paradoxplaza.com/public/557032/holy_order_founded.png "holy_order_founded.png")



This initial Holding granted to the Holy Order will be the basis for the Holy Order’s Levies and Taxes – their Headquarters if you will. You can only create one Holy Order, but you can still end up being the patron of several, for example by taking over land where a Holy Order of your faith has their Headquarters.  

The Headquarters is the stronghold of the Holy Order, and the first King or Emperor upwards in the liege hierarchy is their formal patron, i.e. the one that can use them for free in wars. The patron must, of course, be of the same faith as the Holy Order. However, if there is no ruler of sufficient rank around to patron the Holy Order it is self-sufficient enough to still function!  

![county_view.png](https://forumcontent.paradoxplaza.com/public/557035/county_view.png "county_view.png")



If a Holy Order’s Headquarters is lost another Holding will be selected to fill the role, with a preference for Holdings within the current patron’s realm. But, if the Holy Order has no more holdings the Holy Order is disbanded. Keeping this in mind it’s understandable that the Grandmaster/Grandmistress will take all opportunities they see to get hold of more land…  

After founding a Holy Order you might see some events, much like in Ck2, where the order can gain more Holdings in many Realms. And yes, these events do often involve loans and threats of godly wrath.  

![repay_loan.png](https://forumcontent.paradoxplaza.com/public/557034/repay_loan.png "repay_loan.png")



The Holy Order can also try to expand their forces if they spy a fitting candidate. After all, it is hard to fight heretics without enough warriors!  

![request_child.png](https://forumcontent.paradoxplaza.com/public/557029/request_child.png "request_child.png")



However, we all know that Holy Orders also have a secondary function: to stash your worthless fourth son somewhere where he can’t cause any trouble. You can ask almost all your courtiers to take vows, and depending on your gender doctrines, and the existence of a Holy Order in your faith, they will either be sent to fight for your faith or to become part of the clergy.  

![ask_take_vows.png](https://forumcontent.paradoxplaza.com/public/557030/ask_take_vows.png "ask_take_vows.png")



If you no longer see the need to keep a Holy Order around, or if you *really* need that Holding for something else, you can revoke a Holy Order’s lease to kick them from your land. This will, of course, make both the Grandmaster/Grandmistress and the Head of Faith (if one exists) less than pleased with you.  

I hope you are as excited as I am to see Holy Orders in the game! Or, I’m excited to see them crop up in my faith, not my enemies’... Anyhow, that’s all I have for now. Thank you for reading!  

Next week we will continue the religious theme; stay tuned for both heresies and doctrines!

 

Last edited: Apr 21, 2020

<!-- artifact:reactions:start -->
- 12 Like
- 3 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Heptopus](https://forum.paradoxplaza.com/forum/members/heptopus.1269016/)**
Role: Content Designer
Badges: 2
Messages: 47
Reaction score: 917

*[Full game-badge icon list of 10 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
