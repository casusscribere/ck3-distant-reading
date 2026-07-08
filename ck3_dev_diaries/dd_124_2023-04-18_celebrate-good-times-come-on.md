---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1578426/"
forum_thread_id: 1578426
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 124
title: "Dev Diary #124 - Celebrate Good Times (Come On)"
dd_date: 2023-04-18
author_handle: Paradoksalny Kierownik
expansion: Tours and Tournaments
patch: Patch 1.9
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 6956
inline_image_count: 81
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1578426'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2300.jpg?1681755591
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_164_to_166
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_818_to_821
    action: preserved_and_flagged
    counts:
      Love: 119
      Like: 104
      (unlabeled — rendered as base64 data URI): 11
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_829_to_891
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_892_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2300.jpg?1681755591)
<!-- artifact:thread_banner:end -->

# Dev Diary #124 - Celebrate Good Times (Come On)

<!-- artifact:thread_metadata:start -->
- Thread starter [Paradoksalny Kierownik](https://forum.paradoxplaza.com/forum/members/paradoksalny-kierownik.1725641/)
- Start date [Apr 18, 2023](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-124-celebrate-good-times-come-on.1578426/)
<!-- artifact:thread_metadata:end -->

## Of Weddings, Feasts, and Other Merry-Making​

Welcome, one and all, royal peers from faraway lands, faithful vassals, and errant knights! You are hereby invited to Duchess Matilda’s Grand Wedding!  

![1 - invitation.png](https://forumcontent.paradoxplaza.com/public/955971/1 - invitation.png "1 - invitation.png")


*(Invitation to Duchess Matilda’s Grand Wedding)*  

Today’s town crier, bringing you news about royal marriages, is game designer Areysak.  
Following that, my colleagues will take over to introduce today’s other topics: Bloody Weddings, Feasts, Grand Blots, Grand Rites, and Playdates. We have a packed day, filled with exciting activities, so let’s get started!  


## But Why Weddings?​

Weddings have always been an important event in the life of people; while for the longest time commoners’ weddings lacked much of the formality we have now come to expect from the event, Royal Weddings in the Middle Ages were already a huge deal. Weddings between aristocratic families were, after all, political events of a mostly public nature!  

So far, weddings in CK3 (and even before that, in CK2) were represented by a simple interaction: clean and effective, but hardly apt to represent the magnificence, the expenses, and the ramifications of such an event.  
While the simple interaction is still available and doing its job, we have also decided to give the player the possibility to choose a more immersive and in-depth experience of what a wedding celebration could look like in the world of Medieval nobility. I put the stress on immersive and in-depth to underline the two sides of the coin: immersion relates to roleplaying, since flavor is offered aplenty, while depth calls for new challenges, which we can summarize as Great rewards come to those who are daring - and not too stingy!  


## Of Commitments and Commitment Issues​

But let’s now take a closer look at what a Grand Wedding is.  

A Grand Wedding is a type of Grand Activity exclusively unlocked by the Tours and Tournaments Expansion. Contrary to other activities introduced so far, however, Grand Weddings are not immediately and always available. In fact, they can only be organized for specific betrothed couples to which a Grand Wedding has been promised at the time of the betrothal. I can already see you jumping in your seats — Wait, betrothed? Is this only for children?!  
NO! I can confirm that adults can now be betrothed too!  

When proposing a marriage, you will find a checkbox to add a Grand Wedding clause to it. Valid matches include your own marriage and those of your relatives, as long as your spouse candidate is set to be the dominant side in the couple (i.e., the one whose dynasty the kids will belong to).  
(Please ignore the costs in this and following screenshots, it won’t be that cheap!)  

![2 - offer_gw.png](https://forumcontent.paradoxplaza.com/public/955972/2 - offer_gw.png "2 - offer_gw.png")


*(Arrange marriage interface, with Grand Wedding checkbox and descriptive tooltip)*  

A Grand Wedding is a grandiose and prestigious event, so offering to host one for a spouse will immediately increase their acceptance, perhaps even allowing a character to marry above their station.  
However, this comes with a catch: promising a Grand Wedding is a serious business! It is a diplomatic, bonding agreement in which the reputation of a whole family is at stake, and the validity of the betrothal (and connected alliance) depends on this promise being kept. From the moment the wedding can be organized, the other party will be patient for 3 years; breaking the betrothal or failing to organize the Grand Wedding in the set time will invalidate the betrothal, hurt your reputation, and massively annoy the other party.  

![3 - countdown_gw.png](https://forumcontent.paradoxplaza.com/public/955973/3 - countdown_gw.png "3 - countdown_gw.png")


*(Alert icon and tooltip reminding the player that a Grand Wedding can be organized, and will expire if not)*  

![4 - betrothal_expired.png](https://forumcontent.paradoxplaza.com/public/955974/4 - betrothal_expired.png "4 - betrothal_expired.png")


*(Event shown when a Grand Wedding Betrothal expires)*  

Offering a Grand Wedding is, therefore, a risky commitment, and you might reasonably wonder if the increased acceptance alone is really worth it…  
It probably wouldn’t be, which is why promising a Grand Wedding is only the first step!  


## Do We Need a Wedding Planner?​

The next step is organizing the Activity. Now that we have promised a Grand Wedding, the Activity is available from the activity menu, but can also be easily accessed from a top-screen notification.  

![5 - organize_gw.png](https://forumcontent.paradoxplaza.com/public/955976/5 - organize_gw.png "5 - organize_gw.png")


*(Host a Grand Wedding in the Activity Menu)*  

Since only one Grand Wedding can be promised by the same person at the same time, the setup view comes with the spouses pre-selected — handy!  

![6 - setup_view.png](https://forumcontent.paradoxplaza.com/public/955977/6 - setup_view.png "6 - setup_view.png")


*(Grand Wedding setup view)*  

The activity setup is pretty simple, and similar to other activities. From this interface, you can select where you want to host the Wedding, set your travel up if needed, choose your Intent, invite your guests (for ease of access, the most obvious choices such as the spouses’ families are pre-selected), and change the options.  
Like in the other Activities, Intents steer the events that will happen to your character, or unveil specific ways to react to them. Wedding Intents include some classic “hobbies” of CK3 characters, such as plotting murders and seductions, but also some new and exclusive Intents: Diplomacy and Matchmaking. Can you guess what they do?  

![7 - intents.png](https://forumcontent.paradoxplaza.com/public/955978/7 - intents.png "7 - intents.png")


*(Intent Menu for the host in the setup view of a Grand Wedding)*  

Matchmaking is a flavorful bit of innocent meddling into an unmarried relative’s life; after all, what better occasion than a wedding to find a worthy spouse (or maybe a very unworthy one?) for your younger brother who has been feeling so lonely?  
However, weddings are not all about casual socialization and careless flirting; as mentioned at the beginning of this Dev Diary, weddings are also political events, in which the nobility of a country and their peers from foreign lands sit at the same table and mingle. Intrigue may hide behind every corner, but it’s also the perfect occasion to conduct some official diplomacy. This is where the Diplomacy Intent fits in. By picking this intent, you will choose a guest and be offered occasions to improve their opinion of you, gain hooks on them (even a temporary strong hook on your liege, a very rare opportunity in game!), gain an alliance without the usual requirements (a marriage or a special perk), or even make a more convincing case for subjugation!  

Options, too, are not just flavorful bits you can toy around with for immersion; they can make your Wedding considerably more (or less) expensive, with immediate repercussions not only on the appearance of some events, but mostly on what you can expect to gain from hosting the Grand Wedding! For instance, Entertainment will give you more prestige, Food will make an impression on your guests, and the Venue will increase your Renown.  
Simply put, the more you spend, the more bonuses you can gain back, although not all your vassals will be impressed by the same things.  

![8 - options.jpg](https://forumcontent.paradoxplaza.com/public/955979/8 - options.jpg "8 - options.jpg")


*(Zoomed view of a selected option from the Grand Wedding setup view)*  

Now that everything is ready, let’s get the show started!  


## It’s My Big Day and You Can’t Ruin It!​

![9 - travel.jpg](https://forumcontent.paradoxplaza.com/public/955980/9 - travel.jpg "9 - travel.jpg")


*(Activity interface with traveling spouse)*  

When the activity starts, you and your guests start traveling towards the activity location. In the activity view, you can keep track of where your character and the spouse(s) are at any point.  

Once both spouses have arrived at the wedding venue, you can see an overview of the ongoing pre-celebration party. Look at this merry bunch having the time of their life!  
You might have noticed that the bride has put on her best flower crown, and the groom has a new wedding crown too; they are all ready for the celebration!  


![10 - merry_making.jpg](https://forumcontent.paradoxplaza.com/public/955887/10 - merry_making.jpg "10 - merry_making.jpg")


*(Activity view of a Grand Wedding before the start of the activity. The spouses and some guests who have already arrived are shown while drinking and celebrating)*  

Finally, it’s time to start!  


![11 - ceremony_start.jpg](https://forumcontent.paradoxplaza.com/public/955888/11 - ceremony_start.jpg "11 - ceremony_start.jpg")


*(Opening event of the Grand Wedding)*  

Weddings have 3 phases; the first phase is the Ceremony, which is a less formal event than we are used to thinking in modern times. While the spouses are mostly busy in the required rituals, the guests mingle, get distracted, and occasionally get up to some mayhem.  


![12 - ceremony_event.jpg](https://forumcontent.paradoxplaza.com/public/955889/12 - ceremony_event.jpg "12 - ceremony_event.jpg")


*(The ceremony is happening)*  

For most of the western Middle Ages, a wedding was considered religious and valid independently from where it was celebrated, and it would rarely take place inside a religious building. Rulers’ weddings, which were big political and public events, were much more likely to take place in the open space in front of a church, rather than inside of it, which is the background we have chosen.  
From what we have been able to back-date, traditional Hindu or Muslim weddings don’t belong in religious buildings either. For the Indian background, we have chosen a rendition of the traditional mandap (a canopy made of 4 wooden pillars supporting a frame, decorated with leaves and flowers), and a central position is reserved to the holy fire, which plays a fundamental role in Hindu wedding rituals (although the rebellious daughter above is standing exactly in front of it).  
For Muslim weddings, instead, we preferred a more enclosed space, reminiscent of a household’s courtyard, richly decorated with carpets and veils.  

In Christian tradition, for the longest time, a religious figure was not required to validate a wedding, and if members of the clergy were involved, their function was something in-between bearing witness and giving a special blessing. Considering the social weight of a royal wedding, we generally tried to find a valid religious character to bless your union. After all, what could look more prestigious and attest more to your piety than inviting the Pope and having him bless your wedding personally? However, the spouses can also receive a lay blessing from the host if they are important enough, or in religions with lay clergy.  

It might come as a surprise, considering the long history of arranged, political, and even forced marriages, but it was generally agreed throughout the Middle Ages that the only real requirement for a marriage to be valid was the consent of the spouses (how that consent was obtained was not investigated though). Therefore, the Ceremony culminates and concludes with the formal assent to the union from the spouses. I’ll let you find out by yourselves what happens if you say “I don’t”!  


![13 - i_do.jpg](https://forumcontent.paradoxplaza.com/public/955890/13 - i_do.jpg "13 - i_do.jpg")


*(Concluding event of the Ceremony phase, with the spouses giving their consent to the marriage)*  

If you say “I do”, you are now officially married, congratulations!  

However, the day is still long, as anyone who has at any point gotten married can testify.  

The second phase is called the Banquet, and it’s basically a wedding reception. Offering and partaking in luxurious meals with your guests is an almost universally understood way of celebrating a big event; banquets — more often after the ceremony, but in some cultures even before it — have naturally long accompanied weddings, and the celebrations could last for days!  

Wedding Banquets are quite similar to Feasts, as in liberal amounts of food and drinks are served, to the undying delight of gluttonous and drunkard characters. However, Banquets are also an eminently social moment, ideal to advance your political, seductive, or murderous goals. It is also the perfect time to show off the entertainment you have paid for during the activity setup, to wow your guests with dazzling decorations, and to ensure everything proceeds as planned thanks to a fleet of diligent servants.  


![14 - banquet_event.jpg](https://forumcontent.paradoxplaza.com/public/955892/14 - banquet_event.jpg "14 - banquet_event.jpg")


Finally, the last phase is the Wedding Night. As you can imagine, this phase plays quite differently for the spouses and the guests! For the guests, it is almost an extension of the party, where they can socialize, abscond to a secluded room, or enjoy the slow quieting of the venue in a drunken stupor.  

… Or maybe not so quietly.  


![15 - wedding_night_guest.jpg](https://forumcontent.paradoxplaza.com/public/955893/15 - wedding_night_guest.jpg "15 - wedding_night_guest.jpg")


The spouses, instead, must consummate the marriage! Therefore, the scene moves to the bedchamber — and we have some gorgeous new art for the room, by the way — where awkwardness, wholesomeness, accidents, and even *murder* can happen, for those who are bold enough…  


![16 - night_event.jpg](https://forumcontent.paradoxplaza.com/public/955894/16 - night_event.jpg "16 - night_event.jpg")


When all is said and done, the Grand Wedding finally comes to an end. The satisfied host bids the departing guests goodbye, and the newlyweds return to their new home. Everyone has gained something, depending on the options selected by the host: prestige, opinion, renown, modifiers… After all, there’s great glory in paying for organizing such a magnificent grand event, but there is also in being offered such a luxurious wedding, and even in taking part in the Wedding of the Century!  


![17 - conclusion.jpg](https://forumcontent.paradoxplaza.com/public/955896/17 - conclusion.jpg "17 - conclusion.jpg")


*(Grand Wedding is concluded. Would the live happily ever after?)*  


## Bloody Wedding​

So now you have the whole family gathered together. All in one, nice place. But did no one really come up with the idea of killing all of their enemies using this perfect occasion? Well, they did.  

When Olga of Kiev's husband Igor was murdered by the Drevlians, they sent her a message proposing that she marry his murderer, Prince Mal. According to the Primary Chronicle, 20 ambassadors were chosen to deliver this proposal to Olga, who expressed interest in the marriage, and then buried them alive in revenge.  

A more significant event happened in the year 1357, in Majapahit. King Hayam Wuruk decided to take princess Citra Rashmi, of the Sundanese royal family, as his wife. However, the prime minister of Majapahit had different plans and demanded that Sunda became a vassal of Majapahit and tried to downgrade the princess to a mere concubine.  
As one can imagine, this didn't go down well.  
A skirmish broke out and almost all of the Sundanese royal party - including the king - were massacred.  
The aftermath of this tragedy damaged relations between the two kingdoms in a way that many thought irreparable.  

Another important inspiration for our Bloody Weddings was that of Count García de Castilla and princess Sancha de León, in 1029, quite similar to the Majapahit incident. When Count García traveled to León to finally meet his betrothed, he was instead ambushed by the Vela family, enemies of the counts of Castille for centuries and protected by the king of León, and was assassinated next to the church where he was supposed to be married. This murder had equally extensive consequences, ending the male hereditary line of the counts of Castille.  

The only person that can organize a Bloody Wedding is the host, but you don't need to be the spouse. As we saw above, it was a family close to the spouse that killed the groom, not the wife herself.  

With this in mind, we wanted to offer to the player the power fantasy of ending an enemy lineage in one big, consequential event. And thus, we decided to make the punishments for using it equally consequential. It's not every day that you try to end a house.  

So. The unlocking perk for the Bloody Wedding is Accomplished Forger. For this there are 2 reasons: one, we already used an Intrigue perk for the Murder Feasts (see below) and two, we noticed that the Diplomatic tree was ranked kind of low by many players and wanted to give them something special. It's also important to note that the connection between Weddings and Diplomacy in our game is pretty strong.  


![Bloody Wedding 1.png](https://forumcontent.paradoxplaza.com/public/955897/Bloody Wedding 1.png "Bloody Wedding 1.png")


*(Bloody Wedding perk requirement)*  

But it's not the same thing ending a completely random family than assassinating your liege. To reflect this, targeting your liege or their family in a Bloody Wedding will tank your Prestige level by 3, as will your Piety levels if by chance you target your Head of Faith.  
Obviously, Just, Compassionate and Calm characters are also not big fans of indiscriminate murder, and will get massively stressed while trying to accomplish one.  


![BW 2.png](https://forumcontent.paradoxplaza.com/public/955899/BW 2.png "BW 2.png")


*(Bloody Wedding preparation screen)*  
The activity options and intents are the same as in a regular wedding, to not arouse suspicion, and in case you decide to murder only the spouse you can still get some (greatly lowered) rewards from the decoration or the food. If you wipe their entire family, however, there's nothing you can do to convince your guests of how prestigious you are.  

The cost of organizing a Bloody Wedding is also significantly higher than a regular wedding, contributing to making it quite prohibitive. Of course, it will still escalate with tier and era as with most of our activities (numbers in the screenshots are not final).  


![BW3.png](https://forumcontent.paradoxplaza.com/public/955900/BW3.png "BW3.png")



At the beginning of your wedding you will get a starting event setting the tone of the whole ceremony: do you want to murder all of the family, just the spouse, or just the spouse during your wedding night (only available if you're the one getting married, of course), which leads to a more subtle killing, but leaves the door open to failing in your attempts.  


![BW4.png](https://forumcontent.paradoxplaza.com/public/955905/BW4.png "BW4.png")



After that, the wedding progresses as usual. All the guests get the non suspicious ceremony and gathering events, and even make it to the Banquet phase with (hopefully) no second thoughts. However, when the Banquet is about to reach its end, tragedy happens. If you haven't chosen the Wedding Night kill option, the murder is carried out.  

We have added several different texts that take into account your relationship with the victim, your personality traits and a couple of random chances: in any case, though, the framing of the whole family murder is that mercenaries interrupt the festivities, killing everyone present. In the case of the murder of only the spouse, the framing is that of a hostile agent.  


![BW5.png](https://forumcontent.paradoxplaza.com/public/955906/BW5.png "BW5.png")


![BW6.png](https://forumcontent.paradoxplaza.com/public/955907/BW6.png "BW6.png")




After the murder is done, both guests and host get aftermath events, taking again into account the host's personality and relation to the victim, as well as the guest's (you don't care as much if you hated the poor spouse, for example).  

Then, we hand out the "rewards" for the host, which are more of a punishment than anything - after all, what bigger reward than murdering an entire family?  

![BW7.png](https://forumcontent.paradoxplaza.com/public/955908/BW7.png "BW7.png")



If you've killed the entire family in a wedding under your protection… well, it doesn't go down well with basically anyone. It especially doesn't go down well with your Head of Faith, who doesn't really care whether you did it yourself or not, you've violated the sanctity of marriage and the laws of hospitality, one of the most important laws in the Middle Ages.  

The result? Excommunication. What is more, the Recent Excommunication modifier is extended for 5 years, which (apart from the opinion maluses) prevents you from asking to be taken back until its expiration. And in case your faith doesn't allow for excommunication, you lose Piety levels instead.  
Your Diplomacy is also greatly affected by whatever you tried to pull here: the Distrustful Host modifier greatly lowers your skill, but helps you maintain a dreadful aura.  

Apart from that, everyone that's not particularly sadistic thinks that you are not great, and lose Opinion of you on top of the Excommunication drops.  

All in all, you *can* eradicate a rival family (in case they all show up to the wedding, of course), but you will have to face the consequences for it.  


![BW8.png](https://forumcontent.paradoxplaza.com/public/955909/BW8.png "BW8.png")


![BW9.png](https://forumcontent.paradoxplaza.com/public/955910/BW9.png "BW9.png")



But that's not all! If the victim had surviving relatives, they're not happy with this. A week later you will receive a letter from their closer family member (their heir, if they're alive), berating you for not protecting the spouse. This starts a House Feud. Not only that, you become rivals with the person who sent the letter and every close family member loses even more opinion of you, getting kind of suspicious of your intentions. A Prestige hit is also warranted, as a treat.  

![BW10.png](https://forumcontent.paradoxplaza.com/public/955911/BW10.png "BW10.png")



The AI for Bloody Weddings is heavily weighted to not want anything to do with this. The consequences - and the noble understandings that ruled over the medieval world - are enough for them to not even consider the possibility. However, a particularly Sadistic AI with a lot of gold to burn and an important grudge against someone may try to orchestrate something like this, bringing the world alive.  

You promise a Wedding and organize a Funeral, but keep in mind - the price is high in both gold and blood.  


## More Revamped Activities​

In previous Dev Diaries, we have introduced the New and Improved Versions of Pilgrimages and Hunts, but you might have been wondering: “What about the other old activities?”  
Of course, we have not forgotten about them! Take your seat at the table and join us for a Feast (and more)!  

## Feasts​

Does a Feast need a reason?  

Feasts, together with Hunts, are the main way the game handles stress loss right now, and we wanted to keep that in mind when revamping them. Feasts now have clearer rewards, including prestige and opinion gain not only through events, but also based on the activity options you pick.  

![Feasts 1.png](https://forumcontent.paradoxplaza.com/public/955914/Feasts 1.png "Feasts 1.png")



There are two options when hosting a Feast: Dish Complexity, which affects the prestige gain, and Number of Courses, which affects the attendant opinion. These options start with the middle values, but the player can choose to lower them for a cheaper feast (if you don't really care about Prestige or Opinion and just want the raw stress loss - although do keep in mind that a cheaper feast can lead to some bad events) or increase one of them if that's the reward they're after!  

![F2.png](https://forumcontent.paradoxplaza.com/public/955915/F2.png "F2.png")

![F3.png](https://forumcontent.paradoxplaza.com/public/955916/F3.png "F3.png")



There's also something new we've added in this expansion in the form of Honorary Guests. An Honorary Guest is a special guest that will receive the toast at the center of the Feast, granting them some extra Prestige and Opinion of you. If an invited character is not attending, making them your Honorary Guest will give them a great acceptance boost, so use it wisely.  

![F4.png](https://forumcontent.paradoxplaza.com/public/955921/F4.png "F4.png")



As for intents, we have the usual suspects: Recreation, Murder, Seduce and Befriend. With a special option if you join as a guest: Mischief. Mischief works in a very similar way as Recreation, with a main focus on losing stress, but allowing for more irreverent and malicious - yet funny - situations.  

![F5.png](https://forumcontent.paradoxplaza.com/public/955922/F5.png "F5.png")



When it comes to choosing a place to hold your Feast, you will receive different discounts if you have certain buildings in the province: like manor houses, leisure palaces, or certain special buildings. The chosen province will also get a special modifier as a reward!  

![F6.png](https://forumcontent.paradoxplaza.com/public/955923/F6.png "F6.png")



![F7.png](https://forumcontent.paradoxplaza.com/public/955924/F7.png "F7.png")



And with that, we're ready to start! The events that you will receive during the Feast are some old acquaintances, and their purpose remains the same, although the effects, animations and text have been tweaked in some cases to best reflect the new activity system. New events have also been added to account for the added intents!  

![F8.png](https://forumcontent.paradoxplaza.com/public/955925/F8.png "F8.png")


![F9.png](https://forumcontent.paradoxplaza.com/public/955926/F9.png "F9.png")



We've also added a bunch of Activity Pulse Actions! Random, smaller events that happen throughout the activity to keep it lively. They offer a tiny bit of flavor and help the game feel more alive. And they, of course, can also give you some nice, unexpected rewards in the form of your wife learning someone's secret, or your child gaining some prestige by impressing everyone with their manners.  

![F10.png](https://forumcontent.paradoxplaza.com/public/955928/F10.png "F10.png")


![F11.png](https://forumcontent.paradoxplaza.com/public/955929/F11.png "F11.png")



And then there's the Toast! The Toast is the main event of a Feast, and the host can always choose whether to make a toast in honor of their special guest or, well, just honor themselves.  

![F12.png](https://forumcontent.paradoxplaza.com/public/955930/F12.png "F12.png")


![F13.png](https://forumcontent.paradoxplaza.com/public/955931/F13.png "F13.png")



And with that we reach our end! We collect the rewards, say thank you very much and go back to accumulating stress for the next 5 years!  

![F14.png](https://forumcontent.paradoxplaza.com/public/955932/F14.png "F14.png")



What do I get if I attend a Feast, though? You get more or less the same as the host: stress loss, opinion of the participants, and Reveler xp!  


## Murder Feasts​

Murder Feasts, however, are inspired by an anthropological tale type called "myths of the revenge feast". We find these in Greek mythology (Thyestes), the Poetic Edda (Skadi, Wayland the Smith), etc.  

But we also find examples of this in real life; after all, gathering all of your enemies in the same place and casually slaughtering them feels like an incredibly convenient way of getting rid of all your provinces at once. Among the most famous cases we have the Black Dinner of 1440, where the Clan Douglas served a black bull's head in a non-ominous at all fashion… and then proceeded to murder 16-year-old William Douglas, and his younger brother, just regular inter-clan grudges.  

Something similar happened in the "Toledan night" of 797, where Amrus ben Yusuf invited the richest and more powerful nobles to his palace… then murdered them.  

But Murder Feasts weren't only in legends and History, they were already present in CK3. If you hadn't noticed this don't worry, since they were extremely difficult to trigger to a point that they just never triggered, full of random chances and ultra specific sets of traits. But, they were there!  

With this in mind, we wanted to make Murder Feasts into a type of Feast that both players and AI can access in an intuitive way rather than purely relying on RNG ~~and praying.~~  

*So*. To start a Murder Feast you need to have the Forever Infamous perk, from the Torturer lifestyle tree. We chose the Torturer one for thematic reasons but also because we realized it's just… not that good. The perk is fairly down the tree, also making it harder to obtain.  

![Murder Feast 1.png](https://forumcontent.paradoxplaza.com/public/955933/Murder Feast 1.png "Murder Feast 1.png")


![MF2.png](https://forumcontent.paradoxplaza.com/public/955934/MF2.png "MF2.png")



Targeting your Liege or Head of Faith will make you drop Prestige and Piety levels respectively, as with Bloody Weddings, so keep that in mind. Characters with "good" traits (Just, Compassionate, etc) will also get stressed by engaging in, well, massive murder.  

![MF3.png](https://forumcontent.paradoxplaza.com/public/955935/MF3.png "MF3.png")



You can still choose your Activity Options as in a regular Feast, and you will receive lowered amounts of their default rewards (Opinion and Prestige), but only if you don't murder all of the entourage - in that case, people are a bit too traumatized to think how cool of a host you are.  

Then the most important step: picking your victim. The Honorary Guest will be your murder target, and you will get the opportunity to kill them and their entourage, or just them (more on this later). Of course, for everyone else they will appear as "Honorary Guest" in the same way as in a regular Feast, but for you, you will know.  

(Your intent is also locked in Recreation so the guests don't suspect by seeing a "Slaughter Everyone" intent)  

![MF4.png](https://forumcontent.paradoxplaza.com/public/955936/MF4.png "MF4.png")



Once the Feast starts you'll get a pretty straightforward starting event asking you how you wanna proceed with this: Do you wanna kill your victim and their entourage (which is normally gonna be mostly unlanded courtiers, although not always), kill just your victim or kill your victim and make sure no one knows (which will have a lower chance of succeeding, but also a lower chance of getting caught.  

![MF5.png](https://forumcontent.paradoxplaza.com/public/955937/MF5.png "MF5.png")



Once you decide on the entré, the Feast continues with normality. You'll be getting events about how people are drinking, flirting, getting in fights or just having fun - until the moment of the toast. That's where the massacre happens.  

![MF6.png](https://forumcontent.paradoxplaza.com/public/955938/MF6.png "MF6.png")


![MF7.png](https://forumcontent.paradoxplaza.com/public/955939/MF7.png "MF7.png")



There are 5 different text variations for each of the killing options so you get all the variation you need while plotting (and executing (pun intended)) your slaughter for the 15th time. The thematic, however, is always similar: for the full entourage murder we frame it as an unfortunate fire or the group gets mysteriously poisoned. If the lady or gentleman prefers a single kill, however, we opt for an unfortunate accident with a knife or, well, more poison, all in different flavors. These descriptions, it's worth mentioning, also take your traits into account.  

Once the work is done it's time for the clean up. You show up, lament a bit, and say farewell to the survivors, reaping your rewards.  

![MF8.png](https://forumcontent.paradoxplaza.com/public/955940/MF8.png "MF8.png")


![MF9.png](https://forumcontent.paradoxplaza.com/public/955941/MF9.png "MF9.png")


![MF10.png](https://forumcontent.paradoxplaza.com/public/955942/MF10.png "MF10.png")




And with that, it's all done—... is it?  

![MF11.png](https://forumcontent.paradoxplaza.com/public/955943/MF11.png "MF11.png")



## Blood for the Blood God​

For those of you who purchased Northern Lords we have updated the Grand Blót to work with the new Activity System. All the content, costs, and rewards have remained untouched. While we haven’t added any new content here, however, the new system allows for additional choices when planning a Blót.  


![blot_1.png](https://forumcontent.paradoxplaza.com/public/955944/blot_1.png "blot_1.png")



*[Screen where you elect to host a Blót]*  

You can now select a location in your realm, as long as that location has the ability to conduct grand sacrifices. All your guests will travel to this location.  

![blot_2.png](https://forumcontent.paradoxplaza.com/public/955945/blot_2.png "blot_2.png")


*[Location selection screen for a Blót]*  

The new system also provides more control over the guest list. You can select and deselect the guest invite groups for your Blót at will.  


![blot_3.png](https://forumcontent.paradoxplaza.com/public/955946/blot_3.png "blot_3.png")


*[Guest Selection screen for a Blót]*  

A majority of the event content for Blóts was centered around choices for planning: will you augment the normal arrangement of animal sacrifices with the blood of man to sate the gods’ appetites? These choices, which were previously event options, are now entirely integrated into the Activity planning screen.  

![blot_4.png](https://forumcontent.paradoxplaza.com/public/955947/blot_4.png "blot_4.png")


*[Activity Option for a Blót; “Humans - Majestic” option selected]*  

As for what happens during the Blót, nothing has changed on that front–sacrifices occur, opinion is gained or lost, and the gods are pleased. We haven’t added any new event content, save a small set of Pulse Actions and the new conclusion screen with the Activity Log. Our primary focus here was to better tie some of these smaller activities to the map and transition them to the new system.  

![blot_5.png](https://forumcontent.paradoxplaza.com/public/955948/blot_5.png "blot_5.png")


*[The main event for a Blót]  

![blot_6.png](https://forumcontent.paradoxplaza.com/public/955949/blot_6.png "blot_6.png")


[An example of a Pulse Action for a Blót]  

![blot_7.png](https://forumcontent.paradoxplaza.com/public/955950/blot_7.png "blot_7.png")


[The conclusion screen for a Blót]*  

With that said, we realize that the new Activity system highlights the lack of event content for Blóts in particular. Several of us on the team have commented on this and would like to take another look at it in the future, but alas: ars longa vita brevis. The craft is long, but life short.  

## Grand Rite​


The skillful player will remember what could be the most "secret" activity that we have in the game: the Grand Rite. After all, not that many medieval rulers started their own witch covens to worship the horned one ~~and us, as His humble followers, must remain hidden.~~  

To start a Grand Rite you need to have a Witch Coven; after all, it wouldn't be grand if it's only you yelling at the moon in the middle of a meadow, right? And to start a Witch Coven you need, well, witches.  

The requirements for a Witch Coven remain the same: You need to be the House Head and 4 adult members of your house need to have the Witch trait or secret. Once you've founded one, the usual rewards follow, apart from the ability to host Grand Rites from now on.  

![Grand Rite 1.png](https://forumcontent.paradoxplaza.com/public/955951/Grand Rite 1.png "Grand Rite 1.png")



A Grand Rite is a modest, familiar, cozy activity. You will enjoy a nice evening by rotten trees and murdered squirrels, pools of blood and beautiful *(are those human?)* bones. But the rewards are nothing modest! Apart from some Stress loss in the tranquility of the night, and Opinion gain of your fellow witches, you may also gain valuable Lifestyle experience, coming from studying necromancy and its rituals with great dedication.  

![GR2.png](https://forumcontent.paradoxplaza.com/public/955952/GR2.png "GR2.png")



The Hidden One is a jealous creature, and He doesn't allow for many other, superfluous options that could distract you from your true intent: His worship.  

![GR3.png](https://forumcontent.paradoxplaza.com/public/955953/GR3.png "GR3.png")



As for invites… Well, you can only invite other Witches. Anything else would be like holding court and immediately stripping naked to dance around a bonfire and sacrifice some child - a normal Tuesday.  

As all other activities, Grand Rites have their own set of Pulse Actions that will give you smaller, yet flavourful rewards, like worshiping the moon, playing mournful music and sacrificing small animals while you wait for the main events.  

![GR4.png](https://forumcontent.paradoxplaza.com/public/955954/GR4.png "GR4.png")



We've also tweaked the old events to make them better fit the new assets and features, with what I deem a really cool gothic look to them.  

![GR5.png](https://forumcontent.paradoxplaza.com/public/955955/GR5.png "GR5.png")



But that's all for the Grand Rite! Many in the CK team are fascinated by its secrets and flavor, and would like to take another look at it in the future to make it as grand as it should be. No promises, though! We have a lot to tackle first  

## How do you do, fellow kids?​

If you’ve ever played as a child in CKIII, you know that the Meet Peers Activity is one of the few things you can elect to do. Just as with Blóts and the Grand Rite, we’ve transitioned Meet Peers to use the new Activity System.  


![meet_peers_1.png](https://forumcontent.paradoxplaza.com/public/955956/meet_peers_1.png "meet_peers_1.png")


*[Meet Peers planning screen]*  

There are a slew of categories to choose from when it comes to inviting fellow children. You can choose as many or as few as you like! And they’ll travel to your Realm Capital.  

![meet_peers_2.png](https://forumcontent.paradoxplaza.com/public/955957/meet_peers_2.png "meet_peers_2.png")


*[Guest selection screen for Meet Peers]*  

While transitioning Meet Peers to the new system, we did run into a weird issue where adults would pop up at the Activity… ending up with a situation like this:  

![meet_peers_meme.jpg](https://forumcontent.paradoxplaza.com/public/955958/meet_peers_meme.jpg "meet_peers_meme.jpg")


*[How do you do fellow kids meme]*  

Fear not, for we have fixed the issue. These were often travel companions that tagged along with the kiddos in their travel plans. When characters travel, they have to be landed adults in order to receive travel events and bring along entourage members.  

We haven’t added any new event content for now… but I’m sure this Activity will play some role in our upcoming event pack, Wards & Wardens, so be on the lookout! For now, we have added Pulse Actions and the whole Activity gets the new system interface, complete with a conclusion screen and activity log.  

![meet_peers_3.png](https://forumcontent.paradoxplaza.com/public/955959/meet_peers_3.png "meet_peers_3.png")


*[Meet Peers Activity Pulse Action Example]  

![meet_peers_4.png](https://forumcontent.paradoxplaza.com/public/955960/meet_peers_4.png "meet_peers_4.png")


[Meet Peers event example]  

![meet_peers_5.png](https://forumcontent.paradoxplaza.com/public/955961/meet_peers_5.png "meet_peers_5.png")


[Meet Peers conclusion summary]*  

Beyond that, there isn’t much more to say at the moment about Meet Peers. While there isn’t much event content added to these minor Activities, I hope you can see that we have set the stage for future endeavors  

## Of Days to Come and Tales to Be Told​

This concludes our Dev Diary for today! I hope you found the venue to your liking, the decorations tasteful, and the content meaty.  
Stay tuned for next week’s exciting news on Accolades and Knights!

 

#### Attachments

- [![feast_honorary (1).jpg](https://forumcontent.paradoxplaza.com/thumbnail/public/955783/feast_honorary (1).jpg)](https://forum.paradoxplaza.com/forum/attachments/feast_honorary-1-jpg.968281/)
  
  feast_honorary (1).jpg
  754 KB

 · Views: 0

- [![feast_honorary (1).jpg](https://forumcontent.paradoxplaza.com/thumbnail/public/955784/feast_honorary (1).jpg)](https://forum.paradoxplaza.com/forum/attachments/feast_honorary-1-jpg.968282/)
  
  feast_honorary (1).jpg
  754 KB

 · Views: 0

- [![1 - invitation.jpg](https://forumcontent.paradoxplaza.com/thumbnail/public/955872/1 - invitation.jpg)](https://forum.paradoxplaza.com/forum/attachments/1-invitation-jpg.968370/)
  
  1 - invitation.jpg
  211,6 KB

 · Views: 0

- [![2 - offer_gw.jpg](https://forumcontent.paradoxplaza.com/thumbnail/public/955877/2 - offer_gw.jpg)](https://forum.paradoxplaza.com/forum/attachments/2-offer_gw-jpg.968375/)
  
  2 - offer_gw.jpg
  481 KB

 · Views: 0

- [![3 - countdown_gw.jpg](https://forumcontent.paradoxplaza.com/thumbnail/public/955878/3 - countdown_gw.jpg)](https://forum.paradoxplaza.com/forum/attachments/3-countdown_gw-jpg.968376/)
  
  3 - countdown_gw.jpg
  48,4 KB

 · Views: 0

- [![4 - betrothal_expired.jpg](https://forumcontent.paradoxplaza.com/thumbnail/public/955879/4 - betrothal_expired.jpg)](https://forum.paradoxplaza.com/forum/attachments/4-betrothal_expired-jpg.968377/)
  
  4 - betrothal_expired.jpg
  1,5 MB

 · Views: 0

- [![5 - organize_gw.jpg](https://forumcontent.paradoxplaza.com/thumbnail/public/955880/5 - organize_gw.jpg)](https://forum.paradoxplaza.com/forum/attachments/5-organize_gw-jpg.968378/)
  
  5 - organize_gw.jpg
  431,9 KB

 · Views: 0

- [![6 - setup_view.jpg](https://forumcontent.paradoxplaza.com/thumbnail/public/955881/6 - setup_view.jpg)](https://forum.paradoxplaza.com/forum/attachments/6-setup_view-jpg.968379/)
  
  6 - setup_view.jpg
  527,3 KB

 · Views: 0

- [![7 - intents.jpg](https://forumcontent.paradoxplaza.com/thumbnail/public/955882/7 - intents.jpg)](https://forum.paradoxplaza.com/forum/attachments/7-intents-jpg.968380/)
  
  7 - intents.jpg
  422,8 KB

 · Views: 0

- [![8 - options.jpg](https://forumcontent.paradoxplaza.com/thumbnail/public/955885/8 - options.jpg)](https://forum.paradoxplaza.com/forum/attachments/8-options-jpg.968383/)
  
  8 - options.jpg
  36,8 KB

 · Views: 0

- [![9 - travel.jpg](https://forumcontent.paradoxplaza.com/thumbnail/public/955886/9 - travel.jpg)](https://forum.paradoxplaza.com/forum/attachments/9-travel-jpg.968384/)
  
  9 - travel.jpg
  476,5 KB

 · Views: 0

<!-- artifact:reactions:start -->
- 119 Love
- 104 Like
- 13 (unlabeled — rendered as base64 data URI)
- 11 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Paradoksalny Kierownik](https://forum.paradoxplaza.com/forum/members/paradoksalny-kierownik.1725641/)**
Role: Corporal
Badges: 4
Messages: 27
Reaction score: 1,566

*[Full game-badge icon list of 4 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
