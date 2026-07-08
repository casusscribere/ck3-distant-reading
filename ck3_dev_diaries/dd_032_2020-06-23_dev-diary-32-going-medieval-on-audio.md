---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1401422/"
forum_thread_id: 1401422
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 32
title: "CK3 Dev Diary #32 - Going Medieval on Audio"
dd_date: 2020-06-23
author_handle: Metal King
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1687
inline_image_count: 3
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1401422'
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
    location: raw_lines_~28_to_148
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_147
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1413.jpg?1592907164
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_150_to_152
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_289_to_293
    action: preserved_and_flagged
    counts:
      Love: 182
      Like: 94
      (unlabeled — rendered as base64 data URI): 3
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_301_to_411
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_412_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1413.jpg?1592907164)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #32 - Going Medieval on Audio

<!-- artifact:thread_metadata:start -->
- Thread starter [Metal King](https://forum.paradoxplaza.com/forum/members/metal-king.1027995/)
- Start date [Jun 23, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-32-going-medieval-on-audio.1401422/)
<!-- artifact:thread_metadata:end -->

**Intro**  

Hey! My name is Björn Iversen and I worked as Audio Director on Crusader Kings 3. Finally, I get this opportunity to write a Dev Diary about what the audio team has been working on for a long time!  

We will split up this Dev Diary into different parts: first off, I want to tell a little bit about the Audio Vision and what my ambitions were for game audio. Then we will talk about Sound Design, what is new and improved from previous games, and of course, last but not least, the Soundtrack.  

**Audio Vi****sion**  

To start with a short backstory, it is quite a daunting task to work with the audio for Crusader Kings 3, since CK2 had so many years of development that included some of our most iconic soundtracks which are loved by the community. Later down the line we also started to add more Sound Design to the game which some of the community has appreciated a lot.  

So initially the big question was: What is needed to be improved for the sequel? What do we want to keep from the previous game? What brand new audio features do we want to introduce?  

The first and biggest step up we wanted to do in Crusader Kings III was to have Audio looped in as early in development as possible. CK2 was developed before my time as Audio Director and during those days the studio did not have any dedicated Sound Designers that helped out with the game audio.  

First, Andreas Waldetoft (Our in-house Composer and close co-worker) and I could in the early stages of design work on what we wanted to do with the Soundtrack. Then I could also establish an Audio Vision for the Sound Design already at this stage. This would be helpful when my first Sound Designer, Gustav aka ParadoxGustav, would onboard the project to help out with Sound Design. This meant that we could work more on certain aspects that I felt were a bit lackluster in the Crusader Kings II, and the three main pillars for me were:  

**Storytelling**  
Since the game is about the characters, their actions, and the tales that are created, it was my ambition to bring all events and character actions more into life with the help of audio. As an example, we have added sound effects to the event backgrounds to enhance the immersion of the event, for instance, if it takes place in a Courtyard it should sound like it.  

My goal is that it’s not only the Sound Design that should enhance the immersion of the storytelling, but also have the Music to help with that. A bit more about Music later in the diary.  

**The Map should feel alive**  
I always felt that it was a bit under-developed in the previous title, and since we have created such a beautiful map, it was important for me and the audio team that the map would sound great also. If you zoom in to an area of the map with a lot of rivers and forests, it should sound like it is alive. The same goes with holdings, they should sound populated based on the type and culture.  

**A more calm soundscape**  
Now, this might sound a bit too abstract, but hear me out! One of the main issues with the previous title was also how, unfortunately, every single audio and music asset wanted to play loud and all at the same time. Another one of our main goals was to have a much better soundscape in which no sound effects are competing with each other too much for a place in the mix, and that the music isn’t too intrusive for the player experience. Basically, we wanted the game to sound more “calm” which is more pleasing to the ears after long gaming sessions.  

But enough writing about our goals, let’s show off some of the cool stuff we have been working on with some video footage!  

**Sound Design**  

**Event Windows**  

So, the Event Windows have two elements of sound effects. The first one is an “Event Theme” as we call them, and there are different ones depending on the event. Also then, Art made these beautiful backgrounds for the Events, so we wanted to enhance them by adding ambience sound. Here is an example of Marriage Event with those two elements:  


[https://www.youtube.com/embed/b_xXohZvPQ4?wmode=opaque](https://www.youtube.com/embed/b_xXohZvPQ4?wmode=opaque)


If you listen carefully in the video you will hear a subtle feature, once the Event Window is on-screen, the map ambience is lowered in volume to add focus to the event so it’s more invoking to read and get immersed in the story.  

And to add some extra flavor for the Events, sometimes the Music will also change when it appears. Here is a video with just the Music and the same Event for an example:  


[https://www.youtube.com/embed/31nXYMItkZA?wmode=opaque](https://www.youtube.com/embed/31nXYMItkZA?wmode=opaque)


Once all the pieces are put together you will get this result:  


[https://www.youtube.com/embed/wjzg7w4Jl9g?wmode=opaque](https://www.youtube.com/embed/wjzg7w4Jl9g?wmode=opaque)


I think this is the right approach to enhance the storytelling element of our games that happens through Event Windows.  

Since this worked really well with Event Windows we wanted to combine both SFX & Music for other instances in the game such as declaring war;  


[https://www.youtube.com/embed/mJBOzlKnpps?wmode=opaque](https://www.youtube.com/embed/mJBOzlKnpps?wmode=opaque)


**Ambience**  

As I mentioned before it was important that the map would sound more alive, and that it would sound different based on nature & holdings, which the team has succeeded in creating! Instead of writing so much about it, I would love to give some examples instead:  

Ambience over England here you can hear the different Holdings and Nature ambience:  


[https://www.youtube.com/embed/AZYea8RteyY?wmode=opaque](https://www.youtube.com/embed/AZYea8RteyY?wmode=opaque)


A personal favorite place on the map for listening to the ambience! I like the details of the river and holdings in this part.  


[https://www.youtube.com/embed/1qD7cNrWZwQ?wmode=opaque](https://www.youtube.com/embed/1qD7cNrWZwQ?wmode=opaque)


As a third example we hover over India and listen to Dharmic Holdings:  


[https://www.youtube.com/embed/uN0noufpL6Q?wmode=opaque](https://www.youtube.com/embed/uN0noufpL6Q?wmode=opaque)


**Music**  

Hi, my name is Andreas Waldetoft aka Jazzhole on this forum, and I'm the Senior Composer here at Paradox. I have worked on most of our internal games throughout the years and have had the pleasure to work on Crusader Kings III as well.  

As I composed CK2 back in the days we did not have to completely start from scratch with some of the more recognizable themes. We however wanted a soundtrack that would have much more depth in the sort of sounds one can expect to hear. For example, we have recorded many different medieval instruments, examples are Bagpipes, Hurdy-gurdy, Keyed fiddles, stringed instruments, and many different percussion instruments… to name a few. We also used a full orchestra, solo vocalists, and church choirs.  

![pic01.jpg](https://forumcontent.paradoxplaza.com/public/580577/pic01.jpg "pic01.jpg")


![pic02.jpg](https://forumcontent.paradoxplaza.com/public/580578/pic02.jpg "pic02.jpg")


![pic03.jpg](https://forumcontent.paradoxplaza.com/public/580579/pic03.jpg "pic03.jpg")



Björn has already talked about the use of cue tracks for events and storytelling, which is something we talked about right from the design phase a few years ago. Therefore we have cue-tracks and mood music as a kind of a cornerstone of the soundtrack.  
The cue-tracks are often shorter pieces of music that reacts to events happening in the game.  
Mood tracks are music that as the name implies, is meant to give a more calm moody experience that is pleasing to listen to for long hours.  
Here is an example of a cue I did for an event called “The Crusade Starts”, it is from the Orchestral Session we had in Budapest.  


[https://www.youtube.com/embed/4N9_hxy26Ok?wmode=opaque](https://www.youtube.com/embed/4N9_hxy26Ok?wmode=opaque)


I also did a few orchestral suites for the game to be used as main themes, this excerpt is from a piece called “Knights of Jerusalem” and is once again at the Budapest Scoring Orchestra recording session.  

[https://www.youtube.com/embed/SJc3qvqgfj8?wmode=opaque](https://www.youtube.com/embed/SJc3qvqgfj8?wmode=opaque)


Crusader Kings III has more music than any vanilla strategy game we have developed, so my good friend Philip Wareborn stepped in to help me compose music tracks for different situations in this game. You might have heard his music in the Stellaris: 4th Anniversary trailer which he helped compose.  

That is it about the music, I’m really looking forward to hearing your thoughts once it is released.  

[https://www.youtube.com/embed/sfTDcrTouzg?wmode=opaque](https://www.youtube.com/embed/sfTDcrTouzg?wmode=opaque)



**Modding**  
There will be more updates regarding this in the future, but I will touch briefly on this topic now since I know that the community will ask about it… and yes, there is some modding support! There will be possibilities to change out the assets for Mood Tracks and Cue Tracks. It will also be possible to add more tracks as well.  

This will be short and sweet for now, since I’ll probably need to create a forum post on how to mod the music but that will happen after release.  

But here below is a video showcasing how I switch out “Declare War” Cue Track to another song from Stellaris.  

[https://www.youtube.com/embed/JEbxR9zTBuQ?wmode=opaque](https://www.youtube.com/embed/JEbxR9zTBuQ?wmode=opaque)


So with that, it's time for me to wrap up this Dev Diary. I hope that you all got as excited as we are for you to hear the soundscape we have worked hard on for a long time.

<!-- artifact:reactions:start -->
- 182 Love
- 94 Like
- 16 (unlabeled — rendered as base64 data URI)
- 13 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Metal King](https://forum.paradoxplaza.com/forum/members/metal-king.1027995/)**
Role: Audio Director
Badges: 6
Messages: 143
Reaction score: 2,252

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
