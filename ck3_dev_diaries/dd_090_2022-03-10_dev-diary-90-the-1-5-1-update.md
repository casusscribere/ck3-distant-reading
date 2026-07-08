---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1514785/"
forum_thread_id: 1514785
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 90
title: "CK3 Dev Diary #90: The 1.5.1 Update"
dd_date: 2022-03-10
author_handle: rageair
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 4657
inline_image_count: 39
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1514785'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1889.jpg?1646910483
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_584_to_588
    action: preserved_and_flagged
    counts:
      Like: 135
      Love: 44
      (unlabeled — rendered as base64 data URI): 4
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_596_to_704
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_705_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1889.jpg?1646910483)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #90: The 1.5.1 Update

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Mar 10, 2022](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-90-the-1-5-1-update.1514785/)
<!-- artifact:thread_metadata:end -->

Greetings!  

Royal Court has been out for a while now, and it’s been great to see everything you’ve done with it - fascinating Coat of Arms designs, impressive courts, intriguing cultural hybrids… keep it coming! Seeing how creative you are with the new tools gives us a lot of energy!  

The CoA designer has even given rise to a CK3 Heraldry Reddit board! If you want to check it out, here’s a link:  
<https://www.reddit.com/r/CKHeraldry/>  

We also want to show some of the fantastic CoA creations we’ve seen over the past weeks right here in the DevDiary, of course! Feel free to scroll through them at your own pace (for those of you who are impatient, the Changelog for 1.5.1 is below them!).  



[![1234thomas5.png](https://forumcontent.paradoxplaza.com/thumbnail/public/803983/1234thomas5.png "1234thomas5.png")](https://forumcontent.paradoxplaza.com/public/803983/1234thomas5.png) [![alexhesse7617.png](https://forumcontent.paradoxplaza.com/thumbnail/public/803984/alexhesse7617.png "alexhesse7617.png")](https://forumcontent.paradoxplaza.com/public/803984/alexhesse7617.png) [![arzen353.png](https://forumcontent.paradoxplaza.com/thumbnail/public/803985/arzen353.png "arzen353.png")](https://forumcontent.paradoxplaza.com/public/803985/arzen353.png) [![CKHeraldry.png](https://forumcontent.paradoxplaza.com/thumbnail/public/803986/CKHeraldry.png "CKHeraldry.png")](https://forumcontent.paradoxplaza.com/public/803986/CKHeraldry.png)  
[![DerLarge.png](https://forumcontent.paradoxplaza.com/thumbnail/public/803987/DerLarge.png "DerLarge.png")](https://forumcontent.paradoxplaza.com/public/803987/DerLarge.png) [![dirty-hurdy-gurdy.png](https://forumcontent.paradoxplaza.com/thumbnail/public/803989/dirty-hurdy-gurdy.png "dirty-hurdy-gurdy.png")](https://forumcontent.paradoxplaza.com/public/803989/dirty-hurdy-gurdy.png) [![Givemeajackson.jpg](https://forumcontent.paradoxplaza.com/thumbnail/public/803991/Givemeajackson.jpg "Givemeajackson.jpg")](https://forumcontent.paradoxplaza.com/public/803991/Givemeajackson.jpg) [![HeyImPoro.png](https://forumcontent.paradoxplaza.com/thumbnail/public/803993/HeyImPoro.png "HeyImPoro.png")](https://forumcontent.paradoxplaza.com/public/803993/HeyImPoro.png) [![MrPoKa.png](https://forumcontent.paradoxplaza.com/thumbnail/public/803994/MrPoKa.png "MrPoKa.png")](https://forumcontent.paradoxplaza.com/public/803994/MrPoKa.png)  
[![Forums.png](https://forumcontent.paradoxplaza.com/thumbnail/public/803992/Forums.png "Forums.png")](https://forumcontent.paradoxplaza.com/public/803992/Forums.png) [![obamium1313.png](https://forumcontent.paradoxplaza.com/thumbnail/public/803995/obamium1313.png "obamium1313.png")](https://forumcontent.paradoxplaza.com/public/803995/obamium1313.png) [![OXPEHETb_KAK_KPYTO.png](https://forumcontent.paradoxplaza.com/thumbnail/public/803996/OXPEHETb_KAK_KPYTO.png "OXPEHETb_KAK_KPYTO.png")](https://forumcontent.paradoxplaza.com/public/803996/OXPEHETb_KAK_KPYTO.png) [![pasted image 0.png](https://forumcontent.paradoxplaza.com/thumbnail/public/803997/pasted image 0.png "pasted image 0.png")](<https://forumcontent.paradoxplaza.com/public/803997/pasted image 0.png>) [![SirFireHydrant.png](https://forumcontent.paradoxplaza.com/thumbnail/public/803999/SirFireHydrant.png "SirFireHydrant.png")](https://forumcontent.paradoxplaza.com/public/803999/SirFireHydrant.png) [![WaferDisastrous.png](https://forumcontent.paradoxplaza.com/thumbnail/public/804000/WaferDisastrous.png "WaferDisastrous.png")](https://forumcontent.paradoxplaza.com/public/804000/WaferDisastrous.png)  
[![What Hedgehog3443.jpg](https://forumcontent.paradoxplaza.com/thumbnail/public/804001/What Hedgehog3443.jpg "What Hedgehog3443.jpg")](<https://forumcontent.paradoxplaza.com/public/804001/What Hedgehog3443.jpg>) [![woomy6062.png](https://forumcontent.paradoxplaza.com/thumbnail/public/804002/woomy6062.png "woomy6062.png")](https://forumcontent.paradoxplaza.com/public/804002/woomy6062.png)  
[![Devonesis.png](https://forumcontent.paradoxplaza.com/thumbnail/public/803988/Devonesis.png "Devonesis.png")](https://forumcontent.paradoxplaza.com/public/803988/Devonesis.png)​


A special shout out to Twitter User [canyoupassthepi](https://twitter.com/canyoupassthepi?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor) for these fantastic creations:  


[![canyoupassthepi.png](https://forumcontent.paradoxplaza.com/thumbnail/public/803982/canyoupassthepi.png "canyoupassthepi.png")](https://forumcontent.paradoxplaza.com/public/803982/canyoupassthepi.png)[![canyoupassthepi6.png](https://forumcontent.paradoxplaza.com/thumbnail/public/803977/canyoupassthepi6.png "canyoupassthepi6.png")](https://forumcontent.paradoxplaza.com/public/803977/canyoupassthepi6.png)  
[![canyoupassthepi3.png](https://forumcontent.paradoxplaza.com/thumbnail/public/803980/canyoupassthepi3.png "canyoupassthepi3.png")](https://forumcontent.paradoxplaza.com/public/803980/canyoupassthepi3.png)[![canyoupassthepi2.png](https://forumcontent.paradoxplaza.com/thumbnail/public/803981/canyoupassthepi2.png "canyoupassthepi2.png")](https://forumcontent.paradoxplaza.com/public/803981/canyoupassthepi2.png)  
[![canyoupassthepi4.png](https://forumcontent.paradoxplaza.com/thumbnail/public/803979/canyoupassthepi4.png "canyoupassthepi4.png")](https://forumcontent.paradoxplaza.com/public/803979/canyoupassthepi4.png)  
[![canyoupassthepi5.png](https://forumcontent.paradoxplaza.com/thumbnail/public/803978/canyoupassthepi5.png "canyoupassthepi5.png")](https://forumcontent.paradoxplaza.com/public/803978/canyoupassthepi5.png)​



In the team, we’ve been hard at work on the upcoming 1.5.1 update - there’s a lot in it (check out the changelog below)! We’ve been following your reports and listening to your feedback (if you’re having issues, make sure to report them in the bug forums!). We’re addressing many issues, and we’re even adding some more content! Here are a few examples of new stuff we’re adding:  

Firstly, we've spent a lot of time improving the lighting and shadows of all court scenes. Here's a sample of a few rooms (before is to the left, after to the right):  


![indian_2.png](https://forumcontent.paradoxplaza.com/public/803971/indian_2.png "indian_2.png")


![indian_1.png](https://forumcontent.paradoxplaza.com/public/803972/indian_1.png "indian_1.png")


![mena_1.png](https://forumcontent.paradoxplaza.com/public/803973/mena_1.png "mena_1.png")


![mena_3.png](https://forumcontent.paradoxplaza.com/public/803974/mena_3.png "mena_3.png")


![medi_3.png](https://forumcontent.paradoxplaza.com/public/803975/medi_3.png "medi_3.png")


![western_2.png](https://forumcontent.paradoxplaza.com/public/803976/western_2.png "western_2.png")



We're also adding some more artifact 3D models, of which the Throne of Solomon truly towers above the rest!:  


![throne_of_solomon.png](https://forumcontent.paradoxplaza.com/public/803970/throne_of_solomon.png "throne_of_solomon.png")


![anton_patch_weapons.jpg](https://forumcontent.paradoxplaza.com/public/803969/anton_patch_weapons.jpg "anton_patch_weapons.jpg")


![mediterranean_axe.jpg](https://forumcontent.paradoxplaza.com/public/803968/mediterranean_axe.jpg "mediterranean_axe.jpg")


![Olifant.png](https://forumcontent.paradoxplaza.com/public/803967/Olifant.png "Olifant.png")


*Olifant*  

We're adding some new events, here's a sample (don't want to spoil everything, of course!):  


![image (161).png](https://forumcontent.paradoxplaza.com/public/803962/image (161).png "image (161).png")


![image (162).png](https://forumcontent.paradoxplaza.com/public/803963/image (162).png "image (162).png")


![image (163).png](https://forumcontent.paradoxplaza.com/public/803964/image (163).png "image (163).png")


![image (165).png](https://forumcontent.paradoxplaza.com/public/803965/image (165).png "image (165).png")


![image (170).png](https://forumcontent.paradoxplaza.com/public/803966/image (170).png "image (170).png")



And here’s the changelog (hopefully we’ve not forgotten to add anything!):  

Spoiler: 1.5.1 Changelog

###################  
# Balance  
###################  
- AI's will now leave factions more quickly when they are pleased with you as their liege  
- AI's will no longer press factions for Claimants they like if they also like their current liege a lot, with a decreasing chance at higher opinions (the AI will be less likely to press a claimant they have 80 opinion of if they have 60 opinion of their liege, for example)  
- The AI now considers Faith Hostility when selecting claimants  
- AI vassals are now more likely to offer a gift when paying homage  
- Added a Game Rule (Empire Obscurity) that makes empires that control below 20% of their De Jure counties be destroyed. This should solve empires sticking around forever as micro-realms.  
- Boosted the control gain from requesting Bailiffs from your Liege in a Petition  
- Corrected the modifiers of the Cup of Jamshid  
- Forcing same vote by using a hook on an elector will now last 100 years instead of 5  
- It's now much harder to invite Inspired people to your court, and practically impossible to invite anyone who's currently being sponsored  
- Landless AI's will now try to equip artifacts you gift them via the interaction (depending on rarity)  
- Only House Heads will now demand the return of artifacts if there's only a house claim  
- Strategy Lifestyle bonus to Skirmishers has been moved to the Hit and Run Perk  
- The AI now has a 5 year cooldown towards asking to educate the players children if the player refuses  
- The AI will no longer demand artifacts from players they like a lot, and will no longer keep asking after you've refused once  
- The Chaste trait now only reduces Seduction scheme power  
- The Development progress from the Industrious Cultural Tradition is now applied at most once a year  
- The Holy Site of Qayaliq now gives Archer Cavalry bonuses  
- The Jousting Lists and Archery Ranges Duchy Buildings now give bonuses to camel, elephant, and archer cavalry  
- The Parthian Tactics perk now boosts Elephant and Camel cavalry  
- The Prestige gained from the Architect trait when it's boosted via cultural traditions have been changed from 50% to a flat +0.5/month  
- The War Camps and Hunting Grounds buildings now give Horse Archer bonuses  
- Tweaked various factors in the war for England, in order to reduce the chances of Harold winning  
- AI now moves capital to London on victory in Norman conquest, if possible  
- Northern Lords legacies can now be gotten by dynasts of any culture descendent from Norse as well as Norse culture itself.  
- Sacred Childbirth now grants piety each time a child is born and considers Pregnant a virtuous trait  
- Rebalanced artifact gift opinion gain  
- Tribal Kings and Emperors can now access the Royal Court, but it plays differently:  
- The 'Expected Grandeur' is always the same as their current Grandeur level. It cannot be above or below.  
- All Amenity Levels except the first two are blocked if playing Tribal  
- Amenity Costs are greatly increased if tribal (it was trivially cheap)  
- They only have access to one Court Type: Tribal. This one can be kept if feudalizing, but it doesn't give many benefits, and the AI will switch out of it fairly quickly.  
- All Tutorials and Game Concepts now mention Tribals and the differences they have  
- Several events that were ill-fitting for tribals will not appear for them (i.e. founding new City holdings)  



###################  
# AI  
###################  
- A unit stack wanting to resupply will spread out its subunit stacks into neighboring provinces even though said provinces might not allow resupplying, in order to try and avoid attrition.  
- AI should take player units into account for supply situation when selecting target province.  
- AI stops to raise levies with very small amount of troops  
- Allow units to ignore hostile attrition as a last resort when moving to a target in a neighboring county.  
- Added missing check for if a unit is moving or not when calculating troop strength for supply.  
- For combat evaluation, only count available subunit stacks if they are close enough.  
- If the main subunit stack is already moving, then don't deny being available for order because some units are still technically sieging.  
- Desperate AI will be more bold when selecting targets near enemy units, or when engaging enemy units.  
- Ignore non-castle provinces when giving extra score to province targets near the war goal area.  
- In Great Holy Wars the AI will be more focused on fighting about the war goal and less likely to shy away from confrontation due to numerical weakness.  
- Instructed the AI to adjust its court amenity spending in a more responsive manner  
- AI will no longer go to war for artifacts that are below masterwork, cursed or that it cannot use (like toys).  
- Lowered the AI cooldown on Pay Homage to 2 years from 3  
- Blocked the AI from overspending in Hold Court events  
- Fixed an issue where AI's could get stuck and never go home after a raid  

###################  
# Performance  
###################  
- Significantly improved the performance of all portraits in the game  
- Improved the performance of the Throne Room scenes  

###################  
# Interface  
###################  
- Add check boxes for flipping coat of arm emblems in detail edit mode  
- Budget tooltip entry on liege taxes are now shown as a breakdown instead of being within the budget tooltip  
- Fixed too low left margin for crown authority buttons  
- Recruited prisoners can now be forced to Take the Vows when Negotiating Release  
- When gifting an Artifact, the entry will now show if it is equipped  
- Added a prestige icon to council task descs  
- Empty court positions you cannot hire are now correctly sorted to the bottom of the list  
- Dead characters now have a skull next to their age  
- Renamed the Court tab to Courtiers to differentiate between it and Royal Court  
- Made text labels have more correct margins.  
- Cleaned up margins and spacings in the Faith View.  
- Changed the standard window margins so they no longer overlap the vertical lines at the sides of the window.  


###################  
# Art  
###################  
- Significantly improved the lighting and shadows in all throne rooms  
- Fixed CoA on shield artifacts being mirrored when displayed in the Royal Court  
- Added unique icons for all different types of inspirations  
- Added a new set of Legwear for Arabic clothes sets  
- Added unique art for the Throne of Solomon  
- Olifant now has a unique 3D appearance  
- African and Norse swords now have unique 3D appearance  
- Steppe Axes now have a unique 3D appearance  
- African Axes now have a unique 3D appearance  
- Steppe Maces now have a unique 3D appearance  
- Mediterranean Maces and Axes now have a unique 3D appearance  
- Added several new 2D icons to artifacts  
- Changed which texture quality settings are used on each preset level in the graphics settings menu so that the highest preset default to using the highest quality textures  
- Made it so that orthodox priests should always have a beard  
- Adjusted eyelids that were sometimes causing characters to have overly “squinty” eyes  
- Added a hybrid culture art pattern for options that can mix from two different cultures  
- Added unique CoA for HRE that reformed Roman Empire  

###################  
# Localization  
###################  
- Fixed error string in spanish inspiration sponsored toast  
- Fixed duplicate chinese character issue in court grandeur rank text  
- Fixed the alliance popup string in spanish to use correct custom loc  
- Fixed Spanish warning message for player marriage and betrothal status  
- Fixed broken string in spanish for inspiration  
- Fixed spanish localisation for intrigue window  
- Fixed 2nd and 3rd tier of beauty traits sharing Hermoso localization in Spanish, 2nd tier is now Atractivo  

###################  
# Game Content  
###################  
- Added an additional event for losing language when reached cap for max known  
- Added notification, personal artifact claim, and prestige loss after losing a war banner in battle  
- Added three additional hunt events  
- Added three additional Feast events about artifacts  
- Added a new yearly event about medieval football  
- Added a new martial lifestyle event about improvised weapons  
- Added a new Skulduggery lifestyle event about siege tactics  
- Added a new Intimidation lifestyle event about a forest of corpses  
- Added the establish Yamagate of Samarkand decision  
- Added a new set of events surrounding the Athletic trait  
- Added a new event for characters with the Lisp trait  
- Added an event where you can combine a relic artifact with a weapon artifact  
- Added the 'Passion Play' theology lifestyle event  
- Added a new murder save event about artifacts  
- Added two hostile scheme ongoing events about knowing languages  
- Added the Establish Theravada Faith Event Chain to the Burmese region  
- Added the Olifant artifact as a new artifact that can be found by adventurers  

###################  
# User Modding  
###################  
- Added can_pick trigger to Court Amenities  
- Added equip_artifact_to_owner effect  
- Added equip_artifact_to_owner_replace effect  
- Added unequip_artifact_from_owner effect  
- Court scene editor will now save only current active scene and not overwrite all the other variants  
- Allow setting any angle for pitch in court scene settings  
- Add light type controls to court scene editor  
- Add indications for lights that are enabled and with shadows  
- Add shadow fade per light source  
- Add shadow settings as sliders to scene editor  
- Allow shadow depth fade factor to be influenced by a define  
- Allow lights be affected by all shadows according to a define  
- Fix the has_icon trigger not correctly detecting a faith's icon  
- Fix the past_holder list builder being incorrectly registered as any_any_  
- Added a debug interaction for taking an artifact  

###################  
# Databases  
###################  
- Added Karelian culture in counties between Finnish and Bjarmian  
- Added more straits connecting Zeeland to surrounding counties  
- Adding missing accents to French titles  
- Fixed death date of Konrad Wettin  
- Fixed gaps in history of Sunni caliphs  
- Improved historical setup of Sankt Gallen  
- Yughur is a now divergence of the Uyghur culture  
- Öngüd is a now divergence of the Shatuo culture  
- Added Ayneha language for Sorko, Gaw, & Songhai to model one of their major gulfs from the other major cultural blocks of the western Sahel  
- Added in Rasad, the mother of the Fatimid Caliph in 1066.  
- Cleaned up loose characters in the Chola dynasty tree.  
- Reverted Uxkull to being on the Latvian side of the river  
- Made Ostmark/Brandenburg, Meissen, and Lausitz default names Polabian, changing to German  
- Lubeck and Mecklenburg now use Slavic names as default and change to German  
- Remove anachronistic names in Russia/Central Asia  
- Kanuri now speak Tubu (Saharan) rather than Chadic language  
- Muslim Volga Bolghars are now Clan instead of Feudal in 1066  
- Fixed typo in name of Otranto  
- Fixed two counties sharing name Naissos, and added Niš as a Slavic name for the real one  
- Fixed inconsistent transliteration of Rashka, and name of its capital barony  
- Replaced erroneous Wallachian Bolghar rulers in 867 with Vlachs  
- Fixed misplaced Irish strait graphics between Carrickfergus and Wigtown  
- Fixed historical ruler of Hörðaland, now is correct Eirikr  
- Fatimah is now guaranteed pious traits  
- Renamed Wilhelmshaven to more historical Jever  
- Changed Bulgarian Warrior Culture tradition to Stand and Fight  
- Added Croatian to history of Bulgarian and made Vlach formation later  
- Capital of Bulgaria is now Preslav in 867  
- Extended Avar settlement of Balaton in 867  
- Early bookmark Polish duchies now have tribal names  
- Nupe culture now speak East Kwa language  
- Fixed names of Petropavl and Petropavolsk  
- Changed the english name of Kiev to Kyiv  
- Renamed Courland to Curonia  
- Nizhny Novgorod is now called Obran Osh unless Russian, rather than only if Finnic  
- Fixed leftover Russian Slovianskan chief in 1066  
- Fixed Finnic Russian overlaps in 1066  
- Updated culture around Provence/Savoy borders to reflect Occitan and Frankish dialect spreads  
- Fixed Pecheneg feudal rulers at start  
- Tied Syriac culture to Nestorian faith in both bookmarks  
- Fixes for missing Mayzadids, Syrian borders in 1066, incorrect duke of Cappadocia in 1066, and more  
- Fixed titles used by Arpitan hybrid culture from Anjou to Provence  
- Fixed some Siguic counties which should have been Bidaic  
- Fixed some Mashriqi counties which should have been Bedouin  
- Improved historical cultural setup of Estonia/Latvia  
- Charleroi renamed to Dinant  
- Adjusted Empire borders in the area formerly covered by the South Baltic Empire  
- Improved historical setup of Langres, moved county to Duchy of Burgundy  
- Added more name equivalencies, mostly Sicilian  
- Added missing accents to French titles  
- Improved historical/cultural setup of Sicily in 1066  
- Sicilian culture now hybridizes in 950, to prevent it stating in 1066 that it hybridized in 700 when it doesn't exist in 867  
- Orissa is now a Kingdom at start in 1066  
- Added the Baudh Bhanjas in Kinjali Mandali in 1066  
- Fixed the Somavamsi family tree, and another branch of the Somavamsi dynasty now holds the western part of the kingdom in 1066.  
- Added the Chikitiki Gangas in Swetaka Mandala in 1066.  
- Qocho's vassals should now be Feudal instead of Clan  
- Updated the Unite the West Slavs decision to give you the West-Slavia title  
- Zurvanism is now a doctrine for Zoroastrians rather than a distinct faith  
- Added Behafaridism as a Zoroastrian faith  
- Changed Polabia to be named Sorbia by default  
- Fixed some historical Georgian Bagrationi characters remaining Armenian  
- Remodeled Ari faith, added historical figures in Burma, adjusted pre-existing ones  
- Switched Ari's color to 'roasted plum'  
- Cathars no longer believe in ritual suicide and now believe in reincarnation  
- Renamed Consolementum to Endura  
- Ivar the Boneless is now the youngest son of Ragnarr rather than the oldest  
- Gave Neftegorsk a more appropriate name  
- Moved Hereward and Turdifa to Count Baldwin of Flanders' court. Adjusted Hereward's traits and gave him a pressed claim on Cambridgeshire. Added "the Wake" nickname.  
- Removed Anglo-Saxon id 90029 = 'Edith' was the name of Hereward's mother, not his wife. Added Dutch id (pending) = 'Turfida' was his actual wife, raised in Saint-Omer.  
- Added a dynasty for Hereward the Wake  

###################  
# Bugfixes  
###################  
- Fixed a lot of various issues with Hold Court events which were caused by subsequent events sometimes 'stealing' characters from those ahead in the queue  
- Fixed some cases when a royal court owner dies but events are still in progress, avoiding soft-locks when visiting "dead" royal courts  
- Council task events should now fire again as intended  
- Fixed Prince Electors needing to hold titles as their primary to vote  
- Fixed Gradient Borders not updating when they should  
- Fixed cultural divergence bonuses not updating until you reload the game  
- Children will no longer vie for their lieges attention in Getting Ahead event  
- Defender value in sieges should no longer become insanely high due to changing underlying factors, and sieges should no longer lose progress when the total value falls under current progress.  
- Don't open the decision view behind the court scene when you try to hold court, just open the one decision detail view we need and close just that.  
- Electors will no longer rate themselves based on rank under Saxon Elective  
- Estonians should now have access to Varangian Adventures for owners of Northern Lords  
- Fix add_achievement_variable_effect not incrementing variables properly causing the "Seductive" achievement to never fire.  
- Fix becoming malnourished sending the toast you became obese instead.  
- Fix pending interactions not expiring after the timer runs out.  
- Fix the culture head learning sometimes being out of date in the culture window UI.  
- Fix the hold court decision window being empty if you use a two step decision, like commission artifact, and then open the royal court view.  
- Fix the no cooldown option in hybridizing cultures not correctly applying.  
- Fixed Blackmail interaction being unavailable forever if someone you were blackmailing died before they replied  
- Fixed Go Outside! event firing for celibate characters  
- Fixed Ruler Designed characters receiving banners of historical dynasties they replaced  
- Fixed Slovianskan adventurers being more likely to find Roog artifacts  
- Fixed Sultanate of Rum decision disappearing if capital was in Syria  
- Restore the Papacy in Rome should now be less hidden  
- Fixed all Anglo-Saxon counties forcibly converting to Scots if their ruler owned any counties in Scotland  
- Fixed being able to choose medical treatment for other character's prisoners  
- Fixed being able to use Revoke Title on characters you have a truce with, and thereby avoid truce by forcing war  
- Fixed broken name in artifacts made from deceased pets  
- Fixed characters living in foreign realms being invited to feasts, and having such a good time they never go back  
- Fixed creating a new cadet branch not granting claims on dynasty banner  
- Fixed duplicate Gauthier de Brienne and dynasty  
- Fixed mismatched triggers in Civic Rivalry event  
- Fixed end of partition of Danelaw and England giving Scandinavian Elective and Danelaw CoA to non-Scandinavians  
- Fixed house banner appearing twice in new court event if not a dynasty head  
- Fixed ill characters wearing helmets and coifs with their nighties  
- Fixed issues caused by being able to Petition Liege or Pay Homage while your own court events were awaiting input  
- Fixed lieges who refuse petitions losing opinion of themselves  
- Fixed misleading dynasty trigger in Archduchy of Austria decision  
- Fixed missing loc, empty councils blocking decision, and other minor issues with Petition Liege  
- Fixed not being able gift Dynasty Banners to their Dynasty Head  
- Fixed rewards and text in The King of Livonia event  
- Fixed some Electors being excluded as Candidates due to low rank under Feudal Elective succession  
- Fixed some anachronistic title names in Slovenia  
- Fixed toast from Urban Development stating a Temple is being built instead of a City  
- Fixed issues with scopes in Hero of the Frontier event  
- Improved display of Found Witch Coven decision requirements  
- Fixed clerical gender in Unconventional Preacher event  
- Holy Orders can now raise themselves when at war or pledged to a Great Holy War  
- Information Brokering event no longer includes known secrets of your own children's parentage  
- Missing text in the automatic law change notification should be corrected  
- Unified Songhai color  
- The follow up event of the Cadastre is not hiding in the court view anymore  
- Angelicas Ring will no longer be stored on the floor if found and brought to court by an adventurer  
- Improved tooltip for elective score required to change a character's vote  
- Fixed electors voting themselves based on education  
- Fixed Estonian characters using non-Estonian names in bookmarks  
- Fixed perspective of Introduce New Fashion cooldown trigger  
- Achievement Delusions of Grandeur requirements now work properly  
- Adjusted the achievement ‘The True Royal Court’ to have more intuitive triggers  
- Adjusted effect of performance-enhancing drugs  
- Children should now always lose their childhood traits/guardians upon reaching 16 years of age  
- Claim wars started via Hold Court events no longer cost prestige to declare  
- Corrected incorrectly saved scopes in Cupbearer/Bodyguard/Food Taster murder save events  
- Count only available innovations for progress towards the next era  
- Executing prisoners should no longer sometimes apply stress twice for the same trait.  
- Fix enable/disable light source checkbox in court scene editor  
- Fixed an instance of missing loc in a seduction event if the target was a wanderer  
- Fixed an issue with Claimant factions constantly forming/disbanding under certain circumstances  
- Fixed an issue with the 'The Northerner Menace' event where it could fire for invalid wars  
- Fixed button sometimes missing the name of an executioner in Public Accusation event  
- Fixed incorrect reference to the Bedchamber event picture  
- Fixed issue that would sometimes cause a bad tooltip for executing prisoners when execution happened due to an event choice  
- The game now tells you that vassals cannot become executioners  
- Fixed several hybrid names incorrectly looking for Saxon culture rather than Anglo-Saxon  
- Fixed the Beta Israel achievement being available to ruler designed characters  
- Fixed the referenced character sometimes being wrong in the text for the outcome events of the rival duel event chain  
- Hide ghost widgets visible for few frames when game map just appears on screen  
- If a scheme is exposed, your spymaster won't reveal themselves as the plotter anymore  
- Lowborn characters with a lowborn liege will no longer pretend like they're nobles for purposes of 'marrying down'  
- Republican Legacy is now properly categorized as a Regional Tradition  
- Restore missing shortcuts in the tooltips for side panel buttons in HUD  
- Revoking a lease should now only give stress once  
- The 'Land of the Bow' Tradition is now properly available to cultures with the East African Heritage  
- The Hybrid Culture notification will now only show up if you're in diplomatic range of the founder  
- The Inventory button is now hidden for dead characters  
- The standard seduction outcome event now uses the bedchamber background  
- The traditions Mountaineer Ruralism and Mountain Homes are now properly mutually exclusive  
- Vassals will no longer show up in court and complain about having imprisoned their own relatives  
- Visigothic Culture now starts with Visgothic Codes  
- You can no longer game over if your designated heir becomes a monk, eunuch or otherwise invalid for inheritance  
- You can now click the button to adopt a Court Language in the Culture View  
- You can now only rename children that are your close family, no more renaming any child in the world!  
- FP1 traditions should no longer show up if they're impossible to take  
- Celebrating another culture should no longer have missing effects  
- Excluded children from trying to murder you in The Timely Artifact  
- Fixed issues with A Sweet Farewell event  
- Fixed Marble Scepter using bone visuals, now use regalia  
- Fixed pagan faiths losing their court chaplain titles when reformed  
- A Shadow in the Night should no longer show percent chances of nothing  
- Fixed hunt hide/skull event not firing if no skull was available to make it more common, and improved/fixed other issues with hunt events  
- Fixed OOS caused by duplicate players  
- Fixed another rare OOS


For those of you who missed them, we’ve also had several videos made by excellent creators throughout the release of Royal Court. Here’s a link to a selection of them: <https://www.youtube.com/playlist?list=PL_3rLv22kp6QqJePz0lDr7uZnO8UeTM3d>  

That’s it for this time, we hope you’ll enjoy the changes we’re making in 1.5.1!

<!-- artifact:reactions:start -->
- 135 Like
- 44 Love
- 11 (unlabeled — rendered as base64 data URI)
- 11 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)**
Role: CK3 Game Director
Badges: 43
Reaction score: 11,829

*[Full game-badge icon list of 46 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
