---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1542515/"
forum_thread_id: 1542515
content_type: reply_thread
parent_dd_file: dd_xxx_2022-09-15_update-1-7-1-release.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: CK3 - Update 1.7.1 - Release
dd_date: 2022-09-15
expansion: Friends and Foes
patch: Patch 1.7 (Bastion)
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 3
reply_count: 50
participant_count: 34
reply_date_first: 2022-09-15
reply_date_last: 2022-09-23
body_word_count: 2818
inline_image_count: 0
quoted_span_count: 26
extraction_rationale: |
  Full reply thread captured live via Claude in Chrome (article.message bodies).
  Quote blocks split into artifact:quote spans and excluded from word counts.
  Usernames replaced by stable per-thread participant ids; the dev-diary OP is
  excluded (see parent_dd_file).
notes_for_analyst: |
  Community-voice counterpart to the linked dev diary. Strip YAML + artifact
  comments before tokenizing, exactly as for dd_*.md.
---

# Reply thread — CK3 - Update 1.7.1 - Release

*50 replies from 34 participants across 3 pages*

## Reply 1 — participant_001 · 2022-09-15 · post-28477008

Howdy all! Today we have released Update 1.7.1 which includes a lot of changes to issues that you have been reporting and a few that we found on our own! Please note that we are aware of the "Missing Faces" issue that some of our Community are facing and while it is not being addressed with 1.7.1, there is an update HERE! Without much further ado, here is the changelog: Spoiler: 1.7.1 Changelog AI: AI can no longer hire and fire court position in the same decision cycle, this should fix the issue where AIs could end up in massive prestige deficits Balance: Slightly relaxed requirements for Reviving Taltoism to make it not entirely impossible in 1066 Crusade Targeting - Fixed so that Crusades check for current military strength when excluding target kingdoms instead of max military strength Crusade Targeting - Completely rebalanced Crusade Kingdom Selection; while Jerusalem will still be the most attractive target (for Christians), there will now be much more variation in targets and a faith will tend to defend what is assigned to be their Heartlands to a much greater degree Crusade Targeting - Distance is now a much greater factor when determining a crusade target Crusade Targeting - Catholic Crusades are now much less likely to select a kingdom in the African interior, and slightly less likely to pick a north African kingdom (if the Holy Land is taken, we want the crusades to focus on going deeper into the middle east rather than to die from attrition in the Sahara) Bugfix: Fixed crashes related to loading save files from previous game versions Crusade Targeting - Fixed so that Crusades cannot target an area below 5 counties in size AI House members in Feuds will now be much more likely to start schemes against their enemies Characters will now be more reluctant to allow Feud enemies to raise their children Characters will now be more likely to join schemes against Feud house members Added explanation of score tooltip when ending a Feud Feuds can now only be started against Houses with at least 5 adult members and with Heads within one title tier of your own Added 25 year cooldown between Feuds Reduced frequency of Feud start events Added explanation of Feud reward modifiers to encyclopedia entry Fixed Feuds starting from murders where the murderer is still a secret Fixed an issue where Unpredictable Economical AI's didn't build enough new holdings Handle dead/alive for memories more consistently Fixed an issue where Cautious Economical AI's weren't cautious enough in the early stages of the game Fixed yearly.9110 missing an equals sign, also adjusted down dynasty prestige Fixed a missing equals sign in the Loyalty trait definition Fixed bp1_yearly.5704 missing an is_adult check Fixed pilgrimage.6007 so it does not fire for blind characters Fixed issue where Feud scale tip tooltips would be repeated Added additional missing checks for the A Man in Our Bed event Fixed missing adult and other checks in the A Man in Our Bed event Fixed Guanche Vaulter Infantry leaping across the world as mercenaries Fixed rivals not being less likely to accept alliance proposals Fixed Vengeance event firing alongside At My Mercy for Norse characters who captured a rival in battle Fixed incorrectly displayed/repeating Coat of Arms during longer sessions Localization: Fixed MAX_RECURSIVE_DEPTH error in Chinese localization Fixed grammar of Ibn Marwan of Badajoz's bookmark character With that out of the way, keep up the reports, keep checking out our socials for further info, and we will keep working hard on our next updates and news for the future! -SP

## Reply 2 — participant_002 · 2022-09-15 · post-28477327

Could you please fix these two bug 1.cant form the archduchy of austria because the requirement is that the emperor isnt of my dynasty and doesnt check out 2.the sliders in the coat if arms detail configuration are a little bit offscreen so i cant make them bigger or mive them to the right

## Reply 3 — participant_002 · 2022-09-15 · post-28477329

And please add a long term option for saving abd selecting more than one dna for costume character

## Reply 4 — participant_003 · 2022-09-15 · post-28477342

<!-- artifact:quote:start -->
> PDX_Pariah said: Slightly relaxed requirements for Reviving Taltoism to make it not entirely impossible in 1066 Click to expand...
<!-- artifact:quote:end -->
SICK thanks so much for the quick turnaround on this report!

## Reply 5 — participant_004 · 2022-09-15 · post-28477479

Please, Chinese Font error is still there during a longer session

## Reply 6 — participant_005 · 2022-09-15 · post-28477482

Please review the following topic: When I use the portrait editor in the debug console, there is a submenu called children. I can generate children of two characters there. The generation itself works fine, but I can't do anything with the characters. I can't edit them or access their DNA string in any way. Before update 1.7 I had this "c" button but then it disappeared Any idea why? I already removed all modifications and reinstalled the game, but I still don't see any button.

## Reply 7 — participant_006 · 2022-09-15 · post-28477539

<!-- artifact:quote:start -->
> Fixed rivals not being less likely to accept alliance proposals Click to expand...
<!-- artifact:quote:end -->
Thank you, great to see both Rivalry and Feud modifier for alliances factored in now! Last week it was +30 in this case, now -50, as it should be. { "lightbox_close": "Close", "lightbox_next": "Next", "lightbox_previous": "Previous", "lightbox_error": "The requested content cannot be loaded. Please try again later.", "lightbox_start_slideshow": "Start slideshow", "lightbox_stop_slideshow": "Stop slideshow", "lightbox_full_screen": "Full screen", "lightbox_thumbnails": "Thumbnails", "lightbox_download": "Download", "lightbox_share": "Share", "lightbox_zoom": "Zoom", "lightbox_new_window": "New window", "lightbox_toggle_sidebar": "Toggle sidebar" }

## Reply 8 — participant_007 · 2022-09-15 · post-28477591

I had an event as a child just now where my Flamen asked me to give up my stuffed toy "best friend" and instead spend time with real children and socialize. I had the option of agreeing with my Flamen and taking a negative opinion hit or gaining one of three negative traits. I'd think agreeing to give up my stuffed best friend ought to gain me a positive reaction not a negative one.

## Reply 9 — participant_008 · 2022-09-15 · post-28477630

> Fixed MAX_RECURSIVE_DEPTH error in Chinese localization If this works, it will make a big difference to players in Chinese. Here's hoping.

## Reply 10 — participant_009 · 2022-09-15 · post-28477677

Awesome, thanks for the quick bug fix!

## Reply 11 — participant_010 · 2022-09-15 · post-28477687

glad the mercenary vaulters are finally fixed.

## Reply 12 — participant_011 · 2022-09-15 · post-28477793

Stupid question: where is feud "current situation "? I ll open this new update later but in the previous one I wasnt able to find it. I'm happy with crusades support bugfix. Hope to see crusades and religion updates in the entire ck3 life cycle

## Reply 13 — participant_012 · 2022-09-15 · post-28478036

that feud tier change is probably a really good call. Its so weird when I get pop ups about the insults of some duke in Iberia against my 2nd cousins from a disinherited line of the family when I'm the Emperor of Russia.

## Reply 14 — participant_013 · 2022-09-15 · post-28478273

Will this work with last patch saves?

## Reply 15 — participant_014 · 2022-09-15 · post-28478532

What about the bug that is making the game stutter like crazy when you have a large empire? The vassalisation check is bugged, there is a mod that fixes it for now.

## Reply 16 — participant_015 · 2022-09-15 · post-28478631

<!-- artifact:quote:start -->
> Son_Of_Erebos said: What about the bug that is making the game stutter like crazy when you have a large empire? The vassalisation check is bugged, there is a mod that fixes it for now. Click to expand...
<!-- artifact:quote:end -->
Yeah, this is an extremely important bug to fix. I just tested and can say 1.7.1 hasn't fixed it yet. It's strange, because this used to be a bug that was around for a long time and eventually fixed, only to be reintroduced again with 1.7 somehow.

## Reply 17 — participant_016 · 2022-09-16 · post-28478661

<!-- artifact:quote:start -->
> Koocai said: Yeah, this is an extremely important bug to fix. I just tested and can say 1.7.1 hasn't fixed it yet. It's strange, because this used to be a bug that was around for a long time and eventually fixed, only to be reintroduced again with 1.7 somehow. Click to expand...
<!-- artifact:quote:end -->
Hmm, considering this and the CoA bug that they just re-patched out, I wonder if Paradox accidentally copied over outdated code from somewhere.

## Reply 18 — participant_017 · 2022-09-16 · post-28478730

<!-- artifact:quote:start -->
> RelVleDy said: Hmm, considering this and the CoA bug that they just re-patched out, I wonder if Paradox accidentally copied over outdated code from somewhere. Click to expand...
<!-- artifact:quote:end -->
The dev diary did mention a terrible merging accident

## Reply 19 — participant_018 · 2022-09-16 · post-28479174

<!-- artifact:quote:start -->
> Sunsteel said: Will this work with last patch saves? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> PDX_Pariah said: Bugfix: Fixed crashes related to loading save files from previous game versions Click to expand...
<!-- artifact:quote:end -->
Fortunately yes. I've tested my 1.6.1.2 ironman savegame and it works fine now with 1.7.1

## Reply 20 — participant_019 · 2022-09-16 · post-28479279

Since the 1.7.1 has been applied, I can finally use 1.6 ironman savegame, but the game is now lagging af

## Reply 21 — participant_020 · 2022-09-16 · post-28479340

I can‘t stress enough how happy I‘m about the holy war changes! Thanks a lot, Paradox

## Reply 22 — participant_021 · 2022-09-16 · post-28479366

Many thanks for the patch. I am looking forward on testing it this weekend. I really like those quick bug patches even If they won't fix everything. It is better than waiting weeks to months for one big fix.

## Reply 23 — participant_022 · 2022-09-16 · post-28479426

Excuse me, but when will the conclave and the system of political events associated with it appear?

## Reply 24 — participant_023 · 2022-09-16 · post-28479795

Does anyone still suffer from the loading crash? And is there a way too I've tried playing vanilla and still crashes

## Reply 25 — participant_024 · 2022-09-16 · post-28479796

<!-- artifact:quote:start -->
> camil0n7 said: Please review the following topic: When I use the portrait editor in the debug console, there is a submenu called children. I can generate children of two characters there. The generation itself works fine, but I can't do anything with the characters. I can't edit them or access their DNA string in any way. Before update 1.7 I had this "c" button but then it disappeared Any idea why? I already removed all modifications and reinstalled the game, but I still don't see any button. Click to expand...
<!-- artifact:quote:end -->
I assume the dna that is generated is one string. Within the debug menu you can enter that string into a character and retrieve the format used in the character designer. I would assume you can enter the child's dna there in the same way.

## Reply 26 — participant_025 · 2022-09-16 · post-28480014

<!-- artifact:quote:start -->
> Son_Of_Erebos said: What about the bug that is making the game stutter like crazy when you have a large empire? The vassalisation check is bugged, there is a mod that fixes it for now. Click to expand...
<!-- artifact:quote:end -->
Would you mind sharing which mod that is, please?

## Reply 27 — participant_026 · 2022-09-17 · post-28481336

<!-- artifact:quote:start -->
> Procyon19 said: And please add a long term option for saving abd selecting more than one dna for costume character Click to expand...
<!-- artifact:quote:end -->
The DNA is just a text string, click 'copy DNA' and then use paste function in a text file, voilá.

## Reply 28 — participant_027 · 2022-09-17 · post-28481365

Are there any performance related fixes?

## Reply 29 — participant_028 · 2022-09-17 · post-28481863

Thanks for the update.

## Reply 30 — participant_002 · 2022-09-17 · post-28481998

<!-- artifact:quote:start -->
> onepot said: The DNA is just a text string, click 'copy DNA' and then use paste function in a text file, voilá. Click to expand...
<!-- artifact:quote:end -->
Could you give me a detailed guide with files

## Reply 31 — participant_029 · 2022-09-17 · post-28482362

Hello, I wanted to ask if I may, is there a way to update the game without using Steam? I am asking because my game does not update at all even though I have the option "always keep the game updated" in the properties of the game. I uninstalled the game and then downloaded it again and the game version was 1.7.0 avx_ issue_hotfix. Thank you.

## Reply 32 — participant_013 · 2022-09-18 · post-28483350

<!-- artifact:quote:start -->
> PrimaItalia said: Hello, I wanted to ask if I may, is there a way to update the game without using Steam? I am asking because my game does not update at all even though I have the option "always keep the game updated" in the properties of the game. I uninstalled the game and then downloaded it again and the game version was 1.7.0 avx_ issue_hotfix. Thank you. Click to expand...
<!-- artifact:quote:end -->
Are you on a beta branch?

## Reply 33 — participant_029 · 2022-09-18 · post-28483401

<!-- artifact:quote:start -->
> Sunsteel said: Are you on a beta branch? Click to expand...
<!-- artifact:quote:end -->
Thanks. I was on a beta branch. I did not think of that. I did uninstall and reinstall the game but it had downloaded the previous version. I have changed the setting and now the game has updated to the live version.

## Reply 34 — participant_026 · 2022-09-19 · post-28484753

<!-- artifact:quote:start -->
> Procyon19 said: Could you give me a detailed guide with files Click to expand...
<!-- artifact:quote:end -->
Uhm, it's really simple. In the character creation screen, click 'copy DNA' to store the info in the clipboard. Open a simple text file (.txt or whatever) and in there press CTRL+V or use the right-click context menu and click 'Paste'. Now you have the text string in your text file, save it somewhere for later use. Now to use that saved information, just mark the text from the text file, press CTRL+C or use 'Copy' from right-click context menu and use 'paste DNA' in the character creation screen. I'm using Windows, not familiar with other operating systems but the principle should stay the same. Also, I'm German, so I'm only assuming the English button names, but they should be close enough I guess.

## Reply 35 — participant_024 · 2022-09-19 · post-28484867

<!-- artifact:quote:start -->
> onepot said: Uhm, it's really simple. In the character creation screen, click 'copy DNA' to store the info in the clipboard. Open a simple text file (.txt or whatever) and in there press CTRL+V or use the right-click context menu and click 'Paste'. Now you have the text string in your text file, save it somewhere for later use. Now to use that saved information, just mark the text from the text file, press CTRL+C or use 'Copy' from right-click context menu and use 'paste DNA' in the character creation screen. I'm using Windows, not familiar with other operating systems but the principle should stay the same. Also, I'm German, so I'm only assuming the English button names, but they should be close enough I guess. Click to expand...
<!-- artifact:quote:end -->
no, it is not that simple. there are two ways DNA is shown. one is a text string that looks cryptic. the ruler designer uses text that contains actual information. therefore it is necessary to take the steps I outlined above

## Reply 36 — participant_024 · 2022-09-19 · post-28485364

<!-- artifact:quote:start -->
> Procyon19 said: Could you give me a detailed guide with files Click to expand...
<!-- artifact:quote:end -->
Basic Portrait Editor Tutorial from Princes of Darkness Hello CK3 User Mod community, we wrote this for our Princes of Darkness modding community to start work of developing portraits for our more than a thousand canon characters, but we thought it might be helpful to some of you as well! You do not... forum.paradoxplaza.com I assume the DNA the TO extracted from the children is the "DNA string". In that menu this can be converted into the "persistent DNA" which can be use in character editor. This is the same guy as DNA string Spoiler: Dietwin von Lengefeld extracted from the game e0sp52VZWVbJmCO3AYYAhgGGAIYAegB6AHUAdQB4AXgBggCCAYYAhgGFAYUBgwGDAZUAlQGlAaUBlwCXAHUAdQBqAWoAdgF2AYgAiACIAYgBjAGMAHIAcgByAHIBhgGGAaUApQByAXIBgQGBAaUApQByAXIBiQGJAYwAjAGKAYoAWQBZAZgAmAB/AX8AHQAhAAcBKgAnABwAMAEUACsAEwAdAHoBEQBYAVcAKgHRAAYBlgALAC8BIwAmASIANwAGAUIABAARAAwBAAAXABUAMAALAUoAJQBTAAUBJQEBAS0AAwEaAAwAKQEWAToAFwANAAoAFQAbARUBkwE1AB8BDAEbAFMBPwAlASgAEQF6ABsBEgB9AAkBDwFPAAMBIwAOAQEBQgBIAQ8BJQEtAAAAEQBfAXUD9QQWAQoACwAPAQIA8gBmAhcDBwA9AnsBRQAWABQAigDQADYDVwMsACQBywAbAC0CAAIAA40AkAGCAXcCfgF+BgAHAAhYAsIBEAGKB2wD5wKLATkAlQBkAIAAWwB/AH8A5gDmAAAAAAESARI= Spoiler: Dietwin von Lengefeld transcribed into persitent DNA TODO_choose_portait_key={ type=male id=0 age=0.250000 genes={ hair_color={ 123 75 41 231 } skin_color={ 101 89 89 86 } eye_color={ 201 152 35 183 } gene_chin_forward={ "chin_forward_pos" 134 "chin_forward_neg" 134 } gene_chin_height={ "chin_height_pos" 134 "chin_height_neg" 134 } gene_chin_width={ "chin_width_neg" 122 "chin_width_neg" 122 } gene_eye_angle={ "eye_angle_neg" 117 "eye_angle_neg" 117 } gene_eye_depth={ "eye_depth_neg" 120 "eye_depth_pos" 120 } gene_eye_height={ "eye_height_pos" 130 "eye_height_neg" 130 } gene_eye_distance={ "eye_distance_pos" 134 "eye_distance_neg" 134 } gene_eye_shut={ "eye_shut_pos" 133 "eye_shut_pos" 133 } gene_forehead_angle={ "forehead_angle_pos" 131 "forehead_angle_pos" 131 } gene_forehead_brow_height={ "forehead_brow_height_pos" 149 "forehead_brow_height_neg" 149 } gene_forehead_roundness={ "forehead_roundness_pos" 165 "forehead_roundness_pos" 165 } gene_forehead_width={ "forehead_width_pos" 151 "forehead_width_neg" 151 } gene_forehead_height={ "forehead_height_neg" 117 "forehead_height_neg" 117 } gene_head_height={ "head_height_neg" 106 "head_height_pos" 106 } gene_head_width={ "head_width_neg" 118 "head_width_pos" 118 } gene_head_profile={ "head_profile_pos" 136 "head_profile_neg" 136 } gene_head_top_height={ "head_top_height_neg" 136 "head_top_height_pos" 136 } gene_head_top_width={ "head_top_width_pos" 140 "head_top_width_pos" 140 } gene_jaw_angle={ "jaw_angle_neg" 114 "jaw_angle_neg" 114 } gene_jaw_forward={ "jaw_forward_neg" 114 "jaw_forward_neg" 114 } gene_jaw_height={ "jaw_height_pos" 134 "jaw_height_pos" 134 } gene_jaw_width={ "jaw_width_pos" 165 "jaw_width_neg" 165 } gene_mouth_corner_depth={ "mouth_corner_depth_neg" 114 "mouth_corner_depth_pos" 114 } gene_mouth_corner_height={ "mouth_corner_height_pos" 129 "mouth_corner_height_pos" 129 } gene_mouth_forward={ "mouth_forward_pos" 165 "mouth_forward_neg" 165 } gene_mouth_height={ "mouth_height_neg" 114 "mouth_height_pos" 114 } gene_mouth_width={ "mouth_width_pos" 137 "mouth_width_pos" 137 } gene_mouth_upper_lip_size={ "mouth_upper_lip_size_pos" 140 "mouth_upper_lip_size_neg" 140 } gene_mouth_lower_lip_size={ "mouth_lower_lip_size_pos" 138 "mouth_lower_lip_size_pos" 138 } gene_mouth_open={ "mouth_open_neg" 89 "mouth_open_neg" 89 } gene_neck_length={ "neck_length_pos" 152 "neck_length_neg" 152 } gene_neck_width={ "neck_width_neg" 127 "neck_width_pos" 127 } gene_bs_cheek_forward={ "cheek_forward_neg" 29 "cheek_forward_neg" 33 } gene_bs_cheek_height={ "cheek_height_neg" 7 "cheek_height_pos" 42 } gene_bs_cheek_width={ "cheek_width_neg" 39 "cheek_width_neg" 28 } gene_bs_ear_angle={ "ear_angle_neg" 48 "ear_angle_pos" 20 } gene_bs_ear_inner_shape={ "ear_inner_shape_pos" 43 "ear_inner_shape_pos" 19 } gene_bs_ear_bend={ "ear_lower_bend_pos" 29 "ear_lower_bend_pos" 122 } gene_bs_ear_outward={ "ear_outward_pos" 17 "ear_outward_neg" 88 } gene_bs_ear_size={ "ear_size_pos" 87 "ear_size_neg" 42 } gene_bs_eye_corner_depth={ "eye_corner_depth_pos" 209 "eye_corner_depth_neg" 6 } gene_bs_eye_fold_shape={ "eye_fold_shape_pos" 150 "eye_fold_shape_neg" 11 } gene_bs_eye_size={ "eye_size_neg" 47 "eye_size_pos" 35 } gene_bs_eye_upper_lid_size={ "eye_upper_lid_size_neg" 38 "eye_upper_lid_size_pos" 34 } gene_bs_forehead_brow_curve={ "forehead_brow_curve_neg" 55 "forehead_brow_curve_neg" 6 } gene_bs_forehead_brow_forward={ "forehead_brow_forward_pos" 66 "forehead_brow_forward_neg" 4 } gene_bs_forehead_brow_inner_height={ "forehead_brow_inner_height_neg" 17 "forehead_brow_inner_height_neg" 12 } gene_bs_forehead_brow_outer_height={ "forehead_brow_outer_height_pos" 0 "forehead_brow_outer_height_neg" 23 } gene_bs_forehead_brow_width={ "forehead_brow_width_neg" 21 "forehead_brow_width_neg" 48 } gene_bs_jaw_def={ "jaw_def_neg" 11 "jaw_def_pos" 74 } gene_bs_mouth_lower_lip_def={ "mouth_lower_lip_def_pos" 37 "mouth_lower_lip_def_pos" 83 } gene_bs_mouth_lower_lip_full={ "mouth_lower_lip_full_neg" 5 "mouth_lower_lip_full_pos" 37 } gene_bs_mouth_lower_lip_pad={ "mouth_lower_lip_pad_pos" 1 "mouth_lower_lip_pad_pos" 45 } gene_bs_mouth_lower_lip_width={ "mouth_lower_lip_width_neg" 3 "mouth_lower_lip_width_pos" 26 } gene_bs_mouth_philtrum_def={ "mouth_philtrum_def_pos" 12 "mouth_philtrum_def_pos" 41 } gene_bs_mouth_philtrum_shape={ "mouth_philtrum_shape_pos" 22 "mouth_philtrum_shape_pos" 58 } gene_bs_mouth_philtrum_width={ "mouth_philtrum_width_neg" 23 "mouth_philtrum_width_neg" 13 } gene_bs_mouth_upper_lip_def={ "mouth_upper_lip_def_pos" 10 "mouth_upper_lip_def_pos" 21 } gene_bs_mouth_upper_lip_full={ "mouth_upper_lip_full_neg" 27 "mouth_upper_lip_full_pos" 21 } gene_bs_mouth_upper_lip_profile={ "mouth_upper_lip_profile_pos" 147 "mouth_upper_lip_profile_pos" 53 } gene_bs_mouth_upper_lip_width={ "mouth_upper_lip_width_neg" 31 "mouth_upper_lip_width_pos" 12 } gene_bs_nose_forward={ "nose_forward_pos" 27 "nose_forward_neg" 83 } gene_bs_nose_height={ "nose_height_pos" 63 "nose_height_neg" 37 } gene_bs_nose_length={ "nose_length_pos" 40 "nose_length_neg" 17 } gene_bs_nose_nostril_height={ "nose_nostril_height_pos" 122 "nose_nostril_height_neg" 27 } gene_bs_nose_nostril_width={ "nose_nostril_width_pos" 18 "nose_nostril_width_neg" 125 } gene_bs_nose_profile={ "nose_profile_neg" 9 "nose_profile_pos" 15 } gene_bs_nose_ridge_angle={ "nose_ridge_angle_pos" 79 "nose_ridge_angle_neg" 3 } gene_bs_nose_ridge_width={ "nose_ridge_width_pos" 35 "nose_ridge_width_neg" 14 } gene_bs_nose_size={ "nose_size_pos" 1 "nose_size_pos" 66 } gene_bs_nose_tip_angle={ "nose_tip_angle_neg" 72 "nose_tip_angle_pos" 15 } gene_bs_nose_tip_forward={ "nose_tip_forward_pos" 37 "nose_tip_forward_pos" 45 } gene_bs_nose_tip_width={ "nose_tip_width_neg" 0 "nose_tip_width_neg" 17 } face_detail_cheek_def={ "cheek_def_01" 95 "cheek_def_02" 117 } face_detail_cheek_fat={ "cheek_fat_04_pos" 245 "cheek_fat_01_neg" 22 } face_detail_chin_cleft={ "chin_dimple" 10 "chin_cleft" 11 } face_detail_chin_def={ "chin_def_neg" 15 "chin_def" 2 } face_detail_eye_lower_lid_def={ "eye_lower_lid_def" 242 "eye_lower_lid_def" 102 } face_detail_eye_socket={ "eye_socket_03" 23 "eye_socket_color_01" 7 } face_detail_nasolabial={ "nasolabial_01" 61 "nasolabial_03" 123 } face_detail_nose_ridge_def={ "nose_ridge_def_neg" 69 "nose_ridge_def_pos" 22 } face_detail_nose_tip_def={ "nose_tip_def" 20 "nose_tip_def" 138 } face_detail_temple_def={ "temple_def" 208 "temple_def" 54 } expression_brow_wrinkles={ "brow_wrinkles_04" 87 "brow_wrinkles_04" 44 } expression_eye_wrinkles={ "eye_wrinkles_01" 36 "eye_wrinkles_02" 203 } expression_forehead_wrinkles={ "forehead_wrinkles_01" 27 "forehead_wrinkles_01" 45 } expression_other={ "cheek_wrinkles_both_01" 0 "cheek_wrinkles_both_01" 0 } complexion={ "complexion_4" 141 "complexion_1" 144 } gene_height={ "normal_height" 130 "normal_height" 119 } gene_bs_body_type={ "body_fat_head_fat_medium" 126 "body_fat_head_fat_low" 126 } gene_bs_body_shape={ "body_shape_pear_half" 0 "body_shape_pear_full" 0 } gene_bs_bust={ "bust_shape_3_full" 88 "bust_default" 194 } gene_age={ "old_2" 16 "old_2" 138 } gene_eyebrows_shape={ "far_spacing_low_thickness" 108 "avg_spacing_low_thickness" 231 } gene_eyebrows_fullness={ "layer_2_high_thickness" 139 "layer_2_avg_thickness" 57 } gene_body_hair={ "body_hair_sparse" 149 "body_hair_sparse" 100 } gene_hair_type={ "hair_straight" 128 "hair_straight" 91 } gene_baldness={ "no_baldness" 127 "no_baldness" 127 } eye_accessory={ "normal_eyes" 230 "normal_eyes" 230 } teeth_accessory={ "normal_teeth" 0 "normal_teeth" 0 } eyelashes_accessory={ "normal_eyelashes" 18 "normal_eyelashes" 18 } } entity={ 0 0 } } { "lightbox_close": "Close", "lightbox_next": "Next", "lightbox_previous": "Previous", "lightbox_error": "The requested content cannot be loaded. Please try again later.", "lightbox_start_slideshow": "Start slideshow", "lightbox_stop_slideshow": "Stop slideshow", "lightbox_full_screen": "Full screen", "lightbox_thumbnails": "Thumbnails", "lightbox_download": "Download", "lightbox_share": "Share", "lightbox_zoom": "Zoom", "lightbox_new_window": "New window", "lightbox_toggle_sidebar": "Toggle sidebar" }

## Reply 37 — participant_030 · 2022-09-19 · post-28485458

One thing I've noticed with the new crusade targeting is that the AI will do things like target tribal Lithuania. I know the Northern Crusades are a thing in real life and all, but it feels like an unintended consequence for a crusade to create a new tribal kingdom, and the game isn't really set up to handle the resulting inheritances in a coherent way. Maybe it would be better if crusades and other great holy wars didn't target kingdoms which consist of tribal holdings?

## Reply 38 — participant_026 · 2022-09-19 · post-28485530

<!-- artifact:quote:start -->
> Dietwin von Lengenfeld said: no, it is not that simple. there are two ways DNA is shown. one is a text string that looks cryptic. the ruler designer uses text that contains actual information. therefore it is necessary to take the steps I outlined above Click to expand...
<!-- artifact:quote:end -->
You are talking about something else, my post wasn't directed at you or your issue.

## Reply 39 — participant_031 · 2022-09-20 · post-28485904

When I run an observe game, the games crashes (to desktop) every-time (at various times) within the first 200-300 years (starting at 867). This did not happen before. Are others seeing this same? (Update: This is the Mac version)

## Reply 40 — participant_002 · 2022-09-20 · post-28486024

<!-- artifact:quote:start -->
> onepot said: Uhm, it's really simple. In the character creation screen, click 'copy DNA' to store the info in the clipboard. Open a simple text file (.txt or whatever) and in there press CTRL+V or use the right-click context menu and click 'Paste'. Now you have the text string in your text file, save it somewhere for later use. Now to use that saved information, just mark the text from the text file, press CTRL+C or use 'Copy' from right-click context menu and use 'paste DNA' in the character creation screen. I'm using Windows, not familiar with other operating systems but the principle should stay the same. Also, I'm German, so I'm only assuming the English button names, but they should be close enough I guess. Click to expand...
<!-- artifact:quote:end -->
Lol no way that works XD Thx i will try it.

## Reply 41 — participant_024 · 2022-09-20 · post-28486238

<!-- artifact:quote:start -->
> onepot said: You are talking about something else, my post wasn't directed at you or your issue. Click to expand...
<!-- artifact:quote:end -->
Firstly, I did not have an issue, secondly you were giving Procyon19 false advise. I doubt you have any clue.

## Reply 42 — participant_024 · 2022-09-20 · post-28486239

<!-- artifact:quote:start -->
> Procyon19 said: Lol no way that works XD Thx i will try it. Click to expand...
<!-- artifact:quote:end -->
Did you read my posts? Onepots "solutions" are misleading.

## Reply 43 — participant_002 · 2022-09-20 · post-28487129

<!-- artifact:quote:start -->
> Dietwin von Lengenfeld said: Did you read my posts? Onepots "solutions" are misleading. Click to expand...
<!-- artifact:quote:end -->
yes but not as i replyed to the post.

## Reply 44 — participant_002 · 2022-09-20 · post-28487131

<!-- artifact:quote:start -->
> Dietwin von Lengenfeld said: Did you read my posts? Onepots "solutions" are misleading. Click to expand...
<!-- artifact:quote:end -->
have you a diffrent solution?

## Reply 45 — participant_024 · 2022-09-20 · post-28487151

<!-- artifact:quote:start -->
> Procyon19 said: have you a diffrent solution? Click to expand...
<!-- artifact:quote:end -->
So basically you did not read my posts. Everything you seem to need is layed out here. I am not babysitting you in a one-to-one when you seem to have chosen to ignore the bigger parts of this thread.

## Reply 46 — participant_032 · 2022-09-20 · post-28487547

In ibéria the problem still the same, prist cant convert some areas in Portugal....

## Reply 47 — participant_002 · 2022-09-21 · post-28488092

<!-- artifact:quote:start -->
> Dietwin von Lengenfeld said: So basically you did not read my posts. Everything you seem to need is layed out here. I am not babysitting you in a one-to-one when you seem to have chosen to ignore the bigger parts of this thread. Click to expand...
<!-- artifact:quote:end -->
I have read it but it didnt quit understand what i should do.this was before the character editor and about a mod. So i must have the debug tool and copy the dna off an existing creation of mine and save the dna in a text dokument and when i need it i can just copy it in desktop and use it in game right ?

## Reply 48 — participant_014 · 2022-09-22 · post-28491459

<!-- artifact:quote:start -->
> unmerged(739950) said: Would you mind sharing which mod that is, please? Click to expand...
<!-- artifact:quote:end -->
Steam Workshop::1.7 Stutter Fix steamcommunity.com In the steam workshop page there is a link to the paradox forum post. The zip file download is at the bottom of the page if you are using the gamepass version.

## Reply 49 — participant_033 · 2022-09-23 · post-28494202

I just did a fresh install of the game on my system and it appears that GUI scaling is set to 50% (the lowest) by default. Not really a bug, but it was odd to have the menu be all kinds of tiny on first launch.

## Reply 50 — participant_034 · 2022-09-23 · post-28494225

<!-- artifact:quote:start -->
> Blue Three said: I just did a fresh install of the game on my system and it appears that GUI scaling is set to 50% (the lowest) by default. Not really a bug, but it was odd to have the menu be all kinds of tiny on first launch. Click to expand...
<!-- artifact:quote:end -->
This happened to me as well. I think it might be a bug.

