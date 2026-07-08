---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1861099/"
forum_thread_id: 1861099
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 185
title: "Dev Diary #185 - Playing in China, Japan, and Angkor"
dd_date: 2025-09-30
author_handle: PDX-Trinexx
expansion: All Under Heaven
patch: null
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 11950
inline_image_count: 138
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1861099'
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
    location: raw_lines_1245_to_1249
    action: preserved_and_flagged
    counts:
      Like: 85
      Love: 31
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_1257_to_1369
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_1370_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Dev Diary #185 - Playing in China, Japan, and Angkor

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)
- Start date [Sep 30, 2025](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-185-playing-in-china-japan-and-angkor.1861099/)
<!-- artifact:thread_metadata:end -->

Hello everyone! Today’s dev diary will be a slightly unusual one; while China, Japan, and Southeast Asia have received dedicated dev diaries already, there were enough information gaps in them and unanswered questions from players that we felt the need to revisit them. Simultaneously, we wanted to give players a better understanding of how everything in All Under Heaven actually fits together and interacts when you play it.  

To that end, today’s dev diary will consist of three playthroughs: China in 1066, Japan in 1066, and Angkor in 867. We’ll guide you through the life of a single character in each of these regions, highlighting features that make them mechanically distinct from each other, as well as how these systems interact with the existing core gameplay loop that players are already familiar with.  

One note before we dive in: all character portraits shown in this dev diary are from an older build. After processing significant community feedback, we made some adjustments to the ethnicities of Asian characters. While these changes aren’t in the build we’re displaying in this dev diary, we do have an image showing 20 randomly generated characters using these new ethnicity parameters. While these parameters are still being tweaked, we wanted to let players see the progress that’s being made in that area already.  

![image_01.png](https://forumcontent.paradoxplaza.com/public/1365595/image_01.png "image_01.png")


*[Randomly generated Han Chinese portraits, after adjustment]*  

In addition to that, the usual caveat applies here as well: Everything you see is **under development, numbers are not final, content is subject to change**, and so forth.  



---

### China, 1066​

Before we can begin our first playthrough, we need to go over the circumstances that will be driving most of this campaign.  

We’ll be starting from our new 1066 bookmark, *Song of Splendor*. At this point in time the Tang Dynasty has been gone for nearly two centuries, and the Song Dynasty is approaching the peak of its glory.  

![image_02.png](https://forumcontent.paradoxplaza.com/public/1365596/image_02.png "image_02.png")


*[Song of Splendor, a new 1066 Bookmark focusing on the Song Dynasty]*  

In order to focus on the Minister circuit gameplay and to drive a classic rags-to-riches story, we’ll be playing as Qin Guan. He’s relatively young as far as nobles go, which should allow us plenty of time to focus on advancing through the ranks as a single character.  

![image_03.png](https://forumcontent.paradoxplaza.com/public/1365597/image_03.png "image_03.png")


*[Qin Guan, one of the highlighted characters in this bookmark]*  

The Dynastic Cycle at this stage is currently in an Advancement Era, with the Song focusing on internal affairs and stability. While we can interfere with this and push the Cycle towards an era of our choosing, we’re currently not part of a political movement. We’ll remain Unaligned for now until we have a better feel for how the political situation is evolving.  

![image_04.png](https://forumcontent.paradoxplaza.com/public/1365598/image_04.png "image_04.png")


*[A situation overview event is shown when starting as a character involved with the Dynastic Cycle]*  

Upon starting our campaign, we get the option to focus our character on either Merit or Influence. With our family consisting of only three people and headed up by a 17 year old, we’re in no position to wield any serious influence within the empire. As such, we’re going to focus on Merit for the time being.  

![image_05.png](https://forumcontent.paradoxplaza.com/public/1365599/image_05.png "image_05.png")


![image_06.png](https://forumcontent.paradoxplaza.com/public/1365600/image_06.png "image_06.png")


*[Choosing the top option here gives us the Focusing on Merit modifier, which improves our experience gain in the Confucian Education trait]*  

In classic Crusader Kings III tradition, we also need to find a spouse as quickly as possible. Given our precarious position, we’ll opt to marry into a stronger family. In this case: The Lu family, which is headed up by Grand Marshal Lu Gongbì. Gongbì has an unwed granddaughter, so by marrying her we can build a stronger relationship between Houses Qin and Lu.  

![image_07.png](https://forumcontent.paradoxplaza.com/public/1365601/image_07.png "image_07.png")


*[This marriage improves House Relation between our houses by 10%]*  

We also gain a bit of prestige from this marriage. With our bachelor status officially revoked, we can begin focusing on the Important Stuff; namely, attending a civil exam so we can distinguish ourselves.  

![image_08.png](https://forumcontent.paradoxplaza.com/public/1365602/image_08.png "image_08.png")


*[The state of the Chinese Empire at this point of our campaign]*  

From the Current Situation tab we can see that we have a few options available to us right out of the gate. We can send our two brothers off to the Children’s Examination to kickstart their own careers, and we can also focus on studying Confucian Classics to improve our chances in our own exams when they come up.  

![image_09.png](https://forumcontent.paradoxplaza.com/public/1365603/image_09.png "image_09.png")


*[Studying Confucian Classics should improve our odds of standing out when we take our exams down the line]*  

Sending our brothers off to take their exams will cost us a bit of the precious little influence we have at this point, but it’s well worth it to increase the chances of our family being granted positions in the future.  

![image_10.png](https://forumcontent.paradoxplaza.com/public/1365604/image_10.png "image_10.png")


*[With a 62% chance of failure, we’re unlikely to get a good return on this investment. This is the same logic my own parents used when deciding not to start a college fund for me.]*  

Qín Gòu passes his examination easily enough, but Qín Dí fails. Win some, lose some. This is why you always have backup children! Or brothers. Or any loose family members you have lying around the place, really.  

![image_11.png](https://forumcontent.paradoxplaza.com/public/1365605/image_11.png "image_11.png")


![image_12.png](https://forumcontent.paradoxplaza.com/public/1365606/image_12.png "image_12.png")


*[Qín Dí? More like Qín Dísappointment!]*  

With the scions of our house sorted out for now, we can begin focusing on ourselves by studying Confucian Classics.  

![image_13.png](https://forumcontent.paradoxplaza.com/public/1365607/image_13.png "image_13.png")


*[Taking this Decision is the first step towards improving our odds in the exams]*  

The act of studying the classics is presented in All Under Heaven as a special scheme targeting yourself. As with most schemes, we’re immediately given the opportunity to decide how we approach it.  

![image_14.png](https://forumcontent.paradoxplaza.com/public/1365608/image_14.png "image_14.png")


*[Starting the scheme presents us with a few options right out of the gate]*  

We want to make ourselves a competitive candidate for any positions that open up as quickly as possible, so we’ll take scheme options that should speed up the process as a whole. We miss out on an improved success chance doing this, but speed is of the essence for our purposes.  

### Local Exams​

This ultimately ends up being irrelevant, however, as we’re promptly invited to attend an examination being held by Chen Ji, the current governor of Jinshang.  

![image_15.png](https://forumcontent.paradoxplaza.com/public/1365609/image_15.png "image_15.png")


*[We wanted to study first, dammit!]*  

The exam is being held relatively soon, so we’ll have to spend some extra money during the travel planning process to ensure we get there before it starts. By hiring a Caravan Master and paying for some Mercenary Guards, we manage to get the estimated arrival time under the start date for the examination.  

![image_16.png](https://forumcontent.paradoxplaza.com/public/1365610/image_16.png "image_16.png")


*[Travel planning screen for the Exam activity.]*  

We arrive at the Exam with four days to spare, and as the entrants gather we’re presented with an option to determine how we want to approach the exam: honorably, or pursuing success by any means.  

![image_17.png](https://forumcontent.paradoxplaza.com/public/1365611/image_17.png "image_17.png")


*[Opening event for the Examination activity]*  

We’re not left with many fallback options if we get disqualified, so we'll do things the proper way this time. This ultimately works out for us, as we pass with flying colors.  

![image_18.png](https://forumcontent.paradoxplaza.com/public/1365612/image_18.png "image_18.png")


![image_19.png](https://forumcontent.paradoxplaza.com/public/1365613/image_19.png "image_19.png")


*[The exam concludes.]*  

Passing our exam also grants us enough Merit to reach the 8th rank, as well as allowing us to potentially reach the 5th rank in the future. With this, we now qualify to hold County-level appointments within the empire.  

![image_20.png](https://forumcontent.paradoxplaza.com/public/1365614/image_20.png "image_20.png")


*[Each completed Civil Service Examination type increases your maximum Merit rank; exams are vital to progressing in your career!]*  

With our exam complete and us now qualifying for appointments, there’s nothing left to do but head back to our Estate in Jiangdu. Once we arrive, we can continue our Study scheme to prepare us for Capital Examinations down the line.  


#### Great Projects​

While we continue to focus on our Confucian education (reaching the 7th merit rank and qualifying for Duchy-tier appointments), we receive a notification that an Establish Control great project is being planned in Yunzhou. Four different contributions are required to begin the project proper, and three are immediately made by other families. Unfortunately, a military governorship is required to fill the only remaining contribution, Highway Patrols, so we do not get to participate in this particular project.  

![image_21.png](https://forumcontent.paradoxplaza.com/public/1365615/image_21.png "image_21.png")


*[Establish Control great project]*  

There’s also a Strengthen Capital project being planned in Bianzhou, but we don’t have money to participate in that one, so for now we’re stuck on the sidelines.  

![image_22.png](https://forumcontent.paradoxplaza.com/public/1365616/image_22.png "image_22.png")


*[Strengthen Capital great project]*  

While we can’t interact with these specific projects right now, there’s a steady stream of them being planned throughout the empire. A more established governor or intendant will have several opportunities to engage with this system.  

### Movement Debates​

While we focus on self-improvement, we’re invited to a debate being held by the Conservative Movement. We’re still Unaligned at this stage, but this could present a good opportunity to mingle and potentially increase our Confucian Education experience, so we’ll pack our bags and head for Kaifeng.  

![image_23.png](https://forumcontent.paradoxplaza.com/public/1365617/image_23.png "image_23.png")


*[Invitation to a Movement Debate]*  

We’re promptly informed that we’re not allowed to participate without belonging to a Movement, so we’re forced to decide which one to join in order to proceed with our plans.  

![image_24.png](https://forumcontent.paradoxplaza.com/public/1365620/image_24.png "image_24.png")


*[No grillers allowed.]*  

We consider the options available to us; each Movement has its own advantages and disadvantages to being a member. For this specific time and place, we decide that joining the Advancement Movement aligns closest with our goals.  

![image_25.png](https://forumcontent.paradoxplaza.com/public/1365621/image_25.png "image_25.png")


![image_26.png](https://forumcontent.paradoxplaza.com/public/1365622/image_26.png "image_26.png")


![image_27.png](https://forumcontent.paradoxplaza.com/public/1365623/image_27.png "image_27.png")


![image_28.png](https://forumcontent.paradoxplaza.com/public/1365624/image_28.png "image_28.png")


*[Each Movement has its own associated effects for members]*  

Arriving at the Debate, we’re given the choice between two possible activity Intents: Increase Movement Power, or Gain Elder. We’re not nearly influential enough to swing the scales by any meaningful degree, so instead we’ll focus on trying to find a mentor.  

![image_29.png](https://forumcontent.paradoxplaza.com/public/1365626/image_29.png "image_29.png")


*[Debate Intents]*  

The Debate itself is a power struggle between the existing leader of the Conservative Movement, and a potential upstart who wants to unseat them and take control of the Movement themselves. As the Debate progresses, the scale will move in favor of either the incumbent or the challenger.  

![image_30.png](https://forumcontent.paradoxplaza.com/public/1365627/image_30.png "image_30.png")


*[Debate Sentiment is visible between the Guest List button and our Intent. Currently it favors the incumbent.]*  

As we’ve picked up a ton of stress through incidental events, we’re opting to relax for this stage. Since we’re not members of the Conservative Movement, the result of this power struggle doesn’t particularly concern us.  

We’re presented with a chance to find a new mentor; after considering their skills compared to our existing mentor, we take the opportunity and enter the tutelage of Commandant Li Cān. Ultimately though, the debate is cancelled due to a war breaking out over a border dispute in Lingxi.  

![image_31.png](https://forumcontent.paradoxplaza.com/public/1365628/image_31.png "image_31.png")


*[The debate is cancelled]*  

With the Debate cancelled, we head back to our Estate.  

### Prefecture of Xinzhou​

Fortunately, we don’t have to wait very long. We’re granted the Prefecture of Xinzhou, and our career as a civil servant officially begins!  

![image_32.png](https://forumcontent.paradoxplaza.com/public/1365629/image_32.png "image_32.png")


*[The “Xinhzou” typo here is already fixed, but the fix wasn’t implemented yet in the build this dev diary was based on.]*  

Our new Prefecture is located a fair bit south from where our Estate is, and unfortunately we have a cultural mismatch with it. We’re of Han culture, but Xinzhou itself is currently Yao. This causes a popular Opinion malus with the county, but we can manage this for now.  

There’s also a religious mismatch, with us being of the Daoxue religion while our Prefecture is of Zhengyi, but this is less of a concern for now.  

![image_33.png](https://forumcontent.paradoxplaza.com/public/1365630/image_33.png "image_33.png")


![image_34.png](https://forumcontent.paradoxplaza.com/public/1365631/image_34.png "image_34.png")


*[Cultural and Faiths map of the immediate area.]*  

In any case, we now receive a Prefect’s salary and access to the Xinzhou treasury. Neither of these are enough for us to do anything right out of the gate, but we can leverage some of our influence to convince the Minister of Revenue to allocate additional funds to Xinzhou.  

![image_35.png](https://forumcontent.paradoxplaza.com/public/1365632/image_35.png "image_35.png")


*[Requesting Treasury Funds]*  

This money is earmarked specifically for state use, so it goes into Xinzhou’s treasury; we can’t use it for personal gain! With this influx of money, Xinzhou has enough cash to finance an upgrade to one of the buildings present in Shangrao. We’ll upgrade the Logging Camps, as it will grant additional tax income to the holding.  

![image_36.png](https://forumcontent.paradoxplaza.com/public/1365633/image_36.png "image_36.png")


*[Under Celestial government, Treasury is used to fund construction rather than personal gold]*  

While this is happening, our brother Qín Gòu comes of age and can be betrothed. Fortunately enough, it happens that Huángdì Zhào Shu has a sister in need of a betrothal. We make the arrangements for them to be wed when she comes of age, building a stronger relationship between our house and the imperial family itself.  

![image_37.png](https://forumcontent.paradoxplaza.com/public/1365634/image_37.png "image_37.png")


*[Qín Gòu is moving up in life; marrying a member of the imperial family will grant him significant prestige.]*  

Shortly after making marriage arrangements on our brother’s behalf, the first child of our own is born: a daughter. Better luck next time.  

More importantly, our first Governance Issue has presented itself: An escaped fugitive. We take the contract and travel to Yushan to resolve the problem.  

![image_38.png](https://forumcontent.paradoxplaza.com/public/1365635/image_38.png "image_38.png")


*[The Escaped Justice governance issue]*  

We quickly discover the fugitive upon our arrival, and are given the opportunity to offer him leniency or to banish him outright. The former would grant us Piety, but the latter improves our experience as a Governor. Easy enough choice for someone pursuing a career in civil service.  

![image_39.png](https://forumcontent.paradoxplaza.com/public/1365637/image_39.png "image_39.png")


*[Looks like you’re going to the Shadow Realm, Jimbo]*  

With the Governance Issue resolved and us having taken the first step down the Governor trait line, we head back to Shangrao.  

It’s now 1071 AD, and we decide it’s time for our character to begin finding his own Disciples. Given our current rank, we don’t have any particularly impressive options to choose from, so we nab whoever we can. Each Disciple gives us 30 Merit, so there’s no reason not to stay at our limit of five Disciples.  

![image_40.png](https://forumcontent.paradoxplaza.com/public/1365638/image_40.png "image_40.png")


*[Our personal disciples]*  

They’re a sorry lot, but Merit is Merit. Taking on these Disciples gives us enough Merit to move up to the 6th rank. Without taking the Capital Examination, we’re unable to progress any further. We’re also unable to take an Examination while serving as a Governor, so we’ll be staying at this rank for a while; we’re not ready to give up our appointment just yet.  

### A New Era​


More importantly, however: The Dynastic Cycle is dangerously close to shifting into the Tension era. The Huangdi isn’t hosting examinations, the treasury is bankrupt, and governors are embezzling left and right. The Era will be shifting sooner rather than later.  

![image_41.png](https://forumcontent.paradoxplaza.com/public/1365639/image_41.png "image_41.png")


*[Multiple Catalysts are impacting the Dynastic Cycle in quick succession]*  

It only takes a couple months from this point for the Dynastic Cycle to officially move into the Tension Era.  

![image_42.png](https://forumcontent.paradoxplaza.com/public/1365640/image_42.png "image_42.png")


*[The event declaring a new Era has been entered]*  

As we’re in a new Era, the benefits and drawbacks for each Political Movement have changed. We’re still determined to continue our civil service career however, so we will remain part of the Advancement Movement.  

![image_43.png](https://forumcontent.paradoxplaza.com/public/1365641/image_43.png "image_43.png")


*[Tension Era is not kind to Advancement Movement members]*  

Interestingly enough, the Huangdi calls for a Capital Examination shortly after the Era shift. While we were content to remain where we were previously, being in the Tension Era has changed our priorities.  

![image_44.png](https://forumcontent.paradoxplaza.com/public/1365642/image_44.png "image_44.png")


*[An invitation from the Huangdi to attend the Capital Examination]*  

We need to retire from our current appointment if we want to participate in the examination, and we absolutely want to participate in the examination. Goodbye Xinzhou; you were a lovely prefecture, but we have greater ambitions now. We can’t receive another appointment for three years after stepping down, but there’s no guarantee we’ll get another opportunity to take this exam any time soon.  

![image_45.png](https://forumcontent.paradoxplaza.com/public/1365643/image_45.png "image_45.png")


*[Landed governors cannot participate in examinations, so they are given the opportunity to retire when traveling to an Exam location]*  

The examination is far more competitive than the previous one, and we’re in a distant third place when we’re given the opportunity to impress the Huangdi himself with our essay. We’re given the choice of playing it safe for a set, but small, amount of Exam score, or aiming for a greater score at the risk of failing to gain any points with our essay.  

![image_46.png](https://forumcontent.paradoxplaza.com/public/1365644/image_46.png "image_46.png")


*[The Imperial Essay is a key moment during the Capital Examination]*  

We need to stand out and take whatever advantage we can get, so we take the risk. The gamble pays off, fortunately, and we end up with enough Exam Score to put us in second place. This result lifts the restriction on our merit rank outright, as well as grants us enough merit to immediately reach the 4th rank. We now qualify for Kingdom-tier appointments, and are one of the most highly-qualified candidates in the Empire.  

![image_47.png](https://forumcontent.paradoxplaza.com/public/1365648/image_47.png "image_47.png")


*[Completing the Capital Examination]*  

With no lands to govern and being locked out of appointments for the next three years, we settle into a pattern of managing our family’s Estate. As this system isn’t unique to All Under Heaven, we’ll skip over that for the sake of narrative pacing.  

During this time, our first son is born: Qín Yánqìng. He’s Quick as well, which is a lovely bonus.  

![image_48.png](https://forumcontent.paradoxplaza.com/public/1365649/image_48.png "image_48.png")


*[This baby is an awful governor, with a -50% modifier to his efficiency. Shameful behavior.]*  

After a few years, we’re offered a new appointment: Governor of Huaixi. Huaixi is a Duchy-tier appointment, and is located quite close to the capital. A fine appointment! The salary is also quite nice, but as a dedicated civil servant we’re not as concerned about that. Not even slightly. Honest.  

![image_49.png](https://forumcontent.paradoxplaza.com/public/1365650/image_49.png "image_49.png")


*[Becoming a Governor]*  

We quickly relocate our Estate to Huaixi’s capital prefecture of Shouzhou; we plan on being here for a while, so we should get settled in. We have a spare prefecture as well, so we appoint our brother Qín Gòu to oversee it while reporting to us.  

![image_50.png](https://forumcontent.paradoxplaza.com/public/1365670/image_50.png "image_50.png")


*[Qín Gòu: Prefect.]*  

Unfortunately, around this time a significant number of peasants begin to revolt against imperial governance.  

### The Peasant Uprising of 1075 AD​

50,000 angry farmers take up arms against the Huangdi. Peasant mobs rise up to the north, west, and south of us, forming a crescent of hostile armies around Huaixi.  

![image_51.png](https://forumcontent.paradoxplaza.com/public/1365671/image_51.png "image_51.png")


*[A substantial uprising]*  

While no peasants rise up within Huaixi proper, we do have a fairly large mob running riot in Shenzhou. Our own forces are quite limited, so we may not be able to repel them. Fortunately, this may become a non-issue for us, as Intendant Huáng Dàlín requests to take control of Huaixi’s military. We agree to his request, transferring command of our troops directly to him. This is now his problem to deal with.  

![image_52.png](https://forumcontent.paradoxplaza.com/public/1365672/image_52.png "image_52.png")


*[A request for additional troops]*  

Disparate mobs of angry farmers ultimately prove to be no match against the trained and coordinated power of a professional army, so the Huangdi’s forces quickly begin picking apart the rebels. The uprising is defeated almost as swiftly as it began, despite holding a 5:1 number advantage.  

![image_53.png](https://forumcontent.paradoxplaza.com/public/1365673/image_53.png "image_53.png")


*[A rebel regiment, shortly before having a very bad day]*  

Unfortunately, while this is happening, we discover that our beloved Lady Lu Zìróu has been unfaithful, and that her unborn child was sired by Intendant Chéng Yú. The stress of this revelation compounds on top of the stress of managing our governorship, on top of the stress of pursuing the highest merit rank we could.  

Everything compounds together, and the dam breaks. We’re unable to withstand the strain of it all, and our heart gives out.  

![image_54.png](https://forumcontent.paradoxplaza.com/public/1365674/image_54.png "image_54.png")


*[Stress-induced fatal heart attack]*  

Governor Qín Guan dies from a fatal heart attack on July 22nd, 1076 AD. An unceremonious end, but not an unexpected one considering the strain we put him under.  

In the ten years we lived as him, we rose from an obscure house on the brink of extinction through the ranks of civil service to become governor of an entire duchy. While we didn’t rise as far as we wanted, we achieved a lot in such a short span of time.  

House Qin is now headed by Qín Yánqìng, who is barely a toddler. Qín Gòu, who we positioned as a fallback option, has somehow come down with the Great Pox and is on the verge of death himself. Difficult times lie ahead for our house, certainly more difficult than the times we found ourselves in when we began this run.  

While we ultimately failed in our goal of positioning the Qín as a powerful and stable house within the Song Dynasty’s empire, we hope this playthrough gave you a better understanding of how life as a civil servant in the empire will play out in All Under Heaven.  


---

### Japan, 1066​

Our new 1066 Bookmark, *A Never-Waning Moon*, focuses on the Fujiwara family’s dominance over Japan. Since 858 AD, the Fujiwara have been regents of Japan ruling in the Emperor’s stead. More than 200 years after the first Fujiwara takes power, their family maintains an intricate web of bureaucracy that controls the fate of Japan.  

![image_55.png](https://forumcontent.paradoxplaza.com/public/1365675/image_55.png "image_55.png")


*[A Never-Waning Moon, a new 1066 bookmark focusing on Japan]*  

Japan during our time period was dominated by the centralized administrative-type Ritsuryo government, but slowly transitioned over the centuries to the more feudal-type Soryo government. To hasten this transition along, we’ll be playing as Kiyohara Takenori, one of the most powerful Soryo rulers in this start date.  

![image_56.png](https://forumcontent.paradoxplaza.com/public/1365676/image_56.png "image_56.png")


*[Kiyohara Takenori, one of the highlighted characters in this bookmark]*  

Japan’s political structure in All Under Heaven is based around the concept of House Blocs, which are nested alliances forming distinct political pseudo-entities within Japan. As a Soryo ruler, we’re less involved in the politicking of the Ritsuryo House Blocs, but we can’t afford to ignore the Ritsuryo entirely; their Blocs are powerful, and disregarding them can be a costly mistake. We also need to focus on developing and maintaining our own House Bloc to prevent the Ritsuryo from picking us off one-by-one.  

Upon starting, we’re given the opportunity to decide if we should focus our attention inward to our own land’s stability, or prepare for the eventuality of war with the Ritsuryo apparatus. Given that it's in the central government’s best interest to depose Soryo rulers wherever possible, we’ll be preparing for war.  

![image_57.png](https://forumcontent.paradoxplaza.com/public/1365677/image_57.png "image_57.png")


*[Deciding early on what our focus is]*  

Taking the political situation in at a glance is relatively easy, as Ritsuryo rulers have extremely restricted domain limits. The majority of Southern Japan is still under Ritsuryo control in 1066 AD, with a handful of Soryo rulers (such as ourself) controlling the northern side of the country.  

![image_58.png](https://forumcontent.paradoxplaza.com/public/1365678/image_58.png "image_58.png")


![image_59.png](https://forumcontent.paradoxplaza.com/public/1365679/image_59.png "image_59.png")


*[Individual rulers and the government map mode itself let us know the lay of the land at a glance]*  

On the demographics side, Japan is a cultural monolith at this point with nearly every county being dominated by people of the Yamato culture. There are Emishi-dominated counties in the north, and Ainu-dominated counties even further north in Hokkaido.  

![image_60.png](https://forumcontent.paradoxplaza.com/public/1365680/image_60.png "image_60.png")


*[Culture map of Japan in 1066 AD]*  

Religiously, however, Japan is a kaleidoscope of different faiths and traditions. Religion played a fundamentally different role in Japan than it did in Europe during this time, so there’s significantly less pressure for faiths to consolidate their position. The result is a rich tapestry of different faiths in the region.  

We belong to Pundarika Buddhism, but other branches of Buddhism and Shinto exist all around us.  

![image_61.png](https://forumcontent.paradoxplaza.com/public/1365681/image_61.png "image_61.png")


*[Faith map of Japan in 1066 AD]*  

Right out of the gate, we have enough dynastic Renown to unlock a Legacy. Japanese characters have access to the new Elegance Dynasty Legacy, but as interesting as it is, we’re here to burn as much of the central administration to the ground as we can before Takenori kicks the bucket. Since he’s already 62, it would be better for the goals of this particular playthrough if we focus on the existing Warfare legacy tree.  

![image_62.png](https://forumcontent.paradoxplaza.com/public/1365682/image_62.png "image_62.png")


*[The Elegance Dynasty Legacy path]*  

Turning our attention to our existing military forces, we station our men-at-arms and use some of our existing funds to increase the size of our Mounted Samurai regiment. This will wipe out most of our starting money, but we intend to make it back pretty quickly through Questionable Means™.  

![image_63.png](https://forumcontent.paradoxplaza.com/public/1365683/image_63.png "image_63.png")


*[Mounted Samurai men-at-arms]*  

Taking a look at our immediate warfare options, we have quite a large amount of potential targets. The Bloc Expansion casus belli lets us seize titles for the Kiyohara Bloc we belong to, and form a new member of the House Bloc to assign them to. With the small domain limit that Ritsuryo rulers are restricted to, this leaves a lot of potential targets for us to strike at.  

![image_64.png](https://forumcontent.paradoxplaza.com/public/1365684/image_64.png "image_64.png")


*[Current Situation log showing a large amount of valid war targets. In this build, the number shows their individual strength; the release version of All Under Heaven will show the strength of their House Bloc]*  

### House Blocs​

Many of these rulers belong to existing House Blocs, however, and an attack against them will be seen as an attack against the entire Bloc itself. For some of these rulers, attacking them would be suicide. Additionally, the Kampaku sees the seizure of Ritsuryo-held lands by Soryo forces as a criminal action, so we run the risk of having the central administration itself come down on our heads.  

![image_65.png](https://forumcontent.paradoxplaza.com/public/1365685/image_65.png "image_65.png")


*[Declaring war against a member of a powerful House Bloc]*  

A far safer option for us will be to consolidate the other existing Soryo rulers under our banner before carving out more pieces of Ritsuryo land. Dewa to our west is controlled by our own son of all people, so we can effectively consider them under our control already as they belong to our House Bloc. Tsugaru to the north isn’t a valid target for us either, as they’re not part of the Japanese realm; we’re prohibited from declaring wars with external realms unless the Imperial Policy is set to Imperial Pacification. Currently, the policy is Manor Reform, so we’re unable to expand northward.  

![image_66.png](https://forumcontent.paradoxplaza.com/public/1365686/image_66.png "image_66.png")


*[Manor Reform Imperial Policy]*  

![image_67.png](https://forumcontent.paradoxplaza.com/public/1365687/image_67.png "image_67.png")


*[Imperial Pacification Imperial Policy]*  

![image_68.png](https://forumcontent.paradoxplaza.com/public/1365688/image_68.png "image_68.png")


*[The political layout of Northern Japan in 1066 AD]*  

To the south we have a handful of Soryo realms, but as before we need to be wary of which Blocs they belong to. Jō, a branch of the Taira, belongs to the Kiyohara Bloc already, but the Yamato, a Minamoto branch in Iwase, are completely alone. As they don’t belong to a Bloc, we can utilize a variety of casus belli against them with little fear of retaliation from allies.  

![image_69.png](https://forumcontent.paradoxplaza.com/public/1365689/image_69.png "image_69.png")


*[War declaration screen against an isolated county-tier ruler]*  

Alternatively, we can simply invite them to join the Kiyohara Bloc. They’re slightly resistant to the idea, but an offering of Prestige is enough to swing the scales and get them to agree. Since we’re still reinforcing our newly-expanded Mounted Samurai divisions, this will be a preferable alternative to war.  

![image_70.png](https://forumcontent.paradoxplaza.com/public/1365690/image_70.png "image_70.png")


*[Extending a Bloc invitation to another house; no relation to the Imperial house Yamato!]*  

They happily accept the offer, and the Kiyohara Bloc welcomes them into the fold. Looking at the new House Bloc map mode, we can see a few remaining holdouts that we could potentially sway to our cause.  

![image_71.png](https://forumcontent.paradoxplaza.com/public/1365691/image_71.png "image_71.png")


*[Current House Bloc division in Japan]*  

After snapping up a few stragglers, we’re left with four main Blocs in control of Japan: Kiyohara Bloc, Kawachi Bloc, Hok-ke Bloc, and Murakami Bloc. There’s also Kikuchi Bloc to the far south, but they’re less of a concern for our current situation.  

With the remaining unaligned Soryo rulers having pledged themselves to our House Bloc, our only remaining option to expand our sphere of influence is to wage war. There are a handful of unaligned Ritsuryo rulers, but they refuse any call to join our House Bloc due to the different government types. Well, if they won’t join peacefully…  

![image_72.png](https://forumcontent.paradoxplaza.com/public/1365692/image_72.png "image_72.png")


*[Declaring war against an unaligned Ritsuryo ruler]*  

With that, we march on Totomi. This act of aggression is considered a crime by the Kampaku, but we’ll cross that bridge when we get to it. We raise our armies in the city of Shirakawa, and begin marching them south towards Totomi. While we have a numerical advantage in this war, terrain advantage will be a significant factor in determining who wins each battle. We’ll have to play it carefully as we move onto their holdings.  

Our enemy manages to form a new alliance and call them into the war. Hopefully we’ll have thrashed the Totomi army and started our siege of their castle by the time the new arrivals make it to the fight.  

![image_73.png](https://forumcontent.paradoxplaza.com/public/1365693/image_73.png "image_73.png")


*[An extra 500 men begin marching east]*  

Totomi’s army ends up fleeing from the province before we arrive; while this spares us a battle against defender bonuses, we now have to deal with the potential of them linking up with their allies. As we begin sieging the castle of Toyoda, all we can do is wait and see how the situation unfolds.  

![image_74.png](https://forumcontent.paradoxplaza.com/public/1365694/image_74.png "image_74.png")


*[Sieging down the enemy castle]*  

Their combined forces aren’t enough for them to feel confident attacking into our siege camp, so we take Toyoda without incident and achieve 100% warscore. We press our demands, and seize the county of Totomi for Kiyohara Bloc. We’re then presented with the choice of who to give it to: Our brother, our son, or keep it for ourselves.  

Granting the title to another will increase Bloc cohesion and grant a sizable opinion boost with the person receiving the title, while keeping it for ourselves will damage Bloc cohesion and incur an opinion malus with all potential recipients we’re snubbing in the process. We have room for an addition to our domain, but given the distance from our existing lands, we decide to grant it to our brother Mitsuyori.  

![image_75.png](https://forumcontent.paradoxplaza.com/public/1365695/image_75.png "image_75.png")


*[Deciding who to grant the newly acquired land to]*  

Seizing this land and putting it under the control of a Soryo ruler will not be viewed kindly by the Kampaku. We’re nowhere near ready to make a play for the Imperial Regency itself, so we need to seek a pardon for our crime. Unfortunately, the Kampaku is not very fond of us at the moment. We need to seek additional alliances in the event that he tries to imprison us.  

We quickly marry off our son Takehira to a daughter of House Settsu, forming an alliance with them and securing an additional 847 soldiers if the need should arise. It’s a start, but not enough. We follow up by marrying our son Takemichi to a member of House Oshu Ishikawa, adding an additional 700 men to our potential pool of allied soldiers.  

The Kampaku’s forces still outnumber us 4-to-1 and we’ve exhausted the potential alliances available to us at the moment. Well, if we’re already committing crimes against the Regent…  

![image_76.png](https://forumcontent.paradoxplaza.com/public/1365697/image_76.png "image_76.png")


*[Another Bloc Expansion war has begun]*  

We’re taking a swing at Owari and trying to add it to our Bloc. We’ve already committed a crime worthy of execution and have no way of securing a pardon, so at this point our safest bet is to nab as much land as we can to shore up our strength before the Kampaku tries to enforce his rule. We quickly sweep Owari’s forces away and grant the title to a half-brother, then immediately set our sights on Aki.  

![image_77.png](https://forumcontent.paradoxplaza.com/public/1365698/image_77.png "image_77.png")


*[Declaring yet another Bloc Expansion war]*  

Aki falls in short order, and our son Takemichi takes control of it. We begin striking further and further south, taking aim at Hyuga next. In the midst of this, the Kampaku takes notice and shifts Imperial Policy to Disarmament. This will have a noticeable impact on our ability to wage war across Japan, as the Disarmament policy makes it more expensive to declare war within Japanese borders, as well as increasing the cost of recruiting Men at Arms. More impactful in the long term, this Policy allows Ritsuryo rulers to construct and upgrade Castle holdings, which will make our wars take longer to conclude.  

![image_78.png](https://forumcontent.paradoxplaza.com/public/1365700/image_78.png "image_78.png")


*[Imperial Policy being updated to Disarmament]*  

Hyuga falls under our onslaught, and we decide to take it for ourselves to spare us the trouble of marching our armies all the way south each time. Now we can strike with equal efficiency from the north and south of the realm.  

In three short years we’ve become one of the most powerful Blocs in the realm, but we’re rapidly losing Cohesion within the Bloc. Each House that has a different Aspiration from our own will deplete the Cohesion of our Bloc over time, so we risk our Bloc falling apart unless we do something quickly. The “something” in this case is, unsurprisingly, war. We eject the offending houses from the Bloc and immediately swoop in to “redistribute” their property.  

![image_79.png](https://forumcontent.paradoxplaza.com/public/1365701/image_79.png "image_79.png")


*[The House Bloc panel, showing how Cohesion is impacted by houses within it]*  

Our half-brother’s house, formed when we granted him Totomi earlier, is expelled from the Bloc, and they are forbidden from declaring war on any of the Bloc members for five years. The reverse, however, is not true. We immediately declare war using the Bloc Expansion casus belli. After seizing Totomi once again, we keep it for ourselves before granting it to a vassal. The Bloc helped us expand, but now we need to consolidate Japan under our direct control.  

![image_80.png](https://forumcontent.paradoxplaza.com/public/1365702/image_80.png "image_80.png")


*[Totomi is now part of our realm proper]*  

We will continue to pick our own Bloc apart as opportunity presents itself, but we also need to focus on picking apart other Blocs. This is far trickier as an attack on one member is an attack on all, but there is room for lightning strikes; Ritsuryo rulers are limited to a couple of holdings at most, so if we strike at those along our own borders, we can potentially seize all of their holdings before their allies can arrive.  

It’s risky, but we’re living dangerously here.  

![image_81.png](https://forumcontent.paradoxplaza.com/public/1365703/image_81.png "image_81.png")


*[Declaring war with a Soryo County Conquest CB]*  

Hitachi is right next to our border, and commands very little strength on its own. If we can siege their county quickly enough, then we can snatch lands right out from under the Kawachi Bloc’s control.  

### Bloc Party​

Unfortunately, things go wrong almost instantly. Kawachi Bloc musters up several thousand men (of higher quality than our own!) in the immediate vicinity of our target. We begin our siege, but the amount of hostile armies nearby puts us in extreme danger. We do have allies we can fall back on, but calling on their aid will incur a Prestige cost as this is an offensive war. We’ll wait it out and hope for the best for now.  

![image_82.png](https://forumcontent.paradoxplaza.com/public/1365704/image_82.png "image_82.png")


*[Several high-quality armies begin to consolidate in response to our aggression]*  

We fend off the first wave of attackers, pushing us to 82% war score in the process. Our position is still extremely precarious, however. The best path forward from here is to finish the siege and force 100% warscore.  

![image_83.png](https://forumcontent.paradoxplaza.com/public/1365706/image_83.png "image_83.png")


*[Stinky idiots get wrecked by Kiyohara chads]*  

A second, weaker wave smashes against us immediately after, and is promptly torn to pieces. We reach 100% warscore as a result. Somehow, we’ve snatched victory from the jaws of defeat.  

![image_84.png](https://forumcontent.paradoxplaza.com/public/1365707/image_84.png "image_84.png")


*[The second battle goes even worse for Kawachi Bloc]*  

With the war won, we seize control of Hitachi and grant it to a new vassal under our direct control. Kawachi Bloc has suffered a tremendous loss here, but our own Bloc is still on the verge of total collapse. Ultimately this may suit our purposes however, as the scattered Soryo houses will make for easy pickings against our own might. Allies are lovely, but vassals are far better for the type of Japan we’re hoping to build.  

While this is happening, our son Takesada, ruler of Dewa, dies of pneumonia. Our character finds this deeply upsetting for some reason, and immediately suffers a stress break. We become Melancholic as a result. At our age of 67, the health loss from this trait can cut our campaign short.  

Let’s refocus our efforts on dismantling Kawachi Bloc and take a swing at Shimotsuke, held by House Kawachi itself.  

![image_85.png](https://forumcontent.paradoxplaza.com/public/1365708/image_85.png "image_85.png")


*[Angry red armies everywhere]*  

As before, Kawachi Bloc forces raise thousands of troops across Japan, but as we’re striking against a single target we stand a reasonable chance of ending the war with a metaphorical headshot before they can deliver a meaningful counte- oh. Oh no.  

![image_86.png](https://forumcontent.paradoxplaza.com/public/1365709/image_86.png "image_86.png")


*[Stinky idiots get wrecked by Kawachi chads]*  

Kawachi forces slam directly into us, tearing our army to shreds and gaining an immediate 50% warscore in their favor. With our army in full retreat, we have no recourse but to call our allies into the war. Upon trying to call them into the war, we run into another problem: Our allies hate us and won’t accept a call to arms.  

![image_87.png](https://forumcontent.paradoxplaza.com/public/1365710/image_87.png "image_87.png")


*[Get over here and help me dammit]*  

We manage to use our position as House Head to call Dewa forces into the war, and one of our allies accepts the call to arms. Combined, this nearly doubles our effective manpower. Unfortunately, the Kawachi army was nearly triple our manpower before we got torn apart. The war is not looking promising now.  

We combine our forces and march on Nasu, and are immediately intercepted by Kawachi forces.  

![image_88.png](https://forumcontent.paradoxplaza.com/public/1365711/image_88.png "image_88.png")


*[A losing battle in progress]*  

Also, our son Takehira is killed in the fighting. As before, this is deeply upsetting to our character.  

![image_89.png](https://forumcontent.paradoxplaza.com/public/1365712/image_89.png "image_89.png")


*[Stress break imminent]*  

With the loss of the Battle of Nasu, the enemy achieves 100% warscore and stops the Kiyohara advance dead in its tracks. At this point, our military is in shambles, half of our children are dead, and all of our vassals despise us due to the amount of offensive wars combined with the sudden Legitimacy drop from the lost battles. Additionally, we’re officially Feuding with House Kawachi.  

Also, we have cancer.  

![image_90.png](https://forumcontent.paradoxplaza.com/public/1365713/image_90.png "image_90.png")


[When it rains, it pours]  

Correction: we *had* cancer.  

![image_91.png](https://forumcontent.paradoxplaza.com/public/1365714/image_91.png "image_91.png")


*[RIP in peace, my guy]*  

Kiyohara Takenori dies on June 16th, 1073 AD. We spent only seven years playing as him, but what exactly did we accomplish during this time? Unsurprisingly, not a whole hell of a lot. We managed to put more of Japan under Soryo control, but in the process we destabilized the realm, destroyed our house’s relations with more than half of Japan, and got most of our family killed.  

![image_92.png](https://forumcontent.paradoxplaza.com/public/1365715/image_92.png "image_92.png")


*[The needle has moved slightly towards Soryo; a small victory!]*  

While Kiyohara Bloc remains a major force in Japan, its Cohesion puts it on the verge of total collapse. The Blocs we opposed directly are somehow more powerful than before, and Murakami Bloc is rapidly filling in the power vacuum we caused in Southern Japan.  

A remarkable amount of damage in such a short period of time!  

![image_93.png](https://forumcontent.paradoxplaza.com/public/1365716/image_93.png "image_93.png")


*[House Blocs in Japan as of 1073 AD]*  

While Fujiwara’s moon will shine brightly for a few more decades, the Kiyohara moon is most certainly waning.  

An undignified end to the campaign, but considering our character’s age it was to be expected that we would burn brightly but quickly. We hope this playthrough gives you a better idea of House Bloc dynamics and the interplay between Soryo and Ritsuryo governments!  


---

### Angkor, 867​

Our new 867 Bookmark, *Living Gods on Earth*, focuses on the Devarajas of Southeast Asia. The deep entanglement between spiritual and political power in this region necessitated the creation of an entirely new government type in All Under Heaven to represent these realms: Mandala Government.  

![image_94.png](https://forumcontent.paradoxplaza.com/public/1365717/image_94.png "image_94.png")


*[Living Gods on Earth, a new 867 Bookmark focusing on Southeast Asia]*  

Jayavarman II was a mighty ruler who united the Khmer peoples and founded the Khmer Empire itself. Shattering the power of disparate warlords and firmly establishing control over the region, he would be known as Parameshwara, the Supreme Ruler, after his death.  

We will not be playing as him. Instead, we'll be playing as his son Jayavarman III, who historically... didn't really do much worth mentioning. Let's see if we can change that.  

![image_95.png](https://forumcontent.paradoxplaza.com/public/1365718/image_95.png "image_95.png")


*[Jayavarman III, one of the highlighted characters in this bookmark]*  

Starting out our campaign, we’re in a fairly good position. We hold the duchy-tier title of Angkor, but not the kingdom-tier one. Despite that, we’re one of the eminent powers in our immediate region. The nature of the Mandala government means that this can quickly change though; competing rulers can draw away tributaries if they’re seen as more divine than us.  

![image_96.jpeg](https://forumcontent.paradoxplaza.com/public/1365719/image_96.jpeg "image_96.jpeg")


*[The political landscape of Southeast Asia in 867]*  

![image_97.jpeg](https://forumcontent.paradoxplaza.com/public/1365720/image_97.jpeg "image_97.jpeg")


*[Cultures of Southeast Asia in 867]*  

![SEA-faith-map_fixed.png](https://forumcontent.paradoxplaza.com/public/1366969/SEA-faith-map_fixed.png "SEA-faith-map_fixed.png")


*[Faiths of Southeast Asia in 867]*  

To keep other Mandala rulers in the area from stealing our Tributaries, we need to ensure our Mandala Radiance is as high as possible. This metric is essentially a measure of how powerful our divinity is, and can be raised by a variety of factors. Most noticeably in this playthrough, our Level of Devotion and strength of our Mandala Aspect (more on that later) will determine our Radiance.  

![image_99.png](https://forumcontent.paradoxplaza.com/public/1365722/image_99.png "image_99.png")


*[Mandala Radiance can be seen near your character’s portrait; clicking the button will open the Mandala Mapmode]*  

Using the new Mandala map-mode, we can tell at a glance who can be swayed by our Radiance into pledging themselves to us. Counties are colored on typical green-to-red scale indicating how likely they are to accept a tributization demand, with the addition of white to represent rulers we’re too far away from to attempt tributizing, and black to represent rulers that we’re blocked from sending the interaction to for one reason or another.  

At a glance, we don’t have a ton of options here. We need to focus on improving our piety and Mandala Radiance, or we’ll risk losing territory as our tributaries are swayed by other Devarajas.  

![image_100.png](https://forumcontent.paradoxplaza.com/public/1365724/image_100.png "image_100.png")


*[Mandala Mapmode]*  

Before that, however, we need to decide what kind of God-Kings our line will be. We can do this by assuming a Mandala Aspect, aligning ourselves with a specific nature of divinity.  

We have four main options here, with each one representing a different type of god for us to emulate as well as the approach to governance that we’ll emphasize. They each come with a variety of bonuses relating to their emphasized skill, and can unlock various realm laws (or Decrees) for us to play around with. As we upgrade our Aspect over the generations, the Aspect itself becomes more powerful.  

![image_101.png](https://forumcontent.paradoxplaza.com/public/1365725/image_101.png "image_101.png")


 *[The four Mandala Aspects]*  

The different Mandala Aspects are:  


- **Aspect of Creation**, emphasizing Stewardship
- **Aspect of Serenity**, emphasizing Diplomacy
- **Aspect of Destruction**, emphasizing Martial
- **Aspect of Trickery**, emphasizing Intrigue



![image_102.png](https://forumcontent.paradoxplaza.com/public/1365726/image_102.png "image_102.png")


![image_104.png](https://forumcontent.paradoxplaza.com/public/1365728/image_104.png "image_104.png")



![image_103.png](https://forumcontent.paradoxplaza.com/public/1365727/image_103.png "image_103.png")


![image_105.png](https://forumcontent.paradoxplaza.com/public/1365729/image_105.png "image_105.png")


*[Tier 1 bonuses for each of the Mandala Aspects]*  

This decision won’t affect just ourselves, but continue through our line for quite some time. The Aspect of Serenity offers a modifier increasing our monthly Legitimacy gain that improves every 5 years without an offensive war. As we did a Martial-focused playthrough for Japan, this seems like a suitable option.  

We assume the Aspect of Serenity, and our House view panel updates to visually show what our House’s Aspect is.  

![image_106.png](https://forumcontent.paradoxplaza.com/public/1365731/image_106.png "image_106.png")


*[S-stando?! ゴゴゴ]*  

With our Aspect selected, we can now take a closer look at our current situation. We have few direct vassals, but we do hold sway over a multitude of tributaries who recognize our Radiance. Unfortunately, one of them is considering breaking away and ceasing his tribute to us. That’s unacceptable, of course; we need to secure their loyalty immediately.  

![image_107.png](https://forumcontent.paradoxplaza.com/public/1365732/image_107.png "image_107.png")


*[Current Situation entry alerting us to potential Tributary problems]*  

They’re easily swayed however, and reducing their taxes to us secures their loyalty for 12 months. This isn’t sustainable long-term but it gives us a year to work on our position as a God-King, and hopefully by the end of the grace period they’ll no longer want to stop paying us tribute.  

![image_108.png](https://forumcontent.paradoxplaza.com/public/1365733/image_108.png "image_108.png")


 *[Reasserting Tributary status by decreasing Tax Obligation]*  

How can we improve our position as a God-King, though? Well, simple: Piety. We’ll plan a pilgrimage to a nearby holy site to rack up some Piety and push us to a higher Devotion level. Each Devotion level grants us additional Mandala Radiance, and the more Radiant we are the more stable our position becomes.  

The holy site of Sri Thep is fairly close to us, so we can take a quick trip down the road and pay them a visit.  

![image_109.png](https://forumcontent.paradoxplaza.com/public/1365734/image_109.png "image_109.png")


*[A quick and easy travel plan]*  

While we’re busy showing everyone how humble we are in Sri Thep, one of our tributaries unexpectedly breaks away. We’re given the option to retaliate against them with an offensive war, but our Aspect doesn’t favor that course of action so we’ll let them leave peacefully for now.  

![image_110.png](https://forumcontent.paradoxplaza.com/public/1365735/image_110.png "image_110.png")


*[Tributary breaking away from us]*  

The pilgrimage gives us a fair bit of Piety and pushes our Devotion Level up to Faithful. This in turn increases our Mandala Radiance by a bit, but not enough to meaningfully sway any of our immediate neighbors.  

![image_111.png](https://forumcontent.paradoxplaza.com/public/1365736/image_111.png "image_111.png")


*[Eight Radiance. Not great, not terrible.]*  

Fortunately, our remaining Tributaries are embarking on Tribute Missions to us. We gain a small amount of gold and Piety for each one of these, but we’re expected to grant the Tributary a boon in return. Our options are to grant them a Khmer artifact, finance a trade post in our Tributary’s capital, or to simply reaffirm their right to rule in their lands.  

The first two options cost money, and we refuse to be parted with my gold as a matter of principle. We didn’t make this money to give it to our tributaries, we made this money to oppress our tributaries. We affirm them as the rightful ruler of their lands and send them on their way. Thanks for the money, sucker.  

![image_112.png](https://forumcontent.paradoxplaza.com/public/1365737/image_112.png "image_112.png")


*[Being on the receiving end of a Tribute Mission]*  

This is a good time to check on the state of the Silk Road and Dynastic Cycle. While we don’t participate in either of these Situations directly, their status can present us with opportunities in the future so it’s helpful to keep an eye on them. In All Under Heaven, we’ve introduced a new Situations panel to let players access the different Situation interfaces from one convenient place.  

![image_113.png](https://forumcontent.paradoxplaza.com/public/1365738/image_113.png "image_113.png")


*[The new Situations panel in All Under Heaven]*  

We’re relatively close to two different trade hubs on the Silk Road, but the Innovations they’re currently sending downstream aren’t very useful to us. In 11 years a new Innovation will be available in the Marketplace of Chang’an, so we’ll check back in about a decade.  

![image_114.png](https://forumcontent.paradoxplaza.com/public/1365739/image_114.png "image_114.png")


*[Current state of the Silk Road as of 867 AD]*  

We embark on another pilgrimage, this time to Kanchipuram, but we opt for an oversea route to minimize danger. This sends us through the Berhala Strait and lands belonging to Malayadvipa, who have managed to bring an impressive amount of tributaries under their wing since we last looked this way.  

![image_115.png](https://forumcontent.paradoxplaza.com/public/1365740/image_115.png "image_115.png")


*[Heading home from our second pilgrimage]*  

Events during this pilgrimage give us enough Piety and Legitimacy to increase their respective levels, which also lets us meet the requirements for one of the key aspects of Mandala rulership: Upgrading our Capital Temple Complex. As mentioned in previous dev diaries, the Capital Temple Complex is your ultimate base of power as a Mandala ruler, and it has a tremendous effect on your Mandala Radiance.  

### The Majestic Temple Project​

As competing Devarajas in the area continue to sway more of our Tributaries to themselves, we find ourselves with a mighty need to begin improving our Temple. Unlike other buildings in the game, Capital Temple Complexes are upgraded by planning out a Great Project.  

![image_116.png](https://forumcontent.paradoxplaza.com/public/1365741/image_116.png "image_116.png")


*[Planning our Capital Temple Complex’s upgrade project]*  

With a click of a button, we’ve created a Great Project. That’s only the first step, however; we still need to manage the contributions to it. There’s a set of Mandatory Contributions that must be completed in order for construction to begin, but there’s also a set of Optional Contributions that are, shockingly enough, optional. They’ll grant additional bonuses to the Temple Complex, but we can begin construction without them if we decide it’s necessary to do so.  

With a down payment of 500 godbucks, we can begin the planning stage of the project.  

![image_117.png](https://forumcontent.paradoxplaza.com/public/1365742/image_117.png "image_117.png")


*[Great Projects can be accessed from a new tab at the top of the existing Decisions panel]*  

Most of these Contributions are straightforward enough to accomplish; we can even bully some of our Tributaries into footing the bill on them for us. The big blocker we’re going to be dealing with, however, is the Rite of Worthiness. In order to fulfil this contribution, we have to prove that we’re acting in alignment with the Aspect of Serenity.  

More specifically, the Rite of Worthiness demands the following:  


- Having 25 experience in the Pilgrim trait
- Maintaining 2 alliances with same-or-higher tier rulers outside of our Realm
- Not declaring any offensive wars for at least 5 years
- Having 5 friendships
- Hosting 3 feasts with Exorbitant and Culinary Artpieces Activity Options

We don’t meet the requirements yet, but we can begin taking care of the other Contributions while we work our way towards this one.  

![image_118.png](https://forumcontent.paradoxplaza.com/public/1365743/image_118.png "image_118.png")


*[Tributaries can be convinced to handle some Contributions]*  

For now, we’ll spend 375 Piety to complete the Workforce Contribution. This will give us the Strong Workers modifier for a few years after the Great Project is actually completed, which carries a handful of bonuses for levy reinforcement and building construction rates. It doesn’t benefit us now, but we’ll need to complete this Contribution either way so we might as well do it now.  

More concerning is meeting those requirements for the Rite of Worthiness. We need friends and allies, and we need to host some feasts. Fortunately, we can kill several birds with one stone and make some friends at our feasts! Unlike other government types, Mandala feasts are paid for with Piety. Having forgotten this briefly when paying for the Workforce Contribution, we are left with a moment of lingering regret. We can still host a Feast that meets the requirements of the Rite however, so we charge ahead and set out to befriend one of our Tributaries while chowing down on some decent food.  

![image_119.png](https://forumcontent.paradoxplaza.com/public/1365744/image_119.png "image_119.png")


*[Mandala feasts are funded with Piety, not Gold]*  

The feast goes according to plan, and we successfully befriend our Tributary in the process. Let’s abuse that immediately, and ask our wonderful new friend to fill one of the remaining Contributions. They accept without hesitation, and our Optional Contributions are now filled. Gosh, what a lovely friend we’ve made.  

![image_120.png](https://forumcontent.paradoxplaza.com/public/1365745/image_120.png "image_120.png")


*[Convincing someone to help out with our Great Project]*  

We can also convince one of our Tributaries to kick in 50 gold and 250 Piety to fund the Stacks of Tiles Contribution, but we need to offer them a Weak Hook in exchange for this. It’s not ideal, but we can live with this. With that, the only remaining Contribution aside from the Rite of Worthiness is the Brick Contribution. It’s a mere 50 gold, so we pay that one outright ourselves.  

All we need now is to continue feasting and befriending people. What a terrible fate.  

![image_121.png](https://forumcontent.paradoxplaza.com/public/1365747/image_121.png "image_121.png")


*[The Project nears completion]*  

### How to Make Friends and Influence People​

We can sort the required alliances easily enough; we’ve got plenty of kids loafing about the Temple that we could put to good use. We marry a daughter off to the son of Dvaravati’s God-King, securing both an alliance and preventing a potential enemy from confronting us directly via warfare in the future.  

While we’re trying to figure out which foreign realm we’re shunting our kids off to, we get an alliance request from one of our Tributaries. Normally accepting this would be a no brainer, but unfortunately adding another alliance would incur an acceptance penalty to marriage requests. We need to get our kids assigned first, so we have to reject this request for now.  

![image_122.png](https://forumcontent.paradoxplaza.com/public/1365748/image_122.png "image_122.png")


*[Declining an Alliance offer from one of our Tributaries]*  

Sending another daughter off to the son of Nanzhao’s ruler secures us an additional alliance, and with that we’ve fulfilled another requirement for the Rite of Worthiness. We still have at least 2 years before we can meet the 5 years with no offensive war requirement, so we’ll spend the next couple of years working on our Piety and using it to host additional feasts.  

While we’re occupied with this, we get enough Renown to unlock a Dynasty Legacy. Mandala rulers have access to the new Divine Aspirations Dynasty Legacy, which offers various perks and bonuses to those pursuing the path of divinity. How convenient for us! We’ll unlock the first perk in the tree, Consecration. It offers a few additional sources of Legitimacy, which is always a good thing to have.  

![image_123.png](https://forumcontent.paradoxplaza.com/public/1365749/image_123.png "image_123.png")


*[The Divine Aspirations Dynasty Legacy path]*  

A quick pilgrimage to Varanasi should net us enough Piety to kick off another feast, so we set out on the road once more. While the journey itself is lengthy, it goes without any major complications, so we won’t be covering it here. More importantly, we have a Provincial Ritual opportunity just around the corner from our capital, so we set out for it as soon as we return from the pilgrimage.  

Upon arrival, we’re given the choice between Piety and Legitimacy granting options. Both are lovely to have, but our need for Piety is far more pressing at the moment so we’ll go with that one.  

![image_124.png](https://forumcontent.paradoxplaza.com/public/1365750/image_124.png "image_124.png")


*[Mandala Ritual event]*  

We’ve now crossed the five year mark for the Rite of Worthiness, and at the same time crossed the five year cooldown on upgrading our Mandala Aspect. This will take a significant amount of the Piety we’ve recently worked so hard to get, but the bonuses are hard to ignore. Unfortunately, upgrading the Aspect has similar prerequisites as the Rite itself, so we’ll need to wait until we hold more feasts and make more friends.  

![image_125.png](https://forumcontent.paradoxplaza.com/public/1365751/image_125.png "image_125.png")


*[Upgrading our Mandala Aspect has similar requirements to the Rite of Worthiness]*  

We still have three years to go until another feast can be held, but the Aspect of Serenity gives us access to the Befriend Scheme, so we can still pal around in the meantime. Tributaries are good friends to have, as it makes them less likely to break away from us. Taking a quick look at the Mandala Mapmode reveals that our pursuit of Piety has boosted our Radiance enough to potentially bring new Tributaries into the fold, so we fire off some invitations for these poor saps to worship us.  

![image_126.png](https://forumcontent.paradoxplaza.com/public/1365752/image_126.png "image_126.png")


*[The Mandala Mapmode around Angkor reveals potential recruits to our ~~pyramid scheme~~ Triangle of Opportunity]*  

A few accept our invitation, expanding our sphere of influence ever so slightly. We pick a few nearby independents to target with Befriend schemes to increase their odds of accepting a Tributization offer; nabbing just one of them pushes us over the 5 friend threshold.  

All we need to do now to complete the Rite of Worthiness is to party hard. With fortuitous timing, the feast cooldown has already expired and we can begin planning it immediately.  

![image_127.png](https://forumcontent.paradoxplaza.com/public/1365753/image_127.png "image_127.png")


*[The second feast begins]*  

The feast proceeds without incident and concludes similarly. That’s two feasts down, and one to go.  

While this has been happening, we’ve gotten a few rulers asking us to accept tribute from them. After accepting these, we’ve gained enough land to form the Kingdom of Angkor. Forming titles as a Mandala ruler requires Piety, however, and Kingdom-tier titles are quite expensive at 2,500 Piety.  

![image_128.png](https://forumcontent.paradoxplaza.com/public/1365754/image_128.png "image_128.png")


*[Title creation requirements for a Mandala ruler]*  

We’ve picked up quite a bit of Piety from our pilgrimages as well as by handling governance issues in our realm, so we can meet this threshold after waiting a few months for our passive Piety income to push us over the threshold. With the creation of a Kingdom-tier title, we’re expected to eventually hold a Coronation. As you don’t need this playthrough to tell you how a Coronation works, we’ll skip over that process. Suffice to say that we hold a lovely Coronation ceremony, and everything goes well. It’s expensive, but gold from our Tributaries is more than enough to fund it.  

We continue along as normal, collecting passive Piety while we wait for our next feast to finally finish the Rite of Worthiness, when we suddenly get a Call to War from our ally in Nanzhao.  

![image_129.png](https://forumcontent.paradoxplaza.com/public/1365755/image_129.png "image_129.png")


*[Allied Call to War]*  

A… Hegemonic Consolidation war? What on earth is going on up ther- oh good lord.  

![image_130.png](https://forumcontent.paradoxplaza.com/public/1365757/image_130.png "image_130.png")


*[Bad times ahead]*  

The Dynastic Cycle has entered a Division Era. The ruling Tang Dynasty has collapsed, and various factions are competing to claim the Mandate of Heaven and return China to a peaceful Era. In the Situation window, we can see the three leading competitors for the Mandate of Heaven.  

![image_131.png](https://forumcontent.paradoxplaza.com/public/1365758/image_131.png "image_131.png")


*[The Division Era of the Dynastic Cycle]*  

While this doesn’t concern us directly, it does mean our Yi ally to the north will be calling us into wars on a fairly regular basis for the immediate future. Rejecting a Call to War as a Mandala ruler incurs a loss of Devotion in addition to Fame, so turning them down will set us back significantly on the path to Godhood. We have no choice but to accept.  

That doesn’t necessarily mean that we have to actually participate though. We’ll cheer them on from a distance. Good luck, buddy! More pressing for us, however, is that we’ve suddenly become Infirm.  

![image_132.png](https://forumcontent.paradoxplaza.com/public/1365759/image_132.png "image_132.png")


*[Not pictured: A CM raging at RNG while he tries to finish a playthrough]*  

Our age is starting to catch up to us, and we’re not ready for the next step in the cycle just yet. We have to hold at least one more kegger before we croak! Hitting the highest level of Devotion available would also be nice, since it will allow our successor to progress to the next level past Religious Icon.  

Around this time, we receive word that our allies in the north have been defeated. Sorry pal, maybe you should have allied with someone who assumed the Aspect of Destruction.  

![image_133.png](https://forumcontent.paradoxplaza.com/public/1365760/image_133.png "image_133.png")


*[Hegemonic War conclusion]*  

The activity cooldown expires, and we begin preparations for the third feast. When this concludes, we’ll finally be able to complete the Rite of Worthiness and begin the expansion of our Capital Temple Complex.  

During the feast, we get an event featuring one of our Yi allies in attendance. Lovely people, shame about the war.  

![image_134.png](https://forumcontent.paradoxplaza.com/public/1365761/image_134.png "image_134.png")


*[The third feast is underway]*  

The feast concludes, and we complete the Rite of Worthiness. It took more than a decade, but our Great Project is finally underway! We also take the opportunity to upgrade our Mandala Aspect as well.  

![image_135.png](https://forumcontent.paradoxplaza.com/public/1365762/image_135.png "image_135.png")


*[Great Projects are started when the final Contribution is completed]*  

Construction will take four years to complete, but the result will be well worth it. Shortly after completing the feast and beginning the Great Project, we reach the maximum level of Devotion: Religious Icon.  

![image_136.png](https://forumcontent.paradoxplaza.com/public/1365763/image_136.png "image_136.png")


![image_137.png](https://forumcontent.paradoxplaza.com/public/1365764/image_137.png "image_137.png")


*[The highest level of Devotion… for now]*  

With this accomplishment, we have achieved our goals on this earthly plane. All that remains for now is to await the sweet embrace of death, and have our successor begin forging the next link in our dynasty’s chain.  

We don’t have to wait very long.  

![image_138.png](https://forumcontent.paradoxplaza.com/public/1365765/image_138.png "image_138.png")


*[He ded]*  

Jayavarman III dies on December 9th, 883 AD. In the seventeen years we lived as him, we managed to accomplish quite a bit through Angkor. We elevated our Duchy to a Kingdom-tier title, began construction of an expansion Great Project for our Capital Temple Complex, secured a multitude of tributaries across the region, and achieved the highest possible level of Devotion.  

Normally, this is where our character’s story would end in a standard playthrough. Mandala government is a bit different in that regard, however. Death and succession are a key aspect of progression as a Mandala, and our accomplishments as Jayavarman III allow our daughter Vedvati to reach even greater heights of divinity… if she can prove herself worthy of continuing the line.  

This dev diary is quite long enough already though, so we’ll let you discover this aspect of Mandala at another time.  


---

With that, this dev diary finally comes to a close. While these playthroughs are far from comprehensive breakdowns of their respective regions, we hope they’ve given you a better understanding of how all their individual pieces fit together. We expect you’ll have quite a few questions after everything we’ve covered, and we encourage you to post them below! As always, we’ll be lurking around for a while and answering whatever questions we can.  

Thank you for taking the time to read this dev diary, and I hope we’ll see you again next week for our first (yes, *first*) dev diary covering the mountain of new art that’s coming to Crusader Kings III with All Under Heaven.

 

Last edited: Sep 30, 2025

<!-- artifact:reactions:start -->
- 85 Like
- 31 Love
- 7 (unlabeled — rendered as base64 data URI)
- 5 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)**
Role: Community Manager
Badges: 102
Messages: 642
Reaction score: 17,753

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
