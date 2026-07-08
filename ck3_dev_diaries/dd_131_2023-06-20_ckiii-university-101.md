---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1590985/"
forum_thread_id: 1590985
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 131
title: "Dev Diary #131 – CKIII University 101"
dd_date: 2023-06-20
author_handle: Portable Grump
expansion: Wards and Wardens
patch: Patch 1.10
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1490
inline_image_count: 13
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1590985'
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
    location: raw_lines_~28_to_149
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_148
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2424.jpg?1687254790
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_151_to_153
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_296_to_301
    action: preserved_and_flagged
    counts:
      Like: 128
      Love: 75
      (unlabeled — rendered as base64 data URI): 5
      Haha: 2
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_309_to_390
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_391_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2424.jpg?1687254790)
<!-- artifact:thread_banner:end -->

# Dev Diary #131 – CKIII University 101

<!-- artifact:thread_metadata:start -->
- Thread starter [Portable Grump](https://forum.paradoxplaza.com/forum/members/portable-grump.1503097/)
- Start date [Jun 20, 2023](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-131-ckiii-university-101.1590985/)
<!-- artifact:thread_metadata:end -->

### Opening Remarks​

Good afternoon, and welcome to your first class of the semester! My name is Dr. Areysak, and I’ll be your “CKIII University 101” lecturer.  

I already see some raised hands. You, in the first row, ask away.  

“Why a University Activity? What does it have to do with Wards and Wardens?”  

This is a very interesting question. During the early development of Wards and Wardens, talks of hostages’ education led us to a realization: everything that could influence a character’s education trait happens during childhood. Once a character reaches 16 years of age, they are locked out of any further improvement! And if the player character isn’t directly responsible for the education of their heir, a player can find themselves inheriting an already adult heir character with an education trait they have had no way to influence.  

The University Visit activity is the solution we have chosen to open up new possibilities to the player to influence their character’s personal growth. Therefore, as a first aim, it fulfills a gameplay need; secondly, it allows us to expand upon one of the Middle Ages’ many successful inventions, Universities; thirdly, we got to add a new activity!  

When we talk of Medieval Universities, we are immediately led to think of the famous names of Western Europe, such as Oxford, Cambridge, and Bologna. The name “University”, in fact, comes from Latin and was born to describe specifically the communities (= universitates) of Latin-speaking teachers and students that congregated in these European cities. However, similar institutions existed all over the Old World. Particularly famous are the Indian “universities”, such as Takshashila and Nalanda; the House of Wisdom in Baghdad was one of the most renowned centers of studies of its age, and Madrasas schools were widespread throughout the Islamic world. In this period, it’s also often difficult to separate, as we would do today, between lay and religious centers of studies, since Christian cathedrals, Muslim mosques and, in particular, Buddhist temples were themselves libraries, scriptoria (i.e., where manuscripts were copied), and educational institutions, or had these institutions develop in their immediate vicinity.  


### The Activity​

Let’s now have a look at the activity itself, though!  

The University Visit is a minor activity that adult landed rulers can always initiate, as long as they have the gold! To keep it in line with the pre-existing decision to Go to University, it is quite expensive. To keep the challenge balanced, the final cost is dynamic (like with all activities) and changes with your tier and era.  

![image8.jpg](https://forumcontent.paradoxplaza.com/public/985752/image8.jpg "image8.jpg")


(Activity selection interface showing the University Visit)  

The activity takes 6 months, and can only be started once every 20 years, and only once per location.  

In order to Visit a University, you have to select a valid location in your diplomatic range and travel there.  

![image9.jpg](https://forumcontent.paradoxplaza.com/public/985753/image9.jpg "image9.jpg")


(Activity destination selection interface)  

You might have noticed, however, that not all valid locations are University seats. As discussed above, large religious centers were often centers of study too, and have been included as potential destinations.  

![image11.jpg](https://forumcontent.paradoxplaza.com/public/985754/image11.jpg "image11.jpg")


(The tooltip of a large religious center)  

Being a minor activity, the choice of intents and options is limited but flavorful.  
There are only two intents available, but they represent two contrasting approaches to your university experience, and will significantly change both your approach to your studies and the results you can achieve. In fact, every activity event will have at least one special option unlocked by each intent!  
“Study Hard” is quite self-explanatory: you went there to study, and study hard you will, no matter the stress cost you’ll have to pay! You try to make the most of your time at University, in order to maximize your chances of success at the end of the activity and increase your rewards.  
In fact, the results (and rewards) you obtain at the end of your studies are measured by a value called “Studiousness”, which is a “success” chance similar, e.g., to a Pilgrimage’s Piousness. The activity can’t fail per se, but the entity of your rewards will depend on this value.  

“Goliardic Lifestyle” is a completely different approach, inspired by the European Goliards, wandering students and clerics famous for their satirical poetry (for instance the Carmina Burana) exalting the art of drinking and carnal pleasures. With this intent, your aim is to gain as much first-hand experience of life, both inside and outside the walls of the University, indulging in so-called “Goliardic Shenanigans”. I’ll leave you the pleasure of discovering exactly what your character can get up to; the general idea of the intent, however, is to gain less success chance (and therefore less rewards at the conclusion of the activity), but more immediate bonuses such as lifestyle traits, lifestyle xp, and skill points.  

![image2.jpg](https://forumcontent.paradoxplaza.com/public/985755/image2.jpg "image2.jpg")


(Intents view)  

On the other hand, we only have one option with 3 levels, which represent how much money you plan to invest in study materials. The option chosen will influence your success chance and final rewards, including an Illustrious artifact! (cost values are still wip)  

![image13.jpg](https://forumcontent.paradoxplaza.com/public/985760/image13.jpg "image13.jpg")


(Options view)  

![image4.jpg](https://forumcontent.paradoxplaza.com/public/985761/image4.jpg "image4.jpg")


(Arrival event)  

As you can see, your level of Studiousness is easily traceable from the activity view. To make the interactions more impactful, we have limited the number of guests, which are only a handful of students and teachers, which will be among the wisest minds on the map!  

![image6.jpg](https://forumcontent.paradoxplaza.com/public/985762/image6.jpg "image6.jpg")


(Activity view and teacher’s character view)  

![image7.jpg](https://forumcontent.paradoxplaza.com/public/985763/image7.jpg "image7.jpg")


(Event with Study Hard option)  

![image12.jpg](https://forumcontent.paradoxplaza.com/public/985764/image12.jpg "image12.jpg")


(Event with Goliardic Lifestyle options)  

Be ready to gain a whole bunch of stress! Nobody said that getting a degree was easy…  

I did mention that your teachers will be among the most brilliant minds around, and I’d like to stress it again because if you manage to make a very good impression on them…  

![image3.jpg](https://forumcontent.paradoxplaza.com/public/985765/image3.jpg "image3.jpg")


(Conclusion event)  

You will be able to invite one of them to move back to your court with you!  

But hold on, there is something weird with this teacher… What is that?!  

![image10.jpg](https://forumcontent.paradoxplaza.com/public/985766/image10.jpg "image10.jpg")


(Teacher’s character view with education trait tooltip)  

Is that… A fifth level of the Education Trait?!  

YES!  

Concurrently with the University Visit activity, we have added a new level to all education traits. This final level will be super rare, and mostly reserved for University teachers and University graduates who already started with the fourth-tier trait.  


### Rewards​

As you might have guessed from what has been discussed so far, the main reward for the activity is increasing your education trait one level up. However, there is only a chance to succeed in this endeavor! This chance is higher the lower you current level is (i.e., it’s easier to get from tier 1 to 2 than it is from 2 to 3) and the higher your Studiousness level is.  

![image1.jpg](https://forumcontent.paradoxplaza.com/public/985768/image1.jpg "image1.jpg")


(Tooltip of Tier 4 of Studiousness with the rewards)  

However, even if you were to fail at improving your education, you are ensured to gain a number of Perk points that increases with your achieved Studiousness, an assortment of xp and skill points depending on your event choices, and even an Illustrious book if you chose the most expensive option during the activity setup (and therefore went splurging on rare manuscripts)!  

![image5.jpg](https://forumcontent.paradoxplaza.com/public/985769/image5.jpg "image5.jpg")


(A randomly generated Illustrious book)  


### Conclusions​

This concludes today’s lecture. I hear some buzzing from the end rows, are there any questions?  

“But that’s not how Universities worked! No ruler would go to University like a commoner!!”  

You are, of course, correct. We are perfectly aware of it. However, we believe that the combined bonuses offered by new gameplay possibilities (i.e., improving your character’s education and skills) and the historical flavor of showing a slice of the life at Medieval Universities more than warranted the exception!  

I hope you are excited to Visit a University soon!  

This is the last Dev Diary before the July break, so it seems fitting to just say:  

School’s out! Have a nice summer! And see you all back in August!

<!-- artifact:reactions:start -->
- 128 Like
- 75 Love
- 11 (unlabeled — rendered as base64 data URI)
- 10 (unlabeled — rendered as base64 data URI)
- 5 (unlabeled — rendered as base64 data URI)
- 2 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Portable Grump](https://forum.paradoxplaza.com/forum/members/portable-grump.1503097/)**
Role: ♛ CK3 Community Team ♛
Badges: 18
Messages: 276
Reaction score: 1,620

*[Full game-badge icon list of 19 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
