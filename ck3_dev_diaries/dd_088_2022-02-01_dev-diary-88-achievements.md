---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1508593/"
forum_thread_id: 1508593
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 88
title: "CK3 Dev Diary #88: Achievements"
dd_date: 2022-02-01
author_handle: Trin Tragula
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 821
inline_image_count: 20
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1508593'
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
    location: raw_lines_~28_to_146
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_145
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1853.jpg?1643722271
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_257_to_262
    action: preserved_and_flagged
    counts:
      Like: 78
      Love: 15
      (unlabeled — rendered as base64 data URI): 1
      Haha: 2
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_270_to_369
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_370_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1853.jpg?1643722271)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #88: Achievements

<!-- artifact:thread_metadata:start -->
- Thread starter [Trin Tragula](https://forum.paradoxplaza.com/forum/members/trin-tragula.18587/)
- Start date [Feb 1, 2022](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-88-achievements.1508593/)
<!-- artifact:thread_metadata:end -->

Hello and welcome to another development diary for the Royal Court!  

With release drawing nearer the time has come to show the 20 new achievements that come with the update. As with previous achievements we have aimed to have a good mix of easier to harder achievements with some focusing on new features and others on interesting challenges or starts.  


## Very Easy​

**Patronage**  
[![exp_patronage_achievement.png](https://forumcontent.paradoxplaza.com/thumbnail/public/788200/exp_patronage_achievement.png "exp_patronage_achievement.png")](https://forumcontent.paradoxplaza.com/public/788200/exp_patronage_achievement.png)  
Fund an Inspired character's Project, and receive the end result.  


## Easy​

**I Made This**  
[![exp_i_made_this_achievement.png](https://forumcontent.paradoxplaza.com/thumbnail/public/788196/exp_i_made_this_achievement.png "exp_i_made_this_achievement.png")](https://forumcontent.paradoxplaza.com/public/788196/exp_i_made_this_achievement.png)  
Loot an artifact you do not have a claim on and pass it down to your heir  

**Polyglot**  
[![polyglot.png](https://forumcontent.paradoxplaza.com/thumbnail/public/788207/polyglot.png "polyglot.png")](https://forumcontent.paradoxplaza.com/public/788207/polyglot.png)  
Personally know 10 languages  

**Changing Course**  
[![exp_changing_course_acheivement.png](https://forumcontent.paradoxplaza.com/thumbnail/public/788191/exp_changing_course_acheivement.png "exp_changing_course_acheivement.png")](https://forumcontent.paradoxplaza.com/public/788191/exp_changing_course_acheivement.png)  
Create a Divergent Culture  

**Converging Paths**  
[![exp_converging_paths_achievement.png](https://forumcontent.paradoxplaza.com/thumbnail/public/788192/exp_converging_paths_achievement.png "exp_converging_paths_achievement.png")](https://forumcontent.paradoxplaza.com/public/788192/exp_converging_paths_achievement.png)  
Create a Hybrid Culture  


## Medium​

Hoarder  
[![exp_hoarder_achievement.png](https://forumcontent.paradoxplaza.com/thumbnail/public/788195/exp_hoarder_achievement.png "exp_hoarder_achievement.png")](https://forumcontent.paradoxplaza.com/public/788195/exp_hoarder_achievement.png)  
Have an artifact in every slot in the Inventory and Royal Court  

**Crème de la Crème**  
[![exp_creme_de_la_creme_achievement.png](https://forumcontent.paradoxplaza.com/thumbnail/public/788193/exp_creme_de_la_creme_achievement.png "exp_creme_de_la_creme_achievement.png")](https://forumcontent.paradoxplaza.com/public/788193/exp_creme_de_la_creme_achievement.png)  
Reach the maximum amount of Court Grandeur  

**One of a Kind**  
[![exp_one_of_a_kind_achievement.png](https://forumcontent.paradoxplaza.com/thumbnail/public/788199/exp_one_of_a_kind_achievement.png "exp_one_of_a_kind_achievement.png")](https://forumcontent.paradoxplaza.com/public/788199/exp_one_of_a_kind_achievement.png)  
Obtain an Epic artifact from an Adventurer Inspiration  

**Brave and Bold**  
[![exp_brave_and_bold_achievement.png](https://forumcontent.paradoxplaza.com/thumbnail/public/788190/exp_brave_and_bold_achievement.png "exp_brave_and_bold_achievement.png")](https://forumcontent.paradoxplaza.com/public/788190/exp_brave_and_bold_achievement.png)  
Starting as the Piasts in 867, rule Poland, adopt Feudalism, and own a Famed or Illustrious-rarity regalia, crown, weapon, and armor.  

**They Belong in a Museum**  
[![exp_they_belong_in_a_museum_achievement.png](https://forumcontent.paradoxplaza.com/thumbnail/public/788203/exp_they_belong_in_a_museum_achievement.png "exp_they_belong_in_a_museum_achievement.png")](https://forumcontent.paradoxplaza.com/public/788203/exp_they_belong_in_a_museum_achievement.png)  
Appoint a character with a completed Adventure inspiration as your Antiquarian  

**The True Royal Court**  
[![exp_the_true_royal_court_achievement.png](https://forumcontent.paradoxplaza.com/thumbnail/public/788202/exp_the_true_royal_court_achievement.png "exp_the_true_royal_court_achievement.png")](https://forumcontent.paradoxplaza.com/public/788202/exp_the_true_royal_court_achievement.png)  
As a vassal king to an emperor, have a higher court grandeur than they do  


## Hard​

**Beta Israel**  
[![exp_beta_israel_achievement.png](https://forumcontent.paradoxplaza.com/thumbnail/public/788188/exp_beta_israel_achievement.png "exp_beta_israel_achievement.png")](https://forumcontent.paradoxplaza.com/public/788188/exp_beta_israel_achievement.png)  
Starting and staying as a Jewish ruler in East Africa, rule a Kingdom and diverge your culture  

**Rise of the Ghurids**  
[![exp_rise_of_the_ghurids_achievement.png](https://forumcontent.paradoxplaza.com/thumbnail/public/788201/exp_rise_of_the_ghurids_achievement.png "exp_rise_of_the_ghurids_achievement.png")](https://forumcontent.paradoxplaza.com/public/788201/exp_rise_of_the_ghurids_achievement.png)  
Starting as the Duke of Ghur in 867 or 1066, conquer the borders of the historical Ghurid Empire  

**Turkish Eagle**  
[![exp_turkish_eagle_achievement.png](https://forumcontent.paradoxplaza.com/thumbnail/public/788205/exp_turkish_eagle_achievement.png "exp_turkish_eagle_achievement.png")](https://forumcontent.paradoxplaza.com/public/788205/exp_turkish_eagle_achievement.png)  
As the Seljuk Count in Samosata, form Rum and create a Hybrid Culture between Oghuz and Greek  

**Bod Chen Po**  
[![exp_bod_chen_po_achievement.png](https://forumcontent.paradoxplaza.com/thumbnail/public/788189/exp_bod_chen_po_achievement.png "exp_bod_chen_po_achievement.png")](https://forumcontent.paradoxplaza.com/public/788189/exp_bod_chen_po_achievement.png)  
As a member of the Pugyel Dynasty, re-create the Empire of Tibet  

**Delusions of Grandeur**  
[![exp_delusion_of_grandeur_achievement.png](https://forumcontent.paradoxplaza.com/thumbnail/public/788194/exp_delusion_of_grandeur_achievement.png "exp_delusion_of_grandeur_achievement.png")](https://forumcontent.paradoxplaza.com/public/788194/exp_delusion_of_grandeur_achievement.png)  
Be at least 6 levels above your expected Court Grandeur  

**True Tolerance**  
[![exp_true_tolerance_achievement.png](https://forumcontent.paradoxplaza.com/thumbnail/public/788204/exp_true_tolerance_achievement.png "exp_true_tolerance_achievement.png")](https://forumcontent.paradoxplaza.com/public/788204/exp_true_tolerance_achievement.png)  
Rule a realm containing at least 10 cultures with 95% or more acceptance of your culture  

**Inspirational**  
[![exp_inspirational_achievement.png](https://forumcontent.paradoxplaza.com/thumbnail/public/788197/exp_inspirational_achievement.png "exp_inspirational_achievement.png")](https://forumcontent.paradoxplaza.com/public/788197/exp_inspirational_achievement.png)  
Sponsor 30 successful inspirations in one game  


## Very Hard​


**Lingua Franca**  
[![lingua_franca.png](https://forumcontent.paradoxplaza.com/thumbnail/public/788206/lingua_franca.png "lingua_franca.png")](https://forumcontent.paradoxplaza.com/public/788206/lingua_franca.png)  
Have every Royal Court in the world speak your Court Language  

**Nobody Comes to Fika**  
[![exp_nobody_comes_to_fika_achievement.png](https://forumcontent.paradoxplaza.com/thumbnail/public/788198/exp_nobody_comes_to_fika_achievement.png "exp_nobody_comes_to_fika_achievement.png")](https://forumcontent.paradoxplaza.com/public/788198/exp_nobody_comes_to_fika_achievement.png)  
With the County of Fika as your primary title, diverge your culture and spread it to 30 Counties  


That was all for today and for the very last development diary prior to the release of the Royal Court! Next Tuesday the patch notes for the update that goes along with the Royal Court expansion will be posted.

<!-- artifact:reactions:start -->
- 78 Like
- 15 Love
- 9 (unlabeled — rendered as base64 data URI)
- 7 (unlabeled — rendered as base64 data URI)
- 2 Haha
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Trin Tragula](https://forum.paradoxplaza.com/forum/members/trin-tragula.18587/)**
Role: Game Designer - Crusader Kings 3
Badges: 36
Reaction score: 16,644

*[Full game-badge icon list of 44 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
