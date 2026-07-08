---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1518991/"
forum_thread_id: 1518991
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 92
title: "CK3 Dev Diary #92: Anatomy of a Game: From Report to Resolution"
dd_date: 2022-04-05
author_handle: jakeowaty
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2942
inline_image_count: 12
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1518991'
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
    location: raw_lines_~28_to_138
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_140_to_142
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_355_to_359
    action: preserved_and_flagged
    counts:
      Like: 42
      Haha: 18
      (unlabeled — rendered as base64 data URI): 2
      Love: 9
    note: Reactions block parsed; 3 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_367_to_442
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_443_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #92: Anatomy of a Game: From Report to Resolution

<!-- artifact:thread_metadata:start -->
- Thread starter [jakeowaty](https://forum.paradoxplaza.com/forum/members/jakeowaty.1376360/)
- Start date [Apr 5, 2022](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-92-anatomy-of-a-game-from-report-to-resolution.1518991/)
<!-- artifact:thread_metadata:end -->

Hello, everyone, and welcome back the Dev Diary. Let's have a little talk about the Anatomy of a Game (Development)! I'll be your host for today, [@jakeowaty](https://forum.paradoxplaza.com/forum/members/1376360/), current QA Lead on Crusader Kings 3, and I'm joined by Elisabeth, known as [@PDXOxycoon](https://forum.paradoxplaza.com/forum/members/1587488/) in these here parts - a wonderful programmer, a gentlewoman and a scholar, who you may have seen a few times already! (E*ditor's note:* *Can I mention the raw onion story?)*  

Today we are here to tell you about the process a bug goes through from being reported to being resolved and put into an update. Grab yourself the beverage of your choice, and enjoy this little expose on how we go about resolving bugs on Crusader Kings 3!  

---


### Bug report forum​

![yJCQc4LtcsL3TfoVIneL1a__83p_v7WBJD-UNHq20PCuDb1aP_WuxddM8EN5wXFs91hsR0WisK7tT0l3dhIL8kgcQcZ-hnEeWJa7AKZcLZtOD5VXtAVBNtLy2KQayQjWS5VCGFgf](https://lh3.googleusercontent.com/yJCQc4LtcsL3TfoVIneL1a__83p_v7WBJD-UNHq20PCuDb1aP_WuxddM8EN5wXFs91hsR0WisK7tT0l3dhIL8kgcQcZ-hnEeWJa7AKZcLZtOD5VXtAVBNtLy2KQayQjWS5VCGFgf "")


Whenever you launch the game, get yourself a your favorite gamer juice and steel your resolve for a few good hours of managing a medieval kingdom, there is a lot of stuff that happened behind the scenes to make it a memorable experience, free from issues. For a game as complex as Crusader Kings 3, this is even more important, and as the features get added to the game, it becomes more and more complicated, like a careful balancing act between economy, AI, warfare, interactions - all to ensure the experience you receive in the newest update is something worth waiting for!  

We are but a few humble people, whose job is to find out what works and what doesn’t and report any and all issues to the team before the game hits your platform of choice. But what happens when sometimes issues do remain hidden away and they will take spitting behind your shoulder 3 times on a 3rd fortnight of a 5th month on a leap year, during a full moon while dancing hokey-pokey to uncover?  

This is where you can come in and help! We can get rid of serious, big issues, find them ahead of time before you even realize they existed in the first place, and try and deliver a polished product. For anything else - well, it’s the economy of scale. With the variety of systems, languages, experiences, playstyles - YOU are the biggest help of all, in how a game can be shaped. And for that we have a special platform, called [Bug Report Forum](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/), where you can air out your grievances, provide feedback, reproduction steps and situations that irk you on the constant, so that our QA team can go through them much more efficiently and supply the team with a steady stream of new bugs to iron out for the next bug fix patch or release.  

---


### Verification​

![image5.jpg](https://forumcontent.paradoxplaza.com/public/813786/image5.jpg "image5.jpg")


[Comic on logging]​


Once you take your valuable time to report the issue that ruins your mojo when playing Crusader Kings, it lands on our Forum as a thread. We then take turns, employing QA power to go through the forums and reproduce them locally on our machines to ensure if the issue is serious, or perhaps we can offer support by providing advice on how to avoid it.  

Once the ticket is verified internally, using your reproduction steps, your description, screenshots, crash logs and saves, we then take the time to translate it into a language that our internal team can understand - Jira.  

There’s an art to this. Jira is an extremely helpful and smart tool to use, and QA by nature becomes naturally adept at using it skillfully. It’s usually the QA who does project-wide database evaluations, scrubbing it from obsolete tickets and updating any and all lingering ones to make sure the project team can focus on what’s important - making more fun stuff!  

Wait… **Obsolete**? You mean you just **CLOSE** old tickets?  

We do… *sometimes*. For example, if we had an issue lingering around in some hidden away system for a long time (and sometimes not even you, our community, are able to find it for years on end) - the issue becomes obsolete - either we just make the bug into a feature, or because we change a system entirely - it becomes changed so it’s not even a problem anymore. Happens on occasion, and even we are quite surprised that some bugs that linger for long never get picked up by the players, but hey - bugs are features too! Right?  

Riiiiiiiiiight…?  

---


### Jira - or how I learned to stop worrying about my mental health and learned to embrace the madness​

![image2.png](https://forumcontent.paradoxplaza.com/public/813787/image2.png "image2.png")


[Excerpt from “How to JIRA” guide]​


Now that might look like a lot, but trust me - there’s a way to learn this. First of all, it’s pretty straight forward; complex, but not complicated. We have been campaigning for the team to use Jira tickets efficiently. For example, if we get a ticket that says “Fix the thing we talked about yesterday” and there is nothing else in it, how can we remember what we have done, what needs to be done and how do we go back to it to retest? And again - fast-forward time to a month later and believe me - nobody will remember what in the world such a ticket meant.  

As a result, making sure all the fields are appropriately filled out is paramount to an efficient use of the database, and to make our team’s lives just a little bit easier when having to deal with a big pile of bugs that come from you or from our internal reporting.  

If everything is sorted, and everyone is on the same page, it makes it a lot easier for the producers to schedule when and how to report. And the upvoting on the forum? That’s an incredibly powerful tool to let us know which tickets need to be prioritized and fixed, no matter what. That’s how we can influence what is important to be fixed first.  

![image12.png](https://forumcontent.paradoxplaza.com/public/813788/image12.png "image12.png")


[QA chasing the Programmers]​


---


### The (un)lucky Programmer/Designer​

Once the bug has been verified, put into Jira, assigned a version and prioritized, a Developer can pick the bug up for fixing. This is typically either a Designer or a Programmer, depending on where the bug originates. In some cases the bug is reassigned to another role if the bug is found to be caused in another part of the game. Now that we know what the issue is and how it’s experienced, we need to investigate the how and why it happens.  

As an example of this, let us look at the recently fixed issue where the Holy Orders would raise themselves and immediately disband if they were called into a war. This issue was a side effect of letting Holy Orders raise themselves for Great Holy Wars: whenever a Holy Order is at war as an ally (which they qualify as during the Great Holy Wars), they would raise their armies.  

We start by looking at why the Order is disbanding the armies. If they’re raised, they must have something to fight against, right?  


![image7.png](https://forumcontent.paradoxplaza.com/public/813791/image7.png "image7.png")


[Code controlling if a order’s armies should be disbanded]​


Through developer magic known as debug mode and source code, we can step through each individual function call to see what’s going on. Stepping through this function leads us to finding that the war they are fighting in is not relevant to them, causing them to disband. Looking at the enemies in the war they’re in, none of them are of a hostile Faith. We also see that they are hired by the Grandmaster of the Order, so the Order itself decided to raise their armies, not another character hiring them.  

Holy Orders will not fight in wars where the opposing side does not have any participants of hostile Faith. Because we found the Holy Order disbanding due to being raised against an irrelevant enemy, we must look at the logic which controls how they are raised.  

I will spare you the initial dig down the AI code, but the short of it is: if a Holy Order can be raised, raise it. So we need to see why the Holy Order can be raised when it clearly should not be able to. We arrive at the following function.  


![image9.png](https://forumcontent.paradoxplaza.com/public/813792/image9.png "image9.png")


[Code to check the Holy Order can be hired by a Character]​


This logic checks if the Order can be hired by a character. This goes for any character looking to use the Order in question, even the Grandmaster of the Order. The Grandmaster of the Order is part of the war, so let us see where it leads us. Starting from the top, we check if the character can use the Order. Let us take a look at how that goes.  


![image7.png](https://forumcontent.paradoxplaza.com/public/813793/image7.png "image7.png")


[Code to check if a character can use the Holy Order]​


This is the code that checks if a character can use a Holy Order. When the Holy Order joins a war on its own, pCharacter is the Grandmaster, which is the Owner of the Holy Order. Makes perfect sense that the Grandmaster can make use of his own Holy Order. But, make notice further down: there is a check there, verifying if the character is in a relevant war. This is the same function that caused the army to disband earlier.  

Returning back to the function which checks if a Holy Order can be hired by our Grandmaster.  


![image4.png](https://forumcontent.paradoxplaza.com/public/813794/image4.png "image4.png")


[Code to check the Holy Order can be hired by a Character 2]​


To simplify things, I have collapsed all the irrelevant parts; contained within each “if” section is something which will cause the function to fail, and not allow the Grandmaster to hire their own Order. Let’s go through these relevant parts. We don’t run afoul with the hire limit, as we don’t hire any other Holy Orders as the Grandmaster of one. We are not already hired by someone else, so we skip that part. We own this order, so we don’t touch the third “if” statement. Finally, we can afford to hire our own Order. Look at that, this means we can hire the Holy Order!  

But returning back to the finding that the Holy Order would immediately disband because we’re not in a relevant war. This is where we find our solution: if we own our own Holy Order, we can always use it, but because of this we will not look if the war we are in is relevant at all. So we have a very simple solution to the problem.  


![image13.png](https://forumcontent.paradoxplaza.com/public/813795/image13.png "image13.png")


[Solution to preventing the Holy Order from being raised]​


We know that the check for relevant wars is only skipped if we are the Grandmaster of the Order, we don’t need to check the faith of our own Grandmaster, so this is what we’re left with: if the one who wants to hire the Holy Order is the Owner of the Order, check if they are in a relevant war or not.  

---


### The merge request process - everyone judges you​

When the fix has been created, it is put into what is called the merge request; this is the step before the fix is put into the upcoming build. Before it gets merged, there are a bunch of steps. It starts with one or more members of the team of appropriate discipline reviewing the changes being applied. This is the first step to spotting any unintended side effects that may occur with any given fix. The scrutiny of these reviews increase drastically with several more steps if the fix will go into an upcoming release.  


![image8.png](https://forumcontent.paradoxplaza.com/public/813796/image8.png "image8.png")


[Merge request overview for Preventing Holy Orders from raising themselves in irrelevant wars]​


Merge requests have a template that must be filled in when filed. This process gives both the fixer and reviewer the chance to review the implications of a fix and whether or not to actually commit it to a particular version. We make a serious consideration on how risky a fix is, can the fix have unintended knockon effects and the like, and how it impacts the overall performance of the game, does the fix contain a lot of computationally heavy code or script that will degrade performance.  

The golden rules of managing a merge request are:  


1. Reviewer is right until proven wrong.
2. Discipline leads are always right.

Adding a fix to a build generally requires approval from the discipline lead, tech lead and another reviewer, and only the tech lead can actually merge the fix into the build when we’re getting close to release.  


![image11.png](https://forumcontent.paradoxplaza.com/public/813797/image11.png "image11.png")


[The commit fixing the issue]​


The reviewer(s) give feedback on the merge request, and these must be addressed in one way or another. In the overview, you can see that the fix ended up being five commits in total, where just one of them was the fix itself. The rest were either addressing comments made in the review process or issues raised by the automated build and testing system, which we call pipelines. Speaking of pipelines.  


![image10.png](https://forumcontent.paradoxplaza.com/public/813798/image10.png "image10.png")


[Pipeline for merge request]​


Pipelines verify the integrity and quality of the code, build the game and test the game while the review process is going. All of these must pass for the merge request to be allowed to merge, unless explicit permission is given from the programmers, and in the case of an upcoming release the pipelines must be green. No exceptions.  

Once the fix has been merged, we hand it back over to the sadistic wonderful QA team.  

### The (sadistic) QA verification - where QA asks the fixer: “why are you running?!”​

![image6.png](https://forumcontent.paradoxplaza.com/public/813799/image6.png "image6.png")


[Happy tears from QA after a 2 year old issue was resolved]​


Once a ticket gets processed, churned through the complicated development machine, the issue is removed from the game, the correct code, script or asset gets merged into the game, the ticket is then marked as resolved.  

This is when we get our hands on it one more time to verify if the fix has not only resolved the issue listed therein, but also that it has no other knock-on effects. Think of big fixes like a domino - you push one piece and the others will fall. Sometimes a different set of dominos, that we set up a long time ago, gets randomly pushed and some older issues reappear out of nowhere. It happens when you deal with a complex codebase, in which case you sometimes do see returning fan favorites.  

But all we have to do is revisit the older system, fix it (again), and away we go! Unless yet another bug is retriggered, in which case… Well, we have to revisit yet another system. Videogames are hard, m’kay?  

This is why we sometimes need to go through the same ticket again, and again, and again, until we are very sure it fixes more things than it breaks. Sometimes bugs linger in our database for a long time. Trust us - we know that issues you mentioned on release still persist and we want to fix everything, but with every release we get a new batch of tickets we have to go through…  

So.  
Many.  
Times.  
However, once the fix is confirmed, and the build is locked in - we are ready to press the large green button and release it for your scrutiny and repeat aforementioned hokey-pokey jig again!  

---


### The Update - Are we done yet?​

Not really. On our end we close the bug as resolved, but there is one last thing that comes into play on resolving a bug. This is all of you, the community. The QA team catches most of the problems before a release is made, but sometimes for an issue to reoccur, you need the stars to align on a laptop manufactured on 29th of February 2020 while the player is doing the Macarena.  

Paraphrasing, of course, but there are cases where an issue can reemerge later. This can happen due to a myriad of factors that are hard to account for. Some issues can be related to hardware and specific circumstances we don’t have the capacity to test for. This is when we rely on you all to be vigilant and report issues back to us. The more detailed and specified, the better. Once this is done we go back from the top of this expose and do the dance one more time.  

If no one in the community experiences the issue again, then it stays resolved.  

I hope you all have enjoyed this little expose into the life of a game developer! Thank you for your time, and we wish you a very pleasant day.  

Until next time!

 

- 87

<!-- artifact:reactions:start -->
- 42 Like
- 18 Haha
- 12 (unlabeled — rendered as base64 data URI)
- 9 Love
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [jakeowaty](https://forum.paradoxplaza.com/forum/members/jakeowaty.1376360/)**
Role: Captain
Badges: 44
Messages: 476
Reaction score: 728

*[Full game-badge icon list of 22 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
