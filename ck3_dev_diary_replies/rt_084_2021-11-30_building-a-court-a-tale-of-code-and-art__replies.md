---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1500937/"
forum_thread_id: 1500937
content_type: reply_thread
parent_dd_file: dd_084_2021-11-30_dev-diary-84-building-a-court-a-tale-of.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 84
title: "CK3 Dev Diary #84 - Building a Court - A Tale of Code and Art"
dd_date: 2021-11-30
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 9
reply_count: 164
participant_count: 80
reply_date_first: 2021-11-30
reply_date_last: 2021-12-20
body_word_count: 8723
inline_image_count: 0
quoted_span_count: 125
extraction_rationale: |
  Full reply thread captured live via Claude in Chrome (article.message bodies).
  Quote blocks split into artifact:quote spans and excluded from word counts.
  Usernames replaced by stable per-thread participant ids; the dev-diary OP is
  excluded (see parent_dd_file).
notes_for_analyst: |
  Community-voice counterpart to the linked dev diary. Strip YAML + artifact
  comments before tokenizing, exactly as for dd_*.md.
---

# Reply thread — CK3 Dev Diary #84 - Building a Court - A Tale of Code and Art

*164 replies from 80 participants across 9 pages*

## Reply 1 — participant_001 · 2021-11-30 · post-27933252

First! Check the FAQ Royal Court if you have any question about the upcoming CK3 Expansion! And if you have a question for the developers regarding the Court Types & Content, drop them here

## Reply 2 — participant_002 · 2021-11-30 · post-27933254

Can we have the option to have this into the game ?

## Reply 3 — participant_003 · 2021-11-30 · post-27933260

Just an idea for future diaries, since we have about 2 months before the release: go back to the culture changes, and detail any updates since you last covered it extensively in a DD, and then just info dump us tenets and stuff (and in-game cultures) over 2-3 weeks.

## Reply 4 — participant_004 · 2021-11-30 · post-27933261

Thank you for all your effort I was hoping for some new mechanics tied to Royal Courts' "flavours", like Regencies, but anyway very good job!

## Reply 5 — participant_005 · 2021-11-30 · post-27933265

Nice I hope we get to see more of the cultural traditions in the teasers before release. For the accompanying patch, please look at making AI Kingdoms/Empires more stable, they don't seem to handle rebellions well. Apart from the debt loop the Byzantines seem to be the most stable, which is GOOD, but if their main rivals the Abbasids or Seljuks just fall apart and implode, which they always do, that leaves them with no real challenge and immersion-breaking border gore. Right now there is no incentive to building relations with an AI King, because you know they will be replaced in a rebellion the next year anyway.

## Reply 6 — participant_002 · 2021-11-30 · post-27933266

On a more serious note : How many variations will we get per court type ? Thanks for the work !

## Reply 7 — participant_006 · 2021-11-30 · post-27933268

<!-- artifact:quote:start -->
> Salazard260 said: View attachment 780729 Can we have the option to have this into the game ? Click to expand...
<!-- artifact:quote:end -->
*(no text body — reaction-only or media-only post)*

## Reply 8 — participant_007 · 2021-11-30 · post-27933291

Looks good. One question: Do we get to decide which of the court styles we want? If no: What are the criteria for which one we will get?

## Reply 9 — participant_008 · 2021-11-30 · post-27933298

<!-- artifact:quote:start -->
> Salazard260 said: Can we have the option to have this into the game ? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Salazard260 said: On a more serious note : How many variations will we get per court type ? Thanks for the work ! Click to expand...
<!-- artifact:quote:end -->
I have inquired about it, since I do have some fun memories of that mode in N64 Goldeneye, but no plans of it right now. Maybe I can challenge the character and tech leads to a duel for it in the future, slappers only! There are currently three court variants for each of the visual culture groups, with each of those having three grandeur level variations to them. Landing at a total of 12 variants, 36 counting grandeur variants. Part of the variation is also gained from the artifacts you chose to decorate your courts with, as some artifacts are hung on the walls or stand like furniture on the edges or on pedestals in the center. Edit: corrected a number, math..

## Reply 10 — participant_009 · 2021-11-30 · post-27933310

On the long-term design roadmap, are there any plans to have the characters walk?

## Reply 11 — participant_010 · 2021-11-30 · post-27933312

<!-- artifact:quote:start -->
> Salazard260 said: View attachment 780729 Can we have the option to have this into the game ? Click to expand...
<!-- artifact:quote:end -->
Yeah, in Bobblehead Expansion

## Reply 12 — participant_011 · 2021-11-30 · post-27933325

<!-- artifact:quote:start -->
> fodazd said: Looks good. One question: Do we get to decide which of the court styles we want? If no: What are the criteria for which one we will get? Click to expand...
<!-- artifact:quote:end -->
Visual style is based on various cultural and geographical triggers. A bit similar to how the game decides which holdings and units graphics to use. One way for the player to affect it - is to hybridize cultures and pick the desired visual style there. Spoiler

## Reply 13 — participant_012 · 2021-11-30 · post-27933337

<!-- artifact:quote:start -->
> Carlberg said: Grandeur variants was a further change we added later in the development cycle, which helps give a little extra flavor to the progress of your court's grandeur. Lower court grandeur has less fancy details and furniture extras in the court than the higher level which sports more of them. The surfaces of the room have also been made to look more worn and less taken care of at a lower grandeur level, compared to the high grandeur which look their grandest. Click to expand...
<!-- artifact:quote:end -->
Why are grandeur variants so similar to each other? I can tell one from another only when I see both at once...

## Reply 14 — participant_013 · 2021-11-30 · post-27933341

I somehow don't like the artifact vitrines in the courtroom. They feel totally out of place. Wouldn't they be at the wall or in another special treasure room? It looks really strange.

## Reply 15 — participant_012 · 2021-11-30 · post-27933345

<!-- artifact:quote:start -->
> Alien-47 said: Visual style is based on various cultural and geographical triggers. A bit similar to how the game decides which holdings and units graphics to use. One way for the player to affect it - is to hybridize cultures and pick the desired visual style there. Click to expand...
<!-- artifact:quote:end -->
It reminds me palace building feature from Civilization 1...

## Reply 16 — participant_013 · 2021-11-30 · post-27933347

I really hope that there is a way to get more visual styles later on. Like if there is a DLC dealing with Mongols or other underrepresented cultures that we get new thronrooms styles if we own this DLC. That this will not be the case is my biggest worry for this beeing a DLC locked feature.

## Reply 17 — participant_012 · 2021-11-30 · post-27933353

<!-- artifact:quote:start -->
> Anonymous01 said: On the long-term design roadmap, are there any plans to have the characters walk? Click to expand...
<!-- artifact:quote:end -->
They learn horse-riding before they learn to walk.

## Reply 18 — participant_014 · 2021-11-30 · post-27933354

Is the fireplace still on in the summer? When I'm a Scandinavian lord, is there any change in the seasons, such as the sun getting darker in the winter, or the heavy rain sounds in the rainy season when I'm Raja in India? Anyway, it's a nice room!

## Reply 19 — participant_015 · 2021-11-30 · post-27933366

<!-- artifact:quote:start -->
> Salazard260 said: View attachment 780729 Can we have the option to have this into the game ? Click to expand...
<!-- artifact:quote:end -->
Second the call for an optional Big Head mode.

## Reply 20 — participant_016 · 2021-11-30 · post-27933371

Owners of Northern lords deserve unique Scandinavian courts What's the point of buying flavour packs otherwise

## Reply 21 — participant_017 · 2021-11-30 · post-27933374

Can we choose the specific variant of our court? I like the stone walls for Western courts, but that red/white wallpaper... if it's historical, then sorry, but people in those times had bad taste Other variants looke great, epsecially the ones with big windows. Btw, you have a small typo: "variation to the the grandeur levels"

## Reply 22 — participant_008 · 2021-11-30 · post-27933390

<!-- artifact:quote:start -->
> Anonymous01 said: On the long-term design roadmap, are there any plans to have the characters walk? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Testeria said: Why are grandeur variants so similar to each other? I can tell one from another only when I see both at once... Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Testeria said: It reminds me palace building feature from Civilization 1... Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Asterios_III said: Is the fireplace still on in the summer? When I'm a Scandinavian lord, is there any change in the seasons, such as the sun getting darker in the winter, or the heavy rain sounds in the rainy season when I'm Raja in India? Anyway, it's a nice room! Click to expand...
<!-- artifact:quote:end -->
No plans for walking characters on the books right now i'm afraid. It's a gradual change that happens to the court over time, and we decided to avoid going from luxurious down all the way to overly dilapidated/trashed. A King (or higher) would have some standards was the angle we took. I believe that feature was also present in Civ 2, it was fun to mix and match, slowly improving on it and also brought a bit of a break to the map-staring We did have a bit of a look back at those features when we were first planning for our own courts. The hearth is ever burning in the Kings court. Right now seasons aren't shown in the courts that are indoors, and we don't really model the day-night cycle in the game. But maybe that's something we can think about in the future even if its not planned at the moment. And thanks!

## Reply 23 — participant_018 · 2021-11-30 · post-27933398

Thanks for all your hard work.

## Reply 24 — participant_019 · 2021-11-30 · post-27933408

The courts are looking really nice, a lot better. Can't wait to play. Thanks for all your work!

## Reply 25 — participant_011 · 2021-11-30 · post-27933409

<!-- artifact:quote:start -->
> Agamidae said: Can we choose the specific variant of our court? I like the stone walls for Western courts, but that red/white wallpaper... if it's historical, then sorry, but people in those times had bad taste Other variants looke great, epsecially the ones with big windows. Btw, you have a small typo: "variation to the the grandeur levels" Click to expand...
<!-- artifact:quote:end -->
No, specific variant is picked at random based on your capital location. If you want to try your luck, try moving it several times across different rulers. I realize it's not a very satisfying answer, but player customization is limited to placing artifacts. Making proper UI and mechanics for editing static room elements was simply too much for the scope of the expansion.

## Reply 26 — participant_002 · 2021-11-30 · post-27933415

<!-- artifact:quote:start -->
> Right now seasons aren't shown in the courts that are indoors Click to expand...
<!-- artifact:quote:end -->
Indoor courts? As in some are outdoors ?

## Reply 27 — participant_008 · 2021-11-30 · post-27933418

<!-- artifact:quote:start -->
> Salazard260 said: Indoor courts? As in some are outdoors ? Click to expand...
<!-- artifact:quote:end -->
Bad wording on my part, we dont have any outdoor courts in Royal Court.

## Reply 28 — participant_020 · 2021-11-30 · post-27933425

Oh? That's a bug? Weird, I thought that was a perfectly accurate depiction of the people of that era based on historical art.

## Reply 29 — participant_021 · 2021-11-30 · post-27933432

How open is the whole thing to modding? Will it be hard to add new rooms for certain culture groups? Aside from the difficutly of actually creating those 3D assets I mean.

## Reply 30 — participant_022 · 2021-11-30 · post-27933447

Thanks for this - a very interesting read and insight into the process! I note you say that you hope this will be a great foundation for a feature that you can grow over time - do you refer here specifically to the courtroom feature (so, for example, adding new variants in the future), or to 3D scenes generally (one idea that comes to mind is adding cathedrals and other places of worship in a religion-themed DLC)?

## Reply 31 — participant_013 · 2021-11-30 · post-27933456

<!-- artifact:quote:start -->
> Aztlantix said: Owners of Northern lords deserve unique Scandinavian courts What's the point of buying flavour packs otherwise Click to expand...
<!-- artifact:quote:end -->
Fully agree. That's why i am dissappointed that there are only 4 diffrent styles.

## Reply 32 — participant_023 · 2021-11-30 · post-27933481

I suppose Slavs will use Western type of courts, which is quite disappointing. It would be much better to see separate type of court used by Slavs, Scandinavians and other Northerners.

## Reply 33 — participant_011 · 2021-11-30 · post-27933484

<!-- artifact:quote:start -->
> Silens said: How open is the whole thing to modding? Will it be hard to add new rooms for certain culture groups? Aside from the difficutly of actually creating those 3D assets I mean. Click to expand...
<!-- artifact:quote:end -->
Totally open. Add new culture themes based on triggers, add more variations within the culture. Scene configuration itself is in script files, that one can edit manually or with some debug tools

## Reply 34 — participant_024 · 2021-11-30 · post-27933506

<!-- artifact:quote:start -->
> Alien-47 said: No, specific variant is picked at random based on your capital location. If you want to try your luck, try moving it several times across different rulers. I realize it's not a very satisfying answer, but player customization is limited to placing artifacts. Making proper UI and mechanics for editing static room elements was simply too much for the scope of the expansion. Click to expand...
<!-- artifact:quote:end -->
Could you mod in variation choice similar to how the barbershop works for clothing?

## Reply 35 — participant_025 · 2021-11-30 · post-27933511

I like all these courts, apart from the Western one: it is... too small, it doesn't seem a Throne Room. However the others are great, and the improvements are very radical! As others pointed out, I wish for more variation over the years (with flavor packs or so), and little things like the fire lit or not, the weather, etc etc.

## Reply 36 — participant_017 · 2021-11-30 · post-27933515

<!-- artifact:quote:start -->
> Alien-47 said: No, specific variant is picked at random based on your capital location. Click to expand...
<!-- artifact:quote:end -->
I assume it's scripted, not hardcoded? If so, than no problem, we could set up a way to select it.

## Reply 37 — participant_011 · 2021-11-30 · post-27933523

<!-- artifact:quote:start -->
> Koyraboro said: Could you mod in variation choice similar to how the barbershop works for clothing? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Agamidae said: I assume it's scripted, not hardcoded? If so, than no problem, we could set up a way to select it. Click to expand...
<!-- artifact:quote:end -->
It might be possible with modding the culture theme selection, but not with the variant within the culture.

## Reply 38 — participant_026 · 2021-11-30 · post-27933530

This is probably well beyond the scope of this expansion, but I was wondering if you'd consider having the court rooms change not only by culture but also technology level. I imagine an early Middle Ages courtroom probably looks different than a late Middle Ages one, and both should certainly look different than a tribal era one.

## Reply 39 — participant_027 · 2021-11-30 · post-27933534

<!-- artifact:quote:start -->
> Carlberg said: The hearth is ever burning in the Kings court. Right now seasons aren't shown in the courts that are indoors, and we don't really model the day-night cycle in the game. But maybe that's something we can think about in the future even if its not planned at the moment. Click to expand...
<!-- artifact:quote:end -->
*Stares in Vampire*

## Reply 40 — participant_028 · 2021-11-30 · post-27933539

I know that after this DLC I will not be able to continue playing, I know it is impossible for my toaster to run so many graphics.

## Reply 41 — participant_029 · 2021-11-30 · post-27933540

<!-- artifact:quote:start -->
> Alien-47 said: Totally open. Add new culture themes based on triggers, add more variations within the culture. Scene configuration itself is in script files, that one can edit manually or with some debug tools Click to expand...
<!-- artifact:quote:end -->
So does this mean modders could tie a unique court scene to a title? I'm thinking of mods like Elder Kings with the Ruby Throne room when you own the Imperial City.

## Reply 42 — participant_011 · 2021-11-30 · post-27933550

<!-- artifact:quote:start -->
> Kgboi said: So does this mean modders could tie a unique court scene to a title? I'm thinking of mods like Elder Kings with the Ruby Throne room when you own the Imperial City. Click to expand...
<!-- artifact:quote:end -->
Any interface trigger should work. You can take a look illustrations and their dynamic selection. All you can do there, is also possible for royal court.

## Reply 43 — participant_011 · 2021-11-30 · post-27933553

<!-- artifact:quote:start -->
> juanigas said: I know that after this DLC I will not be able to continue playing, I know it is impossible for my toaster to run so many graphics. Click to expand...
<!-- artifact:quote:end -->
That's not true. If you have character animations disabled, court room will become a static picture, rendered only once - when the view is opened.

## Reply 44 — participant_030 · 2021-11-30 · post-27933557

<!-- artifact:quote:start -->
> Alien-47 said: That's not true. If you have character animations disabled, court room will become a static picture, rendered only once - when the view is opened. Click to expand...
<!-- artifact:quote:end -->
If character animation is enabled we will see characters doing animations?

## Reply 45 — participant_031 · 2021-11-30 · post-27933560

If not this expansion, then in later DLCs or flavor packs, I hope we'll eventually see Ermine Lined Coronation Robes. Even if only in the Court View...

## Reply 46 — participant_028 · 2021-11-30 · post-27933564

<!-- artifact:quote:start -->
> Alien-47 said: That's not true. If you have character animations disabled, court room will become a static picture, rendered only once - when the view is opened. Click to expand...
<!-- artifact:quote:end -->
you made my day

## Reply 47 — participant_011 · 2021-11-30 · post-27933569

<!-- artifact:quote:start -->
> Trinita132 said: If character animation is enabled we will see characters doing animations? Click to expand...
<!-- artifact:quote:end -->
Of course. You get full spectrum of things: animated characters, special animations for some court roles, flickering and trembling lights from fireplaces, smooth camera transitions between points of view, optional slight idle camera panning.

## Reply 48 — participant_032 · 2021-11-30 · post-27933582

Can you replace the zigzaggy texture in the Western variant one? It looks more like someone's accent wall than anything medieval because it's so simple. I'd prefer a wood textured one without colour over it even, were you not dedicated to making it look more authentic.

## Reply 49 — participant_033 · 2021-11-30 · post-27933592

<!-- artifact:quote:start -->
> Alien-47 said: It might be possible with modding the culture theme selection, but not with the variant within the culture. Click to expand...
<!-- artifact:quote:end -->
Why not? Having preset clothing colors that you can change only by creating character from scratch is so inconvenient when everything else is so open to customization. Big sad

## Reply 50 — participant_034 · 2021-11-30 · post-27933595

<!-- artifact:quote:start -->
> Alien-47 said: Visual style is based on various cultural and geographical triggers. A bit similar to how the game decides which holdings and units graphics to use. One way for the player to affect it - is to hybridize cultures and pick the desired visual style there. Spoiler View attachment 780758 Click to expand...
<!-- artifact:quote:end -->
I was wondering how hybridizing cultures would play into the courts' looks. An interesting way to eventually expand on this (and I understand this would be a long way off from happening and maybe not even feasible, but it just popped into my head looking at the screenshots) would be being able to have some sort of mixture of cultural elements in a court for a hybridized culture if it's a hybrid of two different court styles. So if you had, say, a Greek-Levantine hybrid, the court would have a mix of Mediterranean and Middle Eastern court graphics. Just something that would be neat if possible, especially later on if/when more styles of court graphics get added to the game.

## Reply 51 — participant_035 · 2021-11-30 · post-27933616

<!-- artifact:quote:start -->
> Alien-47 said: No, specific variant is picked at random based on your capital location. If you want to try your luck, try moving it several times across different rulers. Click to expand...
<!-- artifact:quote:end -->
I understand the limitation, but please consider adding an option to choose between the three sub-variations for the player. Moving the capital is quite an inconvenience. It could be a minor decision similar to 'exoticise the court room', but your Court Architect offers you a choice between the three sub-variations. Everything is looking great and I'm extremely eager to play with the Royal Court!

## Reply 52 — participant_036 · 2021-11-30 · post-27933630

Any chance we can get more of a showcase of the CoAs creator? That has me excited the most next to hybrid cultures.

## Reply 53 — participant_037 · 2021-11-30 · post-27933653

Looking at the table in the front holding the goblet, the faces towards the camera are almost black, suggesting there is no light source from that side, and yet it casts no shadow whatsoever. Why not?

## Reply 54 — participant_038 · 2021-11-30 · post-27933676

<!-- artifact:quote:start -->
> Tiax said: View attachment 780828 Looking at the table in the front holding the goblet, the faces towards the camera are almost black, suggesting there is no light source from that side, and yet it casts no shadow whatsoever. Why not? Click to expand...
<!-- artifact:quote:end -->
The picture literally has "Under Development" on it. I would imagine that's why.

## Reply 55 — participant_037 · 2021-11-30 · post-27933682

<!-- artifact:quote:start -->
> InsidiousMage said: The picture literally has "Under Development" on it. I would imagine that's why. Click to expand...
<!-- artifact:quote:end -->
I mean yeah, that's certainly a possible explanation, but it's also in a section titled "finished courts", so I'm not clear whether they intend to do further refinement of something so fundamental as the lightning model.

## Reply 56 — participant_038 · 2021-11-30 · post-27933698

<!-- artifact:quote:start -->
> Tiax said: I mean yeah, that's certainly a possible explanation, but it's also in a section titled "finished courts", so I'm not clear whether they intend to do further refinement of something so fundamental as the lightning model. Click to expand...
<!-- artifact:quote:end -->
"Finished" can mean several things in this context, like they've finished the major design and style choices, layouts and whatnot, but are still refining things like camera angles and lighting. I image they will be refining things up until the last minute.

## Reply 57 — participant_039 · 2021-11-30 · post-27933704

<!-- artifact:quote:start -->
> Alien-47 said: That's not true. If you have character animations disabled, court room will become a static picture, rendered only once - when the view is opened. Click to expand...
<!-- artifact:quote:end -->
That is nice to hear. I had a similar concern even though I don't have a complete toaster. I do use a Mac, though, and the game and the graphics don't seem to well-optimised for that. How many different set ups do you test this on? CK3 portrait graphics look always a bit off on my computer and I'm concerned this might intensify with something like the court rooms.

## Reply 58 — participant_034 · 2021-11-30 · post-27933714

<!-- artifact:quote:start -->
> Tiax said: View attachment 780828 Looking at the table in the front holding the goblet, the faces towards the camera are almost black, suggesting there is no light source from that side, and yet it casts no shadow whatsoever. Why not? Click to expand...
<!-- artifact:quote:end -->
If you look closely it actually does cast a shadow. It's just that most of where it would be is already in the greater shadow created by the back wall, whereas the table behind it is casting a shadow into an otherwise lit area so the shadow there is more noticeable.

## Reply 59 — participant_040 · 2021-11-30 · post-27933732

First of all I want to begin by saying thank you for this amazing effort. looks like development is at its ending stages now and it's only QoL improvements and bug fixes to do, good luck and take your time

## Reply 60 — participant_037 · 2021-11-30 · post-27933740

<!-- artifact:quote:start -->
> wilcoxchar said: If you look closely it actually does cast a shadow. It's just that most of where it would be is already in the greater shadow created by the back wall, whereas the table behind it is casting a shadow into an otherwise lit area so the shadow there is more noticeable. Click to expand...
<!-- artifact:quote:end -->
I think the shadow for the one behind it may actually be shadows of the people standing next to it, although it's very tough to tell. The shadows don't seem to connect to the feet of the table, which makes me think they're from the people. I can't see any shadow for the front table, even zoomed in. Only the throne seem to cast a shadow.

## Reply 61 — participant_041 · 2021-11-30 · post-27933755

I know it's probably too late for suggestions, but i think it would be really fucking cool if you made models for cats and dogs and had them appear on the court of a ruler that owns one. Maybe even make different regional variants. That would also help pave the way for when we inevitably get glitterhoof as a councillor. Just a thought, cause I understand this is probably very low on a list of priorities.

## Reply 62 — participant_034 · 2021-11-30 · post-27933777

<!-- artifact:quote:start -->
> Tiax said: I think the shadow for the one behind it may actually be shadows of the people standing next to it, although it's very tough to tell. The shadows don't seem to connect to the feet of the table, which makes me think they're from the people. I can't see any shadow for the front table, even zoomed in. Only the throne seem to cast a shadow. Click to expand...
<!-- artifact:quote:end -->
No, the shadows are pretty consistent with a light source coming from the sun outside the window.

## Reply 63 — participant_037 · 2021-11-30 · post-27933808

<!-- artifact:quote:start -->
> wilcoxchar said: No, the shadows are pretty consistent with a light source coming from the sun outside the window. Click to expand...
<!-- artifact:quote:end -->
Maybe I'm just too colorblind, but I cannot for the life of me see what you've circled below the goblet table. I apologize if this whole question is just my crappy color vision.

## Reply 64 — participant_034 · 2021-11-30 · post-27933815

<!-- artifact:quote:start -->
> Tiax said: Maybe I'm just too colorblind, but I cannot for the life of me see what you've circled below the goblet table. I apologize if this whole question is just my crappy color vision. Click to expand...
<!-- artifact:quote:end -->
No worries. It is pretty subtle since it's really only the shadow from the bottom of the table that's visible before the rest blends with the shadow from the back wall, and I only fully noticed it after zooming in.

## Reply 65 — participant_042 · 2021-11-30 · post-27933843

I have a cosmetic suggestion: To avoid disrupting immersion wouldn't it be appropriate if all the court members adapted the costume styles of the court they are in (unless otherwise specified by the player? also for the same reason it would be interesting to put by default some clothing rules in different cultures and courts. Just to give an example I see way too many women with free flowing hair in those court images, that would not have been considered appropriate in most of the cultures in most of the middle ages not to mention the strict separation of the sexes which occurred in most of the Muslim world ( would it be maybe possible to make rooms reserved for women, add some screens or at least veiling options?) it really breaks the immersion to see female courtiers and members of the ruling family to interact forgetting all those traditions!

## Reply 66 — participant_043 · 2021-11-30 · post-27933945

Hello Paradox! Architecture student here. The throne rooms look mostly great, but I noticed a glaring fault in your architecture which is both visually offputting and - more importantly - ABSOLUTELY NONSENSICAL. Take a look at these collunms, arcs and windows: Notice how in both pictures the window and the collunm stand below the same part of the arc? This is where the load of the arc gets transfered to the element below it - most of the time that element is a colunm. A window, however, is the diametric opposite of such a load-bearing vertical element. A window is a great structural weakness which should absolutely NOT be at that spot below the arc! I edited a picture to show how this should look: Trust me, I am normally not prone to pointing flaws out in such an annoying way. But this is a quiet grave mistake and I implore you to fix this if this is still possible. You‘d only have to move a few already existing assets a few meters. Please Paradox, hear my plea!

## Reply 67 — participant_044 · 2021-11-30 · post-27933946

Shouldn't the floor around the throne itself be elevated with some small steps to make it more "grand and looking at others from above"? Or is it just common trope in the movies?

## Reply 68 — participant_045 · 2021-11-30 · post-27933956

is it possible to introduce by modding courts to lower noble ranks?

## Reply 69 — participant_046 · 2021-11-30 · post-27934026

Is the last buggy image the court of the Red Queen?

## Reply 70 — participant_047 · 2021-11-30 · post-27934138

Will we have the option to keep someone's skull when we have them executed, if they're a rival or something? I'd like to adorn my royal court with enemies' skulls; chicks dig that, I think?

## Reply 71 — participant_048 · 2021-11-30 · post-27934231

Looks great and I look forward to the courts and the culture mechanics. I do have to second the disdain for the European Red and White Wavy pattern. If it was tied some how to your title COA maybe then it may look better. If you want a plaster wall then just a beige-ish or white would be good I’d think.

## Reply 72 — participant_038 · 2021-11-30 · post-27934317

Looks great. My only criticism would be that the courts look too grand for the amount of people in them. There seems to be too few people for too fancy courts. I base this on hollywood and imagination not history. It sort of gives the impression of people lingering after a court session rather than something important going on.

## Reply 73 — participant_034 · 2021-11-30 · post-27934493

Thinking about some possible teasers for tiding us over to the new year. I really enjoyed seeing the screenshots of the culture and court language maps from in progress games and how they evolved over time. Would love to see more of that between now and the release.

## Reply 74 — participant_049 · 2021-11-30 · post-27934497

The camera angle looks still a bit awkward - it focuses on the fore end of the court, not the back end where the throne is - seems counterintuitive for a throne room - and unlike some of the prototype angles, it shows a great deal of floor, which is not a very natural human perspective. Any chance the camera could be dropped down a bit, tilted a hint up, and zoomed in just slight amount?

## Reply 75 — participant_050 · 2021-12-01 · post-27934565

<!-- artifact:quote:start -->
> MirrorMonkey2 said: Hello Paradox! Architecture student here. The throne rooms look mostly great, but I noticed a glaring fault in your architecture which is both visually offputting and - more importantly - ABSOLUTELY NONSENSICAL. Take a look at these collunms, arcs and windows: View attachment 780866 View attachment 780867 Notice how in both pictures the window and the collunm stand below the same part of the arc? This is where the load of the arc gets transfered to the element below it - most of the time that element is a colunm. A window, however, is the diametric opposite of such a load-bearing vertical element. A window is a great structural weakness which should absolutely NOT be at that spot below the arc! I edited a picture to show how this should look: View attachment 780869 Trust me, I am normally not prone to pointing flaws out in such an annoying way. But this is a quiet grave mistake and I implore you to fix this if this is still possible. You‘d only have to move a few already existing assets a few meters. Please Paradox, hear my plea! Click to expand...
<!-- artifact:quote:end -->
mannerism arrived early in ck3world. it's fine

## Reply 76 — participant_051 · 2021-12-01 · post-27934567

It would make sense if the ruler and spouse personality added variance to the general tone, feeling, and lightning of the court room

## Reply 77 — participant_052 · 2021-12-01 · post-27934608

This looks awesome. Can we please get full customization in the future? And not only for court room variants, but especially for picking the color of our character’s clothing. If you guys can do a coat of arms editor as great as the one you showed us, I have total confidence that you can make this possible. Picking colors relates to the very identity of our kingdom and dynasty, and to me it’s an essential customization feature, especially when playing with mods such as Game of Thrones where house colors are a massive deal.

## Reply 78 — participant_053 · 2021-12-01 · post-27934707

What is the difference (variation) between sicilian and byzantine courts? I don't see it. We will see 12 versions of courts (4 types with 3 variants each). It will by loss if 2 are the same Edit: typo

## Reply 79 — participant_054 · 2021-12-01 · post-27934860

<!-- artifact:quote:start -->
> Ksiendzu said: What is the difference (variation) between sicilian and byzantine courts? I don't see it. We will see 12 versions of courts (4 types with 3 variants each). It will by loss if 2 are the same Edit: typo Click to expand...
<!-- artifact:quote:end -->
I too could not detect a difference except furniture.

## Reply 80 — participant_054 · 2021-12-01 · post-27934862

I continue to love what I see with the royal courts. I have hope that the devs will revisit these with additional courts by major cultural areas. I would also like to see differences by by technological era. For example, I wouldn’t expect to see many differences for a Byzantine court by technological era, but I would expect a tribal era royal court in England to differ from a late middle age era court there.

## Reply 81 — participant_043 · 2021-12-01 · post-27935089

<!-- artifact:quote:start -->
> prismaticmarcus said: mannerism arrived early in ck3world. it's fine Click to expand...
<!-- artifact:quote:end -->
Haha yeah I was thinking about adding thst from the Renaissance onward such breaks in style were sometimes willfully done^^ But I concluded that I don‘t have to annoy the forum with any more architectural annecdotes Funny that you brought it up!

## Reply 82 — participant_055 · 2021-12-01 · post-27935208

PARTY HARD TY for the diary!

## Reply 83 — participant_050 · 2021-12-01 · post-27935213

<!-- artifact:quote:start -->
> MasterKaramba said: PARTY HARD View attachment 781130 TY for the diary! Click to expand...
<!-- artifact:quote:end -->
whoa! get down!

## Reply 84 — participant_022 · 2021-12-01 · post-27935233

<!-- artifact:quote:start -->
> VenetianPriest said: For example, I wouldn’t expect to see many differences for a Byzantine court by technological era, but I would expect a tribal era royal court in England to differ from a late middle age era court there. Click to expand...
<!-- artifact:quote:end -->
Indeed - wouldn’t an Anglo-Saxon court in the style of a mead-hall be something to see (think Meduseld, the hall of Theoden, in Lord of the Rings)!

## Reply 85 — participant_032 · 2021-12-01 · post-27935315

<!-- artifact:quote:start -->
> WestuHal said: Indeed - wouldn’t an Anglo-Saxon court in the style of a mead-hall be something to see (think Meduseld, the hall of Theoden, in Lord of the Rings)! Click to expand...
<!-- artifact:quote:end -->
Mead halls aren't what a ruler with great prestige would build as their royal court. You have that mental picture of it because the Anglo-Saxons didn't really build castles, and they moved around a lot to different manors in the kingdom to see to every vassal. Because this Royal Court feature is borrowing elements from 14th-century European courts that was stationary and tied to the capital (a foreign concept in 867 and 1066 for the Anglo-Saxons), the Anglo-Saxon court would also be grander had they had the opportunity to centralise the authority to that degree.

## Reply 86 — participant_056 · 2021-12-01 · post-27935329

Looks very nice! And also interesting to see the range of stuff taken into consideration. One thing I'm curious about: have you looked at how people stood and moved in the eras covered? There's not a huge amount known, but things like living history, art, dance instructions and fighting treatises have given some insight (which have been written about).

## Reply 87 — participant_057 · 2021-12-01 · post-27935583

<!-- artifact:quote:start -->
> Carlberg said: Bad wording on my part, we dont have any outdoor courts in Royal Court. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Kiffe said: I know it's probably too late for suggestions, but i think it would be really fucking cool if you made models for cats and dogs and had them appear on the court of a ruler that owns one. Maybe even make different regional variants. That would also help pave the way for when we inevitably get glitterhoof as a councillor. Just a thought, cause I understand this is probably very low on a list of priorities. Click to expand...
<!-- artifact:quote:end -->
I notice you don't say it can't be done. Only that there isn't one in the DLC. Not that I expect any to be made in a long time, getting the background looking right if there's an open view instead of the walls of a room sounds like a lot of work. I really like this idea. Pets as part of a flavour pack? Seeing them walk around in the court rooms, more events, regional variants of cats & dogs etc etc.

## Reply 88 — participant_058 · 2021-12-01 · post-27935584

Looks amazing

## Reply 89 — participant_053 · 2021-12-01 · post-27935690

I had to. Sorry for poor quality.

## Reply 90 — participant_050 · 2021-12-01 · post-27935720

<!-- artifact:quote:start -->
> MrButtermancer said: ...it's just incredibly depressing that despite all this the outcome is substantially worse than just the oil painting backdrops. This should have its picture next to "uncanny valley phenomenon" in the dictionary. The rooms are bizarrely clean and symmetrical. There has never been a room like this where people live, anywhere. There's no clutter and little furniture. Everything's at 90 degree angles. There are not enough chairs. There's a friggin' cup on a dresser alone in the actual middle of the room. I don't care if, "but muh artifacts." These people live like space aliens. I just spent ten minutes on a Google image adventure of reconstructed throne rooms because I didn't think it could possibly be as bad as I think it is. It's worse than I thought it was. The concept art spoofs are not bad, being primarily smaller, busier, and darker, but it looks like they raised the roofs weirdly high and turned the light up, probably for long shot camera angle purposes and it makes the rooms look like... well, something somebody made with a computer to be a room in a video game. I would bet the undoubtedly short, stiff, not-motion-captured animation loops likely without walking, likely never interacting with furniture, drink, or food, will drive this to 11. 3D models in theatre poses were a great idea and really show off the clothes and models, while still remaining exactly abstracted enough not to appear artificial. They're like actors on a stage and it's pretty easy to accept the essential conceit without losing anything. This is no longer abstracted. To make this not look like dookie you'd basically have to motion-capture an entire group of actors milling about, talking, drinking, laughing, etc, on rooms basically superimposed over existing courts because it's obvious ET did the feng shui with a laser ruler and cannot be trusted to place virtual objects by hand in a room humans are ostensibly inhabiting. Put a flippin' cup on a dresser in the middle of a room. If I had an envoy tell me this is what they witnessed, I'd go on a humanitarian mission to bring civilization to these poor souls, and failing that, send armies to destroy the barbarians. I'd appeal to the pope. I'd declare a Crusade. Click to expand...
<!-- artifact:quote:end -->
it's the throne room. people don't live in it.

## Reply 91 — participant_059 · 2021-12-01 · post-27935792

I'm not sure about putting your priceless Ming vase in the middle of a room full of people, but I imagine it's too late to move artifacts closer to the wall

## Reply 92 — participant_032 · 2021-12-01 · post-27935878

I don't get the artifact display p*rn either.

## Reply 93 — participant_056 · 2021-12-01 · post-27935880

<!-- artifact:quote:start -->
> Ksiendzu said: I had to. Sorry for poor quality. View attachment 781198 Click to expand...
<!-- artifact:quote:end -->
Huh? They're clearly different pictures. I mean, fair enough if you are just not people-focussed, but even the furniture is different.

## Reply 94 — participant_053 · 2021-12-01 · post-27935969

<!-- artifact:quote:start -->
> Balesir said: Huh? They're clearly different pictures. I mean, fair enough if you are just not people-focussed, but even the furniture is different. Click to expand...
<!-- artifact:quote:end -->
Furniture depends mostly on grandeur level. Compare differences between other varinants of the same type to differences between these two. These two mediterranean court variants are the same sadly

## Reply 95 — participant_060 · 2021-12-01 · post-27936075

<!-- artifact:quote:start -->
> Ksiendzu said: I had to. Sorry for poor quality. View attachment 781198 Click to expand...
<!-- artifact:quote:end -->
Way to copy the exact same post I made 3 weeks ago (and poorly for that matter). Good on you mate!

## Reply 96 — participant_037 · 2021-12-01 · post-27936126

<!-- artifact:quote:start -->
> jmpnjkrbbt said: Way to copy the exact same post I made 3 weeks ago (and poorly for that matter). Good on you mate! Click to expand...
<!-- artifact:quote:end -->
*(no text body — reaction-only or media-only post)*

## Reply 97 — participant_061 · 2021-12-01 · post-27936351

I'm totally not into the idea of the 3D throne room. For me, it looks like a waiting room for some generic "second life" like MMORPG from the time when they tried to put 3D into absolutely everything even if it didn't make sense. But it's not the fault of the devs, it's just impossible to cover all the court fantasies that the player have. Sometimes less is simply more and simpler measures work better in the end while keeping some things to the imagination of the players. That saying, all the new systems sound great, so I won't be complaining too much.

## Reply 98 — participant_062 · 2021-12-02 · post-27936780

I can already imagine how depreciated the throne room is going to be a few expansions from now.

## Reply 99 — participant_063 · 2021-12-02 · post-27936905

<!-- artifact:quote:start -->
> Ksiendzu said: What is the difference (variation) between sicilian and byzantine courts? I don't see it. Click to expand...
<!-- artifact:quote:end -->
The only difference I spot (that isn't furniture related) is the Byzantines have the dark rectangles on the wall with an intricate pattern on them, the Sicilians don't have these. These rectangles are definitely part of the wall/court design and not a decoration as you can see the banner further down the wall partly covers one of these rectangles.

## Reply 100 — participant_053 · 2021-12-02 · post-27936968

<!-- artifact:quote:start -->
> pengoyo said: The only difference I spot (that isn't furniture related) is the Byzantines have the dark rectangles on the wall with an intricate pattern on them, the Sicilians don't have these. These rectangles are definitely part of the wall/court design and not a decoration as you can see the banner further down the wall partly covers one of these rectangles. Click to expand...
<!-- artifact:quote:end -->
Maybe it's connected to grandeur level - better looking walls.

## Reply 101 — participant_064 · 2021-12-02 · post-27936995

Nice features! Will you add also primitive viking throne rooms, primitive african subsaarian, primitive desert nomad and primitive steppe nomads too ?

## Reply 102 — participant_063 · 2021-12-02 · post-27937060

<!-- artifact:quote:start -->
> Ksiendzu said: Maybe it's connected to grandeur level - better looking walls. Click to expand...
<!-- artifact:quote:end -->
Maybe, but I don't think so. I think grandeur just adds more items to the room and gets rid of the wear and tear on the wall. Grandeur doesn't seem to change the actual wall design. Plus something like them is also in wall concept art, which I take to mean that this was something that was there from the start.

## Reply 103 — participant_065 · 2021-12-02 · post-27937157

<!-- artifact:quote:start -->
> Prometheus_1 said: Nice features! Will you add also primitive viking throne rooms, primitive african subsaarian, primitive desert nomad and primitive steppe nomads too ? Click to expand...
<!-- artifact:quote:end -->
Why do you keep calling those large swaths of cultures primitive when they weren't?

## Reply 104 — participant_066 · 2021-12-02 · post-27937209

Damn the lighting looks beautiful, but the models dont have shadows.

## Reply 105 — participant_067 · 2021-12-02 · post-27937274

The different courts look great! Love the art in this

## Reply 106 — participant_053 · 2021-12-02 · post-27937291

<!-- artifact:quote:start -->
> pengoyo said: Maybe, but I don't think so. I think grandeur just adds more items to the room and gets rid of the wear and tear on the wall. Grandeur doesn't seem to change the actual wall design. Plus something like them is also in wall concept art, which I take to mean that this was something that was there from the start. Click to expand...
<!-- artifact:quote:end -->
They still look almost identical (that's only one difference)

## Reply 107 — participant_056 · 2021-12-02 · post-27937584

Actually, one criticism of the northern European rooms is the bare masonry walls. Even a relatively poor lord should ba able to afford a lick of paint - which was common in medieval castles (see here for examples in reproduction).

## Reply 108 — participant_011 · 2021-12-02 · post-27937639

<!-- artifact:quote:start -->
> MrButtermancer said: Welcome to active play's first loading screen. Yuck. Click to expand...
<!-- artifact:quote:end -->
Please don't presume to know it in advance. Your statement is not true. Even on extreme low-spec machines it'll take 2-3 frames to give you a complete scene picture.

## Reply 109 — participant_068 · 2021-12-02 · post-27938869

I have only one ask for CK3 and that is for there to be a "Homosexuality Encouraged" doctrine

## Reply 110 — participant_069 · 2021-12-02 · post-27939085

Not enough steps under the throne

## Reply 111 — participant_070 · 2021-12-03 · post-27939300

Will we be able to put portraits/busts/statues of the great leaders in our family history in our throne room?

## Reply 112 — participant_071 · 2021-12-03 · post-27940303

<!-- artifact:quote:start -->
> MrButtermancer said: ...it's just incredibly depressing that despite all this the outcome is substantially worse than just the oil painting backdrops. This should have its picture next to "uncanny valley phenomenon" in the dictionary. The rooms are bizarrely clean and symmetrical. There has never been a room like this where people live, anywhere. There's no clutter and little furniture. Everything's at 90 degree angles. There are not enough chairs. There's a friggin' cup on a dresser alone in the actual middle of the room. I don't care if, "but muh artifacts." These people live like space aliens. I just spent ten minutes on a Google image adventure of reconstructed throne rooms because I didn't think it could possibly be as bad as I think it is. It's worse than I thought it was. The concept art spoofs are not bad, being primarily smaller, busier, and darker, but it looks like they raised the roofs weirdly high and turned the light up, probably for long shot camera angle purposes and it makes the rooms look like... well, something somebody made with a computer to be a room in a video game. I would bet the undoubtedly short, stiff, not-motion-captured animation loops likely without walking, likely never interacting with furniture, drink, or food, will drive this to 11. 3D models in theatre poses were a great idea and really show off the clothes and models, while still remaining exactly abstracted enough not to appear artificial. They're like actors on a stage and it's pretty easy to accept the essential conceit without losing anything. This is no longer abstracted. To make this not look like dookie you'd basically have to motion-capture an entire group of actors milling about, talking, drinking, laughing, etc, on rooms basically superimposed over existing courts because it's obvious ET did the feng shui with a laser ruler and cannot be trusted to place virtual objects by hand in a room humans are ostensibly inhabiting. Put a flippin' cup on a dresser in the middle of a room. If I had an envoy tell me this is what they witnessed, I'd go on a humanitarian mission to bring civilization to these poor souls, and failing that, send armies to destroy the barbarians. I'd appeal to the pope. I'd declare a Crusade. Click to expand...
<!-- artifact:quote:end -->
You raise some good points, I don't see why the artifacts couldn't be closer to the walls and more chairs added. The camera angle certainly needs a change, though I will say that I don't find the courts as badly-done as you appear to be, it just needs changes. The Byzantine and Norman courts are the most aesthetically pleasing. I honestly don't know what is going on in the wooden western European court room, the Stone one is pretty good though.

## Reply 113 — participant_056 · 2021-12-03 · post-27940387

<!-- artifact:quote:start -->
> Tomray94 said: You raise some good points, I don't see why the artifacts couldn't be closer to the walls and more chairs added. The camera angle certainly needs a change, though I will say that I don't find the courts as badly-done as you appear to be, it just needs changes. Click to expand...
<!-- artifact:quote:end -->
Maybe because chairs are really not a thing seen generally in the medieval period? A throne for the lord - or even a chair that would be disassembled and carried around with him - is a possibility, but most folks sat on stools or benches.

## Reply 114 — participant_071 · 2021-12-03 · post-27940544

<!-- artifact:quote:start -->
> Balesir said: Maybe because chairs are really not a thing seen generally in the medieval period? A throne for the lord - or even a chair that would be disassembled and carried around with him - is a possibility, but most folks sat on stools or benches. Click to expand...
<!-- artifact:quote:end -->
I did not mean chairs as chairs, I meant seats of some kind. I understand that we all implicitly agree to use English when speaking in these specific parts of the forums, but many people here do not speak it as a first language and often may use the English equivalent for a word which has expanded meanings in their own language but very specific ones in this one. That is precisely what occurred here, be a little lenient.

## Reply 115 — participant_072 · 2021-12-03 · post-27940625

<!-- artifact:quote:start -->
> Tomray94 said: I did not mean chairs as chairs, I meant seats of some kind. I understand that we all implicitly agree to use English when speaking in these specific parts of the forums, but many people here do not speak it as a first language and often may use the English equivalent for a word which has expanded meanings in their own language but very specific ones in this one. That is precisely what occurred here, be a little lenient. Click to expand...
<!-- artifact:quote:end -->
Your English is essentially perfect, and I'd never have known it was a second language for you. I think "seats" or "seating" is the generic word for this situation, for the little that it matters. That said, seating for the rest of the court would be **rare**. You were generally expected to stand in the formal space of a court, since sitting in the presence of a king was a rare privilege, especially when the king is (as it were) on formal display. But that's excessively picky of me.

## Reply 116 — participant_071 · 2021-12-03 · post-27940749

<!-- artifact:quote:start -->
> DreadLindwyrm said: Your English is essentially perfect, and I'd never have known it was a second language for you. I think "seats" or "seating" is the generic word for this situation, for the little that it matters. That said, seating for the rest of the court would be **rare**. You were generally expected to stand in the formal space of a court, since sitting in the presence of a king was a rare privilege, especially when the king is (as it were) on formal display. But that's excessively picky of me. Click to expand...
<!-- artifact:quote:end -->
I thank you for your kind words! I do not mind the corrections, I only felt the need to clarify my point.

## Reply 117 — participant_050 · 2021-12-03 · post-27940776

<!-- artifact:quote:start -->
> DreadLindwyrm said: I think "seats" or "seating" is the generic word for this situation, for the little that it matters. Click to expand...
<!-- artifact:quote:end -->
i think seats don't have backs to them. that's what makes them seats, generally speaking.

## Reply 118 — participant_056 · 2021-12-03 · post-27940869

<!-- artifact:quote:start -->
> prismaticmarcus said: i think seats don't have backs to them. that's what makes them seats, generally speaking. Click to expand...
<!-- artifact:quote:end -->
No, a chair is a type of seat, so @Tomray94 was exactly right in his or her clarification.

## Reply 119 — participant_050 · 2021-12-03 · post-27940941

<!-- artifact:quote:start -->
> Balesir said: No, a chair is a type of seat, so @Tomray94 was exactly right in his or her clarification. Click to expand...
<!-- artifact:quote:end -->
chairs and seats are both types of seating,

## Reply 120 — participant_056 · 2021-12-03 · post-27941284

<!-- artifact:quote:start -->
> prismaticmarcus said: chairs and seats are both types of seating, Click to expand...
<!-- artifact:quote:end -->
That is true, but if you 'take your seat', it might be a chair that you sit in...

## Reply 121 — participant_072 · 2021-12-03 · post-27941328

<!-- artifact:quote:start -->
> prismaticmarcus said: i think seats don't have backs to them. that's what makes them seats, generally speaking. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> prismaticmarcus said: chairs and seats are both types of seating, Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Balesir said: That is true, but if you 'take your seat', it might be a chair that you sit in... Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> A seat is a place to sit. The term may encompass additional features, such as back, armrest, head restraint Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> A place in which to sit. Click to expand...
<!-- artifact:quote:end -->
I hit wikipedia for a definition. https://en.wikipedia.org/wiki/Seat Wiktionary then concurs as So whilst a back *can* be part of a seat it doesn't have to be. Stools and benches are included in the broader category of "seats", but so are armchairs, thrones, and chairs.

## Reply 122 — participant_064 · 2021-12-04 · post-27941516

<!-- artifact:quote:start -->
> monkey1998 said: Why do you keep calling those large swaths of cultures primitive when they weren't? Click to expand...
<!-- artifact:quote:end -->
Because were more primitive and technologically backward compared to others?

## Reply 123 — participant_073 · 2021-12-04 · post-27941548

I hope this doesn't just turn into a 3d menu where it takes longer to navigate over a text box.

## Reply 124 — participant_056 · 2021-12-04 · post-27942158

<!-- artifact:quote:start -->
> Prometheus_1 said: Because were more primitive and technologically backward compared to others? Click to expand...
<!-- artifact:quote:end -->
Compared to what? Compared to contemporary courts elsewhere in the area covered by the game it's not true, with the possible esception of Byzantium. The steppelands were arguably less economically developed, but even that's not true around the silk road routes. Sub-saharan Africa didn't start to fall behind until the economic damage of the 17th/18th century gold and slave trade kicked in.

## Reply 125 — participant_074 · 2021-12-04 · post-27942800

I know this has been beaten to death by now, but I also want to see the Bighead (or maybe even headless) bug come back, as a console command or something. Or maybe when your character is a lunatic, other characters might sometimes have grossly distorted faces or facial features.

## Reply 126 — participant_064 · 2021-12-04 · post-27943237

<!-- artifact:quote:start -->
> Balesir said: Compared to what? Compared to contemporary courts elsewhere in the area covered by the game it's not true, with the possible esception of Byzantium. The steppelands were arguably less economically developed, but even that's not true around the silk road routes. Sub-saharan Africa didn't start to fall behind until the economic damage of the 17th/18th century gold and slave trade kicked in. Click to expand...
<!-- artifact:quote:end -->
That is not historically true for what I have studied in history classes , but please prove with some sources that those societies where equally technologically advanced and culturaly sophisticated as Venice, Byzanthium, al Andalus , China etc? On most aspect those societies where far backward technologically compared to european powers , middle east, india or China.

## Reply 127 — participant_056 · 2021-12-05 · post-27943850

<!-- artifact:quote:start -->
> Prometheus_1 said: That is not historically true for what I have studied in history classes , but please prove with some sources that those societies where equally advanced and culturaly developed as Venice, Byzanthium, al Andalus , China etc? On most aspect those societies where far backward technologically compared to european powers , middle east, india or China. Click to expand...
<!-- artifact:quote:end -->
The demand that others disprove your assertions is both arrogant and impractical. The people of West Africa had sophisticated clothworking and metalworking as well as reasonably large buildings and agricultural works; what specific technological areas did you have in mind? How were the people of West Africa significantly 'behind' those of further north? Bearing in mind, especially, that Christian Europe was behind the Muslim middle east.

## Reply 128 — participant_050 · 2021-12-05 · post-27943857

<!-- artifact:quote:start -->
> Prometheus_1 said: That is not historically true for what I have studied in history classes , but please prove with some sources that those societies where equally advanced and culturaly developed as Venice, Byzanthium, al Andalus , China etc? On most aspect those societies where far backward technologically compared to european powers , middle east, india or China. Click to expand...
<!-- artifact:quote:end -->
you're confusing technology with cultural development. if the measure of success of a culture is its lifespan, then australian aborigines still win today.

## Reply 129 — participant_034 · 2021-12-05 · post-27944518

<!-- artifact:quote:start -->
> Prometheus_1 said: That is not historically true for what I have studied in history classes , but please prove with some sources that those societies where equally advanced and culturaly developed as Venice, Byzanthium, al Andalus , China etc? On most aspect those societies where far backward technologically compared to european powers , middle east, india or China. Click to expand...
<!-- artifact:quote:end -->
"Culturally developed" oof. There was really no more "advanced" in cultural terms of things like storytelling style, music, artistic expression, or architecture. Especially since we're talking about court art and architectural styles since that's the part relevant to the game. West Africa, Ethiopia, the Central Asian steppes, Scandinavia, all certainly had different and unique art and architecture that would be cool to have represented in a royal court depiction.

## Reply 130 — participant_064 · 2021-12-06 · post-27945024

<!-- artifact:quote:start -->
> Balesir said: The demand that others disprove your assertions is both arrogant and impractical. The people of West Africa had sophisticated clothworking and metalworking as well as reasonably large buildings and agricultural works; what specific technological areas did you have in mind? How were the people of West Africa significantly 'behind' those of further north? Bearing in mind, especially, that Christian Europe was behind the Muslim middle east. Click to expand...
<!-- artifact:quote:end -->
Perhaps first try to read original posts better ! Then I have mentioned both nomadic and more backward societies , Not all societies were equally advanced and saying that vikings or berber tribes were less technologically advanced than others is neither arrogance neither bias , just factual evidence liking it or not. If you have different information from what is certified and asserted by most academic sources be my guest then and show us how a nomadic tribe from deserts of Sahar or a viking settlement from norway was more technologically advanced and culturally more evoluted than the courts of the Chineese or Byzantine emperors in the same timeframe. By technological advancements you might want to include technologies used and by culture advances the sofistication and depth reached. My affirmations do not neglect the presence of cultures and technological achievements by those cultures infact I asked for a representation of those too and not beeing limited only to the most advanced ones. Perhaps you think that those other cultures don't deserve represenration ?

## Reply 131 — participant_064 · 2021-12-06 · post-27945052

<!-- artifact:quote:start -->
> wilcoxchar said: "Culturally developed" oof. There was really no more "advanced" in cultural terms of things like storytelling style, music, artistic expression, or architecture. Especially since we're talking about court art and architectural styles since that's the part relevant to the game. West Africa, Ethiopia, the Central Asian steppes, Scandinavia, all certainly had different and unique art and architecture that would be cool to have represented in a royal court depiction. Click to expand...
<!-- artifact:quote:end -->
That is exactly what I asked for before someone started to debate with a certain amount of bias that all cultures where equally advanced and that I could't write that some where less technologically advanced and backward compared to others. This is historically untrue .

## Reply 132 — participant_064 · 2021-12-06 · post-27945061

<!-- artifact:quote:start -->
> prismaticmarcus said: you're confusing technology with cultural development. if the measure of success of a culture is its lifespan, then australian aborigines still win today. Click to expand...
<!-- artifact:quote:end -->
No I mentioned both and societies had also deeper or simplier levels of sofistication for cultures... some had long oral traditions while others centuries of written documentation and its fair to affirm some are more sophisticated and evoluted than others culturally speaking, technologically too we can distinguish societies with a fair degree of different level of advancements. To say that some where more backward is not to be interpreted as an offense or else but just as a matter of facts which doesnt mean that a culture is to be considered inferior to another! I just write that both deserve to be represented ingame... I endorse the representation of a nomad warlord throneroom may be under a tent or a viking lord in a longhouse rather than a castle.

## Reply 133 — participant_034 · 2021-12-06 · post-27945084

<!-- artifact:quote:start -->
> Prometheus_1 said: That is exactly what I asked for before someone started to debate with a certain amount of bias that all cultures where equally advanced and that I could't write that some where less technologically advanced and backward compared to others. This is historically untrue . Click to expand...
<!-- artifact:quote:end -->
Yes, I saw your original post. People are correctly calling out your bias because you were being biased and unnecessarily condescending, calling such cultures "primitive" and implying those cultures' artistic styles were somehow inferior. If you were really wanting those cultures to have distinct court styles in the game, you shouldn't have been disrespectful toward the cultures, since it made it sound like you were being sarcastic or didn't really want them added since calling them "primitive" betrayed what you really thought of those cultures.

## Reply 134 — participant_050 · 2021-12-06 · post-27945304

<!-- artifact:quote:start -->
> Prometheus_1 said: To say that some where more backward is not to be interpreted as an offense Click to expand...
<!-- artifact:quote:end -->
then stop using the word 'backward.' i think you've found that it does cause offence.

## Reply 135 — participant_056 · 2021-12-06 · post-27945755

<!-- artifact:quote:start -->
> Prometheus_1 said: Perhaps first try to read original posts better ! Then I have mentioned both nomadic and more backward societies , Not all societies were equally advanced and saying that vikings or berber tribes were less technologically advanced than others is neither arrogance neither bias , just factual evidence liking it or not. If you have different information from what is certified and asserted by most academic sources be my guest then and show us how a nomadic tribe from deserts of Sahar or a viking settlement from norway was more technologically advanced and culturally more evoluted than the courts of the Chineese or Byzantine emperors in the same timeframe. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Prometheus_1 said: Nice features! Will you add also primitive viking throne rooms, primitive african subsaarian, primitive desert nomad and primitive steppe nomads too ? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Prometheus_1 said: By technological advancements you might want to include technologies used and by culture advances the sofistication and depth reached. My affirmations do not neglect the presence of cultures and technological achievements by those cultures infact I asked for a representation of those too and not beeing limited only to the most advanced ones. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Prometheus_1 said: Perhaps you think that those other cultures don't deserve represenration ? Click to expand...
<!-- artifact:quote:end -->
Now you are egregiously trying to worm out of the situation instead of accepting criticism with good grace, and that's just irritating. For illustration, here: So, let's just look at the post I was responding to, shall we? So, which of the four that you explicitly called "primitive" there was I suppose to be not assuming you were calling "primitive"? Check out the actual technologies of the time period we are talking about. The arabs, turks, persians and berbers had the most sophisticated ceramics for almost all of the medieval period. Medieval Islamic plates and tiles were (and still are) absolutely stunning. Take a look at West African clothwork; it was used as currency in the region and was the start of a tradition that has lasted until the present day. Look at Scythian metalworking and leatherwork (what little survives). Have you ever seen a 'viking' (early medieval Scandinavian) pattern-welded sword? Both original swords, generally in corroded condition, and stunning reproductions are available in museums and private collections. If we were talking about later periods, you might begin to have a point - but in the early medieval period your assertions/assumptions are just plain wrong. Yes, I absolutely do think they should be represented - that was why I actually liked your original post! The post was a good suggestion, but flawed by a misapprehension that you have made far worse than it originally was by doubling down on your errors for no discernible reason, as far as I can see. Note, however, that doing those courts justice will take a lot of work by the artists involved. I think they would absolutely make a good job of it, but not in time for this particular release! It will take time.

## Reply 136 — participant_071 · 2021-12-06 · post-27946808

<!-- artifact:quote:start -->
> Prometheus_1 said: Perhaps first try to read original posts better ! Then I have mentioned both nomadic and more backward societies , Not all societies were equally advanced and saying that vikings or berber tribes were less technologically advanced than others is neither arrogance neither bias , just factual evidence liking it or not. If you have different information from what is certified and asserted by most academic sources be my guest then and show us how a nomadic tribe from deserts of Sahar or a viking settlement from norway was more technologically advanced and culturally more evoluted than the courts of the Chineese or Byzantine emperors in the same timeframe. By technological advancements you might want to include technologies used and by culture advances the sofistication and depth reached. My affirmations do not neglect the presence of cultures and technological achievements by those cultures infact I asked for a representation of those too and not beeing limited only to the most advanced ones. Perhaps you think that those other cultures don't deserve represenration ? Click to expand...
<!-- artifact:quote:end -->
I won't comment on the rest of the claims you've made in this conversation, since others have tackled them quite well I'd say, but I would like to point out how you sneakily switch between technological and cultural advancement whenever the situation suits your points. When it comes to technology, 80% of the counties on the existing map were essentially on the same foot. Sure, rural villages around Orleans weren't on the level of Paris, but roughly the same sorts of technologies were used in both places. The only exceptions to this rule would be the Baltic, some desert tribes in Arabia and Africa, the northernmost areas of modern day Sweden, Denmark, Finland and Siberia. Despite that, all of these areas are appropriately represented as being on the "tribal era" of technological advancement in-game, so what you are saying there is already acknowledged. Culturally, most of the places on the map were neither inferior nor superior to each other, they were merely different in aesthetics. traditions and culture compared to other areas. The bad-faith element in your arguments is that when someone comes and collapses your cultural superiority arguments, you immediately start introducing the technological dimension. That is all I seek to point out here.

## Reply 137 — participant_075 · 2021-12-07 · post-27948341

One question: Coronation Decision, will it happen?

## Reply 138 — participant_033 · 2021-12-07 · post-27948350

<!-- artifact:quote:start -->
> GurlCatEars said: One question: Coronation Decision, will it happen? Click to expand...
<!-- artifact:quote:end -->
Obviously not in this dlc, or they would've told about it already

## Reply 139 — participant_076 · 2021-12-09 · post-27953082

Now that cultures are being greatly reworked and not everyone in the same culture group needs to have the same everything, would it be possible to add more asthetics/architectures to the game? Right now we have cities in Scotland looking identical to those in Romania and it feels off.

## Reply 140 — participant_077 · 2021-12-09 · post-27953157

By that argument, Carcassonne shouldn't have the same architecture as Byzanople

## Reply 141 — participant_034 · 2021-12-10 · post-27953911

<!-- artifact:quote:start -->
> grommile said: By that argument, Carcassonne shouldn't have the same architecture as Byzanople Click to expand...
<!-- artifact:quote:end -->
Same with Santiago de Compostela and Inverness, or Krakow and Iceland.

## Reply 142 — participant_071 · 2021-12-10 · post-27954328

<!-- artifact:quote:start -->
> Bandua_of_Gallaecia said: Now that cultures are being greatly reworked and not everyone in the same culture group needs to have the same everything, would it be possible to add more asthetics/architectures to the game? Right now we have cities in Scotland looking identical to those in Romania and it feels off. View attachment 784511 Click to expand...
<!-- artifact:quote:end -->
Good idea, Though I'd probably shift Poland to Eastern. I'll admit I have not been there, but as far as I can tell, Northern-Style Buildings only exist in the north and were built later by the Teutonic Order. Any Poles here feel free to correct me if I am wrong. You could also reduce Mediterranean to only include Aragon from Spain and Occitania to join the Continental style, even if it may have certain Mediterranean characteristics. The most obvious issue with this, as pointed out by others above, is that most of these places had many different styles of architecture within them.

## Reply 143 — participant_076 · 2021-12-10 · post-27954470

<!-- artifact:quote:start -->
> Tomray94 said: Good idea, Though I'd probably shift Poland to Eastern. I'll admit I have not been there, but as far as I can tell, Northern-Style Buildings only exist in the north and were built later by the Teutonic Order. Any Poles here feel free to correct me if I am wrong. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> You could also reduce Mediterranean to only include Aragon from Spain and Occitania to join the Continental style, even if it may have certain Mediterranean characteristics. The most obvious issue with this, as pointed out by others above, is that most of these places had many different styles of architecture within them. Click to expand...
<!-- artifact:quote:end -->
For "Northern" i used the BrickGothic style, which is found in Poland, however, like you mentioned indeed this is mostly in the north and west, and built mostly by the teutonic order, so you certainly have a point there. Aragonese and Catalan should share the same style as Occitania. Castile should also have a Medditerranean style (Leonese too, the only reason why i included Asturleonese with Atlantic was because of Asturias). Architecture is heavily impacted by the soil type, even more so than by cultural trends. As you can see in this map of the Stone-types in Europe: In Orange, you can find light coloured rocks such as limestone (white) and sandstone (light orange and yellow). In Red you can find dark-coloured rocks such as granite (A mix of silvery, brown and black pigments) and xist (Greyish dark brown). In Green you can find loose sediments such as clay and gravel, which are poor for construction, so these areas usually built with clay or wood instead. The Asturleonese culture is pretty much divided with the Asturian part having vulcanic rocks like Galician, and the Leonese part having sedimentary rocks like Castilian. If it's not asking too much i would also split Mediterranean into 2 different sets: Eastern/Orthodox Mediterranean (Byzantine, Bulgarian, maybe South Italian) And Western/Catholic Mediterranean (Italian, Occitan, East-Iberian)

## Reply 144 — participant_076 · 2021-12-10 · post-27954497

<!-- artifact:quote:start -->
> grommile said: By that argument, Carcassonne shouldn't have the same architecture as Byzanople Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> wilcoxchar said: Same with Santiago de Compostela and Inverness, or Krakow and Iceland. Click to expand...
<!-- artifact:quote:end -->
Well, we could go around picking outliers all day long, its not like every culture only built every town, castle and temple to look exactly the same. At least the pictures i chose in my sketch fit as a normal type of structures you can find everywhere in Ocitania/Greece, Scotland/Galicia and Krakow. (Iceland will always look silly no matter what) The same cannot be said for how Compostela, Carcassonne, Krakow and Iceland look like right now. Ideally we would have +20 different styles, and a more granular distribution in a per-barony basis. I'm trying to be reasonable to the artists and content designers here.

## Reply 145 — participant_065 · 2021-12-10 · post-27954626

<!-- artifact:quote:start -->
> Bandua_of_Gallaecia said: Now that cultures are being greatly reworked and not everyone in the same culture group needs to have the same everything, would it be possible to add more asthetics/architectures to the game? Right now we have cities in Scotland looking identical to those in Romania and it feels off. View attachment 784511 Click to expand...
<!-- artifact:quote:end -->
They're less than two months away from release with a large part of that time spent with them being on vacation why are y'all trying to further subdivide the court styles knowing good and well there's no way they could complete them right now?

## Reply 146 — participant_076 · 2021-12-10 · post-27954680

<!-- artifact:quote:start -->
> monkey1998 said: They're less than two months away from release with a large part of that time spent with them being on vacation why are y'all trying to further subdivide the court styles knowing good and well there's no way they could complete them right now? Click to expand...
<!-- artifact:quote:end -->
Just food for later thought, i have no expectations for any new styles to be added at the current stage of this DLC development. The only reason why I posted this here and not into it's own dedicated thread was because originally i was only going to argue for Westernmost kingdom of Europe, who isn't even touching the mediterranean to have the Western court graphics insted of the Mediterranean ones, in the following image (View attachment Castelos.png) you may notice the complete absence of any tiles (they were only introduced in Iberian architecture in the 15th century, starting in Seville), no corinthian colums, few large windows, few painted walls and few stone celings , and instead an abundance of stoned walls, small, narrow windows and wood ceilings. I included a castle for every single county to avoid accusations of cherrypicking. But then one thing led to another and i decided to rant on the whole architecture issue altogether.

## Reply 147 — participant_064 · 2021-12-10 · post-27954746

<!-- artifact:quote:start -->
> Balesir said: Now you are egregiously trying to worm out of the situation instead of accepting criticism with good grace, and that's just irritating. For illustration, here: So, let's just look at the post I was responding to, shall we? So, which of the four that you explicitly called "primitive" there was I suppose to be not assuming you were calling "primitive"? Check out the actual technologies of the time period we are talking about. The arabs, turks, persians and berbers had the most sophisticated ceramics for almost all of the medieval period. Medieval Islamic plates and tiles were (and still are) absolutely stunning. Take a look at West African clothwork; it was used as currency in the region and was the start of a tradition that has lasted until the present day. Look at Scythian metalworking and leatherwork (what little survives). Have you ever seen a 'viking' (early medieval Scandinavian) pattern-welded sword? Both original swords, generally in corroded condition, and stunning reproductions are available in museums and private collections. If we were talking about later periods, you might begin to have a point - but in the early medieval period your assertions/assumptions are just plain wrong. Yes, I absolutely do think they should be represented - that was why I actually liked your original post! The post was a good suggestion, but flawed by a misapprehension that you have made far worse than it originally was by doubling down on your errors for no discernible reason, as far as I can see. Note, however, that doing those courts justice will take a lot of work by the artists involved. I think they would absolutely make a good job of it, but not in time for this particular release! It will take time. Click to expand...
<!-- artifact:quote:end -->
Well your answer proves you have either not read well my answers or done superficially! Infact I included major civilizations like muslim ones of Al Andalus up to China and there is factual historical evidence that those civilizations where far more advanced both technologically and culturally! This doesnt mean as you and some others assumed that I stated the other cultures like viking or the subsaharian or steppe ones where inferiors stupid or inept ! It just means that they where lagging behind in technology and culture evolution richness and finess. That they could make nice ornamebts or nuce clothes doesn't mean they could be on par with the most sofisticated of the time. There is a reason why Vikings were so admiring Byzanthium as was so advanced in technology and culture refined much more then their own society. Non admitting this is in my point if view is just personal bias and disagreeing with my posts won't make what I stated less true. That said you are all free to believe in marvel's vision of the Norse in 700 Ad if that's whats liked the most. With this I am out of that offtopic discussion just hoping to see also minor cultures and less technologically advanced thronerooms like tents and huts.

## Reply 148 — participant_065 · 2021-12-10 · post-27954748

<!-- artifact:quote:start -->
> Bandua_of_Gallaecia said: Just food for later thought, i have no expectations for any new styles to be added at the current stage of this DLC development. The only reason why I posted this here and not into it's own dedicated thread was because originally i was only going to argue for Westernmost kingdom of Europe, who isn't even touching the mediterranean to have the Western court graphics insted of the Mediterranean ones, in the following image (View attachment 784743) you may notice the complete absence of any tiles (they were only introduced in Iberian architecture in the 15th century, starting in Seville), no corinthian colums, few large windows, few painted walls and few stone celings , and instead an abundance of stoned walls, small, narrow windows and wood ceilings. I included a castle for every single county to avoid accusations of cherrypicking. But then one thing led to another and i decided to rant on the whole architecture issue altogether. Click to expand...
<!-- artifact:quote:end -->
Oh okay I thought y'all were offering serious suggestions y'all wanted added to Royal Court and not later. Adding it to this dlc would be unrealistic, but it would be nice to see more variety as the game develops. I get the feeling that's something they would continue to tweak and improve.

## Reply 149 — participant_078 · 2021-12-15 · post-27963018

<!-- artifact:quote:start -->
> Tomray94 said: Good idea, Though I'd probably shift Poland to Eastern. I'll admit I have not been there, but as far as I can tell, Northern-Style Buildings only exist in the north and were built later by the Teutonic Order. Any Poles here feel free to correct me if I am wrong Click to expand...
<!-- artifact:quote:end -->
It depends on the time period. Let's take the Wawel castle where Polish kings were seated—in the 1000s it looked like this: And in the 1400s-1500s like this (not counting some roof parts which are younger): The same architects who designed Teutonic castles were eventually hired by Polish kings and noblemen to design manors across the whole country. Red brick gothic was really popular for a while until the Renaissance and the Baroque brought new ideas and most castles were refitted to accommodate new styles.

## Reply 150 — participant_034 · 2021-12-15 · post-27963041

<!-- artifact:quote:start -->
> Bandua_of_Gallaecia said: Well, we could go around picking outliers all day long, Click to expand...
<!-- artifact:quote:end -->
If there's that many outliers, then they're not outliers.

## Reply 151 — participant_079 · 2021-12-15 · post-27963167

<!-- artifact:quote:start -->
> Carlberg said: CK3 Dev Diary #84 - Building a Court - A Tale of Code and Art.​Hello and welcome to Dev Diary #84, I’m @Carlberg , the 3D environment lead artist and today we will be having a closer look at the development of the Royal Court rooms. This is a feature that we’ve been working hard on and it represents a great new step in bringing this historical era to life. Big thanks to @Alien-47 (code), Stella (3D environment art) and Linus (tech art) who's perspectives they've written down for this Dev diary, drawn from their experiences from both code and art in the making of this feature. Heads up! - A lot of the pictures in this post will be of old prototypes and iterations intermixed later with more recent images towards the end. So no need to worry about issues you may spot in the older images.​A new visual feature​With the new 3D character systems implemented in CK3 we wanted to show the characters of the middle ages in a whole new dynamic way. So as we started laying down the foundations of the Royal Court we also wanted to bring the very courts to life and find continued use for these 3D characters. This new feature was a major step in that direction. The inspiration for the feature was partly scenes that hearken back to throne rooms seen in games of old where we wish they had been livelier, with more interaction and chances for us to impact the people and objects in them. We drew upon these concepts and ideas of our own to weave together a visualization of the courts hosted by the most prominent royal titles.​ The Prototyping​At the beginning of the court development we knew that we were in for a challenge to stake out a new visual workflow within the engine that previously had not had any instances of contained 3D scenes and shared lighting systems within it. So we decided that to start off we needed a working prototype - laying a foundation and gradually adding more and more graphical features and complexity. Moving forward only when we’re sure the previous step succeeded. A natural starting point of exploration were the characters. We could already show beautiful animated portraits and the courtroom had to be able to show the same people so players could easily recognize their appearance. Could we reuse the same system that assembles characters - show appropriate body, apply transformation to show age, height, weight, apply the same clothing, hair, set the same animation? First step - success. The people in the courtroom look exactly the same as in portraits. Next step, is it possible to show many people at the same time in the same scene? This is quite different from portraits in the interface and events - those always have 1 person per image, even if the UI tries to combine them nicely together. With some optimization the room could now handle about 20 random characters, and even some objects. So the scene finally resembles a courtroom. Although a bit dark.​ View attachment 780625 The scene could now show several people and items in the prototype​ But what can we do with lights? The ambition for the court scene and requirement for lighting is much higher and more advanced than for regular portraits. We needed more simultaneous light sources. At the same time shadows naturally become much more complicated as well. People and objects can interfere with lights and it needs to be visible. Another issue was making sure characters and objects apply the lighting and shadows in the same way, so it’s easier for artists to manipulate the scene and develop the assets. After a bit of time and several iterations we had upgraded and made many improvements to the lighting system.​ View attachment 780624 Lights and shadows in a shared scene — Proof that multiple lights work and blend as intended, if a bit rough still.​ It was roughly at this time we felt we had confidence that the goal was within reach, and all technology was working as we intended. It was also clear that we could afford the desired complexity of the scene from a performance point of view. After all, players should have an enjoyable experience both on the map and in the court. We had built an understanding of how many people the scene could handle efficiently, how many light sources, and how many shadows we could allow (this is one of the most expensive parts). And so the prototype has been integrated as a proper feature of the game. View attachment 780622 Scene with better lighting, assets, materials, people positions​ From this point on work on the court room continued with multiple people from different disciplines working very closely together. More and more features waited to be implemented, so you can now see the beautiful results of all this effort. Concept art and vision​Being worked alongside the prototype was the vision we had for the Royal Court-rooms. We began by looking at the four main cultural areas we would be covering in the expansion. The west European, Mediterranean, Middle-eastern and Indian courts. We wanted each of these areas to be distinct, having their own visual style through architecture and lighting so to give their own unique feeling. View attachment 780616View attachment 780615 View attachment 780617View attachment 780618 Concepts of the different walls aesthetics of the courts, Mediterranean, Western, Middle-East/North Africa and India. ​ The west European court draws much of its inspiration from courtly interiors of England, Germany, France and neighboring areas. Darker rooms lit by fiery hearths, candles and chandeliers. In the Mediterranean more inspiration comes from the Byzantine courts and those found in Italy and other heirs of Rome. The rooms hint back at this grander past with larger roofs, domes and columns supporting the walls and arches. In the Middle-eastern courts we have a wider spread geographically, as these courts draw inspiration and cues from the courts all the way from Arabia to the architecture of Andalusia. In India we encountered an interesting split, as influences in architecture were pushing in from the west while there were still distinctly Indian courts. This was one of the reasons behind adding more court variants so that we could cover more of these visual flairs. View attachment 780708View attachment 780709View attachment 780710 Style variation exploration, more on those further down in the Dev Diary.​ Each scene was broken down into components like walls, roofs, floors and key assets like thrones, chandeliers and fireplaces. While these were being designed from a plethora of references gathered from each culture we also created variants in the concepts. This was done both as exploration but also to add variance to the courts so that they don't all look the same all the time. You will most likely have seen some variants of these when we’ve shared screenshots in past dev-diaries. ​View attachment 780387​Different courts, different architectural styles, different lighting setups.​ But the concept art phase did not end after the initial stages however, because once the scenes were being put together we returned to the concepts to try out the different lighting setups to help in the lighting of the rooms, giving our artists more ideas of where to focus the light and accentuate the scene further. Since the lighting system was being built alongside this in the prototype, the concept art took inspiration from contemporary game engines to help guide the prototyping, and not just the visual development. A room takes shape​When starting the modeling of the actual assets for the throne rooms there were several constraints to keep in mind. We had decided to go with a modular workflow so we could easily swap out wall-types and materials, so the dimensions would have to be consistent and work with the plans and concepts we had decided to pursue. We were also making several visual variants for each culture, which meant that we had to try and keep the details of the walls and materials equally interesting for each different type. Another big limitation was the fact that we had never before made a scene within our engine like this, so that meant that there were a lot of uncertainties when it came to how much we could push the graphics and where the limits were. Since we were also going to have the artifact system we had to make sure we left enough room for the artifacts and banners without having the environment taking too much attention. This became a trial and error phase to find a good baseline for each throne room. View attachment 780628 Early blocking out of the different artifact and furniture slots to be able to see where in the environments we had to make space.​ To create variation we made sure to have the materials contrast with each other while still fitting together aesthetically so no culture would have throne rooms that all felt exactly the same. This along with changing some architectonic aspects helped the scenes be more distinct. We also worked on adding variation to the grandeur levels, here we wanted the difference to show in the cleanliness and brightness of the environment textures, as well as in the richness of detail in the geometry and amount of decorative props. (Visual examples of this are shown in the final chapter) View attachment 780726 View attachment 780631 Making sure the different materials work together to create a cohesive feeling for each culture, but still looking different from each other. Example images taken from the MENA culture throne rooms.​ Lighting and FX​A lot of our visual tech usually involves considerations for a top-down map, and since we didn’t have much need for full scale 3D room rendering & lighting in the past, we had to do a lot of rethinking to get this to work - we went from previously having 4 lights, moving up to 20 total light sources and expanding the light types available with new ones like area lights - adding sphere & disc area lights. This helps illuminate areas such as room filling bouncing light (seen to great effect in Mediterranean courts) and helps us with light coming in from the windows and other openings. View attachment 780682 A cozily lit interior.​ Another technique we used was animated lights. They move a little, flicker in intensity - very useful for making the fireplace feel like it’s actually on fire and heating up the room a bit. To sell the atmospheric feeling in the room, we added some transparent particles with a little light fade on the sides of the windows and other select places. Even though it isn’t adding to the “real” light of the room, it helps give it that last piece of convincing magic touch. We also used particle systems for effects like the fireplace, candles and torches. The concept art helped us find the vision of what we wanted to do. Starting with just the room geometries, we used the color hues and general light level from the concepts to create a lit space that felt cohesive, which we then could tweak and modify until they felt comfortable to look at. Technical hurdles & Bloopers​One of the hurdles throughout the development of the court scene were tools - a means for developers to manipulate the scene contents more efficiently - edit objects, characters, lights, change their positions, add or remove to have a toolset that allows more quick iteration and direct interaction. It took time to develop a solution that made this part of work less tiresome. One of the downsides of not having readily available tools - you have to do those yourself, and sometimes reinvent a wheel multiple times. But we’re lucky to have an internal tools team that came to rescue us, and it improved the processes immensely. We had plenty of funny bugs over the court of development, resolved by now of course. View attachment 780621 It's not a cult! — Sometimes visual bugs can be quite fun View attachment 780619 Baby Bighead bug. View attachment 780620 They say you shouldn't lose your head in court, but this is ridiculous​ Finished courts and courtly variation​With a working feature, concepts drawn and all the parts built we got to compositing together the scenes. There were a lot of iterative steps working on the textures, lighting and positioning to get all pieces to look their best. The environment team has made a set of three different variations of each cultural court type that each has their own architectural and/or decorative flair and visuals, the scenes differ more in geometry and configuration or the construction materials used. So there may be more windows and ample light, or a fireplace castings its warm light into your court. View attachment 780679View attachment 780680View attachment 780681 The western European inspired courts, with stone and plastered walls. View attachment 780730View attachment 780731View attachment 780732 The Mediterranean courts, drawing inspiration from the Roman past as well as the melding of surrounding cultures. View attachment 780670View attachment 780669View attachment 780668 The Middle Eastern courts, drawn on from architecture found in Arabia to Al-Andalus. View attachment 780675View attachment 780676View attachment 780677 The courts of India, greatly varying interiors.​ Grandeur variants was a further change we added later in the development cycle, which helps give a little extra flavor to the progress of your court's grandeur. Lower court grandeur has less fancy details and furniture extras in the court than the higher level which sports more of them. The surfaces of the room have also been made to look more worn and less taken care of at a lower grandeur level, compared to the high grandeur which look their grandest. View attachment 780392 The Pomeranian kings court has seen better days, its painted plastered walls worn and peeling, the floor tiling tired, scraped and just slightly dirty. Little decorations or extra furniture have been afforded the kings halls. View attachment 780390 After much investment in upping the level of grandeur, the court's floors are fresh and polished, extra candles and seats added to the court, and a long finely woven rug lines the path up to the throne.​ Wrapping up​And with that we’ve come the full way from inception all the way to the finished scenes. We’ve been continuously tweaking and polishing stuff like camera angles, lighting and textures, and we do hope this is a great foundation for a feature that we can grow over time. So a big thanks from the court and environment team for checking into this Dev Diary, which will be the last one of the year, but fret not! We will still be bringing you weekly teasers all the way through December to the start of next year. These teasers will be smaller in scale and focus on some minor features and things we still want to show off, so keep your eyes out for it next week. Click to expand...
<!-- artifact:quote:end -->
Will there be a African court style below the Sahara or will the Arabic court be given to us?

## Reply 152 — participant_034 · 2021-12-15 · post-27963178

<!-- artifact:quote:start -->
> jtheking726 said: Will there be a African court style below the Sahara or will the Arabic court be given to us? Click to expand...
<!-- artifact:quote:end -->
The court styles for the initial release of the DLC are Western, Mediterranean, Middle Eastern, and Indian.

## Reply 153 — participant_072 · 2021-12-15 · post-27964256

<!-- artifact:quote:start -->
> Bandua_of_Gallaecia said: Now that cultures are being greatly reworked and not everyone in the same culture group needs to have the same everything, would it be possible to add more asthetics/architectures to the game? Right now we have cities in Scotland looking identical to those in Romania and it feels off. View attachment 784511 Click to expand...
<!-- artifact:quote:end -->
Notice how both continental and northern have the same timber framed building style showing up on the bottom row? "Atlantic" should have that as well, since it's a common style of the period, and through into Tudor times throughout England. The Château de Roquetaillade is in what you consider Atlantic style, despite being in the mediterranean area. Historic English churches include examples of Atlantic, Continental, and Northern Styles, depending largely on the age and cultural history of the area. As an example, the cathedral in my home city would appear to be in "Continental" style, because it was built back in Norman times and then added onto over the centuries. The churches in some of the parishes where I grew up though are more in keeping with "Atlantic", because they're Saxon in origin. And I'm *fairly* sure those examples are built at wildly different times, with different levels of technology, and even different aims in mind, especially with the castles.

## Reply 154 — participant_064 · 2021-12-16 · post-27965080

<!-- artifact:quote:start -->
> prismaticmarcus said: then stop using the word 'backward.' i think you've found that it does cause offence. Click to expand...
<!-- artifact:quote:end -->
English is not my language I always thought backward meant lagging behind in technology , didn't know it was offensive.

## Reply 155 — participant_050 · 2021-12-16 · post-27965092

<!-- artifact:quote:start -->
> Prometheus_1 said: English is not my language I always thought backward meant lagging behind in technology , didn't know it was offensive. Click to expand...
<!-- artifact:quote:end -->
fair enough. it kind of has the same connotations as 'retarded' which is a word i really hate

## Reply 156 — participant_056 · 2021-12-16 · post-27965395

<!-- artifact:quote:start -->
> Prometheus_1 said: English is not my language I always thought backward meant lagging behind in technology , didn't know it was offensive. Click to expand...
<!-- artifact:quote:end -->
Well, the word can give vibes of "not-intelligent", which is obviously offensive (especially when applied to whole groups of people), but my original point was that the people in these regions were not lagging behind technologically in the time period we are discussing (early-to-mid medieval in northern europe). Bear in mind that most northern europeans at the time were peasant agriculturalists or fisherfolk/hunters/herders living in either mud huts or log cabins (they were actually fairly comfortable, but a modern person seeing them would call them exactly this). They had wrought but not cast ironwork, crude steel and woven and fulled cloth with local dyes. This applied more-or-less everywhere on the CK map, with a few localised 'hot spots' for specific technologies, up to 1200 or so.

## Reply 157 — participant_064 · 2021-12-16 · post-27965408

<!-- artifact:quote:start -->
> prismaticmarcus said: fair enough. it kind of has the same connotations as 'retarded' which is a word i really hate Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Balesir said: Well, the word can give vibes of "not-intelligent", which is obviously offensive (especially when applied to whole groups of people), but my original point was that the people in these regions were not lagging behind technologically in the time period we are discussing (early-to-mid medieval in northern europe). Bear in mind that most northern europeans at the time were peasant agriculturalists or fisherfolk/hunters/herders living in either mud huts or log cabins (they were actually fairly comfortable, but a modern person seeing them would call them exactly this). They had wrought but not cast ironwork, crude steel and woven and fulled cloth with local dyes. This applied more-or-less everywhere on the CK map, with a few localised 'hot spots' for specific technologies, up to 1200 or so. Click to expand...
<!-- artifact:quote:end -->
Ok then my bad I used a wrong word. My word was most probably not correct , of course all people are smart and intelligent, but I made a comparison based on culture and technological advancements of some societies versus other societies like Imperial China vs Mongol steppe lord or Baghdad vs a subsaharian tribe or Byzanthium vs a Viking settlement, this doesn't mean that the first where more intelligent than the second or Mongols wouln't end up conquering China ,Turks Byzanthium and Vikings England and Southern Italy.

## Reply 158 — participant_080 · 2021-12-16 · post-27965536

But the real question is! Can I watch it when I get poisoned by my heir or is the court just faccade?

## Reply 159 — participant_056 · 2021-12-16 · post-27965882

<!-- artifact:quote:start -->
> Prometheus_1 said: My word was most probably not correct , of course all people are smart and intelligent, but I made a comparison based on culture and technological advancements of some societies versus other societies like Imperial China vs Mongol steppe lord or Baghdad vs a subsaharian tribe or Byzanthium vs a Viking settlement, this doesn't mean that the first where more intelligent than the second or Mongols wouln't end up conquering China ,Turks Byzanthium and Vikings England and Southern Italy. Click to expand...
<!-- artifact:quote:end -->
Yes, I think a good way to put it might be like this: 1) There were a lot of very varied cultures across the map area (because travel and communication were slow and expensive), each with different fashions and desired looks. 2) The expense of long-distance trade meant that locally available materials mattered a lot, leading to very different 'look and feel' for everything from drinking vessels to walls and buildings in different regions; the degree of know-how in crafting materials tended to vary with local availability, too, making the differences even more noticeable. All this leads to a LOT of different 'looks' for courts - having as many of them as is pricticable in the game would be good!

## Reply 160 — participant_076 · 2021-12-19 · post-27970341

<!-- artifact:quote:start -->
> DreadLindwyrm said: Notice how both continental and northern have the same timber framed building style showing up on the bottom row? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> DreadLindwyrm said: Atlantic" should have that as well, since it's a common style of the period, and through into Tudor times throughout England. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> DreadLindwyrm said: The Château de Roquetaillade is in what you consider Atlantic style, despite being in the mediterranean area. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> DreadLindwyrm said: Historic English churches include examples of Atlantic, Continental, and Northern Styles, depending largely on the age and cultural history of the area. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> DreadLindwyrm said: And I'm *fairly* sure those examples are built at wildly different times, with different levels of technology, and even different aims in mind, especially with the castles. Click to expand...
<!-- artifact:quote:end -->
So? Just because two styles have a common trait doesn't make them the same. It shouldn't, because Atlantic is far more than just England. Like i said, ideally every barony would have it's own style. I actually wanted Aquitaine to have the Atlantic style as well and only Provence to have the Mediterranean one, just like i wanted Asturias to have the Atlantic one, but Léon the Mediterranean one, but alas dividing existing cultures in half seemed unrealistic to suggest, so lumped all of Ocitanian into a single style, just like i lumped Asturleonese Good, then Atlantic fits, so my suggestion works. The reason why i added the Atlantic style was not because the Western/Continental didn't fit England, but mostly because the Mediterranean one absolutely did not fit West Iberia (and the western/continental didn't fit either, so i needed a new one, which fortunately also fits England quite well, and even better than the current one, at least as far as castles are concerned). Well the graphics don't change with the time, so this is pretty irrelevant. What should i pick for the West, Romanesque or Gothic? Either choice works, depending on which specific timeframe you ask. As long as the specific building belongs well in the game's timeframe, it should work.

## Reply 161 — participant_072 · 2021-12-19 · post-27970759

<!-- artifact:quote:start -->
> Bandua_of_Gallaecia said: So? Just because two styles have a common trait doesn't make them the same. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Bandua_of_Gallaecia said: It shouldn't, because Atlantic is far more than just England. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Bandua_of_Gallaecia said: Like i said, ideally every barony would have it's own style. I actually wanted Aquitaine to have the Atlantic style as well and only Provence to have the Mediterranean one, just like i wanted Asturias to have the Atlantic one, but Léon the Mediterranean one, but alas dividing existing cultures in half seemed unrealistic to suggest, so lumped all of Ocitanian into a single style, just like i lumped Asturleonese Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Bandua_of_Gallaecia said: Good, then Atlantic fits, so my suggestion works. The reason why i added the Atlantic style was not because the Western/Continental didn't fit England, but mostly because the Mediterranean one absolutely did not fit West Iberia (and the western/continental didn't fit either, so i needed a new one, which fortunately also fits England quite well, and even better than the current one, at least as far as castles are concerned). Click to expand...
<!-- artifact:quote:end -->
You are however using the same style in two of the areas you identify whilst then not applying it to an area known for the style. I can't comment on its usage in the other two areas and how appropriate it is though. It is however *the* classic style for towns in the medieval period in the largest section of the "Atlantic" region, whereas the "flint cottage" look isn't. That's appears more in villages and hamlets, and even then only areas that have that style of stone readily available. Most villages were timber framed as well, making the stone cottage look even less suitable. The problem is that you're *still* forcing inappropriate styles onto areas with these changes, and some of them appear worse fits than the existing ones. Well... no. Because "Atlantic" style churches stop abruptly when the Normans turn up. It's not a good fit for the majority of the game time frame. It works for the early start in Saxon England, but I'm not so sure it fits Scotland, Wales, or Ireland during the period. England though in the period is *mostly* known for what you consider "continental" as far as churches go, albeit with old churches surviving in the other two styles. Some even closely resemble the style you've listed as "Eastern". Basically, you're over simplifying the divisions and drawing hard lines on the map that don't actually match reality. Your suggestion of "every barony having its own style" doesn't really work well either, because so much of that is culture dependent, and the real life culture may bear no resemblance to the in game culture. Yes, the style of buildings needs to be reexamined, but the lines you've drawn just don't work for me, because they still have the problem of ignoring that certain styles exist across the arbitrary lines you've drawn, and that you've picked a non-representative style for some of them. I'm not even sure the one you've picked for "Atlantic town" is remotely in period.

## Reply 162 — participant_076 · 2021-12-19 · post-27970988

<!-- artifact:quote:start -->
> DreadLindwyrm said: You are however using the same style in two of the areas you identify whilst then not applying it to an area known for the style. I can't comment on its usage in the other two areas and how appropriate it is though. It is however *the* classic style for towns in the medieval period in the largest section of the "Atlantic" region, whereas the "flint cottage" look isn't. That's appears more in villages and hamlets, and even then only areas that have that style of stone readily available. Most villages were timber framed as well, making the stone cottage look even less suitable. The problem is that you're *still* forcing inappropriate styles onto areas with these changes, and some of them appear worse fits than the existing ones. Well... no. Because "Atlantic" style churches stop abruptly when the Normans turn up. It's not a good fit for the majority of the game time frame. It works for the early start in Saxon England, but I'm not so sure it fits Scotland, Wales, or Ireland during the period. England though in the period is *mostly* known for what you consider "continental" as far as churches go, albeit with old churches surviving in the other two styles. Some even closely resemble the style you've listed as "Eastern". Basically, you're over simplifying the divisions and drawing hard lines on the map that don't actually match reality. Your suggestion of "every barony having its own style" doesn't really work well either, because so much of that is culture dependent, and the real life culture may bear no resemblance to the in game culture. Yes, the style of buildings needs to be reexamined, but the lines you've drawn just don't work for me, because they still have the problem of ignoring that certain styles exist across the arbitrary lines you've drawn, and that you've picked a non-representative style for some of them. I'm not even sure the one you've picked for "Atlantic town" is remotely in period. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Your suggestion of "every barony having its own style" doesn't really work well either, because so much of that is culture dependent, and the real life culture may bear no resemblance to the in game culture. Click to expand...
<!-- artifact:quote:end -->
So... basically what you are arguing about is that English culture should also have what i considered the continental style is that it? Generally speaking architecture is far more geographically dependent than culturally dependent. The castles and towns the crusaders built in the holy land were much more similar to the local fortifications and towns that to those built around Paris and Brugge. Likewise, if some Islamic Empire were to spread to the heart of Europe, they wouldn't be going around building sandstone cities in the Dark Forest. Also, within the same culture you can find widely different styles here is a couple of examples: Both Castilian, erected in the game's timeframe, and 30km from eachother. But one was built on top of a hill (so a smaller area, and slender shape) with significant rain and snowfall (so, with high roofs) and thus resembles more those with similar geographical conditions, I.E: Central Europe. The other was built in a dry plain, geographically a bit similar to the near-east, thus it looks more like the buildings there. Both Portuguese, erected 40km from eachother. But one was built in a granitic territory, so it looks more like the normal type found across the Atlantic seaboard of Europe. The other was built in a Sandstone basin, thus the type of rock and way of carving and assembling such rocks is much more alike those used in places with similar soil types: I.E the Mediterranean seaboard. Roofs in the Atlantic seaboard are either absent or not very pronounced, because it is very rare to snow on the Atlantic coast, regardless if I'm talking about Compostela, Nantes, Cardiff or Galway.

## Reply 163 — participant_072 · 2021-12-20 · post-27971721

<!-- artifact:quote:start -->
> Bandua_of_Gallaecia said: So... basically what you are arguing about is that English culture should also have what i considered the continental style is that it? Click to expand...
<!-- artifact:quote:end -->
No. I'm saying that what you're trying here suffers the same problem you're trying to resolve. You're over simplifying the divisions between geographic areas, even though you've got more divisions. You're also trying to force a particular castle style to *always* go with a particular church style and a particular town style, when that's not the case.

## Reply 164 — participant_076 · 2021-12-20 · post-27972483

<!-- artifact:quote:start -->
> DreadLindwyrm said: No. I'm saying that what you're trying here suffers the same problem you're trying to resolve. You're over simplifying the divisions between geographic areas, even though you've got more divisions. You're also trying to force a particular castle style to *always* go with a particular church style and a particular town style, when that's not the case. Click to expand...
<!-- artifact:quote:end -->
I agree that my suggestion still suffers from oversimplification, everything in this game is simplified, it has to, it's impossible to make it otherwise. I'm just trying to make it slightly less simplified than it currently is, 5 divisions are always going to be better than 2. If you think i assigned some places wrongly, chose the wrong styles or chose the wrong divisions i am glad to listen to the output from other people, especially those who actually live in these places and thus know it better than i do. But what exactly are you arguing for here? Is it that since it will always have some degree oversimplification, they should not even try to improve it?

