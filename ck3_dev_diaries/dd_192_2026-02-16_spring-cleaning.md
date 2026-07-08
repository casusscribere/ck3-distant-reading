---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1902372/"
forum_thread_id: 1902372
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 192
title: "Dev Diary #192 - Spring Cleaning"
dd_date: 2026-02-16
author_handle: Arakrates
expansion: All Under Heaven
patch: null
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 3143
inline_image_count: 12
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1902372'
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
    location: raw_lines_~28_to_143
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_145_to_147
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_421_to_426
    action: preserved_and_flagged
    counts:
      Like: 124
      Love: 59
      (unlabeled — rendered as base64 data URI): 1
      Haha: 3
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_434_to_544
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_545_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Dev Diary #192 - Spring Cleaning

<!-- artifact:thread_metadata:start -->
- Thread starter [Arakrates](https://forum.paradoxplaza.com/forum/members/arakrates.1605676/)
- Start date [Feb 16, 2026](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-192-spring-cleaning.1902372/)
<!-- artifact:thread_metadata:end -->

Spring Cleaning, Our Vision  
Heya y’all! My name is Riad. You may know me as the QA guy who sometimes posts on Reddit, or the guy who showed off the [Black Forge Jam projects](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-182-black-forge-jam-2024.1857719/) last year… or, more recently, the guy who wrote [that apology](https://forum.paradoxplaza.com/forum/threads/update-1-17-0-1-a-long-overdue-apology.1858561/). Yeah.  

Since then, a lot has happened for us at Studio Black. We released our biggest expansion ever, **All Under Heaven**, which added many long-missing parts of the world to Crusader Kings III and, at last, completed what we consider to be the full map of the game.  

We were genuinely blown away by the response from the community after release, both in terms of enthusiasm and the sheer volume of feedback we received. Even more importantly, we were able to act on a lot of that feedback during the post-release period. Once the dust settled, we immediately started spinning up our next projects. While we’re not quite ready to talk about those just yet, I promise you we’ll have more news in the near future.  

If you’re interested in a more in-depth summary of 2025, I highly recommend reading Alexander Oltner’s, our Game Director’s, [end-of-year address to the community](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-191-2025-in-review.1888979/).  

Today, however, I’m not here to talk about anything that’s part of the next chapter. Instead, I want to talk about something else. Something that, in my opinion, is even more important—  

**Game Health**.  

---

### Our Mission​


As we entered the new year, we took the opportunity to reaffirm our commitment: ensuring that Crusader Kings III remains not only fun, but also a stable experience. That means continuing to address long-standing issues, delivering frequently requested quality-of-life improvements, and making sure the game respects your time.  

A bold concept, I know.  

In my view, there’s a clear opportunity for us to share more about how we work and how our development process unfolds. That’s something I’m actively exploring so we can open up more going forward. We may be able to draw inspiration from how our colleagues in sunny Spain approached Tinto Talks in the lead-up to the release of Europa Universalis 5.  

Now again, they have the benefit of not suffering from Vitamin-D deficiency due to the cold dark nights of Sweden – I am not joking, as I am writing this, I received a letter from my doctor with the test results… Donde esta la biblioteca — I’ll be booking my flight to Barcelona soon!  

![image_01.png](https://forumcontent.paradoxplaza.com/public/1456014/image_01.png "image_01.png")


*[I was not joking.]*  

Another major focus for us is better support for modders, both current and future. One concrete area I am exploring together with our Art Director @plundh (he’s weirdly into this stuff), is improving the documentation for many of our script systems, making it easier for people to play and mod the game the way they want to.  

We remain committed to also bringing some meaningful changes that you, the player, will notice. Game wise, I wanted to start out the year with a bang, tackling the community’s requests head-on with some much needed changes.  

---

#### The Q2 Update​


One of the player-facing efforts I’m leading this year is our next major update, currently planned for release at the beginning of Q2. This update is focused on two main things: tackling bugs that have been haunting our backlog, and introducing a set of changes and smaller features that we believe will meaningfully enhance the CK3 experience.  

I don’t have a cool name for it yet. I promise I’ll come up with something suitably dramatic by the time we release the changelog. Until then, I’ll refer to it the same way we do internally: **the Q2 update**. Inspiring, I know.  

Today’s diary won’t cover every detail — the full specifics will come closer to release. The team is still deep in development, and I’d rather keep the focus on quality than on polishing slides.  

![image_02.png](https://forumcontent.paradoxplaza.com/public/1456015/image_02.png "image_02.png")


*[This is a slide from our kickoff meeting earlier in January outlining some of the major changes we have planned. I had to censor some parts.]*  

Instead, I want to outline the vision behind the update and highlight two features where your feedback will be especially valuable.  
Let’s kick it off!  


---

### Our Vision​

### Accolades Revamp​


One of the revamps I’m particularly excited to talk about is the work being done on the Accolades system. We originally released Accolades as part of **Tours and Tournaments** back in May 2023. Since then, we’ve received a… lot… of feedback, both from all of you (and internally).  

We saw a lot of potential with this system, and we’ve always wanted to revisit it in the future to do it justice. Now, we never expected that revisit to happen almost three years later. But here we are. Better late than never!  

One of the primary changes to Accolades is an overhaul of Succession. Previously, when an Acclaimed Knight left for any reason (see: death), the ruler had to have a designated successor in place, or manually set about securing one. This created a lot of maintenance overhead for the player and could quickly become frustrating, especially if you were managing multiple Acclaimed Knights.  

This Succession system has been replaced by our new, hands-free **Squires** system.  

![image_03.png](https://forumcontent.paradoxplaza.com/public/1456016/image_03.png "image_03.png")


*[I take care of my squires]*  

Each Accolade now has a Squires stat that informs you about the potential of its future successor. This stat directly influences the traits and Prowess of the next Acclaimed Knight when they take over. Positively… or perhaps slightly less positively.  

Squires have five aptitude levels:  


- Accomplished
- Capable
- Inexperienced
- Feckless
- Pathetic

The obvious question: how do you improve Squires aptitude? Simple. **Have your Acclaimed Knight actually do their job**.  

Glory, the “experience” a knight gains over time, is the primary driver of Squire aptitude. Other influences include the Acclaimed Knight’s own skills, particularly Prowess and Martial, your relevant skills as their liege, and experience in leveled traits such as Hastiluder and Aspiring Blademaster.  

Succession now works as follows:  


1. First, your current knight dies. Tragic.
2. A new appropriate Acclaimed Knight is either selected from your court or generated and added to your knight roster. This new knight is then buffed or debuffed based on the Squires aptitude level. Once installed, the Squires stat resets, and the new knight’s glorious career begins.

You are, of course, informed via messages. But beyond that, absolutely zero human micromanagement is required.  

![image_04.png](https://forumcontent.paradoxplaza.com/public/1456017/image_04.png "image_04.png")


*[Not so fine now are ye’]*  

Another major focus of the rework was increasing your agency over Accolade Attributes. Upon creation, Accolades now begin with only one Attribute, retaining the existing three ranks of tiered bonuses.  

![image_05.png](https://forumcontent.paradoxplaza.com/public/1456018/image_05.png "image_05.png")


*[Gee Bill! How Come Your Mom Lets You Have Two Attributes!]*  

When your Accolade gains enough Glory to level up, you, as the Liege, can choose to either rank up an existing Attribute or add a new one. Accolades can now have up to three Attributes in total.  

With Men-at-Arms unlocks moved to second-tier rewards, you have far more flexibility in how you mix and match Attributes. This change reinforces the feeling that your Accolade is evolving over time, gathering more prestige and potency.  

![image_06.png](https://forumcontent.paradoxplaza.com/public/1456019/image_06.png "image_06.png")


*[I know he looks a bit daft, but he tries his best ok?]*  

We’ve also added new unlock requirements to most of the 29 or so Attributes. The goal here is to make Attributes something you actively pursue, rather than passively hope for.  

Attribute requirements are now visible in the Accolade window. Instead of opaque triggers like *“the knight must have the Besieger trait”*, you’ll now see gameplay-driven goals such as: *“The knight must participate in 8+ sieges.”*  

This means you can deliberately shape your knight’s career to unlock the Attributes you want. Less mystery. More intentional development.  

![image_07.png](https://forumcontent.paradoxplaza.com/public/1456020/image_07.png "image_07.png")



Now, I know what you’re thinking. “This sounds cool, but why would I ever take my Acclaimed Knight into battle? They’ll just get pounded on, die, and I’ll lose all my hard work.”  

Good news. **Acclaimed Knights are now significantly less likely to be captured or killed in battle**. You no longer have to protect them like priceless porcelain figurines.  

**And if they do die in battle, in a duel, or in any other suitably dramatic warrior’s death, the Accolade loses no Glory upon Succession**.  

Also as a side note: Naming Accolades is as fun as ever. I regret none of my choices.  

![image_08.png](https://forumcontent.paradoxplaza.com/public/1456021/image_08.png "image_08.png")


*[Make the Öresund Bridge One-Way Only!]*  

On top of all that, the UI has received a proper art pass and now looks significantly better. Especially the icons, which are finally nice and crispy instead of the low-resolution exports we somehow lived with for far too long.  

To clarify, I didn’t work on this system directly myself. Instead, the effort was carried out by a group of very dedicated developers, led by Jason: a designer on my team I am super proud of. The team has worked incredibly hard on this revamp, and we genuinely hope you’ll enjoy these changes.  

---

### Working Directly With the Community​


It should come as no surprise that we at Paradox believe our modding community is the lifeblood of our games. Whenever we build systems for Crusader Kings III, we try to ensure they’re scalable and accessible so modders can create tailored experiences for players.  

Over the years, we’ve seen incredible mods ranging from great quality-of-life improvements (many of which inspired our work!), to community bug-fixing efforts, to massive total conversions that recreate entire worlds inside our game.  

During the development of **All Under Heaven**, we worked very closely with the community. Through that process, it became even clearer to me just how important early involvement is. For this update in particular, I wanted to involve the community more directly, because frankly, no one knows better what you want, than you do.  

Over the years, we’ve found ways to collaborate with modders as a way of giving back. This led to our Creator Pack program, including recent releases like **High Medieval Warfare Attire** and **Holy Buildings**.  

But that got me thinking: what if, instead of just content, we involved creators directly in improving the game itself?  

That led me to reach out to our mysterious benefactor, a modder you may know as the creator of █████ █████ and ████████. Much of their work had already inspired us internally and influenced changes we’d made to the game.  
When I reached out, instead of assigning a predefined task, I asked a simple question: what would *you* like to work on?  

They came back with a list so large it genuinely shocked the team. Some of it overlapped with things already in our pipeline, but a lot of it made us collectively ask, “How did we not think of this?”  

![image_09.png](https://forumcontent.paradoxplaza.com/public/1456022/image_09.png "image_09.png")


*[There’s over 60 entries in this bad boy]*  

After a lot of discussion and some very realistic scoping, we landed on a handful of features that felt like a good place to start this collaboration.  

While I’ll let them properly introduce their work in a future dev diary, there’s one feature I couldn’t wait to show off.  

**Introducing: the Ledger**.  

Now, to be clear, this is still very much work in progress. The final version may behave differently after testing, and it will definitely look different once it’s gone through a proper art pass. But even in its current state, I’m extremely excited about what it brings to the table.  

![image_10.png](https://forumcontent.paradoxplaza.com/public/1456023/image_10.png "image_10.png")


*[Now you can actually find out if you’re the best in the world]*  

Now you can fool your boss into thinking you’re reading columns of [ENTER FAVORITE SPREADSHEET PROGRAM], while you’re actually playing Crusader Kings III during work time. It’s a win-win.  

At a high level, the Ledger provides a set of tabs that let players explore and overview different aspects of the world. Like our other systems, we are excited to see what additional tabs players might come up with! Hell, who knows, we might even add more ourselves post-release.  

Each tab also comes with a bunch of filters that allow you to get the exact data you want.  

![image_11.png](https://forumcontent.paradoxplaza.com/public/1456024/image_11.png "image_11.png")


*[Coincidentally, it’s been pretty useful for finding bugs]*  

Some of the confirmed initial tabs include:  


- Artifacts
- Characters
- Ongoing Wars
- Houses
No longer will you have to click through thousands of characters just to find out what artifacts exist in the world. Everything is right there, one click away. And you can favorite them, to keep interesting things in the ledger. Modern technology is truly incredible.  

![image_12.png](https://forumcontent.paradoxplaza.com/public/1456025/image_12.png "image_12.png")


*[This belongs in a museum!]*  

We’re also exploring additional tabs, though some may arrive in a future update if time doesn’t allow:  


- Counties
- Titles
- Holdings
- Faith / Religion
- Cultures

Let us know in the comments which of these you’re most excited about, so we can focus our efforts where they matter most.  

This is just one of several things █████ will be working on with us. In a future dev diary, I’ll let them introduce themselves properly and walk you through their work in more detail. Please look forward to it.  

---

### Spring Cleaning​


Lastly, one of the areas that we are focusing on, as previously mentioned, is to tackle our bug backlog. With the help of our community team, we have been scouring our platforms for issues in order to create a clearer picture of what common issues people are having that we still haven’t addressed.  

We are hard at work tackling this list, and we hope that the update will relieve some of the issues you’ve experienced in your game. If there are any bugs you want to make sure we don’t miss, don’t worry, there is an opportunity to let us know directly.  

I want to try one more thing we’ve never done before. I saw what our sister studio on **Victoria 3** did with their [GDFIX Day](https://forum.paradoxplaza.com/forum/threads/gdfix-day-is-approaching.1858550/), and I immediately shuffled over to [@PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/1654099/), our Community Manager, and said, with the confidence of someone who was never told “no” as a child, *“You see this? I want this.”*  

So, this Thursday, we’ll be hosting our first-ever **Community Fix Day**, where you’ll be able to submit bugs and see* them fixed LIVE, with developers interacting directly in cyberspace (Discord). It’s amazing what technology allows us to do these days.  ** Disclaimer, you won’t actually see developers working on bugs live, that would surely be a violation of their privacy, and some worker laws here in Sweden I am sure.*  

There will be more news about that in a separate post, which Trinexx will follow up with.  

So, what are you expected to pay for all the things we’re working on in this update?  

Nothing. Nada. Zilch. It’s completely free. As in money.  

This update is part of our commitment to improving the long-term health of Crusader Kings III. We play the game too. We run into the same bugs, the same frustrations, the same “why does it do that?” moments. We want the game to be the best version of itself just as much as you do.  

At the same time, it’s worth saying this clearly: the reason we’re able to continue supporting Crusader Kings III six years after release is because you continue to support it. Whether that’s through Chapters, Content Creator Packs, or other individual DLC, that support is what allows us to keep investing in major free updates like this one.  

So this update will be available to all owners of Crusader Kings III on release day. No extra purchase required.  


---

### Our Commitment​


What I’ve shown here is only a slice of what we have planned for the Q2 update. As mentioned earlier, a significant part of this update is focused on bug fixes and tweaks that we hope will lead to a better overall experience for everyone.  
We hope this update will stave off your hunger until we’re ready to reveal all the exciting things planned for our future chapter. We promise more information is coming!  

I want you to see this dev diary not just as another attempt to market upcoming features (I mean, it partly is), but also as a commitment from us at Studio Black. Since being appointed to helm the design team, [@lachek](https://forum.paradoxplaza.com/forum/members/669315/) and I are incredibly excited to work with the rest of the development team to ensure Crusader Kings III lives up to its name and your expectations.  

As part of this effort, we’re also going to try something we very rarely do: **run an Open Beta for the update**.  
This is not something we’ve historically relied on for Crusader Kings III, but we see it as an interesting tool that could help us refine the experience before full release. It gives us the opportunity to gather broader feedback, identify edge cases, and stress-test changes in ways that simply aren’t possible internally.  

We’ll share more details about how this will work at a later date. It’s a fairly involved process on our side, so we want to make sure everything is properly set up before we open the gates.  

Who knows. If it works out and you like it, maybe we’ll do more of them in the future.  

Farewell for now, until next time~  
Please look forward to it!

 

Last edited by a moderator: Feb 17, 2026

<!-- artifact:reactions:start -->
- 124 Like
- 59 Love
- 8 (unlabeled — rendered as base64 data URI)
- 6 (unlabeled — rendered as base64 data URI)
- 3 Haha
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Arakrates](https://forum.paradoxplaza.com/forum/members/arakrates.1605676/)**
Role: Design Manager
Badges: 53
Messages: 167
Reaction score: 1,427

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
