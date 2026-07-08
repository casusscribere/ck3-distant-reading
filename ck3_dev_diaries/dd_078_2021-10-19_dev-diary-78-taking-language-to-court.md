---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1495106/"
forum_thread_id: 1495106
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 78
title: "CK3 Dev Diary #78: Taking Language to Court"
dd_date: 2021-10-19
author_handle: Mrop
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1223
inline_image_count: 9
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1495106'
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
    location: raw_lines_~28_to_146
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_145
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1745.jpg?1634632276
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_249_to_253
    action: preserved_and_flagged
    counts:
      Like: 141
      Love: 55
      (unlabeled — rendered as base64 data URI): 5
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_261_to_371
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_372_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1745.jpg?1634632276)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #78: Taking Language to Court

<!-- artifact:thread_metadata:start -->
- Thread starter [Mrop](https://forum.paradoxplaza.com/forum/members/mrop.638192/)
- Start date [Oct 19, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-78-taking-language-to-court.1495106/)
<!-- artifact:thread_metadata:end -->

Hello there, and welcome to the 78th CK3 Dev Diary!  

I am Mrop, one of the User Experience Designers on CK3. [Last dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-77-becoming-a-polyglot.1494388/), we had a look at languages your Character can learn on their own. Today, we are having a look at how language relates to your Royal Court: Your Court Language.  

## Court Language in History​

Historically, it was not always so that nobles spoke the same language as the commoners. Rather, it was seen as more prestigious to speak another country’s language to show that you were cultivated enough to suck up to your superiors.  

One of the most well known examples of this is how French was spoken across many courts across Europe around the reign of Louis XIV. This is outside the timeframe of Crusader Kings, but there are earlier examples; Norman nobles who invaded England together with William the Conqueror continued to speak French, influencing the development of the English language as we know it today.  

## Court Language and Grandeur​

Each Ruler with a Royal Court has a language chosen as their Court Language. At the start of the game this is determined by what historically was used. If you get a Royal Court later, its Court Language will simply be your native language. You can, of course, choose to change it!  

Each language you can pick as your Court Language changes the Court Grandeur Baseline. You may recall that Grandeur and this Baseline was explained in [Dev Diary 61](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/). As a refresher, your Court Grandeur measures how impressive your Royal Court is. Each month, it moves slowly towards the Baseline value. Changing your Court Language will therefore take time to actually have an effect on your court’s Grandeur.  


![The button to change your Court Language is located in your Royal Court](https://forumcontent.paradoxplaza.com/public/753642/1 Grandeur.jpg "The button to change your Court Language is located in your Royal Court")



So how much Grandeur can you get from a certain Court Language?  

The largest share of Court Grandeur comes from the pecking order of all Royal Courts who speak that language.  

The Royal Court with the highest Court Grandeur is considered the “leader” of that language, and gains Court Grandeur based on how many Royal Courts speak that language. So if you are the leader of a language, you want as many Courts as possible to adopt it! Naturally, you only gain this Grandeur if you can actually speak the language!  

On the other hand, if you are not the grandest Court of the language, you gain Court Grandeur based on the difference of your Grandeur, and the Grandeur of the leading Court. Speaking the Language is not required for this bonus, so even if your neighbors have a language you cannot speak you can attempt to impress them by following their lead.  

In addition to this pecking order, you also gain Grandeur for each County in your Realm that speaks your Court Language, but only if you know the language personally. Finally, if your Court Language is also your native Language, you gain an extra 25% bonus to all the impacts your Court Language has on your Court Grandeur.  

Here is an example of a calculation for having your native Language as Court Language (actual values are very much temporary):  

![An example calculation of Court Grandeur gained from your Court Language](https://forumcontent.paradoxplaza.com/public/753643/1b Grandeur TT.png "An example calculation of Court Grandeur gained from your Court Language")



Since you gain extra Grandeur for matching your Court Language with your native Language, you may want to create a new Hybrid or Divergent Culture (as described in [Dev Diary 65](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/)) to adapt to the language your Realm or Court prefers.  

All in all, this means that weaker and less grand Royal Courts will tend to choose the Court Language of a local, more grand Royal Court. The AI is also more restricted than players, such as taking the Faith of the speakers of the Court Language into account.  

Eventually, once your Royal Court becomes grand enough, it is usually time to choose a language of your own as the Court Language, and start attracting lesser Courts to adopt it.  

## Finding Court Language in the Game​

You can, as shown above, select your Court Language inside your Royal Court, which takes you to a special map mode of all Court Languages in the world.  

![A special Map Mode showing all Court Languages of the World](https://forumcontent.paradoxplaza.com/public/753644/2 Lang Map.png "A special Map Mode showing all Court Languages of the World")



You can also directly adopt the language of a certain Culture by clicking on the button next to the language in that Cultures own View.  

![You can directly adopt a Language as a Court Language in the Culture View](https://forumcontent.paradoxplaza.com/public/753649/4 Language in Culture View.jpg "You can directly adopt a Language as a Court Language in the Culture View")



Beware however, not everyone may speak your Court Language that well (including yourself), so the threat of embarrassment is ever present. Just like in real life.  

![An embarrassing situation occurs when one of your Vassals cannot speak your Court Language](https://forumcontent.paradoxplaza.com/public/753666/4b Event.png "An embarrassing situation occurs when one of your Vassals cannot speak your Court Language")


## Court Language Spread​


Seeing your Court Language spread is one major way to understand how influential your court becomes over the years.  

To see Court Languages spread, let us have a look at the game! Here, each Royal Court that speaks the same Court Language is shown on the map.  

Here is the map at game start in 867 AD. You can see languages such as Arabic being used in the Habbari Sultanate (roughly in modern day Pakistan), and how the king of Bulgaria has chosen Greek due to the influence of nearby Byzantium.  

![Court Languages Map in 867](https://forumcontent.paradoxplaza.com/public/753654/5 867.png "Court Languages Map in 867")



100 years later, Magadhan is slowly becoming more popular in India, and the Kingdom of Italy have adopted French as their Court Language.  

![Court Languages Map in 967](https://forumcontent.paradoxplaza.com/public/753655/6 967.png "Court Languages Map in 967")



In 1067, a century later, Greek is spreading to the newly formed Kingdoms in the Empire of Khazaria. Some new languages like Berber also pop up.  

![Court Languages Map in 1067](https://forumcontent.paradoxplaza.com/public/753656/7 1067.png "Court Languages Map in 1067")



Finally, in 1167, we see four languages dominate the courts of the world. Greek has spread through the now shattered Empire of Khazaria, and is also making its way down to Africa. At the same time, there is still room for smaller Court Languages like Shaz Turkic to thrive.  

![Court Languages Map in 1167](https://forumcontent.paradoxplaza.com/public/753657/8 1167.png "Court Languages Map in 1167")



That is all for now; thank you for reading!

<!-- artifact:reactions:start -->
- 141 Like
- 55 Love
- 16 (unlabeled — rendered as base64 data URI)
- 7 (unlabeled — rendered as base64 data URI)
- 5 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Mrop](https://forum.paradoxplaza.com/forum/members/mrop.638192/)**
Role: good with computer
Badges: 61
Messages: 255
Reaction score: 1,291

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
