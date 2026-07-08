---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1756319/"
forum_thread_id: 1756319
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 172
title: "Dev Diary #172 - The Full Medieval World"
dd_date: 2025-05-21
author_handle: Trin Tragula
expansion: All Under Heaven
patch: null
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 4155
inline_image_count: 9
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1756319'
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
    location: raw_lines_350_to_355
    action: preserved_and_flagged
    counts:
      Love: 171
      Like: 152
      (unlabeled — rendered as base64 data URI): 3
      Haha: 1
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_363_to_473
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_474_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Dev Diary #172 - The Full Medieval World

<!-- artifact:thread_metadata:start -->
- Thread starter [Trin Tragula](https://forum.paradoxplaza.com/forum/members/trin-tragula.18587/)
- Start date [May 21, 2025](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-172-the-full-medieval-world.1756319/)
<!-- artifact:thread_metadata:end -->

Hello and welcome to this first development diary about the upcoming *All Under Heaven* DLC, and its associated update! I am Trin Tragula, one of the design leads on Crusader Kings III and today I get to talk about East Asia in the middle ages!  

This diary is going to be a high level one, where we look at the vision for the entire expansion and all we aim to do in it. It will be followed by many more detailed diaries for the features and the individual regions of the expansion.  

![image_01.png](https://forumcontent.paradoxplaza.com/public/1296645/image_01.png "image_01.png")


*[A first look at the world of Crusader Kings with everything between the Atlantic and the Pacific Ocean. Like everything else in this diary the map is work in progress and subject to change; this includes coloring of the map itself, which is something we are experimenting a bit with right now. Don’t hesitate to tell us what you think of it!]*  

Apart from being Grand Strategy Games, the Paradox games have, for me personally, always also been a way to discover the entire world in a given time period, something that is both a game and a travel guide to the past. With this update, CK will finally get rid of the last artificial barriers to that kind of experience, as the map will no longer arbitrarily end in Burma and Tibet. This lets us shine a spotlight on some of the most interesting states of the time period, such as Tang and Song China, Heian Japan, Angkor, and many others.  

With *All Under Heaven*, we want to not just add the missing parts of the map but also fill it with the living world of the past. The goal is that the new part of the map should feel like an integral part of the game. This means new governments with their own features, but it also means things like special buildings, new cultural traditions, and visual variety. East Asia will have its own look, with event illustrations, clothes, ethnicities, holdings, throne rooms, artifacts, and much more.  

![image_02.png](https://forumcontent.paradoxplaza.com/public/1296646/image_02.png "image_02.png")



As a final word of this introduction: this is also a work in progress. This is a vision and an overview of what we are making, but development is an iterative process and so this diary is also an opportunity for you to give your input on the things we are looking to add. More details are also forthcoming for each and every thing here in the coming diaries but there is nothing stopping you from telling us already if there are things you think we should include or change. This goes for art, features, and even the map itself.  

---

## China​

A central focus of an East Asian expansion, by virtue of its sheer size as well as the reach and impact of its influence and culture, has to be China. While it was in a very different situation in 867, 1066 and 1178 respectively, China remains both a state that others emulated and a political constant in all of these dates.  
We will talk a lot more about China and its features in future diaries, but here is a short overview of what we have planned and how we see its purpose.  

### Hegemony - A New Title Tier​

Since China is a de jure realm that is more expansive than any one of the empires we currently have in the game, we are adding a new title tier for it - a Hegemony. In all our start dates, China is the only existing Hegemony, but others can be created using the decisions we have for uniting India or Rome. For now, there is no generic way to create these super-empires, and beyond China there are no de-jure ones. Instead, we reserve its use for special cases with bespoke rules and justifications.  

![image_03.png](https://forumcontent.paradoxplaza.com/public/1296647/image_03.png "image_03.png")



### Celestial Government & Merit​

China was a bureaucratic state, and though it differed a bit depending on era, positions in government as well as in provincial administration were largely given to career officials based on their perceived merit. Thousands would take the imperial examinations in order to start their career in public service, leading to possibly the most well-educated government apparatus in the world.  

In *All Under Heaven*, the Hegemony of China has a special type of government called the Celestial Government. It builds on the Administrative Government introduced in *Roads to Power* for the Byzantine Empire. House heads and governors are playable, and can build up Influence and acquire positions, while families have a domicile representing their permanent powerbase that they can build up over time.  
Where the Byzantine governors are solely appointed based on spending Influence however, the Chinese system relies more closely on **Merit**. Merit is a value that you build up during a lifetime in public service, through serving in important jobs and taking good decisions. Merit cannot be spent like a currency, instead it is how you are compared to other applicants for any position. A high merit score might mean you can become a circuit (kingdom) tier governor, or even a minister in the central government. Merit does not replace Influence since Influence can still be earned and spent for more underhanded uses, even in a Celestial realm.  

![image_04.png](https://forumcontent.paradoxplaza.com/public/1296648/image_04.png "image_04.png")



In order to ensure a healthy crop of potential administrators at all times, the Empire will regularly host **examination activities** where the applicants can earn a base merit score (or even a higher one) by demonstrating their skills at the Confucian classics, literary style, and essay writing.  
The Emperor, on the other hand, can control what skills are prioritized in the examinations by controlling the curriculum when hosting Exams. Whatever qualities are emphasized will shape which characters are likely to be able to become governors in the future.  

### The Imperial Treasury​

Governors in China will not support themselves using the money from the region they govern. Instead they will send the funds upwards, to the Emperor and his central treasury. The emperor then pays out a salary (gold) to the governor but also assigns funds to the respective treasury of all governorships in the realm.  
Only gold can be spent on personal expenses, such as building up your family estate, paying for tutorship for your children, and so on. Treasury is what is used for any expenses related to governing. This includes things like building buildings, paying troops, or disaster relief.  

Like with everything in this diary, there will be more information about the treasury, including details around how money can be put into or taken out of it by characters, in a future China-centric Developer Diary.  

### The Dynastic Cycle​

Chinese history is traditionally ordered by the dynasty currently in power. This is a phenomenon that goes far back in time, where often a new dynasty would prioritize writing the history of their predecessors. They would use the imperial archives to chart out and describe how the old dynasty rose, how they ruled and how they eventually lost their way and succumbed to corruption (leaving an opening for the new dynasty to save the day and restore order and propriety).  
In our timeline, the Tang, once a very successful and expansive dynasty that ruled a vast and prosperous realm, are already troubled by 867. About 40 years from this start date, their dynasty would break into a multi-factional civil war known as the **Five Dynasties and Ten Kingdoms Era**. Eventually the Song took power and built a new dynasty based even more strongly on the principles of bureaucracy and internal development.  
The Song were eventually replaced by the Yuan dynasty of Kublai Khan, who ruled a China that was unmistakably Chinese, but also still very Mongol dominated. The Yuan and other foreign dynasties are often referred to as Conquest Dynasties due to their different nature (at least initially).  


![image_05.png](https://forumcontent.paradoxplaza.com/public/1296649/image_05.png "image_05.png")




In *All Under Heaven*, we have taken inspiration from how the Chinese described this at the time, a Dynastic Cycle where China can be in a stable era, essentially a type of golden age, where it can build its wealth and progress orienting themselves outwards (like the **Tang**), focusing on military **expansion** and a vast tributary network. Another focus can be **advancing** the core region, with great building projects, economic development, innovation and a strong bureaucracy (more like the **Song** or later **Ming**).  
Common to both types of Stable eras (Expansion and Advancement) is that they can go on for a very long time. As long as the rulers put the right people in positions of government, protect their subjects from invasions and act swiftly against natural disasters, they are able to draw on the resources of China to perform great things. The eras come with different possibilities and rules for how to achieve these goals. In this way China’s neighbors will also know what to expect from the neighboring behemoth.  

Common to both stable eras is that how Legitimacy is built and maintained relates to you moving in alignment with the era. If your dynasty has chosen an Expansion era then your Legitimacy will suffer if you fail to expand and will be even more damaged if outsiders take land or raid your lands.  

With the ruling dynasty faltering, the cycle will eventually proceed to the **Unstable Era**. This is an era with its own rules and impact, just like the two stable variants, but here it is mainly to signify a period of change. Here people have begun to question the mandate of the rulers, and every action they take is under closer scrutiny. Natural disasters, wars, and other things will be viewed in a much more negative light, especially if the central government is unable to act quickly on them. Governors will be less selfless and may not take their responsibilities to the center as seriously, instead preparing for their own future.  
Should the Emperor’s Legitimacy be impacted strongly enough, this era is very likely to slide into a **Chaotic Era**, where the ruling dynasty will fracture into a multi-factional civil war, much like what happened in the Five Dynasties and Ten Kingdoms Era.  

Should the ruling dynasty, on the other hand, navigate the unstable era well enough and emerge on the other side, then they will once again enter a stable era and be able to choose between **Advancement** and **Expansion** once more. In the 867 bookmark the **Tang** starts in the unstable era.  

In the **Chaotic Era**, the Hegemony of China title is suspended while the various empires, kingdoms and duchies in the Chinese realm are splintered into separate realms. These will quickly try to form their own dynasties, in conflict with each other. Once a winner emerges China will once again enter a stable phase, and the new ruling dynasty will be seen to have the Mandate of Heaven to rule the restored Hegemony of China. This will mean choosing a type of stable era as well as taking some other decisions about your long term goals (including what capital to use and the traditional name and color to associate with your dynasty).  

There is much more to be said about the Dynastic Cycle, including how your bureaucrats coordinate to push for trying to change the current type of era, and how it deals with foreign conquest dynasties, but most of that will have to wait for a future diary of its own.  

### Tributaries and China​

For the Chinese Empire, tributaries are not at all what they are to the rulers in the steppe. Independent rulers can choose to enter a relationship with China and be legitimized by trappings of authority from China. The tributary is not expected to play any part in China’s wars, and China will also not defend its tributaries as a general rule, it will however be less likely to be attacked directly.  

Tributaries can attempt to create a closer relationship with their Suzerain Hegemon by going on Tributary missions to the Chinese court, bringing gifts, goods, eunuchs, and other things to please the Emperor. In return they may receive economic benefits, legitimizing artifacts or progress towards Chinese innovations.  

---

## Japan​

One of the more unique regions of the medieval world is Japan. In our timeline (covering 867-1453 AD), Japan is originally a state that is largely inspired by the Chinese way of doing things, with governors who do not directly own land, and a vibrant capital in Kyoto. Noble families play a bigger part in ceremony, fine arts, and intrigue than they do in China, but military campaigns tend to be small and directed at the Ainu or Emishi in the eastern part of the island rather than other families in the realm.  
Over time, some nobles manage to install themselves in hereditary fiefs, and the country starts undergoing a gradual militarization, culminating in the establishment of something much closer to the feudal realms of the west.  

### Soryō and Ritsuryō - Two Types of Vassals in One Realm​

Unlike Administrative realms, where governorships are generally duchies, (and unlike China where they can be any tier) Japanese governorships are generally counties. This means power is a lot more fragmented than it is in other realms.  

In 867 and 1066, the vast majority of counties are held by Ritsuryō rulers - a government very similar to Administrative - while by 1178 most of Japan is ruled by local Soryō lords - more akin to Feudal.  

**Ritsuryō** rulers use Influence to secure appointments and generally don’t have strong armies (unless enabled by their House-related bonuses as described below).  

**Soryō** vassals, on the other hand, have gained de facto control of a region from the central state and made it a permanent fief. Their succession is hereditary, their armies are stronger, and they can more easily expand militarily to control multiple counties. Soryō vassals can be useful to the empire in times of war, but generally they are a liability and a **Ritsuryō** that tries to turn their governorship into a **Soryō** fief will be considered a criminal.  

### House Relations & Blocs​

The long-term relationships between different Houses are now tracked, and move along a sliding scale from great friendship to intense rivalry. Whenever a member of a House takes a significant friendly or hostile action against another House’s member, such as a marriage or a murder, the relation between the Houses will change to reflect the act.  

![image_06.png](https://forumcontent.paradoxplaza.com/public/1296650/image_06.png "image_06.png")



In Japan, houses can also form Blocs. These are groups of houses that all follow the head of one house, largely based on house relations. A bloc is a military alliance that is represented on the map, similar to steppe confederations, though with a clear leader and more far-reaching responsibilities. Bloc members will join the factions and wars of their leader (offensive as well as defensive). This means that when wars break out in Japan they are not as limited despite the fragmented political situation.  

### The Emperor and the Kampaku​

In our era, the Japanese Emperors had varying degrees of power, but were generally relegated to a more ceremonial role than many of their foreign counterparts. The de facto ruler of Japan in all but name is usually the **Kampaku**, a Ritsuryō bureaucrat who rules on the Emperor’s behalf.  

The succession of the Kampaku is determined in a similar way to the Byzantine Emperor’s acclamation, but with a different set of weights (favoring among other things marriage ties with the imperial family).  
The Emperor, or Ten’nō, still has great ceremonial importance and is playable, but only directly rules his own family manor in all our start dates. Like many of the noble families in Japan, he resides in the imperial capital of Kyoto.  

![image_07.png](https://forumcontent.paradoxplaza.com/public/1296651/image_07.png "image_07.png")



Only Ritsuryō rulers may become Kampaku by appointment, but Soryō rulers can take the top job if they can build a powerful enough Faction, and thus establish themselves as a Shōgun (the Soryō equivalent of a Kampaku) by force. The Emperor themselves can also aspire to the top position and, if appointed as Kampaku, is given the option to abdicate the imperial throne and rule as a cloistered emperor, representing periods of strong royal influence.  

Since the Kampaku, or Shōgun, essentially acts as the top liege in the Japanese realm, they wield an enormous amount of power, and will also make use of special Imperial Policy laws to control what can and cannot be done by vassals in the realm. Should a Shōgunate be established by a Soryō ruler this will start to usher in a societal change with more and more of the vassals in Japan forming Soryō fiefs.  

### Japanese Houses​

With most vassals in Japan starting out holding just one county, there is a great need for other ways to build permanent power. The family manor, which is available to **both** Soryō and Ritsuryō rulers, is one way to build up durable power, and Japanese rulers will have many unique manor buildings for this purpose. Costs and benefits are both modified to better fit the needs and resources available in Japan. For the Soryō especially, this is how special men-at-arms are strengthened and unlocked.  

Another way to build up the power of your house is to invest your prestige into **House Aspirations**. House aspirations have a theme and spending more prestige to upgrade them will unlock abilities and modifiers that will allow you to both specialize and grow the resources available to you. Aspirations will allow you to shape the strengths of your House by focusing on military might, intrigue, or economic development, and will also unlock certain upgrades for your family manor.  

---

## Southeast Asia​

![image_08.png](https://forumcontent.paradoxplaza.com/public/1296652/image_08.png "image_08.png")



Southeast Asia in this timeline is not yet as close to the Chinese sphere of influence as Japan or Korea. The mainland as well as the islands are a mix of indigenous faiths with tribal rulers and Indophile states practicing Hinduism or Buddhism. Unlike the bureaucratic nature of the realms to their north, the realms here are often more transitory in nature. Small central realms often control networks of tributaries that contract or grow with relatively little drama. The Great Empires of this region were often more advanced versions of this, with priests administering the realm on behalf of self proclaimed God Kings based in enormous temple cities.  

### Mandala Government​

In *All Under Heaven*, Buddhist and Hindu states in southeast Asia will predominantly start with the new Mandala Government. This government form initially has a lower vassal and domain limit, and instead relies on its own flavor of tributaries in a greater way.  

Mandala realms have the new Temple Citadel as their main holding type, though they can also hold castles and temples.  

#### Devaraja - God Kings​

An independent Mandala ruler is considered a God King, or Devaraja. Most of your authority and power will stem from piety and many things that would otherwise cost prestige or even gold will now consume piety.  

To be a Devaraja means aspiring to be an ideal ruler in Buddhism or Hinduism, with your radiance attracting tributaries and vassals to your cause. The more convincing you are in this respect the more tributaries you will be able to steal from other rulers, and the more your power can grow.  

Devarajas also have access to several new levels of devotion, with increasing benefits that will increase the initially restrictive domain and vassal limits of the government. By advancing your status as a God King, a Mandala can eventually end up quite powerful, even if the initial drawbacks in the form of lower vassal and domain limits might make the government seem weak at first glance.  

#### Capital Temple​

![image_09.png](https://forumcontent.paradoxplaza.com/public/1296654/image_09.png "image_09.png")



As a God King, the cult around your person is essentially the same thing as your authority as a ruler. To remind everyone of their power, rulers would construct great temple cities. Complexes such as Angkor Wat or Borobudur still stand today and demonstrated the divine power of rulers by showcasing their power and by providing a ceremonial center for the realms of the god kings.  
Capital Temples make use of the new Great Project feature to let you, your vassals, and your tributaries invest in the growth of your Capital Temple.  

While they are costly, Capital Temples are the first way in which you can alleviate the domain and vassal limit restrictions of your government type along with many other bonuses. A grand capital temple is also what will make tributaries remain with your heirs, who may not yet be as impressive in their role as divine rulers as you are.  

#### Devaraja Aspects​

Similar to the Japanese House Aspirations, as a God King you will be able to invest piety into developing your personal cult. Focusing on warlike qualities will make it easier to gain piety through wars. Focusing on serenity might instead mean you can earn piety through more peaceful means, as an example. Your choice of Devaraja aspects will also decide what benefits you get from having high levels of devotion.  

---

## Additional Features in *All Under Heaven*​

### Great Projects​

As mentioned above, another new feature to this update is Great Projects. This is a way for multiple rulers to pool their resources together to create something. Usually, this would be the vassals in a realm coming together to help fund something like the Great Wall, but it can also be local governors banding together to help push through disaster relief after a Natural Disaster. Benefits can be both direct, related to what the goal of the project itself is, and more individual, in terms of what the contributors get for helping.  

A new type of building slot has also been introduced to allow Great Projects to create their own type of buildings that coexists with Special Buildings or Monuments. Not all Great Projects relate to a great building or monument however, though all will have tangible effects once they are completed.  

There are a number of new Great Projects introduced in *All Under Heaven*. Like with all other features described today, we will talk more about what projects exist and about Great Projects as a feature in a future diary.  

### Natural Disasters​

Natural Disasters are a type of recurring **Situation** that can strike in known areas. While the disaster impact is over relatively quickly, the Situation will linger and center on the rebuilding of the region after something like a great flood.  

Every Natural disaster comes with a related Great Project, which means multiple characters in the same area can come together to fund the recovery effort. To this end, the projects also come with a number of optional investments that can potentially leverage the situation either for political benefits or lead to rebuilding the area to be more prosperous than it was prior to the disaster. Our intent here is not that natural disasters be a random and extremely punishing blow to your game but rather something to overcome that can present you with opportunities to demonstrate your skills as a ruler and use it as a possibility to ultimately advance your goals.  

### The Silk Road​

While China was enormously important in East Asia and its surroundings, for many parts of the world China’s impact was more indirect. We wanted to take the opportunity to include this in the expansion, since it was still quite tangible.  

For millennia, goods and innovations have flowed from China towards the west. Trade is not a feature of *All Under Heaven*, but the Silk Road will be visible on the map and controlling its entrepots will yield economic benefits if China is in an era where it is stable. Another venue that will be open to western rulers is that travelers to the entrepots of the Silk Road may help spread Chinese innovations to their home realms.  

### What About the Other Parts of the Map?​

This diary tries to give an overview of all major features for the expansion, but it also leaves a lot unsaid for future diaries. In the coming weeks, we will be giving a closer overview of not only the features already described but also things not mentioned, such as Korea, the northern steppe, the tribal states in southeast Asia, and, of course, the map itself. Next week’s diary will start out by giving an overview of the new map, which will then be followed by more detailed breakdowns as we go through the features for each area.

<!-- artifact:reactions:start -->
- 171 Love
- 152 Like
- 15 (unlabeled — rendered as base64 data URI)
- 10 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
- 1 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Trin Tragula](https://forum.paradoxplaza.com/forum/members/trin-tragula.18587/)**
Role: Game Designer - Crusader Kings 3
Badges: 36
Reaction score: 16,644

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
