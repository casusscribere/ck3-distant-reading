---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1701999/"
forum_thread_id: 1701999
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 155
title: "Dev Diary #155 - The Shattered Empire"
dd_date: 2024-09-03
author_handle: PDX-Trinexx
expansion: Roads to Power
patch: Patch 1.13
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 4534
inline_image_count: 47
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1701999'
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
    location: raw_lines_~28_to_152
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_151
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3246.jpg?1725346501
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_154_to_156
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_685_to_689
    action: preserved_and_flagged
    counts:
      Like: 111
      Love: 94
      (unlabeled — rendered as base64 data URI): 9
      Haha: 2
    note: Reactions block parsed; 3 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_697_to_756
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_757_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3246.jpg?1725346501)
<!-- artifact:thread_banner:end -->

# Dev Diary #155 - The Shattered Empire

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)
- Start date [Sep 3, 2024](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-155-the-shattered-empire.1701999/)
<!-- artifact:thread_metadata:end -->

*Note: You can also listen to today's Dev Diary here*[*on our YouTube channel!*](https://www.youtube.com/watch?v=MRySmxrirI4)  

---

Hello everybody! I’m Jacob, the Community Manager for Crusader Kings. This week’s dev diary will be *slightly* different, as we’re going to cover several topics from several different authors. Key subjects are Roman Restoration, the 4th Crusade, and the addition of dynamically spawned Historical Characters once the game has actually started.  

We’ll start off with the new Roman Restoration content coming with Roads to Power, so I’ll hand it over to our resident Byzantine scholar now.  

---

#### Restoring Rome​


*Salvete!* You might remember me from the previous dev diary about Byzantium. I’m Chad, a Game Designer (now turned Programmer) working on CKIII. Today I’ll be discussing one of the smaller updates we’re making to the classic Restore Rome decision in Roads to Power.  

#### Even though they knew themselves as Romans, Byzantium was not the same as the Roman Empire that you can “restore” in game. And thoughts of “restoring” this idealized version of ancient Rome were not common during our period. If you’d like to play a grand strategy game as the Roman Empire, may I point you towards a great one called Imperator: Rome? I think you’d love it. It even recently received an update!​


With that aside, however, I’d like to show off some of the content we’ve updated for reconquering pieces of Rome’s past.  

![image-01.png](https://forumcontent.paradoxplaza.com/public/1173858/image-01.png "image-01.png")


*[Event showing the reconquering of Tunis which is fired from the new “important locations” system]*  

In Roads to Power, you’ll get updated event content for conquering pieces of the historical Roman Empire. This is part of a great new feature from my colleague we’re calling “important locations” that modders will likely be interested in. You can now script a relationship between a landed title and another higher tier title and fire content when they enter and exit the realm. These can be scripte d on the fly as well, allowing for dynamic content about titles changing hands.  

![image-02.png](https://forumcontent.paradoxplaza.com/public/1173859/image-02.png "image-02.png")


*[Script example of setting the county of Rome as an important location for the Byzantine Empire]*  

![image-03.png](https://forumcontent.paradoxplaza.com/public/1173860/image-03.png "image-03.png")


*[Full documentation of the set_important_location script effect showing information about parameters and scopes]*  

We’ve updated how you can “restore” “Rome” as Byzantium with an eye towards how the Byzantines may have thought about such a thing, primarily through the lens of Justinian. With this comes gorgeous new art as well as a new decision to make.  

![image-04.png](https://forumcontent.paradoxplaza.com/public/1173861/image-04.png "image-04.png")


*[Event that occurs when you’ve taken the decision to restore the Roman Empire]*  

![image-05.png](https://forumcontent.paradoxplaza.com/public/1173862/image-05.png "image-05.png")


*[First option when restoring Rome, which provides access to unique bonuses and converts your realm to Hellenism, but turns on hard mode]*  

![image-06.png](https://forumcontent.paradoxplaza.com/public/1173863/image-06.png "image-06.png")


*[Second option for restoring Rome, which keeps the original functionality]*  

We wanted to create an interesting choice here. There were concerns that this increase in difficulty might be perceived as “too gamey” but we ultimately decided that restoring the ancient Roman Empire in the Middle Ages is already a “gamey” notion.  

Managing a massive empire like the de jure territory of Rome should be hard and create a new challenge for players. Of course, if it’s too difficult to keep the whole enterprise together and functioning, you can opt for the historical decision to split it into East and West. Many historical emperors tried their best to maintain control over such a vast territory and failed–ultimately deciding on some variation of dividing power. Perhaps you will be the one to succeed in keeping the realm united–but as I said, it won’t be a walk in the park.  

![image-07.png](https://forumcontent.paradoxplaza.com/public/1173864/image-07.png "image-07.png")


*[Decision to “Cleave the Empire” which splits the Roman Empire into Eastern and Western parts and ends hard mode]*  

This also means that there is now a legitimate way to convert to Hellenism in-game. Upon reforming Hellenism, players have access to a new Faith Tenet called Household Gods.  

![image-08.jpg](https://forumcontent.paradoxplaza.com/public/1173865/image-08.jpg "image-08.jpg")


*[New art for the Household Gods tenet for Hellenism]*  

![image-09.png](https://forumcontent.paradoxplaza.com/public/1173866/image-09.png "image-09.png")


*[Household Gods tenet for Hellenism which gives bonuses to conversion speed among other things]*  

That’s all from me today! I’ll leave you with a heartfelt parting quote from Catullus: *Frater ave, atque vale.* “Goodbye, brother, and fare well.”  

---

### The 4th (more or less) Crusade (sort of)​

*[CM’s Note: This section contains a lot of spoilers for the 4th Crusade mechanics. If you’re bothered by that, then please skip ahead to the next section! (ctrl+f -> "rageair")]*  


#### ​

#### Who Thought Doing This Was a Good Idea?​

Uh… the 4th Crusade? God. God willed it, duh. God was so into it. And besides Him, there was the Marquis de Montferrat, Mathieu de Montmorency, Pierre de Bracieux, and many others. Maybe the Doge of Venice masterminded the whole debacle (if CK2 is to be believed)?  

As far as CK3 content is concerned… I guess I’m the Doge, the architect of our lurid misadventure. My name’s Jason and I’m the most hydrated designer on CK3.  

I started work on the Fourth(ish) Crusade as something small and simple. But — and no one could have seen this coming — the subject matter proved a little complex. And a little dramatic. It seemed to merit a whole hullabaloo.  

So the Fourth Crusade in CK will happen regularly and it absolutely will prove a great and terrible threat to the Byzantine Empire. The Mongols are an apocalypse for all the world; the Latins are an apocalypse to the Greeks. Their empire stands tall, crumbles or is succeeded by some hideous aberration based on whether this strange fight is won or lost.  

![image-10.jpg](https://forumcontent.paradoxplaza.com/public/1173867/image-10.jpg "image-10.jpg")


*[Later artwork of the siege of Constantinople.]*  

#### Historical Brief​

In 1202, Catholic lords and knights began gathering to retake Jerusalem in a new Crusade. A number of these western crusaders chose Venice as their setting-off point. This involved a good bit of sitting and waiting for their fellow lords to show, and it soon became apparent few others were coming. But the Venetians still had to be paid in full.  

The first repayment effort involved sacking the Dalmation port of Zara, and staining their righteous swords in Christian blood. There, the Crusaders were joined by the Marquis of Montferrat and, with him, a claimant to the Byzantine throne, Alexios IV Angelos.  

Still low on funds, the Crusaders accepted an offer from this claimant: he promised them lavish support, money and troops for the holy cause, if the Crusaders could install him on his rightful throne. Though some dissenters instead departed directly for Jerusalem, the rest of the knights got onboard for Constantinople.  

Emperor Alexios III Angelos (who has the same name as the other Greek, yup) failed to fight these foreigners off. He was forced to abdicate in favor of the pilgrims’ claimant. The new Emperor Alexios, however, seeing the impossibility of making good on his promises to the Crusaders, reneged on their deal. The capital was stormed and he, overthrown.  

![image-11.jpg](https://forumcontent.paradoxplaza.com/public/1173868/image-11.jpg "image-11.jpg")


*[Now this is one salty mosaic.]*  

Yet another Emperor Alexios would soon meet the same fate and, after that, Constantinople was truly and historically ravaged by the Latin crusaders. When the pillaging and slaughter was over, so too was the Byzantine Empire. At least, for a time.  

The sort-of Crusaders named their own Latin Emperor, divided newly-won Byzantine territories amongst themselves, and set about the business of establishing their rule.  

I really recommend Geoffroi de Villehardouin’s description of these events. His is a rare medieval firsthand account, as he was one of the Crusader leaders. It offers such a fresh, direct, farm-to-table kind of bias.  

#### Interpreting this Mess into CK​

Well… this is one of those cases where gamefying history means sort-of choosing a narrative; it, too, means truncating events somewhat. *And* — adding a bit of dynamism, as suits the sandbox of CK3.  

Jason, you ask — will the Fourth Crusade happen around 1202?  
No. It *is* most likely to happen from the 1178 start date (and, fair warning, can happen very promptly), but it’s possible from other start dates, though only once the Catholics are onto their second (or later) Crusade.  

Well, it’s the Fourth Crusade though…  
Not necessarily, not in-game. We’re not adding a counter that permits this story only once the # of Crusades = 4. No. In game, this is referred to as the “Crusader War for Imperial Claim” or the “Splintered Crusade.” It was hard to come up with a nice-sounding term that actually fit, I’ll be honest.  

The dynamism of when this thing will strike is matched by it having relatively open ownership. You don’t have to play the Marquis de Montferrat to introduce a wannabe-Byzantine Emperor to some Crusaders; you can be pretty much any European Catholic ruler who has a relation to one such claimant at the right moment.  

This has kinda tipped our hand: the “leader” of the Splintered Crusade will be the above-named champion of the Byzantine aspirant. Putting this character at the helm centralizes authority over the Latin Crusaders more than is historical, yes, but it’s a big plus for playability and agency.  

Oh, and the Splintered Crusade? It isn’t actually a Crusade. This thing is a big, fat, ugly limpet sucking off the underbelly of a proper Catholic Crusade.  

Let’s get into that.  

#### A Great and Pious Venture! - The Latin Perspective​

It begins with a Catholic Crusade against lands east of the Mediterranean. Sure, there’s a Christian Byzantine Emperor, but he’s not involved in this Catholic initiative. Everything seems normal… and then some paltry little Catholic lord is hit with this:  

![image-12.png](https://forumcontent.paradoxplaza.com/public/1173869/image-12.png "image-12.png")


*[A sudden flash of purple: the opening event for the Splintered Crusade]*  

YOU OPT IN AND SHIT IS GONNA GO DOWN.  

JUST NOT RIGHT AWAY. As you wait for the Crusade (that you will, at least temporarily, bail from) to launch, you’re waiting to see who in Christendom is down to say “You son of a Byz! I’m in.”  

The Pope is first to weigh in.  

![image-13.png](https://forumcontent.paradoxplaza.com/public/1173870/image-13.png "image-13.png")


*[The Pope’s letter to his most misguided crusader.]*  

This story would be incomplete without an avaricious financier, and Venice — or the most Venice-y ruler available — fills that role.  

![image-14.png](https://forumcontent.paradoxplaza.com/public/1173871/image-14.png "image-14.png")


*[Your financier goes all in.]*  

As the months pass, other Catholics pledged to the Crusade will instead pledge to join you. And then the Crusade is launched, robbed of your confederates! Y’all set off on a war of your own.  

![image-15.png](https://forumcontent.paradoxplaza.com/public/1173872/image-15.png "image-15.png")


*[The Crusader War for Imperial Claim begins.]*  

The Byzantine Emperor will be fairly outnumbered, but all he needs to do is repel his attackers and this will be ended.  

If he fails, though…  

![image-16.png](https://forumcontent.paradoxplaza.com/public/1173873/image-16.png "image-16.png")


*[The victorious crusaders must deal with their new emperor.]*  

Your claimant may choose to bankrupt the empire in order to properly pay off every Crusader. More often than not, though, he’ll simply offer you a bribe to leave in peace. You can accept, of course, and may then even perhaps join the proper Crusade with your well-earned reinforcements (if it isn’t too late).  

Is anyone really going to leave in peace, though…?  

![image-17.png](https://forumcontent.paradoxplaza.com/public/1173874/image-17.png "image-17.png")


*[It’s Latin Empire time, baby. And it isn’t pretty.]*  

Unlike in a normal Crusade, you can choose to leave your old realm behind and gain the newly-made Latin Empire title yourself. Or you can give it to a relative. Or maybe you’ll reward that kind old selflessly helpful Venice fella, just as the historical crusaders almost did.  

Below the Latin Empire title, are Greek duchies and counties distributed among the most powerful crusaders. These rulers choose new holders for their assigned title much as the Latin Emperor is chosen.  

![image-18.png](https://forumcontent.paradoxplaza.com/public/1173875/image-18.png "image-18.png")


*[Bye bye, Byzantium.]*  

![image-19.png](https://forumcontent.paradoxplaza.com/public/1173876/image-19.png "image-19.png")


*[Whoomp! (There It Is)]*  

The Latin Empire is born; Byzantium dies. Though not cleanly, and not all at once. The collapse is scripted to prefer historicity, but it happens dynamically. The capital kingdom of the (now destroyed) Byzantine empire will go to the Latins. The Venetian Stato da Màr claims some Byzantine maritime holdings. Yet most of the Greeks do not bow to Latin dominion: some mighty governors become Administrative kings, while lesser magistrates claim feudal independence.  

A Crusader trait for these first Latin lords wouldn’t be quite right. They get a new one called Despoiler of Byzantium instead, and it also makes their AI personality aggressive as hell.  

![image-20.png](https://forumcontent.paradoxplaza.com/public/1173877/image-20.png "image-20.png")


*[The new, rare and shiny Despoiler of Byzantium trait.]*  

But how does this all look to an unsuspecting Greek…?  


#### ​

#### A Calamity of Fools! - The Byzantine Perspective​

*SWEET GOD IN HEAVEN, THE FUCKING LATINS ARE-*  

I’m getting ahead of myself.  

The Byzantine Emperor is the first to learn of the threat to come, and is given over a year to adequately gird his loins. For the rest of the empire, the cult of Rome strikes rather more suddenly.  

![image-21.png](https://forumcontent.paradoxplaza.com/public/1173878/image-21.png "image-21.png")


*[The Byzantine flavor on this war declaration does read just a bit different.]*  

Then, if the foreign invaders aren’t repelled…  

![image-22.png](https://forumcontent.paradoxplaza.com/public/1173879/image-22.png "image-22.png")


*[The news from Constantinople isn’t exactly good.]*  

This is right as everything in Byzantium is falling apart. If you’re powerful enough, you can now seize the title of Despot (king), and remain administrative. Otherwise, keeping your estate will mean pledging to another soon-to-be Despot. Your alternative is goin’ back to feudal. And landless house heads? They should find themselves under one of the new Greek Despots.  

In sum: their empire is a wreck, but this isn’t game over for the Greeks. The world marches on.  

#### Frankokratia: ‘The Rule of the Franks’​

The brief, tumultuous age of Latin rule in Greek lands was referred to as such.  

The Latin Emperor faces some interesting choices in the early days of rule.  

![image-23.png](https://forumcontent.paradoxplaza.com/public/1173880/image-23.png "image-23.png")


*[The Venetians offer a quid pro quo.]*  

![image-24.png](https://forumcontent.paradoxplaza.com/public/1173881/image-24.png "image-24.png")


*[The Greeks suggest the Latin Emperor become… Administrative?!?]*  

In order to achieve maximum CK3 turmoil, the fall of Byzantium unlocks a new CB everywhere in the empire: Seize Imperial Duchy. For, in this age of uncertain aftermath, any who possess Byzantine de jure land can lay claim to other such titles.  

![image-25.png](https://forumcontent.paradoxplaza.com/public/1173882/image-25.png "image-25.png")


*[The Latin Emperor uses Seize Imperial Duchy to expand his realm.]*  

And, in a broken realm haunted by armed hosts, earning victory attracts armies to your banner! This should help stronger Latins, Turks and Greeks in the region push their way to dominance.  

But what is de facto dominance without de jure righteousness?  

![image-26.png](https://forumcontent.paradoxplaza.com/public/1173883/image-26.png "image-26.png")


*[Legitimize Latin Dominion Decision.]*  

Latin Emperors of sufficient legitimacy have a unique decision that lets them claim the kingdoms of Byzantium and the hearts of the Greeks, one by one.  

![image-27.png](https://forumcontent.paradoxplaza.com/public/1173884/image-27.png "image-27.png")


*[Expunge Latin Dominion Decision.]*  

And the Byzantines, when/if they manage a comeback, can claw their kingdom titles back. Should they retake Constantinople and establish themselves well enough — the Restore the Byzantine Empire Decision gives the Greeks a pretty easy means to scrub all this nonsense out.  

But y’know, probably just in time for the Ayyubids or the Mongols or the Ottomans or someone else to wipe them out for good.  

*Kýrie, eléison* ![:(](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Frown    :(")  

---

### Historical Characters ​

Greetings! [@rageair](https://forum.paradoxplaza.com/forum/members/375731/) here with a small feature coming in the free update.  

Something I’ve felt the absence of for a long time are certain historical figures appearing as the game progresses. I’m not talking about the likes of Frederick Barbarossa or Mansa Musa - rulers and their kin are simulated with vast branching dynastic trees, divergences here are core to the game! No, I’m talking about the great poets, scientists, scholars, commanders, and tricksters of history - those without a lineage of nobility to back them up.  

In the update following Roads to Power you will see certain well-known historical figures appear across the map, which you can employ - or in case you own RtP - set out on an adventure as!  

![image-28.png](https://forumcontent.paradoxplaza.com/public/1173885/image-28.png "image-28.png")


*[Hildegard von Bingen - everyone’s favorite eccentric nun!]*  

Characters will appear in their historical place of birth (or our best approximation), Hildegard will appear in the barony of Worms, for example. By default you will only be notified if they appear in your Domain or if they are extremely well known (and you are the liege of any vassal holding the barony) - this can be altered via game rules, should you wish.  

![image-29.png](https://forumcontent.paradoxplaza.com/public/1173886/image-29.png "image-29.png")


*[Game Rule controlling how Historical Characters spawn]*  

Now, it’s no fun if these historical characters are too static! After all, no two games of CK are the same, and in one game the barony of Worms might be… of the Ibadi faith and Baranis culture, for example, who knows! In any case, for most characters (who don’t fall into the category of a specific religious minority or proponent) they will adapt to the faith/culture of their place of birth. As an example, here’s Hildegard again, but with the setup mentioned above.  

![image-30.png](https://forumcontent.paradoxplaza.com/public/1173887/image-30.png "image-30.png")


*[Hildegard, in case the barony of Worms was Ibadi and Baranis]*  

All historical characters spawned this way (not historical landed rulers, I’m afraid) have a snippet of information attached to them, explaining who they were in real-life. This snippet can be accessed from a widget near their opinion, and from their ‘Historical Character’-trait. Of course, the destiny that they’ll have in your game is almost always going to differ from their historical one, but it’s fun to compare with nonetheless!  

![image-31.png](https://forumcontent.paradoxplaza.com/public/1173888/image-31.png "image-31.png")


*[Thomas Aquinas also spawns with a Book inspiration - unfortunately we didn’t have time to hook in historical book titles, so they remain random, alas]*  

The trait helps you find them via the character finder, should you desire to see who’s around, and what they’re up to! I like to use it in order to invite them and land them as my vassals…  

![image-32.png](https://forumcontent.paradoxplaza.com/public/1173889/image-32.png "image-32.png")


*[The trait allows for easy searching]*  

If you’re lucky enough to have one of these characters spawn in your realm, you have three options:  

![image-33.png](https://forumcontent.paradoxplaza.com/public/1173890/image-33.png "image-33.png")


*[William Wallace - Illustrating the options]*  

You can choose to ignore them, should you not be in need of their services - or you can employ them and get an obligation hook. As mentioned, you can also abandon your dynasty and set out on an adventure as them - the only time in CK3 where I think it’s fair to do so, because it’s just too cool to be able to go on an adventure as someone like William Wallace or Ibn Battuta, and it would be a crime not to offer you that opportunity!  

![image-34.png](https://forumcontent.paradoxplaza.com/public/1173891/image-34.png "image-34.png")


*[Ibn Battuta will set out on adventure if dismissed, as he did historically!]*  

As the Expansion focuses on Byzantium, I took extra care to add every interesting character that I could for Byzantium and their surroundings, which does mean that an extraordinary amount of characters will appear in constantinople. At the start of 1066, no less than two well-known figures will make their appearance within a year or so…  

![image-35.png](https://forumcontent.paradoxplaza.com/public/1173892/image-35.png "image-35.png")


*[Michael the Stammerer was technically already at court in 1066, so his text mentions that he ‘made a name for himself at court’, rather than ‘wandering my realm’!]*  

![image-36.png](https://forumcontent.paradoxplaza.com/public/1173893/image-36.png "image-36.png")


*[Joseph is very useful in fighting the Seljuks, indeed]*  

We tried to add as many interesting historical characters as we could to this new system, and we ended up with exactly(!) 100 of them, spanning most of the map! There are many very well-known figures, and some that are more obscure but that I’m sure will pique your interest when you see them. Here’s a sample of some of them:  

![image-37.png](https://forumcontent.paradoxplaza.com/public/1173894/image-37.png "image-37.png")


*[Omar Khayyam will also appear close to the 1066 start date]*  

![image-38.png](https://forumcontent.paradoxplaza.com/public/1173895/image-38.png "image-38.png")


*[Perhaps you’d like to set out on a real journey as the famous Dante Alighieri?]*  

![image-39.png](https://forumcontent.paradoxplaza.com/public/1173896/image-39.png "image-39.png")


*[Or maybe you’d like to literally take Ockham’s razor to the throat of your enemies?]*  

![image-40.png](https://forumcontent.paradoxplaza.com/public/1173897/image-40.png "image-40.png")


*[This somewhat controversial pair will appear as lovers, and if you set out on an adventure as Heloise, Peter will join you!]*  

![image-41.png](https://forumcontent.paradoxplaza.com/public/1173898/image-41.png "image-41.png")


*[You didn’t think we’d forget about the Norse, did you? Snorri here is the author of most of what we know about norse mythology today.]*  

![image-42.png](https://forumcontent.paradoxplaza.com/public/1173899/image-42.png "image-42.png")


*[Many famous Jewish personalities, such as Rashi here, will appear across the map]*  

![image-43.png](https://forumcontent.paradoxplaza.com/public/1173900/image-43.png "image-43.png")


*[And we’re not forgetting about India! Here’s Vidyapati, one of the most famous poets and scholars of the area.]*  

![image-44.png](https://forumcontent.paradoxplaza.com/public/1173902/image-44.png "image-44.png")


*[Rumi hails from a non-Persian area in Anatolia, and instead of appearing Greek or Turkish will take his faith and culture from Balkh, as a compromise! Several historical characters hail from one place but take their faith/culture from another.]*  

![image-45.png](https://forumcontent.paradoxplaza.com/public/1173903/image-45.png "image-45.png")


*[Alright alright, not all of the characters are 100% historically verifiable like Jangar here, but if they could have existed and are interesting enough - why not!]*  

![image-46.png](https://forumcontent.paradoxplaza.com/public/1173904/image-46.png "image-46.png")


*[And some most certainly existed, but their stories were embellished over the centuries. Anyone from Turkey here who recognizes this funny fellow?]*  

![image-47.png](https://forumcontent.paradoxplaza.com/public/1173905/image-47.png "image-47.png")


*[You might be familiar with a character named Varys who is a very influential eunuch from a certain popular franchise - John here is the real-life inspiration for that character!]*  

As mentioned above we’ve added a hundred characters (technically 101 but Héloïse d'Argenteuil & Peter Abelard is a package deal!), and here’s the full list (not in chronological order!)  

Karunakara Tondaiman  
Sekkilhar  
Omar Khayyam  
Bhaskaracharya  
Joseph Rabban  
Atisha  
Hemachandra  
Kshemendra  
Akka Mahadevi  
Namdev  
Madhvacharya  
Vidyapati  
Abhinavagupta  
Basava  
Hildegard von Bingen  
Thomas Aquinas  
Dante Alighieri  
Thomas Becket  
Maimonides (Moses ben Maimon)  
Chrétien de Troyes  
Egil Skallagrímsson  
Gunnlaug Ormstunga  
Þorbjörg the Seeress  
Erik Röde  
Ibn al-Haytham (Alhazen)  
Ibn Battuta  
William of Ockham  
Geoffrey Chaucer  
Roger Bacon  
Aaron of Lincoln  
John Wycliffe  
Héloïse d'Argenteuil & Peter Abelard  
Petrarch (Francesco Petrarca)  
Giotto di Bondone  
Leonardo Fibonacci  
Giovanni Boccaccio  
Christine de Pizan  
Snorri Sturluson  
Hrotsvitha  
Ramanuja  
Arnaldus de Villa Nova  
Ibn Khaldun  
Jalaluddin Rumi  
Avicenna  
Averroes  
Al-Biruni  
Rashi (Shlomo Yitzchaki)  
Yehuda Halevi  
Hasdai ibn Shaprut  
Levi ben Gershon (Gersonides)  
Abraham ibn Ezra  
Solomon ibn Gabirol  
Nachmanides (Moses ben Nahman)  
Hasdai Crescas  
Saadia Gaon  
Yusuf ibn 'Awkal  
Benjamin of Tudela  
Marco Polo  
Bridget of Sweden  
Johannes Eckhart (Meister Eckhart)  
Jangar  
Zawisza Czarny  
Theophanes the Greek  
Nicetas Choniates  
Michael Psellos  
John Tzetzes  
Theophylact of Ohrid  
Eustathius of Thessalonica  
Nicephorus Blemmydes  
Georgius Pachymeres  
Manuel Moschopoulos  
Theodore Metochites  
Michael Choniates  
Joseph Tarchaneiotes  
Gemistus Pletho  
Arethas of Caesarea  
Basil Lekapenos  
John the Orphanotrophos AKA totally who Varys is based on  
Samonas  
Peter the Eunuch  
Constantine the Paphlagonian  
Peter the Stratopedarches  
Basilios Bessarion  
Demetrios Kydones  
Manuel Holobolos  
John Axuch  
Mkhitar Gosh  
Shota Rustaveli  
Grigor Tatevatsi  
Sargis Pitsak  
Averardo de' Medici  
Alfonso de Borgia  
William Wallace  
La Hire (Étienne de Vignolles)  
Rabban Bar Sauma  
Nasreddin Hodja  
Widukind of Corvey  
Roger de Flor  
Regino of Prüm  
Geoffrey of Monmouth  


---

That’s all we have for this week! As always, thanks for your time and attention.  

We’ll be back next week to discuss the details of the new Scheme system coming in the Free Update releasing alongside Roads to Power. Until then, if you have any questions or feedback, feel free to leave them in the replies and we’ll do our best to address them.

<!-- artifact:reactions:start -->
- 111 Like
- 94 Love
- 13 (unlabeled — rendered as base64 data URI)
- 9 (unlabeled — rendered as base64 data URI)
- 2 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)**
Role: Community Manager
Badges: 102
Messages: 642
Reaction score: 17,753
<!-- artifact:op_signature:end -->
