---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1402760/"
forum_thread_id: 1402760
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 33
title: "CK3 Dev Diary #33 - An Offer You Can’t Refuse"
dd_date: 2020-06-30
author_handle: blackninja9939
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1463
inline_image_count: 24
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1402760'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1415.jpg?1593519648
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_150_to_152
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_351_to_355
    action: preserved_and_flagged
    counts:
      Love: 169
      Like: 104
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_363_to_424
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_425_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1415.jpg?1593519648)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #33 - An Offer You Can’t Refuse

<!-- artifact:thread_metadata:start -->
- Thread starter [blackninja9939](https://forum.paradoxplaza.com/forum/members/blackninja9939.795679/)
- Start date [Jun 30, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-33-an-offer-you-cant-refuse.1402760/)
<!-- artifact:thread_metadata:end -->

Hello everyone and welcome to the 33rd CK3 Dev Diary!  

I’m Matthew, one of the Programmers on the CK3 team, and today I am going to talk to you about the overhaul we’ve done to Feudal Contracts since Dev Diary 17.  

A quick refresher on what Contracts are: every vassal above baron tier has an individual contract between them and their liege which affects how much the vassal gives to the liege in terms of tax and levies in exchange for the liege’s protection. In the case of Feudal vassals, this contract can be renegotiated.  

We were not fully content with the initial implementation of this setup as it did not help facilitate the drama and storytelling of the deals made between a vassal and their liege and the disagreements that could arise from that. This was a view shared among the community as well which reinforced our desire to give this feature another look, so a couple of our designers and I gave it an overhaul.  

**The Contract**  
You may have seen screenshots or videos of this system in some of the media released from our press events but I’m gonna take you through the new system step by step, so without further ado here is the new interface you’ll see when you interact with a vassal’s feudal contract.  

![ContractView.png](https://forumcontent.paradoxplaza.com/public/582538/ContractView.png "ContractView.png")


[Feudal contract negotiation screen]  

As you can see there are a lot more options now to tailor the contract.  

Going from top to bottom you can see that we have split the base tax and levy obligations into two separate tracks each now with five options. These are the core base of how much taxes and levies are given to the liege, the lower they are the more your vassal will like you, of course, and the higher they are the less content they will be.  
When negotiating a new deal you can only move to adjacent levels of the tax and levy obligations.  

Below that we have what we call the “Fine Print” options. These fine options are unlocked via various innovations and provide various modifications to the contract.  
The first row being the Special Contract options of Scutage, March, and Palatinate which are available for vassals that are Dukes or Kings.  

![Scutage.png](https://forumcontent.paradoxplaza.com/public/582540/Scutage.png "Scutage.png")


[Effects of scutage]  

![March.png](https://forumcontent.paradoxplaza.com/public/582541/March.png "March.png")


[Effects of march]  

![Palatinate.png](https://forumcontent.paradoxplaza.com/public/582542/Palatinate.png "Palatinate.png")


[Effects of palatinate]  

At the bottom we have the rest of the Fine Print options available, these are things like guaranteeing your vassal a spot on the council or granting them coinage rights. Some options are only shown if the vassal meets specific conditions, for example if the vassal is of a different faith to the liege. In such a case the “Religious Protection” gives them special rights to practice their faith without risk of the liege demanding their conversion or converting the faith of their provinces.  

**The Negotiation**  
When negotiating the contract a max of three changes may be made. We experimented with different values and this felt like it wasn’t too limiting whilst also letting you too wildly change your contract in one go.  

With the new obligations that can be changed and enacted this allows you to negotiate a more interesting deal. For example, you as the liege may want to increase the amount of taxes your vassal gives you, but just doing that alone will be viewed as unfair by the vassal and increase your tyranny.  

![NegotiationTyranny.png](https://forumcontent.paradoxplaza.com/public/582543/NegotiationTyranny.png "NegotiationTyranny.png")


[a contract proposal giving tyranny]  

So if you don’t want to take that tyranny hit then you need to look at what changes you can propose that the vassal will want, so in exchange for these increased taxes you could guarantee your vassal a spot on the council meaning you can now enact this deal without being viewed as a tyrant.  

![NegotiationFair.png](https://forumcontent.paradoxplaza.com/public/582544/NegotiationFair.png "NegotiationFair.png")


[a contract proposal with a fair trade]  

Alternatively, if you have a hook on your vassal then you can use that hook to count as one free change in favour of the vassal, so you can use your hook and get those higher taxes without having to give any other concessions and not be viewed as a tyrant. Blackmailing people is surprisingly effective.  

![NegotiationHook.png](https://forumcontent.paradoxplaza.com/public/582545/NegotiationHook.png "NegotiationHook.png")


[a contract proposal using a hook to avoid tyranny]  

It is worth mentioning that even if you propose a “fair” trade that does not give you tyranny this does not mean that the vassal will be perfectly content. There is an opinion change tied to each obligation and what status it is in, vassals will tend to dislike paying more and like paying less, and this opinion modifier will be present in the vassal’s view of their liege.  

The vassal themselves can of course also negotiate the contract, they have the added restriction that they must offer their liege an even trade. So they cannot ask to pay lower taxes without using either a hook or agreeing to give the liege something they would want, be that giving more levies, agreeing to stay with only partition succession, or giving up a benefit they have previously been given such as that guaranteed council spot.  

Some vassals start with contracts different to the default, in the Holy Roman Empire all vassals start with low taxes and levies to represent the internal state and the lower amount of control the Emperor was exerting over their vassals at the time.  

We really wanted the interface to make this feel like an actual paper contract being signed between the liege and the vassal, thankfully we had this beautiful parchment background and wax seal shader lying around that helped spice it up.  

**Modding Contracts**  
All of these different obligations, their effects, how the AI uses them, and how they are shown in the UI is controlled in the script files so you can mod in or change existing obligations to your heart’s content.  

Code:

```
religious_rights = {
    display_mode = checkbox

    is_shown = {

        NOT = {

            scope:vassal.faith = scope:liege.faith

        }

    }

    obligation_levels = {

        religious_rights_none = {

            default = yes

  

            ai_liege_desire = @ai_standard_liege_desire

            ai_vassal_desire = 0

        }

        religious_rights_protected = {

            is_valid = {

                NOT = {

                    scope:vassal.faith = scope:liege.faith

                }

            }

            parent = religious_rights_none

  

            vassal_opinion = 5

  

            vassal_modifier = {

                county_opinion_add = 5

            }

  

            flag = religiously_protected

  

            ai_liege_desire = 0

            ai_vassal_desire = 10

        }

    }
}
```

Here we have the script database entry for the religious protection obligation type, it demonstrates the various options and should be fairly self explanatory in its naming of the options.  

I hope you’ve all enjoyed this dev diary and are excited for the new Feudal Contracts and the more options and interactions they can provide between vassals and lieges!  

We look forward to seeing you next week, in the meanwhile if you want to chat more then I highly recommend joining our [CK Discord Server](https://discord.gg/ck3) as well!  

**Pets of the Dev Team**  
On the Crusader Kings 3 team we are of course very big fans of animals and pets of all kinds. So I thought to cap off this dev diary, and give you all some much needed cuteness overload during these difficult times in the world, I'd collect a bunch of pictures of all our wonderful pets, fluffy or otherwise!  

Spoiler: All of the pet pics

![Pet17.JPG](https://forumcontent.paradoxplaza.com/public/582566/Pet17.JPG "Pet17.JPG")


![Pet1.png](https://forumcontent.paradoxplaza.com/public/582561/Pet1.png "Pet1.png")

![Pet2.png](https://forumcontent.paradoxplaza.com/public/582547/Pet2.png "Pet2.png")

![Pet3.png](https://forumcontent.paradoxplaza.com/public/582548/Pet3.png "Pet3.png")

![Pet4.png](https://forumcontent.paradoxplaza.com/public/582549/Pet4.png "Pet4.png")

![Pet5.png](https://forumcontent.paradoxplaza.com/public/582550/Pet5.png "Pet5.png")

![Pet6.png](https://forumcontent.paradoxplaza.com/public/582551/Pet6.png "Pet6.png")

![Pet7.png](https://forumcontent.paradoxplaza.com/public/582552/Pet7.png "Pet7.png")

![Pet8.png](https://forumcontent.paradoxplaza.com/public/582553/Pet8.png "Pet8.png")

![Pet9.png](https://forumcontent.paradoxplaza.com/public/582554/Pet9.png "Pet9.png")

![Pet10.png](https://forumcontent.paradoxplaza.com/public/582555/Pet10.png "Pet10.png")

![Pet11.png](https://forumcontent.paradoxplaza.com/public/582556/Pet11.png "Pet11.png")

![Pet12.png](https://forumcontent.paradoxplaza.com/public/582557/Pet12.png "Pet12.png")

![Pet13.png](https://forumcontent.paradoxplaza.com/public/582558/Pet13.png "Pet13.png")

![Pet14.png](https://forumcontent.paradoxplaza.com/public/582559/Pet14.png "Pet14.png")

![Pet15.png](https://forumcontent.paradoxplaza.com/public/582560/Pet15.png "Pet15.png")


![Pet16.JPG](https://forumcontent.paradoxplaza.com/public/582565/Pet16.JPG "Pet16.JPG")

<!-- artifact:reactions:start -->
- 169 Love
- 104 Like
- 29 (unlabeled — rendered as base64 data URI)
- 12 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [blackninja9939](https://forum.paradoxplaza.com/forum/members/blackninja9939.795679/)**
Role: Former Senior Programmer - Crusader Kings 3
Badges: 99
Reaction score: 8,575

*[Full game-badge icon list of 1 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
