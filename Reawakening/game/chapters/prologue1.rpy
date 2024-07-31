# Scene 1-1 [OUTSIDE THE SCHOOL] --> HISAKO IS SPEKAING TO THE PLAYERS VIA A MONOLOGUE.
label scene1_1:       
    # RESET NAME 
    $ hk.name = "???"
    $ hkmonologue.name = "???"

    # TALK ABOUT HOPE'S PEAK AND CONNECT TO ORIGINAL GAME 
    hkmonologue "Hope's Peak Academy..."

    # START MUSIC AND SHOW ACADEMY
    play music beyond_the_funk loop volume .85 
    show academy with Dissolve(2.0)

    # CONTINUE DIALOGUE 
    hkmonologue "Sanctioned by the government, this private high school was founded to develop and research the talents of exceptional teenagers,"
    hkmonologue "who would come be known as {color=#efcc00}{b}Ultimates{/b}{/color}."
    hkmonologue "It didn't matter how mundane your ability was."
    hkmonologue "As long as you were the best in your field, you were considered worthy of the title {color=#efcc00}{b}Ultimate{/b}{/color}."
    hkmonologue "From the Ultimate Doctor to the Ultimate Competitive Eater: whatever your ability was, Hope's Peak wanted you."
    hkmonologue "They say that if you graduated from Hope's Peak, you were set for the rest of your life."
    hkmonologue "Income, housing, relationships, family life, all taken care of."
    hkmonologue "A life truly worth living."
      
    # DISSOLVE 
    hide academy with Dissolve(0.65)
    

    # INTRODUCE WHAT HAPPENS TO THE REJECTS 
    hkmonologue "Now, what happen if you had an Ultimate ability, but lost your chance to succeed at life?"
    hkmonologue "You might be asking yourself, \"How do you lose a chance to attend such a prestigious institution?\""
    hkmonologue "Well, there could be a lot of reasons."
    hkmonologue "Maybe they were already on top of the world and didn't really want the added stress of schooling."
    hkmonologue "Maybe they were denied from attending due to poor grades or even not having a fully developed talent."
    hkmonologue "Or maybe...their reputation was tarnished and their acceptance was rescinded."
    hkmonologue "Whatever the circumstance may be, there are many people in this world that are still considered {color=#efcc00}{b}Ultimates{/b}{/color}, but are stuck in limbo."
    hkmonologue "If the whole point of Hope's Peak was to help use the talents of the gifted few to better themselves and society..."
    hkmonologue "...then why does it only take one failure to lose the title of {color=#efcc00}{b}Ultimate{/b}{/color}?" 
    hkmonologue "With so many people and so many talents available..."
    hkmonologue "...Why wouldn't they want to find a way to use their talents to change the world as well?"
    hkmonologue "I mean, it only takes one person's actions to change the world."

    # HOPE'S PEAK UNIVERSITY 
    hkmonologue "With the increasing amount of untapped potential, the government decided to sanction another school, this time, a college."
    hkmonologue "This university was meant to give older individuals with {color=#efcc00}{b}Ultimates{/b}{/color} a chance at redemption:"
    hkmonologue "A second chance at bettering themselves by gaining the same level education those who attended the Academy did."
    hkmonologue "With an institution designed to give second chances, you'd think the government would give the school a matching title, right?"
    hkmonologue "Not really, but on the other hand, the name still has a nostalgic tone to it!"
    hkmonologue "The school's name..."

    # SHOW UNIVERSITY
    show university_overhead with Dissolve(1.2)
    hkmonologue "{color=#efcc00}{b}Hope's Peak University{/b}{/color}."

    # TALK ABOUT IT 
    hkmonologue "Now the University is actually superior to the Academy in several ways."
    hkmonologue "First: since it is a college campus, more money was able to be procured and allocated."
    hkmonologue "This resulted in high-tech, state-of-the-art facilities, tailored to one's particular ability."
    hkmonologue "If accepted into the program, the university works alongside you to help sharpen and hone your potential {color=#efcc00}{b}Ultimate!{/b}{/color}"
    hkmonologue "Second: there is no age cap to attend the university."
    hkmonologue "It doesn't matter how old you are, as long you are an {color=#efcc00}{b}Ultimate{/b}{/color} who is in dire need of a second chance, you are eligible to apply."
    
    # HARD TO APPLY
    hkmonologue "There is, however, a caveat."
    hkmonologue "Hope's Peak University is listed as the hardest school to be accepted by in the country."
    hkmonologue "With this university, the concept of scouting doesn't exist."
    hkmonologue "It is purely based on the individual's circumstances that led them to applying in the first place."
    hkmonologue "And I would highly advise against lying on your application."
    hkmonologue "Consider that free legal advice."
    hide university_overhead with Dissolve(0.65)
    hkmonologue "Remember, the school is funded by the government, so in order to make sure their money is being used properly..."
    hkmonologue "...They want to make sure the accepted students will produce some return-on-investment."
    hkmonologue "As a result, the government has surveillance on every potential {color=#efcc00}{b}Ultimate{/b}{/color} documented, tracking their every move and action."
    hkmonologue "These records, along with each student's application, are used to judge who is deserving of a second chance at life."

    # KAWAHARA INTRODUCTION    
    hkmonologue "Now that I've given the rundown, I should actually formally introduce myself."
    $ hk.name = "Hisako Kawahara" # CHANGE NAME 
    $ hkmonologue.name = "Hisako Kawahara" # CHANGE NAME
    show hisako_halfbody_neutral 
    with fade 
    play character_voice hisako_prologue_voice_1 volume 1.2 noloop
    hk "My name is {color=#efcc00}{b}Hisako Kawahara{/b}{/color}."
    play character_voice hisako_prologue_voice_2 volume 1.2 noloop
    hk "I'm 22 years old, and I come from the Shibuya District."   
    play character_voice hisako_prologue_voice_3 volume 1.35 noloop
    hk "Oh yeah! I'm also the {color=#efcc00}{b}Ultimate Lawyer{/b}{/color}!"
    play character_voice hisako_prologue_voice_4 volume 1.2 noloop
    hk "Or well, at least I hope to be."
    play character_voice hisako_prologue_voice_5 volume 1.2 noloop
    hk "My reason for coming to this University?"
    play character_voice hisako_prologue_voice_6 volume 1.2 noloop
    hk "When I was a paralegal—"

    # ALARM GOES OFF AND SHE IS LATE
    play sfx_channel school_bell volume 1.50 noloop
    sfxText "{i}*Ding Dong Bing Bong*{/i}"
    show hisako_halfbody_upset    
    hide hisako_halfbody_neutral 
    with Dissolve(0.05)  
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff") 
    hk "Oh no! I'm almost late for the first day of Orientation!"              
    hk "Sorry, but that story will have to hold off until later."
    hk "I need to book it to the admissions office!"

    # DISSOLVE HISAKO 
    play sfx_channel running volume 1.75 noloop
    hide hisako_halfbody_upset 
    with Dissolve(0.25)

    # STUMBLING TO THE OFFICE
    hk "Excuse me!"
    hk "Pardon me!"
    hk "That's not it."
    hk "Not there either!"
    hk "Oh! Thank you very much!"
    hk "Okay, there it is!"

    # SHOW UNIVERSITY HALL 
    show university_atrium_1 with Dissolve(0.40)

    # THE RED HERRING     
    hkmonologue "Phew! Finally made it. and just on time too!"
    hkmonologue "Well, this is it."
    hkmonologue "The moment I've been waiting for!"
    hkmonologue "The opportunity to not only polish and sharpen my skills, but also learn more about myself as the {color=#efcc00}{b}Ultimate Lawyer{/b}{/color}!"
    hkmonologue "As I took the first steps into the promise of a better life, a sudden feeling enshrouded me..."
    hkmonologue "...a feeling that wasn't natural by any means."

    # FADE OUT MUSIC AND INSERT DIZZY SFX 
    stop music fadeout 1.5
    play sfx_channel ["<silence 1.10>", dizzy_sfx] noloop
    # INSERT SCHOOL BACKGROUND AND SPRIAL FROM THH HERE 
    show university_atrium_2   
    hide university_atrium_1
    with Dissolve(0.75)
    $ renpy.pause(0.01, hard=True) 
    show university_atrium_3
    hide university_atrium_2
    with Dissolve(0.75)
    $ renpy.pause(0.01, hard=True) 
    show university_atrium_4
    hide university_atrium_3
    with Dissolve(0.75)
    $ renpy.pause(0.01, hard=True) 

    # ENDING OF THE SCENE AND PASSING OUT 
    hkmonologue "Everything started to meld together, congealing into a state of absolute pandemonium."
    hkmonologue "Layer upon layer of distortion invaded my mind and body."
    hkmonologue "Nothing made sense anymore."
    hkmonologue "I was hit with an overwhelming wave of unearned comfort..."
    hkmonologue "...but suddenly shifts to my body feeling like a candle thrown into a furnace, as I immediately melt to the floor."
    hkmonologue "Overcome with these sensations..."

    # PASS OUT HERE END SCENE HERE
    hide university_atrium_4
    with Dissolve(0.25)

    # ENDING
    hkmonologue "Everything went black."
    hkmonologue "I didn't know what was happening."
    hkmonologue "Was I being kidnapped? Was I being targeted?"
    hkmonologue "But why and by who?"
    hkmonologue "Was the life I knew previously gone for good?"

    # FADE IN FIRE CRACKLE AND HKMONOLOGUE 
    play sfx_channel fireplace noloop
    show transition 
    $ renpy.pause(2.5, hard=True)
    hkmonologue "..."
    hkmonologue "..."
    hkmonologue "..."
    hkmonologue "..."

# SCENE 1-2 [ULTIMATES' LOUNGE AREA] --> HISAKO IS STARTING TO WAKE UP FROM THE WEED TRIP AND THE OTHER ULTIMATES 
# (MAINLY NOBURO AND THE BROTHERS) ARE CONVERSING AS SHE DOES.
label scene1_2:  
    # RESET NAMES 
    $ hiko.name = "???"
    $ tetsu.name = "???"
    $ naoki.name = "???"  
    $ noburo.name = "???"   
    #SCENE STARTS OFF BLACK [4 BROS TALKING AROUND HISAKO PASSED OUT]
    naoki "Hey, big bro, I don't think she's going to be waking up any time soon."
    naoki "Like, she isn't responsive in the slightest. It's really unnerving."
    # ADD STERN SFX [0:24] FOR HIKO 
    play sfx_channel stern_sfx volume 1.00 noloop
    hiko "Okay, whose bright idea was it to bring laced desserts to campus during Orientation Week, the first day no less?"
    noburo "I am so sorry, broski. I didn't mean to bring those brownies today."
    noburo "I swear I made two batches: the magic weed brownies and the normal fun ones."
    # ADD THUNDER SFX [0:21] FOR HIKO 
    play sfx_channel thunder_sfx volume 1.00 noloop
    with vpunch
    hiko "YOU LACED IT WITH WEED!?"
    hiko "Wait a minute, there's no way weed would make her react like that."
    hiko "Are you sure there wasn't acid or mushrooms in those instead?"
    tetsu "I mean, she was chowing on those like her life depended on it. Ate at least four or five."
    # ADD THUNDER SFX [0:21] FOR HIKO 
    play sfx_channel thunder_sfx volume 1.00 noloop
    with vpunch
    hiko "Why would you even make them in the first place? Classes haven't even started, my guy."
    noburo "Uh...because I wanted everyone to have such a fun time after Orientation Week was over."
    noburo "I wanted us to get turnt up on Friday, not today. Sorry for the party foul, my dudes."
    tetsu "Whatever, we can talk about the ethics of your baking mishap later, but right now, we need to make sure she didn't overdose."
    hiko "Hey you, you wanna help out and not feel so bad?"
    hiko "Why don't you go and get some water for when she does wake up."
    noburo "Right-io! I can totally do that!" # LEAVE NOBURO
    tetsu "Seriously, I don't understand that guy."
    hk "uhnnn" # HISAKO WAKING UP
    
    # ADD EXCLAMATION SFX FOR NAOKI 
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff")
    naoki "Wait! I think she's starting to come out of it!"
    naoki "Hey! Are you there? Can you hear us?"
    tetsu "I don't know if she's conscious yet."

    # ADD EXCLAMATION SFX FOR TETSU
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff")
    tetsu "No, wait! Her eyes are starting to open!"
    hk "angh...huh?" 

    # SCENE CHANGES FROM BLACK TO LIGHT WITH THE OKUDA TRIO SURROUNDING HISAKO    
    show waking_up 
    hide transition
    with Dissolve(1.5)

    # OKUDAS SPRITES WILL BE BLACK FOR THIS SECTION ONLY 
    show kazuhiko_neutral_dark with Dissolve(0.75)
    hiko "Hey there, Sleepy Head. Welcome back to the land of the living!"
    show naoki_neutral_dark 
    hide kazuhiko_neutral_dark
    with Dissolve(0.25)
    naoki "Oh man, I'm so glad to see that you're alright!"
    show tetsunori_neutral_dark
    hide naoki_neutral_dark
    with Dissolve(0.25)
    tetsu "Did you enjoy your little nap? Although, falling asleep in the Admissions Office: pretty gutsy if you ask me."
    # ADD STERN SFX [0:24] FOR NAOKI    
    show naoki_neutral_dark
    hide tetsunori_neutral_dark
    with Dissolve(0.25)
    play sfx_channel stern_sfx volume 1.00 noloop
    naoki "Come on, bro. it's not like she wanted to pass out there!"
    show tetsunori_neutral_dark
    hide naoki_neutral_dark
    with Dissolve(0.25)
    tetsu "I'm only kidding. I'm just trying to lighten the mood up a bit."
    tetsu "But seriously, glad to see you're doing okay."
    show kazuhiko_neutral_dark
    hide tetsunori_neutral_dark
    with Dissolve(0.25)
    hiko "Do you need any assistance sitting up?"    
    hk "Ah! Thank you very much for the offer."
    hk "However, I should be able to do it myself...woah!"
    
    # ADD EXCLAMATION SFX FOR HIKO
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff")
    hiko "Easy there, Sleeping Beauty!"
    hiko "You just got off an unexpected trip."
    hiko "Here: take my hand, and I'll help you sit up."
    hk "O-Okay."
    
    # HIDE HIKO BEFORE SCENE CHANGE 
    hide kazuhiko_neutral_dark with Dissolve(0.25)

    # SCENE CHANGES FROM SURROUNDING OKUDA TRIO TO NORMAL VN BACKGROUND AND PLAYER/CHARACTER INTERACTION 
    hide waking_up
    with fade
    show lounge 
    with Dissolve(1.5)

    # BACK TO DIALOGUE 
    play music watch_ur_behavior volume 0.90 loop
    show kazuhiko_halfbody_neutral with Dissolve(0.75)
    hiko "There we are now! So, how do you feel right now?"
    hk "I'm fine for the most part. Still pretty exhausted, though."
    hiko "Completely understandable!"
    show kazuhiko_halfbody_thinking
    hide kazuhiko_halfbody_neutral
    with Dissolve(0.25)
    hiko "{i}Why isn't he back with the water? It shouldn't take this long{/i}."
    hk "Is everything all good?"
    show kazuhiko_halfbody_happy
    hide kazuhiko_halfbody_thinking
    with Dissolve(0.25)
    
    # EXCLAMATION SFX FOR HIKO 
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff")
    hiko "Oh, Yeah! Everything's all good! We have someone bringing back water for you."
    hiko "In the meantime, we should probably introduce ourselves. I'll start off!"
    $ hiko.name = "Kazuhiko Okuda" # CHANGE NAME
    show kazuhiko_halfbody_blush
    hide kazuhiko_halfbody_happy
    with Dissolve(0.25)
    hiko "I'm Kazuhiko Okuda, the {color=#efcc00}{b}Ultimate Master of Ceremonies{/b}{/color}! Pleased to make your acquaintance."

    # SHOW CHARACTER CARD HERE [HIKO] [FINISHED 1/23/24]
    show kazuhiko_halfbody_neutral
    hide kazuhiko_halfbody_blush
    show kazuhiko_card_background behind kazuhiko_halfbody_neutral
    with Dissolve(0.25) 
    show kazuhiko_halfbody_neutral at left
    with ease 
    play sfx_channel card_intro_shine volume 2.00 noloop  
    show kazuhiko_card_font behind kazuhiko_halfbody_neutral
    with Dissolve(0.10)
    with hpunch
    $ renpy.pause(2.5, hard=True) 
    hide kazuhiko_card_font
    hide kazuhiko_card_background
    with Dissolve(0.10)
    show kazuhiko_halfbody_neutral at center
    with ease
    

    hk "{color=#efcc00}{b}Master of Ceremonies{/b}{/color}? What does that entail?"
    hiko "Not to worry! After the other introductions, I think that question will answer itself."
    show kazuhiko_halfbody_happy
    hide kazuhiko_halfbody_neutral
    with Dissolve(0.25)
    hiko "Now then, your turn, {color=#efcc00}{b}Tetsu{/b}{/color}!"  

    # HIDE HIKO AND TRANSITION OVER TO TETSU 
    show tetsunori_halfbody_surprised
    hide kazuhiko_halfbody_happy
    with Dissolve(0.25)

    # TETSU INTRO  
    tetsu "Well, looks like I'm next."
    $ tetsu.name = "Tetsunori Okuda" # CHANGE NAME
    show tetsunori_halfbody_happy
    hide tetsunori_halfbody_surprised
    with Dissolve(0.25)
    tetsu "The name's Tetsunori Okuda: {color=#efcc00}{b}Ultimate Breakdancer{/b}{/color}. Look forward to getting to know you better." 
    
    # SHOW CHARACTER CARD [TETSUNORI] [FINISHED 1/23/24]
    show tetsunori_halfbody_neutral
    hide tetsunori_halfbody_happy
    with Dissolve(0.25)
    show tetsunori_card_background behind tetsunori_halfbody_neutral
    with Dissolve(0.25) 
    show tetsunori_halfbody_neutral at left
    with ease    
    play sfx_channel card_intro_shine volume 2.00 noloop
    show tetsunori_card_font behind tetsunori_halfbody_neutral
    with Dissolve(0.10)
    with hpunch
    $ renpy.pause(2.5, hard=True) 
    hide tetsunori_card_font
    hide tetsunori_card_background
    with Dissolve(0.10)
    show tetsunori_halfbody_neutral at center
    with ease

    # BACK TO HIKO AND NAOKI     
    hk "And likewise!"
    show kazuhiko_halfbody_happy
    hide tetsunori_halfbody_neutral
    with Dissolve(0.25)
    hiko "Finally, we got the coolest little dude around!"
    hiko "The true overseer on the wheels of steel, our little bro, {color=#efcc00}{b}Naoki{/b}{/color}!"
    $ naoki.name = "Naoki Okuda" # CHANGE NAME

    # HIKO INTRO 
    show naoki_halfbody_neutral
    hide kazuhiko_halfbody_happy
    with Dissolve(0.25)
    naoki "Um, n-nice to meet you."    
    naoki "Like Hiko said, my name is Naoki Okuda, and I am the {color=#efcc00}{b}Ultimate DJ{/b}{/color}. It's so nice to meet you." 
    
    # SHOW CHARACTER CARD [NAOKI] [FINISHED 1/23/24]
    show naoki_card_background behind naoki_halfbody_neutral
    with Dissolve(0.25) 
    show naoki_halfbody_neutral at left
    with ease  
    play sfx_channel card_intro_shine volume 2.00 noloop  
    show naoki_card_font behind naoki_halfbody_neutral
    with Dissolve(0.10)
    with hpunch
    $ renpy.pause(2.5, hard=True) 
    hide naoki_card_font
    hide naoki_card_background
    with Dissolve(0.10)
    show naoki_halfbody_neutral at center
    with ease

    # URBAN HIGH THREE INTRODUCTION
    hk "Nice to meet all of you!"
    hk "So, from what I've gathered, you're three brothers that are a part of some boy band?"
    show tetsunori_halfbody_neutral
    hide naoki_halfbody_neutral
    with Dissolve(0.25)
    tetsu "Indeed! We are the greatest Hip-Hop trio to ever grace the streets of Harajuku!"
    show kazuhiko_halfbody_happy
    hide tetsunori_halfbody_neutral
    with Dissolve(0.25)
    hiko "We are! .... ...."
    hiko "We are! ...."
    show kazuhiko_halfbody_neutral
    hide kazuhiko_halfbody_happy
    with Dissolve(0.25)
    hiko ".... .... {i}Naoki, that's your cue{/i}!"
    show naoki_halfbody_neutral
    hide kazuhiko_halfbody_neutral
    with Dissolve(0.25)

    # PLAYING EXCLAMATION SFX 
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff")
    naoki "Oops! We are the {color=#efcc00}{b}Urban High Three{/b}{/color}!"

    # NOBURO INTRO 
    show noburo_halfbody_happy
    hide naoki_halfbody_neutral
    with Dissolve(0.25)
    noburo "Did somebody say the Urban High Three?"
    show kazuhiko_halfbody_thinking
    hide noburo_halfbody_happy
    with Dissolve(0.25)
    hiko "Hey, you're finally back. Did you bring the water?"
    show noburo_halfbody_happy
    hide kazuhiko_halfbody_thinking
    with Dissolve(0.25)
    noburo "Totally! I brough a pitcher and some extra cups, just in case."
    show kazuhiko_halfbody_neutral
    hide noburo_halfbody_happy
    with Dissolve(0.25)
    hiko "Perfect. Here, Hisako, take this."
    hk "Oh, thank you."
    show noburo_halfbody_happy
    hide kazuhiko_halfbody_neutral
    with Dissolve(0.25)
    noburo "Ayo, you're finally up! Sorry for accidentally making you go on a drug trip."
    show noburo_halfbody_neutral
    hide noburo_halfbody_happy
    with Dissolve(0.25)
    noburo "I promise I'll try to make it up to you in any way, you name it!"
    hk "Uh, it's okay, honestly. Just make sure that you don't make magic brownies again."
    show noburo_halfbody_happy
    hide noburo_halfbody_neutral
    with Dissolve(0.25)
    noburo "Your wish is my command!"
    show noburo_halfbody_neutral
    hide noburo_halfbody_happy
    with Dissolve(0.25)
    noburo "Oh! I should tell you my name."
    $ noburo.name = "Noburo Nanaka" # CHANGE NAME 
    noburo "I'm Noburo Nanaka, and I am the {color=#efcc00}{b}Ultimate Greek Brother{/b}{/color}!" 
    
    # SHOW CHARACTER CARD [NOBURO] [FINISHED 1/23/24]
    show noburo_card_background behind noburo_halfbody_neutral
    with Dissolve(0.25) 
    show noburo_halfbody_neutral at left
    with ease    
    play sfx_channel card_intro_shine volume 2.00 noloop
    show noburo_card_font behind noburo_halfbody_neutral
    with Dissolve(0.10)
    with hpunch
    $ renpy.pause(2.5, hard=True) 
    hide noburo_card_font
    hide noburo_card_background
    with Dissolve(0.10)
    show noburo_halfbody_neutral at center
    with ease

    # INTRODUCTIONS HAVE FINISHED: WELCOME TO WHITE WYVERN MANOR 
    hkmonologue "...Yeah, now the dots are starting to connect themselves."
    hide noburo_halfbody_neutral
    with Dissolve(0.25)
    hk "Well, a pleasure to meet you, Noburo."
    hk "Now, I am very thankful for all of you helping me out, but don't we need to go back to the Admissions Office for Orientation?"
    show kazuhiko_halfbody_neutral
    with Dissolve(0.25)
    hiko "Yeah, but don't worry, you're all set."
    hk "What do you mean I'm all set?"
    show tetsunori_halfbody_thinking
    hide kazuhiko_halfbody_neutral
    with Dissolve(0.25)
    tetsu "The only reason why you needed to go to the Admissions office was because you needed to get you school ID, keys, and map of the campus."
    hk "So where am I now?"
    show kazuhiko_halfbody_happy
    hide tetsunori_halfbody_thinking
    with Dissolve(0.25)
    hiko "You, my beautiful friend, are in {color=#efcc00}{b}White Wyvern Manor{/b}{/color}!"
    show tetsunori_halfbody_neutral
    hide kazuhiko_halfbody_happy
    with Dissolve(0.25)
    tetsu "Welcome to the {color=#efcc00}{b}Mansion of the Ultimates{/b}{/color}."
    show kazuhiko_halfbody_happy
    hide tetsunori_halfbody_neutral
    with Dissolve(0.25)
    hiko "So don't worry about anything. We even went through the trouble of getting your belongings from the Admissions Office."
    show noburo_halfbody_happy
    hide kazuhiko_halfbody_happy
    with Dissolve(0.25)
    noburo "Yeah, we put them on the back table until you woke up from the brownie trip."
    show naoki_halfbody_happy
    hide noburo_halfbody_happy
    with Dissolve(0.25)
    naoki "Here, I'll go get them!"
    show noburo_halfbody_happy
    hide naoki_halfbody_happy
    with Dissolve(0.25)
    noburo "Awesome-o!"
    show noburo_halfbody_neutral
    hide noburo_halfbody_happy
    with Dissolve(0.25)
    noburo "And...uh...what was your name again?"
    hk "Oh! I completely forgot to introduce myself! I am so sorry!"
    hk "My name is Hisako Kawahara: {color=#efcc00}{b}Ultimate Lawyer{/b}{/color}."

    # TINY ARGUMENT OVER HISAKO 
    show kazuhiko_halfbody_blush
    hide noburo_halfbody_neutral
    with Dissolve(0.25)
    hiko "Hisako Kawahara...what a lovely name. A pleasure to meet you."
    hk "Ah, um, thank you. I look forward to a great school year with you all!"
    show noburo_halfbody_happy
    hide kazuhiko_halfbody_blush
    with Dissolve(0.25)
    noburo "Ditto, bro!"
    show kazuhiko_halfbody_blush
    hide noburo_halfbody_happy
    with Dissolve(0.25)
    hiko "And same with me as well!"
    show tetsunori_halfbody_surprised
    hide kazuhiko_halfbody_blush
    with Dissolve(0.25)
    tetsu "Remember you two: give Hisako some space. Her body is still trying to recover from the weed brownies."
    show noburo_halfbody_upset
    hide tetsunori_halfbody_surprised
    with Dissolve(0.25)
    noburo "Oh yeah, I completely forgot that. My apologies, dudes."
    show kazuhiko_halfbody_frustrated
    hide noburo_halfbody_upset
    with Dissolve(0.25)
    play sfx_channel stern_sfx volume 1.00 noloop
    hiko "Says the guy who handed out said brownies."
    show tetsunori_halfbody_unamused
    hide kazuhiko_halfbody_frustrated
    with Dissolve(0.25)
    tetsu "All right, all right. There's no need to turn this into an argument."
    tetsu "It's still the first day after all."

    # GOING TO SEE THE OTHER ULTIMATES 
    show naoki_halfbody_happy
    hide tetsunori_halfbody_unamused
    with Dissolve(0.25)
    naoki "Ms. Hisako! Here's your belongings."
    hk "Thank you, Naoki! Also, you don't have to address me so formally. We're all equals here!"
    show naoki_halfbody_frustrated
    hide naoki_halfbody_happy
    with Dissolve(0.25)
    naoki "Are you sure?"
    hk "Absolutely! I want all of us to become good friends, and I don't want formalities to get in the way of that."
    show naoki_halfbody_neutral
    hide naoki_halfbody_frustrated
    with Dissolve(0.25)
    naoki "All right then...Hisako."
    show kazuhiko_halfbody_neutral
    hide naoki_halfbody_neutral
    with Dissolve(0.25)
    hiko "Now that you've got everything with you, we should introduce you to the others."
    hk "Others? Do you mean more {color=#efcc00}{b}Ultimates{/b}{/color}?"
    show kazuhiko_halfbody_happy
    hide kazuhiko_halfbody_neutral
    with Dissolve(0.25)
    hiko "That is exactly what I mean!"
    hiko "They would've been here in the main area, but with your unforeseen accident, they didn't want to be rude and chat while you were recovering."
    hk "Aw, I hope I didn't cause too much trouble with that whole thing."
    hiko "None whatsoever!"
    show kazuhiko_halfbody_neutral
    hide kazuhiko_halfbody_happy
    with Dissolve(0.25)
    hiko "Don't be hard on yourself, they'll understand the situtation and be very pleased to see that you're feeling better."
    hiko "Now then, shall we go and visit them?"
    hk "Totally! I am excited to see who my fellow peers are and what abilities they possess!"
    show kazuhiko_halfbody_happy
    hide kazuhiko_halfbody_neutral
    with Dissolve(0.25)
    hiko "It's settled then. Tetsunori, would you be so kind to escort the group over to where our peers are?"
    hiko "I'll stay behind and clean up the lounge."
    show tetsunori_halfbody_thinking
    hide kazuhiko_halfbody_happy
    with Dissolve(0.25)
    tetsu "Are you sure you don't need any assistance with cleaning, Hiko?"
    show kazuhiko_halfbody_neutral
    hide tetsunori_halfbody_thinking
    with Dissolve(0.25)
    hiko "Trust me, I'm all set!"
    hiko "Besides, it's the duty of the big brother to help with the housekeeping. I'll meet up as soon as everything is picked up, I promise."
    show naoki_halfbody_happy
    hide kazuhiko_halfbody_neutral
    with Dissolve(0.25)
    naoki "Don't worry, Tetsu, big bro never lies to us, isn't that right, Hiko?"
    show kazuhiko_halfbody_happy
    hide naoki_halfbody_happy
    with Dissolve(0.25)
    hiko "Damn right!"
    show tetsunori_halfbody_surprised
    hide kazuhiko_halfbody_happy
    with Dissolve(0.25)
    tetsu "Okay then."
    show tetsunori_halfbody_neutral
    hide tetsunori_halfbody_surprised
    with Dissolve(0.25)
    tetsu "Here Hisako, follow me to the dining room. That is where the other Ultimates have been relaxing."

    # PLACE WALKING SFX HERE 
    play sfx_channel walking volume 0.85 noloop
    # TRANSITION OVER TO SCENE [1/16/2024]
    hide tetsunori_halfbody_neutral
    with Dissolve(0.25)
    stop music fadeout 2.0
    hide lounge
    with fade
    show transition
    with Dissolve(2.0)
    $ renpy.pause(1.75, hard=True)
 
# SCENE 1-3 [WHITE WYVERN MANOR - DINING AREA] --> HISAKO IS BEING GUIDED TO THE DINING AREA BY TETSUNORI AND FOLLOWED
# BY NAOKI AND NOBURO. THEY ARE GOING TO BE INTRODUCED TO SEVERAL OTHER ULTIMATES WHO ARRIVED WHEN HISAKO WAS UNCONSCIOUS 
label scene1_3:
    # RESET NAME 
    $ kichi.name = "???"
    $ shinzo.name= "???"
    # START SCENE OUT BY MOVING AWAY FROM TRANSITION SCENE AND INTO THE DINING AREA [STARTED 1/24/24 EST 6:21 AM]
    show dining_room
    hide transition
    with Dissolve(1.5)
    play music new_fonky_step volume 0.85 loop
    $ renpy.pause(1.00, hard=True) 

    # KICHI AND SHINZO CORNY PICK-UP LINE BANTER 
    show shinzo_halfbody_neutral
    with Dissolve(.75)
    shinzo "So...how did it feel...when you fell from Tennessee?"
    show kichi_halfbody_annoyed
    hide shinzo_halfbody_neutral
    with Dissolve(0.25)
    kichi "Hun, I'm pretty sure you messed up your own pick-up line."
    show shinzo_halfbody_upset
    hide kichi_halfbody_annoyed
    with Dissolve(0.25)
    shinzo "No, wait! I got this!"
    show shinzo_halfbody_neutral
    hide shinzo_halfbody_upset
    with Dissolve(0.25)
    shinzo "How did it feel when you...fell from Heaven, because you are only ten I see." 
    show kichi_halfbody_annoyed
    hide shinzo_halfbody_neutral
    with Dissolve(0.25)
    kichi "That was worse the second time around, but I'll give you credit for going through with it."
    show kichi_halfbody_neutral
    hide kichi_halfbody_annoyed
    with Dissolve(0.25)
    kichi "However, Sugar, my answer is still no."
    kichi "Besides the absolute butchering outta 'ya pick-up line, with pants as tight as that, I can tell we would never get anywhere."
    show kichi_halfbody_happy
    hide kichi_halfbody_neutral
    with Dissolve(0.25)
    kichi "The moon is waning and so seems to be you manhood."
    # ADD THUNDER SFX FOR SHINZO    
    show shinzo_halfbody_frustrated
    hide kichi_halfbody_happy
    with Dissolve(0.25)    
    play sfx_channel thunder_sfx volume 1.00 noloop
    with vpunch
    shinzo "Now hold on just a minute there. Why are you gonna start insulting me like I'm a criminal?"
    shinzo "All I did was try to give a beautiful gal like you a nice ol' compliment."
    show kichi_halfbody_happy
    hide shinzo_halfbody_frustrated
    with Dissolve(0.25)
    kichi "First of all, love: I'm flattered by the compliment; however, the whole cowboy aesthetic is just very tacky."
    show kichi_halfbody_neutral
    hide kichi_halfbody_happy
    with Dissolve(0.25)
    kichi "This ain't the 2000's no more, honey. You can stop pretending 'ya a part of {i}Tombstone{/i}."
    show shinzo_halfbody_upset
    hide kichi_halfbody_neutral
    with Dissolve(0.25)
    # ADD DISAPPOINTMENT SFX HERE FOR SHINZO 
    play sfx_channel disappointment_sfx volume 1.25 noloop
    shinzo "And now you decide to aim straight for the center and insult the getup, huh?"
    shinzo "We're peers for the next couple a' years or so. You gotta at least give me a chance to be a companion in friendship."
    show kichi_halfbody_happy
    hide shinzo_halfbody_upset
    with Dissolve(0.25)
    kichi "I'll think about it, baby."
    show shinzo_halfbody_neutral
    hide kichi_halfbody_happy
    with Dissolve(0.25)
    shinzo "All good in my book. Much obliged."

    # ENTER MAIN CHARACTER GROUP 
    show shinzo_halfbody_happy
    hide shinzo_halfbody_neutral
    with Dissolve(0.25)
    shinzo "Well throw me in a train car and call me a can of beans, look who finally decided to show up!"
    show kichi_halfbody_happy
    hide shinzo_halfbody_happy
    with Dissolve(0.25)
    kichi "It's so nice to see you walking about here instead of in the astral planes, Darlin'."
    show tetsunori_halfbody_neutral
    hide kichi_halfbody_happy
    with Dissolve(0.25)
    tetsu "You see, Hisako, everyone was worried about you."
    show kichi_halfbody_neutral
    hide tetsunori_halfbody_neutral
    with Dissolve(0.25)
    kichi "My readings have indicated that \"death\" was approaching sooner than expected, but after we heard about the whole brownie mix-up..."
    show kichi_halfbody_happy
    hide kichi_halfbody_neutral
    with Dissolve(0.25)
    kichi "...we realized \"death\" in this sense meant unexpected change."
    show shinzo_halfbody_frustrated
    hide kichi_halfbody_happy
    with Dissolve(0.25)
    shinzo "I told ya from the start that your fancy reading could be up to interpretation."

    # KICHI AND SHINZO INTRODUCTIONS 
    $ kichi.name = "Kichi Isozaki" # NAME CHANGE     
    show kichi_halfbody_happy
    hide shinzo_halfbody_frustrated
    with Dissolve(0.25)
    kichi "Anyways, a pleasure to meet you, Darlin'. I am Kichi Isozaki, the {color=#efcc00}{b}Ultimate Astrologist{/b}{/color}."
    # SHOW KICHI CHARACTER CARD
    show kichi_halfbody_neutral
    hide kichi_halfbody_happy
    with Dissolve(0.25)
    show kichi_card_background behind kichi_halfbody_neutral
    with Dissolve(0.25) 
    show kichi_halfbody_neutral at left
    with ease 
    play sfx_channel card_intro_shine volume 2.00 noloop  
    show kichi_card_font behind kichi_halfbody_neutral
    with Dissolve(0.10)
    with hpunch
    $ renpy.pause(2.5, hard=True) 
    hide kichi_card_font
    hide kichi_card_background
    with Dissolve(0.10)
    show kichi_halfbody_neutral at center
    with ease
    # BACK TO CONVERSATION
    
    hk "It's a pleasure to meet you as well, Kichi. I'm Hisako Kawahara: {color=#efcc00}{b}Ultimate Lawyer{/b}{/color}!"    
    with Dissolve(0.25)
    kichi "Oooh, a lawyer. So fancy!"
    kichi "If you ever want a reading, don't hesitate to ask, no matter how mundane."
    show kichi_halfbody_happy
    hide kichi_halfbody_neutral
    with Dissolve(0.25)
    kichi "Questions for a test, future success, or maybe seeing who you'll have an adult nap with, hmmm?"
    hk "Um, why would I want to ask about that?"    
    with Dissolve(0.25)
    kichi "You never know, Darlin'. It is truly a slice of Heaven."
    show shinzo_halfbody_frustrated
    hide kichi_halfbody_happy
    with Dissolve(0.25)
    shinzo "I'm gonna step in before this trainwreck of a conversation starts to derail."
    $ shinzo.name = "Shinzo Akagawa" # NAME CHANGE 
    show shinzo_halfbody_neutral
    hide shinzo_halfbody_frustrated
    with Dissolve(0.25)   
    shinzo "The name is Shinzo Akagawa, {color=#efcc00}{b}fastest and deadliest gunslinger in the world{/b}{/color}."
    show kichi_halfbody_upset
    hide shinzo_halfbody_neutral
    with Dissolve(0.25)
    kichi "Oh, honey, don't be embarassin' yourself like that."
    kichi "Just tell the poor girl what your Ultimate is, and stop acting like a hyperactive youngin'."
    show shinzo_halfbody_frustrated
    hide kichi_halfbody_upset
    with Dissolve(0.25)
    shinzo "What do you mean embarassing? That's just who I am!"
    show kichi_halfbody_annoyed
    hide shinzo_halfbody_frustrated
    with Dissolve(0.25)
    kichi "Uh huh, you keep telling yourself that."
    show kichi_halfbody_neutral
    hide kichi_halfbody_annoyed
    with Dissolve(0.25)
    kichi "Sorry bout' that, Sweetheart. Since he wants to continue playing cowboy, I'll just tell you."
    kichi "That country bumpkin's the {color=#efcc00}{b}Ultimate Sharpshooter{/b}{/color}."
    show shinzo_halfbody_upset
    hide kichi_halfbody_neutral
    with Dissolve(0.25) 
    shinzo "There you go back to insultin' me again."
    show shinzo_halfbody_frustrated
    hide shinzo_halfbody_upset
    with Dissolve(0.25)
    shinzo "Fine, I am the {color=#efcc00}{b}Ultimate Sharpshooter{/b}{/color}, at your service." 
    # SHOW SHINZO CHARACTER CARD
    show shinzo_halfbody_neutral
    hide shinzo_halfbody_frustrated
    with Dissolve(0.25)
    show shinzo_card_background behind shinzo_halfbody_neutral
    with Dissolve(0.25) 
    show shinzo_halfbody_neutral at left
    with ease 
    play sfx_channel card_intro_shine volume 2.00 noloop  
    show shinzo_card_font behind shinzo_halfbody_neutral
    with Dissolve(0.10)
    with hpunch
    $ renpy.pause(2.5, hard=True) 
    hide shinzo_card_font
    hide shinzo_card_background
    with Dissolve(0.10)
    show shinzo_halfbody_neutral at center
    with ease

    # EXIT SHINZO HERE
    show shinzo_halfbody_frustrated
    hide shinzo_halfbody_neutral
    with Dissolve(0.25)
    shinzo "Now if you'll excuse me, I'm gonna go and fetch me a bottle of fine whiskey in the other room."
    show shinzo_halfbody_neutral
    hide shinzo_halfbody_frustrated
    with Dissolve(0.25)
    shinzo "Ms. Kawahara, it was lovely seeing you."
    show shinzo_halfbody_frustrated
    hide shinzo_halfbody_neutral
    with Dissolve(0.25)
    shinzo "As for the {color=#efcc00}{b}Psychic{/b}{/color}, hopefully we can solve our problems at a later time."
    show kichi_halfbody_frustrated
    hide shinzo_halfbody_frustrated
    with Dissolve(0.25)
    kichi "I am an {color=#efcc00}{b}Astrologist! AST-ROL-O-GY{/b}{/color}. Ya here that, Sugar?"
    show shinzo_halfbody_frustrated
    hide kichi_halfbody_frustrated
    with Dissolve(0.25)
    shinzo "Please find somewhere else to exist, maybe, the Astral Plane, for example!" 
    # EXIT SHINZO
    play sfx_channel walking volume 0.85 noloop
    hide shinzo_halfbody_frustrated
    with Dissolve(1.00)
    
    #KICHI TALKS TO HISAKO AND THE LOT 
    show kichi_halfbody_frustrated
    with Dissolve(0.75)
    kichi "Why that little crud muffin! He truly gets on my last nerve!"
    show kichi_halfbody_upset
    hide kichi_halfbody_frustrated
    with Dissolve(0.25)
    kichi "Oh, my deepest apologies, Dumplin', I didn't mean to get so heated."
    show kichi_halfbody_frustrated
    hide kichi_halfbody_upset
    with Dissolve(0.25)
    kichi "It's just people like that truly get me angrier than swarm of hornets."
    hkmonologue "... ... ..."
    hk "Oh, ah, it's okay. I completely understand you!"
    show kichi_halfbody_happy
    hide kichi_halfbody_frustrated
    with Dissolve(0.25)
    kichi "Oh, bless your heart!"
    kichi "While you are still around, let me introduce ya' to the others in this room."
    show tetsunori_halfbody_neutral
    hide kichi_halfbody_happy
    with Dissolve(0.25)
    tetsu "Hisako, while you're being introduced, Noburo and I are gonna head back to see if Hiko is finished cleaning up."
    show noburo_halfbody_happy
    hide tetsunori_halfbody_neutral
    with Dissolve(0.25)
    noburo "If you need us, don't be afraid to give us a holler!"
    show naoki_halfbody_neutral
    hide noburo_halfbody_happy
    with Dissolve(0.25)
    naoki "What should I do, Tetsu?"
    show tetsunori_halfbody_surprised
    hide naoki_halfbody_neutral
    with Dissolve(0.25)
    tetsu "Why don't you stay with Hisako and keep her company."
    tetsu "You'll also meet more of your peers and get to know them better!"
    show naoki_halfbody_happy
    hide tetsunori_halfbody_surprised
    with Dissolve(0.25)
    naoki "That sounds like a great idea! Thanks, Tetsu!"
    show tetsunori_halfbody_neutral
    hide naoki_halfbody_happy
    with Dissolve(0.25)
    tetsu "No problem!"
    show tetsunori_halfbody_happy
    hide tetsunori_halfbody_neutral
    with Dissolve(0.25)
    tetsu "Well, Hisako, I'll be seeing you around." 
    # EXIT TETSUNORI AND NOBURO 
    play sfx_channel walking volume 0.85 noloop
    hide tetsunori_halfbody_happy
    with Dissolve(1.00)
    show noburo_halfbody_neutral
    with Dissolve(0.75)
    noburo "See you later, Aligators!"
    play sfx_channel walking volume 0.85 noloop
    hide noburo_halfbody_neutral
    with Dissolve(1.00)
    hk "Okay! See ya!"
    show kichi_halfbody_happy
    with Dissolve(0.25)
    kichi "Alright then! Y'all can just follow me then. Let me show 'ya 'round!"
    hkmonologue "These are definitely a rather interesting group of individuals, so far. I wonder how the others will be."

    # PLACE WALKING SFX HERE 
    play sfx_channel walking volume 0.85 noloop
    # TRANSITION OVER TO SCENE [1/29/2024]
    hide kichi_halfbody_happy
    with Dissolve(0.25)
    stop music fadeout 2.0
    hide dining_room
    with fade
    show transition
    with Dissolve(2.0)
    $ renpy.pause(1.75, hard=True) 

# SCENE 1-4 [WHITE WYVERN MANOR - DINING AREA 2] --> HISAKO IS NOW BEING INTRODUCED TO MORE ULTIMATES IN THE OTHER PART OF THE DINING AREA
# BY NONE OTHER THAN KICHI. AS THEY APPROACH THE NEW BATCH OF ULTIMATES, HISAKO LISTENS IN ON A VERY INTERESTING CONVERSATION.    
label scene1_4:  
    # RESET NAME 
    $ yui.name = "???"
    $ yashimata.name = "???"
    $ eizo.name = "???"
    $ ryosei.name = "???"  

    # MONOLOGUE INTO YASHIMATA NONSENSE 
    hkmonologue "As Kichi was showing us around the expansive dining area, I couldn't help but wonder how much money was invested into this place."
    hkmonologue "The answer is definitely...A LOT!"
    hkmonologue "And as I finally snapped back to reality, I saw some more {color=#efcc00}{b}Ultimates{/b}{/color} near the back of the room."
    hkmonologue "From the looks of the commotion, something was definitely happening."
    hkmonologue "As we approached, I started to tune into the conversation."

    # START SCENE OUT BY MOVING AWAY FROM TRANSITION SCENE AND INTO THE DINING AREA [STARTED 1/31/24 EST 1:34 AM]
    show dining_room_2
    hide transition
    with Dissolve(1.5)
    play music sundowner volume 0.85 loop
    $ renpy.pause(1.00, hard=True)

    # YASHIMATA AND YUI TALKING 
    show yui_halfbody_happy
    with Dissolve(0.75)
    yui "C'mon, C'mon, C'mon! You gotta tell me what your secret is!"
    yui "How are you able to memorize all of the intricate patterns in such a short amount of time?"
    yui "How do you train your leg-eye coordination?"
    show yui_halfbody_cool
    hide yui_halfbody_happy
    with Dissolve(0.25)
    yui "And how are you still not listening to me??"
    show yashimata_halfbody_zoned
    hide yui_halfbody_cool
    with Dissolve(0.25)
    yashimata "... ..."
    yashimata "... ... ..."
    show yashimata_halfbody_neutral
    hide yashimata_halfbody_zoned
    with Dissolve(0.25)
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff") 
    yashimata "Oh! Were you saying something?"
    show yashimata_halfbody_happy
    hide yashimata_halfbody_neutral
    with Dissolve(0.25)
    yashimata "My apologies. I was just thinking: are boneless chicken wings actually just chicken nuggets in disguise?"
    show yui_halfbody_unamused
    hide yashimata_halfbody_happy
    with Dissolve(0.25)
    yui "What? What are you talking about?"
    show yashimata_halfbody_happy
    hide yui_halfbody_unamused
    with Dissolve(0.25)
    yashimata "Like, if you take away the sauce and spice, it's just a beefier chicken nugget."
    show yui_halfbody_thinking
    hide yashimata_halfbody_happy
    with Dissolve(0.25)
    yui "...Is there even a coherent in that brain of yours?"
    show yashimata_halfbody_frustrated
    hide yui_halfbody_thinking
    with Dissolve(0.25)
    yashimata "Uh, absolutely!"
    show yashimata_halfbody_neutral
    hide yashimata_halfbody_frustrated
    with Dissolve(0.25)
    yashimata "... ..."
    show yashimata_halfbody_frustrated
    hide yashimata_halfbody_neutral
    with Dissolve(0.25)
    yashimata "But for real though why do they call it \"toast,\" huh?"    
    yashimata "Why not call it something like, I don't know, \"crunchy bread\"."
    show yashimata_halfbody_happy
    hide yashimata_halfbody_frustrated
    with Dissolve(0.25)
    yashimata "I mean, it definitely sounds more appealing and interesting when you call it \"crunchy bread\" instead of boring, old \"{i}toast{/i}\"."
    show yashimata_halfbody_frustrated
    hide yashimata_halfbody_happy
    with Dissolve(0.25)
    play sfx_channel thunder_sfx volume 1.00 noloop
    with vpunch
    yashimata "And don't even get me started on hot dogs!"   
    yashimata "In my honest and humble opinion, a hot dog is just an elongated sandwich. End of discussion!"

    # EIZO PANIC SLEEP
    show eizo_halfbody_upset
    hide yashimata_halfbody_frustrated
    with Dissolve(0.25)
    eizo "Y-Your sandwich!? Coming right up, sir!"
    show yashimata_halfbody_happy
    hide eizo_halfbody_upset
    with Dissolve(0.25)
    yashimata "Yo! We getting free food from Fatty Fingers?"
    show yui_halfbody_neutral
    hide yashimata_halfbody_happy
    with Dissolve(0.25)
    yui "What? No one ordered anything!"
    show yashimata_halfbody_neutral
    hide yui_halfbody_neutral
    with Dissolve(0.25)
    yashimata "But Fry Boy just said I ordered one."
    hide yashimata_halfbody_neutral
    with Dissolve(0.25)

    # GROUP NOW ENTERS 
    hk "Uh, is everything alright over here?"
    show yui_halfbody_happy
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff") 
    yui "Oh! Hiiiiiiii!!"
    yui "It's so nice to see you up and walking about!"
    yui "You have to tell me..."
    show yui_halfbody_genius
    hide yui_halfbody_happy
    with Dissolve(0.25)
    yui "What's your name?"
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff") 
    yui "What amazing {color=#efcc00}{b}Ultimate{/b}{/color} do you have?"
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff") 
    yui "Do you realize that ate four or five pot brownies?"
    show kichi_halfbody_neutral
    hide yui_halfbody_genius
    with Dissolve(0.25)
    kichi "Easy now, Pumpkin. You gotta remember she just got up not that long ago, and the effects of them brownies are still in play."
    show yui_halfbody_upset
    hide kichi_halfbody_neutral
    with Dissolve(0.25)
    yui "You're right. I'm really sorry, I just get so excited when something acts as a muse for me."
    hk "A muse? So are you a master of the arts?"
    show yui_halfbody_happy
    hide yui_halfbody_upset
    with Dissolve(0.25)
    yui "Indeed I am!"

    # YUI INTRODUCTION
    yui "With the imagination of Stephen King, the immersion of Homer, and don't forget, the prowess of Shakespeare..."
    $ yui.name = "Yui Tsutsui" # NAME CHANGE
    show yui_halfbody_genius
    hide yui_halfbody_happy
    with Dissolve(0.25)
    yui "I am the one and only: Yui Tsutsui - {color=#efcc00}{b}Ultimate Storyteller{/b}{/color}!!!"

    # SHOW YUI CHARACTER CARD
    show yui_halfbody_neutral
    hide yui_halfbody_genius
    with Dissolve(0.25)
    show yui_card_background behind yui_halfbody_neutral
    with Dissolve(0.25) 
    show yui_halfbody_neutral at left
    with ease 
    play sfx_channel card_intro_shine volume 2.00 noloop  
    show yui_card_font behind yui_halfbody_neutral
    with Dissolve(0.10)
    with hpunch
    $ renpy.pause(2.5, hard=True) 
    hide yui_card_font
    hide yui_card_background
    with Dissolve(0.10)
    show yui_halfbody_neutral at center
    with ease
    
    # AFTER INTRO
    hk "The {color=#efcc00}{b}Ultimate Storyteller{/b}{/color}, huh?"
    hk "What stories have you made? Do you go by a pen name or something because I have never heard of you before?"
    show yui_halfbody_happy
    hide yui_halfbody_neutral
    with Dissolve(0.25)
    yui "I have created timeless classics such as {i}Boys of the Mountain{/i} and {i}Secret Admirers and Admirers{/i}."
    show yui_halfbody_thinking
    hide yui_halfbody_happy
    with Dissolve(0.25)
    yui "However, you're more likely to find my books on the clearance rack...or in the dumpster of a public library."
    hkmonologue "Yep. That would do it."
    hk "Well, it is a pleasure to meet you in the flesh!"
    hk "Now back to the topic at hand: what's wrong with him? Are they going to be all right?"
    
    # EIZO INTRODUCTION
    show yui_halfbody_neutral
    hide yui_halfbody_thinking
    with Dissolve(0.25)
    yui "Yeah, that's just Eizo. Apparently, he's The {color=#efcc00}{b}Ultimate Fast Food Worker{/b}{/color}."
    $ eizo.name = "Eizo Daigo" # NAME CHANGE 

    # SHOW EIZO CHARACTER CARD
    show eizo_halfbody_upset
    hide yui_halfbody_neutral
    with Dissolve(0.25)
    show eizo_card_background behind eizo_halfbody_upset
    with Dissolve(0.25) 
    show eizo_halfbody_upset at left
    with ease 
    play sfx_channel card_intro_shine volume 2.00 noloop  
    show eizo_card_font behind eizo_halfbody_upset
    with Dissolve(0.10)
    with hpunch
    $ renpy.pause(2.5, hard=True) 
    hide eizo_card_font
    hide eizo_card_background
    with Dissolve(0.10)
    show eizo_halfbody_upset at center
    with ease

    # AFTER INTRO
    hk "{color=#efcc00}{b}Ultimate Fast Food Worker{/b}{/color}?"
    show yui_halfbody_neutral
    hide eizo_halfbody_upset
    with Dissolve(0.25)
    yui "Yep. I heard he spends most of the working at the Fatty Fingers joint near his house."
    show yui_halfbody_thinking
    hide yui_halfbody_neutral
    with Dissolve(0.25)
    yui "All day. Everyday. His life is consumed by that meager job."
    yui "With the turnover rate so high at his local establishment, he's been forced to work almost every position."
    yui "He doesn't even get paid the overtime he deserves. If I were him, I would quit that job before it affected my health."
    show kichi_halfbody_upset
    hide yui_halfbody_thinking
    with Dissolve(0.25)
    kichi "Oh, the poor boy. He must be running on fumes at this point."
    hk "That's crazy! As much as I am dedicated to my job, I would never do anything as long as what he is doing!"
    show kichi_halfbody_frustrated
    hide kichi_halfbody_upset
    with Dissolve(0.25)
    kichi "I mean, the reason why he's sleeping now is because he just finished up a twelve hour shift."
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff") 
    hk "Twelve hours!?"
    kichi "Mmm hmm! He's so sleep-deprived that he goes into a panic whenever anyone mentions anything remotely fast-food related."
    show yashimata_halfbody_frustrated
    hide kichi_halfbody_frustrated
    with Dissolve(0.25)
    yashimata "So, no free burger?"
    show yui_halfbody_upset
    hide yashimata_halfbody_frustrated
    with Dissolve(0.25)
    yui "Quiet!!"
    show eizo_halfbody_upset
    hide yui_halfbody_upset
    with Dissolve(0.25)
    eizo "Thank you for your order, sir! Your number seven, large, extra fries, no cheese, five cheese, add onions is all good to go!"
    hide eizo_halfbody_upset
    with Dissolve(0.15)
    play sfx_channel faint volume 2.0 noloop
    with vpunch
    sfxText "{i}*SLAM*{/i}"  
    hk "Holy shit! You weren't kidding!"

    # KICHI YUI AND EIZO EXIT HERE
    show yui_halfbody_cool
    with Dissolve(0.25)
    play sfx_channel stern_sfx volume 1.00 noloop
    yui "Hey! What's your deal?"
    yui "You know about Eizo's poor stress. Why do you have to continue and trigger it?"
    show yashimata_halfbody_upset
    hide yui_halfbody_cool
    with Dissolve(0.25)
    yashimata "Oh man, I am so sorry. I really thought we were gonna get...uh...a package delivered..."
    show kichi_halfbody_annoyed
    hide yashimata_halfbody_upset
    with Dissolve(0.25)
    kichi "Well, we gotta step in and help before he really does injure himself."    
    kichi "Yui, darlin', I hate to cut the chatter, but would you be able to help move him upstairs to his room?"
    show kichi_halfbody_neutral
    hide kichi_halfbody_annoyed
    with Dissolve(0.25)
    kichi "A bed would be so much nicer than this big 'ol table."
    show yui_halfbody_upset
    hide kichi_halfbody_neutral
    with Dissolve(0.25)
    yui "Ah, gotcha! Do you want me to carry him by the legs or the arms?"
    show kichi_halfbody_neutral
    hide yui_halfbody_upset
    with Dissolve(0.25)
    kichi "The arms, please!"
    show kichi_halfbody_annoyed
    hide kichi_halfbody_neutral
    with Dissolve(0.25)
    kichi "Now, dumplin', I wish that I could continue with introducin' you to everyone else, but this here truly takes more precedence."
    kichi "My greatest apologies."
    hk "There's no need to apologize, Kichi! You've already helped me quite enough."
    show kichi_halfbody_happy
    hide kichi_halfbody_annoyed
    with Dissolve(0.25)
    kichi "Oh, bless your heart!"
    kichi "The fates have it written in the stars that the rest of the introductions will be enjoyable!"
    show kichi_halfbody_neutral
    hide kichi_halfbody_happy
    with Dissolve(0.25)
    kichi "Alright then, ready, dear?"
    show yui_halfbody_neutral
    hide kichi_halfbody_neutral
    with Dissolve(0.25)
    yui "Indeed I am."
    show yui_halfbody_happy
    hide yui_halfbody_neutral
    with Dissolve(0.25)
    yui "Hey, Hisako, we'll pick up this conversation later, ok?"
    yui "There is still so much inspiration I want to get from you!!"
    hk "Sounds good to me! I look forward to talking with you soon!" # EXIT KICHI YUI EIZO 

    # INSERT MULTIPLE FOOTSTEP SFX HERE ####
    play sfx_channel double_walk_sfx volume 0.85 noloop
    hide yui_halfbody_happy
    with Dissolve(1.0)    

    # YASHIMATA AND THE PSYCHIC INTRODUCTION
    show yashimata_halfbody_happy
    with Dissolve(0.75)
    yashimata "Ah, this is so cool! Getting to meet my peers!"
    yashimata "Glad to hear we're learning more about one another. Ahhhhhhhhhhhh... ..."
    hk "... ..."
    show naoki_halfbody_frustrated
    hide yashimata_halfbody_happy
    with Dissolve(0.25)
    naoki "... ..."
    show yashimata_halfbody_zoned
    hide naoki_halfbody_frustrated
    with Dissolve(0.25)
    yashimata "... ..."
    hk "But, you haven't even introduced yourself."
    show yashimata_halfbody_neutral
    hide yashimata_halfbody_zoned
    with Dissolve(0.25)
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff") 
    yashimata "Oh, really? I guess I forgot that I have an ability as well."
    $ yashimata.name = "Yashimata Yamanaka" # NAME CHANGE 
    show yashimata_halfbody_happy
    hide yashimata_halfbody_neutral
    with Dissolve(0.25)
    yashimata "The name is Yashimata Yamanaka, {color=#efcc00}{b}Ultimate Rhythm Game Player{/b}{/color}."

    # SHOW YASHIMATA CHARACTER CARD
    show yashimata_halfbody_neutral
    hide yashimata_halfbody_happy
    with Dissolve(0.25)
    show yashimata_card_background behind yashimata_halfbody_neutral
    with Dissolve(0.25) 
    show yashimata_halfbody_neutral at left
    with ease 
    play sfx_channel card_intro_shine volume 2.00 noloop  
    show yashimata_card_font behind yashimata_halfbody_neutral
    with Dissolve(0.10)
    with hpunch
    $ renpy.pause(2.5, hard=True) 
    hide yashimata_card_font
    hide yashimata_card_background
    with Dissolve(0.10)
    show yashimata_halfbody_neutral at center
    with ease

    # AFTER INTRO
    hk "The {color=#efcc00}{b}Ultimate Rhythm Game Player{/b}{/color}!! That's so cool! I assume you've been playing since you learned how to walk?"
    show yashimata_halfbody_happy
    hide yashimata_halfbody_neutral
    with Dissolve(0.25)
    yashimata "Nah. I only recently starting playing."
    yashimata "I believe I was 15 when I found my passion for rhythm games."
    show naoki_halfbody_upset
    hide yashimata_halfbody_happy
    with Dissolve(0.25)
    naoki "15? Do you mean it took you that long to realize you had the potential to be an {color=#efcc00}{b}Ultimate{/b}{/color}?"
    show yashimata_halfbody_frustrated
    hide naoki_halfbody_upset
    with Dissolve(0.25)
    yashimata "...I guess so...I mean, I had to kinda work hard to discover my talent."
    yashimata "When I was younger, I thought I didn't have what it took to be an {color=#efcc00}{b}Ultimate{/b}{/color}."
    hkmonologue "Wow, I don't think I've seen somone so humble or dismissive of their own talent."
    hk "That is very interesting. I look forward to being friends with you getting to know you better!"
    show naoki_halfbody_happy
    hide yashimata_halfbody_frustrated
    with Dissolve(0.25)
    naoki "Same here!"
    show yashimata_halfbody_zoned
    hide naoki_halfbody_happy
    with Dissolve(0.25)
    yashimata "... ..."
    show yashimata_halfbody_happy
    hide yashimata_halfbody_zoned
    with Dissolve(0.25)
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff") 
    yashimata "Oh! I look forward to it as well!"
    show yashimata_halfbody_frustrated
    hide yashimata_halfbody_happy
    with Dissolve(0.25)
    yashimata "Sorry, I was spaced out again. I was trting to get a good luck of the new guy flaunting about!"
    show yashimata_halfbody_neutral
    hide yashimata_halfbody_frustrated
    with Dissolve(0.25)
    yashimata "Oh look, here he comes now."
    hide yashimata_halfbody_neutral
    with Dissolve(0.25)

    # PSYCHIC INTRO HERE
    stop music fadeout 1.0
    play sfx_channel fanfare_sfx volume 0.90 noloop
    $ renpy.pause(3.0, hard=True) 
    # INSERT FANFARE HERE 
    hkmonologue "Okay...where did that fanfare come from?"
    show ryosei_halfbody_frustrated
    with Dissolve(0.35)
    ryosei "... ..."
    hk "Uh, hello there. Nice to meet to you?"
    play sfx_channel thunder_sfx volume 1.0 noloop
    with vpunch
    play music high_school_snaps volume 0.85 loop
    ryosei "It is truly {i}*not*{/i} nice to meet you!"    
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff") 
    hk "Huh? Why not?"
    hk "We only just met like five seconds ago. We haven't even introduced ourselves yet!"
    show ryosei_halfbody_happy
    hide ryosei_halfbody_frustrated
    with Dissolve(0.25)
    ryosei "Well, you should know who I am! Is it not painfully obvious who I am? {i}*twinkle twinkle*{/i}"
    hkmonologue "Did he just mutter \"twinkle twinkle\" under his breath?"
    hkmonologue "Those brownies must still be active."
    hk "Um, no, I'm really sorry, I don't know who you are."
    show yashimata_halfbody_frustrated
    hide ryosei_halfbody_happy
    with Dissolve(0.25)
    yashimata "Yeahhhh, I'm in the same boat, I know absolutely nothing."
    yashimata "All I see is...glitter."
    show naoki_halfbody_happy
    hide yashimata_halfbody_frustrated
    with Dissolve(0.25)
    naoki "...Wait! I know who you are!"
    show ryosei_halfbody_happy
    hide naoki_halfbody_happy
    with Dissolve(0.25)
    ryosei "Looks like someone here truly has a brain amongst them!"
    ryosei "Please! Do inform these uneducated peons who is standing before thee."
    show naoki_halfbody_happy
    hide ryosei_halfbody_happy
    with Dissolve(0.25)
    naoki "You're Ryosei Kozato, the {color=#efcc00}{b}Psychic{/b}{/color} from TV!"
    $ ryosei.name = "Ryosei Kozato" # NAME CHANGE
    show ryosei_halfbody_happy
    hide naoki_halfbody_happy
    with Dissolve(0.25)
    ryosei "'Tis true. The one and only {color=#efcc00}{b}Ultimate Psychic{/b}{/color} in the flesh!"

    hkmonologue "{color=#efcc00}{b}Ultimate Psychic{/b}{/color}. With him and Kichi, I might confuse the two's abilities at some point."
    show naoki_halfbody_happy
    hide ryosei_halfbody_happy
    with Dissolve(0.25)
    naoki "Man, this is so cool! I don't care what everyone's been online."
    show naoki_halfbody_neutral
    hide naoki_halfbody_happy
    with Dissolve(0.25)
    naoki "So what if you were wrong? Everyone knows psychics are fake anyway. What matters is your stage presence, dude!"
    show ryosei_halfbody_frustrated
    hide naoki_halfbody_neutral
    with Dissolve(0.25)
    ryosei "... ... ..."
    ryosei "Oh is that what the critics are saying?"
    hk "Um, Naoki, I think you can stop informing us about the {i}totally accurate and amazing Ryosei Kozato{/i}!"
    hkmonologue "Please, Naoki. Please take the hint!! For all of our sakes!"
    show naoki_halfbody_happy
    hide ryosei_halfbody_frustrated
    with Dissolve(0.25)
    naoki "You are so good at getting the crowd to go wild, with your tricks and cold reading techniques!"
    show naoki_halfbody_neutral
    hide naoki_halfbody_happy
    with Dissolve(0.25)
    naoki "I wish people cheered half as loud at my concerts!"
    show ryosei_halfbody_angry
    hide naoki_halfbody_neutral
    with Dissolve(0.25)
    ryosei "... ... ... ..."
    ryosei "That's {i}*very*{/i} nice of you to say."
    show yashimata_halfbody_upset
    hide ryosei_halfbody_angry
    with Dissolve(0.25)
    yashimata "{color=#efcc00}{b}Ultimate Psychic{/b}{/color}, huh? I wish I could've been born with a talent as radical as yours."
    show ryosei_halfbody_happy
    hide yashimata_halfbody_upset
    with Dissolve(0.25)
    ryosei "Why thank you for such a compliment!"
    ryosei "Judging by the passion in your eyes, you know the hardships it takes in obtaining such a coveted acceptance."
    ryosei "You must have Ultimate ability with a prowess that close to that of my own!"
    show yashimata_halfbody_neutral
    hide ryosei_halfbody_happy
    with Dissolve(0.25)
    yashimata "Woah! You know all about that just by looking into my eyes? That's totally tubular!"
    show ryosei_halfbody_happy
    hide yashimata_halfbody_neutral
    with Dissolve(0.25)
    ryosei "But of course! There is nothing that the{color=#efcc00}{b}Ultimate Psychic{/b}{/color} can't see! \"twinkle twinkle\""
    hkmonologue "Yashimata: words cannot describe how lucky we are that you stepped in."

    # ACTUAL PSYCHIC INTRODUCTION
    hk "My apologies, Ryosei. Due to my job, I have too much work to relax or do anything leisurely in general. Truly I am."
    hk "I don't want to start on bad terms, so are you cool if we redo our introductions?"
    show ryosei_halfbody_frustrated
    hide ryosei_halfbody_happy
    with Dissolve(0.25)
    ryosei "I suppose I can give you a pass this time around. But you must promise you not forget anything I tell you!"
    hk "I promise I won't!"
    show ryosei_halfbody_neutral
    hide ryosei_halfbody_frustrated
    with Dissolve(0.25)
    ryosei "Now then, please inform me of yourself."
    hk "Alright! My name is Hisako Kawahara, and I am the {color=#efcc00}{b}Ultimate Lawyer{/b}{/color}!"
    show ryosei_halfbody_surprised
    hide ryosei_halfbody_neutral
    with Dissolve(0.25)
    ryosei "A lawyer! No wonder you have little time for yourself."
    hk "Tell me about it."
    show ryosei_halfbody_neutral
    hide ryosei_halfbody_surprised
    with Dissolve(0.25)
    ryosei "I know you were already given the details of who I am, but I will introduce myself personally as a formality."
    show ryosei_halfbody_happy
    hide ryosei_halfbody_neutral
    with Dissolve(0.25)
    ryosei "I am Ryosei Kozato. My ability is mystical and full of amazement, many might say {color=#efcc00}{b}Ultimate{/b}{/color}."
    ryosei "So therefore, I am referred to as the {color=#efcc00}{b}Ultimate Psychic{/b}{/color}. Bask in my brilliance!"

    # SHOW RYOSEI CHARACTER CARD
    show ryosei_halfbody_neutral
    hide ryosei_halfbody_happy
    with Dissolve(0.25)
    show ryosei_card_background behind ryosei_halfbody_neutral
    with Dissolve(0.25) 
    show ryosei_halfbody_neutral at left
    with ease 
    play sfx_channel card_intro_shine volume 2.00 noloop  
    show ryosei_card_font behind ryosei_halfbody_neutral
    with Dissolve(0.10)
    with hpunch
    $ renpy.pause(2.5, hard=True) 
    hide ryosei_card_font
    hide ryosei_card_background
    with Dissolve(0.10)
    show ryosei_halfbody_neutral at center
    with ease 

    # AFTER INTRO
    hkmonologue "The introduction may have been a bit lengthy, but I will admit, it was very entertaining."
    hk "It is a pleasure to meet you. I hope to become good friends with you!"
    show ryosei_halfbody_happy
    hide ryosei_halfbody_neutral
    with Dissolve(0.25)
    ryosei "Ah, to have the privilege of being my friend."
    ryosei "It will take a lot to impress me, but I can see you have the potential to do so!"
    hk "I look forward to it!"
    hkmonologue "He may be very bombastic and a bit arrogant, but I can see that underneath the facade, he's happy to see someone wants to be his friend."
    hk "Oh! Ryosei, on your way here, did you meet any other {color=#efcc00}{b}Ultimates{/b}{/color}?"
    show ryosei_halfbody_neutral
    hide ryosei_halfbody_happy
    with Dissolve(0.25)
    ryosei "Indeed! There are some sojourners about. My senses indicate you should stop by the library!"
    ryosei "You will most certainly have a very interesting time there!"
    hk "Thank you so much for your insight, Ryosei!"
    show ryosei_halfbody_happy
    hide ryosei_halfbody_neutral
    with Dissolve(0.25)
    ryosei "Haha! Never underestimate my power!"
    hk "I guess I'll be taking my leave! I will see you later!"
    show ryosei_halfbody_neutral
    hide ryosei_halfbody_happy
    with Dissolve(0.25)
    ryosei "Same to you, Ms. Kawahara!"
    hk "C'mon, Naoki, let's go!"
    show naoki_halfbody_neutral
    hide ryosei_halfbody_neutral
    with Dissolve(0.25)
    naoki "Actually, Hisako, I'm gonna probably stay here!"
    show naoki_halfbody_happy
    hide naoki_halfbody_neutral
    with Dissolve(0.25)
    naoki "There's so much I want to ask Yashimata! Like if water is wet, or why an oven is called an \"oven\" in the first place."
    hk "Oh, okay then."
    show ryosei_halfbody_thinking
    hide naoki_halfbody_happy
    with Dissolve(0.25)
    ryosei "Please, go on ahead while you can, Hisako. I can forsee this debate becoming very stupid rather quickly."
    hkmonologue "I think my intuition is picking up on that as well."
    show naoki_halfbody_frustrated
    hide ryosei_halfbody_thinking
    with Dissolve(0.25)
    naoki "So, why is it called an oven when you of in the cold food?"
    hkmonologue "Okay, I'm leaving now."

    # PLACE WALKING SFX HERE 
    play sfx_channel walking volume 0.85 noloop
    # TRANSITION OVER TO SCENE [3/12/2024 @ 1:18 AM]
    hide naoki_halfbody_frustrated
    with Dissolve(0.25)
    stop music fadeout 2.0
    hide dining_room_2
    with fade
    show transition
    with Dissolve(2.0)
    $ renpy.pause(1.75, hard=True) 

# SCENE 1-5 [WHITE WYVERN MANOR - LIBRARY] --> AFTER BEING GIVEN RYOSEI'S ADVICE, HISAKO MOVES ON OVER TO THE MANSION'S LIBRARY
# AS HISAKO CANVASSES THE SEEMINGLY INFINITE NUMBER OF BOOKS, SHE MEETS AND GETS INTO A CONFRONTATION WITH ONE OF THE OTHER ULTIMATES...
label scene1_5:    
    # RESET NAMES 
    $ matsuko.name = "???"
    $ naganori.name = "???" 
    # MONOLOGUE BEFORE ENTERING LIBRARY
    hkmonologue "I really don't know what to exprect from this library."
    hkmonologue "If the dining area was as extravagant as it was, I can't really imagine what the library looks like."
    hkmonologue "Well, this looks like the entrance. Why are the doors so big?"
    hkmonologue "Time to go in, I guess."

    # START SCENE OUT BY MOVING AWAY FROM TRANSITION SCENE AND INTO THE LIBRARY [STARTED 3/12/24 @ EST 4:47 AM]
    show library
    hide transition
    with Dissolve(1.5)
    play music laid_back volume 0.80 loop
    $ renpy.pause(1.00, hard=True)

    # ENTERS LIBRARY
    hkmonologue "... ... ..."
    hkmonologue "Holy shit! This is beyond impressive! It's so beautiful and majestic!"
    hkmonologue "The smell of ink and paper permeates throughout the room, while the mutliple mahagony shelves tower over me, making their presence known."
    hkmonologue "At least I can say the government money is being put to good use."
    hkmonologue "Wait a minute! I bet they don't have it!"
    hkmonologue "Wright...Wright...Wright..."
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff") 
    hkmonologue "There it is!"
    hkmonologue "I've been meaning to read to this for a while. {color=#efcc00}{b}The Underground Trials of the Yakuza: A Lawyer's Memoir{/b}{/color}."   
    hkmonologue "This books recounts the life of Tanaka Wright..."
    hkmonologue "A lawyer from Shinjuku, who took part in secret trials held by the Yakuza to try and convict
    enemies, whistleblowers, and the like to death."
    hkmonologue "Mr. Wright was actually able to prove the innocence of several Yazuka clients within the secret circuit!"
    hkmonologue "His stories are so inspiring! I hope that I'll be able to save people the way Mr. Wright did!"
    hkmonologue "I'm glad they have his memoir here."

    # MATSUKO INTRO 
    hk "Guess I'll continue explori..."
    stop music fadeout 1.0
    play sfx_channel damage_sfx volume 2.5 noloop
    with vpunch
    hk "Ouch!!"
    play sfx_channel stern_sfx volume 1.00 noloop
    matsuko "If you're going to look at a book, at least put it back in its proper place!"
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff")
    hk "What the..."
    play music transfixion volume 0.85 loop
    show matsuko_halfbody_neutral
    with Dissolve(0.25)
    matsuko "Without order, there is chaos. A statement that's been echoed for millennia, yet, still rings true to this day."
    hk "What? So that's that reason why you had to shove me? Was that even warranted?"
    show matsuko_halfbody_frustrated
    hide matsuko_halfbody_neutral
    with Dissolve(0.25)
    matsuko "Yes, it absolutely was! Punishment is not for revenge, but to lessen crime and reform the criminal."
    hk "But I know full well, as a {color=#efcc00}{b}Lawyer{/b}{/color}, that I didn't commit any crime or ill-will!"
    show matsuko_halfbody_neutral
    hide matsuko_halfbody_frustrated
    with Dissolve(0.25)
    matsuko "What I am trying to say is that as the {color=#efcc00}{b}Ultimate Historian{/b}{/color}..."
    matsuko "It is my responsibility to tend to this bastion of knowledge,
    making sure everything stays organized, down to the very last sheet of paper in the filing cabinets."
    hkmonologue "The {color=#efcc00}{b}Ultimate Historian{/b}{/color}. I guess I can see why she'd get upset over me misplacing the book."
    hkmonologue "But that still doesn't warrant such an unanticipated shove! She could've at least said something to me about it."
    hk "Hey, I think we got off on the wrong page here."
    show matsuko_halfbody_calm
    hide matsuko_halfbody_neutral
    with Dissolve(0.25)
    matsuko "{i}*What makes you say that.*{/i}"
    hkmonologue "... ..."
    hk "Anyway...I just wanted to apologize for putting the book back in the wrong place."    
    hk "I should've been thinking and known better that it is someone's job to make sure the library is kept tidy. I shouldn't have been ignorant."
    show matsuko_halfbody_bored
    hide matsuko_halfbody_calm
    with Dissolve(0.25)
    matsuko "{i}*sigh*{/i} Whatever, it's fine. I hope you learned something from this."
    hk "... ...Oh, yeah...I did"
    matsuko "... ..."
    hk "... ..."
    show matsuko_halfbody_neutral
    hide matsuko_halfbody_bored
    with Dissolve(0.25)
    matsuko "What? Were you expecting me to apologize for my \"unwarranted shove?\""
    hk "Um, yeah, kinda."
    show matsuko_halfbody_bored
    hide matsuko_halfbody_neutral
    with Dissolve(0.25)
    matsuko "Fine, whatever. I'm sorry that I had to shove you because you decided to put the book back in the wrong place."
    matsuko "Is that good enough for you?"
    hk "Yes, thank you very much."
    hkmonologue "I'm not even going to fight her on this. I'll take what I can get."
    show matsuko_halfbody_neutral
    hide matsuko_halfbody_bored
    with Dissolve(0.25)
    matsuko "And before you continue to sulk about the apology, you might as well tell me who you are."
    hkmonologue "Daring today, aren't we?"
    hk "Oh, okay! My name is Hisako Kawahara, and I am the {color=#efcc00}{b}Ultimate Lawyer{/b}{/color}! How about yourself?"
    $ matsuko.name = "Matsuko Chigusa" #NAME CHANGE 
    show matsuko_halfbody_bored
    hide matsuko_halfbody_neutral
    with Dissolve(0.25)
    matsuko "{i}*sigh*{/i} Name's Matsuko Chigusa, and as I have already informed you, I am the {color=#efcc00}{b}Ultimate Historian{/b}{/color}."
    
    # SHOW MATSUKO CHARACTER CARD
    show matsuko_halfbody_neutral
    hide matsuko_halfbody_bored
    with Dissolve(0.25)
    show matsuko_card_background behind matsuko_halfbody_neutral
    with Dissolve(0.25) 
    show matsuko_halfbody_neutral at left
    with ease 
    play sfx_channel card_intro_shine volume 2.00 noloop  
    show matsuko_card_font behind matsuko_halfbody_neutral
    with Dissolve(0.10)
    with hpunch
    $ renpy.pause(2.5, hard=True) 
    hide matsuko_card_font
    hide matsuko_card_background
    with Dissolve(0.10)
    show matsuko_halfbody_neutral at center
    with ease

    # AFTER INTRO 
    hk "Well, it's very nice to meet you, and I hope that we can get to know each other better and become good friends!"
    show matsuko_halfbody_bored
    hide matsuko_halfbody_neutral
    with Dissolve(0.25)
    matsuko "Uh huh, okay."
    hkmonologue "Hopefully things will mellow out after Orientation Week."
    hide matsuko_halfbody_bored
    with Dissolve(0.15)
    hk "Cool. Well, I think I will be going on my way..."    
    
    # NAGANORI APPEARS
    stop music fadeout 1.0
    show naganori_halfbody_frustrated
    with Dissolve(0.10)
    play sfx_channel thunder_sfx volume 1.0 noloop
    with vpunch    
    naganori "What's with all of this commotion going on here?"
    hkmonologue "Oh, not again..."
    hk "Well, you see, it's pretty simple."
    hk "I forgot to put a book back in its proper place, and Matsuko over there gave me an important lesson on why I should keep the library tidy."
    show naganori_halfbody_bored
    hide naganori_halfbody_frustrated
    with Dissolve(0.25)
    naganori "While this is such a {i}*heartwarming*{/i} free-time event..."
    naganori "That is something that could've been discussed outside or in one of the many office spaces."
    show naganori_halfbody_frustrated
    hide naganori_halfbody_bored
    with Dissolve(0.25)
    naganori "Didn't anyone ever teach either of you proper about library etiquette?"
    hkmonologue "Okay...I was not expecting both of us to be scolded by someone who is actively breaking the rule of library etiquette as they speak."
    show naganori_halfbody_neutral
    hide naganori_halfbody_frustrated
    with Dissolve(0.25)
    naganori "You, Matsuko: libraries are an integral part of a Historian's job. Try to act more professional from now on."
    show naganori_halfbody_bored
    hide naganori_halfbody_neutral
    with Dissolve(0.25)
    naganori "No one wants to see a 22-year-old playing pretend with a highly gifted ability. We're all {color=#efcc00}{b}Ultimates{/b}{/color} here, arent we?"
       
    # MATSUKO EXITS HERE 
    show matsuko_halfbody_frustrated
    hide naganori_halfbody_bored
    with Dissolve(0.25)
    matsuko "{i}*scoffs*{/i} Whatever." 
    play sfx_channel walking volume 0.85 noloop
    hide matsuko_halfbody_frustrated
    with Dissolve(1.00)

    # NAGANORI INTRODUCTION 
    play music laid_back volume 0.80 loop
    show naganori_halfbody_bored
    with Dissolve(0.50)
    naganori "And as for you: I expected more from a {color=#efcc00}{b}Lawyer{/b}{/color} such as yourself, {color=#efcc00}{b}Hisako{/b}{/color}."
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff")
    hk "Hold on! How did you know my name and {color=#efcc00}{b}Ultimate{/b}{/color}?"
    hk "I haven't even told you!"
    show naganori_halfbody_neutral
    hide naganori_halfbody_bored
    with Dissolve(0.25)
    naganori "Because I was able to use my {color=#efcc00}{b}Ultimate{/b}{/color} to get into the University's database."
    naganori "Not only do I know everything about you, {color=#efcc00}{b}Hisako Kawahara{/b}{/color}, I also know everything about our enire class."
    hk "So you have to be the {color=#efcc00}{b}Ultimate Hacker{/b}{/color}, I presume?"
    show naganori_halfbody_happy
    hide naganori_halfbody_neutral
    with Dissolve(0.25)
    naganori "Correct. Not bad deductions for a lawyer."
    $ naganori.name = "Naganori Miyabe" # NAME CHANGE 
    naganori "Naganori Miyabe, pleased to make your acquaintance."

    # SHOW NAGANORI CHARACTER CARD
    show naganori_halfbody_neutral
    hide naganori_halfbody_happy
    with Dissolve(0.25)
    show naganori_card_background behind naganori_halfbody_neutral
    with Dissolve(0.25) 
    show naganori_halfbody_neutral at left
    with ease 
    play sfx_channel card_intro_shine volume 2.00 noloop  
    show naganori_card_font behind naganori_halfbody_neutral
    with Dissolve(0.10)
    with hpunch
    $ renpy.pause(2.5, hard=True) 
    hide naganori_card_font
    hide naganori_card_background
    with Dissolve(0.10)
    show naganori_halfbody_neutral at center
    with ease
    hk "Pleased to make your acquaintance as well!" 
    hk "... ..."
    naganori "... ..."
    hkmonologue "Why is he staring at me like that?"
    hkmonologue "It's as if he is trying to examine every move I have, can, and will make!"
    show naganori_halfbody_bored
    hide naganori_halfbody_neutral
    with Dissolve(0.25)
    hkmonologue "Is it because he is a hacker and used to anticipating his enemies' next moves?"
    show naganori_halfbody_neutral
    hide naganori_halfbody_bored
    with Dissolve(0.25)
    naganori "Is something the matter, Hisako?"
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff")
    hk "!!!"
    hk "Oh, no! Sorry, I didn't know what else to talk about, then got lost in thought."
    show naganori_halfbody_happy
    hide naganori_halfbody_neutral
    with Dissolve(0.25)
    naganori "There's no need to apologize."
    naganori "I experience that quite often, especially after long sessions of only staring at computer screens."
    hkmonologue "Maybe he was also lost in thought. Maybe I'm just overthinking at this point."
    hk "Well, I can't wait to get to know you better, and I hope to be good friends with you!"
    show naganori_halfbody_bored
    hide naganori_halfbody_happy
    with Dissolve(0.25)
    naganori "...Um, same with you."
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff")
    hkmonologue "What was with the reluctance?"
    hkmonologue "I mean we did just meet, but I'm trying to be very optimistic and outgoing."
    hkmonologue "Again, probably just overthinking about it."

    # OTHER ULTIMATES AND END OF SCENE 
    hk "Hey, Naganori!"
    show naganori_halfbody_neutral
    hide naganori_halfbody_bored
    with Dissolve(0.25)
    naganori "Hmm? Need something?"
    hk "Actually, yes! Do you know if there are any other {color=#efcc00}{b}Ultimates{/b}{/color} in the library?"
    show naganori_halfbody_bored
    hide naganori_halfbody_neutral
    with Dissolve(0.25)
    naganori "Let's see...I don't believe there are others in the library per se, but best bet would be to check the basement."
    hk "The basement?"
    naganori "Yeah. There's a bar downstairs, and I saw the {color=#efcc00}{b}bartender{/b}{/color} there serving drinks."
    hk "Oh, wow! Thank you for the help, Naganori!"
    show naganori_halfbody_happy
    hide naganori_halfbody_bored
    with Dissolve(0.25)
    naganori "No problem."
    hk "I'll see you around!"
    show naganori_halfbody_neutral
    hide naganori_halfbody_happy
    with Dissolve(0.25)
    naganori "And, Hisako, one more thing:"
    show naganori_halfbody_bored
    hide naganori_halfbody_neutral
    with Dissolve(0.25)
    naganori "Take this time to settle down and relax for once, okay?"
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff")
    hk "Ah! O-Okay..."
    show naganori_halfbody_neutral
    hide naganori_halfbody_bored
    with Dissolve(0.25)
    naganori "Good. I'll be seeing you then."
    naganori "Goodbye, Hisako." 
    
    # LEAVE NAGANORI
    play sfx_channel walking volume 0.85 noloop
    hide naganori_halfbody_neutral
    with Dissolve(1.00)
    hk "Um, goodbye..."
    hkmonologue "How does he know about my stress? Does my face really say it all?" 
    
    # END SCENE 5
    # PLACE WALKING SFX HERE 
    play sfx_channel walking volume 0.85 noloop
    # TRANSITION OVER TO SCENE [3/13/2024 @ 2:46 AM]    
    stop music fadeout 2.0
    hide library
    with fade
    show transition
    with Dissolve(2.0)
    $ renpy.pause(1.75, hard=True)

# SCENE 1-6 [WHITE WYVERN MANOR - BASEMENT BAR] --> HISAKO HEADS DOWN TO THE BASEMENT TO VISIT THE MANOR'S BAR. WHO WILL SHE MEET NEXT?
label scene1_6:
    # RESET NAMES 
    $ narumi.name = "???"
    $ yukako.name = "???"
    # START SCENE OUT BY MOVING AWAY FROM TRANSITION SCENE AND INTO THE LIBRARY [STARTED 3/18/24 @ EST 1:26 AM]
    show bar
    hide transition
    with Dissolve(1.5)
    play music bell_pepper_beef volume 0.80 loop
    $ renpy.pause(1.00, hard=True)

    hkmonologue "This is even more breathtaking than the mahogany bookshelves! This bar is so fancy!"
    hkmonologue "Whoever built this place had a real affinity for speakeasies and club life!"
    hkmonologue "Enough staring and being awkward! Let's just go sit at the counter."
    # PLACE WALKING SFX HERE 
    play sfx_channel walking volume 0.85 noloop
    sfxText "{i}*Step Step Step*{/i}"
    # ENTER NARUMI
    show narumi_halfbody_neutral
    with Dissolve(0.50)
    narumi "..." 
    hk "...Um..."
    hkmonologue "Wow! I've dealt with imtimidating individuals before, but this one takes the cake!"
    hkmonologue "Her aura is so ice-cold, I can't even speak in response!"
    show narumi_halfbody_upset
    hide narumi_halfbody_neutral 
    with Dissolve(0.25)
    narumi "So, are you going to order something, or are you just gonna sit there and say nothing?"
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff") 
    hk "Huh? I'm so sorry! I guess I'll order an Ol' Fashioned?"
    show narumi_halfbody_neutral 
    hide narumi_halfbody_upset
    with Dissolve(0.25)
    narumi "Coming right up."
    hk "Thank you very..."
    play sfx_channel ice_cube_sfx volume 1.00 noloop
    sfxText "{i}*Clink Clink Clank*{/i}"
    hk "...Much."
    narumi "Anytime."
    hk "How were you able to make that so quickly? That seems almost impossible!"
    narumi "There are two things that are non-negotiable with my profession: speed and efficiency."
    show narumi_halfbody_frustrated
    hide narumi_halfbody_neutral
    with Dissolve(0.25)
    narumi "Without those two, you'd end up being a worthless {color=#efcc00}{b}Bartender{/b}{/color}!"
    hk "Well, I appreciate it very much."
    show narumi_halfbody_neutral
    hide narumi_halfbody_frustrated
    with Dissolve(0.25)
    narumi "It's part of my job. No need to thank me."
    hk "..."
    show narumi_halfbody_bored
    hide narumi_halfbody_neutral
    with Dissolve(0.25)
    narumi "..."
    hk "So...how do you like the university so far?"
    show narumi_halfbody_neutral
    hide narumi_halfbody_bored
    with Dissolve(0.25)
    narumi "It's fine."
    hk "What do you think about the Manor and the bar?"
    narumi "They're well-stocked, so that's a plus."
    hk "Oh, wow..."
    show narumi_halfbody_bored
    hide narumi_halfbody_neutral
    with Dissolve(0.25)
    narumi "..."
    hk "..."
    show narumi_halfbody_neutral
    hide narumi_halfbody_bored
    with Dissolve(0.25)
    narumi "Do you need anything else? If not, I'm heading to the back and washing some glassware."
    hk "I'm all set, thank you."
    show narumi_halfbody_bored
    hide narumi_halfbody_neutral
    with Dissolve(0.25)
    narumi "Alright then. Holler if you need another drink or whatever."
    play sfx_channel walking volume 0.85 noloop
    hide narumi_halfbody_bored
    with Dissolve(1.00)
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff") 
    hk "Wait!"
    show narumi_halfbody_neutral
    with Dissolve(0.50)
    narumi "What's up?"
    hk "Before you leave, would you mind telling me who are you?"
    show narumi_halfbody_bored
    hide narumi_halfbody_neutral
    with Dissolve(0.25)
    narumi "Narumi Kurihara, pleased to be of service."

    # SHOW NARUMI CHARACTER CARD
    show narumi_halfbody_neutral
    hide narumi_halfbody_bored
    with Dissolve(0.25)
    show narumi_card_background behind narumi_halfbody_neutral
    with Dissolve(0.25) 
    show narumi_halfbody_neutral at left
    with ease 
    play sfx_channel card_intro_shine volume 2.00 noloop  
    show narumi_card_font behind narumi_halfbody_neutral
    with Dissolve(0.10)
    with hpunch
    $ renpy.pause(2.5, hard=True) 
    hide narumi_card_font
    hide narumi_card_background
    with Dissolve(0.10)
    show narumi_halfbody_neutral at center
    with ease

    # AFTER INTRO
    hk "Nice to meet you, Narumi! I'm Hisako Kawahara: {color=#efcc00}{b}Ultimate Lawyer{/b}{/color}!"
    show narumi_halfbody_bored
    hide narumi_halfbody_neutral
    with Dissolve(0.25)
    narumi "Hmph. Interesting to know. I'll be headed to the back now." 
    # EXIT NARUMI
    play sfx_channel walking volume 0.85 noloop
    hide narumi_halfbody_bored
    with Dissolve(1.00)
    hk "Oh, okay."
    hkmonologue "Did I do something wrong?"

    # YUKAKO APPEARANCE AND INTRODUCTION
    show yukako_halfbody_neutral
    with Dissolve(0.25)
    yukako "No, you didn't. Trust me."
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff") 
    hk "W-Wha? When did you get here? And how did you know what I was thinking?"
    hk "Are you a psychic too?"
    show yukako_halfbody_frustrated
    hide yukako_halfbody_neutral 
    with Dissolve(0.25)
    yukako "......"
    yukako "... ... ..."
    show yukako_halfbody_neutral 
    hide yukako_halfbody_frustrated
    with Dissolve(0.25)
    yukako "Sorry, too many questions."
    hk "Oh, I'm really sorry I didn't mean to throw so much at you."    
    yukako "It's okay..."
    yukako "So...I was always here, just sitting near the end of the counter."
    show yukako_halfbody_happy
    hide yukako_halfbody_neutral
    with Dissolve(0.25)
    yukako "As for what you were thinking: I am not a psychic. Your face reads like an open book."
    hk "Does it really?"
    yukako "Mhm. If you haven't realized it...the bartender isn't much of a talker, so don't take it personally."
    show yukako_halfbody_neutral
    hide yukako_halfbody_happy
    with Dissolve(0.25)
    yukako "As with most bartenders, they need to remain stoic and poker-faced."
    yukako "Not only just soley to hide their emotions while on the job, but also to assess everything happening around them."
    yukako "It's their job to make sure their patrons stay safe."
    hk "Saying it that way makes much more sense. Thank you. I feel a little bit better."
    yukako "No problem at all."
    $ yukako.name = "Yukako Maeno" # NAME CHANGE 
    show yukako_halfbody_happy
    hide yukako_halfbody_neutral
    with Dissolve(0.25)
    yukako "I'm Yukako, by the way. Yukako Maeno. And what was your name and {color=#efcc00}{b}Ultimate{/b}{/color} again?"
    hk "Hisako Kawahara and I am the {color=#efcc00}{b}Ultimate Lawyer{/b}{/color}!"
    yukako "Nice to meet you, Hisako Kawahara."
    hk "Same here, Yukako!" 
    hk "Also, what was your {color=#efcc00}{b}Ultimate{/b}{/color}? I don't think you mentioned it."
    show yukako_halfbody_thinking
    hide yukako_halfbody_happy
    with Dissolve(0.25)
    yukako "... ..."
    yukako "Is that so? My apologies."
    show yukako_halfbody_happy
    hide yukako_halfbody_thinking
    with Dissolve(0.25)
    yukako "I am...the {color=#efcc00}{b}Ultimate Forensics Expert{/b}{/color}."

    # SHOW YUKAKO CHARACTER CARD
    show yukako_halfbody_neutral
    hide yukako_halfbody_happy
    with Dissolve(0.25)
    show yukako_card_background behind yukako_halfbody_neutral
    with Dissolve(0.25) 
    show yukako_halfbody_neutral at left
    with ease 
    play sfx_channel card_intro_shine volume 2.00 noloop  
    show yukako_card_font behind yukako_halfbody_neutral
    with Dissolve(0.10)
    with hpunch
    $ renpy.pause(2.5, hard=True) 
    hide yukako_card_font
    hide yukako_card_background
    with Dissolve(0.10)
    show yukako_halfbody_neutral at center
    with ease

    # AFTER INTRO
    hk "You don't need to apologize for something so minor!"
    show yukako_halfbody_happy
    hide yukako_halfbody_neutral
    with Dissolve(0.25)
    yukako "I guess...that is true."
    hk "But I hope to become better friends from you!"
    show yukako_halfbody_neutral
    hide yukako_halfbody_happy
    with Dissolve(0.25)
    yukako "...Same here?"
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff") 
    hkmonologue "Why was that phrased as a question?"
    hk "Hey, are you doing okay?"
    hk "Your speech has been pretty inconsistent, and I just want to make sure you're alright. Have you had too much to drink?"
    show yukako_halfbody_upset
    hide yukako_halfbody_neutral 
    with Dissolve(0.25)
    yukako "... ..."
    yukako "Yeah, I think I've had a little too much...and I'm also quite tired."
    show yukako_halfbody_frustrated
    hide yukako_halfbody_upset
    with Dissolve(0.25)
    yukako "It's been a very long day."
    hk "Oh, I'm really sorry to hear that. Please take care of yourself!"
    show yukako_halfbody_happy
    hide yukako_halfbody_frustrated
    with Dissolve(0.25)
    yukako "I appreciate your concern, Hisako Kawahara, but don't worry, I will be fine."
    hk "If you say so, I'll believe you."
    yukako "Trust me...this happens more than you think."
    hk "I can imagine, especially within a profession such as yours."
    yukako "Indeed..."
    hk "...Well, I guess I will be taking my leave."
    hk "I should try and find the rest of the other {color=#efcc00}{b}Ultimates{/b}{/color} and introduce myself before Orientation Week really gets underway."
    show yukako_halfbody_neutral
    hide yukako_halfbody_happy
    with Dissolve(0.25)
    yukako "My memory is a little hazy, but...try the music room on the...2nd floor?"
    yukako "There should be some more {color=#efcc00}{b}Ultimates{/b}{/color} there for you to conversate with."
    hk "Oh, awesome! Thank you for the tip!"
    show yukako_halfbody_happy
    hide yukako_halfbody_neutral
    with Dissolve(0.25)
    yukako "...You're welcome. Take care and...see you soon."
    hk "Same to you! Hope you feel better!"
    yukako "Many thanks, Hisako Kawahara."  
    
    # END SCENE 6
    # PLACE WALKING SFX HERE 
    hide yukako_halfbody_happy
    with Dissolve(0.25)
    play sfx_channel walking volume 0.85 noloop
    # TRANSITION OVER TO SCENE [3/18/2024 @ 4:33 AM --> 5:04 AM WITH EDITS/REVISIONS]    
    stop music fadeout 2.0
    hide bar
    with fade
    show transition
    with Dissolve(2.0)
    $ renpy.pause(1.75, hard=True)

# SCENE 1-7 [WHITE WYVERN MANOR - MUSIC ROOM] --> AFTER LEAVING YUKAKO AT THE BAR, HISAKO TAKES THE TIP AND HEADS UP TO THE 2ND FLOOR MUSIC ROOM.
# AS SHE ENTERS THE VAST, OPEN HALL, SHE CAN HEAR THE SOUND OF OTHER PEOPLE TALKING.
label scene1_7:
    # RESET NAMESD
    $ azumi.name = "???"
    $ fujiko.name = "???"
    $ chino.name = "???"
    # START SCENE OUT BY MOVING AWAY FROM TRANSITION SCENE AND INTO THE LIBRARY [STARTED 3/19/24 @ EST 2:15 AM]
    show music_room
    hide transition
    with Dissolve(1.5)
    play music harpsichord_fuge volume 0.80 loop
    $ renpy.pause(1.00, hard=True)

    hkmonologue "... ... ..."
    hkmonologue "It's...magnificent!"
    hkmonologue "It is a literal 1-to-1 replica of a Baroque-style music hall!"
    hkmonologue "And someone is playing the harpsichord over there!"
    hkmonologue "Ahhh...just imagine it: a composer like Vivaldi! Someone with such a high prominence in society..."
    hkmonologue "...Standing right before your eyes to conduct a symphony that would be beyond anything a human ever heard before!"
    hkmonologue "The harpsichord plucking at its strings."
    hkmonologue "The ensemble of stringed instruments emanating a bright and sweet sound as the bows move ever so gently."
    hkmonologue "And the brass establishing their presence with their deep bass that amplifies the strings' beauty!"
    hkmonologue "Oh, how I wish I could see such a performance..."

    # AZUMI INTRODUCTION
    show azumi_halfbody_upset
    with Dissolve(0.25)
    azumi "Uh, hey...are you...doing alright?"
    hk "Hu-huh?" 
    azumi "I mean, you entered the hall, and now you're just standing there, staring at the ceiling, mumbling to yourself."
    hk "Oh..."
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff") 
    hk "OH!"
    hk "I am so sorry! I just got caught up in the beauty and wonder of the hall."
    show azumi_halfbody_neutral
    hide azumi_halfbody_upset
    with Dissolve(0.25)
    azumi "Hey! It's okay! I almost had a similar experience, immediately drawn by the grand harpsichord in the corner."
    hk "Same here! I heard its beautiful melody and was suddenly entranced by it!"
    show azumi_halfbody_happy
    hide azumi_halfbody_neutral
    with Dissolve(0.25)
    azumi "Well, it's what they always say: Music is the gateway to the soul!"
    hk "It truly is!"
    hk "Oh, I'm sorry, I never introduced myself. My name is Hisako Kawahara: {color=#efcc00}{b}Ultimate Lawyer{/b}{/color}!"
    show azumi_halfbody_neutral
    hide azumi_halfbody_happy
    with Dissolve(0.25)
    azumi "A lawyer! Noice! It's so nice to meet you, Hisako!"
    $ azumi.name = "Azumi Yoshizawa" # NAME CHANGE 
    azumi "I'm Azumi Yoshizawa, and I am the {color=#efcc00}{b}Ultimate Tattoo Artist{/b}{/color}!"

    # SHOW AZUMI CHARACTER CARD
    show azumi_halfbody_neutral
    with Dissolve(0.25)
    show azumi_card_background behind azumi_halfbody_neutral
    with Dissolve(0.25) 
    show azumi_halfbody_neutral at left
    with ease 
    play sfx_channel card_intro_shine volume 2.00 noloop  
    show azumi_card_font behind azumi_halfbody_neutral
    with Dissolve(0.10)
    with hpunch
    $ renpy.pause(2.5, hard=True) 
    hide azumi_card_font
    hide azumi_card_background
    with Dissolve(0.10)
    show azumi_halfbody_neutral at center
    with ease

    # AFTER INTRO
    hk "A tattoo artist? That's so cool! Your sleeves make so much sense now, and I may say are so beautiful!"
    show azumi_halfbody_happy
    hide azumi_halfbody_neutral
    with Dissolve(0.25)
    azumi "Aw, thank you so much, Hisako! I really appreciate it when people compliment my tats!"
    azumi "So, have you considered getting one?"
    hk "Me? I've considered getting a small one on my wrist, but never really committed to it, due to being so busy with work!"
    show azumi_halfbody_neutral
    hide azumi_halfbody_happy
    with Dissolve(0.25)
    azumi "Well, we're all in uni now, so if you ever commit to it, let me know! I'll even do it free of charge!"
    hk "Are you serious? I'll definitely take you on that offer after Orientation Week!"
    azumi "Sounds good to me!"
    azumi "So, while you're still here, I want to introduce you to the others. Here, follow me!"
    hk "A-Alright."
    hkmonologue "It's weird that she said others in the plural form."
    hkmonologue "I only see one other person in this entire hall, and it's the one who is playing the harpsichord."
    show azumi_halfbody_happy
    hide azumi_halfbody_neutral
    with Dissolve(0.25)
    azumi "Hey, {color=#efcc00}{b}Fujiko{/b}{/color}, I've got someone new to introduce you to!"

    # FUJIKO INTRODUCTION
    show fujiko_halfbody_bored
    hide azumi_halfbody_happy
    with Dissolve(0.25)
    fujiko "Oh, really? It feels as though I've already been introduced to you."
    stop music fadeout 1.0
    show fujiko_halfbody_neutral
    hide fujiko_halfbody_bored
    with Dissolve(0.25)
    fujiko "How do you do {color=#efcc00}{b}Ms. Lawyer{/b}{/color}?"
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff") 
    hk "Wait! How did you know my {color=#efcc00}{b}Ultimate{/b}{/color}? I mean, I know I told Azumi my ability, but that was {i}*way*{/i} over there!"
    show fujiko_halfbody_happy
    hide fujiko_halfbody_neutral
    with Dissolve(0.25)
    fujiko "Well, who's to say that I don't have more than one {color=#efcc00}{b}Ultimate{/b}{/color}?"
    play sfx_channel thunder_sfx volume 1.00 noloop
    with vpunch
    hk "More...than one!?"
    hk "I can tell that you are the {color=#efcc00}{b}Ultimate Pianist{/b}{/color} based purely on the fact that you can have a 
    conversation while playing."
    hk "But now that you knew that I was a lawyer, I'm thinking:"
    hk "Are you also the {color=#efcc00}{b}Ultimate Clairvoyant{/b}{/color}?"
    show fujiko_halfbody_neutral
    hide fujiko_halfbody_happy
    with Dissolve(0.25)
    fujiko "Hmm Hmm Hmmmmmm...So the great lawyer does it again. Amazing deduction!"
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff") 
    hk "Wait, I was right?"
    fujiko "..."
    show fujiko_halfbody_happy
    hide fujiko_halfbody_neutral
    with Dissolve(0.25)
    fujiko "Nah, I'm just fucking with you." 
    with vpunch   
    fujiko "Hup!"    
    play music governor_minuet volume 0.85 loop
    hk "T-The piano...it's still playing?"
    show fujiko_halfbody_bored
    hide fujiko_halfbody_happy
    with Dissolve(0.25)
    fujiko "It's actually a self-plaing {i}*harpsichord*.{/i} Y'know there is a difference between the two."
    hk "W-W-Wait a minute? I'm so confused. Are you the {color=#efcc00}{b}Ultimate Pianist{/b}{/color} and {color=#efcc00}{b}Clairvoyant{/b}{/color},
    or is there something I'm missing?"
    show azumi_halfbody_bored
    hide fujiko_halfbody_bored
    with Dissolve(0.25)
    azumi "C'mon, Fujiko. I think the joke has gone on a little too long. Why don't you just tell her?"
    show fujiko_halfbody_upset
    hide azumi_halfbody_bored
    with Dissolve(0.25)
    fujiko "Alright, alright, you win, Azumi. I am not a clairvoyant."
    hk "Then how did you know that I was a lawyer?"
    show fujiko_halfbody_bored
    hide fujiko_halfbody_upset
    with Dissolve(0.25)
    fujiko "I overheard your conversation with Azumi. The word \"Lawyer\" was said pretty loud during your introduction, ya know."
    hk "Does that mean you are..."
    fujiko "... A pianist? No, not even in the slightest."
    show fujiko_halfbody_neutral
    hide fujiko_halfbody_bored
    with Dissolve(0.25)
    fujiko "I mean, did you actually think that I would be able to play with my fucked up, crippled fingers?"
    hk "I-I just assumed you liked to wrap your finger in tape."
    show fujiko_halfbody_frustrated
    hide fujiko_halfbody_neutral
    with Dissolve(0.25)
    fujiko "Let me guess. You also thought that I was an edgy emo teen who likes to dress up as a court jester, right?" 
    hk "Uh...Um"
    fujiko "Well, I hate to be the bearer of bad news, but I'm in my mid-twenties, moron."
    play sfx_channel disappointment_sfx volume 1.25 noloop
    hk "I'm sorry, I didn't mean to assume anything."
    fujiko "But you ended up doing it anyway. Well you know what I think about that?"
    hkmonologue "Oh, man. Here comes the barrage of insults. I just met Fujiko, and I already made them upset."
    show fujiko_halfbody_happy
    hide fujiko_halfbody_frustrated
    with Dissolve(0.25)
    fujiko "...I think it's absolutely hilarious!"
    hk "Huh?"
    $ fujiko.name = "Fujiko Tsuchiya" # NAME CHANGE 
    fujiko "Yep, that's me! Fujiko Tsuchiya: the {color=#efcc00}{b}Ultimate Puppeteer{/b}{/color}!"
    fujiko "Your little gremlin child here to entertain you! {i}*Rawr xD*{/i}"

    # SHOW FUJIKO CHARACTER CARD
    show fujiko_halfbody_neutral
    hide fujiko_halfbody_happy
    with Dissolve(0.25)
    show fujiko_card_background behind fujiko_halfbody_neutral
    with Dissolve(0.25) 
    show fujiko_halfbody_neutral at left
    with ease 
    play sfx_channel card_intro_shine volume 2.00 noloop  
    show fujiko_card_font behind fujiko_halfbody_neutral
    with Dissolve(0.10)
    with hpunch
    $ renpy.pause(2.5, hard=True) 
    hide fujiko_card_font
    hide fujiko_card_background
    with Dissolve(0.10)
    show fujiko_halfbody_neutral at center
    with ease

    # AFTER INTRO 
    hkmonologue "Did she just say \"Rawr xD\" out loud?"
    show fujiko_halfbody_bored
    hide fujiko_halfbody_neutral
    with Dissolve(0.25)
    fujiko "And before you say it:"
    show fujiko_halfbody_frustrated
    hide fujiko_halfbody_bored
    with Dissolve(0.25)
    fujiko "\"If the sassy, lost child can't properly use her hands, then how would she be able to do puppetry?\""
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff") 
    hk "!!!"
    show fujiko_halfbody_happy
    hide fujiko_halfbody_frustrated
    with Dissolve(0.25)
    fujiko "That expression on your face means I'm right on the money!"
    hk "Y-Yeah, you are."
    show fujiko_halfbody_neutral
    hide fujiko_halfbody_happy
    with Dissolve(0.25)
    fujiko "Well then, I shall explain it to you: I simply work through the nerve pain and force my fingers to work."
    hk "Really!? Wouldn't that just make the situation worse?"

    # ENTER CHINO
    show chino_halfbody_neutral
    hide fujiko_halfbody_neutral
    with Dissolve(0.25)
    chino "Studies have shown that focusing on one's pain can actually make said pain even worse." 
    chino "So by participating in hobbies, it in turn, reduces discomfort and pain from the affected area!"  
    play sfx_channel thunder_sfx volume 1.00 noloop
    with vpunch
    hk "WHAT THE SHIT? WHERE DID YOU COME FROM?"
    show chino_halfbody_upset
    hide chino_halfbody_neutral
    with Dissolve(0.25)
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff") 
    with vpunch
    chino "EEEEEEAAAAA!!!"
    show fujiko_halfbody_frustrated
    hide chino_halfbody_upset
    with Dissolve(0.25)
    fujiko "Are those brownies still in your system or were you not paying attention? {color=#efcc00}{b}Chino{/b}{/color} has been next to you for a while now."
    fujiko "You just never noticed."
    show chino_halfbody_upset
    hide fujiko_halfbody_frustrated
    with Dissolve(0.25)
    chino "I'm s-s-sorry. I didn't mean to scare you or anything. I just didn't want to interrupt your conversation."
    hk "Well, I apologize for reacting the way I did."
    chino "It's okay, I'm pretty much used to reactions such as that."
    hk "I'm sorry to hear that."
    chino "It's alright."
    hk "..."
    chino "..."
    hkmonologue "I gotta break this silence, or else this whole interaction will continue to get more awkward by the second!"
    hk "Well, this is a great time to introduce myself: My name is Hisako Kawahara and I am the {color=#efcc00}{b}Ultimate Lawyer{/b}{/color}!"
    
    # CHINO INTRODUCTION 
    $ chino.name = "Chino Miyahara"
    show chino_halfbody_neutral 
    hide chino_halfbody_upset
    with Dissolve(0.25)
    chino "N-N-Nice to meet you, Hisako. I'm Chino Miyahara."
    chino "My {color=#efcc00}{b}Ultimate{/b}{/color} isn't nearly as great compared to yours, but my ability is being the {color=#efcc00}{b}Ultimate Beekeeper{/b}{/color}."
    
    # SHOW CHINO CHARACTER CARD
    show chino_halfbody_neutral    
    with Dissolve(0.25)
    show chino_card_background behind chino_halfbody_neutral
    with Dissolve(0.25) 
    show chino_halfbody_neutral at left
    with ease 
    play sfx_channel card_intro_shine volume 2.00 noloop  
    show chino_card_font behind chino_halfbody_neutral
    with Dissolve(0.10)
    with hpunch
    $ renpy.pause(2.5, hard=True) 
    hide chino_card_font
    hide chino_card_background
    with Dissolve(0.10)
    show chino_halfbody_neutral at center
    with ease

    # AFTER INTRO
    hk "I have no idea what you're talking about! Being a beekeeper is not only very cool, but also very important, so I commend you for that!"
    show chino_halfbody_blush
    hide chino_halfbody_neutral
    with Dissolve(0.25)
    chino "Really?"
    hk "Absolutely! I swear on my honor as a lawyer!"
    chino "That means s-so much to me. Thank you!"
    hk "There's no need to thank me! I look forward to getting to know you better, all of you!"
    show azumi_halfbody_happy
    hide chino_halfbody_blush
    with Dissolve(0.25)
    azumi "And we all feel the same as well!"
    show fujiko_halfbody_frustrated
    hide azumi_halfbody_happy
    with Dissolve(0.25)
    fujiko "How do you how I feel, Azumi?"
    show azumi_halfbody_neutral 
    hide fujiko_halfbody_frustrated
    with Dissolve(0.25)
    azumi "Because of my gut feeling! I just know."
    show fujiko_halfbody_happy
    hide azumi_halfbody_neutral
    with Dissolve(0.25)
    fujiko "...Hah, you know nothing about me."
    show fujiko_halfbody_neutral
    hide fujiko_halfbody_happy
    with Dissolve(0.25)
    fujiko "...but yes, I do look forward to it as well."
    show azumi_halfbody_neutral
    hide fujiko_halfbody_neutral
    with Dissolve(0.25)
    azumi "See? Told ya!"
    show fujiko_halfbody_frustrated
    hide azumi_halfbody_neutral 
    with Dissolve(0.25)
    play sfx_channel thunder_sfx volume 1.00 noloop
    with vpunch
    fujiko "You were just lucky, that's all."
    hk "Hmm Hmm! I'm so excited for the school year to start!"
    show chino_halfbody_neutral
    hide fujiko_halfbody_frustrated
    with Dissolve(0.25)
    chino "Same he-"
    stop music fadeout 1.0
    play sfx_channel school_bell volume 1.50 noloop
    sfxText "{i}*Bing Bong Ding Dong*{/i}"
    sfxText "{i}Attention: Hope's Peak Orientation Week will be starting in 15 minutes. Will all students make their way to the gymnasium. Thank you."
    show azumi_halfbody_happy
    hide chino_halfbody_neutral
    with Dissolve(0.25)
    azumi "Shall we make our way to the atrium? That's where all of our peers will most likely be!"
    hk "Sounds good to me! Let's go!"  
    
    # END SCENE 7    
    # PLACE WALKING SFX HERE 
    hide azumi_halfbody_happy
    with Dissolve(0.25)
    play sfx_channel walking volume 0.85 noloop
    # TRANSITION OVER TO SCENE [3/20/2024 @ 4:40 AM]        
    hide music_room
    with fade
    show transition
    with Dissolve(2.0)
    $ renpy.pause(1.75, hard=True)

# SCENE 1-8 [WHITE WYVERN MANOR - ATRIUM] --> AFTER THE ANNOUNCEMENT, HISAKO, CHINO, FUJIKO, AND AZUMI MAKE THEIR WAY FROM THE MUSIC ROOM TO THE ATRIUM
# IN ORDER TO GATHER WITH THE OTHER ULTIMATES. AS THEY APPROACH THE ATRIUM THEY REALIZE THEY ARE THE FIRST ONES THERE
label scene1_8: 
    # RESET NAMES 
    $ grimaldi.name = "???"
    $ vladnot.name = "???"
    $ nayoko.name = "???"
    # START SCENE OUT BY MOVING AWAY FROM TRANSITION SCENE AND INTO THE LIBRARY [STARTED 3/20/24 @ EST 4:47 AM]
    show manor_atrium
    hide transition
    with Dissolve(1.5)
    play music lets_party volume 0.80 loop
    $ renpy.pause(1.00, hard=True)

    # GROUP COMES IN 
    show azumi_halfbody_neutral
    with Dissolve(0.25)
    azumi "Well look at that! We're the first ones here!"
    show fujiko_halfbody_neutral
    hide azumi_halfbody_neutral 
    with Dissolve(0.25)
    fujiko "Well, I'm gonna sit down because who knows how long the others will take."
    show chino_halfbody_neutral
    hide fujiko_halfbody_neutral
    with Dissolve(0.25)
    chino "I'm in a-agreement."
    hkmonologue "Fujiko's right about that. The best thing to do right now is just to hand tight until the others arrive."
    hide chino_halfbody_neutral
    with Dissolve(0.25)
    hkmonologue "After a few minutes, the other {color=#efcc00}{b}Ultimates{/b}{/color} started to filter their way in."
    hkmonologue "Some came in small groups, while others by themselves."
    hkmonologue "About five minutes later, all of the familiar faces from earlier were all in one spot."
    show kazuhiko_halfbody_happy
    with Dissolve(0.25)
    hiko "Alright, is that everyone?"
    show noburo_halfbody_happy
    hide kazuhiko_halfbody_happy
    with Dissolve(0.25)
    noburo "Looks like it!"
    show kichi_halfbody_annoyed
    hide noburo_halfbody_happy 
    with Dissolve(0.25)
    kichi "Not yet, hun. We're still missing some stragglers."
    show yukako_halfbody_thinking
    hide kichi_halfbody_annoyed
    with Dissolve(0.25)
    yukako "How many of us are there altogether?"
    show naganori_halfbody_bored
    hide yukako_halfbody_thinking
    with Dissolve(0.25)
    naganori "There should be 21 in total, so we're missing three more."
    show tetsunori_halfbody_unamused
    hide naganori_halfbody_bored
    with Dissolve(0.25)
    tetsu "Well, if they don't come down soon, we're gonna be late to Orientation."
    show matsuko_halfbody_bored
    hide tetsunori_halfbody_unamused
    with Dissolve(0.25)
    matsuko "If that's the case then, we should leave without them."
    matsuko "It would be stupid for all of us to be late for the sake of leaving as a group."
    show naoki_halfbody_frustrated
    hide matsuko_halfbody_bored
    with Dissolve(0.25)
    naoki "I mean, how much time do we have left to get to the gym on time?"
    show chino_halfbody_upset
    hide naoki_halfbody_frustrated
    with Dissolve(0.25)
    chino "F-Four minutes."
    show shinzo_halfbody_frustrated
    hide chino_halfbody_upset
    with Dissolve(0.25)
    shinzo "Then I think it'd be best to high-tail it out of here!"
    show ryosei_halfbody_thinking
    hide shinzo_halfbody_frustrated
    with Dissolve(0.25)
    ryosei "Quiet all of you! I am sensing the others nearby!" 

    # ENTER GRIMALDI, VLADNOT, AND NAYOKO
    show grimaldi_halfbody_neutral
    hide ryosei_halfbody_thinking
    with Dissolve(0.25)
    grimaldi "Sorry for the wait. Grimaldi and {color=#efcc00}{b}Cheerleader{/b}{/color} had to get {color=#efcc00}{b}Mr. Vampire{/b}{/color} out 
    of very dark room."
    show yashimata_halfbody_happy
    hide grimaldi_halfbody_neutral
    with Dissolve(0.25)
    yashimata "My man the {color=#efcc00}{b}Strongman{/b}{/color}! Glad to see you again!"
    $ grimaldi.name = "Grimaldi Pagliacci" # NAME CHANGE
    show grimaldi_halfbody_laughing
    hide yashimata_halfbody_happy
    with Dissolve(0.25)
    grimaldi "Grimaldi is glad to see you too!"

    # SHOW GRIMALDI CHARACTER CARD
    show grimaldi_halfbody_neutral
    hide grimaldi_halfbody_laughing
    with Dissolve(0.25)
    show grimaldi_card_background behind grimaldi_halfbody_neutral
    with Dissolve(0.25) 
    show grimaldi_halfbody_neutral at left
    with ease 
    play sfx_channel card_intro_shine volume 2.00 noloop  
    show grimaldi_card_font behind grimaldi_halfbody_neutral
    with Dissolve(0.10)
    with hpunch
    $ renpy.pause(2.5, hard=True) 
    hide grimaldi_card_font
    hide grimaldi_card_background
    with Dissolve(0.10)
    show grimaldi_halfbody_neutral at center
    with ease
    
    $ nayoko.name = "Nayoko Morimoto" # NAME CHANGE
    show nayoko_halfbody_smug
    hide grimaldi_halfbody_neutral
    with Dissolve(0.25)
    nayoko "Sorry that Mr. Grumpy-Grouchy took so long to get out of his room."
    show nayoko_halfbody_happy
    hide nayoko_halfbody_smug
    with Dissolve(0.25)
    nayoko "Ooo! I'm so happy that everyone is here together!"

    # SHOW NAYOKO CHARACTER CARD
    show nayoko_halfbody_neutral
    hide nayoko_halfbody_happy
    with Dissolve(0.25)
    show nayoko_card_background behind nayoko_halfbody_neutral
    with Dissolve(0.25) 
    show nayoko_halfbody_neutral at left
    with ease 
    play sfx_channel card_intro_shine volume 2.00 noloop  
    show nayoko_card_font behind nayoko_halfbody_neutral
    with Dissolve(0.10)
    with hpunch
    $ renpy.pause(2.5, hard=True) 
    hide nayoko_card_font
    hide nayoko_card_background
    with Dissolve(0.10)
    show nayoko_halfbody_neutral at center
    with ease
    
    $ vladnot.name = "Vladnot Moonclair" # NAME CHANGE 
    show narumi_halfbody_upset
    hide nayoko_halfbody_neutral
    with Dissolve(0.25)
    narumi "Took you long enough."
    show vladnot_halfbody_frustrated
    hide narumi_halfbody_upset
    with Dissolve(0.25)
    vladnot "I would've left on my own time, but THESE TWO kept disturbing my peace, so I decided to oblige them."
    show yui_halfbody_thinking
    hide vladnot_halfbody_frustrated
    with Dissolve(0.25)
    yui "For someone pretending to a {color=#efcc00}{b}vampire{/b}{/color}, you really are going the extra mile! That's so fascinating!"
    show vladnot_halfbody_frustrated
    hide yui_halfbody_thinking
    with Dissolve(0.25)
    vladnot "It is {i}*not*{/i} pretending, as you so call it."
    play sfx_channel thunder volume 1.00 noloop
    with vpunch
    vladnot "You may call it a farce, but I am truly a vampire in the flesh!"

    # SHOW VLADNOT CHARACTER CARD
    show vladnot_halfbody_neutral
    hide vladnot_halfbody_frustrated
    with Dissolve(0.25)
    show vladnot_card_background behind vladnot_halfbody_neutral
    with Dissolve(0.25) 
    show vladnot_halfbody_neutral at left
    with ease 
    play sfx_channel card_intro_shine volume 2.00 noloop  
    show vladnot_card_font behind vladnot_halfbody_neutral
    with Dissolve(0.10)
    with hpunch
    $ renpy.pause(2.5, hard=True) 
    hide vladnot_card_font
    hide vladnot_card_background
    with Dissolve(0.10)
    show vladnot_halfbody_neutral at center
    with ease

    # AFTER INTROS
    show kazuhiko_halfbody_frustrated
    hide vladnot_halfbody_neutral
    with Dissolve(0.25)
    hiko "Alright, enough you two! We need to get moving! Let's go!"    
    hkmonologue "After everyone assembled, we set off toward the gym."

    # DISSOLVE ATRIUM
    hide kazuhiko_halfbody_frustrated
    with Dissolve(0.25)
    stop music fadeout 2.5
    play sfx_channel double_walk volume 1.0 noloop
    hide manor_atrium with Dissolve(0.65)
    

    # ENDING OF THE PART I
    hkmonologue "As we got closer and closer, I could feel my heart beating rapidly. I am definitely nervous, but also excited!"
    hkmonologue "I mean, I'm going to be starting a new journey here at this university alongside a diverse group of peers with many different talents!"
    hkmonologue "As the doors to the gym opened, it became clear that all of this is real and not a dream."
    hkmonologue "While my breath might be stuck in my throat from the anxiety, I have a strong feeling that everything will be okay..."
    hkmonologue "...and all of us are going to have the best time here at {color=#efcc00}{b}Hope's Peak University{/b}{/color}."

    # END PART I [FINISHED CODING @ 3/20/24 5:16 AM] [FINISHED SPRITES @ 5/16/24 AROUND 4:45 AM]   
    jump saveGamePrologueOne

    return

