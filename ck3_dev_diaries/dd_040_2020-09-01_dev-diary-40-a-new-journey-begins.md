---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1414653/"
forum_thread_id: 1414653
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 40
title: "CK3 Dev Diary #40 - A new journey begins"
dd_date: 2020-09-01
author_handle: Fogbound
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1189
inline_image_count: 36
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1414653'
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
    location: raw_lines_~28_to_150
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_149
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1446.jpg?1598963453
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_152_to_154
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_324_to_329
    action: preserved_and_flagged
    counts:
      Like: 183
      Love: 126
      Haha: 30
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_337_to_421
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_422_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1446.jpg?1598963453)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #40 - A new journey begins

<!-- artifact:thread_metadata:start -->
- Thread starter [Fogbound](https://forum.paradoxplaza.com/forum/members/fogbound.1203045/)
- Start date [Sep 1, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-40-a-new-journey-begins.1414653/)
<!-- artifact:thread_metadata:end -->

Greetings and Salutations everyone!  

I am Linda Tiger (aka Fogbound), resident Senior Producer on Crusader Kings III.  
I usually cruise ‘behind the scenes’ to support the team, but today is a rather special day, as you might know.  
In just a few hours from now, we release our labor of love to the world, and you can experience first hand what this amazing development team has been up to for quite some time.  

We have been sharing insights to our game features since we announced back in October last year, so today won’t be about the game - but rather the people behind it from over the years, both past and present.  

Making something is hard. Without a design, it’s impossible. Following up on something so loved and enjoyed as Crusader Kings II was never going to be easy, but with Game Director **Henrik Fåhraeus** at the steering wheel we had a clear vision and goal from the start.  
Lead Designer **Alexander Oltner** has made sure we’ve always had straightforward designs to work with, assisted by Game Designers **Emil Tisander** and **Joakim Andreasson**.  

We wanted to make sure to pave the way for a player focused experience, and creative UX Designers **Jonas Wickerström** & **Peter Johannesson** have been instrumental in driving this work.  

And to make sure that every turn taken and choice made makes a difference, our fantastic team of Content Designers **Linnéa Thimrén, Sean ‘Shoes’ Hughes, Ewan Cowhig Croft, Bianca Savazzi, Mathilda Bjarnehed, Petter Vilberg and Camilla Isaksson** have tirelessly continued to build immersion with the assistance of Content Design Lead **Maximilian Olbers**.  

It takes quite a crew to keep a motor like this running; from architecture and core systems, to making sure that all the different pieces fit nicely together. Tech Leads **Olof Björk, Lysann Schlegel and Joel Hansson** has made sure our talented team of Programmers **Igor Aleksandrowicz, Niklas Strid, Magne Skjæran, Anton Sorokin, Matthew Clohessy, Amanch Esmailzadeh, Ismael Serrano, Jimmy Selling and Daniel Eriksson** have kept their code clean and their cogwheels spinning.  

But it’s not only under-the-hood stuff that matters - making things look great and put things in motion is equally important! Thanks to the skillful work of our Artists **Petter Lundh, Malin Jonsson, Carlos Lundhall, Nils Wadensten, Nikolaos Kaltsogiannis, Anton Leirnes, David Horler, Erik Hammarbäck, Johan Lundqvist, Fabian Soon, Niklas Tammpere, Erik Forsström, Ahmed Albastaki, Ecbel Oueslati, Mattias Larsson, Oscar Sjöstedt and Noelia Skabar** we can offer a visually appealing joyride - all with the help and support of of our Art Producer **Philipp Glietsch**, our Art Lead **Joacim Carlberg** and Art Directors **Pontus Olofsson** & **Fredrik Toll**.  

We are also proud to offer a bombastic audio experience, with music by legendary Music Composer and Producer **Andreas Waldetoft**, and solid soundscapes by Audio Designers **Gustav Landerholm & Franco Freda** - all in tune with Audio Director **Björn Iversen** and ready to be cranked up!  

Talking the talk is all fine and dandy when you know the language, and thanks to our eminent Localization Manager **Sara Wendel-Örtqvist** we can speak up in several languages.  

Creating all these parts might be a distributed effort, but making sure they all come together, stay together (even when the road is long and bumpy) and continues to be a fun filled experience requires a special kind of attention. Our relentless team of QA Testers **Matt Frary, Jakub Potapczyk, Karl Cederslätt, Nicholas Meredith, Andreas Olsson, Alexander Windahl, Anna Johansson, Katya Boestad & Niall Bird**.  

And to round things up, I wouldn’t have gotten to this Release Day without the excellent help of my co-Producers **Carmille Gidfors and Tegan Harris**; navigating maps, greasing machinery, identifying dropped parts and lifting roadblocks left, right and center, to make sure our team gets to the right destination.  

Of course, there are many more supporters at various depots - both internal and external - who have helped in getting us to where we are today. And with a development that spans over a longer period like this one, the team will naturally change significantly over time. The people above have worked in the development team at some point past or present. But named or not, you have our eternal gratitude.  
And there is of course You. Our players, our fans, keeping us motivated to get this show on the road. We really hope you will enjoy the ride <3  

![image4.png](https://forumcontent.paradoxplaza.com/public/602504/image4.png "image4.png")


*CK3 Team Christmas Card 2019*  

PS1) You might run into some of these characters - can you guess who’s who?  

![image1.png](https://forumcontent.paradoxplaza.com/public/602505/image1.png "image1.png")



![image2.png](https://forumcontent.paradoxplaza.com/public/602506/image2.png "image2.png")



![image3.png](https://forumcontent.paradoxplaza.com/public/602507/image3.png "image3.png")



![image5.png](https://forumcontent.paradoxplaza.com/public/602508/image5.png "image5.png")



![image6.png](https://forumcontent.paradoxplaza.com/public/602509/image6.png "image6.png")



![image7.png](https://forumcontent.paradoxplaza.com/public/602510/image7.png "image7.png")



![image8.png](https://forumcontent.paradoxplaza.com/public/602511/image8.png "image8.png")



![image9.png](https://forumcontent.paradoxplaza.com/public/602512/image9.png "image9.png")

![image10.png](https://forumcontent.paradoxplaza.com/public/602513/image10.png "image10.png")



![image11.png](https://forumcontent.paradoxplaza.com/public/602514/image11.png "image11.png")



![image12.png](https://forumcontent.paradoxplaza.com/public/602515/image12.png "image12.png")



![image13.png](https://forumcontent.paradoxplaza.com/public/602516/image13.png "image13.png")


![image14.png](https://forumcontent.paradoxplaza.com/public/602517/image14.png "image14.png")



![image15.png](https://forumcontent.paradoxplaza.com/public/602518/image15.png "image15.png")



![image16.png](https://forumcontent.paradoxplaza.com/public/602519/image16.png "image16.png")



![image17.png](https://forumcontent.paradoxplaza.com/public/602520/image17.png "image17.png")

![image18.png](https://forumcontent.paradoxplaza.com/public/602521/image18.png "image18.png")



![image19.png](https://forumcontent.paradoxplaza.com/public/602522/image19.png "image19.png")


![image20.png](https://forumcontent.paradoxplaza.com/public/602523/image20.png "image20.png")



![image21.png](https://forumcontent.paradoxplaza.com/public/602524/image21.png "image21.png")

![image22.png](https://forumcontent.paradoxplaza.com/public/602525/image22.png "image22.png")


![image23.png](https://forumcontent.paradoxplaza.com/public/602526/image23.png "image23.png")



![image24.png](https://forumcontent.paradoxplaza.com/public/602527/image24.png "image24.png")



![image25.png](https://forumcontent.paradoxplaza.com/public/602528/image25.png "image25.png")


![image26.png](https://forumcontent.paradoxplaza.com/public/602529/image26.png "image26.png")



![image27.png](https://forumcontent.paradoxplaza.com/public/602530/image27.png "image27.png")



![image28.png](https://forumcontent.paradoxplaza.com/public/602531/image28.png "image28.png")



![image29.png](https://forumcontent.paradoxplaza.com/public/602532/image29.png "image29.png")

![image30.png](https://forumcontent.paradoxplaza.com/public/602533/image30.png "image30.png")



![image31.png](https://forumcontent.paradoxplaza.com/public/602534/image31.png "image31.png")



![image32.png](https://forumcontent.paradoxplaza.com/public/602535/image32.png "image32.png")



![image33.png](https://forumcontent.paradoxplaza.com/public/602536/image33.png "image33.png")

![image34.png](https://forumcontent.paradoxplaza.com/public/602537/image34.png "image34.png")



![image35.png](https://forumcontent.paradoxplaza.com/public/602538/image35.png "image35.png")



![image36.png](https://forumcontent.paradoxplaza.com/public/602539/image36.png "image36.png")



PS2) And lastly for the release patch notes!  1.0:  
- Made game

<!-- artifact:reactions:start -->
- 183 Like
- 126 Love
- 30 Haha
- 5 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Fogbound](https://forum.paradoxplaza.com/forum/members/fogbound.1203045/)**
Role: Recruit
Badges: 26
Messages: 9
Reaction score: 454

*[Full game-badge icon list of 26 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
