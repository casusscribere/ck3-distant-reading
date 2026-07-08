---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1479565/"
forum_thread_id: 1479565
content_type: reply_thread
parent_dd_file: dd_064_2021-06-15_dev-diary-64-cultures-are-forever.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 64
title: "CK3 Dev Diary #64 - Cultures Are Forever"
dd_date: 2021-06-15
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 19
reply_count: 372
participant_count: 230
reply_date_first: 2021-06-15
reply_date_last: 2021-09-25
body_word_count: 30180
inline_image_count: 0
quoted_span_count: 207
extraction_rationale: |
  Full reply thread captured live via Claude in Chrome (article.message bodies).
  Quote blocks split into artifact:quote spans and excluded from word counts.
  Usernames replaced by stable per-thread participant ids; the dev-diary OP is
  excluded (see parent_dd_file).
notes_for_analyst: |
  Community-voice counterpart to the linked dev diary. Strip YAML + artifact
  comments before tokenizing, exactly as for dd_*.md.
---

# Reply thread — CK3 Dev Diary #64 - Cultures Are Forever

*372 replies from 230 participants across 19 pages*

## Reply 1 — participant_001 · 2021-06-15 · post-27618275

CK3 Dev Diary #64 - Cultures Are Forever​Salutations! Before we begin, first things first. We are working on an additional patch to fix some of the issues introduced in 1.4. The patch is still being worked on, but if everything goes as planned, we should be able to get it out sometime next week or so. We’ll let you know once the patch is ready. With that out of the way, let’s talk about something I’m quite excited to share with you all. As you probably know already, we’ve talked a bit about how we are revisiting cultures for the next expansion: Royal Court. Unlike faiths, which got a lot of attention prior to release as we made them quite dynamic and customizable, cultures can feel a bit static, and aren't anywhere near as interesting as faiths. That is all about to change! We are revising cultures as you know them. Most exciting is perhaps the possibility to create new cultures! Both for simulating historical events and to create plausible and interesting alt-history scenarios. But I’m getting ahead of myself. For now, let’s start by looking at the foundation of a culture and the different components they are made of. This is what the new culture screen will look like. { "lightbox_close": "Close", "lightbox_next": "Next", "lightbox_previous": "Previous", "lightbox_error": "The requested content cannot be loaded. Please try again later.", "lightbox_start_slideshow": "Start slideshow", "lightbox_stop_slideshow": "Stop slideshow", "lightbox_full_screen": "Full screen", "lightbox_thumbnails": "Thumbnails", "lightbox_download": "Download", "lightbox_share": "Share", "lightbox_zoom": "Zoom", "lightbox_new_window": "New window", "lightbox_toggle_sidebar": "Toggle sidebar" } [Image of the new and updated culture interface]​ Cultural Pillars​A culture has five main Cultural Pillars. These are Ethos, Heritage, Language, Martial Custom, and finally Aesthetics. Of these, the Ethos is perhaps the most significant, but all of them play a particular role in how a culture plays and how cultures view each other. Ethos Each ethos is framed around a particular theme that somehow ties into a fairly broad definition of what a culture is. A culture’s ethos not only provides effects and bonuses for having it, it also ties into how easy or difficult it is to acquire certain traditions (more on this further down). There are seven in total: Bellicose Communal Courtly Egalitarian Inventive Spiritual Stoic Here are a few examples of what they may look like in-game: [Image of the Bellicose ethos] [Image of the Spiritual ethos] [Image of the Inventive ethos]​ Heritage A culture's heritage can be compared to the culture groups that you may be used to in the existing system. Heritages will roughly match said culture groups. You’ll see an Iberian Heritage for cultures like Basque and Castilian, or Turkic Heritage for Turkic cultures, such as Oghuz and Cuman. In terms of gameplay, the most outstanding effect of a shared heritage is the impact it has on Cultural Acceptance. Language Each culture has a designated language. Languages vary greatly across the map and between cultures. Some languages, such as Arabic, are spoken by quite a few cultures. Other languages are spoken by no more than two or three cultures, or in some cases, cultures even have their own unique language. An example of these would be Basque, who really don't have any closely related languages and it wouldn’t make too much sense to group them together with their neighbors. The vast majority of cultures share a language though, as a sort of “language group” rather than a specific language. Characters can always speak the associated language of their culture. They are, however, also able to learn multiple languages over their lifetime. Knowing multiple languages has its benefits, as speaking the same language as another character of a different culture, and county, will reduce the opinion penalty that character, or county, has towards you. Knowing the native language (i.e. the language of their culture) of your vassals is therefore fairly beneficial as a means of increasing their opinion of you. Noble Martial Custom The martial custom decides which gender you may appoint as knights and commanders. As you’d expect, you can either appoint men, women, or both. We always felt that having the gender doctrine on faiths decide which characters can and cannot participate in battles felt off. The doctrine is about the right to rule and the holding of titles, more so than anything else. Just because you want the Equal doctrine to allow female rulers, doesn’t mean that women would automatically lead your armies or join you as knights. Revising cultures gave us the ample opportunity to move the functionality from faiths over to cultures. Which also means that you’ll have additional options in shaping your realm. Aesthetics This pillar is really a collection of several smaller properties for what a culture “looks” like. It decides what type of clothes characters wear, the coat of arms style for dynasties, what architecture holdings use, and the type of armor the units on the map wear. This is also the pillar that contains what naming practices the culture uses. Mainly what character names to use, if they use a dynasty prefix, etc. The naming practice will also be used to change title and holding names, which used to be set per culture, so as to not have titles change names if you create a new culture. For all of you modders out there; all of these can be set individually per culture. Allowing you to mix and match the different aesthetics to your heart’s content. Traditions​Traditions are the meat of the cultural overhaul, and provide that extra layer of variety and immersion that can have a significant impact on gameplay. An important aspect of traditions is that they give us a clear means of visualizing and explaining existing mechanics that previously just “was a thing” and never explained. Take Anglo-Saxon as an example. They have access to the Saxon Elective succession for no apparent reason other than “they do”. Instead, they now have a tradition that grants them the succession law, making it clear as to why they have it. Secondly, and perhaps more importantly, traditions serve as the perfect means of giving a culture additional flavour or gameplay bonuses that add a greater degree of variety across the map. A culture can have no more than five traditions in total, but this number will increase as you enter a new era. Most cultures will start the game with around three or four, which leaves plenty of room for you to shape your culture as you play the game. As the cultural head, you’ll have the ability to establish new traditions. Not all traditions will be available everywhere. We have both regional traditions, as well as traditions that are available depending on your heritage. The vast majority of them can be established regardless of circumstances, but might require certain conditions, such as ‘Hill Dwellers’ having the requirement that your culture must be present in a county with hills. Traditions cost prestige to adopt. Which will be the largest hurdle for you to overcome if you want a specific tradition. The prestige cost is dependent on your ethos. Certain traditions will be more expensive than others, if you don’t have a matching ethos. Similarly, a tradition will increase in cost if your culture, or in some cases the cultural head, doesn’t fulfill a specific and thematic requirement. An example would be a tradition named ‘Only the Strong’, which is more expensive if you as the cultural head don't have at least six knights with at least 12 prowess. The increased cost is meant to act as a softer limit and make it slightly more difficult to establish certain traditions (depending on your circumstances), but not as much as to make it impossible to do so, should you want to go and unlock a particular tradition. Instead of explaining traditions in detail, I’ll just show you a few examples of what traditions may look like, as well as the type of effects you can expect from them. [Image of the Swords for Hire tradition] [Image of the Chivalry tradition] [Image of the Esteemed Hospitality tradition] [Image of the Seafarers tradition] [Image of the Land of the Bow tradition]​ Cultural Acceptance​Cultural acceptance can be described as how well intermingled two cultures are, and how accepting they are of each other. Which means that given enough time, cultures will dislike each other less, and culture converting everything within your realm is no longer the only solution to combat cultural differences. The opinion penalty of being of a different culture used to be a static value. Now, it will depend on the cultural acceptance between your culture and the target culture. Each culture has an acceptance value of another culture, visualized as a percentage. Depending on the amount of acceptance, the “different culture” opinion penalty will gradually be reduced. At 0% acceptance, you’ll have the full opinion penalty. At 100%, the penalty is removed altogether. Acceptance goes both ways. So if the French have a 20% acceptance towards Normans, the same will be true from the Norman perspective. There are two ways for acceptance to change. The first is an acceptance baseline. Which increases if two cultures share similarities with one another. There are a number of different modifiers that can increase the baseline. Such as cultures that share the same religion or faith, ethos, or language. The most impactful modifier, however, is heritage. If two cultures share the same heritage, they have a significant bonus to their baseline. If acceptance is above the baseline, it will slowly decay over time towards the targeted value. Being below the baseline on the other hand, will not make the acceptance increase. A bad relation between cultures won’t disappear overnight. Secondly, acceptance very much changes depending on the circumstances. Don’t expect two cultures that never interact with one another to gain acceptance. If cultures exist within the same realm though, it will increase over time. This applies to both counties of another culture within your realm, as well as vassals. Acceptance is also reactive. Taking certain actions towards characters of a different culture will have consequences on your acceptance, such as declaring war or revoking titles. This generally scales on size. While the difference isn’t huge, revoking a single county from a small culture will decrease your acceptance more than if you would revoke a county from a much larger culture. At the end of the day, if you want to maintain a high acceptance and keep your Occitan vassals in France happy, you are at least gonna have to try and be nice to them. [Image of what the cultural acceptance between two cultures may look like]​ There we go. That’s what a culture will look like in the near future. Oh! Before I forget; Best of all? The cultural rework is free, and will accompany the free update that launches alongside the Royal Court expansion! Until next time!

## Reply 2 — participant_002 · 2021-06-15 · post-27618669

Hey everyone, If you missed the recent information about our next expansion, have a look at our FAQ Royal Court! General questions, Dev Diaries, Videos & Trailer, Press & Articles Previews. As always, thanks for reading our news; Feel free to drop your questions to our development team Cheers,

## Reply 3 — participant_003 · 2021-06-15 · post-27618678

Appreciate the changes. Waiting eagerly.

## Reply 4 — participant_004 · 2021-06-15 · post-27618679

Great work! Question, are you ever going to rework the Baltic area in the future in terms of map, culture, etc. ? There are some things that could be tweaked, like translation and borders. Love you CK3 team <3

## Reply 5 — participant_005 · 2021-06-15 · post-27618681

I love this! I can't wait to see the new culture changes!

## Reply 6 — participant_006 · 2021-06-15 · post-27618683

Sounds good

## Reply 7 — participant_001 · 2021-06-15 · post-27618689

<!-- artifact:quote:start -->
> Nobody_Expects said: Great work! Question, are you ever going to rework the Baltic area in the future in terms of map, culture, etc. ? There are some things that could be tweaked, like translation and borders. Love you CK3 team <3 Click to expand...
<!-- artifact:quote:end -->
No immediate plans, but we always try to improve the map when we can, so we'll probably get back to improving the Baltic area at some point in the future.

## Reply 8 — participant_007 · 2021-06-15 · post-27618702

Will things like the ability to raid now become a cultural tradition?

## Reply 9 — participant_008 · 2021-06-15 · post-27618703

Aesthetics! We'll we get culture-aware UI?

## Reply 10 — participant_009 · 2021-06-15 · post-27618705

Do my eyes deceive me, or does the Bavarian culture end at Carinthia? Could it be? Is Carantanian/Alpine Slavic culture returning?

## Reply 11 — participant_010 · 2021-06-15 · post-27618709

I better not open up the game and see it say that the Vlachs speak a Slavic language.

## Reply 12 — participant_011 · 2021-06-15 · post-27618710

Love this longer and more in depth Dev Diary, the culture rework looks fantastic so far. Will every culture receive unique traditions, or is it only a select few? And are Men at Arms types which were locked behind innovations now tied to tradition?

## Reply 13 — participant_012 · 2021-06-15 · post-27618715

Will it be possible for a culture to have more than one designated language? I'm thinking as one of the mod team members for Realms in Exile, a lot of the cultures in Middle-Earth speak multiple language - a Noldor elf likely speaks Westron, Sindarin and Quenya, a Rohirrim speaks Westron and Rohirric, a Gondorian speaks Westron and Sindarin, etc.

## Reply 14 — participant_013 · 2021-06-15 · post-27618717

Ooh this looks cool. One thing I am wondering about is what about Languages that come into existance during this time frame? Things like Hindi which did not exist at either start date and came about with the various Turkish and Persian empires*. Or how English changed from Old English to Middle English. *Hindustani also shouldn't be a culture at start but a melting port culture.

## Reply 15 — participant_014 · 2021-06-15 · post-27618718

The execution of ethoses is still a major concern for me. I don’t hate the fact that you won’t be locked out of any type of gameplay due to your ethos, and it at least *kinda* makes sense that it would be harder to become a more learning oriented nation if war is the historic main focus of your people, from an irl perspective. I still think that ethos and heritage should be dynamic, changing over many decades if a culture and its leader start acting a certain way for long periods of time. It makes no sense that I could be a nation which includes all the Norse in 900, save up to buy expensive intellectual traits, and then focus on being an isolationist until 1200, and new intellectual traditions still wouldn’t be cheaper, and I wouldn’t get bonuses ro learning at all. The potential issues I’ve noted many times at this point with unintentional stereotyping and the fact that this does not reflect how cultures evolved without becoming new cultures or hybridizing unfortunately still stand as well.

## Reply 16 — participant_015 · 2021-06-15 · post-27618719

This looks fantastic. Regarding the aesthetics parts of the pillars, can modders introduce new sets to choose from? Any plans to expand these options via DLC à la Stellaris?

## Reply 17 — participant_016 · 2021-06-15 · post-27618730

<!-- artifact:quote:start -->
> Servancour said: [Image of the Bellicose ethos] [Image of the Spiritual ethos] [Image of the Inventive ethos]​ Click to expand...
<!-- artifact:quote:end -->
Oh come on just post them all. No one cares about "waiting and seeing them all when it comes out" we'd rather theory craft.

## Reply 18 — participant_017 · 2021-06-15 · post-27618733

Oh my god yes my body is ready. What great arts too!

## Reply 19 — participant_001 · 2021-06-15 · post-27618734

<!-- artifact:quote:start -->
> Stormbound5 said: Love this longer and more in depth Dev Diary, the culture rework looks fantastic so far. Will every culture receive unique traditions, or is it only a select few? And are Men at Arms types which were locked behind innovations now tied to tradition? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> VectorMaximus said: Will it be possible for a culture to have more than one designated language? I'm thinking as one of the mod team members for Realms in Exile, a lot of the cultures in Middle-Earth speak multiple language - a Noldor elf likely speaks Westron, Sindarin and Quenya, a Rohirrim speaks Westron and Rohirric, a Gondorian speaks Westron and Sindarin, etc. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> vyshan said: Ooh this looks cool. One thing I am wondering about is what about Languages that come into existance during this time frame? Things like Hindi which did not exist at either start date and came about with the various Turkish and Persian empires*. Or how English changed from Old English to Middle English. *Hindustani also shouldn't be a culture at start but a melting port culture. Click to expand...
<!-- artifact:quote:end -->
We have a fair amount of both widely available traditions, as well as unique traditions. Some are culture specific, others are for a heritage. Most cultures will have a healthy mix of both. We wanted to keep the language feature fairly simple for now, so a culture will only have a single language. More on stuff like this in future DDs. We don't do anything to introduce new languages over time specifically though.

## Reply 20 — participant_018 · 2021-06-15 · post-27618746

Nice, I always hoped that PDS would do something like this to Cultures in their games. Hopefully other PDS games do something similar. A few questions though: 1. Do cultures diverge only due to player choice, or can events cause divergences as well? 2. Can cultures fuse? 3. Are faiths connected to cultures in any way? Like cultures having a favored religion?

## Reply 21 — participant_019 · 2021-06-15 · post-27618750

Looks great! Anything about cultures that fade into obscurity? I mean, in this game you can rule over a certain culture and that culture will eventually disappear. It is assimilated into your own. Can there be a way for cultures to emerge from this obscurity? Maybe a way to never have them fully disappear, but rather be somehow present (via hidden modifiers) on the map? These cultures would still spawn their own characters and could emerge and be dominant in certain provinces, if some conditions are met.

## Reply 22 — participant_020 · 2021-06-15 · post-27618754

This looks interesting. I have some questions: -> Are there any plans to also implement an "acceptance" mechanic like this for faiths/religions as well, or will they stay at the evil/hostile/astray system? -> In a hypothetical culture/faith combo where on gender is rulers and the other is commanders/knights, how would the martial lifestyle be handled? Since your gender as the ruler "shouldn't" be engaged in martial activities? -> Will it be more difficult to convert to a different culture? Do I need to learn the language first before I can convert? Will counties be easier/harder to convert based on similarity? -> What if I don't like the traditions or ethos of my culture? Can I change them as the culture head, or do I have to diverge?

## Reply 23 — participant_021 · 2021-06-15 · post-27618755

my worry is that just as religions all blend together and feel pointless now, so too will culture. and the idea of creating a culture just seems way too absurd. reminder that the way English culture is formed in CK3 was already far worse than in CK2, and now we will have things like this normalized and engrained in the game... I just don't like the concept at all

## Reply 24 — participant_022 · 2021-06-15 · post-27618756

So, chivalrous cultures like bad poetry, huh? I mean, not everyone is fond of trouvères, but this seems a bit harsh.

## Reply 25 — participant_023 · 2021-06-15 · post-27618758

<!-- artifact:quote:start -->
> Servancour said: An example of these would be Basque, who really don't have any closely related languages and it wouldn’t make too much sense to group them together with their neighbors. The vast majority of cultures share a language though, as a sort of “language group” rather than a specific language. Click to expand...
<!-- artifact:quote:end -->
Please PLEASE do not make the mistake of thinking that the basque nobility spoke basque when they spoke indeed castillian. Dont break the game balance adding issues that didn't exist in the past based on today's prejudices of the modern era. BAsque until recently in history wasn't spoken except by rural folk in the Basque mountains. Same as with the anglo saxon's being inventive. Anglo saxon in the middle ages were anything but invented and their lands certainly didnt have an exceptional development superior to the rest. PLEASE don't develop the game based on modern times stereotypes and recent history.

## Reply 26 — participant_024 · 2021-06-15 · post-27618760

With the culture overhaul is there any chance you will revert the bizarre change that made Finns and Estonians look like they are East Asian?

## Reply 27 — participant_021 · 2021-06-15 · post-27618761

<!-- artifact:quote:start -->
> cristofolmc said: Please PLEASE do not make the mistake of thinking that the basque nobility spoke basque when they spoke indeed castillian. Dont break the game balance adding issues that didn't exist in the past based on today's prejudices of the modern era. BAsque until recently in history wasn't spoken except by rural folk in the Basque mountains. Same as with the anglo saxon's being inventive. Anglo saxon in the middle ages were anything but invented and their lands certainly didnt have an exceptional development superior to the rest. PLEASE don't develop the game based on modern times stereotypes and recent history. Click to expand...
<!-- artifact:quote:end -->
this system invites these problems because the ethos are in fact just baked in stereotypes about warrior cultures, poet cultures etc.

## Reply 28 — participant_017 · 2021-06-15 · post-27618763

Question: do we have a counter to tribal cultures since they can earn renown much much faster than feudal? Does it mean they will be more culturally developed by the end? That is kinda hilarious how a bunch of barbs is more cultured than your esteemed knight LOL.

## Reply 29 — participant_025 · 2021-06-15 · post-27618764

*Chef's Kiss* Beautiful!

## Reply 30 — participant_026 · 2021-06-15 · post-27618766

I'm very curious about how the cultural splits will work with what aspects they inherit. If Dyre the Stranger makes himself a new culture to blend Norse and Russian, will they speak Norse by default? Will it have North Germanic or Slavic heritage? Will he keep his Viking men at arms?

## Reply 31 — participant_027 · 2021-06-15 · post-27618768

Some modding related questions: How will this affect Communal Identity? Will some innovations be changed into traditions or pillars? Does the Tradeport bonus mean a duplicated building line or more modding tools? How does it affect the culture creation decisions and events like the Norse culture split, the Norman culture creation, or Outremer

## Reply 32 — participant_028 · 2021-06-15 · post-27618773

<!-- artifact:quote:start -->
> Servancour said: Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Servancour said: also able to learn multiple languages over their lifetime Click to expand...
<!-- artifact:quote:end -->
What does Available Mercenary Companies do? Will we see a lingua franca system? Imagine a Greek ruler ruling over their Egyptian and Italian subjects, both subjects have to learn to speak a lingua franca (Greek in this case as the official language used in court). Both subjects have to learn the language to be able to communicate better (better opinion bonus, sway power, plot power etc)? Also would be interesting if traces of foreign languages such as Arabic, Latin, Greek could be reflected in local communities. (eg: Middle east Muslims - Arabic; European Catholics - Latin; Greek, Coptic, Syriac, etc in a revived Orthodox ERE game)

## Reply 33 — participant_029 · 2021-06-15 · post-27618774

Excellent work, I can't wait to play around with the new culture feature.

## Reply 34 — participant_030 · 2021-06-15 · post-27618775

Looks great guys, thanks for this work.

## Reply 35 — participant_031 · 2021-06-15 · post-27618776

Excellent, I always wanted something like that in CK2. One question: Does reworked Cultural Acceptance means that, for example, AI will finally stop maniacally converting everything to their culture?

## Reply 36 — participant_001 · 2021-06-15 · post-27618778

<!-- artifact:quote:start -->
> fodazd said: This looks interesting. I have some questions: -> Are there any plans to also implement an "acceptance" mechanic like this for faiths/religions as well, or will they stay at the evil/hostile/astray system? -> In a hypothetical culture/faith combo where on gender is rulers and the other is commanders/knights, how would the martial lifestyle be handled? Since your gender as the ruler "shouldn't" be engaged in martial activities? -> Will it be more difficult to convert to a different culture? Do I need to learn the language first before I can convert? Will counties be easier/harder to convert based on similarity? -> What if I don't like the traditions or ethos of my culture? Can I change them as the culture head, or do I have to diverge? Click to expand...
<!-- artifact:quote:end -->
1. No plans for doing something similar for faiths, no. 2. We don't do anything to block the martial lifestyle. You'll be able to pick it as any character just like you can do at the moment. 3. You won't have to first learn the language in order to convert, but we could probably add a converstion cost bonus (or something similar) if you do. 4. Creating a new culture will be the way for you to change traditions, but we'll go into detail of how that works in a future DD.

## Reply 37 — participant_032 · 2021-06-15 · post-27618781

I don't want to be nice to my vassals, they always revolt against me!

## Reply 38 — participant_033 · 2021-06-15 · post-27618782

Thank you for this very juicy DD With the aesthetics, can we expect more 2D and 3D holding graphics with the upcoming expansion?

## Reply 39 — participant_034 · 2021-06-15 · post-27618784

How many traditions are there going to be, total?

## Reply 40 — participant_035 · 2021-06-15 · post-27618786

Just to be more clear on the topic: will the currently existing cultural specific innovations (e.g. raiding in major rivers, reconquista, huscarls) be transformed into traditions?

## Reply 41 — participant_017 · 2021-06-15 · post-27618787

<!-- artifact:quote:start -->
> Zhetone said: this system invites these problems because the ethos are in fact just baked in stereotypes about warrior cultures, poet cultures etc. Click to expand...
<!-- artifact:quote:end -->
My opinion: I hope that these considerations won't affect the game and make it less fun just because they want to be as neutral as possible and make everything boring and standard. Uniqueness is kinda hard if you can't stereotype. There has to be a layer of abstraction that make these nuance things less daunting and more fun to play with and I'm okay with a bit of stereotyping.

## Reply 42 — participant_036 · 2021-06-15 · post-27618788

Seems like a people of hats trope situation where because you belong to a people you all have the same characteristics like being a warrior or something. Still interesting, and it'll be nice to get some more cultures. I predict Arpitan, Carinthian (based on the observation here) and maybe some more Italian cultures. Will be very interesting what you do with India. Also glad to see some things we attribute to specific cultures being made more general to apply to more cultures. I did not know the Oriya were seafarers but that's the type of things we want to see more of. It can't all be about Vikings.

## Reply 43 — participant_037 · 2021-06-15 · post-27618789

You mentioned opinion modifiers between cultures based on religion - so does each culture have a "default" religion and can that be changed? For example the Galician culture is split between Catholicism and Islam at game start, will they be able to change that depending on how the reconquista goes?

## Reply 44 — participant_038 · 2021-06-15 · post-27618793

<!-- artifact:quote:start -->
> Acceptance is also reactive. Taking certain actions towards characters of a different culture will have consequences on your acceptance, such as declaring war or revoking titles. This generally scales on size. While the difference isn’t huge, revoking a single county from a small culture will decrease your acceptance more than if you would revoke a county from a much larger culture. At the end of the day, if you want to maintain a high acceptance and keep your Occitan vassals in France happy, you are at least gonna have to try and be nice to them. Click to expand...
<!-- artifact:quote:end -->
Sounds like the best way to deal with Occitan vassals would be just making every vassal French and then culture converting, just like now

## Reply 45 — participant_039 · 2021-06-15 · post-27618794

I wonder if the AI will create cultures and how it will pick traditions.

## Reply 46 — participant_040 · 2021-06-15 · post-27618796

<!-- artifact:quote:start -->
> Servancour said: If cultures exist within the same realm though, it [acceptance] will increase over time. Click to expand...
<!-- artifact:quote:end -->
It would be interesting in future iterations to add what would be inter-ethnic/culture tensions within a realm based on governance. So if all counties where culture Y is present in my realm are handled by counts/dukes of culture Z, I expect culture Y to not really like culture Z even though they are in the same realm -- one is discriminated, the other no. But definitely future work I guess.

## Reply 47 — participant_036 · 2021-06-15 · post-27618798

Can you tell us about changes to Innovations? Are there plans for them in Royal Court?

## Reply 48 — participant_041 · 2021-06-15 · post-27618799

Looks very promising, although I'm a bit hesitant about balancing and power creep, as a synergized Culture and Religion could result in some pretty ridicolous combinations. And this isn't even taking into accounts the bonuses gained from a court and artifacs.

## Reply 49 — participant_042 · 2021-06-15 · post-27618800

Quick question. There are currently lifestyle bonuses that decrease the cost of reforming faith. Will cultures get something similar?

## Reply 50 — participant_001 · 2021-06-15 · post-27618801

<!-- artifact:quote:start -->
> Theyn_T said: Some modding related questions: How will this affect Communal Identity? Will some innovations be changed into traditions or pillars? Does the Tradeport bonus mean a duplicated building line or more modding tools? How does it affect the culture creation decisions and events like the Norse culture split, the Norman culture creation, or Outremer Click to expand...
<!-- artifact:quote:end -->
1. Communal Identity should remain largely unaffected and retain the effects it has on conversion and promote culture. 2. Yes. Most of the Men-at-Arms traditions have been converted into traditions. Those innovations were mostly framed around a "cultural" theme anyway, so it made a lot of sense to move them over to the new system. 3. New modding potential! 4. You'll still be able to adopt new cultures like this. We'll go into further details when we talk more about culture creation.

## Reply 51 — participant_028 · 2021-06-15 · post-27618806

<!-- artifact:quote:start -->
> Servancour said: Ethos Each ethos is framed around a particular theme that somehow ties into a fairly broad definition of what a culture is. A culture’s ethos not only provides effects and bonuses for having it, it also ties into how easy or difficult it is to acquire certain traditions (more on this further down). Click to expand...
<!-- artifact:quote:end -->
Can you change your Ethos? This should reflect cultural 'sterotype', personally I like this. IMO one should not be allowed to change their ethos left and right.. Will we have cultural differences separated by religion(post Islamisation & Arabisation), reflected (from CK2)? Such as Muslim Egyptian vs Christian Copts, Lebanese/Mashriqi Arabic vs Syriac Christians?

## Reply 52 — participant_043 · 2021-06-15 · post-27618809

So some concerns and suggestions to prevent those from being a thing. Currently it seems like there is no way to change the traditions a culture has without diverging to a new culture. This means that if you intend to play as for example the french culture, but not start as its culture head, you will end up with the AI choosing a few of those limited tradition slots. Forcing the player into either playing with those traditions or not be french culture. I therefore would suggest adding the ability to replace old traditions with different ones to reflect cultures changing over time (and simultaneously making it so you can 'fix' AI decisions). This could for example have an extra cost on top of the existing prestige cost of adopting said tradition. (say 50% extra prestige). Secondly a question regarding the aesthetics choice. It seems to imply clothing, naming schemes, coat of arms, architecture, and unit models are all locked together. Character ethnicity isn't mentioned at all but I would assume those are in this group as well or maybe in the heritage one? Regardless locking it together would mean it is impossible to diverge into a culture that uses middle eastern clothing, but greek coat of arms and architecture. with west european title names. If this is indeed the case then I would suggest to maybe separate a few of those or merge them into other categories. So that it would be possible to use for example all of the greek bits. Names, architecture, etc, but then have middle eastern or western clothing. Of course my main concern is the traditions being immutable once chosen unless you explicitly stop being that culture (by creating a new one) And I believe I am not alone in this. The secondary concern of not being able to mix and match different parts of the current aesthetic pillar is, well secondary, but nonetheless not nonexistent. I therefore hope these two parts might be reconsidered at least a bit.

## Reply 53 — participant_044 · 2021-06-15 · post-27618810

Will there be language learning opportunities for children? Say if there educator, parents, or a close peer is multilingual?

## Reply 54 — participant_045 · 2021-06-15 · post-27618811

<!-- artifact:quote:start -->
> Vladisvlach said: I better not open up the game and see it say that the Vlachs speak a Slavic language. Click to expand...
<!-- artifact:quote:end -->
I am betting that they will either speak Latin or Eastern Latin but maybe the share the heritage of South Slavs.

## Reply 55 — participant_046 · 2021-06-15 · post-27618815

How does ethnicity tie into this system for new generated characters in a particular culture?

## Reply 56 — participant_047 · 2021-06-15 · post-27618820

Time to revive the legacy of the Indo-Norse

## Reply 57 — participant_048 · 2021-06-15 · post-27618822

This is looking fantastic. I have a suggestion, and a question. The Suggestion : I think it'd be a neat idea to gain culture acceptance if you have provinces ruled by counts of their culture. Or you can lose culture acceptance if provinces are ruled by a count who is from a different culture. The Question : What happens with the ethnicity if you create a new melting pot culture. Say for example the Norse in India. What will the ethnicity of randomly generated characters of the new culture be ?

## Reply 58 — participant_001 · 2021-06-15 · post-27618826

<!-- artifact:quote:start -->
> Sylas said: Thank you for this very juicy DD With the aesthetics, can we expect more 2D and 3D holding graphics with the upcoming expansion? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> CassCD said: How many traditions are there going to be, total? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Voy said: Can you tell us about changes to Innovations? Are there plans for them in Royal Court? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Thranitt said: Looks very promising, although I'm a bit hesitant about balancing and power creep, as a synergized Culture and Religion could result in some pretty ridicolous combinations. And this isn't even taking into accounts the bonuses gained from a court and artifacs. Click to expand...
<!-- artifact:quote:end -->
We don't have anything for holdings graphics in the expansion, sadly. The focus is on the Royal Court itself. We have well over a hundred at the moment, but we'll have to wait and see how many we'll actually end up with! As I mentioned in a previous post. Some innovations, most notebly some of the Men-at-Arms innovations, have been converted into being traditions instead. Other than that, no major changes have been done. A well warranted concern. While we do have traditions that do provide you with bonuses, our approach has been to focus on adding variety and making things feel different when playing as different cultures. Some traditions might give you niche bonuses that won't always be useful, or give you a bonus at the cost of something else, forcing you to a trade off. With that said, we'll keep balance in mind to avoid blatant stat inflation and power creep.

## Reply 59 — participant_049 · 2021-06-15 · post-27618833

Will views of gender of faiths still be a thing? At least they should decide who could be a priest. For example, you can't make a man vestalis, while galli of Cybele are often eunuch.

## Reply 60 — participant_050 · 2021-06-15 · post-27618837

Awesome! 1. Will having a male only Martial culture prevent the AI from picking martial education for girls? I really think it should. 2. Will the Spiritual Ethos give a control growth modifier to all counties, or only "same faith" counties?

## Reply 61 — participant_051 · 2021-06-15 · post-27618842

A pretty minor point, but if a child grows of one culture until a reasonable age (say, 10), and then is educated into another culture, will he automatically speak both cultures' respective languages?

## Reply 62 — participant_052 · 2021-06-15 · post-27618848

It would be really cool have bad cultural things and traditions, and don't be completely good things, like imperialist, give you prestige/levy/tecnological-progress but people of other countrys dislikes you more, and after 100 years for example give the rulers of the culture a trait of decadency. Or just more simple things that the people of your culture is lazy. And one more thing, i really, but really want truly is events of tradition and changes on it. Of course will be events, but i mean more for the roleplay the character and be like more on ck2 that just casually happen and don't big matter, i expect minimum a big repertoire of events for each trait of the culture and variants on it if the event in question do some combination with other trait of the culture. If this BIG DLC is not like this as minimum, i will be disappointed about all this game. I am saying all this here because i don't speak anywhere to developers or something, so i say it here and now because it really cares me this DLC that will mean a lot for me and the game.

## Reply 63 — participant_053 · 2021-06-15 · post-27618857

How will flavourization work from now on ? If there are special names for Welsh titles for example, will they stay the same for a new culture "based" on Welsh ? EDIT: Also regarding flavourization modding will the creation of special title names stay the same ? For example simply specifying that the flavourized title is for "cultures = { welsh }" ?

## Reply 64 — participant_021 · 2021-06-15 · post-27618858

<!-- artifact:quote:start -->
> RAINWORS said: It would be really cool have bad cultural things and traditions, and don't be completely good things, like imperialist, give you prestige/levy/tecnological-progress but people of other countrys dislikes you more, and after 100 years for example give the rulers of the culture a trait of decadency. Or just more simple things that the people of your culture is lazy. And one more thing, i really, but really want truly is events of tradition and changes on it. Of course will be events, but i mean more for the roleplay the character and be like more on ck2 that just casually happen and don't big matter, i expect minimum a big repertoire of events for each trait of the culture and variants on it if the event in question do some combination with other trait of the culture. If this BIG DLC is not like this as minimum, i will be disappointed about all this game. I am saying all this here because i don't speak anywhere to developers or something, so i say it here and now because it really cares me this DLC that will mean a lot for me and the game. Click to expand...
<!-- artifact:quote:end -->
making cultures have negative stereotypes is how people get outraged and accuse paradox of discrimination

## Reply 65 — participant_054 · 2021-06-15 · post-27618859

Very good, I like most of what I see. However, I'm a bit troubled by ethos being the defining headliner and probably locked. After all some cultures tended to change ethos every century depending on the zeitgeist. (Like Swedish going Bellicose or Spiritual to Inventive to Egalitarian over the last 300 years.)

## Reply 66 — participant_001 · 2021-06-15 · post-27618861

<!-- artifact:quote:start -->
> Turean said: Quick question. There are currently lifestyle bonuses that decrease the cost of reforming faith. Will cultures get something similar? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> tribnia said: Will views of gender of faiths still be a thing? At least they should decide who could be a priest. For example, you can't make a man vestalis, while galli of Cybele are often eunuch. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> TheMongoose said: Awesome! 1. Will having a male only Martial culture prevent the AI from picking martial education for girls? I really think it should. 2. Will the Spiritual Ethos give a control growth modifier to all counties, or only "same faith" counties? Click to expand...
<!-- artifact:quote:end -->
We might have a tradition or two that may or may not affect things such as creating or reforming a faith... The different doctrines remains unchanged, outside of the main gender doctrine. Which, as mentioned in the DD, no longer affects who can be a knight or commander. 1. As far as I know, it won't affect the AI for picking education. Might be something to consider though, but I would never want to block it completely. 2. This modifier in question is added to a character, so you will always be able to benefit from it.

## Reply 67 — participant_055 · 2021-06-15 · post-27618862

I liked everything I heard here but I have one request Being that cultures will adopt new traditions as they game goes on. Please, please, PLEASE allow a custom game rule for the AI to follow historicity or a "script" of historical traditions, or at least follow logic. Bordergore and religiongore are one thing, but I don't think I can deal with culturegore too.

## Reply 68 — participant_056 · 2021-06-15 · post-27618865

I'm sorry but I don't like this at all. First off it associates many sterotypes to predetermined cultures (some of these are just absurd... Anglo Saxon inventive??), but my main issue is that it feels too artificial and player guided, same as religion. How many cultures in history were created ex-novo from the decision of a King or Emperor? It could certainly be a factor, but these sort of changes should be 90% dictated by factors external to player, to which one should react to. EDIT, because I did not see a reply from the devs stating that the only way to change a tradition is to create a new culture... how does this make cultures more dynamic? If anything it makes them more static. The game should be able to mimic the way cultures evolved in the span of 600 years. How can it makes sense that without player intervention 9th century Frankish kingdoms have the same culture as mid 15th century France? Please devs do correct me if I did not understand correctly. I have the feeling that you are trying to add su much diversity into this game, but it's ending up making it more... bland, sometimes less is more.

## Reply 69 — participant_057 · 2021-06-15 · post-27618868

<!-- artifact:quote:start -->
> cristofolmc said: Please PLEASE do not make the mistake of thinking that the basque nobility spoke basque when they spoke indeed castillian. Dont break the game balance adding issues that didn't exist in the past based on today's prejudices of the modern era. BAsque until recently in history wasn't spoken except by rural folk in the Basque mountains. Click to expand...
<!-- artifact:quote:end -->
This discussion is way to specific for the dev diary, but I just wanted to point out that this is an interesting point of view, to put it nicely. Just a few points though: - the nobility, burghers and monks in the kingdom of Navarra mostly spoke Occitan, not Castilian - there were Basque nobles who spoke Basque as their native and everyday language; one famous example being Joan Pérez de Lazarraga, author of the eponymous manuscript - the fact that the reformation of the Church of Navarra by Jeanne d'Albret required a translation of the bible into Basque is somewhat demonstrative of the fact that it was widely spoken among the populace; the fact that there is evidence of Basque-Icelandic and Basque-Algonquian pidgin languages having developed in the 16th century shows that the Basque fishermen and whalers who ventured Northwest used their language (and not Castilian) as a matter of course. Usage of Basque was successfully suppressed by a centralist Spanish state beginning the 18th century, resulting indeed in the language being limited mostly to remote villages before the transition to democracy, but that was long after the period covered by CK3. A little more on topic: love this dev diary and the new concept of cultures

## Reply 70 — participant_021 · 2021-06-15 · post-27618870

<!-- artifact:quote:start -->
> Shogun96 said: I'm sorry but I don't like this at all. First off it associates many sterotypes to predetermined cultures (some of these are just absurd... Anglo Saxon inventive??), but my main issue is that it feels too artificial and player guided, same as religion. How many cultures in history were created ex-novo from the decision of a King or Emperor? It could certainly be a factor, but these sort of changes should be 90% dictated by factors external to player, to which one should react to. I have the feeling that you are trying to add su much diversity into this game, but it's ending up making it more... bland, sometimes less is more. Click to expand...
<!-- artifact:quote:end -->
yes... imagine a ruler saying "ok we aren't Greek anymore, we're merging our culture with with the Hungarians so you better all learn a bunch of their words" or something. it's absurd. I get that they want player control over mechanics but the game keeps moving farther away from any sort of realism and it's a bother for me

## Reply 71 — participant_058 · 2021-06-15 · post-27618872

<!-- artifact:quote:start -->
> Servancour said: An example of these would be Basque, who really don't have any closely related languages Click to expand...
<!-- artifact:quote:end -->
Good work there. Looking nice! A couple of questions: Can a culture have more than one language? I ask it mainly because of this case: While that is completely correct it is true too that there seems to have existed a high degree of bilingualism in the Medieval Basque population, being Basque the spoken language and Romance or Spanish the written one, at least for the elite of nobilitiy and town people. Most of the Basque and Navarrese documents and legal codes were written in Spanish, and only a letter mixing Spanish and Basque exist as a written document for the period (the letter by Machin de Zalba to Martín de San Martín in 1416). To have Basques not understanding Spanish would be very odd given that Spanish was so omnipresent as a Municipal, Goverment and Literarly language. Probably that is also the case for other Cultures in this timeframe: maybe England with English and French, Aragon with Catalan and Aragonese, etc. Also, I suppose that the access that Basque, Aragonese, Catalan and Occitan have to Gender Equal Succession and High Partition will become a tradition now. Is that the case? If so, it can be the perfect opportunity to correct a certain historicity issue caused by it

## Reply 72 — participant_059 · 2021-06-15 · post-27618878

<!-- artifact:quote:start -->
> cursorhiker said: You mentioned opinion modifiers between cultures based on religion - so does each culture have a "default" religion and can that be changed? For example the Galician culture is split between Catholicism and Islam at game start, will they be able to change that depending on how the reconquista goes? Click to expand...
<!-- artifact:quote:end -->
No it just checks if the majority religion of provinces of that culture is the same

## Reply 73 — participant_038 · 2021-06-15 · post-27618879

<!-- artifact:quote:start -->
> Unknown Sage said: Secondly a question regarding the aesthetics choice. It seems to imply clothing, naming schemes, coat of arms, architecture, and unit models are all locked together. Character ethnicity isn't mentioned at all but I would assume those are in this group as well or maybe in the heritage one? Regardless locking it together would mean it is impossible to diverge into a culture that uses middle eastern clothing, but greek coat of arms and architecture. with west european title names. Click to expand...
<!-- artifact:quote:end -->
Yeah I'm also interested in that. If for example we create Indo-Norse culture as Norse, and want to have a culture of Norsemen with Indian clothing, what will define ethnicity of new spawned characters? Will they be just Norse, just Indians in looks?

## Reply 74 — participant_014 · 2021-06-15 · post-27618885

<!-- artifact:quote:start -->
> Servancour said: 1. No plans for doing something similar for faiths, no. 2. We don't do anything to block the martial lifestyle. You'll be able to pick it as any character just like you can do at the moment. 3. You won't have to first learn the language in order to convert, but we could probably add a converstion cost bonus (or something similar) if you do. 4. Creating a new culture will be the way for you to change traditions, but we'll go into detail of how that works in a future DD. Click to expand...
<!-- artifact:quote:end -->
point 4 is especially disappointing and frustrating. They’re supposedly dynamic cultures and then you tell us that the only way cultures actually change in CK3 is by making new ones, as if cultures in 867 and 1453 were the exact same and didn’t evolve over time. This looks like a weak base that i’ll need a glut of mods to actually turn into an acceptable system, ngl.

## Reply 75 — participant_060 · 2021-06-15 · post-27618886

<!-- artifact:quote:start -->
> Shogun96 said: I'm sorry but I don't like this at all. First off it associates many sterotypes to predetermined cultures (some of these are just absurd... Anglo Saxon inventive??), but my main issue is that it feels too artificial and player guided, same as religion. How many cultures in history were created ex-novo from the decision of a King or Emperor? It could certainly be a factor, but these sort of changes should be 90% dictated by factors external to player, to which one should react to. I have the feeling that you are trying to add su much diversity into this game, but it's ending up making it more... bland, sometimes less is more. Click to expand...
<!-- artifact:quote:end -->
I get the impression the ethoses (ethosi?) shown are not necessary the ones the attached cultures will have when the DLC is released, but instead are just shown demonstratively here.

## Reply 76 — participant_056 · 2021-06-15 · post-27618889

<!-- artifact:quote:start -->
> Tuo said: I get the impression the ethoses (ethosi?) shown are not necessary the ones the attached cultures will have when the DLC is released, but instead are just shown demonstratively here. Click to expand...
<!-- artifact:quote:end -->
That's also possible, but they still need to associate some predetermined ethos to starting cultures.

## Reply 77 — participant_061 · 2021-06-15 · post-27618890

How will the AI handle the culture changes? As per design the AI never creates new religions, usually simply embraces heresies, will be the same for cultures or will the AI try to dynamically change cultures and/or convert culture?

## Reply 78 — participant_014 · 2021-06-15 · post-27618894

<!-- artifact:quote:start -->
> Unknown Sage said: Of course my main concern is the traditions being immutable once chosen unless you explicitly stop being that culture (by creating a new one) And I believe I am not alone in this. The secondary concern of not being able to mix and match different parts of the current aesthetic pillar is, well secondary, but nonetheless not nonexistent. I therefore hope these two parts might be reconsidered at least a bit. Click to expand...
<!-- artifact:quote:end -->
i second this

## Reply 79 — participant_062 · 2021-06-15 · post-27618897

This is really interesting and I'm definitely looking forward exploring all of the options but I feel like as long as partition remains the default method of inheritance military focused cultures are going to be a lot stronger and more useful than other types simply because they allow you better maintain an intact realm.

## Reply 80 — participant_055 · 2021-06-15 · post-27618899

<!-- artifact:quote:start -->
> peaswar said: point 4 is especially disappointing and frustrating. They’re supposedly dynamic cultures and then you tell us that the only way cultures actually change in CK3 is by making new ones, as if cultures in 867 and 1453 were the exact same and didn’t evolve over time. This looks like a weak base that i’ll need a glut of mods to actually turn into an acceptable system, ngl. Click to expand...
<!-- artifact:quote:end -->
You're taking his response out of context. The original question was "Can I change an ethos if I don't like it" obviously it makes sense that you can't simply change a whole cultural ethos at the whim of a king. IMO "creating a new culture" should be something that takes generations of effort by multiple monarchs to achieve not something that should be able to be done at the click of a button. Besides, read the dev diary, It clearly states that each culture has a max 5 traditions and only starts with 2 or 3. Cultures WILL change as the game progresses. This will obviously be more pronounced as Norse diverges into Swedish or Norman diverges into English etc.

## Reply 81 — participant_014 · 2021-06-15 · post-27618903

<!-- artifact:quote:start -->
> Scrambles said: You're taking his response out of context. The original question was "Can I change an ethos if I don't like it" obviously it makes sense that you can't simply change a whole cultural ethos at the whim of a king. IMO "creating a new culture" should be something that takes generations of effort by multiple monarchs to achieve not something that should be able to be done at the click of a button. Besides, read the dev diary, It clearly states that each culture has a max 5 traditions and only starts with 2 or 3. Cultures WILL change as the game progresses. This will obviously be more pronounced as Norse diverges into Swedish or Norman diverges into English etc. Click to expand...
<!-- artifact:quote:end -->
i referenced this in a thread i made earlier as well as my first comment in this threat. Ethoses not changing at all, even over generations (which is the case here in CK3) is ahistorical. While the OP did ask as you noted, the answer is still relevant to questions of whether an ethos can change over decades or centuries of a certain type of lifestyle becoming the norm for a culture—which is apparently no.

## Reply 82 — participant_021 · 2021-06-15 · post-27618907

<!-- artifact:quote:start -->
> Scrambles said: You're taking his response out of context. The original question was "Can I change an ethos if I don't like it" obviously it makes sense that you can't simply change a whole cultural ethos at the whim of a king. IMO "creating a new culture" should be something that takes generations of effort by multiple monarchs to achieve not something that should be able to be done at the click of a button. Besides, read the dev diary, It clearly states that each culture has a max 5 traditions and only starts with 2 or 3. Cultures WILL change as the game progresses. This will obviously be more pronounced as Norse diverges into Swedish or Norman diverges into English etc. Click to expand...
<!-- artifact:quote:end -->
or it should just be an organic process. why would a dynasty even over generations be able to "create" a culture. this is more Sims-ification of CK

## Reply 83 — participant_063 · 2021-06-15 · post-27618908

This is hands down my favourite CK3 DD so far, great work PDS! Will the counties still have only one predominant culture or can we expect a little more intercultural mixing on the county level apart from just the character level?

## Reply 84 — participant_064 · 2021-06-15 · post-27618909

Maybe such dynamic culture system could also be added in other games, such as eu4 or vic3?

## Reply 85 — participant_014 · 2021-06-15 · post-27618916

<!-- artifact:quote:start -->
> Zhetone said: or it should just be an organic process. why would a dynasty even over generations be able to "create" a culture. this is more Sims-ification of CK Click to expand...
<!-- artifact:quote:end -->
There has to be a certain abstraction in these types of games and you could easily perceive the creation of a culture as something like a royal decree that ‘X nation is far too different from our neighbors to call ourselves french, we are now Xians’ where you’re not really ‘creating the culture’ as much as declaring it to be differentiated. That said, I do agree that a completely organic culture process would be far preferable, considering that things like ethos and traditions (once they’re set) are immutable and static.

## Reply 86 — participant_055 · 2021-06-15 · post-27618927

<!-- artifact:quote:start -->
> peaswar said: i referenced this in a thread i made earlier as well as my first comment in this threat. Ethoses not changing at all, even over generations (which is the case here in CK3) is ahistorical. While the OP did ask as you noted, the answer is still relevant to questions of whether an ethos can change over decades or centuries of a certain type of lifestyle becoming the norm for a culture—which is apparently no. Click to expand...
<!-- artifact:quote:end -->
Can you name a single culture which, over the time the game takes place, went on to accept warrior women or changed languages without a SIGNIFICANT paradigm shift as large as the Norse becoming Swedish or the Normans and Anglo-Saxons mingling to become English?

## Reply 87 — participant_065 · 2021-06-15 · post-27618930

This all sounds amazing! Great job! I'm looking forward to the future DD's and eventually seeing it in the game

## Reply 88 — participant_066 · 2021-06-15 · post-27618931

Are "latin" cultures going to be represented in some ways? Would it be like "romance languages" or "latin heritage" or none?

## Reply 89 — participant_053 · 2021-06-15 · post-27618934

<!-- artifact:quote:start -->
> Zhetone said: or it should just be an organic process. why would a dynasty even over generations be able to "create" a culture. this is more Sims-ification of CK Click to expand...
<!-- artifact:quote:end -->
Well it is probably an abstract way to represent the split of a new culture or the emergence of a new culture based on multiple cultures living together in a realm. I guess it shouldn't be understood that the ruler literally creates the culture, it is probably just a way to allow the whole affair to be controled by the player if they wish to. Creating a new culture probably just aknowledges that a split or merger of cultures has gradually happened.

## Reply 90 — participant_067 · 2021-06-15 · post-27618936

<!-- artifact:quote:start -->
> Servancour said: 1. No plans for doing something similar for faiths, no. Click to expand...
<!-- artifact:quote:end -->
If you do eventually come around to making shared heads of faith, this mutual acceptance of say insular christians with mainland catholics could work nicely. Maybe even split papacies can not only create a ripple in faiths, but that ripple can be felt in cultures, so that you might end up with cultural differences which were kinda encouraged to evolve because of faith disputes. Anyway, the dev diary shows great stuff. I can hardly wait to mold some cultures in fun ways. Pirates of the mediterranean culture here I come!

## Reply 91 — participant_068 · 2021-06-15 · post-27618947

Wow I love this, I can imagine the playing as a Viking adventurer and settling new lands and founding new cultures. Also imagine all the mods, creating elves and dwarves and making them feel truly unique! Great job!

## Reply 92 — participant_069 · 2021-06-15 · post-27618948

Please make it possible to merge all the german cultures into a one unified one.

## Reply 93 — participant_070 · 2021-06-15 · post-27618953

What about Slavic languages? AFAIK back then they weren't that different from each other and their more noticeable split happened later than in some other language groups, hence projects like interslavic or neoslavonic languages that are mostly understood by every Slav without studying it today.

## Reply 94 — participant_014 · 2021-06-15 · post-27618956

<!-- artifact:quote:start -->
> Scrambles said: Can you name a single culture which, over the time the game takes place, went on to accept warrior women or changed languages without a SIGNIFICANT paradigm shift as large as the Norse becoming Swedish or the Normans and Anglo-Saxons mingling to become English? Click to expand...
<!-- artifact:quote:end -->
I think you’ve misunderstood or are intentionally misrepresenting my point. I’m referring mainly to ethoses. Arabia in 867 would historically perhaps be most accurately categorized as ‘Inventive’ but by 1453, the Islamic Golden Age would be for the most part over and I think that there’s a fair few other options for Ethoses that would better represent them (although scientific research was still a key aspect). Traditions are more understandably difficult to change, but to give an example, a focus on grandiose temple building died out among the Tamil kings after the 1200s, as did a seafaring traders dynamic. These traditions no longer existed in Tamil culture but Tamil culture also hadn’t become its own thing.

## Reply 95 — participant_071 · 2021-06-15 · post-27618959

Okay, this is really good. Man I can't wait for the release. Please come out soon.

## Reply 96 — participant_072 · 2021-06-15 · post-27618960

<!-- artifact:quote:start -->
> Servancour said: At the end of the day, if you want to maintain a high acceptance and keep your Occitan vassals in France happy, you are at least gonna have to try and be nice to them. Click to expand...
<!-- artifact:quote:end -->
Okay, my main wish with cultural acceptance, and something I kind of wanted to be in the game at launch: The ability to recruit courtiers from minority cultures within your realm with a simple click of a button in the same way you can generate nobles of your own culture with Invite Noble/Debutante. I know rulers in minority culture realms convert to the native culture usually in the current version, but I'd like the ability to be able to manually give conquered land to minority cultures who don't have any pre-existing characters. Like, could this French king, if he somehow inherited Toulouse but wanted to give it to a new vassal, generate a new Occitan vassal to give it to? In CK2 some cultures that existed early game just ended up dead in the water very early on because they just have no landed people to represent them and no possibility of ever having landed people to represent them. This comes from the position of someone who likes to play characters representing tiny cultures with little representation but doesn't like custom settings or characters.

## Reply 97 — participant_042 · 2021-06-15 · post-27618971

<!-- artifact:quote:start -->
> Servancour said: We might have a tradition or two that may or may not affect things such as creating or reforming a faith... Click to expand...
<!-- artifact:quote:end -->
Sorry if I phrased it wrong. I meant will there be any rework of lifestyle perks? For example, there is a "Prophet" perk that lowers the piety cost of reforming faith. Just wondering if we'll have something similar that lowers the prestige cost of reforming culture.

## Reply 98 — participant_073 · 2021-06-15 · post-27618973

<!-- artifact:quote:start -->
> Servancour said: The naming practice will also be used to change title and holding names, which used to be set per culture, so as to not have titles change names if you create a new culture. Click to expand...
<!-- artifact:quote:end -->
I think names should be kept separate from these, and also to have the ability to use both styles of names if possible.

## Reply 99 — participant_074 · 2021-06-15 · post-27618975

How does converting province steward task work now?

## Reply 100 — participant_075 · 2021-06-15 · post-27618977

Norse-Dutch here we come!

## Reply 101 — participant_076 · 2021-06-15 · post-27618980

Very glad I bought the Royal Edition. Interested to see how the mechanics will work and how it will play with the Ruler Designer. Will you be able to create a ruler with a unique culture and then convert your subjects to it like now or will it be more linear?

## Reply 102 — participant_072 · 2021-06-15 · post-27618981

<!-- artifact:quote:start -->
> HistoryBoyClub said: I think names should be kept separate from these, and also to have the ability to use both styles of names if possible. Click to expand...
<!-- artifact:quote:end -->
Yeah, I don't think naming the land you live in after the dynasty that rules it is anything inherent to people who wear middle eastern garb or anything.

## Reply 103 — participant_077 · 2021-06-15 · post-27618982

Will the fact that Aesthetics, Language and Heritage are separated now mean that cultures in the same "culture group" will be able to have different architectural sets? Does this mean that for example it will be possible that Galicians/Portuguese will be able to have an Atlantic set, as opposed to the Mediterranean style of the Aragonese/Catalans? Examples of what I mean: Galician: Portuguese: Aragonese: Catalan: So right now, all Iberians use the Mediterranean set: Would it be possible for the Galician, Portuguese and Asturleonese cultures to have a different aesthetic to the Castilian/Aragonese/Catalan one? Example of an hypothetical Atlantic set:

## Reply 104 — participant_078 · 2021-06-15 · post-27618985

I'm wondering when the trait is selected that chooses names does that replace the entire name list, inject some names into the new culture's name list, or what? I'm trying to understand what that means.

## Reply 105 — participant_079 · 2021-06-15 · post-27618986

<!-- artifact:quote:start -->
> Servancour said: Aesthetics This pillar is really a collection of several smaller properties for what a culture “looks” like. It decides what type of clothes characters wear, the coat of arms style for dynasties, what architecture holdings use, and the type of armor the units on the map wear. This is also the pillar that contains what naming practices the culture uses. Mainly what character names to use, if they use a dynasty prefix, etc. The naming practice will also be used to change title and holding names, which used to be set per culture, so as to not have titles change names if you create a new culture. For all of you modders out there; all of these can be set individually per culture. Allowing you to mix and match the different aesthetics to your heart’s content. Click to expand...
<!-- artifact:quote:end -->
Incredible dev diary! But I have to ask : Wouldn't it be way more coherent to tie the naming practices to the language group and not to the Aesthetic?

## Reply 106 — participant_072 · 2021-06-15 · post-27618989

<!-- artifact:quote:start -->
> Ul90 said: Incredible dev diary! But I have to ask : Wouldn't it be way more coherent to tie the naming practices to the language group and not to the Aesthetic? Click to expand...
<!-- artifact:quote:end -->
That one completely missed me. Yeah that really makes no sense. Architecture, Fashion, Naming convention, and the way they name their countries are named all being crammed into one concept? When there's already a category for language?

## Reply 107 — participant_073 · 2021-06-15 · post-27618990

<!-- artifact:quote:start -->
> IndigoRage said: Yeah, I don't think naming the land you live in after the dynasty that rules it is anything inherent to people who wear middle eastern garb or anything. Click to expand...
<!-- artifact:quote:end -->
I meant more character's names and the like. I think you should be able to mix and match with both your ruler's culture and the local one or however it works.

## Reply 108 — participant_072 · 2021-06-15 · post-27618996

<!-- artifact:quote:start -->
> HistoryBoyClub said: I meant more character's names and the like. I think you should be able to mix and match with both your ruler's culture and the local one or however it works. Click to expand...
<!-- artifact:quote:end -->
Ah, I misread you, but someone else mentioned it and I agree. "Aesthetics" seems to cram a bunch of things together that don't necessarily have to be, and one of them is directly related to Language, another one of the categories.

## Reply 109 — participant_080 · 2021-06-15 · post-27619005

<!-- artifact:quote:start -->
> Servancour said: [Image of the Seafarers tradition] Click to expand...
<!-- artifact:quote:end -->
So only seafarer cultures can navigate rivers, huh? Shouldn't it be the other way? I'm not a sailor myself so correct me if I'm wrong but shouldn't sailing down Volga be easier than braving the high seas? Wouldn't it make more sense if all cultures were able to navigate rivers but only the seafarers could sail the seas without severe penalties? I mean, it's right there in the name.

## Reply 110 — participant_081 · 2021-06-15 · post-27619012

<!-- artifact:quote:start -->
> Jolius said: With the culture overhaul is there any chance you will revert the bizarre change that made Finns and Estonians look like they are East Asian? Click to expand...
<!-- artifact:quote:end -->
It isn’t a bizarre change since finnic people used to have more ”asiatic” features back in the day, these types of features are still present in the indigenous sámi people, eastern finns, vepsians and karelians, also the original haplogroub of finnic people was N1a which originated in Siberia. It would actually be extremely inaccurate to make the finns and estonians look like nordic vikings since that just simply wasn’t the case.

## Reply 111 — participant_082 · 2021-06-15 · post-27619013

I notice that every ethos and tradition provides purely positive bonuses. Near the end of its development, CK2 really suffered from stacking modifiers and bonuses that made characters into god-like beings, as every DLC added new bonuses. CK3 already has quite a bit of that issue - it's easy to end up with stats in the 40s or 50s, and many modifiers can be stacked to the point of absurdity. If every new DLC just piles on more and more bonuses, how will you maintain game balance?

## Reply 112 — participant_083 · 2021-06-15 · post-27619017

it would make sense to change capital of Kingdom of Georgia Tbilisi to Georgian

## Reply 113 — participant_021 · 2021-06-15 · post-27619018

<!-- artifact:quote:start -->
> Archduke of Bigbrains said: It isn’t a bizarre change since finnic people used to have more ”asiatic” features back in the day, these types of features are still present in the indigenous sámi people, eastern finns, vepsians and karelians, also the original haplogroub of finnic people was N1a which originated in Siberia. It would actually be extremely inaccurate to make the finns and estonians look like nordic vikings since that just simply wasn’t the case. Click to expand...
<!-- artifact:quote:end -->
this is a ridiculous opinion considering how insular finnish culture has been... it's not as if finns mixed with tons of people from then to now to change appearance wholesale

## Reply 114 — participant_084 · 2021-06-15 · post-27619029

Now I can't wait to see all the various traditions and ethoses... but I have a question (that I know you still can't answer, but still) : will there be some traditions that change something in the royal court system from the DLC? The royal court and the culture rework are two different things, yes, but I wonder, if you have a Courtly ethos, how will that impact your, well, royal court?

## Reply 115 — participant_085 · 2021-06-15 · post-27619031

Will the Changes in how Cultures work change certain decisions like for example Unify Italy (only Italian can do it at the moment) or Unite West/South Slavs?

## Reply 116 — participant_072 · 2021-06-15 · post-27619036

<!-- artifact:quote:start -->
> Zhetone said: this is a ridiculous opinion considering how insular finnish culture has been... it's not as if finns mixed with tons of people from then to now to change appearance wholesale Click to expand...
<!-- artifact:quote:end -->
Finno-Ugric people can range from looking generically European to looking East/Central Asian, even to the modern day. There's really no opinion about it so long as we're applying appearances across wide culture regions. It's just hard to represent. Though if we want to get really specific, modern Finns do have a certain amount of DNA from the WHG admixture that isn't nearly as present in a lot of other Finno-Ugric peoples.

## Reply 117 — participant_073 · 2021-06-15 · post-27619038

Whilst overall this looks really good, I think both Aesthetics and Language are too broad categories (aesthetics especially). Language should have names and place names split off and you should be able to choose between them. Aesthetics needs to be made much more customisable in general.

## Reply 118 — participant_086 · 2021-06-15 · post-27619048

Soo the Vlachs will still be in the South Slavic Group or are they in their own culture group (Easter Latin/Romance)?

## Reply 119 — participant_087 · 2021-06-15 · post-27619057

The best rework so far, keep doing a good job.

## Reply 120 — participant_088 · 2021-06-15 · post-27619058

I wonder how the language and cultural 'parent' will work in the new hybrid culture system. If there are Turkic-Indians are they in the Turkic group or the Indian group, will they speak a Turkic language or an Indian one?

## Reply 121 — participant_014 · 2021-06-15 · post-27619060

<!-- artifact:quote:start -->
> Fan of Daenerys said: Soo the Vlachs will still be in the South Slavic Group or are they in their own culture group (Easter Latin/Romance)? Click to expand...
<!-- artifact:quote:end -->
they’ve got to be moved to Romance, right? The language thing forces PDX’s hand, or so I’d hope

## Reply 122 — participant_001 · 2021-06-15 · post-27619063

<!-- artifact:quote:start -->
> Pz. Los said: Very glad I bought the Royal Edition. Interested to see how the mechanics will work and how it will play with the Ruler Designer. Will you be able to create a ruler with a unique culture and then convert your subjects to it like now or will it be more linear? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Ul90 said: Incredible dev diary! But I have to ask : Wouldn't it be way more coherent to tie the naming practices to the language group and not to the Aesthetic? Click to expand...
<!-- artifact:quote:end -->
You won't be able to create a new culture directly in the Ruler Designer, unfortunately. That's a fair point. However, since all cultures have their own name lists, we would have to create a language for every single culture. For gameplay purposes, we kind of like having languages overlap a bit, since it reduces opinion between cultures and adds some interesting immersion. A general note regarding the Aesthetics. While we do lump them together in the interface, they are handled separately. We put them together in the interface mostly out of convenience and as to not blot the interface. They also tie into culture creation a bit. But more on that later!

## Reply 123 — participant_014 · 2021-06-15 · post-27619071

<!-- artifact:quote:start -->
> kemmy23 said: I wonder how the language and cultural 'parent' will work in the new hybrid culture system. If there are Turkic-Indians are they in the Turkic group or the Indian group, will they speak a Turkic language or an Indian one? Click to expand...
<!-- artifact:quote:end -->
the ironic thing is the Turkic Indians (i.e. Delhi Sultanate and Mughals) spoke Farsi (and then, eventually the language of Urdu as more Farsi words were incorporated into Hindi), so neither, until a few hundreds years pass and then they’d speak an Indian language .

## Reply 124 — participant_072 · 2021-06-15 · post-27619076

<!-- artifact:quote:start -->
> Servancour said: You won't be able to create a new culture directly in the Ruler Designer, unfortunately. That's a fair point. However, since all cultures have their own name lists, we would have to create a language for every single culture. For gameplay purposes, we kind of like having languages overlap a bit, since it reduces opinion between cultures and adds some interesting immersion. A general note regarding the Aesthetics. While we do lump them together in the interface, they are handled separately. We put them together in the interface mostly out of convenience and as to not blot the interface. They also tie into culture creation a bit. But more on that later! Click to expand...
<!-- artifact:quote:end -->
Well that's better than I thought at first. It still seems more intuitive for aspects of Language and Aesthetics to be broken down into parts though. Especially since this namelist concern is brought to light. Any way I'll hold off further comment on that until we see more.

## Reply 125 — participant_089 · 2021-06-15 · post-27619085

Oh no... here comes the Paradox paradox. How am I going to play the current version now ,>O<, Oh! I know! I'll pass the time by asking stuff! I was wondering, if the culture system is taking inspiration from the faith system, can we also expect the ability to adopt "extinct" cultures that technically no longer have any counties or characters practising them, but have been well preserved in writing? ...yes I'm asking about the Roman culture (˳˘ ɜ˘) ~♪

## Reply 126 — participant_090 · 2021-06-15 · post-27619088

This looks really promising. I had my doubts about the expansion, but it seems to be a step in the right direction. Good job

## Reply 127 — participant_001 · 2021-06-15 · post-27619093

<!-- artifact:quote:start -->
> Fan of Daenerys said: Soo the Vlachs will still be in the South Slavic Group or are they in their own culture group (Easter Latin/Romance)? Click to expand...
<!-- artifact:quote:end -->
Vlach and what they look like at the moment:

## Reply 128 — participant_091 · 2021-06-15 · post-27619095

Will we be able to metge cultures like getting anglois from english and french merging

## Reply 129 — participant_092 · 2021-06-15 · post-27619098

Stop my hypeboner can only withstand so much!

## Reply 130 — participant_038 · 2021-06-15 · post-27619104

<!-- artifact:quote:start -->
> JamCom said: Will we be able to metge cultures like getting anglois from english and french merging Click to expand...
<!-- artifact:quote:end -->
It will be creating new culture, not merging existent ones

## Reply 131 — participant_093 · 2021-06-15 · post-27619109

can't wait for the changes to the cultures

## Reply 132 — participant_092 · 2021-06-15 · post-27619112

<!-- artifact:quote:start -->
> Servancour said: You won't be able to create a new culture directly in the Ruler Designer, unfortunately. That's a fair point. However, since all cultures have their own name lists, we would have to create a language for every single culture. For gameplay purposes, we kind of like having languages overlap a bit, since it reduces opinion between cultures and adds some interesting immersion. A general note regarding the Aesthetics. While we do lump them together in the interface, they are handled separately. We put them together in the interface mostly out of convenience and as to not blot the interface. They also tie into culture creation a bit. But more on that later! Click to expand...
<!-- artifact:quote:end -->
Is the creation of custom cultures something you ever plan on adding or are the prereq nature of traditions (for example making a culture that has the hill people tradition despite your starting point not having hills) something that will dissuade you from every implementing that feature?

## Reply 133 — participant_094 · 2021-06-15 · post-27619120

This is one of the best changes ever, actually. I always wanted cultures in your games to be more then just modifier. CK3 is truly new age in Paradox games. I so hope similar changes innovations gonna be in Vic3 and in EU5 in the future. Like in EU in future I'd love to see THIS. Like more simulation, of cultures, religions, regions, trade, Empire management, colony management then just simply modifiers upon modifiers. Hope that governments gonna have actual in game representation then just +5% manpower or +10% tax modifier. I love this so much.

## Reply 134 — participant_095 · 2021-06-15 · post-27619124

I think it would be cool for bellicose cultures to have a resistance to the "long offensive war" penalty bc the flavor text seems to fit that description. Really good dd as well

## Reply 135 — participant_079 · 2021-06-15 · post-27619127

<!-- artifact:quote:start -->
> Servancour said: That's a fair point. However, since all cultures have their own name lists, we would have to create a language for every single culture. For gameplay purposes, we kind of like having languages overlap a bit, since it reduces opinion between cultures and adds some interesting immersion. A general note regarding the Aesthetics. While we do lump them together in the interface, they are handled separately. We put them together in the interface mostly out of convenience and as to not blot the interface. They also tie into culture creation a bit. But more on that later! Click to expand...
<!-- artifact:quote:end -->
Thank you very much, that's an extremely interesting answer. I'm eager to learn more. I'll try my luck with another question : What are the differences in aesthetic choices between divergence and hybridation when creating a new culture? If I am French and diverge into a new culture, do I only have access to French Aesthetic or to any other aesthetic on the map? Same question for hybridation, if I create a hybrid culture French-German, do I have access to only French and German Aesthetic?

## Reply 136 — participant_060 · 2021-06-15 · post-27619131

Can we assume rulers can lead their own armies regardless of the Noble Martial Custom of their culture?

## Reply 137 — participant_096 · 2021-06-15 · post-27619139

<!-- artifact:quote:start -->
> daniloy said: but maybe the share the heritage of South Slavs. Click to expand...
<!-- artifact:quote:end -->
Which would be just as stupid, now if they would share south slavic aesthetics now that is what makes sense ...

## Reply 138 — participant_082 · 2021-06-15 · post-27619141

In 1.4, it's very difficult for the AI to maintain vassals of a different culture group. This is because you get a several penalties, first there's a wrong-group opinion modifier, and second, vassals of the wrong culture group are significantly more likely to join factions, and third, there's the popular opinion penalty. This makes an HRE that elects a Bohemian as emperor extremely unstable, even in the core German lands. It also makes the Seljuks extremely unstable (even moreso than they were in real life) because they're Oghuz. Looking at the example acceptance, in which French and Bavarian have a baseline of only 10%, I'm a little concerned that this issue will only be exacerbated. Especially with how belligerent small AI realms are, I would expect many neighboring cultures to rack up a lot of negative acceptance from wars. You give the example of a French king needing to treat his Occitan well, but that's just one ruler. What about all the wars that Occitan and French vassals will fight with one another? Also, will all cultures start with the same baseline acceptance, or will cultures that have already been in the same realm for hundreds of years at game start begin with more acceptance? So far it seems like the design philosophy is just to start everyone at the baseline (see fervor for example), but this creates a lot of ahistorical outcomes. It seems like it wouldn't be too much work to add a cultural acceptance history file, and just code in some special modifiers for cultures that need it. Obviously most pairs would just be left at the default - no need to specially designate how Icelanders and Tibetans feel about each other!

## Reply 139 — participant_053 · 2021-06-15 · post-27619144

<!-- artifact:quote:start -->
> Tuo said: Can we assume rulers can lead their own armies regardless of the Noble Martial Custom of their culture? Click to expand...
<!-- artifact:quote:end -->
It would be nice to have an event or two where some nobles disagree with for example their female ruler leading them into battle as it is against tradition and to have diplomatic/martial ways to resolve the event and gain their respect when playing as said ruler.

## Reply 140 — participant_001 · 2021-06-15 · post-27619164

<!-- artifact:quote:start -->
> Ul90 said: I'll try my luck with another question : What are the differences in aesthetic choices between divergence and hybridation when creating a new culture? If I am French and diverge into a new culture, do I only have access to French Aesthetic or to any other aesthetic on the map? Same question for hybridation, if I create a hybrid culture French-German, do I have access to only French and German Aesthetic? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Tuo said: Can we assume rulers can lead their own armies regardless of the Noble Martial Custom of their culture? Click to expand...
<!-- artifact:quote:end -->
Patience my friend. Patience. Correct! I forgot to mention that in the DD.

## Reply 141 — participant_084 · 2021-06-15 · post-27619179

Seconded what @WolfAleron says, this cultural rework looks really promising, and if it actually works well in-game, I'd love to have something similar in other PDX titles. Things like dynamic cultural acceptance or hybridization especially seem like they should belong in almost any PDX game, now that the tech to do it seems to be here.

## Reply 142 — participant_097 · 2021-06-15 · post-27619182

<!-- artifact:quote:start -->
> Servancour said: We might have a tradition or two that may or may not affect things such as creating or reforming a faith... Click to expand...
<!-- artifact:quote:end -->
I think this question was on lifestyles affecting culture costs. In the learning lifestyle there is Prophet and Apostate that affect costs on reforming/creating religions and converting to new religions, will there be similar lifestyle choices that affect the costs for altering/creating or changing cultures?

## Reply 143 — participant_098 · 2021-06-15 · post-27619187

<!-- artifact:quote:start -->
> Servancour said: We wanted to keep the language feature fairly simple for now, so a culture will only have a single language. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Servancour said: That's a fair point. However, since all cultures have their own name lists, we would have to create a language for every single culture. For gameplay purposes, we kind of like having languages overlap a bit, since it reduces opinion between cultures and adds some interesting immersion. Click to expand...
<!-- artifact:quote:end -->
Considering the culture focus of this expansion, will you be taking the opportunity to add some additional ones to the map? Coptic Egyptian is especially glimmering by its absence, particularly after it was added in the latter stages of CK2. After all, you can't do a proper Old Egyptian revival run with Egyptian Arabic. Based on the wording, is it feasible that this feature might be worked on down the line? I personally think it would be cool and make some degree of sense, if for instance you had one large Frankish culture stretching over Gaul and the Rhineland, that speaks Oïl, Dutch, and High German, while next door are the Thuringians and Bavarians who also speak High German, but not the others. Could you not simply tie name lists to languages instead of cultures and avoid creating a separate langue for each culture that way? I don't really see why cultures who speak the same language should have different name lists anyway. Rather, variation in naming customs can come by having characters occasionally give their children names from the local language instead of their own.

## Reply 144 — participant_099 · 2021-06-15 · post-27619194

Not sure if its asked before, probably is. But will gender rules from faiths still have effect? Like if I make my culture to promote equality, would that be enough or does my faith also need to be changed?

## Reply 145 — participant_096 · 2021-06-15 · post-27619195

<!-- artifact:quote:start -->
> Servancour said: Vlach and what they look like at the moment: View attachment 731981 Click to expand...
<!-- artifact:quote:end -->
Yea still doesnt make sense, why you ask? Heritage means (definition taken from merriam-webster) something transmitted by or acquired from a predecessor. Synonyms: Legacy, Inheritance This heritage would mean that Romanians are descendant of south slavs that just happen to speak a Latin language. I think it should be replaced with south slavs aesthetics in order to show the influence the south slavs had on Romanian culture.( btw the Byzantines influenced our culture more than the south slavs did but that's a discussion for another time)

## Reply 146 — participant_100 · 2021-06-15 · post-27619208

Very disappointed that you guys decided to keep the same "1 level" way of viewing heritage. While by 1066, it could be said that English and Norwegian/Danish/Swedish have diverged enough to consider them separate cultures (even if the real change happened after this point in history), having norse and anglo-saxon use different heritages, despite having a common heritage, having mutually intelligible languages makes little sense (Same with Saxon/Anglo-Saxon, where they even share names). This could have been fixed by having had a super level for heritage, like say "Germanic" or "Slavic" or "Latin" etc. in which lower level heritages like Iberian, Italian etc. to simulate more granularity. At this point it feels like i will still have the issue of having an Indian adventurer coming in have the same cultural acceptance issues as a Norse adventurer in the region of Germany, which breaks immersion because people would be much more hostile to someone who doesn't just speak a slightly strange language, but looks like a strange man as well. Something I had hoped would be fixed in this update. EDIT: With the new Vlach Screenshot, I see that Languages will be based on Language Families, which while addressing my upper layer concern, it makes me worry about specific languages not being represented this way. For example, the french of back then, would vary wildly to the romanian of back then, so even if both speak a romance language, an insurmountable language barrier would exist, maybe even to the point where guessing the meaning of words will not be enough to continue understanding each other, which is possible in languages like Russian and Ukrainian today.

## Reply 147 — participant_053 · 2021-06-15 · post-27619211

<!-- artifact:quote:start -->
> Djaevlenselv said: Considering the culture focus of this expansion, will you be taking the opportunity to add some additional ones to the map? Coptic Egyptian is especially glimmering by its absence, particularly after it was added in the latter stages of CK2. After all, you can't do a proper Old Egyptian revival run with Egyptian Arabic. Based on the wording, is it feasible that this feature might be worked on down the line? I personally think it would be cool and make some degree of sense, if for instance you had one large Frankish culture stretching over Gaul and the Rhineland, that speaks Oïl, Dutch, and High German, while next door are the Thuringians and Bavarians who also speak High German, but not the others. Could you not simply tie name lists to languages instead of cultures and avoid creating a separate langue for each culture that way? I don't really see why cultures who speak the same language should have different name lists anyway. Rather, variation in naming customs can come by having characters occasionally give their children names from the local language instead of their own. Click to expand...
<!-- artifact:quote:end -->
Well as was said before the language a culture speaks is more in line with belonging to a group of related languages. My guess would be that for example both Polish and Czech will have the same language due to them being similiar (even intelligible during the Middle Ages), however, it wouldn't be very accurate to give both of them the same name list as these would differ (though of course having many similarities).

## Reply 148 — participant_060 · 2021-06-15 · post-27619212

<!-- artifact:quote:start -->
> Sergej Provesky said: Not sure if its asked before, probably is. But will gender rules from faiths still have effect? Like if I make my culture to promote equality, would that be enough or does my faith also need to be changed? Click to expand...
<!-- artifact:quote:end -->
The faith gender doctrine will affect gender law availability (and a few other things), but no longer will affect who can serve as knights and commanders - that part is now on culture alone.

## Reply 149 — participant_101 · 2021-06-15 · post-27619219

Will the new Acceptance system be used for more reasonable innovation spread? It always felt weird how you are as likely to get spread from a neighboring culture who shares a realm as you are from a culture on the other side of the world that just happen to share a religion.

## Reply 150 — participant_102 · 2021-06-15 · post-27619223

<!-- artifact:quote:start -->
> Servancour said: We might have a tradition or two that may or may not affect things such as creating or reforming a faith... The different doctrines remains unchanged, outside of the main gender doctrine. Which, as mentioned in the DD, no longer affects who can be a knight or commander. 1. As far as I know, it won't affect the AI for picking education. Might be something to consider though, but I would never want to block it completely. 2. This modifier in question is added to a character, so you will always be able to benefit from it. Click to expand...
<!-- artifact:quote:end -->
There's always people who buck the trend. Joan of Arc is probably the most well-known. So even if a culture doesn't want female knights, there will always be some women who study martial and dream of being able to lead an army to kick the English out.

## Reply 151 — participant_043 · 2021-06-15 · post-27619229

So I feel like I should probably add another point to my earlier post regarding the immutability of culture traditions. If the only way to change existing traditions is to create a completely new culture you will end up with the following situation: Say we use as example the Rajput culture. It seems to have in the beginning 4 traditions already taken (I assume this is in the beginning since it is researching armillary sphere which is in the early medieval era and rajput is very close to entering high medieval in 1066) So given the importance of the ganges river in india (which is where we will be taking our nation in this example) we want the seafarers tradition. Which leaves room for perhaps esteemed hospitality. Now our tradition slots are full. After a while we start focusing on inward stability once we got a nice empire carved out of the region. So we ideally want to replace quarrelsome (which sounds like it is bad for internal stability) But the only way to do this is by creating a completely new culture. So what we will do is create a new one to swap out the specific tradition for another. Everything else remains the same of course because we only want a different tradition. Now we can just name our new culture Rajput but that will be extremely confusing. So we'll need a new one. We will just completely abandon the old culture and replace it with an entirely new one. Fast forward to a bit later again when we want to maybe no longer have warrior culture. Perhaps our empire has been at peace for several hundreds of years now and it simply doesn't fit anymore. Again we'll have to create an entirely new culture to swap out warrior culture for another tradition. repeating the above explained process. If the option exists to simply change traditions of your existing culture without having to make a new one then this whole jumping through hoops having to reconvert all your lands back to your new culture can be avoided entirely. It is therefore not just immersion breaking to have immutable cultural traditions. But also mechanically much more elegant to be able to swap traditions within the same culture. The point of diverging or hybridization should never be to simulate your culture changing internally over time. But rather to split off of the main culture, as the name suggests for divergence, or to merge with another existing culture in the case of hybridization. Traditions changing over time should be a separate option from those where the culture itself changes rather than having a new one emerge Specifically the current system very much means that "Cultures are not Forever". Because you have to abandon and possibly entirely replace them if you want a slightly different set of traditions

## Reply 152 — participant_103 · 2021-06-15 · post-27619232

<!-- artifact:quote:start -->
> riadach said: Will things like the ability to raid now become a cultural tradition? Click to expand...
<!-- artifact:quote:end -->
I think that's a wonderful idea, I hate it when I can't raid as vikings in 1066 just because I don't want to get 3278656345 piety to convert to Asatru

## Reply 153 — participant_104 · 2021-06-15 · post-27619235

<!-- artifact:quote:start -->
> Servancour said: This is also the pillar that contains what naming practices the culture uses. Mainly what character names to use, if they use a dynasty prefix, etc. The naming practice will also be used to change title and holding names, which used to be set per culture, so as to not have titles change names if you create a new culture. Click to expand...
<!-- artifact:quote:end -->
Thank you for this huge dev diary! Does this include Forms of Address? Can you pleeeeeaaaase give us a hint as to whether Form of Address customization is at least being considered? It would add so much immersion and replayability value at relatively low programming cost (I presume).

## Reply 154 — participant_058 · 2021-06-15 · post-27619237

<!-- artifact:quote:start -->
> Servancour said: Noble Martial Custom The martial custom decides which gender you may appoint as knights and commanders. As you’d expect, you can either appoint men, women, or both. We always felt that having the gender doctrine on faiths decide which characters can and cannot participate in battles felt off. The doctrine is about the right to rule and the holding of titles, more so than anything else. Just because you want the Equal doctrine to allow female rulers, doesn’t mean that women would automatically lead your armies or join you as knights. Revising cultures gave us the ample opportunity to move the functionality from faiths over to cultures. Which also means that you’ll have additional options in shaping your realm. Click to expand...
<!-- artifact:quote:end -->
Can you give us an overview of which Cultures have Only Men, Both or Only Women Martial Custom? I'm taking for granted that nothing may be permanent right now but just to have an idea. I thought that cultures that previously had Male Domination or Equal doctrines Faiths would have it accordingly but IIRC the Rajputs are usually Srikula-Shaktism, which is an Equal religion yet they have Only Men warriors in the screenshot.

## Reply 155 — participant_105 · 2021-06-15 · post-27619240

<!-- artifact:quote:start -->
> Servancour said: We don't have anything for holdings graphics in the expansion, sadly. The focus is on the Royal Court itself. Click to expand...
<!-- artifact:quote:end -->
And what about new clothing sets or ethnicities?

## Reply 156 — participant_014 · 2021-06-15 · post-27619241

<!-- artifact:quote:start -->
> Djaevlenselv said: Considering the culture focus of this expansion, will you be taking the opportunity to add some additional ones to the map? Coptic Egyptian is especially glimmering by its absence, particularly after it was added in the latter stages of CK2. After all, you can't do a proper Old Egyptian revival run with Egyptian Arabic. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> EldarPanic said: Yea still doesnt make sense, why you ask? Heritage means (definition taken from merriam-webster) something transmitted by or acquired from a predecessor. Synonyms: Legacy, Inheritance This heritage would mean that Romanians are descendant of south slavs that just happen to speak a Latin language. I think it should be replaced with south slavs aesthetics in order to show the influence the south slavs had on Romanian culture.( btw the Byzantines influenced our culture more than the south slavs did but that's a discussion for another time) Click to expand...
<!-- artifact:quote:end -->
Coptic Egyptian is a huge missing culture, as are Albanians and Malayalis. I think the heritage as a game mechanic seems to mean something different than it does as an actual world, but yes this further kinda exemplifies how these mechanics are really big issues in terms of building coherent and immersive cultures and interactions in-game.

## Reply 157 — participant_106 · 2021-06-15 · post-27619260

Interesting. Not sure I like the idea of clicking a button and now my culture is different but I don't hate it. I see a potential for great wailing and gnashing of teeth when people's favorite/real life culture isn't right or doesn't match their perception of that culture.

## Reply 158 — participant_007 · 2021-06-15 · post-27619266

I wonder why there's a line through Bavarian language? Are they mute? Can we assume then that Irish/Gaelic will share Old Irish/Old Gaelic and likewise Welsh, Cumbric, Cornish and Breton will share Common Brythonic? Will all Romance cultures speak Latin?

## Reply 159 — participant_107 · 2021-06-15 · post-27619271

Holy crap guys. This might just be the best and most exciting dev diary I've seen yet, for any of your games. This is gonna fundamentally change the game and add SO much flavor. And it's free?? That's the best part. That means it can be expanded in the future with unique components and not be reliant on someone having multiple DLCs. Are some of the features of Northern Lords going to be moved to the new culture system? Like the unique Dynasty Legacies and planned invasions?

## Reply 160 — participant_108 · 2021-06-15 · post-27619281

<!-- artifact:quote:start -->
> kemmy23 said: I wonder how the language and cultural 'parent' will work in the new hybrid culture system. If there are Turkic-Indians are they in the Turkic group or the Indian group, will they speak a Turkic language or an Indian one? Click to expand...
<!-- artifact:quote:end -->
Well, they could be in the Turkic culture group but speak an Indian language. It'll depend on the choices made when they come into existence.

## Reply 161 — participant_109 · 2021-06-15 · post-27619283

nice！！！I need chinese cultural and clothes

## Reply 162 — participant_110 · 2021-06-15 · post-27619287

Verte Nice!!! Add the crimean-gothic culture!!!!

## Reply 163 — participant_111 · 2021-06-15 · post-27619288

I really like what you have done in terms of progression with CK3. Being able to gather renown and improve your dynasty adds elements similar to roguelike games in the sense that although you "start over" with your heir, you still have an overall progression due to the dynasty mechanics and inheritable traits. From the looks of it, cultures could serve a similar purpose and combining different kinds of cultures looks to be very interesting and even encouraged. We may not be able to become immortal genius herculean lunatics in the game (yet) like in CK2, but I enjoy the progression in this game a lot. But I am hoping that we will still get the same amount of quirky and outright ridicolous events like immortality or child of satan like in CK 2 or the special cults like lucifer's own or other secret societies.

## Reply 164 — participant_112 · 2021-06-15 · post-27619291

I really like this, but I do have one question: How will Anglo-Saxon culture change with the Norman or Norwegian conquest? How does situations like these cause cultures conquered by other cultures to evolve?

## Reply 165 — participant_113 · 2021-06-15 · post-27619292

How are the Jewish cultures gonna be represented? If you create Israel could you re-adopt the Hebrew language?

## Reply 166 — participant_062 · 2021-06-15 · post-27619293

<!-- artifact:quote:start -->
> riadach said: I wonder why there's a line through Bavarian language? Click to expand...
<!-- artifact:quote:end -->
Because the character is French and doesn’t speak the language.

## Reply 167 — participant_114 · 2021-06-15 · post-27619297

<!-- artifact:quote:start -->
> Servancour said: Vlach and what they look like at the moment: View attachment 731981 Click to expand...
<!-- artifact:quote:end -->
A suggestion or two , from my discord Romanian community 1 Adding Melting Pots for Vlach culture with Russian to make Moldovian, Vlach with Avar to make Transilvanian. Vlach ,Moldovian , Transilvanian to make Romanian after a while like the norse do with Swedish Danish and Norvegian,And also Vlachs were shepherds they migrated all over Balkans creating new communities everywhere maybe u can make a tradition with this info,some example of Romanian shepherds communities outside the border: (Ethnics outside borders). 2 And about Traditions we Romanians we have a lot of them from Romans and pagan synergized with christian religion.

## Reply 168 — participant_115 · 2021-06-15 · post-27619298

We can revive dead cultures?

## Reply 169 — participant_001 · 2021-06-15 · post-27619300

<!-- artifact:quote:start -->
> Delta5ff said: I think this question was on lifestyles affecting culture costs. In the learning lifestyle there is Prophet and Apostate that affect costs on reforming/creating religions and converting to new religions, will there be similar lifestyle choices that affect the costs for altering/creating or changing cultures? Click to expand...
<!-- artifact:quote:end -->
Right. I misunderstood the question. Lifestyles don't have any Perks that affects culture costs. Reasoning is that we don't want it to be too closely related to the actual ruler, but more dependent on the circumstances of your culture.

## Reply 170 — participant_116 · 2021-06-15 · post-27619302

Ohhh Occitano-catalan culture, here we go!

## Reply 171 — participant_117 · 2021-06-15 · post-27619306

<!-- artifact:quote:start -->
> Tuo said: The faith gender doctrine will affect gender law availability (and a few other things), but no longer will affect who can serve as knights and commanders - that part is now on culture alone. Click to expand...
<!-- artifact:quote:end -->
That makes me wonder whose culture. The ruler's or the knight's? Will a male-only culture accept female knights that way?

## Reply 172 — participant_118 · 2021-06-15 · post-27619311

I like the overall concept, as it represents how different peoples had different lifestyles based on their geography and history. The Norse, with their coastline became excellent sailors. The steppe peoples became excellent riders and horse archers. The Greeks have a long, storied history of hospitality that they kept religiously. However, I am concerned about some of the bonuses given. Let's use Chivalry here as an example. It gives knight effectiveness. Now, why do I not like this? This is because knight effectiveness is based on individual characters. Many, many cultures had knight equivalents (hence why everyone has knights in-game, even if they are not called such), they were generally nobles, raised from birth to fight and lead. Being French does not make one better at that. A better bonus would likely be to heavy cavalry, since the French with their vast fields and farmlands punctuated with forests naturally gravitated towards heavily armored horse warfare and had history of it. I feel similarly with inventive. People are not more intelligent or more able to learn new things due to their culture. Certainly, different factors can lead to leaps in technology in certain areas. The Middle East in this time-period generally remained ahead of their European counterparts technologically up until the the very end of the CK3 timeframe when the Renaissance began to kick off, aided by forced innovation caused by the sudden loss of life caused by the Black Death. So, in summary, I like the idea and cultural acceptance as a non-binary gradient looks great, but I would personally like for the bonuses to be looked at carefully and those bonuses that affect characters to be replaced with more general bonuses unless there is a good reason to do otherwise.

## Reply 173 — participant_038 · 2021-06-15 · post-27619319

<!-- artifact:quote:start -->
> riadach said: I wonder why there's a line through Bavarian language? Are they mute? Click to expand...
<!-- artifact:quote:end -->
I think that means that your character doesn't know that language.

## Reply 174 — participant_007 · 2021-06-15 · post-27619322

<!-- artifact:quote:start -->
> InsidiousMage said: Because the character is French and doesn’t speak the language. Click to expand...
<!-- artifact:quote:end -->
Ah, very good.

## Reply 175 — participant_119 · 2021-06-15 · post-27619327

Could we get a map of what new cultures are being added or can we see which culture are being added? Or will this be covered in a future dev diary. I wanna help with accuracy so that things like carantanian/slovene missing or dutch culture being placed really weird are avoided.

## Reply 176 — participant_097 · 2021-06-15 · post-27619328

<!-- artifact:quote:start -->
> Servancour said: Right. I misunderstood the question. Lifestyles don't have any Perks that affects culture costs. Reasoning is that we don't want it to be too closely related to the actual ruler, but more dependent on the circumstances of your culture. Click to expand...
<!-- artifact:quote:end -->
Thank you for the clarification, I disagree a little with you as the person creating or changing the culture would have an easier time if they was extremely capable/charismatic or particularly scary to the populace. Will the stats and traits of the ruler have any impact at all on the costs or will it be the same regardless of who you are playing? Also will the size of the realm have an effect on cost as I imagine a small duchy/kingdom been easier to introduce cultural changes too over a massive empire?

## Reply 177 — participant_120 · 2021-06-15 · post-27619340

Please rename "Frankish Culture Group" to "French Culture Group" and move Frankish to "Central Germanic Culture Group".

## Reply 178 — participant_121 · 2021-06-15 · post-27619351

Amazing!!

## Reply 179 — participant_122 · 2021-06-15 · post-27619357

Languages!!!!! YES!

## Reply 180 — participant_123 · 2021-06-15 · post-27619362

How difficult/impossible will it be for me to seduce a lady whose language I do not speak? Will my good looks and winner smile be enough?

## Reply 181 — participant_060 · 2021-06-15 · post-27619366

<!-- artifact:quote:start -->
> Elfangor567 said: I like the overall concept, as it represents how different peoples had different lifestyles based on their geography and history. The Norse, with their coastline became excellent sailors. The steppe peoples became excellent riders and horse archers. The Greeks have a long, storied history of hospitality that they kept religiously. However, I am concerned about some of the bonuses given. Let's use Chivalry here as an example. It gives knight effectiveness. Now, why do I not like this? This is because knight effectiveness is based on individual characters. Many, many cultures had knight equivalents (hence why everyone has knights in-game, even if they are not called such), they were generally nobles, raised from birth to fight and lead. Being French does not make one better at that. A better bonus would likely be to heavy cavalry, since the French with their vast fields and farmlands punctuated with forests naturally gravitated towards heavily armored horse warfare and had history of it. I feel similarly with inventive. People are not more intelligent or more able to learn new things due to their culture. Certainly, different factors can lead to leaps in technology in certain areas. The Middle East in this time-period generally remained ahead of their European counterparts technologically up until the the very end of the CK3 timeframe when the Renaissance began to kick off, aided by forced innovation caused by the sudden loss of life caused by the Black Death. So, in summary, I like the idea and cultural acceptance as a non-binary gradient looks great, but I would personally like for the bonuses to be looked at carefully and those bonuses that affect characters to be replaced with more general bonuses unless there is a good reason to do otherwise. Click to expand...
<!-- artifact:quote:end -->
People might not be smarter or stronger for the cultures they come from, but having your culture provide the means for talented people can make a difference - if a culture, for instance, celebrates learning, you'll likely find centers of learning and libraries where they live, and scholars might be sponsored by nobility. Is it so strange that in such circumstances individuals would have higher potential to learn and research?

## Reply 182 — participant_124 · 2021-06-15 · post-27619371

I will be honest and say that the announcement of Royal Court didn't hype me, but this Dev Diary sure did, cultures are looking amazing! Thank you for your hard work, plz keep it up!

## Reply 183 — participant_125 · 2021-06-15 · post-27619373

<!-- artifact:quote:start -->
> Servancour said: Vlach and what they look like at the moment: View attachment 731981 Click to expand...
<!-- artifact:quote:end -->
Does this mean that all of the Romance languages are going to be grouped as Latin Language? Or is there going to be like a split at some point in history?

## Reply 184 — participant_122 · 2021-06-15 · post-27619374

<!-- artifact:quote:start -->
> Servancour said: We have a fair amount of both widely available traditions, as well as unique traditions. Some are culture specific, others are for a heritage. Most cultures will have a healthy mix of both. We wanted to keep the language feature fairly simple for now, so a culture will only have a single language. More on stuff like this in future DDs. We don't do anything to introduce new languages over time specifically though. Click to expand...
<!-- artifact:quote:end -->
This is so cool! One question though: i get that a culture is tied to only one language but characters can speak multiple languages. Should the "second" language of a character infuenced by the languages spoken by his/her parents? Also, will this culture overhaul included in the free patch or in the paid DLC? Thanks for the amazing job!

## Reply 185 — participant_126 · 2021-06-15 · post-27619380

Does the new culture system mean you will acknowledge the existence of other east Slavic cultures or you'll keep calling everyone Russian?

## Reply 186 — participant_127 · 2021-06-15 · post-27619383

now that culture's getting reworked, are the albanians going to be added?

## Reply 187 — participant_128 · 2021-06-15 · post-27619390

This is a great Dev Diary. I really love the changes. It would be fun if the Ethos could be changed in specific circumstances. Like if you have the absolute majority of the culture as culture head and it hadn't changed in the past 100 years or similar cirumstances. Nevertheless, I am looking forward to it.

## Reply 188 — participant_129 · 2021-06-15 · post-27619406

Will there be a cultural coats of arms design like CK2 in the future? Also is the coats of arms designer coming any time soon?

## Reply 189 — participant_130 · 2021-06-15 · post-27619451

How will this change effect content from Northern Lords? There are a number of features that are restricted to the North Germanic cultures in the DLC, such as runestones and Varangian Invasions. Will any of these features be represented somehow in the new culture system? I would love to be able to construct Runestones as a Celtic culture if I have the Northern Lords DLC, for example.

## Reply 190 — participant_131 · 2021-06-15 · post-27619457

Will there be more cultural hybridization coming with this update (or otherwise planned), and if so, will it be primarily dynamic or entirely scripted?

## Reply 191 — participant_132 · 2021-06-15 · post-27619468

<!-- artifact:quote:start -->
> Servancour said: Vlach and what they look like at the moment: View attachment 731981 Click to expand...
<!-- artifact:quote:end -->
Do Vlachs keep Latin through the game or does it change to Vlach eventually? Same for other Latin cultures, since for most of the timeframe those were all different languages with their own dialects. Even Spain had and has multiple, so it seems odd to have linguistic groups *that* large through the period. All the different Spanish languages could be grouped up though, but Portuguese and Vlachs speaking the same seems odd to me.

## Reply 192 — participant_133 · 2021-06-15 · post-27619476

So just two questions... How will high cultural acceptance between two cultures factor into the AI's decision to culture convert? Will they continue to culture blob into that culture or simply not convert them at all?

## Reply 193 — participant_134 · 2021-06-15 · post-27619503

Wow. This is a lot more in-depth than what I was initially expecting. I'm especially happy about using this system to handle things like special succession rules, as the current system is a little bit "hacky". I'm also hopeful for the ability to have cultures increase their acceptance of each other over time, as this should help prevent things like the HRE disintegrating within a generation due to culture revolts if an Italian or Czech character becomes emperor.

## Reply 194 — participant_135 · 2021-06-15 · post-27619511

My favorite comment: "At the end of the day, if you want to maintain a high acceptance and keep your Occitan vassals in France happy, you are at least gonna have to try and be nice to them." This expansion on culture sounds great! Jumping way ahead here, but will that make nomadism a cultural pillar or tradition?

## Reply 195 — participant_136 · 2021-06-15 · post-27619514

Tremendously excited about this great dev diary! Seems great! There have been some concerns in this thread about the issue that cultures could only be reformed by creating a new culture. Could this be addressed by allowing subcultures in the future? Say, each culture would still have a cultural head, but just as dynasties can create cadet branches or religions have heresies, prestigious and powerful rulers could create subcultures. These could be altered more cheaply than forming a new culture, and they could have some maximum amount of divergence from the culture heads culture without becoming entirely separate from it. For example 3/5 traditions could be designated as "core traditions" that can only be changed by culture head, but sub-culture heads could change the other 2/5. By default subcultures would have a better opinion of each other than any foreign cultures, but slightly lower opinion than having exactly the same culture.

## Reply 196 — participant_137 · 2021-06-15 · post-27619517

This is just awesome. As a roleplayer it's exactly the kind of content that I want to see.

## Reply 197 — participant_138 · 2021-06-15 · post-27619542

<!-- artifact:quote:start -->
> Princess Stabbity said: Oh no... here comes the Paradox paradox. How am I going to play the current version now ,>O<, Oh! I know! I'll pass the time by asking stuff! I was wondering, if the culture system is taking inspiration from the faith system, can we also expect the ability to adopt "extinct" cultures that technically no longer have any counties or characters practising them, but have been well preserved in writing? ...yes I'm asking about the Roman culture (˳˘ ɜ˘) ~♪ Click to expand...
<!-- artifact:quote:end -->
I mean in 867 "Romans" still exist, and not just in Byzantium. 9th Century Rome was pretty "Byzantine" and still fairly classical (there's a reason Italy was largely dominated by city states, the Papal Bureaucracy, and an autocratic Siculo-Norman dynasty, rather than succumbing wholly to feudal landlords like in France or Spain). From a gameplay perspective Venetian, southern Lombard, Sardinian, and "Latin"/"Roman" culture in Latium and the Romagna should have high acceptance for Greek at the start and possibly even a Greek aesthetic, but less over time, as they were all still heavily influenced by the Eastern Roman Empire.

## Reply 198 — participant_082 · 2021-06-15 · post-27619549

<!-- artifact:quote:start -->
> Ryeboy98 said: So just two questions... How will high cultural acceptance between two cultures factor into the AI's decision to culture convert? Will they continue to culture blob into that culture or simply not convert them at all? Click to expand...
<!-- artifact:quote:end -->
It feels like from a gameplay perspective, the "optimal" answer would be to still convert (maybe avoiding some very low development provinces). After all, even if you have perfect acceptance now, that could all change with a few wars, and then it'd be a disaster. It feels like, despite all these nifty toys to play with, the game heavily incentivizes cultural homogenizing. Culture-converting provinces is cheap, quick, and low risk. Not culture-converting is a dangerous game that will eventually come back to bite the AI (a competent human can get away with just about anything). The same problem exists with religion - we have lots of unique local religions in the first few years, and they all get obliterated because there's no downside or expense or difficulty to doing so. I'm concerned the same will happen with cultures, and a lot of this cool work will go to waste.

## Reply 199 — participant_139 · 2021-06-15 · post-27619550

Great job, I can't wait for the next DDs to see where this is going. When looking into the Bavarian culture print I noticed a culture south of the Czech that does not exist on the game as it is right now, with that a few questions come into my mind: 1 - With that cultural rework the team is planning on doing a rework on the culture placement on the world? for example bringing in some new cultures that are not represented on the game such as Albanian or the Crimean Goths, making a more historically accurate cultural map? 2 - Is the team planning on reworking the cultural groups? with Cultural Acceptance now a mechanic I don't see a reason to cultures that are not historically on the same group being placed at the same group on the game for easier player management such as the Occitan being on the Frankish group, Basque being on the Iberian group or Visigothic being on the Iberian group. 3 - Will there be a rework on how ethnicities work and is passed on to cultures? For example the Baranis culture at the 800s start having a Mediterranean/African substrate and with the spread, influence and dominance of the Maghrebi culture they acquire the Arabic substrate.

## Reply 200 — participant_140 · 2021-06-15 · post-27619554

Does cultural acceptance affect popular opinion?

## Reply 201 — participant_141 · 2021-06-15 · post-27619560

<!-- artifact:quote:start -->
> EmoPro said: What does Available Mercenary Companies do? Click to expand...
<!-- artifact:quote:end -->
It affect the number of mercenary companies, of that culture, that are available.

## Reply 202 — participant_082 · 2021-06-15 · post-27619610

<!-- artifact:quote:start -->
> iniudan said: It affect the number of mercenary companies, of that culture, that are available. Click to expand...
<!-- artifact:quote:end -->
I thought each culture generated 1 to 3 companies, so +20% doesn't make a lot of sense for that range. Have they said anything about changing how mercenaries work?

## Reply 203 — participant_142 · 2021-06-15 · post-27619644

I hope we can make an epic crop with all the mergers of culture in one. I like when I am the most powerful. But I hope it will be possible. But very difficult at least.

## Reply 204 — participant_143 · 2021-06-15 · post-27619658

Will we be able to make new cultural pillars?

## Reply 205 — participant_144 · 2021-06-15 · post-27619692

Can't wait to turkify anatolia =)

## Reply 206 — participant_141 · 2021-06-15 · post-27619696

<!-- artifact:quote:start -->
> Tiax said: I thought each culture generated 1 to 3 companies, so +20% doesn't make a lot of sense for that range. Have they said anything about changing how mercenaries work? Click to expand...
<!-- artifact:quote:end -->
By itself maybe, as it not high enough to get to 4 in a culture that can get 3 without modifier, but there is an other +50% in the DD. Combine both together and you get to 5 companies. Also there is already a late medieval Italia regional innovation that does that in the game. Condottieri, which is +100%.

## Reply 207 — participant_046 · 2021-06-15 · post-27619701

<!-- artifact:quote:start -->
> Tiax said: It feels like from a gameplay perspective, the "optimal" answer would be to still convert (maybe avoiding some very low development provinces). After all, even if you have perfect acceptance now, that could all change with a few wars, and then it'd be a disaster. It feels like, despite all these nifty toys to play with, the game heavily incentivizes cultural homogenizing. Culture-converting provinces is cheap, quick, and low risk. Not culture-converting is a dangerous game that will eventually come back to bite the AI (a competent human can get away with just about anything). The same problem exists with religion - we have lots of unique local religions in the first few years, and they all get obliterated because there's no downside or expense or difficulty to doing so. I'm concerned the same will happen with cultures, and a lot of this cool work will go to waste. Click to expand...
<!-- artifact:quote:end -->
I always play with Culture Conversion set to “Significantly Slower”, which I think would help mitigate this.

## Reply 208 — participant_145 · 2021-06-15 · post-27619751

This looks REALLY good. My biggest and only concern is that of balance: Some of these look WILDLY stronger than others. I know CK has always had an attitude of not caring about balance issues, but I definitely feel it should be paid extra attention here so you don't end up with "dud" cultures that just are far weaker than their neighbors. As much as you can try to people should RP or whatever, if one culture right next to another is blatantly stronger it'll lead to nobody wanting the weaker one.

## Reply 209 — participant_146 · 2021-06-15 · post-27619781

I want something Geto-Dacic too for the Vlachs - aout resilience and taking refuge on the mountains.

## Reply 210 — participant_038 · 2021-06-15 · post-27619817

<!-- artifact:quote:start -->
> BrotherJonathan said: Wow. This is a lot more in-depth than what I was initially expecting. Click to expand...
<!-- artifact:quote:end -->
What is really is "in-depth" here though? Genuine question. It looks like the same modular system we have for religion (with Pillars and Traditions instead of Tenets and Doctrines" and is basically a set of bonuses for different cultures. Yeah it might be fun to mess around with creating new hybrids and picking bonuses, but what is deep about that? --- Downvoted, yet still everyone refuses (or just unable to) to explain what is deep about this -- Still not a single explanation so yeah, just a herd instinct by this point

## Reply 211 — participant_147 · 2021-06-15 · post-27619825

<!-- artifact:quote:start -->
> Liquid Ghost said: How difficult/impossible will it be for me to seduce a lady whose language I do not speak? Will my good looks and winner smile be enough? Click to expand...
<!-- artifact:quote:end -->
i think you need work with your language hard

## Reply 212 — participant_148 · 2021-06-15 · post-27619852

<!-- artifact:quote:start -->
> Servancour said: CK3 Dev Diary #64 - Cultures Are Forever​Salutations! Before we begin, first things first. We are working on an additional patch to fix some of the issues introduced in 1.4. The patch is still being worked on, but if everything goes as planned, we should be able to get it out sometime next week or so. We’ll let you know once the patch is ready. With that out of the way, let’s talk about something I’m quite excited to share with you all. As you probably know already, we’ve talked a bit about how we are revisiting cultures for the next expansion: Royal Court. Unlike faiths, which got a lot of attention prior to release as we made them quite dynamic and customizable, cultures can feel a bit static, and aren't anywhere near as interesting as faiths. That is all about to change! We are revising cultures as you know them. Most exciting is perhaps the possibility to create new cultures! Both for simulating historical events and to create plausible and interesting alt-history scenarios. But I’m getting ahead of myself. For now, let’s start by looking at the foundation of a culture and the different components they are made of. This is what the new culture screen will look like. View attachment 731851 [Image of the new and updated culture interface]​ Cultural Pillars​A culture has five main Cultural Pillars. These are Ethos, Heritage, Language, Martial Custom, and finally Aesthetics. Of these, the Ethos is perhaps the most significant, but all of them play a particular role in how a culture plays and how cultures view each other. Ethos Each ethos is framed around a particular theme that somehow ties into a fairly broad definition of what a culture is. A culture’s ethos not only provides effects and bonuses for having it, it also ties into how easy or difficult it is to acquire certain traditions (more on this further down). There are seven in total: Bellicose Communal Courtly Egalitarian Inventive Spiritual Stoic Here are a few examples of what they may look like in-game: View attachment 731852 [Image of the Bellicose ethos] View attachment 731853 [Image of the Spiritual ethos] View attachment 731854 [Image of the Inventive ethos]​ Heritage A culture's heritage can be compared to the culture groups that you may be used to in the existing system. Heritages will roughly match said culture groups. You’ll see an Iberian Heritage for cultures like Basque and Castilian, or Turkic Heritage for Turkic cultures, such as Oghuz and Cuman. In terms of gameplay, the most outstanding effect of a shared heritage is the impact it has on Cultural Acceptance. Language Each culture has a designated language. Languages vary greatly across the map and between cultures. Some languages, such as Arabic, are spoken by quite a few cultures. Other languages are spoken by no more than two or three cultures, or in some cases, cultures even have their own unique language. An example of these would be Basque, who really don't have any closely related languages and it wouldn’t make too much sense to group them together with their neighbors. The vast majority of cultures share a language though, as a sort of “language group” rather than a specific language. Characters can always speak the associated language of their culture. They are, however, also able to learn multiple languages over their lifetime. Knowing multiple languages has its benefits, as speaking the same language as another character of a different culture, and county, will reduce the opinion penalty that character, or county, has towards you. Knowing the native language (i.e. the language of their culture) of your vassals is therefore fairly beneficial as a means of increasing their opinion of you. Noble Martial Custom The martial custom decides which gender you may appoint as knights and commanders. As you’d expect, you can either appoint men, women, or both. We always felt that having the gender doctrine on faiths decide which characters can and cannot participate in battles felt off. The doctrine is about the right to rule and the holding of titles, more so than anything else. Just because you want the Equal doctrine to allow female rulers, doesn’t mean that women would automatically lead your armies or join you as knights. Revising cultures gave us the ample opportunity to move the functionality from faiths over to cultures. Which also means that you’ll have additional options in shaping your realm. Aesthetics This pillar is really a collection of several smaller properties for what a culture “looks” like. It decides what type of clothes characters wear, the coat of arms style for dynasties, what architecture holdings use, and the type of armor the units on the map wear. This is also the pillar that contains what naming practices the culture uses. Mainly what character names to use, if they use a dynasty prefix, etc. The naming practice will also be used to change title and holding names, which used to be set per culture, so as to not have titles change names if you create a new culture. For all of you modders out there; all of these can be set individually per culture. Allowing you to mix and match the different aesthetics to your heart’s content. Traditions​Traditions are the meat of the cultural overhaul, and provide that extra layer of variety and immersion that can have a significant impact on gameplay. An important aspect of traditions is that they give us a clear means of visualizing and explaining existing mechanics that previously just “was a thing” and never explained. Take Anglo-Saxon as an example. They have access to the Saxon Elective succession for no apparent reason other than “they do”. Instead, they now have a tradition that grants them the succession law, making it clear as to why they have it. Secondly, and perhaps more importantly, traditions serve as the perfect means of giving a culture additional flavour or gameplay bonuses that add a greater degree of variety across the map. A culture can have no more than five traditions in total, but this number will increase as you enter a new era. Most cultures will start the game with around three or four, which leaves plenty of room for you to shape your culture as you play the game. As the cultural head, you’ll have the ability to establish new traditions. Not all traditions will be available everywhere. We have both regional traditions, as well as traditions that are available depending on your heritage. The vast majority of them can be established regardless of circumstances, but might require certain conditions, such as ‘Hill Dwellers’ having the requirement that your culture must be present in a county with hills. Traditions cost prestige to adopt. Which will be the largest hurdle for you to overcome if you want a specific tradition. The prestige cost is dependent on your ethos. Certain traditions will be more expensive than others, if you don’t have a matching ethos. Similarly, a tradition will increase in cost if your culture, or in some cases the cultural head, doesn’t fulfill a specific and thematic requirement. An example would be a tradition named ‘Only the Strong’, which is more expensive if you as the cultural head don't have at least six knights with at least 12 prowess. The increased cost is meant to act as a softer limit and make it slightly more difficult to establish certain traditions (depending on your circumstances), but not as much as to make it impossible to do so, should you want to go and unlock a particular tradition. Instead of explaining traditions in detail, I’ll just show you a few examples of what traditions may look like, as well as the type of effects you can expect from them. View attachment 731855 [Image of the Swords for Hire tradition] View attachment 731856 [Image of the Chivalry tradition] View attachment 731857 [Image of the Esteemed Hospitality tradition] View attachment 731858 [Image of the Seafarers tradition] View attachment 731859 [Image of the Land of the Bow tradition]​ Cultural Acceptance​Cultural acceptance can be described as how well intermingled two cultures are, and how accepting they are of each other. Which means that given enough time, cultures will dislike each other less, and culture converting everything within your realm is no longer the only solution to combat cultural differences. The opinion penalty of being of a different culture used to be a static value. Now, it will depend on the cultural acceptance between your culture and the target culture. Each culture has an acceptance value of another culture, visualized as a percentage. Depending on the amount of acceptance, the “different culture” opinion penalty will gradually be reduced. At 0% acceptance, you’ll have the full opinion penalty. At 100%, the penalty is removed altogether. Acceptance goes both ways. So if the French have a 20% acceptance towards Normans, the same will be true from the Norman perspective. There are two ways for acceptance to change. The first is an acceptance baseline. Which increases if two cultures share similarities with one another. There are a number of different modifiers that can increase the baseline. Such as cultures that share the same religion or faith, ethos, or language. The most impactful modifier, however, is heritage. If two cultures share the same heritage, they have a significant bonus to their baseline. If acceptance is above the baseline, it will slowly decay over time towards the targeted value. Being below the baseline on the other hand, will not make the acceptance increase. A bad relation between cultures won’t disappear overnight. Secondly, acceptance very much changes depending on the circumstances. Don’t expect two cultures that never interact with one another to gain acceptance. If cultures exist within the same realm though, it will increase over time. This applies to both counties of another culture within your realm, as well as vassals. Acceptance is also reactive. Taking certain actions towards characters of a different culture will have consequences on your acceptance, such as declaring war or revoking titles. This generally scales on size. While the difference isn’t huge, revoking a single county from a small culture will decrease your acceptance more than if you would revoke a county from a much larger culture. At the end of the day, if you want to maintain a high acceptance and keep your Occitan vassals in France happy, you are at least gonna have to try and be nice to them. View attachment 731860 [Image of what the cultural acceptance between two cultures may look like]​ There we go. That’s what a culture will look like in the near future. Oh! Before I forget; Best of all? The cultural rework is free, and will accompany the free update that launches alongside the Royal Court expansion! Until next time! Click to expand...
<!-- artifact:quote:end -->
Make it so names won’t depend on aesthetics, but rather language or etc. it will be cool to see vikings in India wearing Indian outfit and building Indian buildings, but they must have Indian names!!

## Reply 213 — participant_060 · 2021-06-15 · post-27619858

<!-- artifact:quote:start -->
> OlegOlegov said: Make it so names won’t depend on aesthetics, but rather language or etc. it will be cool to see vikings in India wearing Indian outfit and building Indian buildings, but they must have Indian names!! Click to expand...
<!-- artifact:quote:end -->
This was already answered - each culture has its own namelist, while most languages are shared by several cultures. Assigning namelists to languages would mean that each culture would have to have its own language, which is explicitly not the design they chose to go with.

## Reply 214 — participant_149 · 2021-06-15 · post-27619893

The culture elements seem great, though I hope for whatever reason there will not be a possible meta in the horizon.

## Reply 215 — participant_089 · 2021-06-15 · post-27619911

<!-- artifact:quote:start -->
> Undead Martyr said: I mean in 867 "Romans" still exist, and not just in Byzantium. 9th Century Rome was pretty "Byzantine" and still fairly classical (there's a reason Italy was largely dominated by city states, the Papal Bureaucracy, and an autocratic Siculo-Norman dynasty, rather than succumbing wholly to feudal landlords like in France or Spain). From a gameplay perspective Venetian, southern Lombard, Sardinian, and "Latin"/"Roman" culture in Latium and the Romagna should have high acceptance for Greek at the start and possibly even a Greek aesthetic, but less over time, as they were all still heavily influenced by the Eastern Roman Empire. Click to expand...
<!-- artifact:quote:end -->
Academically, yes, but the specific example I was referring to was the in-game "roman" culture entry (common\culture\cultures\00_latin.txt, line 209) which currently has a lot of unique flavour associated with it, such as alternative text for the Roman Restoration events, a special MAA and even its own title flavouring. As of right now, there is no way to adopt any aspects of that culture besides using mods, console commands, or Ruler Designer to start with it. So I'm hoping that with the culture system rework, all those things will either become Traditions we can pick to gain access to that content, or there will be a way to somehow adopt the whole preset culture.

## Reply 216 — participant_150 · 2021-06-15 · post-27619920

Are the gender of the generated captain and knights of the mercenary companies controlled by the new cultural martial setting? Right now I’m playing with a female dominated faith and both the captains and knights of my cultural mercenary companies are male even though they have my faith which seems a bit off.

## Reply 217 — participant_151 · 2021-06-15 · post-27619926

<!-- artifact:quote:start -->
> peaswar said: The execution of ethoses is still a major concern for me. I don’t hate the fact that you won’t be locked out of any type of gameplay due to your ethos, and it at least *kinda* makes sense that it would be harder to become a more learning oriented nation if war is the historic main focus of your people, from an irl perspective. I still think that ethos and heritage should be dynamic, changing over many decades if a culture and its leader start acting a certain way for long periods of time. It makes no sense that I could be a nation which includes all the Norse in 900, save up to buy expensive intellectual traits, and then focus on being an isolationist until 1200, and new intellectual traditions still wouldn’t be cheaper, and I wouldn’t get bonuses ro learning at all. The potential issues I’ve noted many times at this point with unintentional stereotyping and the fact that this does not reflect how cultures evolved without becoming new cultures or hybridizing unfortunately still stand as well. Click to expand...
<!-- artifact:quote:end -->
Which is why I believe cultural heads (or ruler attitudes) should have a say in determining the Ethos every time a new technological Era starts.

## Reply 218 — participant_152 · 2021-06-15 · post-27619969

Would be nice if aesthetics were splitted into several elements. Let's say I want to create an indo-norse culture which uses norse names and rajput clothing, this would be a cool feature!

## Reply 219 — participant_060 · 2021-06-15 · post-27619988

<!-- artifact:quote:start -->
> FleetingRain said: Which is why I believe cultural heads (or ruler attitudes) should have a say in determining the Ethos every time a new technological Era starts. Click to expand...
<!-- artifact:quote:end -->
If the culture head could decide the cultural ethos on reaching a new era, I feel there should be a grace period where it could be changed again before it sets - you'll often see culture head temporarily shift to the second-most relevant ruler on inheritance, and with so few opportunities to change it, it would quite suck to lose the choice for good due to ill-timed succession.

## Reply 220 — participant_153 · 2021-06-15 · post-27619997

While I find the culture rework overall great, there are some concerns I have (or more accurately places where I hope more could be done). First I love that cultures essentially belong to two groups: language and heritage (not surprising as I made a similar suggestion in the past, though I like your implementation more). I do wonder if there is also a grouping above this. So does the game group Central Germanic, Norther Germanic and Western Germanic? The one I think that could be really cool is a grouping of langues. So assuming English and German are both languages in game, could be cool to have a Germanic language family they both belong to. With the benefit being it's easier to learn languages that are in the same language family as your primary language (or maybe any language you already know). I think traditions and cultural acceptance are fantastic and have no problem with either. I honestly didn't think a feature like cultural acceptance would be possible/feasible when I made my culture overhaul recommendation around the release of CK3. I guess I need to set my sights higher for future suggestions. For the Noble Martial Custom: I'm glad to see martial gender norms are being split off from the rest of the gender rules, but was hoping it would go a bit further. For instance I have a personal mod (that I've been think of releasing if people are interested) that creates a new gender doctrine for martial (so same idea as the new cultural pillar), but it also splits it up into 5 levels that act as a spectrum: Men Only, Only Male Combatants (commanders are both genders), Both Men and Women, Only Female Commanders (combatants are both genders), & Women Only. So as you go from 'Men Only' to 'Female Only' either the commander gender (which determines who can be your marshal or commanders) changes one step or the combatant gender (which determine who can be knights or fight in duels). I find it nice as it makes the thing less of a binary (or trinary) , and allows depicting place like China and Perisa (at least before the Muslim invasion, though still a bit after) in which women would serve as generals, but having female knights still doesn't really make sense. Also I was kinda hoping that all the gender doctrines would be set by the faith, but the culture could some how modify them. But as I can't really think of a cohesive way to get that to work, so I can understand why you went with splitting them between the two. But it's ethos that I still have some concerns about. While I'm glad to see the bonuses are all percentages (outside of the prowess for martial, which I think is just a game limitation). I like the percentages as they really just are giving a bonus to character that act in accordance with their cultural ethos while still allowing character to ignore it. But it still comes off a bit sterotype-y to me, as it's a giant banner across the top of the culture. So even though you say it's just one of the 5 pillars, it really comes across as the main defining feature. To help with that I hope it can change over time without needing to diverge or hybridize (maybe give the culture head the ability to change it). I also I still think having two cultural ethoses would be more interesting (and would be less sterotypey as it would not run the risk of making a culture appear as it's been reduced down to one word). Not only would it allow for more unique combinations. I think would be more interesting to role play. As role playing a character from bellicose culture is just being a warrior (or rejecting being a warrior). But trying to role play a bellicose and spiritual culture sound more interesting as you have to decide what it means to be both bellicose and spiritual. Plus whether your current character will lean more into one vs the other, and to what degree, or reject both altogether. Anyways, looking forward to more dev diaries on culture and the Royal Court. I think you all are doing a great job.

## Reply 221 — participant_154 · 2021-06-15 · post-27620008

Excellent dev diary. Loaded with content, clearly structured, colourful, and very easy to understand.

## Reply 222 — participant_007 · 2021-06-15 · post-27620030

<!-- artifact:quote:start -->
> Scanz said: i think you need work with your language hard Click to expand...
<!-- artifact:quote:end -->
A very cunning linguist, as it were?

## Reply 223 — participant_153 · 2021-06-15 · post-27620049

<!-- artifact:quote:start -->
> Tuo said: If the culture head could decide the cultural ethos on reaching a new era, I feel there should be a grace period where it could be changed again before it sets - you'll often see culture head temporarily shift to the second-most relevant ruler on inheritance, and with so few opportunities to change it, it would quite suck to lose the choice for good due to ill-timed succession. Click to expand...
<!-- artifact:quote:end -->
There is a period where you meet all the requirement for the next era, but your culture is still unlocking it. Could have it so that the new ethos can be set by the player anytime during that period (and potential the AI will also sometimes change the ethos, but only if they are the culture head at the start of the period). Then when the era is unlocked, the cultural ethos of the culture comes whatever it was last set to during that grace period (and since there is a grace period, if the AI is temporally culture head at the beginning of the period and sets it to some the player doesn't like, the player can reset it to what they want when they come the cultural head again). Maybe something like that could work? Also thinking you get an alert during that grace period so you don't forget to set the ethos, if you want to.

## Reply 224 — participant_155 · 2021-06-15 · post-27620064

I'm not a huge fan. I find the appeal of the game to be about relationships between individual characters, not stereotypes. Not to mention that the additional boni are yet again powercreep... That the "cultural head" can reform his culture is also weird and unrealistic. Relationships between cultures will also be weird and won't make much sense (all english will like the french less because that one king didn't like that one stupid excommunicated english count - yeah, sure). I like languages though.

## Reply 225 — participant_156 · 2021-06-15 · post-27620088

I honestly can't believe it, you guys are going to make the cultural system work wonderfully!!! I absolutely love it, can't wait to try this new feature Thanks for your hard work, and best of luck in your projects!!!

## Reply 226 — participant_157 · 2021-06-15 · post-27620211

<!-- artifact:quote:start -->
> Servancour said: Secondly, acceptance very much changes depending on the circumstances. Don’t expect two cultures that never interact with one another to gain acceptance. If cultures exist within the same realm though, it will increase over time. This applies to both counties of another culture within your realm, as well as vassals. Acceptance is also reactive. Taking certain actions towards characters of a different culture will have consequences on your acceptance, such as declaring war or revoking titles. This generally scales on size. While the difference isn’t huge, revoking a single county from a small culture will decrease your acceptance more than if you would revoke a county from a much larger culture. At the end of the day, if you want to maintain a high acceptance and keep your Occitan vassals in France happy, you are at least gonna have to try and be nice to them. Click to expand...
<!-- artifact:quote:end -->
Would how much/whether revoking a title from a differently cultured vassal be affected by whether the revocation is justified or not? Likewise is there some sort of bonus for the reverse, giving titles to differently cultured vassals? It would be nice for me as the king of France to able to revoke a title from Duke Traitor the Aptly Named of Toulouse and avoid this act of justice hurting the acceptance between French and Occitan by making sure that the new duke of toulouse also is occitan. That'd also make sense from an in-universe perspective since that'd mean that it really would be a punishment toward ex-duke Traitor specifically, and not an instance of occitan people getting a bit more marginalized from the kingdoms halls of power.

## Reply 227 — participant_158 · 2021-06-15 · post-27620251

Does aesthetic also determine what ethnicity new characters of that culture are generated with?

## Reply 228 — participant_159 · 2021-06-15 · post-27620317

These changes look really good and I'm really waiting to play an Iberian campaign with them. A quick question tho. If you remove all the new mechanics, the changes on the game as it is now only concern the opinion modifier, with a lever to decrease it. The modifier we have right now being the worst case. Are you considering increasing the modifier to take in account that we will have an hand on it ? My concerns being that it will end up with being cool with everybody or if not "well, it's just the usual malus, but with less people than before".

## Reply 229 — participant_014 · 2021-06-15 · post-27620334

<!-- artifact:quote:start -->
> FleetingRain said: Which is why I believe cultural heads (or ruler attitudes) should have a say in determining the Ethos every time a new technological Era starts. Click to expand...
<!-- artifact:quote:end -->
this would be acceptable if there's a few more dynamic systems and it's not an absolute decision

## Reply 230 — participant_160 · 2021-06-15 · post-27620339

<!-- artifact:quote:start -->
> Servancour said: ​ A culture can have no more than five traditions in total, but this number will increase as you enter a new era. Most cultures will start the game with around three or four, which leaves plenty of room for you to shape your culture as you play the game. As the cultural head, you’ll have the ability to establish new traditions. Click to expand...
<!-- artifact:quote:end -->
If there's only five in total with all ages unlocked, then does everyone start with 2 in 867 and some still have only 2 in 1066? Big gap.

## Reply 231 — participant_060 · 2021-06-15 · post-27620348

<!-- artifact:quote:start -->
> Darsara said: If there's only five in total with all ages unlocked, then does everyone start with 2 in 867 and some still have only 2 in 1066? Big gap. Click to expand...
<!-- artifact:quote:end -->
I'd like to point out the screenshot in the post shows 4/6 traditions.

## Reply 232 — participant_161 · 2021-06-15 · post-27620352

Carantanian culture when?

## Reply 233 — participant_153 · 2021-06-15 · post-27620363

<!-- artifact:quote:start -->
> Darsara said: If there's only five in total with all ages unlocked, then does everyone start with 2 in 867 and some still have only 2 in 1066? Big gap. Click to expand...
<!-- artifact:quote:end -->
Yeah I think the wording is awkward. They mean you start with 5 as your cap, but your cap goes up by one with each new era.

## Reply 234 — participant_162 · 2021-06-15 · post-27620366

How will the cultural mingling work for melting pot cultures? Will the specific requirements of adapting to a new culture be clearly listed in the game? For example If I’m Anglo-Saxon will I be told what I need to do in order to become English? At present you become either a French or Norman culture and then take a decision to become English, but I imagine with cultural mingling it should be a much more gradual process? Or is it still decision based? Will you need a certain level of cultural appreciation? Will my ruler first need to learn French? Or do I simply create a new culture altogether?

## Reply 235 — participant_153 · 2021-06-15 · post-27620368

<!-- artifact:quote:start -->
> Marcus Pica said: Carantanian culture when? Click to expand...
<!-- artifact:quote:end -->
One Proud Bavarian pointed out that Bavian culture no longer goes to the Mediterranean in the Bavian screen shot. So maybe that means they added some new cultures.

## Reply 236 — participant_163 · 2021-06-15 · post-27620373

This is a huge improvement over the current way cultures are represented in game. I really love it. I'd also really like to know how will be handled some of the current in-game events, like the Roman restoration that currently excludes some cultures like "Cisalpine", Sicilian and Sardinian, despite being Italian too like the central Italians. And will be Coptic culture come back?

## Reply 237 — participant_153 · 2021-06-15 · post-27620377

<!-- artifact:quote:start -->
> Vegetalss4 said: Would how much/whether revoking a title from a differently cultured vassal be affected by whether the revocation is justified or not? Likewise is there some sort of bonus for the reverse, giving titles to differently cultured vassals? It would be nice for me as the king of France to able to revoke a title from Duke Traitor the Aptly Named of Toulouse and avoid this act of justice hurting the acceptance between French and Occitan by making sure that the new duke of toulouse also is occitan. That'd also make sense from an in-universe perspective since that'd mean that it really would be a punishment toward ex-duke Traitor specifically, and not an instance of occitan people getting a bit more marginalized from the kingdoms halls of power. Click to expand...
<!-- artifact:quote:end -->
I would love the acceptance system to work something like this. Related to this I hope they make it easier to grant titles to character that match the local culture For instance being able to set a filter to grab character that is the same as the local culture (and/or faith) without having to type what that is each time. Also if the auto grant title button came in two flavours, one that granted to a character of your culture/faith and another that granted to a character of the local culture/faith.

## Reply 238 — participant_164 · 2021-06-16 · post-27620438

I really hope tenets will be reworked to have an arbitrary number like cultural traditions in the future.

## Reply 239 — participant_165 · 2021-06-16 · post-27620441

I think gender roles should be mostly moved from the religion system to the culture system. It has felt very strange to me that a ruler can create a new faith with a radically different gender doctrine and everybody who converts to the faith just goes along with it. The addition of Noble Martial Customs is a great bit of nuance, but the culture rework should go further and tie gender roles to culture while adding more nuance (such as what existed in CK2).

## Reply 240 — participant_160 · 2021-06-16 · post-27620454

<!-- artifact:quote:start -->
> Tuo said: I'd like to point out the screenshot in the post shows 4/6 traditions. Click to expand...
<!-- artifact:quote:end -->
True... so saying 5 in total in the text is just... really, really weird/wrong. Should be five BASE, unless the pictures are out of date. ADD: I'd even wondered if they meant extra unlocking with age, but convinced myself they wouldn't have used 'total' then... sigh.

## Reply 241 — participant_166 · 2021-06-16 · post-27620472

This DLC looks amazing, absolutely can't wait for this.

## Reply 242 — participant_167 · 2021-06-16 · post-27620484

Perhaps it might be more interesting for the cultural head to be the character or landed character of that culture with the highest learning score, i.e. the most learned living notable person at any given time. Or some other factor than just highest county number. This would make for more dynamic gameplay, as it's already so easy to be cultural head, dynasty and house head after early game. Now maybe there'd be more of a decision, maybe you go after influencing your culture or influencing your dynasty but it's harder for a character to end up managing both.

## Reply 243 — participant_168 · 2021-06-16 · post-27620497

Eu simplesmente adorei! Essa remodelação de cultura vai mudar completamente a minha maneira de jogar, também acredito que vai tornar o jogo muito orgânico!

## Reply 244 — participant_169 · 2021-06-16 · post-27620524

Sorry if its been asked before, but how come we can no longer see the reactions to the main post anymore? At least it dosent appear in my mobile device.

## Reply 245 — participant_170 · 2021-06-16 · post-27620541

<!-- artifact:quote:start -->
> Zhetone said: this system invites these problems because the ethos are in fact just baked in stereotypes about warrior cultures, poet cultures etc. Click to expand...
<!-- artifact:quote:end -->
yeah i actually think this system is kinda gross for this reason. its literally just stereotypes galore in a way that i am very much not a fan of.

## Reply 246 — participant_171 · 2021-06-16 · post-27620562

The cultural rework is really awesome cant wait to try it, thank you for your great work. If you can please enable reformation for religions with the patch, so we dont need to found a new religion for every change. If we have the control and can pay the piety we should be able to reform a religion by editing it instead of creating a new one. So we can slowly reform a religion and not only a one time thing where we have to change it all at once. That would allow both features to work even better together.

## Reply 247 — participant_172 · 2021-06-16 · post-27620571

I'm curious as to the reason as to why you chose Inventive for the Anglo-Saxons and Spiritual for the Mashriqis. I've never really associated the Anglo-Saxons as being great scientists and the Levant had incredible universities in the Middle Ages.

## Reply 248 — participant_173 · 2021-06-16 · post-27620579

yo this is actually pretty fucking cool

## Reply 249 — participant_174 · 2021-06-16 · post-27620715

Yes!, question Will be able to merge cultures now like develop new cutlures from two or more cultures in your domains?

## Reply 250 — participant_175 · 2021-06-16 · post-27620732

Very interesting. I would like it if these new traditions and cultural acceptance mechanics played an interesting role in establishing melting pot cultures. I.e. having similar traditions and heritage increases cultural acceptance and high levels of cultural acceptance and proximity leads to a melting-pot. This could also be applied to languages if they can be created dynamically. Would love to have a dynasty speak Sino-Nordic creole. This would be a decent facsimile of the effects the Norman Conquest had on english culture and languages, as well as other cultural mixing that occurred throughout the time period.

## Reply 251 — participant_176 · 2021-06-16 · post-27620753

Looks absolutely great, really excited to experience the new features. CK3 is definitely a worthy successor to CK2, keep it up

## Reply 252 — participant_177 · 2021-06-16 · post-27620756

This is fantastic news! A much needed flavor boost. I can't wait to get into it... once my current playthrough is over of course. Great work!

## Reply 253 — participant_178 · 2021-06-16 · post-27620758

<!-- artifact:quote:start -->
> Servancour said: CK3 Dev Diary #64 - Cultures Are Forever​Salutations! Before we begin, first things first. We are working on an additional patch to fix some of the issues introduced in 1.4. The patch is still being worked on, but if everything goes as planned, we should be able to get it out sometime next week or so. We’ll let you know once the patch is ready. With that out of the way, let’s talk about something I’m quite excited to share with you all. As you probably know already, we’ve talked a bit about how we are revisiting cultures for the next expansion: Royal Court. Unlike faiths, which got a lot of attention prior to release as we made them quite dynamic and customizable, cultures can feel a bit static, and aren't anywhere near as interesting as faiths. That is all about to change! We are revising cultures as you know them. Most exciting is perhaps the possibility to create new cultures! Both for simulating historical events and to create plausible and interesting alt-history scenarios. But I’m getting ahead of myself. For now, let’s start by looking at the foundation of a culture and the different components they are made of. This is what the new culture screen will look like. View attachment 731851 [Image of the new and updated culture interface]​ Cultural Pillars​A culture has five main Cultural Pillars. These are Ethos, Heritage, Language, Martial Custom, and finally Aesthetics. Of these, the Ethos is perhaps the most significant, but all of them play a particular role in how a culture plays and how cultures view each other. Ethos Each ethos is framed around a particular theme that somehow ties into a fairly broad definition of what a culture is. A culture’s ethos not only provides effects and bonuses for having it, it also ties into how easy or difficult it is to acquire certain traditions (more on this further down). There are seven in total: Bellicose Communal Courtly Egalitarian Inventive Spiritual Stoic Here are a few examples of what they may look like in-game: View attachment 731852 [Image of the Bellicose ethos] View attachment 731853 [Image of the Spiritual ethos] View attachment 731854 [Image of the Inventive ethos]​ Heritage A culture's heritage can be compared to the culture groups that you may be used to in the existing system. Heritages will roughly match said culture groups. You’ll see an Iberian Heritage for cultures like Basque and Castilian, or Turkic Heritage for Turkic cultures, such as Oghuz and Cuman. In terms of gameplay, the most outstanding effect of a shared heritage is the impact it has on Cultural Acceptance. Language Each culture has a designated language. Languages vary greatly across the map and between cultures. Some languages, such as Arabic, are spoken by quite a few cultures. Other languages are spoken by no more than two or three cultures, or in some cases, cultures even have their own unique language. An example of these would be Basque, who really don't have any closely related languages and it wouldn’t make too much sense to group them together with their neighbors. The vast majority of cultures share a language though, as a sort of “language group” rather than a specific language. Characters can always speak the associated language of their culture. They are, however, also able to learn multiple languages over their lifetime. Knowing multiple languages has its benefits, as speaking the same language as another character of a different culture, and county, will reduce the opinion penalty that character, or county, has towards you. Knowing the native language (i.e. the language of their culture) of your vassals is therefore fairly beneficial as a means of increasing their opinion of you. Noble Martial Custom The martial custom decides which gender you may appoint as knights and commanders. As you’d expect, you can either appoint men, women, or both. We always felt that having the gender doctrine on faiths decide which characters can and cannot participate in battles felt off. The doctrine is about the right to rule and the holding of titles, more so than anything else. Just because you want the Equal doctrine to allow female rulers, doesn’t mean that women would automatically lead your armies or join you as knights. Revising cultures gave us the ample opportunity to move the functionality from faiths over to cultures. Which also means that you’ll have additional options in shaping your realm. Aesthetics This pillar is really a collection of several smaller properties for what a culture “looks” like. It decides what type of clothes characters wear, the coat of arms style for dynasties, what architecture holdings use, and the type of armor the units on the map wear. This is also the pillar that contains what naming practices the culture uses. Mainly what character names to use, if they use a dynasty prefix, etc. The naming practice will also be used to change title and holding names, which used to be set per culture, so as to not have titles change names if you create a new culture. For all of you modders out there; all of these can be set individually per culture. Allowing you to mix and match the different aesthetics to your heart’s content. Traditions​Traditions are the meat of the cultural overhaul, and provide that extra layer of variety and immersion that can have a significant impact on gameplay. An important aspect of traditions is that they give us a clear means of visualizing and explaining existing mechanics that previously just “was a thing” and never explained. Take Anglo-Saxon as an example. They have access to the Saxon Elective succession for no apparent reason other than “they do”. Instead, they now have a tradition that grants them the succession law, making it clear as to why they have it. Secondly, and perhaps more importantly, traditions serve as the perfect means of giving a culture additional flavour or gameplay bonuses that add a greater degree of variety across the map. A culture can have no more than five traditions in total, but this number will increase as you enter a new era. Most cultures will start the game with around three or four, which leaves plenty of room for you to shape your culture as you play the game. As the cultural head, you’ll have the ability to establish new traditions. Not all traditions will be available everywhere. We have both regional traditions, as well as traditions that are available depending on your heritage. The vast majority of them can be established regardless of circumstances, but might require certain conditions, such as ‘Hill Dwellers’ having the requirement that your culture must be present in a county with hills. Traditions cost prestige to adopt. Which will be the largest hurdle for you to overcome if you want a specific tradition. The prestige cost is dependent on your ethos. Certain traditions will be more expensive than others, if you don’t have a matching ethos. Similarly, a tradition will increase in cost if your culture, or in some cases the cultural head, doesn’t fulfill a specific and thematic requirement. An example would be a tradition named ‘Only the Strong’, which is more expensive if you as the cultural head don't have at least six knights with at least 12 prowess. The increased cost is meant to act as a softer limit and make it slightly more difficult to establish certain traditions (depending on your circumstances), but not as much as to make it impossible to do so, should you want to go and unlock a particular tradition. Instead of explaining traditions in detail, I’ll just show you a few examples of what traditions may look like, as well as the type of effects you can expect from them. View attachment 731855 [Image of the Swords for Hire tradition] View attachment 731856 [Image of the Chivalry tradition] View attachment 731857 [Image of the Esteemed Hospitality tradition] View attachment 731858 [Image of the Seafarers tradition] View attachment 731859 [Image of the Land of the Bow tradition]​ Cultural Acceptance​Cultural acceptance can be described as how well intermingled two cultures are, and how accepting they are of each other. Which means that given enough time, cultures will dislike each other less, and culture converting everything within your realm is no longer the only solution to combat cultural differences. The opinion penalty of being of a different culture used to be a static value. Now, it will depend on the cultural acceptance between your culture and the target culture. Each culture has an acceptance value of another culture, visualized as a percentage. Depending on the amount of acceptance, the “different culture” opinion penalty will gradually be reduced. At 0% acceptance, you’ll have the full opinion penalty. At 100%, the penalty is removed altogether. Acceptance goes both ways. So if the French have a 20% acceptance towards Normans, the same will be true from the Norman perspective. There are two ways for acceptance to change. The first is an acceptance baseline. Which increases if two cultures share similarities with one another. There are a number of different modifiers that can increase the baseline. Such as cultures that share the same religion or faith, ethos, or language. The most impactful modifier, however, is heritage. If two cultures share the same heritage, they have a significant bonus to their baseline. If acceptance is above the baseline, it will slowly decay over time towards the targeted value. Being below the baseline on the other hand, will not make the acceptance increase. A bad relation between cultures won’t disappear overnight. Secondly, acceptance very much changes depending on the circumstances. Don’t expect two cultures that never interact with one another to gain acceptance. If cultures exist within the same realm though, it will increase over time. This applies to both counties of another culture within your realm, as well as vassals. Acceptance is also reactive. Taking certain actions towards characters of a different culture will have consequences on your acceptance, such as declaring war or revoking titles. This generally scales on size. While the difference isn’t huge, revoking a single county from a small culture will decrease your acceptance more than if you would revoke a county from a much larger culture. At the end of the day, if you want to maintain a high acceptance and keep your Occitan vassals in France happy, you are at least gonna have to try and be nice to them. View attachment 731860 [Image of what the cultural acceptance between two cultures may look like]​ There we go. That’s what a culture will look like in the near future. Oh! Before I forget; Best of all? The cultural rework is free, and will accompany the free update that launches alongside the Royal Court expansion! Until next time! Click to expand...
<!-- artifact:quote:end -->
I like where this is going. wonder if we can get more from this with being able to pick up culture alined men at arms and mercenaries to boot. it will go a long way if anyone wants to try and restore rome and her natural borders to try and pick up the stuff from the old borders of the empire from england to iraq and everything in between.

## Reply 254 — participant_179 · 2021-06-16 · post-27620799

Love the potential here, can't wait to hear more about cultural divergence and new cultures. Personally I'd like having the ability to change Traditions without having to create a whole new culture. But having the Pillars be sort of locked in seems fine and I think that would be a good middle ground.

## Reply 255 — participant_180 · 2021-06-16 · post-27620807

Could we get a sneak peak at Sephardi and Ashkenazi cultures? They're not, like, a huge spoiler hopefully, so that'd be okay, right?

## Reply 256 — participant_181 · 2021-06-16 · post-27620816

Looks very interesting. And it is about time the Nubians got their appropriate archer men-at-arms.

## Reply 257 — participant_014 · 2021-06-16 · post-27620817

<!-- artifact:quote:start -->
> Karlingid said: Could we get a sneak peak at Sephardi and Ashkenazi cultures? They're not, like, a huge spoiler hopefully, so that'd be okay, right? Click to expand...
<!-- artifact:quote:end -->
If we're requesting Cultural sneak peaks, I'd like to see the Tamils if possible, thank you

## Reply 258 — participant_091 · 2021-06-16 · post-27620827

Ok for you guys who are questioning anglo saxon inventiveness. The anglo saxons and by large part the romano brytonics had turned england from a land of almost completely forests and other unproductive terrain into a fairly large agricultural area in a relative to its neighboring regions

## Reply 259 — participant_182 · 2021-06-16 · post-27620842

No plans for moving more of the gender laws to culture? Who can and cannot be appointed as councillor also seems more sensible to add to cultural properties.

## Reply 260 — participant_183 · 2021-06-16 · post-27620868

This looks good.

## Reply 261 — participant_184 · 2021-06-16 · post-27620891

@Servancour Does aesthetics dictate both ethnicity and the way people dress?I think it would be great if instead you can separate them and have people of say the Asian ethnicity in European dress for example.

## Reply 262 — participant_185 · 2021-06-16 · post-27620927

Who will be the cultural head? As now, the ruler with the most same-culture counties? This could be made more challenging, too. It could be based on more factor, not just one. Being an idiot and conquering all same-culture counties does not make you a cultural figurehead. Possible factors: Development of all same-culture provinces under your rule. Learning Perks from the Scholarship tree Level of Fame Court Grandeur Dynasty's Level of Splendor Cultural buildings and county modifiers in your realm (university, runestone...) Same-culture Inspired characters in your court This could mean that even a vassal could be the cultural head, coming before his same-culture liege. It also initiates a culture-head race between rulers.

## Reply 263 — participant_186 · 2021-06-16 · post-27621008

Will it be possible to change existing cultures in a similar way to how you modify existing religions? I know it's unrealistic, but I'd still prefer to change my existing culture to allow women in the military instead of creating a new one solely for that purpose...

## Reply 264 — participant_187 · 2021-06-16 · post-27621033

<!-- artifact:quote:start -->
> Josh is Stupid said: Will it be possible to change existing cultures in a similar way to how you modify existing religions? I know it's unrealistic, but I'd still prefer to change my existing culture to allow women in the military instead of creating a new one solely for that purpose... Click to expand...
<!-- artifact:quote:end -->
You create a new faith to modify its tenets, same would probably pertain to culture.

## Reply 265 — participant_188 · 2021-06-16 · post-27621040

If you switch cultures, does your character "forget" his former language? I hope not. And if you keep the ability to speak your old language, would not "Convert to local culture" be the much easier way to deal with a bilingual realm, given how easy that decision is? Id argue that switching cultures should be more difficult than learning languages. Id even say that learning the language of a culture should be necessary before you can call yourself "of that culture".

## Reply 266 — participant_189 · 2021-06-16 · post-27621080

I like the new system, except ethos and creating cultures. Ethos are way to stereotypical sadly and creating new cultures as ruler seems bizarre. Otherwise I like the system, even the traditions. Just ethoses are too much in my opinion.

## Reply 267 — participant_038 · 2021-06-16 · post-27621113

<!-- artifact:quote:start -->
> Frigabus said: Who will be the cultural head? As now, the ruler with the most same-culture counties? This could be made more challenging, too. It could be based on more factor, not just one. Being an idiot and conquering all same-culture counties does not make you a cultural figurehead. Click to expand...
<!-- artifact:quote:end -->
Agree, at the very minimum it should be "who has the most development in this culture provinces" (first suggestion) instead of how it works now

## Reply 268 — participant_038 · 2021-06-16 · post-27621120

<!-- artifact:quote:start -->
> Josh is Stupid said: Will it be possible to change existing cultures in a similar way to how you modify existing religions? Click to expand...
<!-- artifact:quote:end -->
But you can't modify religions now? Only creating new Faiths

## Reply 269 — participant_190 · 2021-06-16 · post-27621256

Please tell me, won't cultures now assimilate as quickly as they used to? It was just strange when the conditional Ireland could make the whole of Paris speak Irish in 10 years. At least in the history of the Middle Ages, as far as I know, the policy of assimilation was not widespread among the rulers. People were primarily united by religion, and who you are - German, French or Icelander - did not matter. And if now we set the assimilation rate to the lowest, will it be possible to play in a state where there are many different cultures that are tolerant of each other?

## Reply 270 — participant_191 · 2021-06-16 · post-27621281

I love this, I have always wanted more differentiation for cultures in CK, as well as means of peaceful coexistence.

## Reply 271 — participant_192 · 2021-06-16 · post-27621337

<!-- artifact:quote:start -->
> Servancour said: A culture can have no more than five traditions in total, but this number will increase as you enter a new era. Most cultures will start the game with around three or four, which leaves plenty of room for you to shape your culture as you play the game. As the cultural head, you’ll have the ability to establish new traditions. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Servancour said: f acceptance is above the baseline, it will slowly decay over time towards the targeted value. Being below the baseline on the other hand, will not make the acceptance increase. A bad relation between cultures won’t disappear overnight. Secondly, acceptance very much changes depending on the circumstances. Click to expand...
<!-- artifact:quote:end -->
Maybe I'm missing something obvious, but if you start with 4/5 slots filled, that doesn't immediately sound like a lot of choice. Are there ways to abandon traditions too? (presumably carving out your own new proto-culture if you are a non-cultural head, like how creating your own religion works). Are there plans for special schemes or plots to try and cause cultural friction between groups in other realms? e.g. if a neighbouring king has annexed people of another culture, can I send my spies to all the pubs and inns in the region and stoke "cultural tensions" with the peasants - or even the annexed vassal-lords - to trigger revolts? Or if I can get in good with their realm's clergy (or equiv), such as if the new ruler is impious, I can have them do that tension-stoking work, vs their new overlords, for me?

## Reply 272 — participant_001 · 2021-06-16 · post-27621427

<!-- artifact:quote:start -->
> Pancakelord said: Maybe I'm missing something obvious, but if you start with 4/5 slots filled, that doesn't immediately sound like a lot of choice. Click to expand...
<!-- artifact:quote:end -->
I shouldn't have used the words "in total", that was needlessly confusing. While numbers are subject to change, the current setup is that you start with a maximum of 5 tradition slots in the tribal era, and then gain +1 for each additional era your culture enters, for a maximum of 8 slots once you are in the Late Medieval era.

## Reply 273 — participant_193 · 2021-06-16 · post-27621475

The culture overhaul is something I'm really looking forward! That said, something about this feels weird to me and I think it is the way traditions are handled. If I've understood correctly, you buy a tradition for an amount of prestige determined by your ethos and certain criteria, like the size of your military for military traditions. The latter however, only raises the price. Here's an example of the stiff situation I'm worried about: My people in-game are seafarers who live in the hills, and they've done so for years. For whatever reason we have neither the seafarers nor the hill-dweller traditions (maybe we came from somewhere else originally, or maybe the devs gave us chivalry instead?). But here's the deal, I only have enough prestige for one tradition and I pick seafaring. So, while I wait for more prestige to come in so I can buy hill-dwellers, what are my people up to? Are they too dumb to figure out how hills work? Granted, I don't really know how this will work in-game with balancing and such. However, if the base price is based on your ethos and further penalties are applied if you don't fullfill certain criteria, wouldn't say a spiritual culture potentially be better at figuring out hills than say an egalitarian? I don't know, but it sounds weird to me. Ideally I would have liked My first instinct would be a system inspired perhaps by institutions in EU4 (how they work on a province level and how the price depends on how many provinces they're present in) and/or general traits in HoI4 (how their xp is based on what your generals are up to). So for instance, seafaring traditions should spread and grow in all coastal provinces, and if you in addition to that sail a lot, you get seafaring "xp". And then depending on how many provinces you have with the seafaring tradition, and how much xp you have, you get a discount. Maybe it could even be free if you have enough? This might just be an overcomplication though. (EDIT) I just want to clarify that I don't want a carbon-copy of the institutions-system were by the end of the game, everyone has every tradition. What I want is a system were, for instance, everyone who lives by the coast slowly develop a tradition in seafaring, just like how institutions are developed in EU4-provinces. The prestige-cost could then be visualized as convincing the rest of your culture that seafaring is indeed your way of life. (EDIT2) What I feel is that the connection between flavour and gameplay is too weak for me. It makes perfect sense that militaristic cultures should have an easier time getting military traditions, but when you start giving said traditions fancy names, things stop adding up for me. Take Hill-dwellers for instance. What's spiritual about hills? what's militaristic about hills? what's egalitarian about hills? If the bonus is a combut buff in hills then yes, it makes sense for it to be a militaristic tradition etc. But at a glance there's nothing suggesting that. The name only implies that your people live in the hills, and for me that comes down to human nature, our adaptability, and not how spiritual or inventive we are. I will however say that this entire critique applies primarily to the more geographical traditions. The others look okay.

## Reply 274 — participant_194 · 2021-06-16 · post-27621526

Two ethoses per Culture would have probably been better for making them more nuanced. It'd also help create a sense of continuity if you could only change one per divergence/hybridization.

## Reply 275 — participant_195 · 2021-06-16 · post-27621566

<!-- artifact:quote:start -->
> AtilaJ.Reis said: Eu simplesmente adorei! Essa remodelação de cultura vai mudar completamente a minha maneira de jogar, também acredito que vai tornar o jogo muito orgânico! Click to expand...
<!-- artifact:quote:end -->
this is an English only forum

## Reply 276 — participant_027 · 2021-06-16 · post-27621570

<!-- artifact:quote:start -->
> Servancour said: I shouldn't have used the words "in total", that was needlessly confusing. While numbers are subject to change, the current setup is that you start with a maximum of 5 tradition slots in the tribal era, and then gain +1 for each additional era your culture enters, for a maximum of 8 slots once you are in the Late Medieval era. Click to expand...
<!-- artifact:quote:end -->
Since things like doctrines and tenets seem to be a direct inspiration for cultural pillars and traditions respectively, will we also get culture descriptions like faiths have faith descriptions? Will modders be able to add such tradition slot unlocks in script? E.g. an innovation that unlocks a tradition slot, or forming a particular title for the first time unlocks a tradition slot for the founding culture?

## Reply 277 — participant_196 · 2021-06-16 · post-27621666

@Servancour Apart from the Men-at-Arms modifiers, are there e.g. some regional/cultural techs that are going to be moved into cultures? For example the Czech Seniority succession (maybe all West Slavs should have that?) Longships and Ostsiedlung come to mind as well. What about the techs giving access to special retinues, like e.g. "Konni", will they be moved too?

## Reply 278 — participant_197 · 2021-06-16 · post-27621726

Oh wow these changes are amazing for roleplaying. Thank you!! I had a question though that may be tangentially related. Like many, I gravitated towards playing my own culture/region, in my case, the Levant. It's been really fun (like 200hrs worth of content fun), but I have to say it felt rather homogeneous compared to other parts of the map. I think Britain has more cultures than the entire Middle Eastern peninsula. Also some faith assignments have me scratching my head. It was good to see Druze for example, but why are the Maronites represented as Orthodox? Given their role in the Catholic crusades, it feels very off. I'm hoping we'll see some more compartmentalization with this culture change in the area as well. If not, at least the chosen Mashriqi ethos (spiritual) I see in the DD is very accurate. Thanks!

## Reply 279 — participant_198 · 2021-06-16 · post-27621939

One way to allow for more dynamic cultures would be to allow characters to choose another "culture" bonus as a second bonus, if they've completed a lifestyle tree that is similar to that culture and the character has other connections to that culture (for instance, Land of the Bow can't be taken without connections to Nubian counties, rulers, or counties in the Nile area). Then possessing that culture's bonus could make other aspects of ruling or changing cultures easier.

## Reply 280 — participant_199 · 2021-06-16 · post-27622032

This looks AWESOME

## Reply 281 — participant_200 · 2021-06-16 · post-27622136

This looks great but I didn't get what you need to do to gain the bonuses from the cultures. To gain the bonuses is the culture of your ruler/character that matters ? Is it the culture in your capital ? is it the culture that is most dominating in your realm ? I'm a bit confused how it works.

## Reply 282 — participant_201 · 2021-06-16 · post-27622158

I notice in the screenshot at the top of the Dev Diary mentions "Rajput Culture", and that being in reference to the culture there in the Early Medieval Period. I would like to point out that there are quite a few problems with this screenshot from a historical and linguistic point of view. First, and most importantly, the term "Rajput" to describe the hereditary class only really emerged in the 1500s. Prior to that, it referred to a courtier of sorts, which was an appointed position and absolutely not one that had anything to do with the ruling class or the nobility. Thus, during CK3's time frame, using the term Rajput to describe a culture makes absolutely no sense, even if it is being just applied to the ruling class. Further, using Rajput as a cultural term at all to describe the people of modern-day Rajasthan and Madhya Pradesh makes absolutely no sense, it would be like calling the people of France "noble" culture. Ideally, the term "Rajasthani" would be used to describe the culture of these peoples. The same really also applies to the "Rajput Aesthetics" and "Warrior Culture" portions, those make a ton of sense for EU4's time frame but really don't reflect the region until the very end of ck3's time frame, until when Rajputs were generally pastoral nomads who had a fortified settlement or such in their name. Second, the "Rajasthani language" is incorrectly applied to the timeframe of ck3. In the earlier start date, a Prakrit would likely be used as the literary language, and Old Gujarati as a spoken language. In the later start dates, even the literary language would shift to Old Gujarati. Most people agree Old Gujarati was the language spoken in both Gujarat and Rajasthan up until about the 14th century. It's only after that that "Middle Rajasthani" as a language begins to diverge. Further, modern Rajasthani is actually just a term applied together on several distinct Indo-Aryan famalies that don't necessarily have a high degree of mutual intelligibility, so it would be incorrect even if the research done to establish this "Rajasthani" language in ck3's time frame was done based on the modern-day languages of the region. I don't have specific sources for the bit on Rajput culture, this is extremely well-known information and is readily available and agreed on. As for the "Rajasthani" language, for a contemporary source, you can refer to works by Hemachandra, as well as a wealth of literature in this language written in both (modern-day) Rajasthan and Gujarat. A modern source would be Dr. Ayyappa Paniker, specifically, Medieval Indian Literature volume 3, which contains relevant information on the language.

## Reply 283 — participant_060 · 2021-06-16 · post-27622160

<!-- artifact:quote:start -->
> Metztli said: This looks great but I didn't get what you need to do to gain the bonuses from the cultures. To gain the bonuses is the culture of your ruler/character that matters ? Is it the culture in your capital ? is it the culture that is most dominating in your realm ? I'm a bit confused how it works. Click to expand...
<!-- artifact:quote:end -->
Seems pretty clear to me - if the bonus applies to character, it applies to any character of that culture, and if the bonus applies to holding/county, it applies in any county with that culture.

## Reply 284 — participant_202 · 2021-06-16 · post-27622492

<!-- artifact:quote:start -->
> Servancour said: I shouldn't have used the words "in total", that was needlessly confusing. While numbers are subject to change, the current setup is that you start with a maximum of 5 tradition slots in the tribal era, and then gain +1 for each additional era your culture enters, for a maximum of 8 slots once you are in the Late Medieval era. Click to expand...
<!-- artifact:quote:end -->
Does the default UI scale well to cultures that mysteriously acquire more traditions because the game balance demanded my obviously superior culture is not made mechanically stronger than the rest?

## Reply 285 — participant_203 · 2021-06-16 · post-27622566

Cultures Are Forever is my favourite JoJo arch. Anyway it seems interesting.

## Reply 286 — participant_204 · 2021-06-16 · post-27623009

<!-- artifact:quote:start -->
> Theyn_T said: Will modders be able to add such tradition slot unlocks in script? E.g. an innovation that unlocks a tradition slot, or forming a particular title for the first time unlocks a tradition slot for the founding culture? Click to expand...
<!-- artifact:quote:end -->
Its a modifier type that exists on the culture so it can be granted by anything applying modifiers on a culture such as eras and innovations. Less sure about forming a specific title as that won't have any tied culture modifier, but that seems pretty unrelated to a potentially larger culture spreading across the map anyway so not sure it'd make sense for that to be tied together there anyway.

## Reply 287 — participant_063 · 2021-06-17 · post-27623128

will there be mechanics for reuniting same culture counties? for example a tradition that would provide a cb for conquering neighbouring counties that are of the same culture

## Reply 288 — participant_082 · 2021-06-17 · post-27623140

<!-- artifact:quote:start -->
> Servancour said: An important aspect of traditions is that they give us a clear means of visualizing and explaining existing mechanics that previously just “was a thing” and never explained. Take Anglo-Saxon as an example. They have access to the Saxon Elective succession for no apparent reason other than “they do”. Instead, they now have a tradition that grants them the succession law, making it clear as to why they have it.​ Click to expand...
<!-- artifact:quote:end -->
I'm curious if there are plans to add more unique succession types and tie them to cultural traditions. For example, Makuria used a matrilineal form of succession, in which the kingship passed through the female line, but was held by a male. So the king would be succeeded not by his son, but by his nephew - specifically his eldest sister's eldest son. The Karakhanids used a seniority-like succession, but with elements of partition, where the sons of a ruler would inherit their own appenages, but the top title would go to the eldest member of the dynasty (or house). Essentially a blend of High Partition and Seniority. As it stands right now, the ability to add some of these more unique succession types (especially Makuria's) via mods feels limited - there's just not enough functionality exposed to make them happen, as far as I can tell. So since we have to rely on them being implemented in the engine (or an upgrade to the scripting power for succession laws), it seems like a cultural overhaul would be a convenient time to do so.

## Reply 289 — participant_205 · 2021-06-17 · post-27623264

<!-- artifact:quote:start -->
> Bandua_of_Gallaecia said: Will the fact that Aesthetics, Language and Heritage are separated now mean that cultures in the same "culture group" will be able to have different architectural sets? Does this mean that for example it will be possible that Galicians/Portuguese will be able to have an Atlantic set, as opposed to the Mediterranean style of the Aragonese/Catalans? Examples of what I mean: Galician: View attachment 731970View attachment 731969View attachment 731967View attachment 731972 Portuguese:View attachment 731973View attachment 731968View attachment 731966View attachment 731971 Aragonese:View attachment 731963View attachment 731962View attachment 731964View attachment 731959 Catalan:View attachment 731961View attachment 731960View attachment 731958View attachment 731965 So right now, all Iberians use the Mediterranean set: View attachment 731975 Would it be possible for the Galician, Portuguese and Asturleonese cultures to have a different aesthetic to the Castilian/Aragonese/Catalan one? Example of an hypothetical Atlantic set: View attachment 731978 Click to expand...
<!-- artifact:quote:end -->
IMHO I’d like to see three variables in the holding images: terrain, building materials, and building (culture-based) style. These could combine to give unique graphics that are also location-realistic.

## Reply 290 — participant_077 · 2021-06-17 · post-27623320

<!-- artifact:quote:start -->
> james24eagle said: IMHO I’d like to see three variables in the holding images: terrain, building materials, and building (culture-based) style. These could combine to give unique graphics that are also location-realistic. Click to expand...
<!-- artifact:quote:end -->
This is a fantastic idea. Arquitecture is the way it is more due to geographic reasons, than cultural per say. East, Central and North Europeans built high roofs because it was better to handle the weight of the snow. When the crusaders built castles in the middle East they wouldn't build these roofs in the same way they would in Europe. Middle Easterners didn't build roofs because excess rain wasn't an issue. Had they ever built a castle in Ireland or Galicia and they would most definitely have to build a roof or the incessant rain would collapse the entire ceiling. And while French castles in Brittany and Gascony might have similar designs overall, the type of rock you can find in Brittany is quite different from the one found in Gascony, so even though the shape might be similar, the colour and texture will most definitely be not.

## Reply 291 — participant_185 · 2021-06-17 · post-27623589

What about learning foreign languages in childhood? If the child has a guardian with a foreign culture, it might give her/him a chance to learn the guardian's language.

## Reply 292 — participant_051 · 2021-06-17 · post-27623677

<!-- artifact:quote:start -->
> Xain said: A pretty minor point, but if a child grows of one culture until a reasonable age (say, 10), and then is educated into another culture, will he automatically speak both cultures' respective languages? Click to expand...
<!-- artifact:quote:end -->
@rageair @Servancour ?

## Reply 293 — participant_206 · 2021-06-17 · post-27624607

<!-- artifact:quote:start -->
> Tuo said: I get the impression the ethoses (ethosi?) Click to expand...
<!-- artifact:quote:end -->
Ethoi.

## Reply 294 — participant_108 · 2021-06-17 · post-27624812

For "growing up speaking languages", perhaps the child should have a strong chance of learning the language of *both* their parents and their tutor? After all it'd be hard for their tutor to teach them anything if they don't share a language. Perhaps it should even be a requirement that the tutor speaks *a* language in common with the child (and thus presumably their controlling parent) to start with?

## Reply 295 — participant_207 · 2021-06-17 · post-27625026

<!-- artifact:quote:start -->
> Tuo said: I get the impression the ethoses (ethosi?) shown are not necessary the ones the attached cultures will have when the DLC is released, but instead are just shown demonstratively here. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Lorehead said: Ethoi. Click to expand...
<!-- artifact:quote:end -->
Ethoses. "Ethoi" is incorrect. (I know the link says it's incorrect, I'm posting this just in case someone doesn't bother checking the link. )

## Reply 296 — participant_187 · 2021-06-17 · post-27625079

<!-- artifact:quote:start -->
> Karlington said: Ethoses. "Ethoi" is incorrect. (I know the link says it's incorrect, I'm posting this just in case someone doesn't bother checking the link. ) Click to expand...
<!-- artifact:quote:end -->
Yeah, technically ethos should give ethe (ἤθη).

## Reply 297 — participant_206 · 2021-06-17 · post-27625089

<!-- artifact:quote:start -->
> Karlington said: Ethoses. "Ethoi" is incorrect. (I know the link says it's incorrect, I'm posting this just in case someone doesn't bother checking the link. ) Click to expand...
<!-- artifact:quote:end -->
The actual plural in Classical Greek would have been ethea or ethe. In English, the plural is ethoses.

## Reply 298 — participant_208 · 2021-06-17 · post-27625319

Overall, I like it quite a lot. There are quite a few interesting tidbits of information here. First, I like the sheer amount of various traditions. With more than a hundred of them we'd be able to make quite unique cultures. Secondly, I think it was already hinted at before, but the heritage pillar makes it pretty clear that culture groups as we know them are gone. Given how pillars can be changed thanks to divergence and hybridization, and with the comment in this diary about how the system is mod friendly, I think this also means that with the help of effect scripting you'll be able to replace a heritage pillar for a culture without changing the culture itself. Which is particularly useful for me, because I'm working on a personal project on expanding the scope of forming the Empire of Slavia. One of the aspects of that projects is making so all Slavic cultures become a single culture group, as I find it rather ridiculous that after unifying all Slavs as, let's say, West Slavic character, your East and South Slavic subjects still have the same opinion penalty towards you as if you were Mongol. And since you can't move cultures from one culture group to another, it requires an annoying workaround of creating copies of each Slavic culture within the new unified Slavic group, and then making so all Slavic characters and provinces change their culture from their old West/East/South Slavic culture to their equivalent Slavic culture (mirroring the way events like culture splits are coded). Which in turn requires updating all kinds of files, starting with a few hundred cultural names for holdings. But now, if things here work as I hope they do, all that will be required is to make it so all Slavic cultures change their heritage pillar from West/East/South Slavic to the new Slavic one. Speaking of which, please make it so we can make traits that give opinion bonuses from characters whose culture shares the heritage pillar of yours. With the current culture/culture group system you can make traits that give an opinion bonus based on same culture, but not same culture group (let alone specific culture groups). Moving on, the third thing I like is the granularity of the cultural acceptance system. What particularly grabbed my attention is the mention of cultures sharing a religion. Which, in turn, indicates that cultures and religions are going to be linked in some way and, judging by the screenshot, cultures will have a majority religion/faith associated with them. Onto the things I dislike then. First of all, I already mentioned in both previous two dev diaries for the Royal Court is that, as much as like what I'm seeing, I don't see how the amount of content it's going to have justifies the 50% price of the DLC compared to DLCs of previous PDX titles, even big ones like Emperor (which still cost 20 dollars unlike the 30 for CKIII's DLCs). Or, more specifically, how it fulfills the criteria of Paradox's own justification of the price increase. And that was when the only piece of the announced content that was specified to be a part of the free patch was the return of the minor titles. Now it's been confirmed that the big culture overhaul is going to be free content too. And sure, we will still have cultural divergence and hybridization in the DLC. But those are only going us to allow to swap the building blocks of the new culture system around. The mean of the new culture system is going to be a part of the free patch, while divergence and hybridization are just the sauce. Side dish at best. And contrary to what certain ivory aficionados of the gallant persuasion tried to push as the truth in response to this being pointed out, the aforementioned justification for the price increase of the DLCs by Paradox itself clearly stated that it's because of the increased size of the DLC content itself. With no mention of the free patch content playing into that as well. Even though in that very same post about the new pricing structure for CKIII, just one paragraph earlier no less, Paradox itself made a clear delineation between DLCs (further separated between flavor packs and major expansions) and free patches. Besides, the free patch is quite telling here. The free patch content simply cannot justify the price increase of the DLCs (even if it's the free patch accompanying that exact DLC), because at that point it ceases to be truly free. Don't get me wrong, it's not like I'm against free patch content. Just the opposite. Given how Paradox works, DLC content is rarely ever updated in later DLCs or linked to their own systems, no matter how much it'd make sense for them to be linked. But free content can be further updated by DLCs because, well, it's free. But that's beside the point here. Paradox promised the 50% DLC price hike will be justified by increase in content and the DLC content just shrunk significantly thanks to this confirmation. And I was willing to give Paradox the benefit of the doubt here, thinking that there will be hefty amount of artwork to go with the new mechanics. But third Royal Court dev diary in a row they themselves dispelled the validity of giving them that benefit. First they announced that they will be creating just four visual styles for the courts (corresponding to the four general areas that start as feudal/clan, despite the fact that all other areas are supposed to turn feudal/clan anyway), even though we are still months away from the release which would give them ample time to create the necessary artwork. And now they confirmed the whole shtick with culture aesthetic is not going to translate to anything in regards to holding graphics. Moving on to something I also already addressed in reply to the previous Royal Court dev diary, i.e. cultural ethea. Particularly with how they correlate to the topic of the previous dev diary, i.e. court types. The issue here is that the court type is, by the sounds of it, going to be a pretty important decision. Except thanks to how it interacts with ethea, it's a heavily limited choice. And like I said in the previous diary, in general choice is good for games. But not when done like this. There are seven ethea and five court types, with each ethos giving access to multiple court types. But not all of them. My guess is two or maybe three at best. The problem here is that the ethos of your culture is locked into place from the get go. So let's say you want to play as a Swedish character because that time you decided to try surströmming made you develop Stockholm syndrome towards the Swedish culture. Giving Paradox's penchant for nationalistic chest-thumping and memes, I'm going to guess that the ethos of Swedish culture is going to be bellicose because vikings. Which, in turn, is probably going to give you access to martial and intrigue courts. Now, what happens if you want to have a stewardship court instead? You're simply out of luck. In both this and the previous dev diary Paradox explicitly stated that your only choice to change the ethos of your culture is to use either cultural divergence or hybridization. Which means creating a culture that's explicitly not Swedish. Completely defeating the point of wanting to play as a specifically Swedish character in the first place. As such, if you want to remain Swedish it means your choice is limited in the aforementioned bad way. It's as if Paradox prevented Catholic characters from picking the intrigue lifestyle, because a pious Catholic would not partake in such endeavors. What makes it even more annoying is that even when it comes to other aspects of culture you are not limited in this way. Sure, you get 3 or 4 traditions from the get go, but the remaining 5 or 4 choices are still up to you. Actually, now that they stated the base culture overhaul is part of the free patch, the whole monetization topic from before kinda plays into this as well. Because if the cultural overhaul itself is free but the features that allow you to change aspects of a culture are fancy paid content toys and these are about creating new cultures, of course Paradox is not going to give us the ability to change the base cultures as well, as this would disincentivize people from buying the expansion, no matter how slightly. Also, while I'm on the topic of ethea, I find their selection to be weirdly limiting. The lack of any ethos focusing on business acumen is particularly surprising. But so is the lack of anything about arts or architecture. I suppose Paradox wanted to avoid some stereotypes here, but all current ethea are a can of stereotypical worms regardless. Finally, a neutral observation. More of a question, really. Are mercenary companies, particularly how they interplay with culture, going to be changed as well? Because the way it works right now is that a culture can spawn up to three different mercenary companies, depending on its size. And no more, even if you manage to convert the entire world to your culture. So I'm confused as to how the bonuses to available mercenary companies from the bellicose ethos and the swords for hire tradition are going to work. Because that translates up to, respectively, 3.6 and 4.5 mercenary companies. Is this going to be rounded up all the way to 4 and 5, respectively? Also, what's the point of more mercenary companies of your culture in the first place? Will that interplay with the mercenary cost changes from 1.4 in some way and you'll get a discount for mercenary companies from your cultures? Oh, and while I'm asking questions, do the borders of traditions mean anything? I assume the background color corresponds to its relevant attribute, but what about the borders? I noticed that, barring the color of course, the borders for land of the bow and esteemed hospitality are the same, for example.

## Reply 299 — participant_043 · 2021-06-17 · post-27625582

<!-- artifact:quote:start -->
> SauronGorthaur said: Actually, now that they stated the base culture overhaul is part of the free patch, the whole monetization topic from before kinda plays into this as well. Because if the cultural overhaul itself is free but the features that allow you to change aspects of a culture are fancy paid content toys and these are about creating new cultures, of course Paradox is not going to give us the ability to change the base cultures as well, as this would disincentivize people from buying the expansion, no matter how slightly. Click to expand...
<!-- artifact:quote:end -->
I think you might be onto something here. And honestly if that is indeed the reason they aren't going to make a proper system for adjusting your existing culture without branching off into a new one then that is seriously bad news for future ck3 mechanics Still though this problem then could be avoided by making the switching of ethos and traditions of an existing culture part of the dlc features

## Reply 300 — participant_209 · 2021-06-18 · post-27626143

Oh geez, I wish I would have asked this earlier to when the Dev Diary was released, but hopefully I can still get an answer: What determines what languages your ruler can learn? I ask this specifically because I have a roleplay scenario where I play myself married to my girlfriend (who is Taiwanese) so I always just slapped her down with Chinese culture in the middle of the Netherlands with me where my ancestors are from. Is it regionally proximity based? If I can only learn the languages of surrounded regions, does that mean I won't be able to learn my partners language? Or is it more character focused? so long as you have a character willing to tutor you. You can learn their language (I.E. I can force my wife to become my tutor and teach me a useless language in my region to make her happy) I would love to know. Thank you

## Reply 301 — participant_210 · 2021-06-18 · post-27626207

This new system seems perfect for cultures like Estonian which was archaeologically indistinguishable from Eastern Scandinavia for centuries because of very strong contacts/connections and having the same way of life like seafaring/raiding/trading etc already since the Bronze Age. Currently just the language defines the "culture group". With the new system, Estonian and Norse would be very similar in most regards with just the language being different. I don't know if this is useful information for anyone but it is highly likely that a large part of Estonians (and people in coastal Finland who had migrated there by sea from Estonia in the Iron Age) spoke Norse as a 2nd language and also many Eastern Scandinavians spoke a Finnic language, most likely some form of Estonian as it was the dominant and most numerous Finnic culture. The archaeological picture being indistinguishable for centuries (without an indication of Scandinavian colonisation/aggression) gives us the impression of this bilingualism.

## Reply 302 — participant_206 · 2021-06-18 · post-27626216

This would probably also change how I play the Khazars or Ethiopian Jews when I go back to them someday. Previously, I would tend to drop Sephardi or Ashkenazi characters as my feudal vassals, while my tribal lands became Khazar. But any character with a different culture from me would quickly assimilate to the local culture. Maybe now, they’ll develop some kind of fusion or melting-pot.

## Reply 303 — participant_211 · 2021-06-18 · post-27626248

Is there a limit on how many languages someone can learn? You could have one language from the father, one from the mother, one from where the character resides in, and one from religious education (such as Latin, Greek, or Arabic). Languages within the same family language should be easier to learn.

## Reply 304 — participant_212 · 2021-06-18 · post-27626331

<!-- artifact:quote:start -->
> Servancour said: There are a number of different modifiers that can increase the baseline. Such as cultures that share the same religion or faith, ethos, or language Click to expand...
<!-- artifact:quote:end -->
What does it mean for a culture to have a religion? Is it based on whatever happens to be the majority religion in that culture? Also, how does forming a hybrid culture affect regnal titles? What is a Turko-Persian emperor called for instance?

## Reply 305 — participant_213 · 2021-06-18 · post-27626334

<!-- artifact:quote:start -->
> DreadLindwyrm said: For "growing up speaking languages", perhaps the child should have a strong chance of learning the language of *both* their parents and their tutor? After all it'd be hard for their tutor to teach them anything if they don't share a language. Perhaps it should even be a requirement that the tutor speaks *a* language in common with the child (and thus presumably their controlling parent) to start with? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Xefjord said: Oh geez, I wish I would have asked this earlier to when the Dev Diary was released, but hopefully I can still get an answer: What determines what languages your ruler can learn? I ask this specifically because I have a roleplay scenario where I play myself married to my girlfriend (who is Taiwanese) so I always just slapped her down with Chinese culture in the middle of the Netherlands with me where my ancestors are from. Is it regionally proximity based? If I can only learn the languages of surrounded regions, does that mean I won't be able to learn my partners language? Or is it more character focused? so long as you have a character willing to tutor you. You can learn their language (I.E. I can force my wife to become my tutor and teach me a useless language in my region to make her happy) I would love to know. Thank you Click to expand...
<!-- artifact:quote:end -->
I think it shouldn't be a guarantee of learning both parents' languages and your guardian. The reason being is that you can send your child to be tutored in another court for their entire childhood. If you do, there's no reason they should necessarily learn the language(s) of their parents. They should definitely learn the language of their guardian, though. Also, if a parent dies early in the childhood, the chance of learning that parent's language should drop based on how long the parent was alive during the childhood. I'd really like a more dynamic way of learning languages and not just automatically learn the languages of your parents and guardian regardless of your situation. Perhaps if a guardian knows the language(s) of the parents in addition to their own language, they can teach the child all of those languages (only those and not additional languages the guardian may know). If the guardian only knows their own language, they cannot teach the parents' language(s) to the child. For the child to learn their parents' language(s) during childhood, they'll need to spend a certain amount of time in their parent's court or their parents' language(s) need to be spoken by a decent number of people in the court where the child is being raised by the guardian. Just throwing out options. The idea being that it would be better to have the way you learn languages vary based on circumstance rather than just getting a "default" set of languages. It could even be a matter of learning a language being similar to experience points - for every year you're with your parents growing up, you get X points toward learning their language. For every year you're with your guardian, you get X points to learn their language. With enough points, you become proficient in the language (i.e. you gain the language). This can be set up so that your first perhaps 2-3 years of life you have no languages. After that, you gain one language and that language is either your parent's language if you're at home the entire time or your guardian's language if you're with them the entire time. If you're at home part of that time and with the guardian part of that time, then it'll be wherever you are at the greatest length of time. In terms of what parent's language to learn if they have different languages, have it be the ruler whose court you are in. After that, you gain "experience" in other languages based on proximity to them over a period of time. Long enough and you learn the language. As an adult, you can also use schemes to learn languages by asking people to teach them to you. It may take multiple schemes for a given language before you gain enough "experience" to learn it. And you might even have events during the scheme (or at the end of it) where you might gain or lose "experience" because of something happening. Even as an adult, you can still learn language through proximity if you gain enough "experience." I believe I read that you can learn languages from specific people and not just your neighbors, so you can invite someone with another language to court and learn from them (perhaps not even having to invite them). I could be wrong in how I remember that, but I'm pretty sure that I saw that.

## Reply 306 — participant_187 · 2021-06-18 · post-27626449

<!-- artifact:quote:start -->
> es333 said: Currently just the language defines the "culture group". Click to expand...
<!-- artifact:quote:end -->
This is not fully true - just look at Basque, Vlach, or the whole Byzantine culture group. Estonians were similar to Finns in more than language, it might even be somewhat anachronistic to have them split in 867 - which does not undermine your point of the important similarities between them and Norse.

## Reply 307 — participant_210 · 2021-06-18 · post-27626869

<!-- artifact:quote:start -->
> Viridianus said: This is not fully true - just look at Basque, Vlach, or the whole Byzantine culture group. Estonians were similar to Finns in more than language, it might even be somewhat anachronistic to have them split in 867 - which does not undermine your point of the important similarities between them and Norse. Click to expand...
<!-- artifact:quote:end -->
There's a saying that fits perfectly here: "The exception proves the rule." In the majority of cases, cultures and culture groups are strongly language oriented in the pre-expansion CK. "Estonians were similar to Finns" sounds quite odd if you know the context. Estonians are proto-Finnics and the expansion of Finnic languages started from Northern-Estonia. In the CK time frame, Iron Age Estonian seafarers had settled southern and south-western Finland, while most of Finland was still Sami. The Estonians outnumbered the (Finnic/Estonian) Finns by about 5 times. Finns being a separate "culture" in the game is more based on the situation in 2020 than the actual reality in the 9th century. It can be a separate culture and it could be a part of Estonian, I don't mind either way, both are kind of correct in a way. The point is that most of Estonia and southern & south-western Finland were all an integral part of the Norse world. Similarities between Estonians/Finns aren't even important here because as I said, Finland had recently been settled by Iron Age Estonian seafarers. In the CK time frame, Finns weren't notably different from the dominant Finnic culture, the Estonians, yet. The population of Finnic Finns (excluding Sami inhabitants of Finland) in the 9th century was most likely no more than 10 000. For comparison, the population of entire modern-day Finland (including the Sami) in 1100AD was about ~30 000. That's why we know a lot about Estonians being vikings and raiders for many centuries even before the Viking age as they were quite numerous (about 100K people in the late Viking age) but the Finns aren't really known for it because they were a very small group back then (but they were seafarers and had the same way of life as the Estonians and the Scandinavians) and the migration wave from Estonia to Finland lasted until the 13th century.

## Reply 308 — participant_187 · 2021-06-18 · post-27626908

<!-- artifact:quote:start -->
> es333 said: Finns being a separate "culture" in the game is more based on the situation in 2020 than the actual reality in the 9th century. It can be a separate culture and it could be a part of Estonian, I don't mind either way, both are kind of correct in a way. Click to expand...
<!-- artifact:quote:end -->
Well, yeah, that's what I was leading to - except I am not certain it would be reasonable to call the barely-split proto-Finnic culture "Estonian", as you do. I would more readily use "Estonian" for Seto (who definitely were split by that time) and "Finnish" for the Finnish-Estonian.

## Reply 309 — participant_210 · 2021-06-18 · post-27627155

<!-- artifact:quote:start -->
> Viridianus said: Well, yeah, that's what I was leading to - except I am not certain it would be reasonable to call the barely-split proto-Finnic culture "Estonian", as you do. I would more readily use "Estonian" for Seto (who definitely were split by that time) and "Finnish" for the Finnish-Estonian. Click to expand...
<!-- artifact:quote:end -->
lol what? 1. proto-Finnic arose in Estonia and spread out of Estonia in several waves. Of course they were not "Estonian", there were different tribes but they were just from the geographical area of Estonia in the same way that Proto-Germanics are Scandinavian. 2. The Seto are definitely not a good example of "Estonian". They're outliers in many ways as they were geographically (impassable bogs & forests) from Estonian tribes since the Bronze Age, this geographical separation still shows in their genes. The "Seto" were more similar (and had connections) to Finnic people living east of lake Peipus than to Estonians. Saying that the Seto are a good example of Estonians is like saying that Karelians are a good example of Finns but the Seto are just even more different.

## Reply 310 — participant_214 · 2021-06-18 · post-27627323

<!-- artifact:quote:start -->
> SauronGorthaur said: Onto the things I dislike then. First of all, I already mentioned in both previous two dev diaries for the Royal Court is that, as much as like what I'm seeing, I don't see how the amount of content it's going to have justifies the 50% price of the DLC compared to DLCs of previous PDX titles, even big ones like Emperor (which still cost 20 dollars unlike the 30 for CKIII's DLCs). Or, more specifically, how it fulfills the criteria of Paradox's own justification of the price increase. And that was when the only piece of the announced content that was specified to be a part of the free patch was the return of the minor titles. Now it's been confirmed that the big culture overhaul is going to be free content too. And sure, we will still have cultural divergence and hybridization in the DLC. But those are only going us to allow to swap the building blocks of the new culture system around. The mean of the new culture system is going to be a part of the free patch, while divergence and hybridization are just the sauce. Side dish at best. And contrary to what certain ivory aficionados of the gallant persuasion tried to push as the truth in response to this being pointed out, the aforementioned justification for the price increase of the DLCs by Paradox itself clearly stated that it's because of the increased size of the DLC content itself. With no mention of the free patch content playing into that as well. Even though in that very same post about the new pricing structure for CKIII, just one paragraph earlier no less, Paradox itself made a clear delineation between DLCs (further separated between flavor packs and major expansions) and free patches. Besides, the free patch is quite telling here. The free patch content simply cannot justify the price increase of the DLCs (even if it's the free patch accompanying that exact DLC), because at that point it ceases to be truly free. Don't get me wrong, it's not like I'm against free patch content. Just the opposite. Given how Paradox works, DLC content is rarely ever updated in later DLCs or linked to their own systems, no matter how much it'd make sense for them to be linked. But free content can be further updated by DLCs because, well, it's free. But that's beside the point here. Paradox promised the 50% DLC price hike will be justified by increase in content and the DLC content just shrunk significantly thanks to this confirmation. And I was willing to give Paradox the benefit of the doubt here, thinking that there will be hefty amount of artwork to go with the new mechanics. But third Royal Court dev diary in a row they themselves dispelled the validity of giving them that benefit. First they announced that they will be creating just four visual styles for the courts (corresponding to the four general areas that start as feudal/clan, despite the fact that all other areas are supposed to turn feudal/clan anyway), even though we are still months away from the release which would give them ample time to create the necessary artwork. And now they confirmed the whole shtick with culture aesthetic is not going to translate to anything in regards to holding graphics. Moving on to something I also already addressed in reply to the previous Royal Court dev diary, i.e. cultural ethea. Particularly with how they correlate to the topic of the previous dev diary, i.e. court types. The issue here is that the court type is, by the sounds of it, going to be a pretty important decision. Except thanks to how it interacts with ethea, it's a heavily limited choice. And like I said in the previous diary, in general choice is good for games. But not when done like this. There are seven ethea and five court types, with each ethos giving access to multiple court types. But not all of them. My guess is two or maybe three at best. The problem here is that the ethos of your culture is locked into place from the get go. So let's say you want to play as a Swedish character because that time you decided to try surströmming made you develop Stockholm syndrome towards the Swedish culture. Giving Paradox's penchant for nationalistic chest-thumping and memes, I'm going to guess that the ethos of Swedish culture is going to be bellicose because vikings. Which, in turn, is probably going to give you access to martial and intrigue courts. Now, what happens if you want to have a stewardship court instead? You're simply out of luck. In both this and the previous dev diary Paradox explicitly stated that your only choice to change the ethos of your culture is to use either cultural divergence or hybridization. Which means creating a culture that's explicitly not Swedish. Completely defeating the point of wanting to play as a specifically Swedish character in the first place. As such, if you want to remain Swedish it means your choice is limited in the aforementioned bad way. Click to expand...
<!-- artifact:quote:end -->
I pretty much agree with your statement about the ethos/court style interaction. It feels wrong not being able to have a certain kind of court because your culture doesn't allow it. If your character is into stewardship, he should be able to create a steward court. His individuality should be more important than the preferences of his cultural background. Especially in a role playing game where you play as individual characters as opposed to playing a vague blob on a map. But I have a different perspective on the monetisation issue. Does it look like the amount of paid content is going to be underwhelming for a 30$ expansion when you compare it to a 20$ expansion of CK2 at the moment? Yes, a bit. But my payment of 30$ funded the culture overhaul anyways, regardless if it's released for free or not. It would not exist were it not for us paying for the expansion pass/DLCs. My attitude to this resembles that of a patron. I like the concept of this game so much that I want to give Paradox money so they can create and improve this game so I can enjoy playing it. But yeah, maybe this is a strange attitude. And I wouldn't have this attitude for any game, only those which are uniquely interesting in my eyes.

## Reply 311 — participant_187 · 2021-06-18 · post-27627350

<!-- artifact:quote:start -->
> es333 said: lol what? 1. proto-Finnic arose in Estonia and spread out of Estonia in several waves. Of course they were not "Estonian", there were different tribes but they were just from the geographical area of Estonia in the same way that Proto-Germanics are Scandinavian. 2. The Seto are definitely not a good example of "Estonian". They're outliers in many ways as they were geographically (impassable bogs & forests) from Estonian tribes since the Bronze Age, this geographical separation still shows in their genes. The "Seto" were more similar (and had connections) to Finnic people living east of lake Peipus than to Estonians. Saying that the Seto are a good example of Estonians is like saying that Karelians are a good example of Finns but the Seto are just even more different. Click to expand...
<!-- artifact:quote:end -->
I like to re-use names from vanilla to signify the distinctions that actually make sense. So... 1. So? Calling proto-Finnic Estonians because they happened to frequent Estonia before they frequented Finland is like calling proto-Italic people something other than Italic because they obviously originated north of Alps. Using the vanilla Finnish for both vanilla Finnish and vanilla Estonian is likewise more fitting. 2. Yes! Seto were, by linguistic data, the first to split from the proto-Finnic branch, before all the Karelian/Finnish/Estonian split. They are not a good example of present-day Estonians, but they are good place to put the distinction and actually re-use the "Estonian" label freed by point 1.

## Reply 312 — participant_108 · 2021-06-18 · post-27627435

<!-- artifact:quote:start -->
> Riamus said: I think it shouldn't be a guarantee of learning both parents' languages and your guardian. The reason being is that you can send your child to be tutored in another court for their entire childhood. If you do, there's no reason they should necessarily learn the language(s) of their parents. They should definitely learn the language of their guardian, though. Also, if a parent dies early in the childhood, the chance of learning that parent's language should drop based on how long the parent was alive during the childhood. I'd really like a more dynamic way of learning languages and not just automatically learn the languages of your parents and guardian regardless of your situation. Perhaps if a guardian knows the language(s) of the parents in addition to their own language, they can teach the child all of those languages (only those and not additional languages the guardian may know). If the guardian only knows their own language, they cannot teach the parents' language(s) to the child. For the child to learn their parents' language(s) during childhood, they'll need to spend a certain amount of time in their parent's court or their parents' language(s) need to be spoken by a decent number of people in the court where the child is being raised by the guardian. Just throwing out options. The idea being that it would be better to have the way you learn languages vary based on circumstance rather than just getting a "default" set of languages. It could even be a matter of learning a language being similar to experience points - for every year you're with your parents growing up, you get X points toward learning their language. For every year you're with your guardian, you get X points to learn their language. With enough points, you become proficient in the language (i.e. you gain the language). This can be set up so that your first perhaps 2-3 years of life you have no languages. After that, you gain one language and that language is either your parent's language if you're at home the entire time or your guardian's language if you're with them the entire time. If you're at home part of that time and with the guardian part of that time, then it'll be wherever you are at the greatest length of time. In terms of what parent's language to learn if they have different languages, have it be the ruler whose court you are in. After that, you gain "experience" in other languages based on proximity to them over a period of time. Long enough and you learn the language. As an adult, you can also use schemes to learn languages by asking people to teach them to you. It may take multiple schemes for a given language before you gain enough "experience" to learn it. And you might even have events during the scheme (or at the end of it) where you might gain or lose "experience" because of something happening. Even as an adult, you can still learn language through proximity if you gain enough "experience." I believe I read that you can learn languages from specific people and not just your neighbors, so you can invite someone with another language to court and learn from them (perhaps not even having to invite them). I could be wrong in how I remember that, but I'm pretty sure that I saw that. Click to expand...
<!-- artifact:quote:end -->
I'm broadly along side that. I was thinking that usually you'd learn the primary language of your dominant parent as you age up to about 6, before being sent to your tutor and *possibly* picking up their language (and they need to be able to speak your language to even be able to tutor you... after all, if you've grown up in a court that only speaks Norse, and you're sent to a tutor who speaks Italian, your tutoring won't be that effective...). However if, as is reasonably usual for my playthroughs the tutor is in the court of the ruler-parent (or is the ruler parent), then learning the non-dominant parent's language if different could be a possibility. But yeah, your expansion of the concept makes sense, even if it's a little more complicated than I was thinking.

## Reply 313 — participant_059 · 2021-06-18 · post-27627913

@Servancour Would it be possible through modding to have a Tradition unlock a Court Type? Also small suggestion taken from the Victoria III DD, it would be nice to have one or two reserved posts under the DD to centralise your answers to questions rather than to have them dispersed all across the thread. Thank you!

## Reply 314 — participant_215 · 2021-06-18 · post-27627920

<!-- artifact:quote:start -->
> Koyraboro said: @Servancour Would it be possible through modding to have a Tradition unlock a Court Type? Also small suggestion taken from the Victoria III DD, it would be nice to have one or two reserved posts under the DD to centralise your answers to questions rather than to have them dispersed all across the thread. Thank you! Click to expand...
<!-- artifact:quote:end -->
It sometimes takes a while, but answers in DD comments are usually added to the FAQ post. This is the one for the Royal Court : https://forum.paradoxplaza.com/foru...er-diaries-q-a-important-information.1475394/

## Reply 315 — participant_208 · 2021-06-18 · post-27628360

<!-- artifact:quote:start -->
> MirrorMonkey2 said: I pretty much agree with your statement about the ethos/court style interaction. It feels wrong not being able to have a certain kind of court because your culture doesn't allow it. If your character is into stewardship, he should be able to create a steward court. His individuality should be more important than the preferences of his cultural background. Especially in a role playing game where you play as individual characters as opposed to playing a vague blob on a map. But I have a different perspective on the monetisation issue. Does it look like the amount of paid content is going to be underwhelming for a 30$ expansion when you compare it to a 20$ expansion of CK2 at the moment? Yes, a bit. But my payment of 30$ funded the culture overhaul anyways, regardless if it's released for free or not. It would not exist were it not for us paying for the expansion pass/DLCs. My attitude to this resembles that of a patron. I like the concept of this game so much that I want to give Paradox money so they can create and improve this game so I can enjoy playing it. But yeah, maybe this is a strange attitude. And I wouldn't have this attitude for any game, only those which are uniquely interesting in my eyes. Click to expand...
<!-- artifact:quote:end -->
Yes, of course the free patch content isn't charity work. But there is quite a significant difference, at least to me, between "free patch content gets funded by the DLCs" (which I have no problems with) and "the 50% increase in DLC price is justified by the free patch content". Especially since there are multiple significant problems with the latter. As I already pointed out, that runs contrary to Paradox's own statements on the issue. According to them the price increase is (or at least is supposed to be) justified by the increased scope of the expansion content itself. It's not like CKIII is the first game where PDX started releasing free patch content alongside (and sometimes even between) DLCs. Holy Fury, Emperor and Leviathan, despite being significantly larger DLCs than their contemporaries still cost the same and still had free patch content. Royal Court isn't even going to have an unusual amount of free patch content. Right now the stated free patch content is the culture overhaul and minor titles. Just two things. And while the culture overhaul is a pretty hefty change, so were other pieces of free content in the past, like the revamp of crusades in the free patch accompanying Holy Fury. Not to mention some of the map changes for their past titles, which were always part of the free patch.

## Reply 316 — participant_210 · 2021-06-19 · post-27628476

<!-- artifact:quote:start -->
> Viridianus said: I like to re-use names from vanilla to signify the distinctions that actually make sense. So... 1. So? Calling proto-Finnic Estonians because they happened to frequent Estonia before they frequented Finland is like calling proto-Italic people something other than Italic because they obviously originated north of Alps. Using the vanilla Finnish for both vanilla Finnish and vanilla Estonian is likewise more fitting. 2. Yes! Seto were, by linguistic data, the first to split from the proto-Finnic branch, before all the Karelian/Finnish/Estonian split. They are not a good example of present-day Estonians, but they are good place to put the distinction and actually re-use the "Estonian" label freed by point 1. Click to expand...
<!-- artifact:quote:end -->
You have some very radical and alternative views, I can tell you that. Germanics didn't originate in Germany just because they're called "Germanic". In the same sense, Finnics did not originate from Finland just because they're called "Finnic". Germanics arose in Southern-Scandinavia. Finnics arose in Northern-Estonia from where they expanded in all directions, reaching as far west as central Scandinavia and as far north as Finland. Calling the Estonians "Finnish" in CK start dates would make as much sense as calling the Norse culture, "Icelandic". Both Finnish and Icelandic are very small numbered and rather insignificant cultures compared to the dominant North-Germanic culture, Norse and dominant Finnic culture which was Estonian. I mean, this discussion doesn't really seem to have a point as you cannot grasp even the basics of population movements and ethnic history of Northern-Europe while I studied it in university. I recommend reading about Finnic cultures if you're trying to be serious here. I legit think that you might be trolling us here if you say that the "Estonian" culture should be located around Pskov while the actual Estonian culture in Estonia should be called "Finnish". I'm just done.

## Reply 317 — participant_014 · 2021-06-19 · post-27628485

<!-- artifact:quote:start -->
> Viridianus said: I like to re-use names from vanilla to signify the distinctions that actually make sense. So... 1. So? Calling proto-Finnic Estonians because they happened to frequent Estonia before they frequented Finland is like calling proto-Italic people something other than Italic because they obviously originated north of Alps. Using the vanilla Finnish for both vanilla Finnish and vanilla Estonian is likewise more fitting. 2. Yes! Seto were, by linguistic data, the first to split from the proto-Finnic branch, before all the Karelian/Finnish/Estonian split. They are not a good example of present-day Estonians, but they are good place to put the distinction and actually re-use the "Estonian" label freed by point 1. Click to expand...
<!-- artifact:quote:end -->
There's an easy solution to this: in the 867 start, make the cultures Seto and Proto-Finnic, with options for Proto-Finnic characters to become Estonian or Finnish based on where they live and other modifiers over time. I'm not knowledgeable to know how groups like the Livonians come into play here, but presumably they can be involved too At least according to Wikipedia, Karelians weren't viewed as separate before the 1000s, and Estonians before the 1100s. No idea how accurate this is, but presumably that's around when this split could occur, I suppose

## Reply 318 — participant_216 · 2021-06-19 · post-27628620

<!-- artifact:quote:start -->
> Servancour said: This is also the pillar that contains what naming practices the culture uses. Mainly what character names to use, if they use a dynasty prefix, etc. The naming practice will also be used to change title and holding names, which used to be set per culture, so as to not have titles change names if you create a new culture. Click to expand...
<!-- artifact:quote:end -->
Wouldn't this fit Language rather than Aesthetics? edit: nevermind, it was replied in the thread and detailed in the 65th dev diary.

## Reply 319 — participant_187 · 2021-06-19 · post-27628736

<!-- artifact:quote:start -->
> es333 said: I mean, this discussion doesn't really seem to have a point as you cannot grasp even the basics of population movements and ethnic history of Northern-Europe while I studied it in university. Click to expand...
<!-- artifact:quote:end -->
I have grasped it, as we do not have a single factual disagreement. As far as I can see, we both agree on the following scenario of what actually happened. There was a Pan-Proto-Finnic group (itself probably deriving from an earlier split with Sami), living around modern-day Estonia. Then Seto split (their being first is robustly confirmed by linguistic data). Then the rest started colonizing nearby areas such as Karelia and Finland. The only disagreement we do have is whether to call this remaining group (ancestral to Finns, modern-day Estonians, and Karelians) "Estonian" in-game - and, aside from their being in Estonia (which is not enough as I indicated by the Italic example and you support by the well-known Germanic example - again, judging by that, we both know that's a non-argument), there is no particular reason to call them that.

## Reply 320 — participant_213 · 2021-06-19 · post-27628742

<!-- artifact:quote:start -->
> DreadLindwyrm said: I'm broadly along side that. I was thinking that usually you'd learn the primary language of your dominant parent as you age up to about 6, before being sent to your tutor and *possibly* picking up their language (and they need to be able to speak your language to even be able to tutor you... after all, if you've grown up in a court that only speaks Norse, and you're sent to a tutor who speaks Italian, your tutoring won't be that effective...). However if, as is reasonably usual for my playthroughs the tutor is in the court of the ruler-parent (or is the ruler parent), then learning the non-dominant parent's language if different could be a possibility. But yeah, your expansion of the concept makes sense, even if it's a little more complicated than I was thinking. Click to expand...
<!-- artifact:quote:end -->
Yeah, basically where I was going. My thinking though is that sometimes a child has a guardian set up right away rather than at 6. But I'm actually not certain if they leave immediately or wait until 6 before they leave if the guardian is in another court. I'd have to test that (or someone else can if they want). If the child remains in the parent's court until 6, then absolutely they should always learn the parent's language. If they can leave the court right away, then they wouldn't necessarily learn the parent's language if they spend their entire childhood in a different court.

## Reply 321 — participant_210 · 2021-06-19 · post-27629022

<!-- artifact:quote:start -->
> Viridianus said: I have grasped it, as we do not have a single factual disagreement. As far as I can see, we both agree on the following scenario of what actually happened. There was a Pan-Proto-Finnic group (itself probably deriving from an earlier split with Sami), living around modern-day Estonia. Then Seto split (their being first is robustly confirmed by linguistic data). Then the rest started colonizing nearby areas such as Karelia and Finland. The only disagreement we do have is whether to call this remaining group (ancestral to Finns, modern-day Estonians, and Karelians) "Estonian" in-game - and, aside from their being in Estonia (which is not enough as I indicated by the Italic example and you support by the well-known Germanic example - again, judging by that, we both know that's a non-argument), there is no particular reason to call them that. Click to expand...
<!-- artifact:quote:end -->
Finnic didn't split from Sami, they're rather distantly related and the Sami had lived in Scandinavia for thousands of years before the first proto-Finnics arrived to Finland by sea from the proto-Finnic homeland of Estonia. The small amount of shared vocabulary and similarities between Sami & Finnic is a result of contacts starting in the late Bronze Age. The timeline and history of those 2 groups is so different that the last time that they spoke the same language was some form of Western Uralic around the Volga river region at the very early stages of the Uralic language family. By CK start dates, Finnic seafarers from Estonia had settled just the southern and south-western coast of Finland and they were still the minority group in Finland as the Sami still inhabited most of Finland. As I said, if you think that every Finnic person at that point should be called "Finnish", then we should rename Norse to "Icelandic". Estonian, Veps, Finnish etc are good enough names/splits for the different subgroups. Map (by Marika Mägi) of the 9th century ethnic situation:

## Reply 322 — participant_187 · 2021-06-19 · post-27629117

<!-- artifact:quote:start -->
> es333 said: Finnic didn't split from Sami, they're rather distantly related and the Sami had lived in Scandinavia for thousands of years before the first proto-Finnics arrived to Finland by sea from the proto-Finnic homeland of Estonia. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> es333 said: As I said, if you think that every Finnic person at that point should be called "Finnish", then we should rename Norse to "Icelandic". Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> es333 said: Estonian, Veps, Finnish etc are good enough names/splits for the different subgroups. Click to expand...
<!-- artifact:quote:end -->
1)You're nitpicking a side point which does not in any way affect the main claim I made (namely, that we perceive the map identically - more or less akin to the picture you show - and only debate around the name). 2)In this point, however, we do have an additional disagreement previously unseen - namely, on the validity of Finno-Samic hypothesis (wikilink for potential readers). I think that Finnish, Karelian and Estonian are all anachronistic misnomers (they probably called themselves something like Maarahva) but, if choosing among the misnomers the vanilla game suggests, Finnish is less of an offence than Estonian - because we could re-use Estonian for a group that actually was separate by that time. And yes, if the devs weren't themselves Swedish, Norse would probably be called Icelandic (just like we have Turkish and Bosnian and Portuguese and what-not), and you know what? It would be OK. Not great, but OK. It is anachronistic to split them though. At least at the level of granularity most cultures have.

## Reply 323 — participant_133 · 2021-06-19 · post-27630037

<!-- artifact:quote:start -->
> Tiax said: It feels like from a gameplay perspective, the "optimal" answer would be to still convert (maybe avoiding some very low development provinces). After all, even if you have perfect acceptance now, that could all change with a few wars, and then it'd be a disaster. It feels like, despite all these nifty toys to play with, the game heavily incentivizes cultural homogenizing. Culture-converting provinces is cheap, quick, and low risk. Not culture-converting is a dangerous game that will eventually come back to bite the AI (a competent human can get away with just about anything). The same problem exists with religion - we have lots of unique local religions in the first few years, and they all get obliterated because there's no downside or expense or difficulty to doing so. I'm concerned the same will happen with cultures, and a lot of this cool work will go to waste. Click to expand...
<!-- artifact:quote:end -->
I mean if the AI ruler is encountering problems relating to political stability from a culture that is outraged at the actions of the ruling culture, I don't really see a problem. I'm sure there have been many times throughout history where two different communities live in relative peace, until something happens that divides them deeply(war, injustice, persecution, change of leadership) etc. Honestly it makes the game more fun if certain circumstances(the cultural acceptance mechanic) can change the stability of a realm, it's pretty much emergent gameplay which I think is a good thing for CK3's replayability. CK3 should have more disasters imo if we want to make the game more challenging or even less predictable.

## Reply 324 — participant_108 · 2021-06-20 · post-27630252

<!-- artifact:quote:start -->
> Ryeboy98 said: I mean if the AI ruler is encountering problems relating to political stability from a culture that is outraged at the actions of the ruling culture, I don't really see a problem. I'm sure there have been many times throughout history where two different communities live in relative peace, until something happens that divides them deeply(war, injustice, persecution, change of leadership) etc. Honestly it makes the game more fun if certain circumstances(the cultural acceptance mechanic) can change the stability of a realm, it's pretty much emergent gameplay which I think is a good thing for CK3's replayability. CK3 should have more disasters imo if we want to make the game more challenging or even less predictable. Click to expand...
<!-- artifact:quote:end -->
I can potentially see problems where Ruler A, with a population split between cultures 1 and 2 has their realm get into some severe trouble because Ruler B (with culture 1) and Ruler C (with culture 2) have ended up in an extended series of wars, even though Ruler A has a more of both cultures in his realm than either B or C. Say for example Ruler A is Emperor of Francia, but for whatever reason there is a small pool of French and Occitan land that is not under his control, and the rulers of those areas are at war. Depending on how the weighting for the cultures being at peace in the larger realm against the smaller realms being at war is handled, it could make a really, really, big difference.

## Reply 325 — participant_217 · 2021-06-20 · post-27630727

I want this content as soon as possible !!

## Reply 326 — participant_218 · 2021-06-20 · post-27631404

I hoped so much to see dynamic cultures like this when CK3 was released, and was so disappointed they were as static as CK2! This is what'll make me finally upgrade from CK2 to CK3

## Reply 327 — participant_059 · 2021-06-20 · post-27631692

Can we condition some Traditions to (not) having one or multiple Pillars?

## Reply 328 — participant_219 · 2021-06-21 · post-27631760

<!-- artifact:quote:start -->
> Ryeboy98 said: CK3 should have more disasters imo if we want to make the game more challenging Click to expand...
<!-- artifact:quote:end -->
Paradox games tend to sit at a spot on the curve where changes that might ostensibly make the game mechanically harder frequently end up making the single-player game practically easier.

## Reply 329 — participant_191 · 2021-06-21 · post-27632978

@Servancour have you considered adding Mercantile ethos? It seems really obvious for some cultures (Flemish, Yemeni...) and it's strange how there is no ethos for earning money.

## Reply 330 — participant_014 · 2021-06-21 · post-27633250

<!-- artifact:quote:start -->
> Krajzen said: @Servancour have you considered adding Mercantile ethos? It seems really obvious for some cultures (Flemish, Yemeni...) and it's strange how there is no ethos for earning money. Click to expand...
<!-- artifact:quote:end -->
i think its more of a tradition type deal

## Reply 331 — participant_220 · 2021-06-21 · post-27633751

So I have a question about the expansion I haven't seen yet. Can we re-name titles? Like, say I'm playing as the Coptic King of Egypt, can I re-name the title of Malik of Egypt to Pharaoh of Egypt?

## Reply 332 — participant_014 · 2021-06-22 · post-27633961

<!-- artifact:quote:start -->
> Jon the Wizard said: So I have a question about the expansion I haven't seen yet. Can we re-name titles? Like, say I'm playing as the Coptic King of Egypt, can I re-name the title of Malik of Egypt to Pharaoh of Egypt? Click to expand...
<!-- artifact:quote:end -->
well copts aren't a culture in CK3 atm, but if they were, they'd prob have a coptic aesthetic and titles, no?

## Reply 333 — participant_108 · 2021-06-22 · post-27634093

<!-- artifact:quote:start -->
> Jon the Wizard said: So I have a question about the expansion I haven't seen yet. Can we re-name titles? Like, say I'm playing as the Coptic King of Egypt, can I re-name the title of Malik of Egypt to Pharaoh of Egypt? Click to expand...
<!-- artifact:quote:end -->
It'd be nice to have that option. Same as on the religious front being able to rename priest titles and the God/High God/Evil God slots.

## Reply 334 — participant_221 · 2021-06-22 · post-27634223

<!-- artifact:quote:start -->
> Servancour said: Answer to the question: "1. Will having a male only Martial culture prevent the AI from picking martial education for girls? I really think it should." by TheMongoose. 1. As far as I know, it won't affect the AI for picking education. Might be something to consider though, but I would never want to block it completely. Click to expand...
<!-- artifact:quote:end -->
As martial education is a real education and not just "I picked it up while I watched the knights fight" thing (that can be represented by martial skill points and prowess) it should be picked rarely by the AI. It would be nice if characters from a man/woman only warrior culture would have an opinion penalty of the "incorrect" gender having a martial education. (We are okay with this woman being of a different culture. As long as she does the things like they are meant to be done {it est like we do}).

## Reply 335 — participant_220 · 2021-06-22 · post-27634259

<!-- artifact:quote:start -->
> peaswar said: well copts aren't a culture in CK3 atm, but if they were, they'd prob have a coptic aesthetic and titles, no? Click to expand...
<!-- artifact:quote:end -->
No, the culture I'm part of is Egyptian. I thought it'd be apropos to be the Pharaoh of Egypt as opposed to the likely more correct title of Malik.

## Reply 336 — participant_222 · 2021-06-22 · post-27635754

<!-- artifact:quote:start -->
> sreckom92 said: Looks great! Anything about cultures that fade into obscurity? I mean, in this game you can rule over a certain culture and that culture will eventually disappear. It is assimilated into your own. Can there be a way for cultures to emerge from this obscurity? Maybe a way to never have them fully disappear, but rather be somehow present (via hidden modifiers) on the map? These cultures would still spawn their own characters and could emerge and be dominant in certain provinces, if some conditions are met. Click to expand...
<!-- artifact:quote:end -->
This sort of thing would only ever make sense with a POP mechanic. I've wanted something similar for religion so there's a distinction between "51% of this county's people are Orthodox" and "99.9% of this county's people are Orthodox", and was disappointed when it didn't happen. Probably won't

## Reply 337 — participant_223 · 2021-06-23 · post-27636526

<!-- artifact:quote:start -->
> cristofolmc said: Please PLEASE do not make the mistake of thinking that the basque nobility spoke basque when they spoke indeed castillian. Dont break the game balance adding issues that didn't exist in the past based on today's prejudices of the modern era. BAsque until recently in history wasn't spoken except by rural folk in the Basque mountains. Same as with the anglo saxon's being inventive. Anglo saxon in the middle ages were anything but invented and their lands certainly didnt have an exceptional development superior to the rest. PLEASE don't develop the game based on modern times stereotypes and recent history. Click to expand...
<!-- artifact:quote:end -->
I'm not really sure if I can believe you since Francoist suppression of the Basque langauge is well known, and it indeed had a modern revival in response to that suppression, but I don't know if you mean the state of the Basque language post-Franco as how it's always been or if it was previously like that.

## Reply 338 — participant_216 · 2021-06-23 · post-27636797

<!-- artifact:quote:start -->
> PatrykCXXVIII said: What about Slavic languages? AFAIK back then they weren't that different from each other and their more noticeable split happened later than in some other language groups, hence projects like interslavic or neoslavonic languages that are mostly understood by every Slav without studying it today. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Fulbert said: So only seafarer cultures can navigate rivers, huh? Shouldn't it be the other way? I'm not a sailor myself so correct me if I'm wrong but shouldn't sailing down Volga be easier than braving the high seas? Wouldn't it make more sense if all cultures were able to navigate rivers but only the seafarers could sail the seas without severe penalties? I mean, it's right there in the name. Click to expand...
<!-- artifact:quote:end -->
It would be best to have three Slavic languages: "East Slavic", "South Slavic" and "West Slavic". Agreed.

## Reply 339 — participant_224 · 2021-06-23 · post-27637084

I don't know if it's been answered already since there are 17 pages in this thread but will cultural acceptance affect culture conversion? You know, for those of us who still do want to create somewhat monocultural realms.

## Reply 340 — participant_187 · 2021-06-23 · post-27637299

<!-- artifact:quote:start -->
> SMiki Lorebringer said: It would be best to have three Slavic languages: "East Slavic", "South Slavic" and "West Slavic". Click to expand...
<!-- artifact:quote:end -->
Not really, for two reasons. 1. West, East and South language groups are each later consolidations of at least two other groups which do not have a prior relatedness beyond being Slavic (Polish-Kashubian and Czech-Slovak; Old Pskov-Novgorod and "mainland" Old East Slavic; Serbian, Croatian, and Bulgarian - respectively); 2. Slavs did not generally use or require a translator till as late as XVI century, more-or-less freely conversing in their languages. If we have all Romance languages use Latin, we cannot pretend Slavs are more diverse.

## Reply 341 — participant_216 · 2021-06-23 · post-27638544

<!-- artifact:quote:start -->
> Viridianus said: If we have all Romance languages use Latin … Click to expand...
<!-- artifact:quote:end -->
Was this confirmed at any point?

## Reply 342 — participant_225 · 2021-06-24 · post-27639046

<!-- artifact:quote:start -->
> Matihood1 said: I don't know if it's been answered already since there are 17 pages in this thread but will cultural acceptance affect culture conversion? You know, for those of us who still do want to create somewhat monocultural realms. Click to expand...
<!-- artifact:quote:end -->
Cultural acceptance does affect the prestige cost of culture hybridization. I don't think this answers your question about conversion.

## Reply 343 — participant_062 · 2021-06-24 · post-27639657

<!-- artifact:quote:start -->
> SMiki Lorebringer said: Was this confirmed at any point? Click to expand...
<!-- artifact:quote:end -->
Not explicitly, but it's to be inferred from the confirmed fact that Vlach culture uses 'Latin' language. Were it after me, I'd instead propose for Romance languages to be divided into: - Balkanic Latin (Vlach)* - Italic Latin (Italian, Lombard, Sicilian and possibly Sardinian as to not have the latter in a category of its own) - Gallic Latin (Cisalpine, French, Norman, Occitan, Catalan) - Iberic Latin (Aragonese, Asturleonese, Castilian, Galician, Portuguese) Naturally, some better terminology could be thought up as to avoid hyphenated names or two word constructs with adjectives. *Although I'd also propose for Dalmatian to be added, as well as a distinct Romanian culture representing the divergent culture of the North Danubian Vlachs (ergo Vlach culture is of Byzantine heritage and is present on both sides of the Danube as an abstraction for the undifferentiated ethnolinguistic identity which was shared among the Latin-speaking ancestors of today's Romanians and Aromanians; Romanian culture is of South Slavic heritage and forms in de jure Wallachia and Moldavia as a melting pot culture while the Aromanians of the Balkans remain as Vlach).

## Reply 344 — participant_062 · 2021-06-25 · post-27642856

<!-- artifact:quote:start -->
> Dynastic rule is hard to ascribe, given the loose traditional definition of the ruling family (on principle, princes were chosen from any branch, including a previous ruler's bastard sons – being defined as os de domn – "of domn marrow", or as having hereghie – "heredity" (from the Latin hereditas); the institutions charged with the election, dominated by the boyars, had fluctuating degrees of influence). The system itself was challenged by usurpers, and became obsolete with the Phanariote epoch. Click to expand...
<!-- artifact:quote:end -->
On a different note, Vlach culture should have a form of elective monarchy as one of its possible traditions. List of monarchs of Moldavia - Wikipedia en.wikipedia.org List of princes of Wallachia - Wikipedia en.wikipedia.org Vlach elective could be defined as: The Ruler and all direct De Jure Vassals of one or two Ranks below the Title can nominate an Heir from amongst the Ruler's Extended Family and any available Claimants.

## Reply 345 — participant_207 · 2021-06-25 · post-27643035

<!-- artifact:quote:start -->
> Hospodar said: On a different note, Vlach culture should have a form of elective monarchy as one of its possible traditions. List of monarchs of Moldavia - Wikipedia en.wikipedia.org List of princes of Wallachia - Wikipedia en.wikipedia.org Vlach elective could be defined as: The Ruler and all direct De Jure Vassals of one or two Ranks below the Title can nominate an Heir from amongst the Ruler's Extended Family and any available Claimants. Click to expand...
<!-- artifact:quote:end -->
I wouldn't trust those articles too much. The text in question was added in identical copies to those two articles around 15 years ago, and in all this time not a single source has been given. That's not to say the claims are not correct, but they lack evidence. It could have been made up and added by you, me, or Moon Boy for all we know.

## Reply 346 — participant_062 · 2021-06-25 · post-27643057

<!-- artifact:quote:start -->
> Karlington said: I wouldn't trust those articles too much. The text in question was added in identical copies to those two articles around 15 years ago, and in all this time not a single source has been given. That's not to say the claims are not correct, but they lack evidence. It could have been made up and added by you, me, or Moon Boy for all we know. Click to expand...
<!-- artifact:quote:end -->
I could look up some Romanian academic sources and translate the appropriate passages if so desired. That said, the succession to both the Wallachian and Moldavian thrones of various rulers is not a matter of contention, so the elective character of it can be simply inferred.

## Reply 347 — participant_062 · 2021-06-25 · post-27643086

Better yet, I've found a professional English translation of a book written by one of the leading contemporary historians of Romania (whose works tend to annoy Romanian nationalists and other mystifiers of history no less). Here you go, @Karlington: "The unfortunate system of succession to the throne (or rather the lack of any real system) came as a supplementary handicap. The succession was neither hereditary nor simply elective but a mixture of the two: hereditary in principle, with two dynasties (Basarab in Wallachia and Musatin in Moldavia), but without the Western criterion of transmission of the throne in the direct line. Not only sons but also brothers or more distant relatives could aspire to princedom (women were excluded from the start). The only condition was to be ‘princely bone’, to belong to the family. At first, selection worked within reasonable limits. In time, however, the pretenders multiplied. Even illegitimate sons succeeded to the throne, and, in these conditions, there were of course men who only pretended to be sons of a prince. (Such was the case with Michael the Brave, the most renowned of all of the Romanian voivodes, who declared himself to be the posthumous son of the voivode Petrascu the Good; modern historians seem less than convinced of this relationship, which would in any case be impossible to prove.) In time, very distant relatives appeared who were not really relatives at all; some adopted the name Basarab in order to be more convincing. In a final phase, not even this formality mattered anymore; the rulers were now appointed by the Turks anyway. How were rulers chosen, whether from within the dynasty or from outside it? In principle, they were picked by an assembly of boyars, sometimes by a larger assembly of the country. However, in the absence of a strict procedure (unless a prince had made his son an associate on the throne, thus theoretically ensuring his succession), conflicts were numerous. In addition, help was sometimes sought from outside, providing an excuse for the Hungarians or Turks to intervene. In these circumstances, not all reigns reached their natural term; some rulers were deposed or killed. There were, however, a few long reigns, and it is to them that the most lasting political and cultural achievements belong. Thus we have Mircea the Old (1386–1418) in Wallachia, and his contemporary Alexander the Good (1400–1432) in Moldavia; then Stephen the Great (1457–1504), whose reign – the longest of all – is considered the most glorious period in Moldavia’s history; the parallel reigns of Matei Basarab (1633–54) in Wallachia and Vasile Lupu (or Basil the Wolf, 1634–53) in Moldavia; and finally, in Wallachia, Constantin Brîncoveanu (1688–1714). But these are the exceptions. The norm was frequent changes of rule, short reigns of a few years at the most and an instability which increased with each century that passed." - Lucian Boia, Romania: Borderland of Europe (London: Reaktion Books, 2001), 63-4. And from another esteemed Romanian historian (and Westernophile): "The system of succession to the throne was one of the most unfortunate of our medieval institutions. Despite the fact that the first two successions in Wallachia seem to have happened without difficulty, after the third generation – or the second, in Moldavia – we find that the throne was not automatically handed down to the eldest son of the defunct voivode (as the kings of France or England had managed) but that a successor was elected from his sons. It was as if the descendants of former knyazes, voivodes and other lords in the land wanted to revive the initial election of the Great Voivode. From that moment on, this would become the rule – with rare exceptions, such as the extraordinary figures of Mircea the Elder in Wallachia and Stephen the Great in Moldavia, who succeeded in placing their eldest sons on the throne before they died. When the throne became vacant, the “country” would elect a new voivode from the house of Basarab (in Wallachia) or Bogdan (in Moldavia). It was an elective hereditary system. Any member of the house was eligible if they were considered worthy, even illegitimate children (in fact, many of our greatest rulers were bastards, such as Stephen the Great, Petru Rareş, Neagoe Basarab and Michael the Brave). It was enough to be “of the blood” of voivodes – or, as it was said in Romanian, “from the bone” of voivodes." - Neagu Djuvara, A Brief Illustrated History of Romanians (Bucharest: Humanitas, 2016).* * I'd give page numbers, but I've found it only in .epub format. You can check chapter 2 ('The Dawn of the Romanian Medieval States'), subchapter 6 ('Succession to the throne').

## Reply 348 — participant_226 · 2021-06-26 · post-27645016

<!-- artifact:quote:start -->
> Servancour said: No immediate plans, but we always try to improve the map when we can, so we'll probably get back to improving the Baltic area at some point in the future. Click to expand...
<!-- artifact:quote:end -->
Something I thought would be quite cool would be to have a decision similar to "Elevate the Kingdom of Mann & the Isles" except for Visby making it a trade hub in the Baltic, its situated right in the middle of the Baltic with good trade access to basically all the countries there. It wouldn't be too historically inaccurate either because they were a member of the Hanseatic League which was all about trade and as far as I am aware Visby technically became a kingdom under Valdemar IV in 1361. I personally really enjoyed the "Elevate the Kingdom of Mann & the Isles" concept and I think it could be used more in places like Visby to add in some unique kingdoms that are not exactly easy to create.

## Reply 349 — participant_227 · 2021-06-28 · post-27648132

I have two main questions, mostly pertaining to historical realism with regards to cultures: 1. Will the culture update attempt to redress the issues with Muwalladism as its own distinct faith within islam? This fact has never made sense to me, as the Iberians' view on homosexuality et al was largely cultural (on the basis of past cultural heritage), not religious. From what I can gather, the Muslims of Cordoba were religiously indistinguishable from the Muslims of Baghdad. 2. With the advent of languages, will pidgin languages be represented in some way? This can be done perhaps as a lingua franca that can be learned relatively easily by people and serves as a shared language. Historical precedent for this is of course Sabir, which although derived heavily from certain European languages was its own distinct language.

## Reply 350 — participant_186 · 2021-07-06 · post-27664210

<!-- artifact:quote:start -->
> TempestM said: But you can't modify religions now? Only creating new Faiths Click to expand...
<!-- artifact:quote:end -->
You can, actually, it's just incredibly difficult and you can (usually) only do if it if you're the religious head

## Reply 351 — participant_038 · 2021-07-06 · post-27664213

<!-- artifact:quote:start -->
> Josh is Stupid said: You can, actually, it's just incredibly difficult and you can (usually) only do if it if you're the religious head Click to expand...
<!-- artifact:quote:end -->
How?

## Reply 352 — participant_207 · 2021-07-06 · post-27664571

<!-- artifact:quote:start -->
> Josh is Stupid said: You can, actually, it's just incredibly difficult and you can (usually) only do if it if you're the religious head Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> TempestM said: How? Click to expand...
<!-- artifact:quote:end -->
I think it works if you are the liege of the religious head as well. @TempestM, I don't remember the exact conditions to trigger it, but there's a random event where you can get the option to change one facet of the faith. It's limited to a few things (like instituting incest), it's random which option you get, and IIRC it can only happen once per faith.

## Reply 353 — participant_043 · 2021-07-07 · post-27665543

<!-- artifact:quote:start -->
> Karlington said: I think it works if you are the liege of the religious head as well. @TempestM, I don't remember the exact conditions to trigger it, but there's a random event where you can get the option to change one facet of the faith. It's limited to a few things (like instituting incest), it's random which option you get, and IIRC it can only happen once per faith. Click to expand...
<!-- artifact:quote:end -->
I very much doubt this is actually a thing. Source: I've looked at all the religion event code and I can't see anything that would change an existing faiths doctrines aside from the unique decisions such as the dismantle papacy one. Edit: Turns out there is actually one such event. So ignore this statement

## Reply 354 — participant_153 · 2021-07-07 · post-27665822

<!-- artifact:quote:start -->
> Unknown Sage said: I very much doubt this is actually a thing. Source: I've looked at all the religion event code and I can't see anything that would change an existing faiths doctrines aside from the unique decisions such as the dismantle papacy one. Click to expand...
<!-- artifact:quote:end -->
It's not in the religious event code because it's a learning event. They are referring to event: learning_theology_special.1001 and follow up event learning_theology_special.1002 (@Karlington 's description is dead on) Spoiler: learning_theology_special.1001 Code: learning_theology_special.1001 = { type = character_event title = learning_theology_special.1001.t desc = learning_theology_special.1001.desc theme = learning_theology_focus left_portrait = scope:portrait trigger = { is_ai = no has_focus = learning_theology_focus NOT = { has_character_flag = had_learning_theology_special_1001_this_lifetime } faith = { NOR = { exists = var:variable_changed_doctrine_learning_theology_special_1001 has_doctrine = unreformed_faith_doctrine } } OR = { exists = cp:councillor_court_chaplain AND = { exists = faith.religious_head root = faith.religious_head } AND = { exists = faith.religious_head exists = faith.religious_head.liege faith.religious_head.liege = root } } OR = { has_trait = scholar learning >= very_high_skill_rating } } weight_multiplier = { base = 1 modifier = { add = -0.5 faith = { fervor < medium_fervor_value } } modifier = { add = -0.5 NOR = { AND = { exists = faith.religious_head root = faith.religious_head } AND = { exists = faith.religious_head exists = faith.religious_head.liege faith.religious_head.liege = root faith.religious_head = { is_ai = yes } } } } } immediate = { add_character_flag = had_learning_theology_special_1001_this_lifetime if = { limit = { exists = faith.religious_head root = faith.religious_head } faith.religious_head = { save_scope_as = player_pope save_scope_as = portrait #For portrait } } else_if = { limit = { exists = faith.religious_head exists = faith.religious_head.liege faith.religious_head.liege = root faith.religious_head = { is_ai = yes } } faith.religious_head = { save_scope_as = vassal_pope save_scope_as = portrait #For portrait } save_scope_as = pope_liege } else_if = { limit = { exists = cp:councillor_court_chaplain } cp:councillor_court_chaplain = { save_scope_as = bishop save_scope_as = portrait #For portrait } } hidden_effect = { #To randomize the doctrine that's changed random_list = { 10 = { trigger = { NOT = { faith = { has_doctrine = doctrine_adultery_women_accepted } } } save_scope_value_as = { name = female_adultery_doctrine value = yes } } 10 = { trigger = { NOT = { faith = { has_doctrine = doctrine_adultery_men_accepted } } } save_scope_value_as = { name = male_adultery_doctrine value = yes } } 10 = { trigger = { NOT = { faith = { has_doctrine = doctrine_homosexuality_accepted } } } save_scope_value_as = { name = homosexuality_doctrine value = yes } } 10 = { trigger = { NOT = { faith = { has_doctrine = doctrine_kinslaying_accepted } } } save_scope_value_as = { name = kinslyaing_doctrine value = yes } } 10 = { trigger = { NOT = { faith = { has_doctrine = doctrine_witchcraft_accepted } } } save_scope_value_as = { name = witchcraft_doctrine value = yes } } 10 = { trigger = { NOT = { faith = { has_doctrine = doctrine_consanguinity_unrestricted } } } save_scope_value_as = { name = consanguinity_doctrine value = yes } } } } } option = { #Player Religious Head decides to incorporate doctrine. name = learning_theology_special.1001.d trigger = { exists = scope:player_pope faith = { fervor >= medium_fervor_value } } duel = { skill = learning value = extremely_high_skill_rating 10 = { desc = learning_theology_special.1001.d.success compare_modifier = { value = scope:duel_value multiplier = 1 } show_as_tooltip = { learning_theology_special_1001_doctrine_effect = yes add_learning_lifestyle_perk_points = 1 } trigger_event = learning_theology_special.1002 } 20 = { desc = learning_theology_special.1001.d.failure send_interface_toast = { title = learning_theology_special.1001.d.failure.toast left_icon = root add_learning_lifestyle_xp = minor_lifestyle_xp add_piety = major_piety_loss } } } stress_impact = { zealous = medium_stress_impact_gain } ai_chance = { base = 0 } } option = { #Player petitions vassal religious head to integrate doctrine. name = learning_theology_special.1001.e trigger = { exists = scope:vassal_pope faith = { fervor >= medium_fervor_value } } duel = { skill = learning target = scope:vassal_pope 1 = { desc = learning_theology_special.1001.e.success compare_modifier = { value = scope:duel_value multiplier = 2 } opinion_modifier = { # Opinion Factor who = scope:vassal_pope opinion_target = root multiplier = 0.25 } show_as_tooltip = { learning_theology_special_1001_doctrine_effect = yes add_learning_lifestyle_perk_points = 1 } trigger_event = learning_theology_special.1002 } 50 = { desc = learning_theology_special.1001.e.failure send_interface_toast = { title = learning_theology_special.1001.e.failure.toast left_icon = scope:vassal_pope add_learning_lifestyle_xp = minor_lifestyle_xp add_piety = major_piety_loss } } } stress_impact = { zealous = medium_stress_impact_gain } ai_chance = { base = 0 } } option = { #Share findings with Court Chaplain. name = learning_theology_special.1001.a trigger = { exists = scope:bishop } scope:bishop = { add_opinion = { target = root modifier = respect_opinion opinion = 15 } } random_list = { desc = learning_theology_special.1001.a.desc 100 = { desc = learning_theology_special.1001.a.success show_chance = no modifier = { add = { value = scope:bishop.ai_zeal } } send_interface_toast = { title = learning_theology_special.1001.a.success.toast add_learning_lifestyle_perk_points = 1 } } 100 = { desc = learning_theology_special.1001.a.failure show_chance = no modifier = { #Make this instant success scope:bishop.ai_zeal >= low_positive_ai_value add = -1000 } modifier = { add = { value = scope:bishop.ai_zeal multiply = -1 } } send_interface_toast = { title = learning_theology_special.1001.a.failure.toast left_icon = scope:bishop add_learning_lifestyle_xp = miniscule_lifestyle_xp add_piety = minor_piety_gain } } } stress_impact = { zealous = minor_stress_impact_loss cynical = minor_stress_impact_gain } ai_chance = { base = 100 } } option = { #Study in private. name = learning_theology_special.1001.b add_learning_lifestyle_xp = medium_lifestyle_xp add_piety = minor_piety_loss stress_impact = { zealous = medium_stress_impact_gain cynical = medium_stress_impact_loss } ai_chance = { base = 100 ai_value_modifier = { ai_zeal = -0.5 } } } option = { #Burn. name = learning_theology_special.1001.c add_piety = medium_piety_gain zealous_progression_effect = yes stress_impact = { zealous = medium_stress_impact_loss cynical = medium_stress_impact_gain } ai_chance = { base = 100 ai_value_modifier = { ai_zeal = 1.5 } } } } Spoiler: learning_theology_special.1002 Code: #Player successfully changed the faith's doctrine. learning_theology_special.1002 = { type = character_event title = learning_theology_special.1002.t desc = { first_valid = { triggered_desc = { trigger = { exists = scope:player_pope } desc = learning_theology_special.1002.a.desc } triggered_desc = { trigger = { exists = scope:vassal_pope } desc = learning_theology_special.1002.b.desc } } } theme = learning_theology_focus right_portrait = scope:portrait immediate = { learning_theology_special_1001_doctrine_effect = yes add_learning_lifestyle_perk_points = 1 } option = { # name = learning_theology_special.1002.a every_player = { limit = { NOR = { this = root this = scope:vassal_pope } faith = root.faith } trigger_event = learning_theology_special.1003 } } } Spoiler: learning_theology_special_1001_doctrine_effect Code: learning_theology_special_1001_doctrine_effect = { if = { limit = { exists = scope:female_adultery_doctrine } faith = { add_doctrine = doctrine_adultery_women_accepted } } else_if = { limit = { exists = scope:male_adultery_doctrine } faith = { add_doctrine = doctrine_adultery_men_accepted } } else_if = { limit = { exists = scope:homosexuality_doctrine } faith = { add_doctrine = doctrine_homosexuality_accepted } } else_if = { limit = { exists = scope:kinslyaing_doctrine } faith = { add_doctrine = doctrine_kinslaying_accepted } } else_if = { limit = { exists = scope:witchcraft_doctrine } faith = { add_doctrine = doctrine_witchcraft_accepted } } else_if = { limit = { exists = scope:consanguinity_doctrine } faith = { add_doctrine = doctrine_consanguinity_unrestricted } } faith = { change_fervor = medium_fervor_loss set_variable = { name = variable_changed_doctrine_learning_theology_special_1001 value = yes years = 250 } } } edit: clarity and formatting

## Reply 355 — participant_043 · 2021-07-07 · post-27666023

<!-- artifact:quote:start -->
> pengoyo said: It's not in the religious event code because it's a learning event. They are referring to event: learning_theology_special.1001 and follow up event learning_theology_special.1002 (@Karlington 's description is dead on) Spoiler: learning_theology_special.1001 Code: learning_theology_special.1001 = { type = character_event title = learning_theology_special.1001.t desc = learning_theology_special.1001.desc theme = learning_theology_focus left_portrait = scope:portrait trigger = { is_ai = no has_focus = learning_theology_focus NOT = { has_character_flag = had_learning_theology_special_1001_this_lifetime } faith = { NOR = { exists = var:variable_changed_doctrine_learning_theology_special_1001 has_doctrine = unreformed_faith_doctrine } } OR = { exists = cp:councillor_court_chaplain AND = { exists = faith.religious_head root = faith.religious_head } AND = { exists = faith.religious_head exists = faith.religious_head.liege faith.religious_head.liege = root } } OR = { has_trait = scholar learning >= very_high_skill_rating } } weight_multiplier = { base = 1 modifier = { add = -0.5 faith = { fervor < medium_fervor_value } } modifier = { add = -0.5 NOR = { AND = { exists = faith.religious_head root = faith.religious_head } AND = { exists = faith.religious_head exists = faith.religious_head.liege faith.religious_head.liege = root faith.religious_head = { is_ai = yes } } } } } immediate = { add_character_flag = had_learning_theology_special_1001_this_lifetime if = { limit = { exists = faith.religious_head root = faith.religious_head } faith.religious_head = { save_scope_as = player_pope save_scope_as = portrait #For portrait } } else_if = { limit = { exists = faith.religious_head exists = faith.religious_head.liege faith.religious_head.liege = root faith.religious_head = { is_ai = yes } } faith.religious_head = { save_scope_as = vassal_pope save_scope_as = portrait #For portrait } save_scope_as = pope_liege } else_if = { limit = { exists = cp:councillor_court_chaplain } cp:councillor_court_chaplain = { save_scope_as = bishop save_scope_as = portrait #For portrait } } hidden_effect = { #To randomize the doctrine that's changed random_list = { 10 = { trigger = { NOT = { faith = { has_doctrine = doctrine_adultery_women_accepted } } } save_scope_value_as = { name = female_adultery_doctrine value = yes } } 10 = { trigger = { NOT = { faith = { has_doctrine = doctrine_adultery_men_accepted } } } save_scope_value_as = { name = male_adultery_doctrine value = yes } } 10 = { trigger = { NOT = { faith = { has_doctrine = doctrine_homosexuality_accepted } } } save_scope_value_as = { name = homosexuality_doctrine value = yes } } 10 = { trigger = { NOT = { faith = { has_doctrine = doctrine_kinslaying_accepted } } } save_scope_value_as = { name = kinslyaing_doctrine value = yes } } 10 = { trigger = { NOT = { faith = { has_doctrine = doctrine_witchcraft_accepted } } } save_scope_value_as = { name = witchcraft_doctrine value = yes } } 10 = { trigger = { NOT = { faith = { has_doctrine = doctrine_consanguinity_unrestricted } } } save_scope_value_as = { name = consanguinity_doctrine value = yes } } } } } option = { #Player Religious Head decides to incorporate doctrine. name = learning_theology_special.1001.d trigger = { exists = scope:player_pope faith = { fervor >= medium_fervor_value } } duel = { skill = learning value = extremely_high_skill_rating 10 = { desc = learning_theology_special.1001.d.success compare_modifier = { value = scope:duel_value multiplier = 1 } show_as_tooltip = { learning_theology_special_1001_doctrine_effect = yes add_learning_lifestyle_perk_points = 1 } trigger_event = learning_theology_special.1002 } 20 = { desc = learning_theology_special.1001.d.failure send_interface_toast = { title = learning_theology_special.1001.d.failure.toast left_icon = root add_learning_lifestyle_xp = minor_lifestyle_xp add_piety = major_piety_loss } } } stress_impact = { zealous = medium_stress_impact_gain } ai_chance = { base = 0 } } option = { #Player petitions vassal religious head to integrate doctrine. name = learning_theology_special.1001.e trigger = { exists = scope:vassal_pope faith = { fervor >= medium_fervor_value } } duel = { skill = learning target = scope:vassal_pope 1 = { desc = learning_theology_special.1001.e.success compare_modifier = { value = scope:duel_value multiplier = 2 } opinion_modifier = { # Opinion Factor who = scope:vassal_pope opinion_target = root multiplier = 0.25 } show_as_tooltip = { learning_theology_special_1001_doctrine_effect = yes add_learning_lifestyle_perk_points = 1 } trigger_event = learning_theology_special.1002 } 50 = { desc = learning_theology_special.1001.e.failure send_interface_toast = { title = learning_theology_special.1001.e.failure.toast left_icon = scope:vassal_pope add_learning_lifestyle_xp = minor_lifestyle_xp add_piety = major_piety_loss } } } stress_impact = { zealous = medium_stress_impact_gain } ai_chance = { base = 0 } } option = { #Share findings with Court Chaplain. name = learning_theology_special.1001.a trigger = { exists = scope:bishop } scope:bishop = { add_opinion = { target = root modifier = respect_opinion opinion = 15 } } random_list = { desc = learning_theology_special.1001.a.desc 100 = { desc = learning_theology_special.1001.a.success show_chance = no modifier = { add = { value = scope:bishop.ai_zeal } } send_interface_toast = { title = learning_theology_special.1001.a.success.toast add_learning_lifestyle_perk_points = 1 } } 100 = { desc = learning_theology_special.1001.a.failure show_chance = no modifier = { #Make this instant success scope:bishop.ai_zeal >= low_positive_ai_value add = -1000 } modifier = { add = { value = scope:bishop.ai_zeal multiply = -1 } } send_interface_toast = { title = learning_theology_special.1001.a.failure.toast left_icon = scope:bishop add_learning_lifestyle_xp = miniscule_lifestyle_xp add_piety = minor_piety_gain } } } stress_impact = { zealous = minor_stress_impact_loss cynical = minor_stress_impact_gain } ai_chance = { base = 100 } } option = { #Study in private. name = learning_theology_special.1001.b add_learning_lifestyle_xp = medium_lifestyle_xp add_piety = minor_piety_loss stress_impact = { zealous = medium_stress_impact_gain cynical = medium_stress_impact_loss } ai_chance = { base = 100 ai_value_modifier = { ai_zeal = -0.5 } } } option = { #Burn. name = learning_theology_special.1001.c add_piety = medium_piety_gain zealous_progression_effect = yes stress_impact = { zealous = medium_stress_impact_loss cynical = medium_stress_impact_gain } ai_chance = { base = 100 ai_value_modifier = { ai_zeal = 1.5 } } } } Spoiler: learning_theology_special.1002 Code: #Player successfully changed the faith's doctrine. learning_theology_special.1002 = { type = character_event title = learning_theology_special.1002.t desc = { first_valid = { triggered_desc = { trigger = { exists = scope:player_pope } desc = learning_theology_special.1002.a.desc } triggered_desc = { trigger = { exists = scope:vassal_pope } desc = learning_theology_special.1002.b.desc } } } theme = learning_theology_focus right_portrait = scope:portrait immediate = { learning_theology_special_1001_doctrine_effect = yes add_learning_lifestyle_perk_points = 1 } option = { # name = learning_theology_special.1002.a every_player = { limit = { NOR = { this = root this = scope:vassal_pope } faith = root.faith } trigger_event = learning_theology_special.1003 } } } Spoiler: learning_theology_special_1001_doctrine_effect Code: learning_theology_special_1001_doctrine_effect = { if = { limit = { exists = scope:female_adultery_doctrine } faith = { add_doctrine = doctrine_adultery_women_accepted } } else_if = { limit = { exists = scope:male_adultery_doctrine } faith = { add_doctrine = doctrine_adultery_men_accepted } } else_if = { limit = { exists = scope:homosexuality_doctrine } faith = { add_doctrine = doctrine_homosexuality_accepted } } else_if = { limit = { exists = scope:kinslyaing_doctrine } faith = { add_doctrine = doctrine_kinslaying_accepted } } else_if = { limit = { exists = scope:witchcraft_doctrine } faith = { add_doctrine = doctrine_witchcraft_accepted } } else_if = { limit = { exists = scope:consanguinity_doctrine } faith = { add_doctrine = doctrine_consanguinity_unrestricted } } faith = { change_fervor = medium_fervor_loss set_variable = { name = variable_changed_doctrine_learning_theology_special_1001 value = yes years = 250 } } } edit: clarity and formatting Click to expand...
<!-- artifact:quote:end -->
huh it seems I stand corrected. Still I consider it weird though that they decided to include such an event instead of a proper mechanic to do such changes to existing religions. Say something similar to reformation except it changes the existing religion instead of making a new one. Provided you fulfill the logical requirements for that, (such as having the religious head as your vassal)

## Reply 356 — participant_187 · 2021-07-08 · post-27667105

<!-- artifact:quote:start -->
> Unknown Sage said: Say something similar to reformation except it changes the existing religion instead of making a new one. Click to expand...
<!-- artifact:quote:end -->
Well, that wouldn't make sense. If you make a change to religion, you create a new religion because people still have the option to disagree with your change. Of course, you can then oppress the old religion and come out on top, but the change should not normally be automatic (and if you are, say, the last Copt and create a new religion, the change will effectively be automatic - but you will not inherit ecumenical acceptance which is, again, OK). Note that nearly each Ecumenical Council left a "heresy" (that is, a faith that did not accept its decisions) behind.

## Reply 357 — participant_043 · 2021-07-08 · post-27667708

<!-- artifact:quote:start -->
> Viridianus said: Well, that wouldn't make sense. If you make a change to religion, you create a new religion because people still have the option to disagree with your change. Of course, you can then oppress the old religion and come out on top, but the change should not normally be automatic (and if you are, say, the last Copt and create a new religion, the change will effectively be automatic - but you will not inherit ecumenical acceptance which is, again, OK). Note that nearly each Ecumenical Council left a "heresy" (that is, a faith that did not accept its decisions) behind. Click to expand...
<!-- artifact:quote:end -->
I see the point you are making. But I myself would be willing to sacrifice perfect realism for a mechanic that works like the idea I described (and clearly the event in question that sort of does this already works under the same assumption). Instead you can maybe simulate the populace being unhappy about this with a drop in fervour so that heresies are likely to pop up after such a change?

## Reply 358 — participant_108 · 2021-07-08 · post-27668411

<!-- artifact:quote:start -->
> Unknown Sage said: I see the point you are making. But I myself would be willing to sacrifice perfect realism for a mechanic that works like the idea I described (and clearly the event in question that sort of does this already works under the same assumption). Instead you can maybe simulate the populace being unhappy about this with a drop in fervour so that heresies are likely to pop up after such a change? Click to expand...
<!-- artifact:quote:end -->
That would only really matter in a case where fervour is already slightly low, and where there are a lot of other faiths in the religion for people to change to. It would be virtually useless with (for example) the pagan faiths where there is the Old, unreformed, faith and whatever you've created. It wouldn't make sense for Catholicism to change tenets, and as a result people become *anything but Catholic* without there being an "old" Catholic rump left behind. Even this event doesn't entirely make sense to me, even though it's more limited in scope to doctrines. There's also that being able, as a single ruler in Europe, to change the entire Catholic religion would be *weird* at best. At least with the event you're only changing one tenet *and* have to be either the HoF or able to tell the HoF what to do.

## Reply 359 — participant_043 · 2021-07-08 · post-27668581

<!-- artifact:quote:start -->
> DreadLindwyrm said: That would only really matter in a case where fervour is already slightly low, and where there are a lot of other faiths in the religion for people to change to. It would be virtually useless with (for example) the pagan faiths where there is the Old, unreformed, faith and whatever you've created. It wouldn't make sense for Catholicism to change tenets, and as a result people become *anything but Catholic* without there being an "old" Catholic rump left behind. Even this event doesn't entirely make sense to me, even though it's more limited in scope to doctrines. There's also that being able, as a single ruler in Europe, to change the entire Catholic religion would be *weird* at best. At least with the event you're only changing one tenet *and* have to be either the HoF or able to tell the HoF what to do. Click to expand...
<!-- artifact:quote:end -->
That's fair. I suppose we just disagree on this then. Though maybe I did not make it clear that I didn't specifically want it to be possible to change all the faith doctrines at once. All I wanted was a mechanic that simply allows you to direct what should be changed. Instead of a random event altering a random doctrine, provided you indeed either are the HoF or have the HoF as a vassal. Specifically I consider this important because otherwise there is no way to ever change your religion ever (without trying to glitch your way through) if you at any point in time become a temporal HoF.

## Reply 360 — participant_108 · 2021-07-08 · post-27668648

<!-- artifact:quote:start -->
> Unknown Sage said: That's fair. I suppose we just disagree on this then. Though maybe I did not make it clear that I didn't specifically want it to be possible to change all the faith doctrines at once. All I wanted was a mechanic that simply allows you to direct what should be changed. Instead of a random event altering a random doctrine, provided you indeed either are the HoF or have the HoF as a vassal. Specifically I consider this important because otherwise there is no way to ever change your religion ever (without trying to glitch your way through) if you at any point in time become a temporal HoF. Click to expand...
<!-- artifact:quote:end -->
Giving away the HoF title and form a new faith would work in this case.

## Reply 361 — participant_216 · 2021-07-10 · post-27672737

<!-- artifact:quote:start -->
> DreadLindwyrm said: There's also that being able, as a single ruler in Europe, to change the entire Catholic religion would be *weird* at best. Click to expand...
<!-- artifact:quote:end -->
Tbh I can see it happening if you've vassalized the Pope and control most of the Catholic territory.

## Reply 362 — participant_160 · 2021-08-25 · post-27753146

<!-- artifact:quote:start -->
> Servancour said: View attachment 731859 [Image of the Land of the Bow tradition]​ Click to expand...
<!-- artifact:quote:end -->
I know it's been a while, but I was thinking about playing as the Nubians, and are you sure Hunting Grounds are the best building for the bonus effect on archers, since Nubians won't be able to build many of them? In both start dates there are 23 Nubian counties, of which only 6 are eligible thanks to having Drylands as the terrain in there capitol baronies, with the rest being 15 floodplains, one Desert and one Desert Mountain. There are 24 non-capital baronies that can build Hunting Grounds (all Drylands), but only 5 are able to have castles built in them even if want to try and hold them for the bonus (the rest either have cities/temples built in them, or are in counties with only 3 holdings anyways). So unless A) the terrain range for hunting grounds is being expanded; B) Nubians get the ability to build hunting grounds in floodplains, or C) Barony level Men-at-arms bonus now apply to the county holder, they won't actually be using that bonus until they start expanding out of their starting area. From a pure balance point I could understand wanting to limit bonus stacking, but it's weird to me that a culture should have a major affinity for something they'll have so little familiarity with. Like the Anglo-Saxons being good with Wetland Farms or the Spanish with Forestry.

## Reply 363 — participant_228 · 2021-09-23 · post-27807516

Any particular reason for Anglo-Saxon being "inventive"? Before the 19th century, the English were known for being parochial and conservative, the inspiration for Hobbits from LOTR. A couple example quotes: "the English are great lovers of themselves , and of everything belonging to them ; they think that there are no other men than themselves , and no other world but England ; and whenever they see a handsome foreigner , they say that“ he looks like an Englishman , and that “it is a great pity that he should not be an Englishman;” and when they partake of any delicacy with a foreigner , they ask him , " whether such a thing is made in their country ? " "-A relation of the Island of England, 1498, translated in 1847. "Thanks to our sullen resistance to innovation, thanks to the cold sluggishness of our national character, we still bear the stamp of our forefathers."-Reflections on the Revolution in France, 1790 I find it most likely that this extends back into the medieval period but I don't have proof of it.

## Reply 364 — participant_108 · 2021-09-23 · post-27808300

<!-- artifact:quote:start -->
> Jarolleon said: Any particular reason for Anglo-Saxon being "inventive"? Before the 19th century, the English were known for being parochial and conservative, the inspiration for Hobbits from LOTR. A couple example quotes: "the English are great lovers of themselves , and of everything belonging to them ; they think that there are no other men than themselves , and no other world but England ; and whenever they see a handsome foreigner , they say that“ he looks like an Englishman , and that “it is a great pity that he should not be an Englishman;” and when they partake of any delicacy with a foreigner , they ask him , " whether such a thing is made in their country ? " "-A relation of the Island of England, 1498, translated in 1847. "Thanks to our sullen resistance to innovation, thanks to the cold sluggishness of our national character, we still bear the stamp of our forefathers."-Reflections on the Revolution in France, 1790 I find it most likely that this extends back into the medieval period but I don't have proof of it. Click to expand...
<!-- artifact:quote:end -->
Well, "English", and "Anglo-Saxon" are different cultures, so the 15th and 19th century visions of "English" culture aren't necessarily accurate for 9th century Anglo-Saxons.

## Reply 365 — participant_229 · 2021-09-23 · post-27808322

<!-- artifact:quote:start -->
> Jarolleon said: Any particular reason for Anglo-Saxon being "inventive"? Click to expand...
<!-- artifact:quote:end -->
My guess is that it is a reference to famous Old English scholars like the Venerable Bede, Alcuin of York, and Eilmer of Malmesbury, or even the scholarship of Alfred the Great himself. Pre-conquest English culture is a completely different beast than even late medieval England.

## Reply 366 — participant_230 · 2021-09-23 · post-27808414

For game balance sake, are ethos and traditions going to give bonuses only? I soppose for each bonus a penalty in some other area should apply.... Based on the screens hots, upon 1.5, there goes another round of nodding for balancing the gameplay of the new content.

## Reply 367 — participant_108 · 2021-09-23 · post-27808457

<!-- artifact:quote:start -->
> Torredebelem said: For game balance sake, are ethos and traditions going to give bonuses only? I soppose for each bonus a penalty in some other area should apply.... Based on the screens hots, upon 1.5, there goes another round of nodding for balancing the gameplay of the new content. Click to expand...
<!-- artifact:quote:end -->
Since everyone gets a bonus - that's theoretically equal - from ethos they don't need to have penalties there. And to be honest, I don't want to feel penalised by a culture *having* to take penalties to get bonuses as it then becomes restrictive and very "forced". Imagine a culture that has about 50% dry plains and 50% wet plains. If you want to take two culture traits to get bonuses in both terrains, then that's already got the inherent opportunity cost of taking up two of your limited number of slots; but if the "wet commander" and "dry commander" come with penalties to the other terrain, then not only has it cost you two slots, but it's also costing you most of the bonuses of taking the traits in the first place. (An area which might have both "wet" and "dry" terrain would be somewhere like Egypt, where the Nile banks are potentially *very* wet, but the lands further away from the Nile are notoriously dry.)

## Reply 368 — participant_230 · 2021-09-23 · post-27808486

<!-- artifact:quote:start -->
> DreadLindwyrm said: Since everyone gets a bonus - that's theoretically equal - from ethos they don't need to have penalties there. And to be honest, I don't want to feel penalised by a culture *having* to take penalties to get bonuses as it then becomes restrictive and very "forced". Imagine a culture that has about 50% dry plains and 50% wet plains. If you want to take two culture traits to get bonuses in both terrains, then that's already got the inherent opportunity cost of taking up two of your limited number of slots; but if the "wet commander" and "dry commander" come with penalties to the other terrain, then not only has it cost you two slots, but it's also costing you most of the bonuses of taking the traits in the first place. (An area which might have both "wet" and "dry" terrain would be somewhere like Egypt, where the Nile banks are potentially *very* wet, but the lands further away from the Nile are notoriously dry.) Click to expand...
<!-- artifact:quote:end -->
There is a huge number of modifiers to pick from, not only the notable case you present and for which you have all the reason. It is a matter of picking the right penalties. From a design standpoint I prefer to have penalties included too. After all more bonuses will be mostly taken advantage by the player to their utmost and only serve to unbalance the game even more, turn the game even easier and cause the players to lose interest in the campaign even faster. Curiously and as an oversight of mine - I was reading the DD and writing my previous post on my phone - it seems the French culture has a penalty included: +50% Tyranny for being Chivalrous. Good news, at least in this case!

## Reply 369 — participant_108 · 2021-09-23 · post-27808511

<!-- artifact:quote:start -->
> Torredebelem said: There is a huge number of modifiers to pick from, not only the notable case you present and for which you have all the reason. It is a matter of picking the right penalties. From a design standpoint I prefer to have penalties included too. After all more bonuses will be mostly taken advantage by the player to their utmost and only serve to unbalance the game even more, turn the game even easier and cause the players to lose interest in the campaign even faster. Curiously and as an oversight of mine - I was reading the DD and writing my previous post on my phone - it seems the French culture has a penalty included: +50% Tyranny for being Chivalrous. Good news, at least in this case! Click to expand...
<!-- artifact:quote:end -->
The problem is that you need to make the penalties ones that universally make sense. In most cases it's difficult to think of a penalty that should logically *always* go with a particular bonus, without being nonsensical in some situations. What penalties do you give to a culture for having access to tanistry for example?

## Reply 370 — participant_230 · 2021-09-23 · post-27808564

<!-- artifact:quote:start -->
> DreadLindwyrm said: The problem is that you need to make the penalties ones that universally make sense. In most cases it's difficult to think of a penalty that should logically *always* go with a particular bonus, without being nonsensical in some situations. What penalties do you give to a culture for having access to tanistry for example? Click to expand...
<!-- artifact:quote:end -->
If the only bonus is to give access to tanistry certainly no penalty is warranted. But let me give you some meaningful penalties using all the screenshots from the dev diary to show you how easy it is to come up with some logical options as penalties: Bellicose - 3 to Diplomacy -10% success to Sway Spiritual -10% to Monthly Prestige -10% to Development Inventive -25% to Control Swords for Hire +10% MaA recruitment cost +10% MaA maintenance cost Chivalry (It's balanced right now) +50% Tyranny gained Esteemed Hospitality -10% Success Chance for Hostile Schemes Seafarers -20% for Levy Size Land of the Bow -5 Attacker Advantage Cannot recruit Armoured Footmen

## Reply 371 — participant_108 · 2021-09-23 · post-27808733

<!-- artifact:quote:start -->
> Torredebelem said: Bellicose - 3 to Diplomacy -10% success to Sway Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Torredebelem said: Spiritual -10% to Monthly Prestige -10% to Development Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Torredebelem said: Inventive -25% to Control Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Torredebelem said: Swords for Hire +10% MaA recruitment cost +10% MaA maintenance cost Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Torredebelem said: Esteemed Hospitality -10% Success Chance for Hostile Schemes Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Torredebelem said: Seafarers -20% for Levy Size Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Torredebelem said: Land of the Bow -5 Attacker Advantage Cannot recruit Armoured Footmen Click to expand...
<!-- artifact:quote:end -->
That's quite a large diplomacy penalty, and swaying someone doesn't have to be entirely diplomatic. Plus "war is diplomacy by other means". Here though you're effectively saying you can't be both a warlord and diplomatic. I'd have to disagree with this somewhat. I'm not convinced that merely being spiritually minded would reduce your prestige - especially amongst *other* people who are also spiritually minded. Even more so with the flavour text stating that to this culture "Spirituality is the only way forward in a harsh and uncaring world" - such that they see it as the "correct" and thus most prestigious way forward, since they don't value other approaches. Development penalties also strike me as generally bad. It's one of the major factors in why Insular Christianity is considered bad, because it's inherently crippling, since it then rolls over into innovations and thus tech progress, as well as overall wealth. I see no reason for this to make sense at all. So, we've got a warrior culture that trains a higher proportion of its population to take up the sword, but it's harder to recruit people to take up the sword? Yes, you lose some to the mercenary companies, but that's counterbalanced by having more potential warriors overall in the society. Logical for some hostile schemes, not so logical for others. Abducting someone on the pretext that you've invited them to enjoy your hospitality *could* be easier. Since one part of the trait *raises* levy size in some cases, this is effectively just removing one of the strengths of the trait. Falls into the same problem as my Nile example earlier if you also have a reason for a heavy armour foot tradition. Say you've got a history of heavy foot supported by archers.

## Reply 372 — participant_230 · 2021-09-25 · post-27812575

<!-- artifact:quote:start -->
> DreadLindwyrm said: That's quite a large diplomacy penalty, and swaying someone doesn't have to be entirely diplomatic. Plus "war is diplomacy by other means". Here though you're effectively saying you can't be both a warlord and diplomatic. I'd have to disagree with this somewhat. I'm not convinced that merely being spiritually minded would reduce your prestige - especially amongst *other* people who are also spiritually minded. Even more so with the flavour text stating that to this culture "Spirituality is the only way forward in a harsh and uncaring world" - such that they see it as the "correct" and thus most prestigious way forward, since they don't value other approaches. Development penalties also strike me as generally bad. It's one of the major factors in why Insular Christianity is considered bad, because it's inherently crippling, since it then rolls over into innovations and thus tech progress, as well as overall wealth. I see no reason for this to make sense at all. So, we've got a warrior culture that trains a higher proportion of its population to take up the sword, but it's harder to recruit people to take up the sword? Yes, you lose some to the mercenary companies, but that's counterbalanced by having more potential warriors overall in the society. Logical for some hostile schemes, not so logical for others. Abducting someone on the pretext that you've invited them to enjoy your hospitality *could* be easier. Since one part of the trait *raises* levy size in some cases, this is effectively just removing one of the strengths of the trait. Falls into the same problem as my Nile example earlier if you also have a reason for a heavy armour foot tradition. Say you've got a history of heavy foot supported by archers. Click to expand...
<!-- artifact:quote:end -->
To each its own and certainly for the sake of argument one can find drawbacks in almost all bonuses or penalties being presented. Had I the patience to do it, I certainly could defend my choices with the same level of savvy as you criticize them. Easy to come up with the arguments either to criticize or to support them. But I *do* confess I did all the bonuses on the fly while answering your post, without giving much thought to each. It is dead easy to come up with penalties for each Ethos & Tradition, based on the bonuses each gives and its character. What is certain is that with bonuses mostly, game balance will be even more tilted as the player is the one who will take mostly the advantages given. And even in 1.4 game balance is already quite poor, in my opinion, with lots of bonuses and gameplay far too much "sugared" with all sorts of positive modifiers. Also having penalties to consider when making the option of picking Ethos & Traditions would increase the dilemma faced and the complexity of the choices presented to the player, thus would be a good gameplay element.

