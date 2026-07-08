---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1289167/"
forum_thread_id: 1289167
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 5
title: "CK3 Dev Diary #5 - Schemes, Secrets and Hooks"
dd_date: 2019-11-26
author_handle: Voffvoffhunden
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1596
inline_image_count: 6
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1289167'
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
    location: raw_lines_~28_to_144
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_146_to_148
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_232_to_234
    action: preserved_and_flagged
    counts:
      Like: 5
      Love: 3
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 2 of 3 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_242_to_309
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_310_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #5 - Schemes, Secrets and Hooks

<!-- artifact:thread_metadata:start -->
- Thread starter [Voffvoffhunden](https://forum.paradoxplaza.com/forum/members/voffvoffhunden.246161/)
- Start date [Nov 26, 2019](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-5-schemes-secrets-and-hooks.1289167/)
<!-- artifact:thread_metadata:end -->

Greetings, dear would-be kings and queens!  

I’m Voffvoffhunden (also known as Petter on the discord or even in private life), one of the game’s content designers. Most people probably haven’t seen me around a lot, since I’ve been working on CK3 in secret since the release of HoI4. It’s been a long journey, but it’s been fun to see the game develop and grow over time, and it’s even more fun now that we get to talk about it to all of you! Today, said talking will be about a handful of new features that together cover some of the most important parts of the Crusader Kings experience. So where better to start than with murder?  

We’ve all been there. A united Scandinavia is within your grasp, if only it hadn’t been for your meddling siblings! In CK2, these kinds of problems were handled with the gentle application of the “Murder Plot”, as it was popularly called. That system has been expanded and replaced with our brand new Scheme system!  

For Crusader Kings 3, we wanted a system that was slightly easier to predict while keeping it unreliable in its outcome, so that murder remains an… option, rather than a safe bet. We also wanted to reduce the number of agents that you need, to make it more valuable to focus on a few candidates close to the victim, rather than having to send messengers with bags of gold to every single courtier and vassal in the land.  

All this is achieved through our new Scheme system, where you can use target a character with a Scheme in accordance with your plans, recruit Agents, build up your Scheme Success Chance, and finally achieve your goal. I’ll try to illustrate how it all works by referring to that most iconic of all Schemes: Murder.  

![ongoing murder scheme USABLE.PNG](https://forumcontent.paradoxplaza.com/public/515775/ongoing murder scheme USABLE.PNG "ongoing murder scheme USABLE.PNG")




By now, the progress bar might have caught your eye. Each month, a Scheme has a chance of progressing one step, with the odds determined by the Owner’s Scheme Power, and the Target’s Scheme Resistance. These two values are based on the relevant Skill (Intrigue in the case of Murder) but are also affected by Spymasters (in the case of Intrigue-type schemes), various modifiers, and of course - the Owner’s Agents. The closer a Murder Scheme’s Agents are to the Target (and the better their Intrigue), the more Scheme Power they add.  

Once the Scheme has progressed 10 steps, it tries to execute. The chance of a successful outcome is determined by the Scheme’s Success Chance (which has a slightly different set of modifiers to Scheme Power), while its Secrecy is used to check whether you are discovered or not when you try to execute.  

If you’ve gathered capable agents and you’re lucky enough to not get caught, that inheritance will be as good as yours!  

As the Scheme's Owner, you are protected from discovery until you actually attempt to execute your scheme. This protection does not extend to your agents, however! And being discovered as a participant in a murder plot is rarely good for one’s reputation, or for one’s habit of seeing sunlight every day.  

It is worth noting that when the existence of a Scheme is discovered in this way, its chance of success drops significantly, as the appointed victim makes every preparation possible to foil your plans.  

On the other hand, perhaps you’re just not the murderous type? Thankfully the Scheme system is so flexible that it can be used for all manner of long-term interactions. On the opposite end of the spectrum, Seduction makes a return as a Scheme. Seduce does not use Agents in the way Murder does, and it’s not dangerous in the same way… unless your target happens to be married, that is. Achieving success - determined by things such as your skill at seduction, their sexual preference, and whether you get along whatsoever - can net you a new Lover.  
I know where your minds are going at that thought, and yes - it’s a great way of acquiring Agents for your Murder Scheme!  

Sway is another returning favourite that’s now a Scheme. Sway also doesn't use Agents but largely relies on your Diplomacy instead. It simply progresses towards its execution and then checks whether you successfully improve their opinion or not. Then it loops around and starts over, building up the target’s opinion of you until you stop it -- or commit some horrible diplomatic faux pas...  

To add to the convenience, all characters can run one Hostile Scheme (such as murder) and one Personal Scheme (such as Seduction or Sway) at the same time. Unfortunately, you can only target a given character with a single scheme at a time, so you won’t be able to both murder and seduce the same person, just to see which one pays off sooner. You have to do one after the other.  

Now, as I indicated earlier, trying to murder someone is usually illegal. (Fun fact: according to Paradox’s legal department this is also the case in real life.) However, if you’re not discovered when you do it, you’re off the hook, right? Not so! Let me introduce you to something that will change the way you nervously glance over your shoulder forever: Secrets!  

![hooks and secrets USABLE.PNG](https://forumcontent.paradoxplaza.com/public/515777/hooks and secrets USABLE.PNG "hooks and secrets USABLE.PNG")




Characters can acquire Secrets when they do something that is frowned upon or outright illegal. You want to keep your own Secrets close to your chest, while it can be of great benefit to uncover the Secrets of others. By sending your Spymaster to… well, spy, it’s possible to find out what is going on with your annoying vassals, your threatening neighbour, or even at your own court!  

So what do you do when you discover a Secret? One possible course of action is to expose it for the world to see, of course! This will apply various effects depending on how serious the Secret is. Being the King’s secret lover will cause a scandal, being a Secret Deviant will leave you with the Deviant trait, while being exposed as a secret murderer is exactly the excuse your Liege has been waiting for to throw you in the dungeon. Not to mention those horrible Kinslaying penalties (“Hey, they’re my family, and I choose what to do with them, okay?”).  

The other possible course of action ties into our new evolution of CK2’s Favors. This is now a generalised system called “Hooks”, which come in various flavours. Favors is one of these, while another might represent the loyalty that a House member owes to the House Head.  

A Hook is used to force characters to do what you want them to, such as accepting marriage offers, changing your Feudal Contract, or forcing them to join your Scheme as an Agent…  

![forcing prince bishop to accept USABLE.png](https://forumcontent.paradoxplaza.com/public/515784/forcing prince bishop to accept USABLE.png "forcing prince bishop to accept USABLE.png")

  


There are Weak and Strong Hooks, where weak Hooks are used up once expended, while Strong Hooks only get a cooldown, ready to be used again later. The source of a Hook determines its strength, and the strongest Hooks come from Blackmailing someone over their most horrible secrets…  

![blackmail over incest USABLE.PNG](https://forumcontent.paradoxplaza.com/public/515780/blackmail over incest USABLE.PNG "blackmail over incest USABLE.PNG")




You might want to keep hold of a Hook once you have it, though, rather than spending it. Having a Hook on someone can prevent them from taking hostile actions towards you -- particularly useful when dealing with pesky vassals. Be warned, however. While having a strong Blackmail Hook on someone really gives you the upper hand, it will be lost if the Secret you are blackmailing over is exposed.  

There are many types of Schemes, Secrets and Hooks in the game, and while it would be entirely possible to list them all, I think it would be way more fun for you to gradually discover them through future dev diaries or once the game is released.  

Hopefully, it’s clear by now how everything I have talked about hangs together. Maybe you want to murder someone, so you need some Agents. However, no one wants to join, so you dig for Secrets that can be converted into Blackmail Hooks. Meanwhile, you’re running a Personal Scheme (such as Sway) to increase another potential Agent’s opinion of you, so that you can convince them that -- yes, their Liege really is that bad.  

But what if everyone hates you (on account of all the murderin’) and you’re unable to find a single blackmail-worthy speck of dirt on anyone?  

Well, in Crusader Kings 3 there might be something you can do about that…  

![Fabricate Hook teaser USABLE.PNG](https://forumcontent.paradoxplaza.com/public/515779/Fabricate Hook teaser USABLE.PNG "Fabricate Hook teaser USABLE.PNG")

 

#### Attachments

- [![forcing prince bishop to accept USABLE.PNG](https://forumcontent.paradoxplaza.com/thumbnail/public/515778/forcing prince bishop to accept USABLE.PNG)](https://forum.paradoxplaza.com/forum/attachments/forcing-prince-bishop-to-accept-usable-png.528423/)
  
  forcing prince bishop to accept USABLE.PNG
  672,9 KB

 · Views: 34.249

<!-- artifact:reactions:start -->
- 5 Like
- 3 Love
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Voffvoffhunden](https://forum.paradoxplaza.com/forum/members/voffvoffhunden.246161/)**
Role: Rouge Game Dev - Former CK3 Content Designer
Badges: 74
Messages: 261
Reaction score: 1,286

*[Full game-badge icon list of 2 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
