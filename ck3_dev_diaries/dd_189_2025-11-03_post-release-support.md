---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1866461/"
forum_thread_id: 1866461
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 189
title: "Dev Diary #189 - Post-Release Support"
dd_date: 2025-11-03
author_handle: rageair
expansion: All Under Heaven
patch: null
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1618
inline_image_count: 16
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1866461'
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
    location: raw_lines_326_to_331
    action: preserved_and_flagged
    counts:
      Like: 92
      Love: 41
      (unlabeled — rendered as base64 data URI): 2
      Haha: 1
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_339_to_423
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_424_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Dev Diary #189 - Post-Release Support

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Nov 3, 2025](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-189-post-release-support.1866461/)
<!-- artifact:thread_metadata:end -->

Greetings everyone, [@rageair](https://forum.paradoxplaza.com/forum/members/375731/) and [@egghorse](https://forum.paradoxplaza.com/forum/members/1672622/) here!  

It’s been almost a week since All Under Heaven went live, and it’s really humbling to see how many of you are playing - and we’ve been having a blast following your reactions and reading your comments! We’ve also seen plenty of suggestions, requests and inspiring mods from the community in the past few days, which made us want to shed some light on our post-release plans for All Under Heaven.  

Last Thursday, we launched the first post-release patch for All Under Heaven (you can see the changelog for Update 1.18.0.1 [here](https://forum.paradoxplaza.com/forum/threads/update-1-18-0-1.1865285/)), where we tackled a few key issues such as crashes. I’m happy to report that this was the first of many more to come. Let’s take a look at what we’re currently working on!  

Update 1.18.0.2 (upcoming minor update)  

Update 1.18.0.2 is releasing tomorrow on Steam, with a grab bag of bugfixes, crash fixes, balance changes and improvements to databases. The full changelog will be released alongside the update itself, but for now we want to cover some highlights from this update as well as the updates still to come.  

Family members not enthused about their studies  

We’ve seen many players report that your immediate family is a bit hard to wrangle when it comes to getting their credentials. To make this less frustrating, we’ve added a decision called “Command Family to take Exams,” which will be available to House Heads. Taking this decision will make your unlanded family members independently go to local exams (if they need to pass the local exam) and Capital Exams (if they need to pass the Metropolitan or Palace exam) without the need for you to take them there. As long as they are within the same top realm as you, they will create their own travels, and you will be notified via Feed Message if they pass. Additionally, when playing as a Governor in a realm with Merit, courtiers will now always move to your new location when you gain or lose a title; If a courtier gets 'lost' in a location they should not be in, they'll return within a year.  

Improvements to Celestial Government  

A few balance changes have been made to address ongoing frustrations when playing in China:  


- Removed the MaA Maintenance and Army maintenance penalties imposed by the Dynastic Cycle on the Huangdi; the Celestial government already had increased maintenance from the Treasury defines, and didn't need more. This should make China more resistant to going bankrupt during revolts.
- Removed some excessive men_at_arms_cap modifiers from the Celestial government, as this is handled through the Army Command Structure laws instead.
- The Grand Campaign war will no longer result in China gaining additional tributaries. Instead, it will always give contested titles directly to the Hegemon.
- The Chinese Emperor will now be able to use the “Consolidation” CB on within these De Jure Empires: Zhongyuan, Jingyang, Lingnan, Liangyi and Yongliang (with the exception of the De Jure Kingdoms of Xia, Hexi, Dali and Viet - we don’t want Song to immediately fight Xia in 1066) regardless of the era the Dynastic Cycle is in.
- The Hegemon can now reject tributary missions in the event where they come bearing tribute. This allows you to not get tributaries sworn to you that you do not want (for example if you’d rather attack them).
We are also continuing to improve our databases and localization based on player feedback we’ve been receiving since Tuesday. For example, consorts of the Chinese Hegemon should now be correctly called Húanghòu, if female, or Húangfū, respectively, if male.  

If a fix you’ve been waiting for is not included in 1.18.0.2, it’s very likely that it will be part of the larger updates coming soon, such as 1.18.1. Oftentimes, if it’s a tricky bug to solve, we need more time to test to ensure we haven’t broken other things in the process. Content that requires new localization also needs a bit of time in the oven to be translated!  

That said, we will also have a few slightly bigger patches for *All Under Heaven* coming out in the next few weeks. What is and isn’t included in these patches is, of course, subject to change - we keep an eye on community sentiment, suggestions and bug reports, and try to juggle between severity, impact, and risk.  

Update 1.18.1  

We’re planning for update 1.18.1 to go live sometime next week. As usual, the changelog will be available once the update rolls out, but we’ll try to give you a sneak peek in the section below.  
Some visual improvements will be coming to South East Asia, with several new headwear pieces and clothing being added. In total, we will be adding 4 clothes, 7 hairstyles and 4 headgears.  

![](http:// "")

![image_01.png](https://forumcontent.paradoxplaza.com/public/1387419/image_01.png "image_01.png")


![](http:// "")


![](http:// "")

![image_02.png](https://forumcontent.paradoxplaza.com/public/1387420/image_02.png "image_02.png")


![](http:// "")


![image_03.png](https://forumcontent.paradoxplaza.com/public/1387421/image_03.png "image_03.png")


![](http:// "")


![](http:// "")

![image_04.png](https://forumcontent.paradoxplaza.com/public/1387422/image_04.png "image_04.png")


![](http:// "")


![](http:// "")

![image_05.png](https://forumcontent.paradoxplaza.com/public/1387423/image_05.png "image_05.png")



![image_06.png](https://forumcontent.paradoxplaza.com/public/1387424/image_06.png "image_06.png")



![image_07.png](https://forumcontent.paradoxplaza.com/public/1387425/image_07.png "image_07.png")



![image_08.png](https://forumcontent.paradoxplaza.com/public/1387426/image_08.png "image_08.png")


*[Some examples of hairstyles and headgear being added to Southeast Asia.]*  

For a small touch of realism, we’re also adding blendshapes for long ears.  

![](http:// "")

![image_09.png](https://forumcontent.paradoxplaza.com/public/1387429/image_09.png "image_09.png")


*[Screenshots of the new long ear blendshapes in Southeast Asia.]*  

Here’s also a work-in-progress screenshot of something one of our character artists is working on for Japan: a new mask for Disfigured characters.  

![](http:// "")

![image_10.png](https://forumcontent.paradoxplaza.com/public/1387430/image_10.png "image_10.png")


*[A work-in-progress screenshot of a Japanese mask.]*  

Our character art team is also looking at improving character lighting, as we’ve gotten reports of it looking vastly different (and not necessarily better) on various machines.  

This update is also adding various fixes to the map and terrain: shoreline fixes, making sure all lakes have water where they should, adjustments to the heightmap etc.  


![](http:// "")


![image_11.png](https://forumcontent.paradoxplaza.com/public/1387431/image_11.png "image_11.png")


*[Bugfix: Rotated Heian-Kyo city and added the Palace model to it.]*  

Our environment team has also been trying to add a bit more mood to the Chinese courtroom. Based on community feedback, the team has added more candles and carpets, pillars and drapes. The imperial tent has also been updated.  

![](http:// "")

![image_12.png](https://forumcontent.paradoxplaza.com/public/1387432/image_12.png "image_12.png")


*[Updated lighting in the Chinese Royal Court.]*  

This update also includes a few minor interface fixes. For example, House Relation icons have been added to the House Coat-of-Arms to improve usability:  

![](http:// "")

![image_13.jpeg](https://forumcontent.paradoxplaza.com/public/1387433/image_13.jpeg "image_13.jpeg")


*[House Relation icon on the House CoA.]*  

A new Legend skin for Asia has been added to improve flavor and consistency:  

![](http:// "")

![image_14.jpeg](https://forumcontent.paradoxplaza.com/public/1387434/image_14.jpeg "image_14.jpeg")


*[New Legend Chronicle skin.]*  

We’re also adjusting the AI to better utilize Legends.  

Besides updates from our artists, we also have some new bits of content. Below you can see a new decision to “Found a Ryukyuan Empire” which you’ll be able to try out in 1.18.1. For our world conquest enthusiasts, the decision to establish a Ryukyuan Empire presents a formidable challenge due to its Realm Size requirements. However, we all know this was your destiny to begin with if you choose to play as a Ryukyuan! You will also get to choose a family heirloom as a reward to solidify your achievement of showing the world the power of the Three Mountains.  

![](http:// "")

![image_15.png](https://forumcontent.paradoxplaza.com/public/1387435/image_15.png "image_15.png")


*[Screenshot of the “Found a Ryukyuan Empire” decision.]*  

We’ve also added a decision to “Found the Siam Kingdom,” which is meant to represent the Tai people's ambition to unite under a single banner after their flight to the southern lands.  

![](http:// "")

![image_16.png](https://forumcontent.paradoxplaza.com/public/1387436/image_16.png "image_16.png")


*[Screenshot of the “Found the Siam Kingdom” decision.]*  

Update 1.18.2  

Closer to the end of November, we plan to release another update: 1.18.2. One of the main focuses, next to a batch of bugfixes, will be improving gameplay as a Minister, adding content variation to that playstyle.  

Further Updates  

We plan to continue addressing bugs in *All Under Heaven* beyond the updates shared above. You shouldn’t be surprised if you see a smaller patch drop in-between or after the ones already listed.  

If you want to know more about the post-release process generally works for us at Paradox Black, Trinexx did an excellent job at describing how our post-release support process usually works a few dev diaries ago, back in May when we released Khans of the Steppe: [Dev Diary #171 - Post-Release Support](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-171-post-release-support.1755412/).  

Stay tuned for the coming updates!

<!-- artifact:reactions:start -->
- 92 Like
- 41 Love
- 5 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
- 1 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)**
Role: CK3 Game Director
Badges: 43
Reaction score: 11,829

*[Full game-badge icon list of 22 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
