---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1386925/"
forum_thread_id: 1386925
content_type: reply_thread
parent_dd_file: dd_024_2020-04-28_fervor-religious-hostility-and-doctrine.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 24
title: "Dev Diary #24 - Fervor, Religious Hostility, and Doctrine Showcase"
dd_date: 2020-04-28
expansion: Base game
patch: Crusader Kings III
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 13
reply_count: 249
participant_count: 109
reply_date_first: 2020-04-28
reply_date_last: 2020-06-08
body_word_count: 18626
inline_image_count: 0
quoted_span_count: 205
extraction_rationale: |
  Full reply thread captured live via Claude in Chrome (article.message bodies).
  Quote blocks split into artifact:quote spans and excluded from word counts.
  Usernames replaced by stable per-thread participant ids; the dev-diary OP is
  excluded (see parent_dd_file).
notes_for_analyst: |
  Community-voice counterpart to the linked dev diary. Strip YAML + artifact
  comments before tokenizing, exactly as for dd_*.md.
---

# Reply thread — Dev Diary #24 - Fervor, Religious Hostility, and Doctrine Showcase

*249 replies from 109 participants across 13 pages*

## Reply 1 — participant_001 · 2020-04-28 · post-26529967

My lord this looks good. Just a tiny bit worried that at the end of a game the entire world will just be a hodgepodge of different heresies and new religions. Feels like it would be tricky to balance with the systems explained. Will there be dominant religions still if the fevor can be so fluctuating?

## Reply 2 — participant_002 · 2020-04-28 · post-26529968

Interesting. In the final screenshot why are some tenets hatched out? Are these already chosen, or somehow unavailable? Is there any way to change the religious hostility value in game without changing tenets? Could you in some fashion manage to make Catholics and Orthodox consider each other "Righteous", and thus co-valid paths to salvation? (Maybe as a first step in an eventual "mend the schism" pathway for future use?)

## Reply 3 — participant_003 · 2020-04-28 · post-26529991

How many doctrines can a religion have? 4 as seen for Catholicism? Do you "add" them to a new religion the same way as tenets, or does you religion just "inherit" them from its "parent"? I think having doctrines and tenets be so separate, while largely doing the same thing is very confusing. So far Catholicism has the tenets of "Armed Pilgrimages", "Communion" and "Monasticism" and the doctrines of "Male Dominated", "Righteous", "Theocratic" and "Ecumenism".

## Reply 4 — participant_004 · 2020-04-28 · post-26529992

Out of curiosity, why is pope wearing gloves? EDIT: It was a simple joke question for artists, calm down.

## Reply 5 — participant_005 · 2020-04-28 · post-26529995

I have some questions about religion: 1. Is there a doctrine for how the Religious Head is chosen? For example, if it uses a College of Cardinals or another way of appointing him. 2. What does the Clerical function Clergy Doctrine do? For example we saw that Catholic Clergy's function was "Control". What does that mean? 3. What does the "Teachings of Jesus" doctrine do? 4. How does the Witchcraft Crime doctrine apply to Abrahamic and Pagan faiths?

## Reply 6 — participant_006 · 2020-04-28 · post-26530001

Great update! A few questions: 1. Do the greyed out tenets in the last screenshot mean they cannot be selected for whatever reason? 2. Does having no religious head make your fervor less volatile or does it default to being based off your realm court chaplain's traits? 3. How is Mending the Schism treated with these mechanics? 4. Is it possible to create a faith that is considered righteous by the parent faith but is still distinct? For example can I have a Church of France that is considered to be in Full Communion with the Pope in Rome? 5. Speaking of the Pope in Rome, is it possible for multiple religions to have the same religious head? Can the Pope be head of Catholicism and also Irish Insular Christianity? Or perhaps for the Kharjites to accept the Caliph in Baghdad as the true Caliph (as they did consider some of the Caliphs to be the rightful leader of the ummah)

## Reply 7 — participant_007 · 2020-04-28 · post-26530012

nice stuff. What next DD will be about?

## Reply 8 — participant_008 · 2020-04-28 · post-26530014

Excellent work, thanks yet again ! Anyway, does that mean that religious hostility is not dynamic ?

## Reply 9 — participant_009 · 2020-04-28 · post-26530018

Will fervor be a map encompassing thing for that entire faith? Or is there any chance we might have more localized fervor / moral authority? One of the things that I loved / hated about moral authority was how universal and trans-continental it was. One of my favorite things to do was what I called 'the match of the Irish.' Where you would start in tribal Ireland as a Catholic. And you would pick your duchy / lands in Ireland, and then just burn down the rest. You as a Catholic Irish tribal can just burn down your own churches both in Ireland and England, and eventually widdle the moral authority down to the point where heresies would start popping up. Now I see the heresy system is different and looks better. But the reality was in CK2 once you got that ball rolling, the heresies just snow balled and you could literally just burn Europe to the ground in heresy uprisings just raiding from Ireland. So is moral authority still one value, or is there any sort of local aspect to it? Where like if some Irish dude is burning down churches, that doesn't make me in Italy less likely to convet.

## Reply 10 — participant_010 · 2020-04-28 · post-26530020

<!-- artifact:quote:start -->
> Nefertem said: Just a tiny bit worried that at the end of a game the entire world will just be a hodgepodge of different heresies and new religions. Feels like it would be tricky to balance with the systems explained. Will there be dominant religions still if the fevor can be so fluctuating? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> DreadLindwyrm said: Interesting. In the final screenshot why are some tenets hatched out? Are these already chosen, or somehow unavailable? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Is there any way to change the religious hostility value in game without changing tenets? Could you in some fashion manage to make Catholics and Orthodox consider each other "Righteous", and thus co-valid paths to salvation? (Maybe as a first step in an eventual "mend the schism" pathway for future use?) Click to expand...
<!-- artifact:quote:end -->
We have the AI play automated games every night, and the 'big' faiths like Catholicism and Ash'ari generally remain quite powerful. Even though they regularly suffer from heresy outbreaks, their sheer bulk and military might means they almost always end up re-asserting themselves as a dominant power. Unavailable due to being incompatible with currently selected Tenets/Doctrines. Switching the blocking Doctrine out for something else will enable them to be chosen. You need to use either a Tenet or a Doctrine to change religious hostility. Either option works just as well; Ecumenism is a Doctrine for example, while Christian Syncretism is a Tenet. Currently only Gnostics are able to achieve a Righteous view of other Faiths, but mods can change or expand upon this to enable schism reformations and the like without too much trouble.

## Reply 11 — participant_002 · 2020-04-28 · post-26530030

<!-- artifact:quote:start -->
> King Anund said: I have some questions about religion: 1. Is there a doctrine for how the Religious Head is chosen? For example, if it uses a College of Cardinals or another way of appointing him. Click to expand...
<!-- artifact:quote:end -->
I think this is covered by one of the Main Doctrines. Catholics get "Theocratic". It might also be handled through a "Head of Faith" doctrine as shown in DD 20.

## Reply 12 — participant_011 · 2020-04-28 · post-26530034

Esoteric Education?? Is this a new type of child education or just a new name for a Learning based education? Reincarnation , Sun Worship, Auspicious Birthright !?! Players are going to going full piety to form all sorts of new Faiths when the game is released.

## Reply 13 — participant_012 · 2020-04-28 · post-26530038

I like the idea that stabilized religion will lose fervor. It makes sense. Now if Christianity will rise to power and completely swallow Islam, they probably won't be almost global faith, because heresies will race in Muslim's stead. It seems interesting

## Reply 14 — participant_010 · 2020-04-28 · post-26530041

<!-- artifact:quote:start -->
> Asiak said: Will fervor be a map encompassing thing for that entire faith? Or is there any chance we might have more localized fervor / moral authority? Click to expand...
<!-- artifact:quote:end -->
Fervor is global for the entire Faith. However, the more dynamic nature of the Fervor system means that Faiths simply won't end up in the 'heresy death-spiral' that CK2 had, since Fervor will jump back up after an outbreak and give the original Faith some breathing room to recover and deal with the heretics.

## Reply 15 — participant_013 · 2020-04-28 · post-26530050

I think that making holy wars cost fervor to declare and giving the target a fervor bonus when they lose is a really good change. It will hopefully prevent situations typical for CK2, where one faith sits at a permanent 100 MA for winning a lot of holy wars, and every other religion falls into a death spiral of low MA. It also means that you can no longer use holy wars as a basically free CB for grabbing unlimited land. I am curious how the faith hostility system will play out in practice, but it does seem to differentiate the three religious families from each other significantly, which I appreciate.

## Reply 16 — participant_014 · 2020-04-28 · post-26530072

A triumphant faith losing fervor makes no sense in an era where success in war showed God’s favor and loss showed the opposite. This is a change that I really don’t like

## Reply 17 — participant_015 · 2020-04-28 · post-26530073

why only unreformed pagan? heresy outbreak looks like a good idea but not sure about only ruler can start it part was hoping sun worship give more then less desert attrition what are the actual effect of miracle worker?

## Reply 18 — participant_016 · 2020-04-28 · post-26530080

<!-- artifact:quote:start -->
> Baron von Shoes said: For starters, the Catholic, Orthodox, Apostolic, and Coptic Faiths all have the ‘Ecumenism’ Doctrine, which changes the Hostility of any other Faith with the same Doctrine to just ‘Astray’, thus allowing these Faiths to have cordial relations with each other. Click to expand...
<!-- artifact:quote:end -->
The new Fervor system sounds like a big improvement on the moral authority system, especially since it seems it will generally exist in a state of constant flux (keeping things spicy) and that bigger religions will suffer more from their own size and success over smaller local faiths (allowing for the survival of religious differences on the map). Is "Insular" going to have Ecumenism as well? People have pointed out how so-called "Celtic" Christianity (which I think is what "Insular" is trying to represent) was considered pretty much like a bunch of problematic Catholics that were slightly resistant to Rome's authority and had a few differences on doctrines (mostly minor stuff that got smoothed over time). I reckon that there should be either a "Righteous" or "Astray" relation between Insular and Roman Catholics (unless Insular is meant to represent something else).

## Reply 19 — participant_017 · 2020-04-28 · post-26530086

<!-- artifact:quote:start -->
> Baron von Shoes said: every Holy War declared will slightly damage a Faiths’ Fervor, while losing land to hostile Holy Wars will actually increase your Faith’s Fervor as the embattled faithful dig in and fight for their way of life Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Baron von Shoes said: this both protects the burgeoning Faith while simultaneously limiting its influence in distant lands. Click to expand...
<!-- artifact:quote:end -->
YES. Oh my God(s), finally. Having your faith threatened shouldn't weaken it immediately every time, it should make the adherents tighter in the defense of their faith, at least for some time. Finally no more snowball effect with heresies and holy wars. Good! No more random Lollards spreading in Britain, Germany, Italy and Portugal at the same time And OH MY LORD the doctrines and tenets. I absolutely love it, and I'm already starting to plan what I shall pick in my first campaign. I especially like the fact that most of them are not simple modifiers but actually influence gameplay, add events and new mechanics, change trait importance and so on. Lovely, lovely!

## Reply 20 — participant_018 · 2020-04-28 · post-26530095

The Astray-Hostile-Evil system seems very neat! Will it play a role in what rulers are able to offer to join a holy war? As in, Gnostics being able to help each other out since they're all considered Righteous, but Catholics helping Orthodox (and vice-versa) not so much, since they're only at "Astray" level.

## Reply 21 — participant_019 · 2020-04-28 · post-26530119

Im gonna be downvoted to hell, but i cant get over on how bad most of the character models look, it feels muddy, out of focus with weird proportions

## Reply 22 — participant_020 · 2020-04-28 · post-26530132

Great Dev Diary, Religion seems to be Ck3’s strongest selling point so far, but I have a few worries on something mentioned What are the relations between Armenians and Coptics? It should be Righteous as described in the dev diary since they were the same religion with different local leaders, Coptic Pope over Egypt, Armenian Catholicos over Armenia. Actually I don’t think even that would represent how close they are as a single religion, but I think a Righteous status at the very least would be the most accurate description of their relationship... if not righteous then what is their relationship? Otherwise great dev diary that continues to make the game more and more appealing.

## Reply 23 — participant_021 · 2020-04-28 · post-26530141

Does this > , they will become a heresiarch and start espousing the doctrines of a brand new Faith, which is typically (but not always), one from their Religion. Mean that, say, some heretic uprisings in, like, Greece for example will be Hellenic rather than christian? Like, where there is an associated dead faith, that joins the list of possible heresies in the area?

## Reply 24 — participant_022 · 2020-04-28 · post-26530143

If there are two gnostic faiths that would normally consider one another Astray, do they see each other as Righteous? I assume this is the case, but the tooltip makes this unclear

## Reply 25 — participant_023 · 2020-04-28 · post-26530158

Question: why are pagan faiths hostile to other pagan religions? Considering the nature of pagan religions wouldn't it be regarded as Astray instead. I don't think that the norse when settling in Russia / Ukraine were religiously hostile to the Slavic pagans.

## Reply 26 — participant_008 · 2020-04-28 · post-26530171

<!-- artifact:quote:start -->
> vyshan said: Question: why are pagan faiths hostile to other pagan religions? Considering the nature of pagan religions wouldn't it be regarded as Astray instead. I don't think that the norse when settling in Russia / Ukraine were religiously hostile to the Slavic pagans. Click to expand...
<!-- artifact:quote:end -->
Maybe some faiths will be in the same religion : slavic, norse, baltic could be together ; magyar and tengri too ; same for african pagan faiths

## Reply 27 — participant_024 · 2020-04-28 · post-26530204

What will the next dev diary be about?

## Reply 28 — participant_025 · 2020-04-28 · post-26530207

<!-- artifact:quote:start -->
> Baron von Shoes said: as a result, every Holy War declared will slightly damage a Faiths’ Fervor, Click to expand...
<!-- artifact:quote:end -->
As a mechanic, this is fine; it'll keep realms from exploiting Holy Wars for blobbing. As a representation of RL, I think it misses the mark: I'd imagine people's fervor would spike after a calling for an Holy War that would retrieve land and righteous believers from heathens. And even more if it's successful. When can we see the new units in detail, and is there going to be different types for the different culture groups?

## Reply 29 — participant_026 · 2020-04-28 · post-26530222

I think Holy Wars should give Fervor but only if you do not take the land for yourself. You should gain Fervor for giving the land to the pope.

## Reply 30 — participant_027 · 2020-04-28 · post-26530232

<!-- artifact:quote:start -->
> Baron von Shoes said: View attachment 571932 [A screenshot showing various Tenets of a more spiritual nature: Astrology, Auspicious Birthright, Reincarnation, Sun Worship, Sky Burials, and Esotericism] Click to expand...
<!-- artifact:quote:end -->
Esotericism and Auspicious Birthright are very interesting indeed. I assume an Esoteric Education will give a high likelihood of making the child one of Wise Man, Mystic, or Miracle Worker, at the expense of not being able to control other childhood traits. When are we getting a childhood education dev diary? The system clearly has one big change at the very least!

## Reply 31 — participant_028 · 2020-04-28 · post-26530239

A very interesting DD, but still, I guess I still have some questions. 1. Will organized religions actually be organized? Is there a church panel where players could see, influence and nominate religious leaders? 2. Can adherents of the same faith have different religious heads? (I will expand on this idea some day; hopefully it is not impossible to mod, since it requires adding another level beneath faiths) 3. Is there a breaking point for bonuses in Fervor when you lose a holy war? It seems strange for a faith to repeatedly lose land ... yet be more and more self-justified.

## Reply 32 — participant_029 · 2020-04-28 · post-26530248

<!-- artifact:quote:start -->
> halbort said: I think Holy Wars should give Fervor but only if you do not take the land for yourself. You should gain Fervor for giving the land to the pope. Click to expand...
<!-- artifact:quote:end -->
I don't think that really happened though. Maybe you can avoid the fervor loss by setting up a new kingdom of the religion but you lose fervor if it really is just a land grab? Each Holy War could have an associated candidate, similar to the current crusades mechanic in ck2

## Reply 33 — participant_030 · 2020-04-28 · post-26530249

Interesting indeed, a shame that the religious opinion system seems rather static instead of dynamic though.

## Reply 34 — participant_031 · 2020-04-28 · post-26530256

It seems a really off to have astrology give naval speed implying a link to celestial navigation. Astronomy is a science and completely distinct from astrology. Sure many astronomers during the time period were also astrologers, but many other medieval astronomers thought such practices were heretical.

## Reply 35 — participant_032 · 2020-04-28 · post-26530261

Praise the sun! Zunists are confirmed, that is great news.

## Reply 36 — participant_033 · 2020-04-28 · post-26530264

<!-- artifact:quote:start -->
> Baron von Shoes said: they will become a heresiarch and start espousing the doctrines of a brand new Faith, which is typically (but not always), one from their Religion. Click to expand...
<!-- artifact:quote:end -->
"Well, Catholicism isn't all it's cracked up to be, time to become a Qarmatian."

## Reply 37 — participant_034 · 2020-04-28 · post-26530276

<!-- artifact:quote:start -->
> viola said: Is "Insular" going to have Ecumenism as well? People have pointed out how so-called "Celtic" Christianity (which I think is what "Insular" is trying to represent) was considered pretty much like a bunch of problematic Catholics that were slightly resistant to Rome's authority and had a few differences on doctrines (mostly minor stuff that got smoothed over time). I reckon that there should be either a "Righteous" or "Astray" relation between Insular and Roman Catholics (unless Insular is meant to represent something else). Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Gildas said: it has become a proverb far and wide, that the Britons are neither brave in war nor faithful in time of peace. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> vyshan said: Question: why are pagan faiths hostile to other pagan religions? Considering the nature of pagan religions wouldn't it be regarded as Astray instead. I don't think that the norse when settling in Russia / Ukraine were religiously hostile to the Slavic pagans. Click to expand...
<!-- artifact:quote:end -->
I think your understanding of the gameplay is mislead by the fact that the good Baron seems to have misread his own table: it says nothing about the relations between different Faiths of the same Religion. Insular and Catholicism will both be Faiths within the Christian Religion. So they're not in the table: I guess that means the default relationship between them is Astray? But I wholeheartedly agree that it makes no sense to have Catholics considering Insular Christians as further away than the Greeks. The Insular should surely have the Ecumenism Doctrine too. After all, they were so committed to Ecunemism that they basically negotiated away their future in northern England at the Synod of Whitby.... I also hope that Insular also needs to drop the 'Armed Pilgrimages' Tenet that Catholicism has. To quote an Insular Christian from a few centuries before the CKII era: There were plenty of brave British/Welsh warriors, but they spent too much time fighting each other and arguably not enough time fighting the pagans.... Old Norse religion is really not my thing, but weren't they largely tribal gods rather than universal gods?

## Reply 38 — participant_023 · 2020-04-28 · post-26530284

<!-- artifact:quote:start -->
> Despotism said: Praise the sun! Zunists are confirmed, that is great news. Click to expand...
<!-- artifact:quote:end -->
IIRC The Zun religion was more like the localized Hindu beliefs of the Zunbils. With the way CK3 is handling religion, which has broken up Hinduism itself, Zunism existing makes perfect sense. So another question for @Baron von Shoes What religious group is Zunism in? Eastern or Pagan. I hope that they are in Eastern.

## Reply 39 — participant_035 · 2020-04-28 · post-26530285

<!-- artifact:quote:start -->
> Baron von Shoes said: Heresy Outbreaks A heresy outbreak is what happens when a ruler becomes disillusioned with their current Faith and is swayed to join a different one. Click to expand...
<!-- artifact:quote:end -->
Question, If i'm right fervor is global to everyone ? If yes so every rulers from a religion can embrace a heresy outbreak when the fervor get too low ? So what's the difference between those who do and those who do not ? And one another question : Only righteous faiths call call each other to crusade and great holy war ?

## Reply 40 — participant_036 · 2020-04-28 · post-26530296

I spy Stonehenge and the Tower of London on the map. I wonder what other landmarks we will see and how they will function in the game. CKII's Stonehenge was a little silly.

## Reply 41 — participant_037 · 2020-04-28 · post-26530299

<!-- artifact:quote:start -->
> DreadLindwyrm said: Interesting. In the final screenshot why are some tenets hatched out? Are these already chosen, or somehow unavailable? Is there any way to change the religious hostility value in game without changing tenets? Could you in some fashion manage to make Catholics and Orthodox consider each other "Righteous", and thus co-valid paths to salvation? (Maybe as a first step in an eventual "mend the schism" pathway for future use?) Click to expand...
<!-- artifact:quote:end -->
I've asked question about the tenets being changeable for the same religion during the game. It won't be in the base game, but is planned to be added later on, so things like e.g. councils can reshape the doctrines. I suppose that's enough to make gradual drift apart or reconciliation between the Western and Eastern Christianity possible.

## Reply 42 — participant_038 · 2020-04-28 · post-26530305

I like the concept of fervor and I absolutely see the reasoning behind the holy wars change, however, does fervor lost this way have a cap of sorts ? In case of the absence of one I could imagine a situation where the Catholics reconquering the Mediterranean from the Muslims creates a great turmoil inside the Catholic world, leading people to doubt the church to be right and just, although the Christian God supposedly has just helped them in recovering long lost territories from their arguably biggest rivals. Which frankly doesn't make much sense in my opinion. Love the Dev Diary though. EDIT: And the faster the conquests the greater the turmoil which would be a bit counter-intuitive. People getting tired from constant "crusading" makes sense, but not people abandoning their religion for being too succesful.

## Reply 43 — participant_002 · 2020-04-28 · post-26530306

<!-- artifact:quote:start -->
> SeekTruthFromFx said: I think your understanding of the gameplay is mislead by the fact that the good Baron seems to have misread his own table: it says nothing about the relations between different Faiths of the same Religion. Insular and Catholicism will both be Faiths within the Christian Religion. So they're not in the table: I guess that means the default relationship between them is Astray? Click to expand...
<!-- artifact:quote:end -->
So, if you are Abrahamic (as Christians will be), and both same family/same religion (as different Christian faiths will be), you are looking at different faiths being "hostile" by default. Same family/same religion implies "Different faith" here.

## Reply 44 — participant_039 · 2020-04-28 · post-26530317

This looks great. EDITED: Like I've said before, when we get the proper Byzantium DLC, the creeds I will unleash will be glorious.

## Reply 45 — participant_040 · 2020-04-28 · post-26530318

If Catholic has the "ecumenic" trait, then an heresy having the ecumenic trait will be considered "just" astray? Also, it would be great if the tolérance of the religion groups was dynamic, too... But I guess that would be overcomplicated to implement, and I would not even know how it could be implemented...

## Reply 46 — participant_032 · 2020-04-28 · post-26530334

<!-- artifact:quote:start -->
> vyshan said: IIRC The Zun religion was more like the localized Hindu beliefs of the Zunbils. With the way CK3 is handling religion, which has broken up Hinduism itself, Zunism existing makes perfect sense. So another question for @Baron von Shoes What religious group is Zunism in? Eastern or Pagan. I hope that they are in Eastern. Click to expand...
<!-- artifact:quote:end -->
Well, I was not really worried about them being unable to create Zunism, so much as Zunism not being included since 867 seems to be the earliest start date they are going to have. I know Zunists were still around during 867, but not for much longer, so I was not sure if they would make the cut.

## Reply 47 — participant_027 · 2020-04-28 · post-26530336

<!-- artifact:quote:start -->
> Xain said: If Catholic has the "ecumenic" trait, then an heresy having the ecumenic trait will be considered "just" astray? Also, it would be great if the tolérance of the religion groups was dynamic, too... But I guess that would be overcomplicated to implement, and I would not even know how it could be implemented... Click to expand...
<!-- artifact:quote:end -->
Remember, heresies are simply different faiths of the same religion now. Catholicism and Orthodox are different faiths of the same religion, Chrisitanity, and do not get heresies specific to their faith, like they did in CK2.

## Reply 48 — participant_041 · 2020-04-28 · post-26530354

So about that Sun Worship doctrine, does that mean that Zunism will still exist in CK3’s 867 start date or will it be a dead faith by the time the game has started?

## Reply 49 — participant_042 · 2020-04-28 · post-26530356

Could you reveal which Pagan Religions (not the individual Faiths, just the Religions) are there?

## Reply 50 — participant_043 · 2020-04-28 · post-26530359

<!-- artifact:quote:start -->
> vyshan said: IIRC The Zun religion was more like the localized Hindu beliefs of the Zunbils. With the way CK3 is handling religion, which has broken up Hinduism itself, Zunism existing makes perfect sense. So another question for @Baron von Shoes What religious group is Zunism in? Eastern or Pagan. I hope that they are in Eastern. Click to expand...
<!-- artifact:quote:end -->
Technically speaking, Zunism isn't simply a localized variant of Hinduism. The worship of Zun has its roots in Hepthalite paganism, but Zunism was heavily influenced by Shaivist and Suryanite Hinduism, and to a lesser extent by other surrounding religions like Buddhism, Zoroastrianism, and local Indo-Iranian polytheistic traditions.

## Reply 51 — participant_002 · 2020-04-28 · post-26530360

<!-- artifact:quote:start -->
> Xain said: If Catholic has the "ecumenic" trait, then an heresy having the ecumenic trait will be considered "just" astray? Also, it would be great if the tolérance of the religion groups was dynamic, too... But I guess that would be overcomplicated to implement, and I would not even know how it could be implemented... Click to expand...
<!-- artifact:quote:end -->
It could eventually be done by having a "base" value for relations between faiths, with relations outside of the base value decaying towards the base, with ecumenicism and gnosticism (and similar traits) changing the base. You could then have numbers of similar/identical traits affect the decay rate or provide a boost/penalty to the value you trend towards. So : if you'd consider the other faith "evil", the base might be -100. If you consider them "hostile" it might be 0, If you consider them astray it might be +100, if you consider them righteous it might be +200. You then have various things alter this, much like the relationship counter between empires/characters in other games. However it'd be based on the faiths' attitudes and similarities rather than any one character's traits. This would be *somewhat* more complicated, admittedly, and would be worth being the core of a later mechanical change.

## Reply 52 — participant_044 · 2020-04-28 · post-26530371

Whats the next Dev Diary going to be about?

## Reply 53 — participant_045 · 2020-04-28 · post-26530402

Only one question. Will Popes who wrongfully Excommunicate good Catholic Rulers-either on their own, or at the behest of other Rulers-still get free passes like they do in CK2?

## Reply 54 — participant_046 · 2020-04-28 · post-26530405

This looks like such a great system. Really excited for this. I was skeptical about whether CK3 would really be much of an improvement over CK2, but this is the first game system where I legitimately feel like continuing to play 2 will be unrewarding now that I know how 3 works (I'll still play 2 for a long time though, I'm sure).

## Reply 55 — participant_047 · 2020-04-28 · post-26530406

Tell me more about esotericism, wise men, miracle workers and mystics pllleeeaaaassseeeee.

## Reply 56 — participant_048 · 2020-04-28 · post-26530429

The Pope is cought with his pants down, what do you do? Option 4: Abolish the Papacy and begin the Renaissance centuries earlier. (Suicidally difficult, savescum for best results) Option 5: Abolish the Papacy and restore the Pentarchy (You kids like to be OP too much)

## Reply 57 — participant_049 · 2020-04-28 · post-26530445

Well, I like this dev diary more than the last one (which in my mind created more questions than solved). I like the 4 opinions with the faiths, but I would love a more dynamic approach to that (and maybe a fifth one between astray and hostile). The build up of frevor is so much better than the moral authority of CK2. Either catholicism or the muslim religions had an enormous downfall after losing some holy wars through heresies and this changes the picture.

## Reply 58 — participant_050 · 2020-04-28 · post-26530456

<!-- artifact:quote:start -->
> Eltener said: It seems a really off to have astrology give naval speed implying a link to celestial navigation. Astronomy is a science and completely distinct from astrology. Sure many astronomers during the time period were also astrologers, but many other medieval astronomers thought such practices were heretical. Click to expand...
<!-- artifact:quote:end -->
Was the astrology-astronomy dichotomy even a thing at this point?

## Reply 59 — participant_051 · 2020-04-28 · post-26530463

Can we have an event in which a sinful pope is murdered by his lover´s spouse?

## Reply 60 — participant_014 · 2020-04-28 · post-26530467

People can "respectfully disagree" with my comment, but no one seems to have an actual argument that they're posting - when in real life did a religion winning wars against other faiths make its adherents less fervent in their faith, and when did losing make them more fervent? How could you say the first crusade weakened Catholicism and made heresies more likely to pop up? How can you say that Zoroastrians being wiped out made them stronger when in fact their religion collapsed more than ever? It's a nonsensical mechanic. I get why it's implemented, you don't want snowballing and you want it to be harder to wipe out faiths like Catholicism or Sunni Islam, but please do it a different way and don't punish players for success, because that's just annoying and ahistorical

## Reply 61 — participant_042 · 2020-04-28 · post-26530480

@Baron von Shoes A couple of further questions: 1. Are there going to be fantasy elements like in the latest editions of CK2? By that I mean e.g. the following question: will Astrology's "Divine the Stars" just give some sort of a morale boost (or stuff like that), or will the mechanics assume that "predicting the future" can actually work? Same question regarding "Miracle Workers" (will the mechanics assume that "miracles" can actually happen?) and so on. 2. Why is Sky Burial giving a health boost? I'd say that it should rather give a malus to health, due to birds spreading diseases from corpses.

## Reply 62 — participant_052 · 2020-04-28 · post-26530487

I am uncertain why Abrahamics see each others faith as evil instead of hostile. I don't think that, say, Catholics saw Sunni or pagans as fundamentally more evil than Cathars. I think that "evil" conveys something akin to satanic cannibalistic cult, not established religion that countries that practice it maintain diplomatic relations with. I'd limit "evil" to religions that have at least one total opposite tenet or doctrine, such as all religions that see honest as virtue will see those with sacred lies tenet as evil instead of merely hostile, or those who allow witchcraft vs those who criminalize it. And all gnostics seeing each other as righteous is a bit too generous in my opinion, it's not like various sects didn't bicker with each other when they had the opportunity, it's just that most of time they were too busy with being stomped on by mainstream religion.

## Reply 63 — participant_053 · 2020-04-28 · post-26530490

<!-- artifact:quote:start -->
> Bearnest said: As a mechanic, this is fine; it'll keep realms from exploiting Holy Wars for blobbing. As a representation of RL, I think it misses the mark: I'd imagine people's fervor would spike after a calling for an Holy War that would retrieve land and righteous believers from heathens. And even more if it's successful. When can we see the new units in detail, and is there going to be different types for the different culture groups? Click to expand...
<!-- artifact:quote:end -->
I think you have it backwards. You need to whip people up into a religious fervor to get them motivated enough to declare the Holy War, otherwise most people are just going to shrug and question why they're being asked to fight a war thousands of miles away. For the purpose of declaring holy wars, fervor is more like political capital.

## Reply 64 — participant_054 · 2020-04-28 · post-26530494

@Baron von Shoes There were many medieval periods when Abrahamic religions managed to coexist peacefully with other religious groups, and ally and even intermarry each other. - Islam obviously included a lot of Christans, Jews, and later Hindus on its realms and it varied greatly between periods of religious persecution and relatively high tolerance - There was a famous case of multicultural Sicily - Christian and Muslim realms in Iberia did frequently ally "infidels" to fight "brethren" - Georgians and Armenians largely coexisted with Muslims (well how would they survive otherwise) - Even in India Muslim invaders had periods of high tolerance for Hindus (it was way worse for Buddhists) - Crusader states also wouldn't survive as long if they didn't practice reasonable diplomacy with Muslims neighbors So, how is all of this modeled in game?

## Reply 65 — participant_055 · 2020-04-28 · post-26530512

<!-- artifact:quote:start -->
> Baron von Shoes said: Fervor is global for the entire Faith. However, the more dynamic nature of the Fervor system means that Faiths simply won't end up in the 'heresy death-spiral' that CK2 had, since Fervor will jump back up after an outbreak and give the original Faith some breathing room to recover and deal with the heretics. Click to expand...
<!-- artifact:quote:end -->
No more heresy death spiral is the best feature of CK3 so far.

## Reply 66 — participant_056 · 2020-04-28 · post-26530532

Do we have meritocracy doctrine? And is there any special action for a specific combination of doctrine?

## Reply 67 — participant_053 · 2020-04-28 · post-26530549

<!-- artifact:quote:start -->
> Duuk said: No more heresy death spiral is the best feature of CK3 so far. Click to expand...
<!-- artifact:quote:end -->
Now I'm wondering what the best way to spread a new faith is. I guess successive rounds of conquest and conversion and stabilization.

## Reply 68 — participant_038 · 2020-04-28 · post-26530564

<!-- artifact:quote:start -->
> Mackus said: I am uncertain why Abrahamics see each others faith as evil instead of hostile. I don't think that, say, Catholics saw Sunni or pagans as fundamentally more evil than Cathars. I think that "evil" conveys something akin to satanic cannibalistic cult, not established religion that countries that practice it maintain diplomatic relations with. I'd limit "evil" to religions that have at least one total opposite tenet or doctrine, such as all religions that see honest as virtue will see those with sacred lies tenet as evil instead of merely hostile, or those who allow witchcraft vs those who criminalize it. And all gnostics seeing each other as righteous is a bit too generous in mind opinion, it's not like various sects didn't bicker with each other when they had the opportunity, it's just that most of time they were too busy with being stomped on by mainstream religion. Click to expand...
<!-- artifact:quote:end -->
I think the wording is just a bit off, where realistically evil would be on a level bellow its current position, however what is now "evil" should still have the same consequences as it has now. And since satanism isn't probably a thing in Ck3 having another layer might be a bit redundant.

## Reply 69 — participant_038 · 2020-04-28 · post-26530579

<!-- artifact:quote:start -->
> Zhetone said: People can "respectfully disagree" with my comment, but no one seems to have an actual argument that they're posting - when in real life did a religion winning wars against other faiths make its adherents less fervent in their faith, and when did losing make them more fervent? How could you say the first crusade weakened Catholicism and made heresies more likely to pop up? How can you say that Zoroastrians being wiped out made them stronger when in fact their religion collapsed more than ever? It's a nonsensical mechanic. I get why it's implemented, you don't want snowballing and you want it to be harder to wipe out faiths like Catholicism or Sunni Islam, but please do it a different way and don't punish players for success, because that's just annoying and ahistorical Click to expand...
<!-- artifact:quote:end -->
The loss of fervor probably represents people getting tired of fighting more and more holy wars, whereas people who are losing more and more territory want to fight back all the harder since they don't want to lose their land the same way others did. In my honest opinion the system just needs to have a cap for how much fervor can be lost in this way (and possibly even gained).

## Reply 70 — participant_046 · 2020-04-28 · post-26530590

<!-- artifact:quote:start -->
> Krajzen said: There were many medieval periods when Abrahamic religions managed to coexist peacefully with other religious groups, and ally and even intermarry each other. Click to expand...
<!-- artifact:quote:end -->
Agree, I'd really like to see this sort of "localized syncreticism" that doesn't affect the entire faith, just a particular region with multiple faiths. May not be that relevant, though, since CK games generally don't represent multiculturalism/multi-religion regions very well (compare, like, how Stellaris handles pop species now: pie charts for everyone).

## Reply 71 — participant_057 · 2020-04-28 · post-26530594

<!-- artifact:quote:start -->
> Zhetone said: People can "respectfully disagree" with my comment, but no one seems to have an actual argument that they're posting - when in real life did a religion winning wars against other faiths make its adherents less fervent in their faith, and when did losing make them more fervent? How could you say the first crusade weakened Catholicism and made heresies more likely to pop up? How can you say that Zoroastrians being wiped out made them stronger when in fact their religion collapsed more than ever? It's a nonsensical mechanic. I get why it's implemented, you don't want snowballing and you want it to be harder to wipe out faiths like Catholicism or Sunni Islam, but please do it a different way and don't punish players for success, because that's just annoying and ahistorical Click to expand...
<!-- artifact:quote:end -->
The First Crusade focused on retaking land, recapturing Nicea which had been taken just a decade earlier, and other territories seen as "theirs". Then the fall of the crusader state of Edessa triggered the second Crusade. Then the fall of Jerusalem triggered the Third Crusade. What it horrendously misrepresents is the Rise of Islam and fall of Zoroastrianism. But honestly, any system that could represent that period of history accurately would make for a terrible game, because Mohammed and the Rightly Guided Caliphs were crazy OP. And Fervor isn't lost by winning wars. It's lost by declaring them, and only by a slight amount. So you can't have everyone spamming it - and Oh, look, in real life there was a cooldown period between Crusades, and it wasn't just exactly 30 years but rather was related to events going on at the time. C.f. say Bogomil and Bogomilism. It was founded in the 900's around the time Christian rulers were getting involved in tons of wars with pagans all over Europe, to mixed results, though rarely outright losing territory to Pagans.

## Reply 72 — participant_058 · 2020-04-28 · post-26530596

Just a small idea. Give a small mitigation to opinion penalties between two Astray religious followers if there is a hostile religion bordering (or nearby) both rulers. The 'we've got bigger problems than each other' consideration. Same could be done for hostile Vs evil too.

## Reply 73 — participant_059 · 2020-04-28 · post-26530599

<!-- artifact:quote:start -->
> Zhetone said: People can "respectfully disagree" with my comment, but no one seems to have an actual argument that they're posting - when in real life did a religion winning wars against other faiths make its adherents less fervent in their faith, and when did losing make them more fervent? How could you say the first crusade weakened Catholicism and made heresies more likely to pop up? How can you say that Zoroastrians being wiped out made them stronger when in fact their religion collapsed more than ever? It's a nonsensical mechanic. I get why it's implemented, you don't want snowballing and you want it to be harder to wipe out faiths like Catholicism or Sunni Islam, but please do it a different way and don't punish players for success, because that's just annoying and ahistorical Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> wilcoxchar said: I think you have it backwards. You need to whip people up into a religious fervor to get them motivated enough to declare the Holy War, otherwise most people are just going to shrug and question why they're being asked to fight a war thousands of miles away. For the purpose of declaring holy wars, fervor is more like political capital. Click to expand...
<!-- artifact:quote:end -->
Yeah, I think it makes sense this way: the first few holy wars, especially if they liberate a holy site, will still leave a faith with high enough fervor. But once the holy land is already in Christian hands and kings keep on invoking non-stop holy wars to justify land grabs in far-off places in Persia and the Arabian peninsula, fervor is going to take a hit because people can tell the religion is being used cynically and opportunistically.

## Reply 74 — participant_002 · 2020-04-28 · post-26530627

<!-- artifact:quote:start -->
> Zhetone said: People can "respectfully disagree" with my comment, but no one seems to have an actual argument that they're posting - when in real life did a religion winning wars against other faiths make its adherents less fervent in their faith, and when did losing make them more fervent? How could you say the first crusade weakened Catholicism and made heresies more likely to pop up? How can you say that Zoroastrians being wiped out made them stronger when in fact their religion collapsed more than ever? It's a nonsensical mechanic. I get why it's implemented, you don't want snowballing and you want it to be harder to wipe out faiths like Catholicism or Sunni Islam, but please do it a different way and don't punish players for success, because that's just annoying and ahistorical Click to expand...
<!-- artifact:quote:end -->
As far as losing making someone more fervent, the Crusades being won and lost had a tendency to make the loser more fervent with regard to re-capturing the lost Holy Land. With winning reducing how fervent people are... perhaps the idea is to encourage them to consolidate the land they've taken, convert their new population and then push onwards. There's also a need to work up a new wave of interest in another Great Holy War against a new target.

## Reply 75 — participant_053 · 2020-04-28 · post-26530630

<!-- artifact:quote:start -->
> Zhetone said: People can "respectfully disagree" with my comment, but no one seems to have an actual argument that they're posting - when in real life did a religion winning wars against other faiths make its adherents less fervent in their faith, and when did losing make them more fervent? How could you say the first crusade weakened Catholicism and made heresies more likely to pop up? How can you say that Zoroastrians being wiped out made them stronger when in fact their religion collapsed more than ever? It's a nonsensical mechanic. I get why it's implemented, you don't want snowballing and you want it to be harder to wipe out faiths like Catholicism or Sunni Islam, but please do it a different way and don't punish players for success, because that's just annoying and ahistorical Click to expand...
<!-- artifact:quote:end -->
Most historical heresies, at least of the Christian variety, have been condemnations of how much wealth those higher up in a faith and its clergy have. So it makes sense that the more temporal power a faith (and especially the leaders of that faith) has, the greater perception among both secular leaders and the more spiritual minded clergy that the faith is corrupt and out of touch with the common people, and calls will be made for a rejection of that wealth and power with new teachings as a rejuvenation of the faith's guiding principles. Look at the origins of the Waldensians and Lollards. Plus, the Second and Third Crusades were started by the loss of holy wars (the falls of Edessa and Jerusalem respectively).

## Reply 76 — participant_060 · 2020-04-28 · post-26530640

It looks great. I suppose a Christian tenet could be 'Communion with Rome' which destroys your Head of Faith (i.e. makes the Pope your HoF) but makes Catholicism and you consider eachother righteous, provided certain other triggers are in place (maybe at most 1 other tenet difference?). In that case it would also make things like the Council of Florence possible - an Orthodox ruler deciding to reform his faith to be friendlier with the Pope, but getting internal resistance to changing the faith. And the fervor-for-Holy-War thing, while obviously a rubber band kind of mechanism and thus hard to truly justify (since game probably came before justification), does fit with how these things went; the French were much more militarily religious when they could hop over the Pyrenees to help the Spanish, and a lot more cynical when there were catholic all around them with little risk. And Catholicism's largest fervor after the Crusades was probably the Reformation era. Loss leads to a desire to fight back; only long-term repeated loss leads to disheartening, which could be a separate mechanic (maybe just a result of having no Holy Sites).

## Reply 77 — participant_042 · 2020-04-28 · post-26530643

<!-- artifact:quote:start -->
> Videogames said: Yeah, I think it makes sense this way: the first few holy wars, especially if they liberate a holy site, will still leave a faith with high enough fervor. But once the holy land is already in Christian hands and kings keep on invoking non-stop holy wars to justify land grabs in far-off places in Persia and the Arabian peninsula, fervor is going to take a hit because people can tell the religion is being used cynically and opportunistically. Click to expand...
<!-- artifact:quote:end -->
An idea: if a Faith's Holy Site belongs to the territory targeted by a Holy War, don't reduce the Fervor for declaring said Holy War (and maybe even increase it), but if the targeted territory contains no Holy Sites of this Faith, do apply the Fervor reduction.

## Reply 78 — participant_061 · 2020-04-28 · post-26530654

So when I create a christian heresy which has the Ecumenism doctrine it will not be hostile towards catholizism and the pope can't do anything despite me renouncing him?

## Reply 79 — participant_029 · 2020-04-28 · post-26530656

<!-- artifact:quote:start -->
> DreadLindwyrm said: So, if you are Abrahamic (as Christians will be), and both same family/same religion (as different Christian faiths will be), you are looking at different faiths being "hostile" by default. Same family/same religion implies "Different faith" here. Click to expand...
<!-- artifact:quote:end -->
Yeah that makes sense to me, and "Hostile" fits with what happened to Insular Christianity irl: The lack of papal control over how things were run in Ireland is what led to the pope at the time (the only English pope) giving the English king the sanction to invade Ireland and reassert Roman authority and implement Roman reforms

## Reply 80 — participant_062 · 2020-04-28 · post-26530663

I see the reasoning behind holy wars costing you fervour. But on the other hand... yeah, we are talking about a time period where winning wars and battles was largely seen as a sign of divine approval. Plus I do not think there were many new heresies created because Charlemagne conquered some Germanic pagans, rather the opposite. It seemed to strengthen Western Christianity.

## Reply 81 — participant_063 · 2020-04-28 · post-26530664

Zunist confirmed to be present, praise the Sun. \[+]/

## Reply 82 — participant_016 · 2020-04-28 · post-26530671

<!-- artifact:quote:start -->
> Zhetone said: People can "respectfully disagree" with my comment, but no one seems to have an actual argument that they're posting - when in real life did a religion winning wars against other faiths make its adherents less fervent in their faith, and when did losing make them more fervent? Click to expand...
<!-- artifact:quote:end -->
Probably nowhere, it doesn't matter, it's a gameplay solution to stop powerful religions from snowballing weak religions and ensure that there can be an interesting religious situation on the map even later on in the campaign, such as powerful religions suffering temporary bursts of heresy or weak religions being able to rally against their encroaching enemies. If you're desperate for a flavour explanation then assume that rallying people for holy wars "spends" their religious fervor. You don't lose fervor for winning but just for declaring channels popular religious zeal making them less interested in joining for the next ones.

## Reply 83 — participant_033 · 2020-04-28 · post-26530704

<!-- artifact:quote:start -->
> viola said: it's a gameplay solution to stop powerful religions from snowballing weak religions Click to expand...
<!-- artifact:quote:end -->
But, I mean--shouldn't they? I don't mean that an intolerant sort of way. But there's a historical reason why Zunism didn't survive and Abrahamic religions won in the region depicted here (minus India), particularly that they are good at converting, fond of holy wars no matter the cause, and simply have more adherents to begin with. The fact that a player can turn that around and make a pagan faith dominant means that they're a good player and present an interesting what-if scenario, sure, but as the EU dev diary today points out, the AI forming a majority non-Abrahamic Europe quickly is unrealistic.

## Reply 84 — participant_016 · 2020-04-28 · post-26530705

<!-- artifact:quote:start -->
> HighChanceOfRai said: Yeah that makes sense to me, and "Hostile" fits with what happened to Insular Christianity irl: The lack of papal control over how things were run in Ireland is what led to the pope at the time (the only English pope) giving the English king the sanction to invade Ireland and reassert Roman authority and implement Roman reforms Click to expand...
<!-- artifact:quote:end -->
Not really: "Hostile" is the threshold for holy wars and nobody would ever think of having a holy war between Insulars and Catholics at the time. The churches in Ireland were still considered and also considered themselves to be in communion with Rome, even if there were tensions about local rites and practices being non-standard compared to Rome.

## Reply 85 — participant_064 · 2020-04-28 · post-26530707

<!-- artifact:quote:start -->
> Baron von Shoes said: You need to use either a Tenet or a Doctrine to change religious hostility. Either option works just as well; Ecumenism is a Doctrine for example, while Christian Syncretism is a Tenet. Currently only Gnostics are able to achieve a Righteous view of other Faiths, but mods can change or expand upon this to enable schism reformations and the like without too much trouble. Click to expand...
<!-- artifact:quote:end -->
I encourage you to look for a way to represent the Schism, so that, in the early years, Catholics and Orthodox view each other as Righteous.

## Reply 86 — participant_065 · 2020-04-28 · post-26530709

I died a little inside when I saw the Lollards are making a comeback. Unless you're planning to stretch the game through to the 16th century these guys really shouldn't be making an appearance. No doubt we'll be seeing a return of late 15th century Muslim heretics the Zikri too.

## Reply 87 — participant_066 · 2020-04-28 · post-26530718

<!-- artifact:quote:start -->
> Baron von Shoes said: Fervor is global for the entire Faith. However, the more dynamic nature of the Fervor system means that Faiths simply won't end up in the 'heresy death-spiral' that CK2 had, since Fervor will jump back up after an outbreak and give the original Faith some breathing room to recover and deal with the heretics. Click to expand...
<!-- artifact:quote:end -->
Question, how well will the system deal with religious fervor locally? IMO the system should not be pure global based. News dont travel that efficient in those days and I'd imagine your local hedonist cannibal duke, local bishop should have the same weightage as corrupt pope across half the continent; then a random petty king that not everyone cares about, locally should have far less effect on that person's religious fervor...

## Reply 88 — participant_063 · 2020-04-28 · post-26530756

<!-- artifact:quote:start -->
> Xain said: If Catholic has the "ecumenic" trait, then an heresy having the ecumenic trait will be considered "just" astray? Click to expand...
<!-- artifact:quote:end -->
Which make perfect sense, especially if we consider Ireland, which should be also be ecumenical but a different Christian faith then Catholic, as they didn't answer to the pope until the 12th century and their church leadership was based around monasteries instead of bishopric.

## Reply 89 — participant_067 · 2020-04-28 · post-26530764

<!-- artifact:quote:start -->
> Baron von Shoes said: Click to expand...
<!-- artifact:quote:end -->
The Roman Sun worship, that of Sol Invictus, had its major celebration on 25th December, not in the summer, as can be seen in this Roman calendar.

## Reply 90 — participant_062 · 2020-04-28 · post-26530772

<!-- artifact:quote:start -->
> DominusNovus said: I encourage you to look for a way to represent the Schism, so that, in the early years, Catholics and Orthodox view each other as Righteous. Click to expand...
<!-- artifact:quote:end -->
I would argue that they saw each other, de facto as astray, as represented here. Before the Schism, due to centuries of differentiation in religious practice and after the Schism as well (the so-called 'Great Schism' was not seen as important by any people at the time.)

## Reply 91 — participant_016 · 2020-04-28 · post-26530781

<!-- artifact:quote:start -->
> Varus90 said: But, I mean--shouldn't they? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Varus90 said: I don't mean that an intolerant sort of way. But there's a historical reason why Zunism didn't survive and Abrahamic religions won in the region depicted here (minus India), particularly that they are good at converting, fond of holy wars no matter the cause, and simply have more adherents to begin with. The fact that a player can turn that around and make a pagan faith dominant means that they're a good player and present an interesting what-if scenario, sure, but as the EU dev diary today points out, the AI forming a majority non-Abrahamic Europe quickly is unrealistic. Click to expand...
<!-- artifact:quote:end -->
No. If you want interesting and dynamic religious gameplay in this game you probably don't want for Catholicism, Orthodoxy, Sunni denomination #3 and Hinduism to be the only surviving religions 100 years into the game and then never ever change whatsoever due to how powerful they are. You want a system where even strong religions can suddenly struggle with heresies (like it historically happened with Catholicism in Europe, as the latter part of the Middle Ages was all about the Papacy struggling with antipopes and heresies popping out in protest to the perceived immorality of the clergy) and weak religions aren't doomed to disappear in a death spiral caused by military losses to stronger opponents. Why are you even bringing up non-Abrahamics? The system is just meant to make it possible for Cathars to pop up in Europe and be an issue like they historically were even if Catholicism is militarily strong. I have absolutely no idea where you got the idea of Europe being converted to paganism quickly from.

## Reply 92 — participant_068 · 2020-04-28 · post-26530787

Will there be any religious dynamic events? The thing about CK 2 is that it felt the same no matter how many years the game went on. CK 3 has addressed many of the more dynamic upcoming aspects about the game, but what about dynamic events? I'm going to illustrate what I mean. But in short, they are pretty similar to the Crusades, which is a perfect example of a dynamic event where the game adapts to recent changes. The examples below will be based on Catholicism and should be tweaked to fit the other religions as well. These ideas are thought up in the concept of CK 2, so I do not know whether or not all of them can be implemented in CK 3. But I will list the examples anyway, as I think dynamic events like this may add a lot of flavor to the game. 1. Religious Orthodoxy as a response to a longer period of high moral authority Spoiler The catholic faith has reached its maximum moral authority and there is no doubt in the legitimacy of its dogmas and religious institutions be it from the peasants or from the nobility. During this period, the religious zeal is at its peak. Virtues are considered even more valuable than before, granting an increased opinion among the clergy and a bonus to overall stats, and it's more important for a ruler to be pietous than to be prestigious. Sinful rulers are pennalized and the Holy Orders gain a +30% morale damage and defense buff. The Pope is likely to grant others claims for titles if he considers the ruling dynasty or men unfit for their position. 2. Prestige and hedonism as a response to a low moral authority and and abnormal amount of epidemics and warfare Spoiler In the last decade, the world has seen an abnormal amount of epidemics and warfare, resulting in the peoples' questioning of the Lord almighty. Noble rulers have taken the opportunity to exalt worldly features. The worth of Prestige has been doubled and characteristics associated with vices have changed for the better, all while the worth of Piety on the other hand has been halved and rulers favoring virtuous traits are now seen as weak and meek. Noble adventures are more likely to appear in conquest for their claims. 3. Witch Hunt as a response to apostasy and witchcraft Spoiler It has come to the clergy's attention that more and more people have turned away from the gospel to embrace the sweet promises of the dark lord. All around the Christian world, the clergy are encouraging the hunting of witches and apostates. Rulers are expected to hunt witches, and they are expected to burn anyone accused of witchcraft, no matter be it a close relative or a lowborn stranger. Rulers who let an accused witch go free, may get excommunicated and accused of apostasy him- or herself. On the other hand: those who make a name for themselves as an outstanding beacon of faith, may leave a bloodline behind. 4. Religious revolt as a response to religious oppression Spoiler Infidel rulers have settled down on Christian land, seeking to proselytize their Devilish Religion. In this dark times, the Catholic Pope of Rome is especially looking at the Visigoths suffering under Umayyad rule in Iberia. In a major speech, The Pope urges the people of the land to take up arms [Catholic uprising revolts], knowing that the Pope - and God - stands with them! Catholic Peasant revolts in infidel lands have now increased to a global +10% for one year. Religious revolt risk has been increased among Catholic peasantry in all counties ruled by secular rulers not of the catholic faith. OBS: I know that CK 3 has a different revolt system, so changes can me made to increase instability in counties. 5. Bonus moral authority events for heretics as a result of heretical expansion Spoiler For some time now, heretics have gained political influence, winning terrain. The Catholic Pope seems unable to hold the Christian realm together, making some question if he truly has the blessing of the Lord almighty. Catholic moral authority will now be lowered by -10 for the next 10 years while all Catholic heresies will get a +10 buff each. 6. Free investiture events as a result of failed crusades and low moral authority Spoiler The Noble leaders have for a long time been dissatisfied with the ruling Pope of Rome. Failed Catholic Crusades and his inability to combat heretics have resulted in the cynical, cruel, arbitrary, ambitious or envious leaders, or those excommunicated and or with a negative opinion of the pope, to implement Free Investiture [automatic change]. The Pope is not pleased. OBS: CK 3 will have a different trait-system than in CK 2, so the listed traits can be replaced with what is suitable for CK 3. 7. Continuation of the Free Investiture event above (#6) Spoiler To combat the nobles' grasp on the spiritual power, the Pope of Rome has started a decree where he threatens to excommunicate all leaders with Free Investiture unless they change their laws in accordance with the will of the Church. Each ruler with Free Investiture have now been given an option to decide [automatic change]. 8. A religious (last) stand as a result of low moral authority and low religious population Spoiler To counter the decreased Moral Authority of the Catholic Church, the Pope of Rome has started a campaign where he urges all true believers to take up the spiritual fight against evil. Catholics will now be harder to convert, some might gain the Zealous trait and those secretly Catholic will openly practice their beliefs! 9. Religious anti-papal war as a result of the current Pope being a wicked priest Spoiler For some time now, the Pope of Rome has reigned over the Spiritual world in sin. An immoral man of the cloth, the pious rulers of the Catholic world no longer recognize his claim. An [independent] Antipope has been setup [random among the Cardinals?] and all rulers have been given an option to determine whom to recognize as the true successor of Saint Peter. Furthermore, they have started a war to depose of the old Pope! Trembling in fear, the Pope of Rome asks all true pious Catholic rulers to take up arms in defense of the lord almighty! All true pious Catholics willing to lend him a hand will be greatly rewarded should he win! (Piety, Paragon of virtue? Coronation / Sainthood?). These are some examples, hope you found them to your liking! Note that the idea of the events above is what I'm trying to point out, and not the specific examples. Examples may be added or removed but the point of dynamic events is what's of importance and which may be a very good asset to the game.

## Reply 93 — participant_028 · 2020-04-28 · post-26530796

<!-- artifact:quote:start -->
> Gunthah said: The Roman Sun worship, that of Sol Invictus, had its major celebration on 25th December, not in the summer, as can be seen in this Roman calendar. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> viola said: No. If you want interesting and dynamic religious gameplay in this game you probably don't want for Catholicism, Orthodoxy, Sunni denomination #3 and Hinduism to be the only surviving religions 100 years into the game and then never ever change whatsoever due to how powerful they are. You want a system where even strong religions can suddenly struggle with heresies (like it historically happened with Catholicism in Europe, as the latter part of the Middle Ages was all about the Papacy struggling with antipopes and heresies popping out in protest to the perceived immorality of the clergy) and weak religions aren't doomed to disappear in a death spiral caused by military losses to stronger opponents. Why are you even bringing up non-Abrahamics? The system is just meant to make it possible for Cathars to pop up in Europe and be an issue like they historically were even if Catholicism is militarily strong. I have absolutely no idea where you got the idea of Europe being converted to paganism quickly from. Click to expand...
<!-- artifact:quote:end -->
Now that sounds familiar somehow ... I propose events that erode the Fervor of faiths whose clergy are rich - that way, we can let holy war successes translate into Fervor hits down the line instead of immediately.​

## Reply 94 — participant_069 · 2020-04-28 · post-26530802

Can different faiths have the same religious head? for example, can Maronites recognise the Pope but follow their own rites? Do the Celtic Christians acknowledge the Pope as the head of their faith but still marry?

## Reply 95 — participant_053 · 2020-04-28 · post-26530819

<!-- artifact:quote:start -->
> Varus90 said: But, I mean--shouldn't they? I don't mean that an intolerant sort of way. But there's a historical reason why Zunism didn't survive and Abrahamic religions won in the region depicted here (minus India), particularly that they are good at converting, fond of holy wars no matter the cause, and simply have more adherents to begin with. The fact that a player can turn that around and make a pagan faith dominant means that they're a good player and present an interesting what-if scenario, sure, but as the EU dev diary today points out, the AI forming a majority non-Abrahamic Europe quickly is unrealistic. Click to expand...
<!-- artifact:quote:end -->
No. It often took centuries to completely wipe out a religion. I mean, Zoroastrianism still survives to this day. It makes a lot of sense that as religions become more persecuted and diminished to smaller but more concentrated communities, the zeal in those communities toward maintaining their traditional beliefs against the push of conversion efforts would be extremely strong.

## Reply 96 — participant_033 · 2020-04-28 · post-26530824

<!-- artifact:quote:start -->
> viola said: and weak religions are doomed to disappear in a death spiral caused by military losses to stronger opponents Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> viola said: Why are you even bringing up non-Abrahamics? The system is just meant to make it possible for Cathars to pop up in Europe and be an issue like they historically were even if Catholicism is militarily strong. I have absolutely no idea where you got the idea of Europe being converted to paganism quickly from. Click to expand...
<!-- artifact:quote:end -->
The heretical faiths may appear, but will be quickly suppressed, which is, yes, realistic. Cathar endurance and victories were due as much to the sociopolitical factors of the time unrelated directly to religion as to the direct brutality of the Church-sponsored forces. Well, because if you don't have a heretic outpost on your borders, what's going to be the next "weak religion" to be targeted by a Holy War CB? The way OP phrased it there suggested it was intended to gameplay balance all Religions as well as Faiths (remember, in CK3 terms Cathars are of course still Christian, just a separate Fatih).

## Reply 97 — participant_057 · 2020-04-28 · post-26530853

My questions: What family does Zoroastrianism belong to? Will Tengrii have a special tenet allowing them to Marry "evil" faiths? Is the marriage restriction just for the offer recipient? Will Jainism be the most stubbornly persistent religion under this system? Can heresiarchs espouse a new faith belonging to a different religious family? E.g. a pagan revival in Christian Europe, a Tengrii spontaneously converting to Judaism, or an Indian Hindu adopting an obscure branch of Christianity. Are there any tenets that increase hostility? There were many minor "heretical" Eastern religious leaders who advocated religious violence and intolerance.

## Reply 98 — participant_053 · 2020-04-28 · post-26530864

<!-- artifact:quote:start -->
> Varus90 said: The heretical faiths may appear, but will be quickly suppressed, which is, yes, realistic. Cathar endurance and victories were due as much to the sociopolitical factors of the time unrelated directly to religion as to the direct brutality of the Church-sponsored forces. Click to expand...
<!-- artifact:quote:end -->
The Cathars weren't unique in their strength or how long they lasted though. For one, the Waldensians lasted for centuries in Swtzerland, Italy, and France even influencing Reformation thinkers and, by the way, they're still around today. The idea that the Cathars were unique as a Catholic heresy that wasn't quickly suppressed is really wrong.

## Reply 99 — participant_024 · 2020-04-28 · post-26530865

<!-- artifact:quote:start -->
> MinotaurWarrior said: My questions: What family does Zoroastrianism belong to? Click to expand...
<!-- artifact:quote:end -->
They said previously that Zoroastrianism will be in the eastern/oriental group

## Reply 100 — participant_028 · 2020-04-28 · post-26530875

<!-- artifact:quote:start -->
> MinotaurWarrior said: My questions: What family does Zoroastrianism belong to? Will Tengrii have a special tenet allowing them to Marry "evil" faiths? Click to expand...
<!-- artifact:quote:end -->
1. “Eastern", or Oriental 2. That should fall under concubinage

## Reply 101 — participant_033 · 2020-04-28 · post-26530889

<!-- artifact:quote:start -->
> wilcoxchar said: The Cathars weren't unique in their strength or how long they lasted though. For one, the Waldensians lasted for centuries in Swtzerland, Italy, and France even influencing Reformation thinkers and, by the way, they're still around today. The idea that the Cathars were unique as a Catholic heresy that wasn't quickly suppressed is really wrong. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> viola said: The system is just meant to make it possible for Cathars to pop up in Europe and be an issue like they historically were Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> wilcoxchar said: No. It often took centuries to completely wipe out a religion. Click to expand...
<!-- artifact:quote:end -->
First, tell that to But anyway, Nobody said they would be completely annihilated--simply removed from positions of political power. Waldensians influencing philosophers is important down the line, but the fact that there are no officially Waldensian countries in Europe today is the important gameplay part. Removing all characters with it from the game does not mean that they no longer exist (there are many, many people offscreen, after all), simply that they have no significant influence politically speaking.

## Reply 102 — participant_016 · 2020-04-28 · post-26530904

<!-- artifact:quote:start -->
> Varus90 said: The heretical faiths may appear, but will be quickly suppressed, which is, yes, realistic. Click to expand...
<!-- artifact:quote:end -->
Or maybe not? Crusader Kings isn't about realism, it's about alternate history, even of the implausible kind. I don't get it. Do you really like the idea of an immutable, monolithic Catholic blob that crushes everything in its wake and is never challenged over a system where religions can wax and wane in power, well, dynamically?

## Reply 103 — participant_070 · 2020-04-28 · post-26530918

<!-- artifact:quote:start -->
> Baron von Shoes said: View attachment 571930 [A screenshot showing various warfare-focuses Doctrines and Tenets, including Armed Pilgrimages which enables Crusades] Click to expand...
<!-- artifact:quote:end -->
CK3 will allow me to have warrior-priests in my ranks? This game is truly blessed by Sigmar!

## Reply 104 — participant_053 · 2020-04-28 · post-26530919

<!-- artifact:quote:start -->
> Varus90 said: First, tell that to But anyway, Nobody said they would be completely annihilated--simply removed from positions of political power. Waldensians influencing philosophers is important down the line, but the fact that there are no officially Waldensian countries in Europe today is the important gameplay part. Removing all characters with it from the game does not mean that they no longer exist (there are many, many people offscreen, after all), simply that they have no significant influence politically speaking. Click to expand...
<!-- artifact:quote:end -->
Except it was not "influencing" philosophers. It is literally the Waldensian Church continued to exist into and past the Reformation and was considered the Italian branch of Calvinism before merging with the Italian Methodist Church in the 1970s. https://en.wikipedia.org/wiki/Waldensian_Evangelical_Church

## Reply 105 — participant_033 · 2020-04-28 · post-26530920

<!-- artifact:quote:start -->
> viola said: Or maybe not? Crusader Kings isn't about realism, it's about alternate history, even of the implausible kind. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> wilcoxchar said: Except it was not "influencing" philosophers. It is literally the Waldensian Church continued to exist into and past the Reformation and was considered the Italian branch of Calvinism before merging with the Italian Methodist Church in the 1970s. https://en.wikipedia.org/wiki/Waldensian_Evangelical_Church Click to expand...
<!-- artifact:quote:end -->
Which I do frequently enjoy, buuut...three years later, when an Irish count spontaneously turns into a Bogomilist polar bear married to a horse before getting sacrificed to Aztec sun gods, there's kind of a limit. Internal division should be crippling, yes, but it should arise in a realistic way--winning a Crusade, as stated, does not make people believe less in divine approval. Maybe something similar to the existing Stress mechanic or reform desire from EUIV? Which does not answer the question of what political power it held in Italy versus the dominant religion (Roman Catholicism). Something terribly drastic would have to happen for the locals to convert, which could indeed arise in game, but winning a holy war would not be it. If you do have any suggestions for a more realistic mechanic than either Moral Authority or this system, such as the ideas I floated above, that would be a helpful discussion.

## Reply 106 — participant_062 · 2020-04-28 · post-26530921

<!-- artifact:quote:start -->
> viola said: Or maybe not? Crusader Kings isn't about realism, it's about alternate history, even of the implausible kind. I don't get it. Do you really like the idea of an immutable, monolithic Catholic blob that crushes everything in its wake and is never challenged over a system where religions can wax and wane in power, well, dynamically? Click to expand...
<!-- artifact:quote:end -->
I believe nobody is disputing that. The issue is that it seems impossible for a Catholic blob to crush everything, as it had done, for centuries, before the reformation. I don't think there is ANYONE here or anywhere else, disliking the idea of dynamicity. But I also think that there is a large portion of the community that likes for historical outcomes to, if not likely, to at least be possible.

## Reply 107 — participant_040 · 2020-04-28 · post-26530936

<!-- artifact:quote:start -->
> spaninq said: Remember, heresies are simply different faiths of the same religion now. Catholicism and Orthodox are different faiths of the same religion, Christianity, and do not get heresies specific to their faith, like they did in CK2. Click to expand...
<!-- artifact:quote:end -->
Yes, by "heresy" here I was thinking of a new religion founded by a human ruler - sorry for the misleading language. My question was - from a gameplay perspective, it would be overwhelmingly more advantageous for a ruler of a Catholic realm to keep every new religion he might want to found as "ecumenic", so to escape effectively most of the issues of being of a "wrong" religion. The only case in which it would not be a too easy advantage to take is if we are founding a new religion explicitly in order to wage holy wars against your neighbours...

## Reply 108 — participant_053 · 2020-04-28 · post-26530947

<!-- artifact:quote:start -->
> Skales said: I believe nobody is disputing that. The issue is that it seems impossible for a Catholic blob to crush everything, as it had done, for centuries, before the reformation. I don't think there is ANYONE here or anywhere else, disliking the idea of dynamicity. But I also think that there is a large portion of the community that likes for historical outcomes to, if not likely, to at least be possible. Click to expand...
<!-- artifact:quote:end -->
The historical outcome is that the Catholic blob was not able to crush everything, so the historical outcome seems pretty possible here.

## Reply 109 — participant_028 · 2020-04-28 · post-26530954

<!-- artifact:quote:start -->
> Varus90 said: Internal division should be crippling, yes, but it should arise in a realistic way--winning a Crusade, as stated, does not make people believe less in divine approval. Click to expand...
<!-- artifact:quote:end -->
I fullheartedly agree with your sagacity - but of course, the gold brimming the coffers of the Pope and other clergymen after a Crusade, on the other hand...

## Reply 110 — participant_002 · 2020-04-28 · post-26530955

<!-- artifact:quote:start -->
> Xain said: Yes, by "heresy" here I was thinking of a new religion founded by a human ruler - sorry for the misleading language. My question was - from a gameplay perspective, it would be overwhelmingly more advantageous for a ruler of a Catholic realm to keep every new religion he might want to found as "ecumenic", so to escape effectively most of the issues of being of a "wrong" religion. The only case in which it would not be a too easy advantage to take is if we are founding a new religion explicitly in order to wage holy wars against your neighbours... Click to expand...
<!-- artifact:quote:end -->
But... it's a slot that you could spend on something more useful to you.

## Reply 111 — participant_062 · 2020-04-28 · post-26530957

<!-- artifact:quote:start -->
> wilcoxchar said: The historical outcome is that the Catholic blob was not able to crush everything, so the historical outcome seems pretty possible here. Click to expand...
<!-- artifact:quote:end -->
The only major heresy the Catholic blob was unable to crush, to the point that in-game it would hold provinces. Was Hussitism. Every other heresy was relegated to underground or obscurity.

## Reply 112 — participant_016 · 2020-04-28 · post-26530960

<!-- artifact:quote:start -->
> Varus90 said: Which I do frequently enjoy, buuut...three years later, when an Irish count spontaneously turns into a Bogomilist polar bear married to a horse before getting sacrificed to Aztec sun gods, there's kind of a limit. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Varus90 said: Internal division should be crippling, yes, but it should arise in a realistic way--winning a Crusade, as stated, does not make people believe less in divine approval. Click to expand...
<!-- artifact:quote:end -->
So, you believe that having a system where victorious religions aren't allowed to stack positive moral authority bonuses on top of positive moral authority bonuses to give a chance for heresies to pop up and losing religions to not just die is equivalent to... That thing? That's interesting. Well, you're in luck: that's not how the system works.

## Reply 113 — participant_071 · 2020-04-28 · post-26530969

Anybody knows what is, in the first image, that head with a red lightning? Has it been explained?

## Reply 114 — participant_062 · 2020-04-28 · post-26530974

<!-- artifact:quote:start -->
> Cagallo said: Anybody knows what is, in the first image, that head with a red lightning? Has it been explained? Click to expand...
<!-- artifact:quote:end -->
Stress I assume?

## Reply 115 — participant_028 · 2020-04-28 · post-26530975

<!-- artifact:quote:start -->
> Cagallo said: Anybody knows what is, in the first image, that head with a red lightning? Has it been explained? Click to expand...
<!-- artifact:quote:end -->
That, kind sir, is the game's greatest improvement - period - over CK2: Stress.

## Reply 116 — participant_027 · 2020-04-28 · post-26530980

<!-- artifact:quote:start -->
> DreadLindwyrm said: But... it's a slot that you could spend on something more useful to you. Click to expand...
<!-- artifact:quote:end -->
I dunno, I think the idea of being a Christian heresy who can't be excommunicated (because you have no or are the religious head) and can't be Crusaded upon by other Christians sounds *very* useful.

## Reply 117 — participant_033 · 2020-04-28 · post-26530982

<!-- artifact:quote:start -->
> viola said: So, you believe that having a system where victorious religions aren't allowed to stacking positive moral authority bonuses on top of positive moral authority bonuses to give a chance for heresies to pop up and losing religions to not just die is equivalent to... That thing? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> viola said: isn't about realism, it's about alternate history, even of the implausible kind. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> viola said: Well, you're in luck: that's not how the system works. Click to expand...
<!-- artifact:quote:end -->
So, You're admitting your favored system is unrealistic and implausible? That's interesting. Well, you're out of luck, because here's how it works if you actually read the DD: 1. Declaring Holy Wars drops Fervor. 2. Religions with low Fervor become more susceptible to heresy and conversion (I.E., believing less in divine approval). And what does one do when previous Holy Wars went well, even if one isn't opportunistic?

## Reply 118 — participant_028 · 2020-04-28 · post-26530995

<!-- artifact:quote:start -->
> Varus90 said: 1. Declaring Holy Wars drops Fervor. 2. Religions with low Fervor become more susceptible to heresy and conversion (I.E., believing less in divine approval). Click to expand...
<!-- artifact:quote:end -->
I think this can be numerically balanced, like Holy Wars give a -1% to Fervor, but "low" Fervor is lower than 50% or something like that. So as long as you faith doesn't declare 50 holy wars at once you should be ok.

## Reply 119 — participant_033 · 2020-04-28 · post-26531003

<!-- artifact:quote:start -->
> FondMemberofSociety said: I think this can be numerically balanced, like Holy Wars give a -1% to Fervor, but "low" Fervor is lower than 50% or something like that. So as long as you faith doesn't declare 50 holy wars at once you should be ok. Click to expand...
<!-- artifact:quote:end -->
That does seem more fair and more historical, admittedly (I can see people being distrustful of all those wars at once), the problem just being that it includes AI holy wars. Well, maybe if they balance the AI.

## Reply 120 — participant_016 · 2020-04-28 · post-26531005

<!-- artifact:quote:start -->
> Varus90 said: You're admitting your favored system is unrealistic and implausible? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Varus90 said: Well, you're out of luck Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Varus90 said: because here's how it works if you actually read the DD: 1. Declaring Holy Wars drops Fervor. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Varus90 said: winning a Crusade Click to expand...
<!-- artifact:quote:end -->
Yes. Even if losing fervor for declaring a holy war does not make a lot of sense (unless you buy into the devs' explanation) it still favours religious dynamism over monolithic religious blobs. The argument has always been about gameplay first and realism later. And it took you this long to figure it out apparently. You think so? Yes. Declaring holy wars. Not Could you explain me the difference between winning and declaring a war?

## Reply 121 — participant_012 · 2020-04-28 · post-26531007

<!-- artifact:quote:start -->
> Skales said: The only major heresy the Catholic blob was unable to crush, to the point that in-game it would hold provinces. Was Hussitism. Every other heresy was relegated to underground or obscurity. Click to expand...
<!-- artifact:quote:end -->
And that makes great point for Hussitism to appear in CK3

## Reply 122 — participant_028 · 2020-04-28 · post-26531014

<!-- artifact:quote:start -->
> Varus90 said: That does seem more fair, admittedly, the problem just being that it includes AI holy wars. Well, maybe if they balance the AI. Click to expand...
<!-- artifact:quote:end -->
I admit my bias, but it is pretty rare for 50 holy wars of the same religion to start in CK2. But that may be because I play as Mazdayasnians too often.

## Reply 123 — participant_072 · 2020-04-28 · post-26531015

Do religious relations tenets like "Ecumenism" heavily restrict your other religious options? Because it seems both ahistorical and imbalanced from the gameplay perspective to be able to create a gender-equal pro-gay witchcraft-allowed party faith and have Catholics view you as only "astray".

## Reply 124 — participant_053 · 2020-04-28 · post-26531021

<!-- artifact:quote:start -->
> Varus90 said: 1. Declaring Holy Wars drops Fervor. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Varus90 said: 2. Religions with low Fervor become more susceptible to heresy and conversion (I.E., believing less in divine approval). Click to expand...
<!-- artifact:quote:end -->
As it should. You (or your religious head) are in effect spending religious capital that you have built up in order to whip your followers into a frenzy over a land they've almost certainly never seen before thousands of miles away. Yes. You have spent capital in declaring that someone is a religious enemy that needs to be focused on and dealt with right now. That will mean effort and energy is spent less on other potential religious incursions, whether that be in protecting followers in realms of other faiths or in ensuring local religious figures stay true to the official doctrine. Hence a greater chance of conversion or other faiths popping up.

## Reply 125 — participant_012 · 2020-04-28 · post-26531023

<!-- artifact:quote:start -->
> spaninq said: I dunno, I think the idea of being a Christian heresy who can't be excommunicated (because you have no or are the religious head) and can't be Crusaded upon by other Christians sounds *very* useful. Click to expand...
<!-- artifact:quote:end -->
You can create incest, cannibalistic but ecumenical religion and thus not considered evil or even hostile by other Christians. Sounds fun

## Reply 126 — participant_033 · 2020-04-28 · post-26531025

<!-- artifact:quote:start -->
> viola said: Could you explain me the difference between winning and declaring a war? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Varus90 said: And what does one do when previous Holy Wars went well, even if one isn't opportunistic? Click to expand...
<!-- artifact:quote:end -->
I can certainly explain it to you, you just have to keep reading! Difficult task, apparently. So I do think so! And it took you this long to figure it out apparently.

## Reply 127 — participant_028 · 2020-04-28 · post-26531029

<!-- artifact:quote:start -->
> Illusive_Mike said: Do religious relations tenets like "Ecumenism" heavily restrict your other religious options? Because it seems both ahistorical and imbalanced from the gameplay perspective to be able to create a gender-equal pro-gay witchcraft-allowed party faith and have Catholics view you as only "astray". Click to expand...
<!-- artifact:quote:end -->
I think there is something that could be called "doctrinal restraints" at play here.

## Reply 128 — participant_057 · 2020-04-28 · post-26531032

<!-- artifact:quote:start -->
> Skales said: The only major heresy the Catholic blob was unable to crush, to the point that in-game it would hold provinces. Was Hussitism. Every other heresy was relegated to underground or obscurity. Click to expand...
<!-- artifact:quote:end -->
The Fraticelli were founded in 1278, immediately welcomed by the Armenian King, had a Holy Roman Emperor in 1328, and Count Stefano de' Conti was imprisoned for his heresy in 1466, with popular support (a county being Fraticelli with no ruler being Fraticelli) likely persisting for some time after. Probably the most frequently cited Medieval Catholic Philosopher, William Of Ockham, was a Fraticelli.

## Reply 129 — participant_033 · 2020-04-28 · post-26531041

<!-- artifact:quote:start -->
> wilcoxchar said: As it should. You (or your religious head) are in effect spending religious capital that you have built up in order to whip your followers into a frenzy over a land they've almost certainly never seen before thousands of miles away. Click to expand...
<!-- artifact:quote:end -->
That's "religious mana", and trying to apply it to real life is absurd. Local Catholics in 1066 Ireland should not lose faith in the system because Duke Rando in Austria declared war on a heathen neighbor. Now, if they hear about dozens of holy wars happening at once...

## Reply 130 — participant_073 · 2020-04-28 · post-26531042

Not sure I am a fan of the new 3d characters. Seem a bit uncanny to me. This seems like religion will be very diverse, however the sheer number of faiths makes me concerned the important ones: Catholic, Orthodox, Sunni, etc. will be a collection of traits pulled from the same pool of choices as something as obscure as Kushitic. Those big players should have a variety of unique features and events and the like, beyond a list of virtues vices and marriage restrictions.

## Reply 131 — participant_062 · 2020-04-28 · post-26531051

<!-- artifact:quote:start -->
> NarcomancerPL said: And that makes great point for Hussitism to appear in CK3 Click to expand...
<!-- artifact:quote:end -->
Definitely. Although note that Hussitism definitely did not come into being because the Catholic Church was winning too many holy wars

## Reply 132 — participant_072 · 2020-04-28 · post-26531053

<!-- artifact:quote:start -->
> FondMemberofSociety said: I think there is something that could be called "doctrinal restraints" at play here. Click to expand...
<!-- artifact:quote:end -->
That's exactly what I'm asking. How heavily does ecumenism (and various syncretism) restrict your doctrine options? And will it be viewable in the interface in some consice way beyond you having a bunch of doctrine options greyed out in various doctrine menus when you pick these tenets?

## Reply 133 — participant_016 · 2020-04-28 · post-26531056

<!-- artifact:quote:start -->
> Varus90 said: I can certainly explain it to you, you just have to keep reading! Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Varus90 said: Difficult task, apparently. Click to expand...
<!-- artifact:quote:end -->
I'm looking at it, and it looks like you really can't, sorry to say. You clearly know about it. Next time try actually reading the dev diaries before having to change your tune mid-argument.

## Reply 134 — participant_053 · 2020-04-28 · post-26531063

<!-- artifact:quote:start -->
> MinotaurWarrior said: The Fraticelli were founded in 1278, immediately welcomed by the Armenian King, had a Holy Roman Emperor in 1328, and Count Stefano de' Conti was imprisoned for his heresy in 1466, with popular support (a county being Fraticelli with no ruler being Fraticelli) likely persisting for some time after. Probably the most frequently cited Medieval Catholic Philosopher, William Of Ockham, was a Fraticelli. Click to expand...
<!-- artifact:quote:end -->
So that's Catharism, Waldensianism, Fraticelli... Wow it sure seems like the only Catholic heresy that's being carried over from CK2 that did get quickly suppressed was Lollardy. And that still lasted long enough to be absorbed into the Reformation.

## Reply 135 — participant_040 · 2020-04-28 · post-26531066

Also, just curious: what is a Sun Trial?

## Reply 136 — participant_028 · 2020-04-28 · post-26531076

<!-- artifact:quote:start -->
> Illusive_Mike said: That's exactly what I'm asking. How heavily does ecumenism (and various syncretism) restrict your doctrine options? And will it be viewable in the interface in some consice way beyond you having a bunch of doctrine options greyed out in various doctrine menus when you pick these tenets? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Xain said: Also, just curious: what is a Sun Trial? Click to expand...
<!-- artifact:quote:end -->
Will post a few of my takes on the issue. Ecumenism should not be a tenet, but something like HOI global tension that is a measure of unity in the church. Low ecumenism will see churches seceding and forming their own faiths; Doctrines take precedence to tenets according to previous dds, so the doctrines that make ecumenism possible in the first place would exclude the more ... outlandish options. *Insert CK2 Zunist gameplay experience here.

## Reply 137 — participant_033 · 2020-04-28 · post-26531093

<!-- artifact:quote:start -->
> wilcoxchar said: So that's Catharism, Waldensianism, Fraticelli... Wow it sure seems like the only Catholic heresy that's being carried over from CK2 that did get quickly suppressed was Lollardy. And that still lasted long enough to be absorbed into the Reformation. Click to expand...
<!-- artifact:quote:end -->
And that's why the Reformation was unnecessary, because there were so many other existing Christian religions to join already and be tolerated by the political authority! Wait. Maybe then there were no wars to suppress the Reformation because Fervor was so low? Wait. Look, it isn't impossible for it to have happened. But again...it should be harder for them to get a grasp on political control and keep it, making it something worthy of an achievement rather than yet another Reddit screenshot of "Lollard WC by 1100".

## Reply 138 — participant_028 · 2020-04-28 · post-26531117

<!-- artifact:quote:start -->
> Varus90 said: "Lollard WC by 1100" Click to expand...
<!-- artifact:quote:end -->
Did the player in question do it with an Altaic culture character?

## Reply 139 — participant_062 · 2020-04-28 · post-26531120

<!-- artifact:quote:start -->
> wilcoxchar said: So that's Catharism, Waldensianism, Fraticelli... Wow it sure seems like the only Catholic heresy that's being carried over from CK2 that did get quickly suppressed was Lollardy. And that still lasted long enough to be absorbed into the Reformation. Click to expand...
<!-- artifact:quote:end -->
Did any of those hold large, contiguous land areas for a long period of time? No? Did they only get a few isolated people and a very occasional ruler? Seems pretty suppressed to me.

## Reply 140 — participant_033 · 2020-04-28 · post-26531128

<!-- artifact:quote:start -->
> Xain said: Also, just curious: what is a Sun Trial? Click to expand...
<!-- artifact:quote:end -->
*(no text body — reaction-only or media-only post)*

## Reply 141 — participant_074 · 2020-04-28 · post-26531148

I really need to read through all these dev diaries when we get a release date.

## Reply 142 — participant_073 · 2020-04-28 · post-26531166

<!-- artifact:quote:start -->
> General Von Trapp said: I really need to read through all these dev diaries when we get a release date. Click to expand...
<!-- artifact:quote:end -->
All we know is "Fall" as it was said during a earnings report they posted on Twitch.

## Reply 143 — participant_053 · 2020-04-28 · post-26531187

<!-- artifact:quote:start -->
> Varus90 said: And that's why the Reformation was unnecessary, because there were so many other existing Christian religions to join already and be tolerated by the political authority! Wait. Maybe then there were no wars to suppress the Reformation because Fervor was so low? Wait. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Varus90 said: Look, it isn't impossible for it to have happened. But again...it should be harder for them to get a grasp on political control and keep it, making it something worthy of an achievement rather than yet another Reddit screenshot of "Lollard WC by 1100". Click to expand...
<!-- artifact:quote:end -->
Gee, it's almost like the Catholic Church declaring a bunch of Holy Wars against Granada, North Africa, the New World, the Hussites, the Ottomans, etc. and a few scandalous Popes, indulgence peddling, and a couple politically motivated excommunications and refusals to grant divorces did enough to lower Catholic Fervor that a few priests and princes created their own faiths instead and were able to quickly convert a large area. Then I have good news for you. It sounds like it will be very difficult to achieve a Lollard world conquest by 1100 precisely because of the fervor mechanic. If Lollardy is spreading that much that fast, it's likely because of holy wars, so that will lower Lollard fervor and make it easier for Catholics to convert Lollard provinces and characters back. The fervor mechanic will work both ways, you know.

## Reply 144 — participant_033 · 2020-04-28 · post-26531208

<!-- artifact:quote:start -->
> viola said: I'm looking at it, and it looks like you really can't, sorry to say. You clearly know about it. Next time try actually reading the dev diaries before having to change your tune mid-argument. Click to expand...
<!-- artifact:quote:end -->
Objection: badgering. Note the lack of content or explanation for the arrival at the conclusion. After admitting that I was correct earlier in the page, and that they just like an unrealistic system, they claim that I switched positions by coming down against unrealistic systems, which (historical) is what I said to begin with. This simply proves that you can't or won't read other people's arguments and just have a personal preference that you think should be immutable game design law. I do think we're done here. You like things unrealistic (except the things you don't, like Aztecs and bears), others do as well, others do not. That's how it'll be.

## Reply 145 — participant_033 · 2020-04-28 · post-26531221

<!-- artifact:quote:start -->
> wilcoxchar said: Gee, it's almost like the Catholic Church declaring a bunch of Holy Wars against Granada, North Africa, the New World, the Hussites, the Ottomans, etc. and a few scandalous Popes, indulgence peddling, and a couple politically motivated excommunications and refusals to grant divorces did enough to lower Catholic Fervor that a few priests and princes created their own faiths instead and were able to quickly convert a large area. Click to expand...
<!-- artifact:quote:end -->
Gee, it's almost like that's reform desire from EUIV, which is out of the game time scale.

## Reply 146 — participant_053 · 2020-04-28 · post-26531225

<!-- artifact:quote:start -->
> Varus90 said: Gee, it's almost like that's reform desire from EUIV, which is out of the game time scale. Click to expand...
<!-- artifact:quote:end -->
You're the one who tried bringing the reasons for the Reformation into this, so not sure what you're complaining about.

## Reply 147 — participant_033 · 2020-04-28 · post-26531255

<!-- artifact:quote:start -->
> wilcoxchar said: You're the one who tried bringing the reasons for the Reformation into this, so not sure what you're complaining about. Click to expand...
<!-- artifact:quote:end -->
I was responding to your bringing up the Reformation, yes. It may have laid the groundwork for it, but that's neither here nor there in terms of gameplay. It would be very interesting to see a game that's just about religious doctrinal struggles for a thousand years, but what matters in CK is land and money. EUIV's custom Protestant faiths, while underwhelming, are what you're thinking of here.

## Reply 148 — participant_075 · 2020-04-28 · post-26531265

Is there any relationship that can make a religion defend other religions in holy wars? That's something that's really important for both modding and stuff like the Sunni schools. Two separate states for when they do defend other members of the religion and where they simply have no negative modifiers are important.

## Reply 149 — participant_076 · 2020-04-28 · post-26531276

<!-- artifact:quote:start -->
> halbort said: I think Holy Wars should give Fervor but only if you do not take the land for yourself. You should gain Fervor for giving the land to the pope. Click to expand...
<!-- artifact:quote:end -->
Fervour is a number universal for all Catholics.

## Reply 150 — participant_014 · 2020-04-28 · post-26531294

clearly there is a large faction who prefers unrealistic constraints and nonsensical systems in place to force outcomes that they like in this game - the OP seems to confirm that that's the direction Paradox is taking with this game, which doesn't bode well for its realism. Not that I had much hope for it anyway.

## Reply 151 — participant_028 · 2020-04-28 · post-26531310

Guys let's try not to derail this thread ok? Anyway, I am going to follow in the footsteps of Torngasuk, and post a thread on grand scale facsimile on the church - some time ago, faiths alone convinced me to buy the game on release, but I have been ... awakened by this DD. Churches are something different from faiths - and with them in place, many problems would be solved.

## Reply 152 — participant_053 · 2020-04-28 · post-26531314

<!-- artifact:quote:start -->
> Varus90 said: I was responding to your bringing up the Reformation, yes. It may have laid the groundwork for it, but that's neither here nor there in terms of gameplay. It would be very interesting to see a game that's just about religious doctrinal struggles for a thousand years, but what matters in CK is land and money. EUIV's custom Protestant faiths, while underwhelming, are what you're thinking of here. Click to expand...
<!-- artifact:quote:end -->
I suggest you read up on the actual histories of these heresies, since it's pretty clear you don't really understand the extent of many of them into the 15th and 16th centuries and the roles they played both in interacting with and separate from the Reformation. Especially with respect to Waldensians and the Swiss Reformation. Anyway, the original comment about it taking centuries to suppress a faith wasn't just about heresies. You just need to look at the histories of religions like Zoroastrianism and various what would be in-game pagan faiths (especially in Africa) in the face of Christian and Muslim conquests to see how they actually lasted quite long in the face of an advancing larger religion.

## Reply 153 — participant_053 · 2020-04-28 · post-26531327

<!-- artifact:quote:start -->
> Zhetone said: clearly there is a large faction who prefers unrealistic constraints and nonsensical systems in place to force outcomes that they like in this game - the OP seems to confirm that that's the direction Paradox is taking with this game, which doesn't bode well for its realism. Not that I had much hope for it anyway. Click to expand...
<!-- artifact:quote:end -->
Gameplay and fun should always be prioritized over historical determinism when those priorities clash.

## Reply 154 — participant_033 · 2020-04-28 · post-26531340

<!-- artifact:quote:start -->
> wilcoxchar said: I suggest you read up on the actual histories of these heresies, since it's pretty clear you don't really understand the extent of many of them into the 15th and 16th centuries and the roles they played both in interacting with and separate from the Reformation. Especially with respect to Waldensians and the Swiss Reformation. Click to expand...
<!-- artifact:quote:end -->
Again you bring up the Reformation, something which will not be part of the game's timeline. It is an interesting topic, that's true. A game based entirely on religious divisions in the era could be very good. But, since CK simplifies things for the sake of gameplay, and obviously we did not see Catholic hold on the majority of non-Orthodox Europe broken before then, not too relevant at this point in time. CK2 and 3 end halfway through the 15th century and most players will not even reach that. And since you argue that gameplay is more important than historical realism, why are you citing history to justify your view? If you want unrealistic outcomes, that's just one viewpoint you can just say.

## Reply 155 — participant_028 · 2020-04-28 · post-26531350

<!-- artifact:quote:start -->
> wilcoxchar said: Gameplay and fun should always be prioritized over historical determinism when those priorities clash. Click to expand...
<!-- artifact:quote:end -->
Hoping mechanics are actually a facsimile of history instead of counteracting history is not too much to ask.

## Reply 156 — participant_053 · 2020-04-28 · post-26531357

<!-- artifact:quote:start -->
> Varus90 said: Again you bring up the Reformation, something which will not be part of the game's timeline. It is an interesting topic, that's true. A game based entirely on religious divisions in the era could be very good. But, since CK simplifies things for the sake of gameplay, and obviously we did not see Catholic hold on the majority of non-Orthodox Europe broken before then, not too relevant at this point in time. CK2 and 3 end halfway through the 15th century and most players will not even reach that. Click to expand...
<!-- artifact:quote:end -->
I'm only bringing up the Reformation to show how they were not as easily suppressed as you and others seem to think and show just how long they lasted in a strong enough position to remain represented in the game.

## Reply 157 — participant_053 · 2020-04-28 · post-26531361

<!-- artifact:quote:start -->
> FondMemberofSociety said: Hoping mechanics are actually a facsimile of history instead of counteracting history is not too much to ask. Click to expand...
<!-- artifact:quote:end -->
Mechanics should be a emulation of historical processes, not historical outcomes. The outcomes should be at the whims of the decision-making of the AI, the player, and chance.

## Reply 158 — participant_077 · 2020-04-28 · post-26531362

Does the conversion vulnerability from low fervor balance out with pagan conversion penalty? So if Catholicism is falling apart, the Norse can actually convert England?

## Reply 159 — participant_028 · 2020-04-28 · post-26531379

<!-- artifact:quote:start -->
> wilcoxchar said: Mechanics should be a emulation of historical processes, not historical outcomes. Click to expand...
<!-- artifact:quote:end -->
If declaring 8 Crusades of increasingly pathetic military successes boosted Catholic fervor, I'd really like to see the historical process behind it.

## Reply 160 — participant_025 · 2020-04-28 · post-26531391

<!-- artifact:quote:start -->
> wilcoxchar said: I think you have it backwards. You need to whip people up into a religious fervor to get them motivated enough to declare the Holy War, otherwise most people are just going to shrug and question why they're being asked to fight a war thousands of miles away. For the purpose of declaring holy wars, fervor is more like political capital. Click to expand...
<!-- artifact:quote:end -->
I actually think calling a Holy War would be akin to a populist move: something people want to hear, that they've been waiting for. I modeled my previous post in something closer in time, sine it's better understood and better documented than what happened in the Middle Ages, and since it must've been a similar feeling to a medieval mindset immersed in religious fervor: the nationalistic fervor at the outbreak of WWI. It was something that was brewing for decades, the troops marched to the front singing, confident in a quick victory and being back home for Christmas, but then the war extended, and the attrition and hardships melted the fervor away. Surely, by the Fourth Crusade some people may have gone "What we're fighting for, again?". But the initial reaction is what should be taken into account. NOTE: I'm not trying to discuss WWI here, I'm just explaining my mindset and what this mechanic made me think of. Heck, even something mundane like an important football match could be used to parallel the effect: the people don't need to be stirred up for the match; they're stirred up because of it. And winning stirs them even more! Like I said, I understand where the mechanic's coming from (at least I think so), but it doesn't seem all that realistic to me.

## Reply 161 — participant_033 · 2020-04-28 · post-26531414

Okay, okay, now. On consideration, I actually am completely behind the idea that you cannot declare a Crusade/Jihad/etc. if there's low Fervor, because that both makes historical sense and is a good gameplay balance tool which should please both sides. I'm not sure about not declaring holy wars at all (not sure if that's what they mean?) however, unless Fervor hits 0, because yeah, there's always going to be someone who just wants a war and calls it holy. Still don't think the actual declaration should be what causes the dip, or victory, though.

## Reply 162 — participant_053 · 2020-04-28 · post-26531428

<!-- artifact:quote:start -->
> Bearnest said: I actually think calling a Holy War would be akin to a populist move: something people want to hear, that they've been waiting for. I modeled my previous post in something closer in time, sine it's better understood and better documented than what happened in the Middle Ages, and since it must've been a similar feeling to a medieval mindset immersed in religious fervor: the nationalistic fervor at the outbreak of WWI. It was something that was brewing for decades, the troops marched to the front singing, confident in a quick victory and being back home for Christmas, but then the war extended, and the attrition and hardships melted the fervor away. Surely, by the Fourth Crusade some people may have gone "What we're fighting for, again?". But the initial reaction is what should be taken into account. NOTE: I'm not trying to discuss WWI here, I'm just explaining my mindset and what this mechanic made me think of. Heck, even something mundane like an important football match could be used to parallel the effect: the people don't need to be stirred up for the match; they're stirred up because of it. And winning stirs them even more! Like I said, I understand where the mechanic's coming from (at least I think so), but it doesn't seem all that realistic to me. Click to expand...
<!-- artifact:quote:end -->
But that fervor you describe is what is being represented. The fervor prior to the declaration of the crusade, the fervor drummed up by the fall of Nicaea (First), the fall of Edessa (Second), or the fall of Jerusalem (Third Crusade). The actual declaration of the crusade is just utilizing the pent up fervor to get people to go off to the war, when the anticipation of "someone must do something" is wiped out and the reality of the work and strife of the fight sets in. What you're talking about for the purpose of the CK3 time period is a reason to build up fervor in preparation for declaring a holy war, not a boost in fervor by declaring a crusade. If you declare a holy war at high fervor, it's not going to hurt the religious cohesion much because you've already swept the people up in the cause. If you declare a holy war at low fervor though, it's not going to suddenly make people less disillusioned, it's just going to look like a desperate and cynical ploy to drum up favor and people are going to be even more disillusioned by the idea of fighting for a religious head they don't have much faith in. People don't take up arms and then invent a reason to justify having done it. They invent a reason to fight and then use that as justification to take up arms.

## Reply 163 — participant_062 · 2020-04-28 · post-26531440

<!-- artifact:quote:start -->
> wilcoxchar said: Mechanics should be a emulation of historical processes, not historical outcomes. The outcomes should be at the whims of the decision-making of the AI, the player, and chance. Click to expand...
<!-- artifact:quote:end -->
I am sorry, but if you do mechanics that properly simulate historical processes. You are fairly likely to end up with outcomes similar-ish to history. Which is not what you want, you want 'gameplay' to take priority, which is your choice entirely. But 'gameplay' can mean different things for different people, not including the large section of the fanbase who just like immersing themselves in a historical setting. Truth be told. I have always wanted Paradox to look at the games they are making this way 'With our current mechanics, would it, theoretically, be possible to recreate real history?'. The answer for most of their games would sadly be no, and that is fine. But they should strive to get close, in my opinion.

## Reply 164 — participant_053 · 2020-04-28 · post-26531467

<!-- artifact:quote:start -->
> Skales said: I am sorry, but if you do mechanics that properly simulate historical processes. You are fairly likely to end up with outcomes similar-ish to history. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Skales said: Which is not what you want, you want 'gameplay' to take priority, which is your choice entirely. But 'gameplay' can mean different things for different people, not including the large section of the fanbase who just like immersing themselves in a historical setting. Truth be told. I have always wanted Paradox to look at the games they are making this way 'With our current mechanics, would it, theoretically, be possible to recreate real history?'. The answer for most of their games would sadly be no, and that is fine. But they should strive to get close, in my opinion. Click to expand...
<!-- artifact:quote:end -->
Not necessarily. The processes would be capable of producing a similar outcome to history, but only if the same or similar players make the same or similar decisions to history, use the processes at the same or similar times to history, and have the same or similar luck as history continuously throughout the game. A process is merely that, a process. It can easily produce a wide range of different outputs based on different inputs. Theoretically, yes, in all Paradox games it is possible to recreate real history. If you have every controllable entity acting exactly as they did historically, you can recreate quite closely to real history in a Paradox game. But the player is very unlikely to do that, and you need to have the AI capable of reacting to the player's alternate decisions or to the alternate decisions of the other AI. A game that prioritized recreating real history would be either extremely limited and unfun in how the player could interact with it or be quickly made ridiculous by the player deviating because of their foresight as to what happened historically.

## Reply 165 — participant_062 · 2020-04-28 · post-26531480

<!-- artifact:quote:start -->
> wilcoxchar said: Not necessarily. The processes would be capable of producing a similar outcome to history, but only if the same or similar players make the same or similar decisions to history, use the processes at the same or similar times to history, and have the same or similar luck as history continuously throughout the game. A process is merely that, a process. It can easily produce a wide range of different outputs based on different inputs. Theoretically, yes, in all Paradox games it is possible to recreate real history. If you have every controllable entity acting exactly as they did historically, you can recreate quite closely to real history in a Paradox game. But the player is very unlikely to do that, and you need to have the AI capable of reacting to the player's alternate decisions or to the alternate decisions of the other AI. A game that prioritized recreating real history would be either extremely limited and unfun in how the player could interact with it or be quickly made ridiculous by the player deviating because of their foresight as to what happened historically. Click to expand...
<!-- artifact:quote:end -->
No, you really can't. There would be lacking mechanics all over the place, which is fine, you can't possibly represent every edge case. But you should definitely strive to do so. Ideally with mechanics that can be applied and interpreted broadly.

## Reply 166 — participant_078 · 2020-04-28 · post-26531499

Can we have something similar to Fervour for culture, so that cultures have little holdouts against total annihilation? (It could also encourage massive cultures to fracture into regional variants). You could even have it so that less valuable and controllable places (deep forest, mountains, deserts) are harder to convert than plains and farmlands, so even massive empires have little pockets and enclaves of "old" cultures in their hinterlands.

## Reply 167 — participant_053 · 2020-04-28 · post-26531517

<!-- artifact:quote:start -->
> Kenlin said: Can we have something similar to Fervour for culture, so that cultures have little holdouts against total annihilation? (It could also encourage massive cultures to fracture into regional variants). You could even have it so that less valuable and controllable places (deep forest, mountains, deserts) are harder to convert than plains and farmlands, so even massive empires have little pockets and enclaves of "old" cultures in their hinterlands. Click to expand...
<!-- artifact:quote:end -->
I would like this as well. The era CK3 covers, especially the late era, was the first emergence of modern nationalism, with (off the top of my head) unified French, Italian, Dutch, Swiss, Spanish, and English nations starting to be solidified near the endgame years. A more dynamic process for cultural shifts would be interesting too, with things like Tuscan, Lombard, and others lasting longer but perhaps in the later game being able to rise as the dominant culture of their group like Tuscan did with Italian (and yes I know that was primarily in the linguistic aspect of culture).

## Reply 168 — participant_025 · 2020-04-28 · post-26531525

<!-- artifact:quote:start -->
> wilcoxchar said: People don't take up arms and then invent a reason to justify having done it. They invent a reason to fight and then use that as justification to take up arms. Click to expand...
<!-- artifact:quote:end -->
Ok, we probably have different concepts. What I've been saying is that people would rejoice to take up arms if that's what they've wanted to do all along. To sum up my previous post: Fervor shouldn't take a dip because a HW has been called, it should spike because that's what people have been wanting to hear. I'll repeat myself (again) that I don't have anything against the mechanic, but I think it's a little unrealistic and probably should be tweaked to raise the fervor after the first HW is called, but later sink if this is exploited (e.g. if declaring another one before 50 years -or a century- has passed, but the cooldown being something like 30 years before you can call another; in this way, if the mechanic is abused, it'll wear out the previous Fervor, and the Fervor won after the HW)

## Reply 169 — participant_053 · 2020-04-28 · post-26531535

<!-- artifact:quote:start -->
> Bearnest said: Ok, we probably have different concepts. What I've been saying is that people would rejoice to take up arms if that's what they've wanted to do all along. To sum up my previous post: Fervor shouldn't take a dip because a HW has been called, it should spike because that's what people have been wanting to hear. I'll repeat myself (again) that I don't have anything against the mechanic, but I think it's a little unrealistic and probably should be tweaked to raise the fervor after the first HW is called, but later sink if this is exploited (e.g. if declaring another one before 50 years -or a century- has passed, but the cooldown being something like 30 years before you can call another; in this way, if the mechanic is abused, it'll wear out the previous Fervor, and the Fervor won after the HW) Click to expand...
<!-- artifact:quote:end -->
But that's what I'm saying. They are rejoicing in taking up arms. That people have been wanting to hear and call for a holy war is represented by the preexisting fervor. Actually taking the action, they are expending that existing energy by taking up arms.

## Reply 170 — participant_033 · 2020-04-28 · post-26531568

<!-- artifact:quote:start -->
> wilcoxchar said: But that's what I'm saying. They are rejoicing in taking up arms. That people have been wanting to hear and call for a holy war is represented by the preexisting fervor. Actually taking the action, they are expending that existing energy by taking up arms. Click to expand...
<!-- artifact:quote:end -->
Faith isn't a zero-sum game, though... although granted, the piety mechanic makes it seem that way, but that's getting a rework, too. Point is, you can stay excited while doing something, especially when you see how many other people are, too.

## Reply 171 — participant_057 · 2020-04-28 · post-26531623

<!-- artifact:quote:start -->
> Varus90 said: Faith isn't a zero-sum game, though... although granted, the piety mechanic makes it seem that way, but that's getting a rework, too. Point is, you can stay excited while doing something, especially when you see how many other people are, too. Click to expand...
<!-- artifact:quote:end -->
But is it approximately Zero Sum? Remember, declaring a holy war has a "slight" penalty to Fervor. In reality, religious fervor is an impossibly complex multidimensional phenomenon. But is it approximately true that a motivation of any kind can only be used to motivate a finite number of things. To declare a GHW, Fervor must be high. Declaring it will slightly decrease it - so it will still be high.

## Reply 172 — participant_053 · 2020-04-28 · post-26531646

<!-- artifact:quote:start -->
> Baron von Shoes said: We have the AI play automated games every night, and the 'big' faiths like Catholicism and Ash'ari generally remain quite powerful. Even though they regularly suffer from heresy outbreaks, their sheer bulk and military might means they almost always end up re-asserting themselves as a dominant power. Click to expand...
<!-- artifact:quote:end -->
Also, on this note, it would be great if we could see a screenshot or two of the result of some of the automated games at some point. Just a thought.

## Reply 173 — participant_062 · 2020-04-28 · post-26531676

<!-- artifact:quote:start -->
> wilcoxchar said: Also, on this note, it would be great if we could see a screenshot or two of the result of some of the automated games at some point. Just a thought. Click to expand...
<!-- artifact:quote:end -->
Not wanting to be a pessimist, but the border gore, which we all deep inside know will be there. Will probably discourage many players once they actually see it.

## Reply 174 — participant_079 · 2020-04-28 · post-26531696

Is Religious Hostility going to be a static modifier? If so, shouldn't you consider to make it a more dynamic system, maybe letting each faith change his point of view towards other faiths?

## Reply 175 — participant_080 · 2020-04-28 · post-26531716

<!-- artifact:quote:start -->
> TheMind said: Is Religious Hostility going to be a static modifier? If so, shouldn't you consider to make it a more dynamic system, maybe letting each faith change his point of view towards other faiths? Click to expand...
<!-- artifact:quote:end -->
I'm not sure it would be a good idea to keep track of individual stances to other faiths in game with there being over 100.

## Reply 176 — participant_062 · 2020-04-28 · post-26531719

<!-- artifact:quote:start -->
> Blackwhitecavias said: I'm not sure it would be a good idea to keep track of individual stances to other faiths in game with there being over 100. Click to expand...
<!-- artifact:quote:end -->
Give the player additional reason to holy war and destroy other faiths PERFORMANCE V*LT.

## Reply 177 — participant_057 · 2020-04-28 · post-26531760

<!-- artifact:quote:start -->
> Blackwhitecavias said: I'm not sure it would be a good idea to keep track of individual stances to other faiths in game with there being over 100. Click to expand...
<!-- artifact:quote:end -->
The game keeps track of individual relationships between characters with there being well over a hundred. I'm sure it must fudge a lot of that, but if that can be fudged I'm sure this can be too.

## Reply 178 — participant_081 · 2020-04-28 · post-26531839

So Fervour is an anti-blobbing mechanism however i'm unsure on what defines low Fervour ,amount wise, and what defines fervour which is reduced from declaring HW because i'm not too sure if being more susceptible to conversion after you defeated some infidels makes sense, i must be missing something here or im a bit stupid?

## Reply 179 — participant_080 · 2020-04-28 · post-26531891

<!-- artifact:quote:start -->
> MinotaurWarrior said: The game keeps track of individual relationships between characters with there being well over a hundred. I'm sure it must fudge a lot of that, but if that can be fudged I'm sure this can be too. Click to expand...
<!-- artifact:quote:end -->
I wasn't talking about performance in this case, but making it clear to the player: Having a list with the relation to each other religion wouldn't really work, so it would be at least a bit obscure.

## Reply 180 — participant_057 · 2020-04-28 · post-26531945

<!-- artifact:quote:start -->
> Blackwhitecavias said: I wasn't talking about performance in this case, but making it clear to the player: Having a list with the relation to each other religion wouldn't really work, so it would be at least a bit obscure. Click to expand...
<!-- artifact:quote:end -->
I mean that applies to character relationships as well. I've never even tried to understand who hates who beyond scrolling for yellow thumbs in CKII. Even without dynamic hostility, I feel like there's a good chance I'll occasionally forget who is ecumenical or syncretic and presumably I'll be able to mouse over the faith icon and see "Astray" or maybe there will be a list on my faith tab. Worst case scenario, I mouse over a character of that faith and see their opinion modifier. This actually reminds me of something - will we be able to see the causes of other Faith's fervor? Occasionally in CKII I'd secretly covert - > personally adopt - > adopt local faith just to see that info.

## Reply 181 — participant_082 · 2020-04-29 · post-26532077

So, I have a question: Will there be a way for Muslim faiths to be more tolerant of non-Muslim Abrahamics within the same realm? Perhaps a Doctrine? I'm thinking the Umayyads here, since they had no real problem with having dhimmi administrators but fought jihads like the rest.

## Reply 182 — participant_028 · 2020-04-29 · post-26532174

<!-- artifact:quote:start -->
> Ramidel said: So, I have a question: Will there be a way for Muslim faiths to be more tolerant of non-Muslim Abrahamics within the same realm? Perhaps a Doctrine? I'm thinking the Umayyads here, since they had no real problem with having dhimmi administrators but fought jihads like the rest. Click to expand...
<!-- artifact:quote:end -->
The People of the book doctrine, hmmm. Sounds interesting enough, I guess we would have to wait and see.

## Reply 183 — participant_083 · 2020-04-29 · post-26532293

F-Fervor!?... Oh god, please don't repeat Creative Assembly's mistake. Let's get it right the first time.

## Reply 184 — participant_084 · 2020-04-29 · post-26532331

so this is stupid and nitpicky and maybe not in the appropriate place but today I discovered in the ck2 files that for some reason "Brahma" is listed as the high god for Buddhism. Can you please make sure not to have such an error in the next game. This is the equivalent of having the son of the Christian god being named Satan. I can see how this error was made as Brahma is listed as king of the Gods in some texts, but "Gods" in Buddhism aren't seen in the same light as Gods in other faiths. In Buddhism a being that is qualified as a God doesn't necessarily have any more divinity than a human would, they just experience an existence that is magnitudes more enjoyable. Only beings that are on the path of enlightenment are worthy of being described as divine. I respect that this game isn't specifically focused on the religions of the Indian subcontinent but if they are going to be included it seems important that they are at least represented in an appropriate way. Some appropriate terms would include Buddha (awakened one - this is the ultimate be-all and end-all), Arhat (one who has gained insight into the true nature of existence and has achieved nirvana), Tathagata (one who has come, one who has gone), Bodhisattva (one whose goal is awakening), Dakini (sky dancer/wind dancer - the embodiment of female enlightened energy). There is also not just one Buddha as Buddhahood or enlightenment is the ultimate goal for all practitioners. If this issue has been addressed please just ignore my comment. I'm not trying to be obnoxious at all. I only just noticed as I don't play Buddhist characters very often as they don't really have any interesting mechanics compared to the depth and richness of other faiths. Though I am truly looking forward to what you guys are working on with this next iteration! Thanks for listening to the ramblings of an enthused Buddhist!

## Reply 185 — participant_085 · 2020-04-29 · post-26532338

<!-- artifact:quote:start -->
> fodazd said: I think that making holy wars cost fervor to declare and giving the target a fervor bonus when they lose is a really good change. It will hopefully prevent situations typical for CK2, where one faith sits at a permanent 100 MA for winning a lot of holy wars, and every other religion falls into a death spiral of low MA. It also means that you can no longer use holy wars as a basically free CB for grabbing unlimited land. I am curious how the faith hostility system will play out in practice, but it does seem to differentiate the three religious families from each other significantly, which I appreciate. Click to expand...
<!-- artifact:quote:end -->
Exactly. No more Catholicism sitting at 0 MA in earlier starts because of Vikings. No more ridiculous Holy War exploits. No more Heresy spirals.

## Reply 186 — participant_086 · 2020-04-29 · post-26532366

I like the new hostility system (though evil seems a bit strong, for instance this is saying a Muslim views other people of the book as evil). Now seeing the religious hostility system, I still don't see why oriental religion group makes sense for Zoroastrianism. The last major Zoroastrian power (the Sasanian Empire) persecuted not just other religious families (Christians), but also the Manicheans, who I assume are in the same religious family as Zoroastrianism. Additionally, Zoroastrianism, and related religious like Yazidism, aren't for marrying outside your faith. Both of those don't seem to fit well with the Oriental religious families' hostility settings.

## Reply 187 — participant_016 · 2020-04-29 · post-26532372

<!-- artifact:quote:start -->
> pengoyo said: I like the new hostility system (though evil seems a bit strong, for instance this is saying a Muslim views other people of the book as evil). Now seeing the religious hostility system, I still don't see why oriental religion group makes sense for Zoroastrianism. The last major Zoroastrian power (the Sasanian Empire) persecuted not just other religious families (Christians), but also the Manicheans, who I assume are in the same religious family as Zoroastrianism. Additionally, Zoroastrianism, and related religious like Yazidism, aren't for marrying outside your faith. Both of those don't seem to fit well with the Oriental religious families' hostility settings. Click to expand...
<!-- artifact:quote:end -->
The Oriental/Eastern group could definitely be helped with a split. I'm thinking of an Iranian group for Zoroastrianism and other faiths in the sphere of the old Persian empire, an Indian group for Dharmic religions and an Eastern group for Chinese religions which are apparently in the game and don't really fit with Hinduism honestly.

## Reply 188 — participant_087 · 2020-04-30 · post-26532611

Looks fantastic, wish heresies were more based in politics than fervor though. Historically the big heresies of the era were more about rejecting failures in the political establishment as a whole than feeling there wasnt enough faith or caused by widespready apathy or disbelief. In a way if fervor wasnt really high, dissidents wouldn't go to heresy but more secular directions anyway. And if heresies are just about belief then well, "Adherents of a Faith with high Fervor are willing to fight and die for their beliefs." that's how those kinds of heresies start. when fervor is so high that focus on a small part of it spirals into a major dispute. I don't know how I'd prefer it though. Maybe have fervor give all the boons and bonuses but raise heresy chance? so it's a balance game, you can raise fervor for the modifiers and holy wars etc, but that runs the risk of fervor getting peasents taking religion a bit too far/rebels turning to religion/dangerous aspects of the faith being raised in awareness/etc and heresies breaking out? instead of, it being an all good one side, all bad the other. if people dont care about religion enough.. heresies?

## Reply 189 — participant_088 · 2020-04-30 · post-26532853

I don't think the idea of rulers as heresiarchs is particularly accurate, unfortunately. CK2's system was a better rendition, in this regard. But the intermarriages between different religions (except those regarding the other as 'evil') are a very welcome and historical addition! (EDIT: Although I just saw the spreadsheet apparently showing that no Muslim-Christian marriages are allowed, even now... which is, demonstrably, ahistorical.)

## Reply 190 — participant_089 · 2020-04-30 · post-26533444

<!-- artifact:quote:start -->
> Baron von Shoes said: However, while these Holy Wars are ostensibly waged in the name of the divine, in practice they often tend to be little more than opportunistic land-grabs — as a result, every Holy War declared will slightly damage a Faiths’ Fervor! Click to expand...
<!-- artifact:quote:end -->
Will this be the case for Holy Wars only or Great Holy Wars too? I can see why the former might reduce Fervor, but the latter less so. The capture a great, almost mythical, city or land of your faith would surely be a source of great awe for your people. Whether or not you believe that the motivations we holy or not (which there are good arguments either way for) the impact it would have on the faith's people, literature and music would undoubtedly be positive. Also, on a totally separate point, how hard will it be to convert the populace as a smaller religion? Are we talking like CK2 where you only have like 1% chance of converting a county or will it be higher? One of my major gripes with CK2 was that playing alt-history with religions was near on impossible for some due to the way holy sites worked. If you wanted to play a Monophysite Italy or a Manichaen North Africa, you could pretty much forget about it because you were so far away from the holy sites that you never get your MA high enough to convert provinces. It would be nice if there was a bit more flexibility and if you, for example, moved the head of your religion to your realm, therefore making your lands the faith's base of operations, then that would have a significant impact on your ability to convert provinces.

## Reply 191 — participant_047 · 2020-04-30 · post-26533533

So, if anyone else was curious, miracle worker is apparently the trait you get at the end of the mystic tree where you've cultivated a reputation for having magical powers. You don't actually have magical powers mind you, but people think you do. Also, I learned about a tenet called adoricism which I had to google and it's apparently the opposite of exorcism where you attract a spirit to possess you. I got both of these from the Discord dev questions btw. So! Right now I'm thinking: female dominated Gnostic faith in Wales with esotericism, adoricism and something else suitable as the tenets. The Demiurge and his shepards are leading the world astray. They will be freed. Maybe an AAR called the Witches of Wales.

## Reply 192 — participant_028 · 2020-04-30 · post-26533557

<!-- artifact:quote:start -->
> classicist said: (EDIT: Although I just saw the spreadsheet apparently showing that no Muslim-Christian marriages are allowed, even now... which is, demonstrably, ahistorical.) Click to expand...
<!-- artifact:quote:end -->
Just asking here, but which Christian denominations did intermarry with Muslims? I don't really recall any ...

## Reply 193 — participant_090 · 2020-04-30 · post-26533747

<!-- artifact:quote:start -->
> FondMemberofSociety said: Just asking here, but which Christian denominations did intermarry with Muslims? I don't really recall any ... Click to expand...
<!-- artifact:quote:end -->
Emperors of Trebizond married off their daughters to Muslim rulers. As an example, https://en.wikipedia.org/wiki/Despina_Khatun

## Reply 194 — participant_091 · 2020-04-30 · post-26533765

Really cool dev diary!

## Reply 195 — participant_057 · 2020-04-30 · post-26533769

<!-- artifact:quote:start -->
> suplanter said: so this is stupid and nitpicky and maybe not in the appropriate place but today I discovered in the ck2 files that for some reason "Brahma" is listed as the high god for Buddhism. Can you please make sure not to have such an error in the next game. This is the equivalent of having the son of the Christian god being named Satan. I can see how this error was made as Brahma is listed as king of the Gods in some texts, but "Gods" in Buddhism aren't seen in the same light as Gods in other faiths. In Buddhism a being that is qualified as a God doesn't necessarily have any more divinity than a human would, they just experience an existence that is magnitudes more enjoyable. Only beings that are on the path of enlightenment are worthy of being described as divine. I respect that this game isn't specifically focused on the religions of the Indian subcontinent but if they are going to be included it seems important that they are at least represented in an appropriate way. Some appropriate terms would include Buddha (awakened one - this is the ultimate be-all and end-all), Arhat (one who has gained insight into the true nature of existence and has achieved nirvana), Tathagata (one who has come, one who has gone), Bodhisattva (one whose goal is awakening), Dakini (sky dancer/wind dancer - the embodiment of female enlightened energy). There is also not just one Buddha as Buddhahood or enlightenment is the ultimate goal for all practitioners. If this issue has been addressed please just ignore my comment. I'm not trying to be obnoxious at all. I only just noticed as I don't play Buddhist characters very often as they don't really have any interesting mechanics compared to the depth and richness of other faiths. Though I am truly looking forward to what you guys are working on with this next iteration! Thanks for listening to the ramblings of an enthused Buddhist! Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> pengoyo said: I like the new hostility system (though evil seems a bit strong, for instance this is saying a Muslim views other people of the book as evil). Now seeing the religious hostility system, I still don't see why oriental religion group makes sense for Zoroastrianism. The last major Zoroastrian power (the Sasanian Empire) persecuted not just other religious families (Christians), but also the Manicheans, who I assume are in the same religious family as Zoroastrianism. Additionally, Zoroastrianism, and related religious like Yazidism, aren't for marrying outside your faith. Both of those don't seem to fit well with the Oriental religious families' hostility settings. Click to expand...
<!-- artifact:quote:end -->
The bigger issue in CKII wasn't the name list, but the text that surrounded it. It doesn't make any sense to say, "They are with the Arhant now" on the ruler death screen, for instance. As well, there's the problem of the highly divergent sects. In any sect, if Brahma Sahampati shows up and tells your Buddhist ruler something, you'll know who that is and be enthused about "the voice of Brahma" but a Sri Lankan Theravadin is going to be like, "Dakini who?" Honestly, Buddhists and Jains are always going to be the odd ones out and unfortunately I bet there's still going to be some awfully hilarious madlibs from inserting their words into christian templates. Given that, I might rather they just use the names of lowly supernatural beings like Devas, Nagas, Garudas, etc, who do appear in visions in all on-map varieties of Buddhism and many of whom are unskillful enough to endorse wars and oppression. Also CKII Buddhists are pretty fun. Tibetans are like muslims without decadence and Indian Buddhists have open succession and kingdom-level subjugation. With Zoroastrianism it's tough, and doesn't track through their whole history. On the surface, Iranian and Indian religions consider each other to be, basically, demon worshippers, with Ahura / Asura and Daeva / Deva basically flipping side from one religious group to the other in terms of good and bad. Proto-Mazdan tribes were likely engaged in horrible religious warfare that drove Deva worshipers to India and the near east. Mazdans had prayers like the Frawardin Yasht section twelve, which talks about killing deva-worshippers by the hundreds of thousands of hundreds of thousands (AKA ten billion). But practically, they had much more antagonistic opportunities against non-deva worshippers, especially Christians and Muslims (just before the time of the game) and made only relatively minor, non-genocidal incursions into India. Then they lost all their lands, were welcomed into Gujarat, and have been fine neighbors to their Deva-worshipping co-nationalists with occasional intermarriage (far beyond the game scope, but Indira Ghandi's husband was a Parsi). I suspect that this can all be modeled by tenets and doctrines that modify hostility and intermarriage, but it's also another example of why dynamic hostility would be great. If they stay a minority, Zoroastrians should grow more and more accepting with time, but in an Alt-History where they restore the persian empire, they should gradually get more hostile. Also, I really think the Abrahamic settings really only make sense for Christianity. Even a hypothetical restore-the-temple, reinstate animal sacrifice, resume religious execution, "We've got a Kohen Gadol Yo" version of Judaism would, absent unknowable political pressure, see Christians and Muslims as compliant with the seven Noahide laws and thus merely "astray".

## Reply 196 — participant_092 · 2020-04-30 · post-26534022

Something I’d like to know is will there be a way to have interfaith marriages between people of evil faiths? (Like a Christian marrying a Muslim)?

## Reply 197 — participant_057 · 2020-04-30 · post-26534058

<!-- artifact:quote:start -->
> SSA said: Something I’d like to know is will there be a way to have interfaith marriages between people of evil faiths? (Like a Christian marrying a Muslim)? Click to expand...
<!-- artifact:quote:end -->
The dev diary says "Rulers will almost never accept marriages with characters of an Evil Faith, making alliances all-but-impossible." My guess is that you can still force marriages on your courtiers, and use hooks to force through proposals.

## Reply 198 — participant_092 · 2020-04-30 · post-26534085

<!-- artifact:quote:start -->
> MinotaurWarrior said: The dev diary says "Rulers will almost never accept marriages with characters of an Evil Faith, making alliances all-but-impossible." My guess is that you can still force marriages on your courtiers, and use hooks to force through proposals. Click to expand...
<!-- artifact:quote:end -->
The thing about hooks, is that they seem like you can’t really guarantee anything like Favors in CK2 and there’s a chance they’ll say no.

## Reply 199 — participant_016 · 2020-04-30 · post-26534208

The religious hostility system could be improved too honestly. The way it was worded in previous dev diaries made me think that it could have been able to represent stuff like occasional intermarrying between Christians and Muslims, or how Muslims themselves tended to be more tolerant toward Christians and Jews compared to pagans (you'd think that Christians and Muslims would view each others as "Hostile" instead of full on "Evil", especially when it comes to the Muslim view on Christianity. They'd still holy war each others to death, but the shared Abrahamic roots should matter somewhat like they mattered in real life).

## Reply 200 — participant_093 · 2020-04-30 · post-26534502

Just two things. 1 you should gain ferver for being attacked, not losing. assuming it is meant to represent actual ferver and zeal more so than religious unity, which are related but different. and 2. will there be a skepticism doctrine? id quite like to remake a certain obscure Hindu offshoot.

## Reply 201 — participant_094 · 2020-04-30 · post-26534832

<!-- artifact:quote:start -->
> viola said: The religious hostility system could be improved too honestly. The way it was worded in previous dev diaries made me think that it could have been able to represent stuff like occasional intermarrying between Christians and Muslims, or how Muslims themselves tended to be more tolerant toward Christians and Jews compared to pagans (you'd think that Christians and Muslims would view each others as "Hostile" instead of full on "Evil", especially when it comes to the Muslim view on Christianity. They'd still holy war each others to death, but the shared Abrahamic roots should matter somewhat like they mattered in real life). Click to expand...
<!-- artifact:quote:end -->
It's especially odd seeing as the interfaith hostility rules get overridden so often. Muslims ignore the default altogether and use caliphal succession doctrines as their guide instead. Most major Christian denominations consider each other Astray, instead of Hostile. It seems like that rule really only means that Christians and Jews both hate heretics (which, fair enough for the Christians, but was there really that much internecine Jewish violence in the Middle Ages?).

## Reply 202 — participant_057 · 2020-04-30 · post-26535068

<!-- artifact:quote:start -->
> Varren said: It's especially odd seeing as the interfaith hostility rules get overridden so often. Muslims ignore the default altogether and use caliphal succession doctrines as their guide instead. Most major Christian denominations consider each other Astray, instead of Hostile. It seems like that rule really only means that Christians and Jews both hate heretics (which, fair enough for the Christians, but was there really that much internecine Jewish violence in the Middle Ages?). Click to expand...
<!-- artifact:quote:end -->
There problem is that there weren't (m)any Jewish rulers at the time. However, it is true that by the era of the game, the Jewish - Samaritan divide had been officially quieted down with the simple idea of "treat them like Jews insofar as they are like Jews".

## Reply 203 — participant_095 · 2020-04-30 · post-26535362

<!-- artifact:quote:start -->
> Baron von Shoes said: While Fervor has a slow ticking increase over time, it is primarily influenced by the virtuousness or sinfulness of that Faith’s leaders. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Baron von Shoes said: They gain bonus resistance to attempts to convert them to another faith, and both secular and religious leaders can declare Holy Wars to spread their Faith across the world. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Baron von Shoes said: every Holy War declared will slightly damage a Faiths’ Fervor, while losing land to hostile Holy Wars will actually increase your Faith’s Fervor Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Baron von Shoes said: This means that while heresy outbreaks can vary wildly in size, converts to the new heresy will tend to remain clustered together in a specific region — this both protects the burgeoning Faith while simultaneously limiting its influence in distant lands. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Baron von Shoes said: after a heresy outbreak occurs both the old Faith and the new heretical Faith will gain a substantial increase to their Fervor score. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Baron von Shoes said: Now we’re going to take some time to reveal a bunch of the various Doctrines and Tenets available for Faiths in Crusader Kings 3. For starters, the Catholic, Orthodox, Apostolic, and Coptic Faiths all have the ‘Ecumenism’ Doctrine, which changes the Hostility of any other Faith with the same Doctrine to just ‘Astray’, thus allowing these Faiths to have cordial relations with each other. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Baron von Shoes said: The various Sunni Faiths all see each other as Astray, with the same being true for the collective Shia Faiths and the collective Muhakkima Faiths. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Baron von Shoes said: The embattled minority of Gnostic Faiths have an ever stronger version of this; having always struggled to have their beliefs accepted, they see all other Gnostic Faiths as being fully ‘Righteous’. This allows us to have coalitions of Faiths within or even outside of a Religion that see some Faiths as allies and others as enemies, completely changing the dynamic of how religious relations play out in Crusader Kings III. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Baron von Shoes said: Click to expand...
<!-- artifact:quote:end -->
This is the Dev Diary I have been waiting for and it did not disappoint! Right off the bat, 100% better than Moral Authority. Leaning into the roleplay, and opening up opportunities like sending your spymaster to look for dirt on the Pope in order to lower Fervor right before initiating a schism. Or maybe the opportunity will just fall into your lap. Does this mean that Holy Wars can't be declared with low Fervor? Or is it just that the AI will usually choose not to in order to avoid decreasing it further? This seems like it's fairly controversial on here, but I think it's both historically accurate and good for gameplay. Think about it: when a Holy War/Crusade is declared, the people who are signing up are the most fervent ones. Once they're gone, those left are less fervent overall. Those who leave will either die or mostly feel like they have put in their time and are too old/injured/busy to go to war again. Fervor ticks up constantly, so the next generation will be back to fully ready to wage war, likely primed by their parent's stories. And while it is true that it's a little unrealistic that a Holy War in Africa hurts Fervor in Ireland, for pretty much every Faith other than Catholic it makes complete sense to have one unified score, so I get it. Also, I imagine if you win a Crusade you still gain a ton of piety, prestige, and gold in addition to more land, so it's not like it's not worth it. You just can't spam them because you'll be literally depleting your populace's percentage of people willing to go to war for your Faith. Very nice, much better than random sprouting of heresies all over. This is a great mechanic. I would imagine an area with two Faiths at high fervor is basically polarized, either you're one thing or you're the other, and everyone's willing to kill to decide who comes out on top for control of the region. Now this is fascinating. The fact that ecumenism is a main doctrine implies that any Christian Faith can take it without sacrificing a Tenet slot, although I imagine if you want both that and a gay witch sex cult Faith it is going to cost an absolute metric ton of Piety, with I think is a good mechanical way to prevent such things from being relatively trivial to accomplish. That would probably be something to dedicate a run to, rather than a fun side project. It would feel very unrealistic to be able to implement a super out-there Faith while remaining ecumenical unless everyone in Europe pretty much agreed you were the most pious person since Saul. Ok, I will take this, although I still think various Sunni/Shia faiths should share Holy Site bonuses. This is super cool. I'm imagining a multiplayer mod where each player starts with a Faith that has a modified Tenet that makes them consider all the other player Faiths Righteous. Then everyone takes over the world, leading to religious harmony. Some of these seem super cool, and some seem nearly useless. Unless Divining the Stars and the benefits of a Sky Burial are super powerful, that is.

## Reply 204 — participant_014 · 2020-04-30 · post-26535540

what I will still say is the implementation if "Insular Christianity" is a mess - they were loyal to the Pope in Rome, yet you've implemented them to be like a third branch of Catholicism and Orthodoxy, where they will have the same attitude that they have to each other, as well as being wholly independent. This is going to make the Isles a mess religiously and politically and will make any sort of situation where the Irish fall back under Catholicism peacefully basically impossible. The best implementation would've been to at least make them a heresy of Catholicism but have some mechanic where they aren't being holy warred constantly, since apparently it's impossible to make them have the Pope as an authority while being "different". You should have just not put them in the game until a later patch/DLC allows for shared religious heads, to be honest.

## Reply 205 — participant_096 · 2020-04-30 · post-26535691

<!-- artifact:quote:start -->
> Zhetone said: A triumphant faith losing fervor makes no sense in an era where success in war showed God’s favor and loss showed the opposite. This is a change that I really don’t like Click to expand...
<!-- artifact:quote:end -->
So I see both your point and the devs' about this. I'd like to suggest a way that's both balanced and realistic: declaring a holy war, and losing a holy war (on offense or defense), both reduce fervor; having a holy war declared on you, and winning a holy war (ditto), both increase fervor by the same (or a similar) amount. This squares realistically with how people thought about each scenario AND is balanced, in that winning an offensive holy war, and losing a defensive one, would give little or no net Fervor change. Losing an offensive one would result in a big hit that could set back a religion that's blobbing, for realistic reasons, and winning a defensive one would strengthen a small faith.

## Reply 206 — participant_086 · 2020-04-30 · post-26535693

<!-- artifact:quote:start -->
> MinotaurWarrior said: With Zoroastrianism it's tough, and doesn't track through their whole history. On the surface, Iranian and Indian religions consider each other to be, basically, demon worshippers, with Ahura / Asura and Daeva / Deva basically flipping side from one religious group to the other in terms of good and bad. Proto-Mazdan tribes were likely engaged in horrible religious warfare that drove Deva worshipers to India and the near east. Mazdans had prayers like the Frawardin Yasht section twelve, which talks about killing deva-worshippers by the hundreds of thousands of hundreds of thousands (AKA ten billion). But practically, they had much more antagonistic opportunities against non-deva worshippers, especially Christians and Muslims (just before the time of the game) and made only relatively minor, non-genocidal incursions into India. Then they lost all their lands, were welcomed into Gujarat, and have been fine neighbors to their Deva-worshipping co-nationalists with occasional intermarriage (far beyond the game scope, but Indira Ghandi's husband was a Parsi). I suspect that this can all be modeled by tenets and doctrines that modify hostility and intermarriage, but it's also another example of why dynamic hostility would be great. If they stay a minority, Zoroastrians should grow more and more accepting with time, but in an Alt-History where they restore the persian empire, they should gradually get more hostile. Also, I really think the Abrahamic settings really only make sense for Christianity. Even a hypothetical restore-the-temple, reinstate animal sacrifice, resume religious execution, "We've got a Kohen Gadol Yo" version of Judaism would, absent unknowable political pressure, see Christians and Muslims as compliant with the seven Noahide laws and thus merely "astray". Click to expand...
<!-- artifact:quote:end -->
I kinda wonder if the best way to view the hostility settings is as a representation of how the faith acts to other faith when it has power. As a faith without the ability to act on its view of other faiths will essentially act more peacefully. That said I believe the form of Zoroastrianism in Iran (Zurvinite and Mazdan) and the one in India (Parsi) should each be a different faith. This would allow the Parsi to have changes to their tenets and doctrines to show the integration with the local Indian culture. I wonder if a system that allows religions to go up or down one step in hostility would both preserve the feeling of different religions being more or less accepting of different faiths bu also allow for some dynamic change over time.

## Reply 207 — participant_096 · 2020-04-30 · post-26535709

<!-- artifact:quote:start -->
> Eltener said: It seems a really off to have astrology give naval speed implying a link to celestial navigation. Astronomy is a science and completely distinct from astrology. Sure many astronomers during the time period were also astrologers, but many other medieval astronomers thought such practices were heretical. Click to expand...
<!-- artifact:quote:end -->
I think the point is that if people believe the sky determines your fate, they'll spend more time watching it and learning about what happens in it. Also, if there's going to be a celestial navigation boost, it should also increase income from trade (maybe represented as more revenue from coastal cities), since your ships are better at reaching their intended destinations.

## Reply 208 — participant_096 · 2020-04-30 · post-26535713

<!-- artifact:quote:start -->
> Danir said: I like the concept of fervor and I absolutely see the reasoning behind the holy wars change, however, does fervor lost this way have a cap of sorts ? In case of the absence of one I could imagine a situation where the Catholics reconquering the Mediterranean from the Muslims creates a great turmoil inside the Catholic world, leading people to doubt the church to be right and just, although the Christian God supposedly has just helped them in recovering long lost territories from their arguably biggest rivals. Which frankly doesn't make much sense in my opinion. Love the Dev Diary though. EDIT: And the faster the conquests the greater the turmoil which would be a bit counter-intuitive. People getting tired from constant "crusading" makes sense, but not people abandoning their religion for being too succesful. Click to expand...
<!-- artifact:quote:end -->
I think a better way would be to have *declaring* a holy war reduce Fervor, and *winning* the holy war increase it (by the same amount, or slightly more). The reverse would also be true. This is realistic for the reasons you describe, while still balanced.

## Reply 209 — participant_096 · 2020-05-01 · post-26535744

<!-- artifact:quote:start -->
> Skales said: Not wanting to be a pessimist, but the border gore, which we all deep inside know will be there. Will probably discourage many players once they actually see it. Click to expand...
<!-- artifact:quote:end -->
They put some decent anti-gore game rules into CK2. If they keep those it may not be too bad.

## Reply 210 — participant_016 · 2020-05-01 · post-26535886

<!-- artifact:quote:start -->
> QuinnMallory said: I think a better way would be to have *declaring* a holy war reduce Fervor, and *winning* the holy war increase it (by the same amount, or slightly more). The reverse would also be true. This is realistic for the reasons you describe, while still balanced. Click to expand...
<!-- artifact:quote:end -->
That would just defeat the point of stopping blobbing religions. Winning religions don't need a mechanic that helps them win harder.

## Reply 211 — participant_096 · 2020-05-01 · post-26536281

<!-- artifact:quote:start -->
> viola said: That would just defeat the point of stopping blobbing religions. Winning religions don't need a mechanic that helps them win harder. Click to expand...
<!-- artifact:quote:end -->
If it's the same on both sides, then there's no net change in fervor, so it doesn't help them win. Maybe have the gain from winning be slightly less, like 75%? That would simulate the effects on popular opinion well, while still preventing religious blobbing and death spirals.

## Reply 212 — participant_097 · 2020-05-01 · post-26537048

Extremely minor but I'm not a fan of the Proud trait seemingly being renamed Arrogant. (might have been mentioned but the new forum layout is a pain)

## Reply 213 — participant_098 · 2020-05-01 · post-26537062

<!-- artifact:quote:start -->
> Aquamancer said: Technically speaking, Zunism isn't simply a localized variant of Hinduism. The worship of Zun has its roots in Hepthalite paganism, but Zunism was heavily influenced by Shaivist and Suryanite Hinduism, and to a lesser extent by other surrounding religions like Buddhism, Zoroastrianism, and local Indo-Iranian polytheistic traditions. Click to expand...
<!-- artifact:quote:end -->
Technically speaking, we just don't have enough information to back that claim. Given the archaeological evidence, we can say that it was very close to religious practices found in India, with emphasis on sun worship. The rest is speculation. It could feature the remnant of a Greek Apollo cult influence, it could even predate that, it could be Hephthalite influence (though it seems very unlikely)... we don't know. This forum is the only place where you'll find people with such confidence about the "zunist" religion. All scholars are aware of the lack of evidence.

## Reply 214 — participant_027 · 2020-05-01 · post-26537142

<!-- artifact:quote:start -->
> Kainser said: (might have been mentioned but the new forum layout is a pain) Click to expand...
<!-- artifact:quote:end -->
While I agree with you, the CK3 team has no control over the forum layout, and there is a subforum dedicated to forum help, where you should complain instead: https://forum.paradoxplaza.com/forum/forums/forum-help-issues-rules.600/

## Reply 215 — participant_085 · 2020-05-02 · post-26538415

<!-- artifact:quote:start -->
> BoomKidneyShot said: Emperors of Trebizond married off their daughters to Muslim rulers. As an example, https://en.wikipedia.org/wiki/Despina_Khatun Click to expand...
<!-- artifact:quote:end -->
Good point, but these sorts of interfaith marriages should still be fairly rare. Maybe add an attribute to certain cultures (Byzantine, Spanish, Crusader, etc.) that makes them more likely to accept interfaith marriage proposals?

## Reply 216 — participant_059 · 2020-05-02 · post-26538430

<!-- artifact:quote:start -->
> BrotherJonathan said: Good point, but these sorts of interfaith marriages should still be fairly rare. Maybe add an attribute to certain cultures (Byzantine, Spanish, Crusader, etc.) that makes them more likely to accept interfaith marriage proposals? Click to expand...
<!-- artifact:quote:end -->
I'd suggest making these interfaith marriages acceptable for neighboring realms only. So, as a matter of principle the parties will refuse, but they'll make exceptions for rulers who are right at their borders who they interact with more closely.

## Reply 217 — participant_099 · 2020-05-03 · post-26541033

<!-- artifact:quote:start -->
> SeekTruthFromFx said: I think your understanding of the gameplay is mislead by the fact that the good Baron seems to have misread his own table: it says nothing about the relations between different Faiths of the same Religion. Insular and Catholicism will both be Faiths within the Christian Religion. So they're not in the table: I guess that means the default relationship between them is Astray? Click to expand...
<!-- artifact:quote:end -->
Someone has probably already said this to you, but the table absolutely says something about different faiths of the same religion; For Abrahamic religions, faiths in the same religion (and redundantly the same family) are hostile, with exception to the ecumenism doctrine.

## Reply 218 — participant_100 · 2020-05-03 · post-26541993

<!-- artifact:quote:start -->
> GingerContingent said: Some of these seem super cool, and some seem nearly useless. Unless Divining the Stars and the benefits of a Sky Burial are super powerful, that is. Click to expand...
<!-- artifact:quote:end -->
I doubt Tenets are supposed to be of equal importance. Faiths will probably have one or two really defining Tenets and one that's less important. Even for Catholicism, Armed Pilgrimages seems to be bit of a showstopper, Communion pretty important, and Monasticism more of a neat thing.

## Reply 219 — participant_057 · 2020-05-03 · post-26542046

<!-- artifact:quote:start -->
> Provenance said: I doubt Tenets are supposed to be of equal importance. Faiths will probably have one or two really defining Tenets and one that's less important. Even for Catholicism, Armed Pilgrimages seems to be bit of a showstopper, Communion pretty important, and Monasticism more of a neat thing. Click to expand...
<!-- artifact:quote:end -->
Also hinted at by their different piety costs. If you want to found "The Church of Minmax World Domination" it will be more expensive than "Catholicism, but slightly different". Also, CKII Religions weren't "balanced" so this isn't a change.

## Reply 220 — participant_021 · 2020-05-04 · post-26543133

<!-- artifact:quote:start -->
> wilcoxchar said: Also, on this note, it would be great if we could see a screenshot or two of the result of some of the automated games at some point. Just a thought. Click to expand...
<!-- artifact:quote:end -->
I'd like a timelapse of a full one of these, with the Territory, Religion and Culture mapmodes

## Reply 221 — participant_101 · 2020-05-04 · post-26543203

So whats a sun trial? Are we going to be able to execute people by strapping them to a rock and leaving them in a blazing desert if we become sun worshipers because thats pretty sick.

## Reply 222 — participant_016 · 2020-05-04 · post-26543460

<!-- artifact:quote:start -->
> Arukueido said: So whats a sun trial? Are we going to be able to execute people by strapping them to a rock and leaving them in a blazing desert if we become sun worshipers because thats pretty sick. Click to expand...
<!-- artifact:quote:end -->
It's something Zunists can already do in CK2. I think mechanically it's a way to gamble at executing someone with no penalty, but also with a chance of them overcoming the trial and be set free.

## Reply 223 — participant_088 · 2020-05-04 · post-26543518

<!-- artifact:quote:start -->
> FondMemberofSociety said: Just asking here, but which Christian denominations did intermarry with Muslims? I don't really recall any ... Click to expand...
<!-- artifact:quote:end -->
Obviously one cannot generalize in these things according to denominations (not in real life). One does not even need to look to the Nestorians or the examples from Habesha (Ethiopia). There are loads of examples of Christian-Muslim marriages for instance from the Caucasus over several centuries. Often politically motivated, yes - but then again, which marriages weren't, in the period depicted? The Georgian ruling classes, in particular, are noteworthy See, for instance, Andrew M. Sharp 2018, 'The Eastern Churches and Islam', p. 387, in D. Thomas (ed.), Routledge Handbook on Christian-Muslim Relations.

## Reply 224 — participant_028 · 2020-05-04 · post-26543540

<!-- artifact:quote:start -->
> classicist said: Obviously one cannot generalize in these things according to denominations (not in real life). One does not even need to look to the Nestorians or the examples from Habesha (Ethiopia). There are loads of examples of Christian-Muslim marriages for instance from the Caucasus over several centuries. Often politically motivated, yes - but then again, which marriages weren't, in the period depicted? The Georgian ruling classes, in particular, are noteworthy. See, for instance, Andrew M. Sharp 2018, 'The Eastern Churches and Islam', p. 387, in D. Thomas (ed.), Routledge Handbook on Christian-Muslim Relations. Click to expand...
<!-- artifact:quote:end -->
Point noted. Perhaps a special on-action for neighboring realms then, I think, would suit these situations best.

## Reply 225 — participant_094 · 2020-05-04 · post-26544533

It should just be something baked in to the AI acceptance of interfaith marriages. Say: The AI will always reject marriage with an Evil faith unless under duress (say, from a hook or peace deal) or if they'd get a non-aggression pact with a ludicrously more powerful empire (like how, even in CK2, you can marry a Chinese princess regardless of religious differences). The AI will reject most marriages with a Hostile faith, but it will at least consider them when a non-aggression pact or potential claim is on the line. They'd still have a penalty to acceptance, but it wouldn't be impossible. The AI will consider marriages with an Astray faith normally, with a small penalty to acceptance. The AI will treat marriages with a Righteous faith exactly the same as same-faith marriage. After that, it's just a matter of letting Cynical and/or Sympathic rulers treat the marriage as one tier higher (or, ideally, making Abrahamic faiths treat each other as Hostile rather than Evil), and you can get the occasional interfaith political marriage.

## Reply 226 — participant_102 · 2020-05-05 · post-26545485

<!-- artifact:quote:start -->
> MinotaurWarrior said: With Zoroastrianism it's tough, and doesn't track through their whole history. On the surface, Iranian and Indian religions consider each other to be, basically, demon worshippers, with Ahura / Asura and Daeva / Deva basically flipping side from one religious group to the other in terms of good and bad. Proto-Mazdan tribes were likely engaged in horrible religious warfare that drove Deva worshipers to India and the near east. Click to expand...
<!-- artifact:quote:end -->
In the earliest Vedic texts the term asuras is Sometimes used to refer to some Davas. The Term asuras gained negative connotations in later Hindu texts. In the case of Zoroastrian and Hindu using those terms its probably not due to Schism and more due to the root words being used somewhat synonymously, and the word respectively evolving in both religions to take on opposite meanings.

## Reply 227 — participant_103 · 2020-05-05 · post-26545573

<!-- artifact:quote:start -->
> RedCoat1608 said: CKII's Stonehenge was a little silly. Click to expand...
<!-- artifact:quote:end -->
Let's be honest during the middle ages Stonehenge was an obstacle on good farming land. The church frowned upon heretical practices and tourism wan't bound to start before victorian times so... Stonehenge is useless

## Reply 228 — participant_062 · 2020-05-05 · post-26545802

<!-- artifact:quote:start -->
> NFZed said: Let's be honest during the middle ages Stonehenge was an obstacle on good farming land. The church frowned upon heretical practices and tourism won't bound to start before victorian times so... Stonehenge is useless Click to expand...
<!-- artifact:quote:end -->
I would not go, or God forbid farm anywhere near that! Do you want me to get cursed?

## Reply 229 — participant_104 · 2020-05-05 · post-26546249

<!-- artifact:quote:start -->
> Zhetone said: what I will still say is the implementation if "Insular Christianity" is a mess - they were loyal to the Pope in Rome, yet you've implemented them to be like a third branch of Catholicism and Orthodoxy, where they will have the same attitude that they have to each other, as well as being wholly independent. This is going to make the Isles a mess religiously and politically and will make any sort of situation where the Irish fall back under Catholicism peacefully basically impossible. The best implementation would've been to at least make them a heresy of Catholicism but have some mechanic where they aren't being holy warred constantly, since apparently it's impossible to make them have the Pope as an authority while being "different". You should have just not put them in the game until a later patch/DLC allows for shared religious heads, to be honest. Click to expand...
<!-- artifact:quote:end -->
Couldn't you just give Insular Christianity a doctrine making Catholicism viewed as Righteous.

## Reply 230 — participant_062 · 2020-05-05 · post-26546362

<!-- artifact:quote:start -->
> Katana500 said: Couldn't you just give Insular Christianity a doctrine making Catholicism viewed as Righteous. Click to expand...
<!-- artifact:quote:end -->
That still would not represent them anywhere near accurately. TBH I am just not sure why Paradox did this, they create smaller, new faiths, for no real reason (CK2 worked well enough in this area), but then don't go all the way to make them actually work properly.

## Reply 231 — participant_103 · 2020-05-05 · post-26546641

<!-- artifact:quote:start -->
> Skales said: I would not go, or God forbid farm anywhere near that! Do you want me to get cursed? Click to expand...
<!-- artifact:quote:end -->
Sure you wouldn't you are from modern enlightend times, you know that Stonehenge is dangerous, but those poor stupid farmers in 1066, nah they'd first let their sheep graze there and in the evening enjoy their wives or vice versa...

## Reply 232 — participant_057 · 2020-05-05 · post-26546830

<!-- artifact:quote:start -->
> Trudon21 said: In the earliest Vedic texts the term asuras is Sometimes used to refer to some Davas. The Term asuras gained negative connotations in later Hindu texts. In the case of Zoroastrian and Hindu using those terms its probably not due to Schism and more due to the root words being used somewhat synonymously, and the word respectively evolving in both religions to take on opposite meanings. Click to expand...
<!-- artifact:quote:end -->
Well the earliest layers of Vedic texts are in common not just with the Avestas but also even as far as the Eddas (in very small fragments, themes, and a few lists) and in general these texts often conserve elements that, even at the time, were archaic. In the Time of the Buddha, only three of four Vedas had been composed, but Asuras and Devas were distinct opposed groups of preternatural beings. Yet, (presumably) later Hindu developments like the story of Holi include heroic Asuras like Prahlada (though most of the Asuras in the story are evil). However, this conflation of devas and asuras does not exist in Mazdaism. From the earliest mentions, Daeva are always foreign, prohibited, adversarial, evil beings. The people who were able to win out and stay in Iran 'always' viewed the Daevas and Daeva worshippers as foreign and bad. Now, Zoroastrianism and Hinduism both post-date the prehistorical Schism between the proto-Iranians and the Proto-Indians. I don't want to overstate the historical value or relevancy of the texts. My point is just this: 1) Prehistoric Mazdans pushed other groups out of Iran into India and the Fertile Crescent (the proof of this is linguistic and archeological) 2) The Zoroastrian religion is theoretically more violent and hostile towards other religions than is literally possible to implement (and thus, that theoretical hostility was never actually practiced) 3) Historical Mazdan states never acted that prejudicially against Eastern religions 4) Mazdans in the timespan of the game were mostly a peaceful minority that coexisted with other faiths. And thus, their hostility is complicated. As a side note, famously Cyrus the Great is the one to have basically saved Abrahamic religions by ending the Babylonian exile.

## Reply 233 — participant_105 · 2020-05-06 · post-26547992

I think the Fervor mechanic makes sense You lose it on declaration of a holy war, this essentially is utilizing/investing the people's zeal to do something. Since you will gain piety and more from converting the land, you will regain the fervor over time for being a righteous ruler. The defender gaining it on a loss makes sense too, it is basically revanchism. The other changes look great, I am feeling my first bit of hype for this now. Don't screw it up.

## Reply 234 — participant_028 · 2020-05-06 · post-26548639

<!-- artifact:quote:start -->
> MinotaurWarrior said: My point is just this: 1) Prehistoric Mazdans pushed other groups out of Iran into India and the Fertile Crescent (the proof of this is linguistic and archeological) 2) The Zoroastrian religion is theoretically more violent and hostile towards other religions than is literally possible to implement (and thus, that theoretical hostility was never actually practiced) 3) Historical Mazdan states never acted that prejudicially against Eastern religions 4) Mazdans in the timespan of the game were mostly a peaceful minority that coexisted with other faiths. And thus, their hostility is complicated. As a side note, famously Cyrus the Great is the one to have basically saved Abrahamic religions by ending the Babylonian exile. Click to expand...
<!-- artifact:quote:end -->
I will respectfully disagree regarding point 2. I mean, in an age where church structure doesn't exist, can tribal hostilities really be interpreted in terms of religion? The concurrent Old Chinese also drove the Miao and Yue peoples south into the mountains and hills of southern China, but I'm assuming the source of said hostility is not religion. And in reality, the Sassanid Empire (which was the only state to have Zoroastrianism as a state religion and be relevant to the players that still exist in the game's timeframe) was a lot more hostile to Christians than to Hindus and Buddhists, as far as we know. Well, because they did not interact that much - the "White Hun" occupation of the "Buddhist Corridor" is also an important event in China, because it facilitated the transfer of Buddhism from India to China, until the Muslims occupied and cut off the route some two hundred years before CK3's earliest start date, accelerating a divide to appear between Mahayana (in East Asia mostly) and Theravada (SEA etc.) adherents.

## Reply 235 — participant_106 · 2020-05-06 · post-26548908

Make the polygamy mormon...

## Reply 236 — participant_028 · 2020-05-06 · post-26549274

<!-- artifact:quote:start -->
> J.P.Cliffer said: Make the polygamy mormon... Click to expand...
<!-- artifact:quote:end -->
It is possible to make a polygamy-endorsing Christian sect, but people at the time don't know enough about the universe to actually found Mormonism. There are limits to how ahistorical a game of CKIII could get, and I say science is one of them. Also, I'm pretty sure any Christian sect of the age would not let Jews into their version of heaven.

## Reply 237 — participant_057 · 2020-05-06 · post-26549376

<!-- artifact:quote:start -->
> FondMemberofSociety said: I will respectfully disagree regarding point 2. I mean, in an age where church structure doesn't exist, can tribal hostilities really be interpreted in terms of religion? The concurrent Old Chinese also drove the Miao and Yue peoples south into the mountains and hills of southern China, but I'm assuming the source of said hostility is not religion. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> FondMemberofSociety said: And in reality, the Sassanid Empire (which was the only state to have Zoroastrianism as a state religion and be relevant to the players that still exist in the game's timeframe) was a lot more hostile to Christians than to Hindus and Buddhists, as far as we know. Well, because they did not interact that much - the "White Hun" occupation of the "Buddhist Corridor" is also an important event in China, because it facilitated the transfer of Buddhism from India to China, until the Muslims occupied and cut off the route some two hundred years before CK3's earliest start date, accelerating a divide to appear between Mahayana (in East Asia mostly) and Theravada (SEA etc.) adherents. Click to expand...
<!-- artifact:quote:end -->
I think you actually mean point 1. And the answer is that the "church structure" (of semi-hereditary priesthood with a strong oral tradition) already existed in the prehistoric era. I'm not saying that the source of the conflict was religion, but religion (and all other aspects of life) was part of it. This is prehistorical, so we don't know any of the details of what happened, but broadly speaking we can say that in prehistorical Iran there were proto-Mazdans and proto-Hindus (as well as proto-Mittani and proto-who knows what, and also to be clear these proto-Hindus aren't "where Hinduism comes from" as there were existing peoples in India who were co-sources for Indian religion), that they conflicted, that the proto-Mazdans remained, and that the Proto-Hindus (and proto-Mittani) were driven out. Also, while Chinese Folk Religion isn't something I know a ton about, it is my understanding that the Mythology of the Three Sovereigns and Five Emperors is thought to be kinda-sorta-vaguely related to the actual prehistoric expansion of proto-Han culture. However, even in the mythology, the expansion reflects the cosmopolitan attitudes of the Chinese folk religion with acts of confederation, and their mythological enemies being deified. 1) The Sassanid Empire was dead as can be by the game era 2) The Sassasanid Empire had it's own major branch of Christianity after the council of Ephesus and even had a partially-Jewish Shanashah (Shapur II) Overall I think it's very very tough to generalize Mazdan religion's "religious hostility", especially since it only really matters for an alternative history where they rise to power, and giving them the "Oriental" default settings is, while not "100% Accurate" probably fine.

## Reply 238 — participant_028 · 2020-05-06 · post-26549621

<!-- artifact:quote:start -->
> MinotaurWarrior said: I think you actually mean point 1. And the answer is that the "church structure" (of semi-hereditary priesthood with a strong oral tradition) already existed in the prehistoric era. I'm not saying that the source of the conflict was religion, but religion (and all other aspects of life) was part of it. This is prehistorical, so we don't know any of the details of what happened, but broadly speaking we can say that in prehistorical Iran there were proto-Mazdans and proto-Hindus (as well as proto-Mittani and proto-who knows what, and also to be clear these proto-Hindus aren't "where Hinduism comes from" as there were existing peoples in India who were co-sources for Indian religion), that they conflicted, that the proto-Mazdans remained, and that the Proto-Hindus (and proto-Mittani) were driven out. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> MinotaurWarrior said: Also, while Chinese Folk Religion isn't something I know a ton about, it is my understanding that the Mythology of the Three Sovereigns and Five Emperors is thought to be kinda-sorta-vaguely related to the actual prehistoric expansion of proto-Han culture. However, even in the mythology, the expansion reflects the cosmopolitan attitudes of the Chinese folk religion with acts of confederation, and their mythological enemies being deified. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> MinotaurWarrior said: 1) The Sassanid Empire was dead as can be by the game era 2) The Sassasanid Empire had it's own major branch of Christianity after the council of Ephesus and even had a partially-Jewish Shanashah (Shapur II) Overall I think it's very very tough to generalize Mazdan religion's "religious hostility", especially since it only really matters for an alternative history where they rise to power, and giving them the "Oriental" default settings is, while not "100% Accurate" probably fine. Click to expand...
<!-- artifact:quote:end -->
Whoops, yes, I meant point 1. Or rather the interplay between 1 and 2. Can prehistoric conflicts really factor in relatively late religious hostilities? I don't know, I think devs used a "ratings" and not numerical system do streamline the problem somewhat. In addition to the confederation you pointed out, the Miao were warped from (relatively shorter and darker) people to outright demonic beings, with their leader Chi You having "many eyes, a roar that tears the earth," and he "eats rocks to grow his horns." Chi You is also said to wield wicked magicks. So ... yeah, you now have more or less an overview of the tale of Huangdi, the very first emperor of China's enemies. 1) Point is legit, but later Mazdan rulers did call upon their legacy, and in the event Mazdayasna regains mainstream status, Sassanian legal norms would likely also be recovered and reused; 2) The Nestorians did count on the Sassanids for protection ... in their capacity as king of kings, not protector of the holy flames. In fact, the Shahanshah most closely related to Jews (it's Yazdegerd I, not Shapur II by the way) was forced to move against Nestorians at the behest of his court, after Nestorians started attacking Mazdayasnaian fire-temples. I agree with the last point. So long as hardcoded material is not that big of a problem, we can always resort to modding to change anything and everything. Devs even made a point of showcasing religion mod-friendliness.

## Reply 239 — participant_088 · 2020-05-07 · post-26550624

<!-- artifact:quote:start -->
> FondMemberofSociety said: And in reality, the Sassanid Empire (which was the only state to have Zoroastrianism as a state religion and be relevant to the players that still exist in the game's timeframe) was a lot more hostile to Christians than to Hindus and Buddhists, as far as we know. Click to expand...
<!-- artifact:quote:end -->
But this is also a very complex issue. We certainly know that at several stages the Sassanian approach to several Christian groups - especially non-Chalcidian and thus ones which were most often persecuted and sidelined in the Roman state - was either tolerant or explicitly supportive. At other times (i.e. under specific rulers) this could be reversed, but there very meager evidence for wholesale hostile stance towards 'Christians' as such.

## Reply 240 — participant_092 · 2020-05-07 · post-26550657

One of the tenants, I find interesting is the esoteric tenant; it’s interesting that each tenant gives extremely unique mechanics to how you play your game. (An “Armed Pilgrimage” holy war doctrine will act differently with different buffs than “Struggle of Submission”.)

## Reply 241 — participant_028 · 2020-05-07 · post-26550659

<!-- artifact:quote:start -->
> classicist said: But this is also a very complex issue. We certainly know that at several stages the Sassanian approach to several Christian groups - especially non-Chalcidian and thus ones which were most often persecuted and sidelined in the Roman state - was either tolerant or explicitly supportive. At other times (i.e. under specific rulers) this could be reversed, but there very meager evidence for wholesale hostile stance towards 'Christians' as such. Click to expand...
<!-- artifact:quote:end -->
Yes, it is a complex issue indeed. I think if we take religious hostility as a general rule, things would be more easily clarified than adapting the hostility system to all the intricacies Late Antique and Middle Ages leadership implies. Individual situations have individual opinion modifiers factoring in after all. Still, there is some evidence of Christian-Mazdayasnian relations as a whole in the event I mentioned in the post above. The tenure of Mihr-Narseh Suren as wuzurg framatar began with massed attacks on fire temples by Christians, and the nobles said "Yazdegerd, we know you don't hate Christians nor Romans, but this is going too far". Not much, but it's a start for an analysis of a general stance.

## Reply 242 — participant_057 · 2020-05-07 · post-26550984

<!-- artifact:quote:start -->
> FondMemberofSociety said: Whoops, yes, I meant point 1. Or rather the interplay between 1 and 2. Can prehistoric conflicts really factor in relatively late religious hostilities? I don't know, I think devs used a "ratings" and not numerical system do streamline the problem somewhat. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> FondMemberofSociety said: In addition to the confederation you pointed out, the Miao were warped from (relatively shorter and darker) people to outright demonic beings, with their leader Chi You having "many eyes, a roar that tears the earth," and he "eats rocks to grow his horns." Chi You is also said to wield wicked magicks. So ... yeah, you now have more or less an overview of the tale of Huangdi, the very first emperor of China's enemies. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> FondMemberofSociety said: 1) Point is legit, but later Mazdan rulers did call upon their legacy, and in the event Mazdayasna regains mainstream status, Sassanian legal norms would likely also be recovered and reused; Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> FondMemberofSociety said: 2) The Nestorians did count on the Sassanids for protection ... in their capacity as king of kings, not protector of the holy flames. In fact, the Shahanshah most closely related to Jews (it's Yazdegerd I, not Shapur II by the way) was forced to move against Nestorians at the behest of his court, after Nestorians started attacking Mazdayasnaian fire-temples. I agree with the last point. So long as hardcoded material is not that big of a problem, we can always resort to modding to change anything and everything. Devs even made a point of showcasing religion mod-friendliness. Click to expand...
<!-- artifact:quote:end -->
Can they? Well, yes. The time span between when Canaan was given to the Twelve Tribes of Israel by G-d and when the modern state of Israel formed is pretty substantial. Do I think this ancient and theoretical hostility should outweigh other considerations? No. As well, I think it is an example of how hostility realistically is not a fixed value. And then later, the historical first Emperor named himself after Huangdi and worshiped Chi You. I don't know. In CKII, not playing as a Mazdan you mostly saw Muslims win out in Persia and Mazdans only enduring in the Steppe. And under player control, I think the easiest start was still up there, growing in strength while waiting for the Muslims to weaken. Even when a Uighyr or Khazar or Sogdian Khagan takes the mantle of Shanashah and rules over the "Persian Empire", neither he nor his subjects are really going to know what that means, with at least a century between them and the Sassanids. The biggest defining event for religious hostility would realistically be however the Mazdans retake Persia. 100 years of assassination and holy war between big states? That would logically make things quite hostile. Diplomatic shenanigans with honorably-earned hooks leading to a peaceful succession? Probably going to make things less hostile. Shapur II was the son of Jewish woman Ifra Hormizd. Yazdegerd I had a Jewish wife, but was not ethnically Jewish himself. Though I was wrong in saying the Sassanids had a partially Jewish Shanashah, as Bahram V, Yazdegerd I's son was also ethnically half (or, well, half + some other fraction) Jewish. Also the events you're describing are really just a religious minority revolt, which I think are supposed to be independent of the hostility system.

## Reply 243 — participant_028 · 2020-05-08 · post-26553065

<!-- artifact:quote:start -->
> MinotaurWarrior said: Can they? Well, yes. The time span between when Canaan was given to the Twelve Tribes of Israel by G-d and when the modern state of Israel formed is pretty substantial. Do I think this ancient and theoretical hostility should outweigh other considerations? No. As well, I think it is an example of how hostility realistically is not a fixed value. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> MinotaurWarrior said: And then later, the historical first Emperor named himself after Huangdi and worshiped Chi You. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> MinotaurWarrior said: I don't know. In CKII, not playing as a Mazdan you mostly saw Muslims win out in Persia and Mazdans only enduring in the Steppe. And under player control, I think the easiest start was still up there, growing in strength while waiting for the Muslims to weaken. Even when a Uighyr or Khazar or Sogdian Khagan takes the mantle of Shanashah and rules over the "Persian Empire", neither he nor his subjects are really going to know what that means, with at least a century between them and the Sassanids. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> MinotaurWarrior said: Shapur II was the son of Jewish woman Ifra Hormizd. Yazdegerd I had a Jewish wife, but was not ethnically Jewish himself. Though I was wrong in saying the Sassanids had a partially Jewish Shanashah, as Bahram V, Yazdegerd I's son was also ethnically half (or, well, half + some other fraction) Jewish. Also the events you're describing are really just a religious minority revolt, which I think are supposed to be independent of the hostility system. Click to expand...
<!-- artifact:quote:end -->
Well, this much we can concur. I admit the demonization of Chi You was a gradual process, but Shihuangdi named his new title after all the mythological rulers of China (Three Huangs Five Dis ... ugh it sounds so horrible like that) and perhaps, worshipped Chi You to placate his Miao subjects - Yunnan was not as easy to govern back in the day after all. I meant the anti-Muslim revolts like Mardavij, but you do have a point for the Khazars and Uyghurs. Yes, there would be ... complications for such a scenario, and the game doesn't simulate the need to recruit Persian bureaucrats to rule over Persian lands, something that would have easily disseminated knowledge of the old empire's legal systems into the new government. Even though that does explain where he got the backing he needed to eventually become a powerful King of kings, I still would have to ask for your sources on Shapur II's parentage. Emmm ... shouldn't religious hostilities affect all adherents of said faiths, regardless of whether they were of the same realm or not? Having a province full of people who follow a religion that hates yours should make them a lot likely to revolt, shouldn't it?

## Reply 244 — participant_033 · 2020-05-09 · post-26555033

<!-- artifact:quote:start -->
> FondMemberofSociety said: Having a province full of people who follow a religion that hates yours should make them a lot likely to revolt, shouldn't it? Click to expand...
<!-- artifact:quote:end -->
Well, that really depends on how you treat theirs. If you don't ban their worship or force them to observe yours, you won't really be giving them a reason to hate you for it. They might prefer a ruler of Religion X, but if you're tolerant, coexistence even among rival religions can happen (such as at some points in Mughal India).

## Reply 245 — participant_107 · 2020-05-09 · post-26555079

<!-- artifact:quote:start -->
> Varus90 said: Well, that really depends on how you treat theirs. If you don't ban their worship or force them to observe yours, you won't really be giving them a reason to hate you for it. They might prefer a ruler of Religion X, but if you're tolerant, coexistence even among rival religions can happen (such as at some points in Mughal India). Click to expand...
<!-- artifact:quote:end -->
This is probably represented by traits like the Adaptive trait mentioned by a Dev in the recent Islam thread - it was IIRC described as minimizing religious discontent in your ruled areas / with vassals, on account of your laissez faire attitude to their practices.

## Reply 246 — participant_108 · 2020-05-29 · post-26615065

I don't know if this has been asked before, sorry if that is the case, but is their going to be requirements for some of the tenets? LIke that you can't take one tenet without taking a certain other? and that you can't combine some?

## Reply 247 — participant_033 · 2020-05-29 · post-26615108

<!-- artifact:quote:start -->
> Maistronom said: I don't know if this has been asked before, sorry if that is the case, but is their going to be requirements for some of the tenets? LIke that you can't take one tenet without taking a certain other? and that you can't combine some? Click to expand...
<!-- artifact:quote:end -->
Yes. We can see that from the popups shown. For instance, you can't take the primitivism one with any tenet that considers a particular action criminal.

## Reply 248 — participant_108 · 2020-05-29 · post-26615117

<!-- artifact:quote:start -->
> Varus90 said: Yes. We can see that from the popups shown. For instance, you can't take the primitivism one with any tenet that considers a particular action criminal. Click to expand...
<!-- artifact:quote:end -->
Hmmm, okay, it makes sense, just that when I first saw these I got an idea of a religion I wanted to make and I'm pretty sure it ain't gonna work since some tenets exclude some others.

## Reply 249 — participant_109 · 2020-06-08 · post-26640065

What conditions have to be met to convert from one religious family to another? Like, say from an Abrahamic religion to a Pagan one?

