# SCENE 2-1 [WHITE WYVERN MANOR - ATRIUM] --> EVERYONE ARRIVES BACK AT THE WHITE WYVERN MANOR. THE AUDIENCE WILL THINK THEY WENT TO SEE THE HEADMASTER, BUT
# MET WITH THE DEAN OF THE SCHOOL INSTEAD. IN THIS SCENE, EVERYONE WILL DECIDE TO THROW A PARTY TONIGHT TO CELEBRATE NEW BEGINNINGS
label scene2_1: 
    # COMING BACK TO THE MANOR [STARTED 6/12/24 @ 8:44 PM]

    # SHOW NEW BACKGROUND OF THE ATRIUM HERE 
    show manor_atrium
    with Dissolve(1.5)
    play music lets_party volume 0.80 loop
    $ renpy.pause(1.00, hard=True)

    # START SHOWING KAZUHIKO HERE
    show kazuhiko_halfbody_happy
    with Dissolve(0.25)
    hiko "Well, that meeting went surprisingly well!"
    show yui_halfbody_happy
    hide kazuhiko_halfbody_happy
    with Dissolve(0.25)
    yui "I will admit, I thought that something bad was going to happen, and I'm so glad it didn't!"
    show yui_halfbody_genius
    hide yui_halfbody_happy
    with Dissolve(0.25)
    yui "However, it would make for a very compelling storyline for a thriller novel!"
    yui "Oh, Muse, you never fail to inspire me!"
    show azumi_halfbody_neutral
    hide yui_halfbody_genius
    with Dissolve(0.25)
    azumi "Yeah, I wasn't expecting the Dean to be so warm and welcoming!"
    show naganori_halfbody_neutral
    hide azumi_halfbody_neutral
    with Dissolve(0.25)
    naganori "Shouldn't that always be the bare minimum?"
    naganori "If your university becomes a place filled with hatred and hostility, no one will want to come here."
    show nayoko_halfbody_smug
    hide naganori_halfbody_neutral
    with Dissolve(0.25)
    nayoko "Aw, gee! You gotta stop overthinking and be optimistic!"
    show nayoko_halfbody_happy
    hide nayoko_halfbody_smug
    with Dissolve(0.25)
    nayoko "Our Dean is a wonderfully kind person, and that is what we should focus on!"
    show tetsunori_halfbody_surprised
    hide nayoko_halfbody_happy
    with Dissolve(0.25)
    tetsu "I also very surpised by how swift and orangized they are."
    show tetsunori_halfbody_neutral
    hide tetsunori_halfbody_surprised
    with Dissolve(0.25)
    tetsu "They already gave us everything we needed for the start of classes next week, and it's still only the first day of Orientation Week!"
    show yukako_halfbody_sleepy
    hide tetsunori_halfbody_neutral
    with Dissolve(0.25)
    yukako "With a place like this...I can see why."
    yukako "The sooner they figure out the logistics of the program, the faster they help us hone in on our {color=#efcc00}{b}Ultimate Talent{/b}{/color}..."
    show yukako_halfbody_happy
    hide yukako_halfbody_sleepy
    with Dissolve(0.25)
    yukako "...and the sooner we can go out into the world and improve it."
    show tetsunori_halfbody_thinking
    hide yukako_halfbody_happy
    with Dissolve(0.25)
    tetsu "I never thought of it from that point of view."
    show kazuhiko_halfbody_happy
    hide tetsunori_halfbody_thinking
    with Dissolve(0.25)
    hiko "Man, I am so pumped for classes to start!"
    hiko "I'll get to learn new concepts and ideas, see new people, make new friends, and also find ways to improve myself!"
    show naoki_halfbody_happy
    hide kazuhiko_halfbody_happy
    with Dissolve(0.25)
    naoki "That's the spirit, Hiko!"
    show nayoko_halfbody_happy
    hide naoki_halfbody_happy
    with Dissolve(0.25)
    nayoko "All of this positivity has me so excited! I can't wait to enjoy becoming friends with all of you!"
    show grimaldi_halfbody_laughing
    hide nayoko_halfbody_happy
    with Dissolve(0.25)
    grimaldi "Yes, Grimaldi agress with Cheerleading friend!"
    show yashimata_halfbody_neutral
    hide grimaldi_halfbody_laughing
    with Dissolve(0.25)
    yashimata "Hell yeah! You said it best, brother!"
    hide yashimata_halfbody_neutral
    with Dissolve(0.25)
    hkmonologue "Seeing everyone so excited for the semester to begin is quite contagious."
    hkmonologue "Although I'm still a little bit nervous, seeing everyone smile and be merry comforts any doubts I have!"

    # PARTY ANNOUNCEMENT 
    show noburo_halfbody_happy
    with Dissolve(0.25)
    noburo "Yo, everyone! Listen up!! I got a huge announcement to make!"
    show fujiko_halfbody_bored
    hide noburo_halfbody_happy
    with Dissolve(0.25)
    fujiko "Oh man, I wonder what it could be this time!"
    show fujiko_halfbody_neutral
    hide fujiko_halfbody_bored
    with Dissolve(0.25)
    fujiko "Do you think he wants to make some more pot brownies again? That would pretty funny!"
    show azumi_halfbody_bored
    hide fujiko_halfbody_neutral
    with Dissolve(0.25)
    azumi "Fujiko!"
    show fujiko_halfbody_upset
    hide azumi_halfbody_bored
    with Dissolve(0.25)
    fujiko "Okay, I'll listen."
    show noburo_halfbody_neutral
    hide fujiko_halfbody_upset
    with Dissolve(0.25)
    noburo "Let's have a party tonight! To celebrate our newfound friends and the beginning of a new era for all of us!"
    show naganori_halfbody_bored
    hide noburo_halfbody_neutral
    with Dissolve(0.25)
    naganori "If I recall correctly, you said you wanted to host a party at the end of Orientation. Did you not?"
    show noburo_halfbody_happy
    hide naganori_halfbody_bored
    with Dissolve(0.25)
    noburo "I totally said that, but I think having a party tonight would be better for all of us!"
    show naganori_halfbody_neutral
    hide noburo_halfbody_happy
    with Dissolve(0.25)
    naganori "How so?"
    show noburo_halfbody_happy
    hide naganori_halfbody_neutral
    with Dissolve(0.25)
    noburo "Well, first of all, we're all pretty hyped right now! I even saw the vampire over there crack a smile or two!"
    noburo "We definitely need to keep that momentum going!"
    show matsuko_halfbody_neutral
    hide noburo_halfbody_happy
    with Dissolve(0.25)
    matsuko "Go on? We haven't got all day."
    show noburo_halfbody_neutral
    hide matsuko_halfbody_neutral
    with Dissolve(0.25)
    noburo "Not only will we continue to have fun and be happy, but in addition, it would be an awesome way for us to get to know each other better!"
    show azumi_halfbody_neutral
    hide noburo_halfbody_neutral
    with Dissolve(0.25)
    azumi "Like a mixer!"
    show noburo_halfbody_happy
    hide azumi_halfbody_neutral
    with Dissolve(0.25)
    noburo "Absolutely! Just like a mixer!"
    show yukako_halfbody_neutral
    hide noburo_halfbody_happy
    with Dissolve(0.25)
    yukako "I mean...we are going to be peers for the next couple of years, so...we might as well."
    show noburo_halfbody_neutral
    hide yukako_halfbody_neutral
    with Dissolve(0.25)
    noburo "Are we all in agreement then?"
    show kazuhiko_halfbody_neutral
    hide noburo_halfbody_neutral
    with Dissolve(0.25)
    hiko "Going once..."
    hiko "Going twice..."
    show vladnot_halfbody_frustrated
    hide kazuhiko_halfbody_neutral
    with Dissolve(0.25)
    vladnot "I...Mmph...Mmph...Hgph..."
    show vladnot_halfbody_upset
    hide vladnot_halfbody_frustrated
    with Dissolve(0.25)
    play sfx_channel thunder_sfx volume 1.00 noloop
    with vpunch
    vladnot "{i}*Let go...Grimaldi...*{/i}"
    show grimaldi_halfbody_unamused
    hide vladnot_halfbody_upset
    with Dissolve(0.25)
    grimaldi "Grimaldi will not let go until friends all go to mixer."
    show kazuhiko_halfbody_happy
    hide grimaldi_halfbody_unamused
    with Dissolve(0.25)
    hiko "And going thrice! It's settled then!"

    # SPLITING OFF INTO GROUPS 
    show noburo_halfbody_confused
    hide kazuhiko_halfbody_happy
    with Dissolve(0.25)
    noburo "So......what now then?"
    show nayoko_halfbody_surprised
    hide noburo_halfbody_confused
    with Dissolve(0.25)
    nayoko "We need to start setting up for the party, that's what!"
    show noburo_halfbody_neutral
    hide nayoko_halfbody_surprised
    with Dissolve(0.25)
    noburo "Oh yeah, I usually forget that part. I was always the one fixing up grub for everyone."
    show kazuhiko_halfbody_thinking
    hide noburo_halfbody_neutral
    with Dissolve(0.25)
    hiko "Well then, in order for this mixer to run as smooth as possible, let's all take a task, break up into small groups, and work on it together.
    Sound good?"
    show yashimata_halfbody_neutral
    hide kazuhiko_halfbody_thinking
    with Dissolve(0.25)
    yashimata "All right! This is the perfect event for me to bust out the cooking skills! Can I join you, Noburo?"
    show noburo_halfbody_happy
    hide yashimata_halfbody_neutral
    with Dissolve(0.25)
    noburo "Absolutely!"
    show grimaldi_halfbody_neutral
    hide noburo_halfbody_happy
    with Dissolve(0.25)
    grimaldi "Grimaldi would also like to join the cooking festivities! Can he cook food from homeland?"
    show noburo_halfbody_happy
    hide grimaldi_halfbody_neutral
    with Dissolve(0.25)
    noburo "Totally! The more the merrier, dude!"

    # HISAKO AND EIZO SHOULD GO UPSTAIRS
    show kazuhiko_halfbody_thinking
    hide noburo_halfbody_happy
    with Dissolve(0.25)
    hiko "Before we split up, I think it would be wise for both Eizo and Hisako to rest of the time being, especially Eizo." # PAN TO EIZO 
    show eizo_halfbody_upset
    hide kazuhiko_halfbody_thinking
    with Dissolve(0.25)
    eizo "... ... ... ..."
    show naoki_halfbody_frustrated
    hide eizo_halfbody_upset
    with Dissolve(0.25)
    naoki "I don't think he is going to be able to do anything, let alone stand in that state!"
    show tetsunori_halfbody_neutral
    hide naoki_halfbody_frustrated
    with Dissolve(0.25)
    tetsu "Hisako, would you be able to take Eizo back to his bedroom please?"
    hk "No problem at all, Tetsunori!"
    show tetsunori_halfbody_surprised
    hide tetsunori_halfbody_neutral
    with Dissolve(0.25)
    tetsu "Vladnot, could you accompany Hisako and help her out? And while you're at it, show her where her room is located!"
    show vladnot_halfbody_frustrated
    hide tetsunori_halfbody_surprised
    with Dissolve(0.25)
    vladnot "Of all the people in this manor, you want me to do this task. Why is that?"
    show ryosei_halfbody_frustrated
    hide vladnot_halfbody_frustrated
    with Dissolve(0.25)
    ryosei "Because we all know that you'll slink away to your room, not to help any one of us."
    ryosei "Then you'll stay there in complete darkness until Grimaldi and Nayoko barge in again and force you to attend the mixer."
    show vladnot_halfbody_frustrated
    hide ryosei_halfbody_frustrated
    with Dissolve(0.25)
    vladnot "... ..."
    show vladnot_halfbody_neutral
    hide vladnot_halfbody_frustrated
    with Dissolve(0.25)
    vladnot "Understandable then. I shall accompany Hisako and help lay the soul of the poor fast food worker to rest."
    show yashimata_halfbody_neutral
    hide vladnot_halfbody_neutral
    with Dissolve(0.25)
    yashimata "Woah, that guy really is a psychic."
    show ryosei_halfbody_happy
    hide yashimata_halfbody_neutral
    with Dissolve(0.25)
    ryosei "And you thought that I was a farce? Hah! Ryosei Kozato will always be a true psychic, outshining all others!"
    hkmonologue "Ryosei's showmanship will always be on a higher level. I'm really glad he was able to help persuade Vladnot to help me out."

    # HIKO TETSU NAOKI LEAVE 
    show kazuhiko_halfbody_neutral
    hide ryosei_halfbody_happy
    with Dissolve(0.25)
    hiko "Okay! With all that setled, let's break up and set up! Best of luck everyone!"
    show kazuhiko_halfbody_happy
    hide kazuhiko_halfbody_neutral
    with Dissolve(0.25)
    hiko "Tetsu. Naoki. You're with me!" 
    # EXIT HIKO
    play sfx_channel walking volume 0.85 noloop
    hide kazuhiko_halfbody_happy
    with Dissolve(1.00)

    show tetsunori_halfbody_neutral
    with Dissolve(0.25)
    tetsu "Sounds good to me." 
   
    # EXIT TETSU 
    play sfx_channel walking volume 0.85 noloop
    hide tetsunori_halfbody_neutral
    with Dissolve(1.00)

    show naoki_halfbody_happy
    with Dissolve(0.25)
    naoki "Okay then! See you around, Hisako!"  
    hk "See you later guys!"

    # EXIT NAOKI
    play sfx_channel walking volume 0.85 noloop
    hide naoki_halfbody_happy
    with Dissolve(1.00)

    # YASHIMATA NOBURO GRIMALDI LEAVE 
    show yashimata_halfbody_happy
    with Dissolve(0.25)
    yashimata "What are we waiting for, you two? Let's go down to the kitchen and make some bomb-ass food! Last one there is a rotten egg!" 
   
    # EXIT YASHIMATA
    play sfx_channel running volume 0.85 noloop
    hide yashimata_halfbody_happy
    with Dissolve(1.00)

    show noburo_halfbody_upset
    with Dissolve(0.25)
    noburo "Hey! No fair, Yashimata! You have, like, unlimited stamina!!" 
    
    # EXIT NOBURO 
    play sfx_channel running volume 0.85 noloop
    hide noburo_halfbody_upset
    with Dissolve(1.00)

    show grimaldi_halfbody_upset
    with Dissolve(0.25)
    grimaldi "Grimaldi hate rotten egg, so he definitely does not want to be one!" 
    
    # EXIT GRIMALDI 
    play sfx_channel running volume 0.85 noloop
    hide grimaldi_halfbody_upset
    with Dissolve(1.00)

    #RYOSEI KICHI SHINZO 
    show ryosei_halfbody_thinking
    with Dissolve(0.25)
    ryosei "I have a bad feeling those fools are going to be making quite the mess. I'm going down as well to ensure this future does not come to pass."
    show kichi_halfbody_annoyed
    hide ryosei_halfbody_thinking
    with Dissolve(0.25)
    kichi "Well, I can tell you this much that I didn't come down and help, I'd be more useless than tits on a bull."
    show shinzo_halfbody_frustrated
    hide kichi_halfbody_annoyed
    with Dissolve(0.25)
    shinzo "Why does a lass like you have to have the mouth and language of a verteran sheriff?"
    show kichi_halfbody_happy
    hide shinzo_halfbody_frustrated
    with Dissolve(0.25)
    kichi "I think it's quite fun, Mr. Cowboy. And by the looks of it, you ain't as innocent as you make yourself out to be." 
    
    # EXIT KICHI 
    play sfx_channel walking volume 0.85 noloop
    hide kichi_halfbody_happy
    with Dissolve(1.00)

    show shinzo_halfbody_upset
    with Dissolve(0.25)
    shinzo "I...Uh...Um...That's something that can't be helped!!!" 
    
    # EXIT SHINZO 
    play sfx_channel walking volume 0.85 noloop
    hide shinzo_halfbody_upset
    with Dissolve(1.00)

    show ryosei_halfbody_thinking
    with Dissolve(0.25)
    ryosei "I sense I'm making a grave mistake for my mental sanity with this one."
    hk "Do take care of yourself, Ryosei."
    show ryosei_halfbody_neutral
    hide ryosei_halfbody_thinking
    with Dissolve(0.25)
    ryosei "I shall overcome this. I see it in my future...There's nothing a few ibuprofen can't do."
    ryosei "Farewell, Ms. Lawyer." 
    
    # EXIT RYOSEI 
    play sfx_channel walking volume 0.85 noloop
    hide ryosei_halfbody_neutral
    with Dissolve(1.00)

    hkmonologue "I don't know if he'll make it out of there alive. Let's hope he does."

    # AZUMI FUJIKO CHINO 
    show fujiko_halfbody_happy
    with Dissolve(0.25)
    fujiko "Hey Azumi, are you thinking what I'm thinking {i}*smug*{/i}?"
    show azumi_halfbody_neutral
    hide fujiko_halfbody_happy
    with Dissolve(0.25)
    azumi "Going back to the music room to find our entertainment for the evening?"
    show fujiko_halfbody_happy
    hide azumi_halfbody_neutral
    with Dissolve(0.25)
    fujiko "Bingo! Let's go!"
    show azumi_halfbody_happy
    hide fujiko_halfbody_happy
    with Dissolve(0.25)
    azumi "Chino, you're coming with us!"
    show chino_halfbody_blush
    hide azumi_halfbody_happy
    with Dissolve(0.25)
    chino "O-Okay! I'll do my best to make sure I don't get in the way!"
    show fujiko_halfbody_neutral
    hide chino_halfbody_blush
    with Dissolve(0.25)
    fujiko "Chino, you've been everything {i}*but*{/i} troublesome for Azumi and me."
    show azumi_halfbody_neutral
    hide fujiko_halfbody_neutral
    with Dissolve(0.25)
    azumi "We'd never think that about you!"
    show chino_halfbody_blush
    hide azumi_halfbody_neutral
    with Dissolve(0.25)
    chino "T-Thank you. That means so much to me!" 
    
    # EXIT AZUMI FUJIKO CHINO 
    play sfx_channel double_walk_sfx volume 0.85 noloop
    hide chino_halfbody_blush
    with Dissolve(1.00)

    #NARUMI MATSUKO NAGANORI 
    show narumi_halfbody_bored
    with Dissolve(0.25)
    narumi "I believe there is no need for me to be here."
    narumi "I'm going back to the bar, and it would be greatly appreciated if no one were there to bother me."
    show naganori_halfbody_bored
    hide narumi_halfbody_bored
    with Dissolve(0.25)
    naganori "I will be going down regardless. I refuse to work in places with such din and cacophony."
    show narumi_halfbody_neutral
    hide naganori_halfbody_bored
    with Dissolve(0.25)
    narumi "As long as you don't interrupt me doing my job and don't make too much noise, I don't care."
    show matsuko_halfbody_neutral
    hide narumi_halfbody_neutral
    with Dissolve(0.25)
    matsuko "I shall tag along as wel. The more that work in silence, the better."
    
    # EXIT NARUMI MATUSKO NAGANORI 
    play sfx_channel double_walk_sfx volume 0.85 noloop
    hide matsuko_halfbody_neutral
    with Dissolve(1.00)

    # YUKAKO YUI NAYOKO 
    show yui_halfbody_happy
    with Dissolve(0.25)
    yui "Well, I guess that just leaves the us!! Oh, I'm so excited!!"
    show nayoko_halfbody_surprised
    hide yui_halfbody_happy
    with Dissolve(0.25)
    nayoko "What should we do to help out with the party?"
    show yukako_halfbody_thinking
    hide nayoko_halfbody_surprised
    with Dissolve(0.25)
    yukako "I uh..."
    show yui_halfbody_neutral
    hide yukako_halfbody_thinking
    with Dissolve(0.25)
    yui "You got a good point! I have no idea what we should do. What do you think we should do?"
    show yukako_halfbody_neutral
    hide yui_halfbody_neutral
    with Dissolve(0.25)
    yukako "I think..."
    show nayoko_halfbody_smug
    hide yukako_halfbody_neutral
    with Dissolve(0.25)
    nayoko "No fair! I asked you first, Yui!"
    $ multipleppl.name = "Yui & Nayoko" # MUTLIPLE PEOPLE NAME CHANGE 
    show nayoko_halfbody_surprised at right
    show yui_halfbody_happy at left
    hide nayoko_halfbody_smug   
    with Dissolve(0.25)
    multipleppl "Yukako, what do you think?"
    show yukako_halfbody_frustrated    
    with Dissolve(0.25)
    yukako "... ..."
    yukako "Sorry, give me a quick second..."
    show yukako_halfbody_sleepy
    hide yukako_halfbody_frustrated
    with Dissolve(0.25)
    yukako "I think we should...go down to the main area near the bar, then help clean and set up there."
    show nayoko_halfbody_smug at right
    show yui_halfbody_unamused at left  
    hide nayoko_halfbody_surprised
    hide yui_halfbody_happy
    with Dissolve(0.25)
    multipleppl "... ..."
    hkmonologue "Oh no. Some about this conversation feels very tense all of a sudden."
    show nayoko_halfbody_surprised at right
    hide nayoko_halfbody_smug
    with Dissolve(0.25)
    nayoko "... OH...MY...GOSH!!! Yukako, You are such a genius!!"
    show yui_halfbody_happy at left 
    hide yui_halfbody_unamused
    with Dissolve(0.25)
    yui "How did I not think of that! Without a clean venue, the party would essentially be over before it even started!!"
    show nayoko_halfbody_happy at right 
    hide nayoko_halfbody_surprised
    with Dissolve(0.25)
    nayoko "Thank you so much for your help, Yukako! You're so awesome!"
    show yukako_halfbody_thinking 
    hide yukako_halfbody_sleepy   
    with Dissolve(0.25)
    yukako "Um...you're welcome. I didn't do much."
    show nayoko_halfbody_neutral at right 
    hide nayoko_halfbody_happy
    with Dissolve(0.25)
    nayoko "Of course you did! Now c'mon!"
    show yukako_halfbody_upset 
    hide yukako_halfbody_thinking   
    with Dissolve(0.25)
    with hpunch
    yukako "Woah!!"
    show yui_halfbody_genius at left
    hide yui_halfbody_happy
    with Dissolve(0.25)
    yui "Let's go down and clean, you two! There's no time to waste!!"
    show yukako_halfbody_upset 
    with hpunch
    yukako "Could you not drag me so much, please??" 
    
    # EXIT YUI YUKAKO NAYOKO
    play sfx_channel double_walk_sfx volume 0.85 noloop
    hide yukako_halfbody_upset
    hide yui_halfbody_genius
    hide nayoko_halfbody_neutral
    with Dissolve(1.00)

    # BACK HK MONO
    hkmonologue "Well, I'm happy that they're having fun with this!"
    hkmonologue "Now then, time to bring the poor kid to his room. And by the looks of it, he definitely needs more than just a few hours of rest!"

    # VLAD AND HISAKO 
    show vladnot_halfbody_neutral
    with Dissolve(0.25)
    vladnot "Since you are unaware of the location of our dormitories..."
    show vladnot_halfbody_calm
    hide vladnot_halfbody_neutral
    with Dissolve(0.25)
    vladnot "I shall be your guide, your Charon, if you must, through the vast hallways of this manor."
    hkmonologue "He really is going a little far with the vampire persona..."
    hk "Thank you for your help! I truly appreciate it!"
    show vladnot_halfbody_neutral
    hide vladnot_halfbody_calm
    with Dissolve(0.25)
    vladnot "No matter. Allow me to help you with the one who is almost a corpse. I shall get one side and you the other?"
    hk "Sounds good to me! Hup!"
    vladnot "Follow me, Practitioner of the Law."
    hk "Practitioner?"
    show vladnot_halfbody_frustrated
    hide vladnot_halfbody_neutral
    with Dissolve(0.25)
    vladnot "Do you not practice the law as a lawyer?"
    hk "...Yes, I do."    
    vladnot "Then you are a practitioner as such."
    show vladnot_halfbody_neutral
    hide vladnot_halfbody_frustrated
    with Dissolve(0.25)
    vladnot "Now follow me to the living chambers."
    hkmonologue "Oh, boy..."

    # END SCENE 2-1 [FINISHED ON 6/22/24 @ 9:16 PM]
    # PLACE WALKING SFX HERE 
    play sfx_channel walking volume 0.85 noloop
    # TRANSITION OVER TO SCENE 
    hide vladnot_halfbody_neutral
    with Dissolve(0.25)
    stop music fadeout 2.0
    hide manor_atrium
    with fade
    show transition
    with Dissolve(2.0)
    $ renpy.pause(1.75, hard=True)

# SCENE 2-2 [WHITE WYVERN MANOR - EIZO'S ROOM] --> HISAKO AND VLADNOT HAVE FINALLY BROUGHT EIZO: THE ULTIMATE FAST FOOD WORKER BACK TO HIS ROOM.
# UPON UNLOCKING AND ENTERING HIS ROOM, THEY ARE COMPLETELY FLABBERGASTED BY WHAT THEY SEE INSIDE. AFTER LEAVING EIZO, VLAD WILL DIRECT HISAKO TO WHERE 
# HER ROOM IS LOCATED [STARTED 6/26/24 @ 9:08 PM]
label scene2_2: 
    # SHOW NEW BACKGROUND OF EIZO ROOM HERE 
    show eizo_room
    hide transition
    with Dissolve(1.5)   
    $ renpy.pause(1.00, hard=True)

    hk "... ... ..."
    hk "... ... ..."
    show vladnot_halfbody_upset
    with Dissolve(0.25)
    vladnot "... ... ..."
    vladnot "... ... ..."
    hk "Vlad, are you see what I'm seeing?"
    vladnot "I feel as if this is all a mirage, but it's right there in front of me!"
    hk "This can't be real! It just can't be!"
    show vladnot_halfbody_calm
    hide vladnot_halfbody_upset
    with Dissolve(0.25)
    vladnot "Oh, but it is, my dear!"
    hk "Eizo's room looks like the inside of a Fatty Fingers..."
    show vladnot_halfbody_frustrated
    hide vladnot_halfbody_calm
    with Dissolve(0.25)
    vladnot "And it's not all merely for decoration! Look over there near the change machine!"
    hk "A full-on grill? And a fryer?"
    hk "The poor boy can't even escape work in his sleep!"
    show vladnot_halfbody_neutral
    hide vladnot_halfbody_frustrated
    with Dissolve(0.25)
    vladnot "To eat, work, and sleep fast food. Truly a modern-day Sisyphus!"
    hk "If my room were modeled after a courtroom, I'd honestly go insane after a week or two!"
    hk "There needs to be a balance between work and home life, and one should never overshadow the other!"
    show vladnot_halfbody_frustrated
    hide vladnot_halfbody_neutral
    with Dissolve(0.25)
    vladnot "... ..."
    vladnot "... ..."
    show vladnot_halfbody_happy
    hide vladnot_halfbody_frustrated
    with Dissolve(0.25)
    play sfx_channel thunder_sfx volume 1.00 noloop
    with vpunch
    play music perdue2 volume 0.80 loop
    vladnot "At least vampires don't have to deal with such trivial matters!"
    hkmonologue "There he goes again. I'm no psychoanalyst, but I'm pretty sure he just broke character for a moment."
    show vladnot_halfbody_neutral
    hide vladnot_halfbody_happy
    with Dissolve(0.25)
    vladnot "What do you think, hmm?"
    hk "!!!"
    hk "Huh?? I'm so sorry. I got lost in my own thoughts. What did you ask me?"
    vladnot "I asked if you think he enjoys what he does."
    hk "I'd like to think that he enjoys being the {color=#efcc00}{b}Ultimate Fast Food Worker{/b}{/color}..."
    hk "However, it is very apparent that he has been overworking himself, completely disregarding his health and purely focusing on work."
    show vladnot_halfbody_frustrated
    hide vladnot_halfbody_neutral
    with Dissolve(0.25)
    vladnot "Do you think he'll be okay here at Hope's Peak?"
    hk "I don't know what set of circumstances led him to his destructive work habits in the first place..."
    hk "But I truly believe that he'll be able to recuperate and learn how to balance and maintain his health."
    hk "Once he does that, he'll also be able to meet the demands that come from being an {color=#efcc00}{b}Ultimate{/b}{/color} in the fast food sector!"
    hk "I mean isn't that why we're all here in the first place?"
    show vladnot_halfbody_neutral
    hide vladnot_halfbody_frustrated
    with Dissolve(0.25)
    vladnot "In what way do you mean?"
    hk "All of us {color=#efcc00}{b}Ultimates{/b}{/color}: 
    we have come to this school because there are particular flaws within our lives that need attending."
    hk "We all may technically be the best in our field, but it doesn't mean we are perfect."
    show vladnot_halfbody_calm
    hide vladnot_halfbody_neutral
    with Dissolve(0.25)
    vladnot "Hmmm....You do make a compelling argument."
    hk "We would all like to think that our {color=#efcc00}{b}Ultimate Abilities{/b}{/color} are what sets us apart from the others in our fields."
    hk "If we had no problems, flaws, or any imperfections, we wouldn't need to be here."
    show vladnot_halfbody_frustrated
    hide vladnot_halfbody_calm
    with Dissolve(0.25)
    vladnot "How do our {color=#efcc00}{b}Ultimate Abilities{/b}{/color} not put us at the top immediately? That's the whole point of an {color=#efcc00}{b}Ultimate{/b}{/color}."
    hk "Sure, being an Ultimate distinguishes you from the crowd, but it also depends on your personality, actions, and character as a whole."
    hk "You can be an Ultimate, but have a personality that is so repulsive that it negatively impacts you."
    show vladnot_halfbody_neutral
    hide vladnot_halfbody_frustrated
    with Dissolve(0.25)
    vladnot "I'm starting to see your point of view now."
    hk "Everyone here in this manor are all really genuine people! Sure, we've all come from different backgrounds and professions..."
    hk "But what truly matters is that we empathize and listen to each other, and help encourage one another to be the person they can be!"
    show vladnot_halfbody_calm
    hide vladnot_halfbody_neutral
    with Dissolve(0.25)
    vladnot "Empathize...hmmm. I understand."
    show vladnot_halfbody_neutral
    hide vladnot_halfbody_calm
    with Dissolve(0.25)
    vladnot "That was kind of reassuring, Madam Hisako. I do hope to become good friends and empathize with you."
    hkmonologue "I'm really happy that I was able to get pass the showmanship, and have a genuine heart-to-heart moment with him!"
    hk "Same here, Vladnot! I also wanted to thank you for helping me with Eizo in bringing him back to his room!"
    show vladnot_halfbody_happy
    hide vladnot_halfbody_neutral
    with Dissolve(0.25)
    vladnot "'Tis no problem from an immortal!"
    hkmonologue "Well, at least he is a good person all around!"
    show vladnot_halfbody_neutral
    hide vladnot_halfbody_happy
    with Dissolve(0.25)
    vladnot "One more thing before you leave: Your chambers are the last one down and to the left."
    hk "Thank you! Well, I'm gonna go check it out then!"
    vladnot "You go and do that. I will return to thine place of living and allow the darkness to develop and comfort me."
    vladnot "If you need my attention, do please knock ahead of time."
    hk "Will do! I'll see you at the party!"
    show vladnot_halfbody_calm
    hide vladnot_halfbody_neutral
    with Dissolve(0.25)
    vladnot "See you around." 
    
    # EXIT VLADNOT 
    play sfx_channel walking volume 0.35 noloop
    hide vladnot_halfbody_calm
    with Dissolve(1.00)

    hkmonologue "Okay! Time to go to my room and look around some. I just hope that it isn't a courtroom."
    hkmonologue "Knock on wood, fingers crossed, whatever I need for good luck!"

    # END SCENE 2-2       
    # TRANSITION OVER TO SCENE [6/26/2024 @ 9:36 PM & 10:03 PM]    
    stop music fadeout 2.0
    hide eizo_room
    with fade
    show transition
    with Dissolve(2.0)
    $ renpy.pause(1.75, hard=True)

# SCENE 2-3 [WHITE WYVERN MANOR - HISAKO'S ROOM] --> AFTER BRINGING EIZO BAK TO HIS ROOM, HISAKO DECIDES TO GO AND CHECK OUT HER ROOM
# TO HER AMAZEMENT, HER ROOM IS THEMED ACCORDING TO HER PARTICULAR TASTE IN STLE AS WELL AS HER TO HER ULTIMATE ABILITY
# SHE WILL DELVE INTO MORE DETAIL ABOUT HER ROOM, REST FOR A QUICK MINUTE, THEN HEAD BACK DOWNSTAIRS TO HELP SET UP FOR THE PARTY (MULTICHOICE)
label scene2_3:   
    # SET CHAPTER NUMBER AND SCENE ROOM FOR INVESTIGATION HERE 
    $ sceneRoom = "prologue_hisakoRoom"
    $ magGlassNum = 4

    # BOOLEAN VALUE     
    define isMagGlassOneSeen = "false"
    define isMagGlassTwoSeen = "false"
    define isMagGlassThreeSeen = "false"
    define isMagGlassFourSeen = "false"

    # SHOW HISAKO ROOM      
    show hisako_room
    hide transition
    with Dissolve(1.5)   
    $ renpy.pause(1.00, hard=True)

    # PLAY MUSIC HERE 
    play music calm_seas volume 0.75 loop

    # MONOLOGUE HERE 
    hkmonologue "This is absolutely amazing! It looks completely different from Eizo's that's for sure!"
    hkmonologue "And it's exactly how I would've modeled my dream apartment!"
    hkmonologue "They weren't kidding when they said they knew everything about us."
    hkmonologue "Hmmmm, I wonder what else they know about my dream designs...."

    # TEST OUTLINE FOR EXPLORATION WITH UI EXPLORATION 
    sfxText "Hello! Since you are new to the game, allow me to introduce some of the core mechanics of the game."
    sfxText "When in a room, you can do one of three things:"
    sfxText "#1. You can {color=#efcc00}{b}Investigate{/b}{/color} a room and search for very important clues."
    sfxText "#2. If another student is in the room, you can {color=#efcc00}{b}Talk{/b}{/color} to them and get to know them better."
    sfxText "#3. You can decide to {color=#efcc00}{b}Move{/b}{/color} to another room or section around campus."
    sfxText "Interested in doing it yourself? Click on the {color=#efcc00}{b}\"Investigate\"{/b}{/color} box to look around your new room!"
    
    # INVESTIGATION SCREEN
    call screen investigation(0,0)
       
    # POST INVESTIGATION SCENE [FINISHED 7/16/24 @ 7:39 PM]
    label scene2_3_Post_Investigation:  
        # RESTART DIALOGUE    
        hkmonologue "Oh man...."  
        hkmonologue "I'm so glad that I was given this opportunity and privilege of a second chance to prove myself as the 
        {color=#efcc00}{b}Ultimate Lawyer{/b}{/color}!"
        hkmonologue "I promise not only to the school and the government, but also to myself that I will put 110%% into everything I do here!"
        hkmonologue "Oh, man...this place is so amazing!" 
        hkmonologue "I know these next four years will fly by, but right now, I just want to enjoy one day at a time! And tonight, we're gonna have a party!"
        hkmonologue "We're all going to get to know each other, eat good food, and have drinks prepared by the greatest bartender ever!"
        hkmonologue "And most importantly, we're all going to have so much fun before classes start!"
        hkmonologue "I'm so excited, I can hardly contain myself!"
        hkmonologue "...Oh, yeah! I know I was told to rest, but I honestly feel better already!"
        hkmonologue "I appreciate everyone's concern, but I would feel terrible if I didn't help at least a little bit with the party set-up."
        hkmonologue "The question now is: where do I go and help out?"
        hkmonologue "Hmmmmm...Decisions...Decisions"

        # MULTICHOICE BRANCH-OFF
        menu:
            "Lounge":
                hkmonologue "It's decided then! I'll head on down to the lounge and help out the Okuda brothers!"
                # END SCENE 2-3       
                # TRANSITION OVER TO SCENE [7/17/2024 @ 8:43 PM]    
                stop music fadeout 2.0
                hide hisako_room
                with fade
                show transition
                with Dissolve(2.0)
                $ renpy.pause(1.75, hard=True)
                jump scene2_4
            "Kitchen":
                hkmonologue "I think I'll head over to the kitchen to check up on Noburo and the gang."
                hkmonologue "I'm just hoping they didn't make too much of a mess!"
                # END SCENE 2-3       
                # TRANSITION OVER TO SCENE [7/17/2024 @ 9:25 PM]    
                stop music fadeout 2.0
                hide hisako_room
                with fade
                show transition
                with Dissolve(2.0)
                $ renpy.pause(1.75, hard=True)
                jump scene2_5
            "Dining Room":
                hkmonologue "Let's go to the dining room to see how Shinzo, Kichi, and Ryosei are holding up."
                hkmonologue "I'm just hoping that Noburo and the others haven't caused mayhem in the kitchen!"
                # END SCENE 2-3       
                # TRANSITION OVER TO SCENE [7/17/2024 @ 9:25 PM]    
                stop music fadeout 2.0
                hide hisako_room
                with fade
                show transition
                with Dissolve(2.0)
                $ renpy.pause(1.75, hard=True)
                jump scene2_6
            "Bar":
                hkmonologue "I know I'm going to regret this very soon..."
                hkmonologue "But I guess I'll go down to the bar and see if Narumi and the others need some extra hands."
                # END SCENE 2-3       
                # TRANSITION OVER TO SCENE [7/17/2024 @ 9:25 PM]    
                stop music fadeout 2.0
                hide hisako_room
                with fade
                show transition
                with Dissolve(2.0)
                $ renpy.pause(1.75, hard=True)
                jump scene2_7
            "Recreation Room":
                hkmonologue "Let's go check and see what Yukako, Yui, and Nayoko are up to in the rec room!"
                # END SCENE 2-3       
                # TRANSITION OVER TO SCENE [7/17/2024 @ 9:25 PM]    
                stop music fadeout 2.0
                hide hisako_room
                with fade
                show transition
                with Dissolve(2.0)
                $ renpy.pause(1.75, hard=True)
                jump scene2_8
            "Music Room":
                hkmonologue "I think I'll go see if Azumi and Fujiko need any help in the music room!"
                # END SCENE 2-3       
                # TRANSITION OVER TO SCENE [7/17/2024 @ 9:25 PM]    
                stop music fadeout 2.0
                hide hisako_room
                with fade
                show transition
                with Dissolve(2.0)
                $ renpy.pause(1.75, hard=True)
                jump scene2_9

        # END SCENE 3

# SCENE 4 [WHITE WYVERN MANOR - LOUNGE (MULTICHOICE OPTION 1)] --> HISAKO DECIDES TO HELP OUT THE AKUDA BROTHERS
# IN THE LOUNGE WITH SOME HEAVY LIFTING OF THEIR DJ EQUIPMENT. [STARTED 7/17/24 @ 8:41 PM]
label scene2_4:  
    # SHOW LOUNGE 
    show lounge
    hide transition
    with Dissolve(1.5)   
    $ renpy.pause(1.00, hard=True)

    # PLAY MUSIC HERE 
    play music funkman volume 0.70 loop
    # BROTHERS ARE TALKING   
    show kazuhiko_halfbody_neutral
    with Dissolve(0.25)       
    hiko "Alright, there's one more box!"
    hiko "Naoki, how are you doing? Is everything good?"
    show naoki_halfbody_neutral
    hide kazuhiko_halfbody_neutral
    with Dissolve(0.25)
    naoki "I'm all good! Just brought over the turntables and mixer from my room. I also have most of my records with me as well!"
    show kazuhiko_halfbody_happy
    hide naoki_halfbody_neutral
    with Dissolve(0.25)
    hiko "That's excellent! And how about you, Tetsu?"
    show tetsunori_halfbody_neutral
    hide kazuhiko_halfbody_happy
    with Dissolve(0.25)
    tetsu "Everything's good on my end as well. I was able to bring down some speakers, lights, and other loose cables from Naoki's room!"
    show tetsunori_halfbody_surprised
    hide tetsunori_halfbody_neutral
    with Dissolve(0.25)
    tetsu "I'm pretty sure we have everything we need."
    show kazuhiko_halfbody_neutral
    hide tetsunori_halfbody_surprised
    with Dissolve(0.25)
    hiko "Nice! Nice! I see that we have everything accounted for!"
    show kazuhiko_halfbody_thinking
    hide kazuhiko_halfbody_neutral
    with Dissolve(0.25)
    hiko "However, there is one small issue..."
    show naoki_halfbody_frustrated
    hide kazuhiko_halfbody_thinking
    with Dissolve(0.25)
    naoki "And what's that, Hiko?"
    show kazuhiko_halfbody_upset
    hide naoki_halfbody_frustrated
    with Dissolve(0.25)
    hiko "We have way too many boxes to bring to the rec room, and we still need time to set up down there as well."
    show naoki_halfbody_upset
    hide kazuhiko_halfbody_upset
    with Dissolve(0.25)
    naoki "I didn't even notice!"
    show tetsunori_halfbody_upset
    hide naoki_halfbody_upset
    with Dissolve(0.25)
    tetsu "I hate to admit it, but I think we got a {i}*little*{/i} too excited to be the entertainment for this party."
    show kazuhiko_halfbody_upset
    hide tetsunori_halfbody_upset
    with Dissolve(0.25)
    hiko "..."
    show naoki_halfbody_frustrated
    hide kazuhiko_halfbody_upset
    with Dissolve(0.25)
    naoki "Is something the matter, Hiko?"
    show kazuhiko_halfbody_happy
    hide naoki_halfbody_frustrated 
    with Dissolve(0.25)   
    # ADD EXCLAMATION SFX FOR HIKO
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff")     
    hiko "!!!"
    hiko "No, no, I'm totally fine!"
    show kazuhiko_halfbody_thinking
    hide kazuhiko_halfbody_happy
    with Dissolve(0.25)
    hiko "However, I do think you are right, Tetsu."
    show kazuhiko_halfbody_happy
    hide kazuhiko_halfbody_thinking
    with Dissolve(0.25)
    hiko "We may have over prepared for this event!"
    show kazuhiko_halfbody_blush
    hide kazuhiko_halfbody_happy
    with Dissolve(0.25)
    hiko "I guess I'm so used to performing in large venues, I forgot what it's like to prep for smaller events!"
    show naoki_halfbody_neutral
    hide kazuhiko_halfbody_blush
    with Dissolve(0.25)
    naoki "It's okay, Hiko! I had the same problem!"
    show naoki_halfbody_happy
    hide naoki_halfbody_neutral
    with Dissolve(0.25)
    naoki "The last time we were at a small venue was when I was starting high school!"

    # HISAKO ENTERS
    # ADD EXCLAMATION SFX FOR TETSU
    show tetsunori_halfbody_surprised
    hide naoki_halfbody_happy
    with Dissolve(0.25)
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff")    
    tetsu "Wait a minute, is that Hisako?"
    show kazuhiko_halfbody_upset
    hide tetsunori_halfbody_surprised
    with Dissolve(0.25)
    hiko "It shouldn't be. I thought we said she should go back to her toom and rest."
    show tetsunori_halfbody_unamused
    hide kazuhiko_halfbody_upset
    with Dissolve(0.25)
    tetsu "Whie I agree with you on that, I'm pretty sure that is Hisako!"
    show kazuhiko_halfbody_thinking
    hide tetsunori_halfbody_unamused
    with Dissolve(0.25)
    hiko "Are you sure, Tetsu?"
    hide kazuhiko_halfbody_thinking
    with Dissolve(0.25)

    # MULTI-SPLIT OF BROTHERS HERE 
    hk "Hey guys, what's up?"
    $ multipleppl.name = "Okuda Brothers"

    show kazuhiko_halfbody_upset at center
    with Dissolve(0.25)
    show tetsunori_halfbody_upset at right 
    with Dissolve(0.25)
    show naoki_halfbody_upset at left
    with Dissolve(0.25)    
    multipleppl "Hisako!"
    hk "How are you all doing?"
    show tetsunori_halfbody_surprised at right 
    hide tetsunori_halfbody_upset
    with Dissolve(0.25)
    tetsu "That's the same question we should be asking you!"
    show kazuhiko_halfbody_thinking at center
    hide kazuhiko_halfbody_upset
    with Dissolve(0.25)
    hiko "How are you feeling? You should be resting in your room!"
    hk "I'm feeling 1000%% better than I did earlier!"
    show naoki_halfbody_happy at left 
    hide naoki_halfbody_upset
    with Dissolve(0.25)
    naoki "That's wonderful to hear!"
    hk "So, I decided to come down here and see if you needed any help!"
    show kazuhiko_halfbody_upset at center 
    hide kazuhiko_halfbody_thinking
    with Dissolve(0.25)
    hiko "Are you sure about that? I honestly think that's a bad idea."
    hk "Why is that? I feel fine!"
    show kazuhiko_halfbody_neutral at center 
    hide kazuhiko_halfbody_upset 
    with Dissolve(0.25)
    hiko "I know that you're feeling better than you did earlier, which I am really happy to hear, by the way."
    show kazuhiko_halfbody_thinking at center 
    hide kazuhiko_halfbody_neutral
    with Dissolve(0.25)
    hiko "But you shouldn't exert yourself so quickly and risk feeling even worse than before!"
    show naoki_halfbody_neutral at left
    hide naoki_halfbody_happy
    with Dissolve(0.25)
    naoki "We want you to enjoy yourself at the party, not feel crappy and miserable!"
    show tetsunori_halfbody_neutral at right 
    hide tetsunori_halfbody_surprised
    with Dissolve(0.25)
    tetsu "We still think that it would be best if you went back to your room and relaxed until the party starts."

    # ADD EXCLAMATION SFX FOR HISAKO
    play sfx_channel exclamation volume 1.50 noloop 
    with Fade(0.1, 0.0, 0.3, color="#fff")
    show kazuhiko_halfbody_upset at center
    hide kazuhiko_halfbody_thinking
    show tetsunori_halfbody_upset at right 
    hide tetsunori_halfbody_neutral
    show naoki_halfbody_upset at left
    hide naoki_halfbody_neutral

    hk "Kazuhiko! Tetsunori! Naoki!"
    hk "I really appreciate the concern for my health and safety, but I promise that I feel good enough to help you set up for the party!"
    hk "Besides, if I went back to my room, I would be very restless and feel very guilty."
    show tetsunori_halfbody_surprised at right 
    hide tetsunori_halfbody_upset
    with Dissolve(0.25)
    tetsu "Guilty? Why would you feel guilty?"
    hk "Because everyone else is working very hard to prepare for the party, knowing full well that I could help out in some way that isn't just resting."
    show kazuhiko_halfbody_blush at center 
    hide kazuhiko_halfbody_upset
    with Dissolve(0.25)
    hiko "Dang it. You beat me to it."
    hk "With that in mind, is it cool if I help you out?"
    show kazuhiko_halfbody_thinking at center 
    hide kazuhiko_halfbody_blush
    with Dissolve(0.25)
    hiko "Hmmm... I still have some very strong reservations about this."
    show naoki_halfbody_neutral at left 
    hide naoki_halfbody_upset
    with Dissolve(0.25)
    naoki "If Hisako says she's does feel better, I say it's good in my book!"
    show tetsunori_halfbody_unamused at right 
    hide tetsunori_halfbody_surprised
    with Dissolve(0.25)
    tetsu "I agree. And if we're being completely honest here, we can use all the help we can get right now."
    hiko "Hmmmm...okay."    
    hiko "You can help us, but you have to promise me that the minute you start feeling unwell, you will tell us and take it easy! Promise?"
    hk "I promise!"
    show kazuhiko_halfbody_neutral at center 
    hide kazuhiko_halfbody_thinking
    with Dissolve(0.25)
    hiko "Alright then. With that, I feel better about having you help us!"
    hiko "Now then...We haven't a moment to waste!"
    show kazuhiko_halfbody_thinking at center 
    hide kazuhiko_halfbody_neutral
    with Dissolve(0.25)
    hiko "Listen up real quick! We have about an hour-and-a-half to get all of these boxes and equipment down to the basement!"
    hiko "We also need to keep in mind that we need to set up shop, before the first guest arrive! Let's get to it, shall we?"
    hk "Understood!"
    show kazuhiko_halfbody_neutral at center 
    hide kazuhiko_halfbody_thinking
    with Dissolve(0.25)
    hiko "Naoki: continue carrying your turntables and mixer downstairs, and then start setting up!"
    hiko "Your job is the most integral part to this whole operation! I'm counting on you!"
    show naoki_halfbody_happy at left 
    hide naoki_halfbody_neutral
    with Dissolve(0.25)
    naoki "On it, bro!"
    
    # NAOKI LEAVE 
    play sfx_channel walking volume 0.85 noloop
    hide naoki_halfbody_happy 
    with Dissolve(0.65)

    
    hiko "Tetsu: help me carry these bigger boxes along with the power supplies! We can't have the music bumpin' without these!"
    show tetsunori_halfbody_surprised at right 
    hide tetsunori_halfbody_unamused
    with Dissolve(0.25)
    tetsu "Right!"

    # TETSU LEAVE 
    play sfx_channel walking volume 0.85 noloop
    hide tetsunori_halfbody_surprised
    with Dissolve(0.65)

    show kazuhiko_halfbody_thinking at center 
    hide kazuhiko_halfbody_neutral
    with Dissolve(0.25)
    hiko "And Hisako: why don't you help Naoki out by carrying down his speakers and records crate."
    show kazuhiko_halfbody_neutral at center 
    hide kazuhiko_halfbody_thinking
    with Dissolve(0.25)
    hiko "Can't have a lively party without the speakers and the music!"
    hk "Absolutely! Right on it, Kazuhiko!"
    show kazuhiko_halfbody_thinking at center 
    hide kazuhiko_halfbody_neutral
    with Dissolve(0.25)
    hiko "And more thing, Hisako..."
    show kazuhiko_halfbody_blush
    hide kazuhiko_halfbody_thinking
    with Dissolve(0.25)
    hiko "Thank you once again for helping us out."
    hk "It's no problem at all!"
    hk "If it allows you three to set up what you need to faster, while avoiding reckless decisions, then I'm happy to help!"
    hk "Now then, on we go!"

    # FADE TO BLACK HERE AND THEN REAPPEAR AT THE BASEMENT!
    # PLACE WALKING SFX HERE 
    play sfx_channel walking volume 0.85 noloop
    # TRANSITION OVER TO SCENE 
    hide kazuhiko_halfbody_blush
    with Dissolve(0.25)    
    hide lounge
    with fade
    show transition
    with Dissolve(2.0)
    $ renpy.pause(1.75, hard=True)

    # REAPPEAR HERE 

    hk "And that should be the rest of the records!"
    naoki "Awesome!! Thank you, Hisako!!"
    tetsu "And with that, we've managed to finish moving everything down from the lounge!"
    tetsu "In addition, Naoki is almost done setting up his booth, and with 15 minutes to spare too!" 
    hiko "Thanks for the update, Tetsu!"
    hiko "Now then, Hisako, on behalf of the three of us, I would like to thank you once again for your help!"
    hiko "Without you, we would've never been able to set up on time!"
    hk "It's no problem at all!"
    hiko "I also want to apologize for being very insistant and pushy earlier regarding your bedrest."
    hiko "Knowing firsthand what happened earlier, we just wanted to make sure that those brownies were out of your system before jumping into hard labor."
    hk "It's okay! I really appreciate your apology!"
    hk "I completely understand that you three care about me, and that's what friends do for one another!"
    hiko "Hisako..."
    hk "Again, I'm happy I was able to help, but I'm also glad I was able to have fun helping my friends too!"
    hiko "That really means a lot! Thank you so much...for everything!"
    hiko "Now, I'd recommend you go upstairs and get ready for the party!"
    hk "You know, I think I'll take you up on your recommendation!"
    hiko "Hahaha! Your humor is impeccable!"
    hiko "Take care, Hisako!"
    hk "I'll see you all very soon!"
    tetsu "See ya!"
    naoki "Bye, Hisako!"
    hk "Bye Bye!"

    # END SCENE 2-4
    jump scene2_10

# SCENE 5 [WHITE WYVERN MANOR - KITCHEN (MULTICHOICE OPTION 2)] --> HISAKO DECIDES TO LEND A HAND TO YASHIMATA, 
# NOBURO, AND GRIMALDI IN THE KITCHEN. WHAT SHE DOESN'T EXPECT FROM THE BROS WILL HER BLOW HER MIND!
label scene2_5:  
    # HISAKO MONOLOGUING 
    hkmonologue "I honestly have no idea what to expect! I know they all mean well..."
    hkmonologue "But with them being as chaotic and accident-prone as they are, I'm just praying that the kitchen is still in one piece."
    hkmonologue "But what if they spilled something already?"
    hkmonologue "What if they started a fire by accident and are trying to put it out?"
    hkmonologue "What happens if the whole mansion burns down!?!?"

    # HISAKO ENTERS THE KITCHEN
    hkmonologue "What if...huh??"
    hkmonologue "The kitchen...it's spotless!"
    hkmonologue "Not even a single crumb anywhere on the floor!"
    hkmonologue "And the guys, they're absolutely silent, completely engrossed in their cooking!"
    hkmonologue "How is this even possible? I've never heard them be so quiet before!"
    hkmonologue "I don't even know if they even need any help at this point, but I'm still going to check just in case."

    # DUDES IN THE KITCHEN
    yashimata "Hey, Noburo! How's the punch coming along?"
    noburo "It's going pretty well! Just putting the finishing touches!"
    noburo "How about you, Broseph? How goes the cooking?"
    yashimata "Everything is going perfectly as planeed! Just reducing the heat to a simmer for a few minutes and it should be all good!!"
    yashimata "And don't think I forgot about you, Grimaldi! How you doing over there, big guy?"
    grimaldi "Grimaldi be having wonderful time! I too am almost done with dish from homeland!"
    grimaldi "All that need to be finished is brief pan-fry with seasoning and spices!"
    yashimata "Awesome!! And we're also earlier than expected!!"
    noburo "Hell yeah!!"

    # HISAKO APPEARS
    sfxText "{i}*knock knock knock*{/i}"
    hk "Hey guys!"
    yashimata "Hisako!"
    grimaldi "Hello, my friend!"
    noburo "Glad to see you up and about!"
    hk "How is everything going in here?"
    noburo "Everything is perfect! All of us are just about finished with our dishes."
    noburo "All we have left is a final taste test and then we're gucci!"
    yashimata "Noburo, I have a pretty radical idea!"
    noburo "What's that, my guy?"
    yashimata "Instead of us tasting our own dishes, why don't we have Hisako taste them for us!"
    hk "are you sure? I'm not exactly known for my exquisite palate."
    yashimata "Exactly! With you tasting our dishes, we'll have an unbiased result about how good they taste!"
    noburo "I think that's an excellent idea, dude! What about you, Grimaldi?"
    grimaldi "Grimaldi believes that is a lovely idea!"
    hk "I don't know. What happens if I mess up a dish because I don't like it?"
    yashimata "Nonsense! I have a very strong feeling that you are the perfect person for this!"
    yashimata "Noburo. Grimaldi. Do you have that same feeling I do?"
    noburo "I totally agree with you, bro! Hisako is definitely the one!"
    grimaldi "Grimaldi is also in agreement! Let us prepare food for Hisako!"
    yashimata "It's settled then!"
    yashimata "Now before the tasting starts, are you all okay with Hisako trying my dish first?"
    noburo "By all means!"
    grimaldi "Let Hisako save Grimaldi's dish for last!"       

    # HISAKO TRIES YASHIMATA'S DISH FIRST
    yashimata "Awesome!! Come over here to my station, Hisako!"
    hk "O-Okay."
    yashimata "Alright! Let me plate this, pour this, and BOOM! My world-famous beans and rice!"
    hk "Oh wow! This looks amazing!"
    yashimata "I can't wait to hear your thoughts!"
    sfxText "{i}*munch munch chew chew*{/i}"
    yashimata "Soooooooo??"
    hk "This is very delicious, Yashimata! I can assure you that everyone will love your dish!"
    yashimata "Thank you very much, Hisako! That means a lot."
    hk "I do have just one question."
    yashimata "Hmm?"
    hk "Why did you choose rice and beans, specifically? There's nothing wrong with your choice. I'm just a little curious!"
    yashimata "Well...this is the only thing I know how to cook."
    yashimata "I know that it's just rice and beans, but my mom taught me how to make it, and it's really good too!"
    hk "Awww! That's very sweet! I'm glad that you were able to make us a dish that means so much to you!"
    yashimata "It's no problem! I'm just happy I can do something for all of you!"
    yashimata "Thank you once again or tasting it! Glad to hear you loved it!"
    hk "You're welcome, and I truly did love it!"

    # NOBURO'S PUNCH 
    nobruo "Okay, my turn! Come over here, Hisako, and witness the true power of a punch master!"
    hk "Haha! Okay, let's see how this punch...looks..."
    noburo "What's the matter, Hisako?"
    hk "I'm just wondering why the punch is pitch black?"
    noburo "It's supposed to be that color!"
    hk "But it's bubbling and smoking???"
    noburo "That's the dry ice!"
    hk "What's the flavor???"
    noburo "Well, I can't really pinpoint a particular flavor. However, I do have a wicked name for it!"
    hk "And what is it?"
    noburo "I call it: AMBROSIA!!!!"
    hk "Ambrosia? Like the drink of the gods?"
    noburo "EXACTLY!!!"
    hkmonologue "This drink looks like something that could kill a god."
    hkmonologue "I really hope this is closer to the Ambrosia of life and not what I see before me..."
    hk "How does one go about making Ambrosia?"
    noburo "It's pretty simple!"
    noburo "You know when you were in the bathroom as a kid, and you would just mix every lotion, shampoo, and conditioner into a mystical potion?"
    hk "Um...Yes...?"
    noburo "That's pretty much how I make all of my drink for parties!"
    hk "And how are the end results?"
    noburo "At first it used to be very trial-and-error-y, but I as I perfected drink-making, my drinks are pretty much bombin' most of the time!"
    hk "Most of the time?"
    noburo "Yes, and this is one of those times! So, go on: try it!"
    hk "...Uh...Um...Alright."
    noburo "Radical!"
    hkmonologue "Here it goes, I hope I don't die from this..."
    noburo "Drink! Drink! Drink! Drink!"
    sfxText "{i}*sip sip sip*{/i}"
    hk "Woah!"
    noburo "Uh Huh! Told ya!"
    hk "That's crazy! One minute it tastes like a sangria..."
    hk "Then the next moment it tastes like fruit punch, right before going over to a Malibu sunset!!"
    noburo "That's to be expected from a potions expert as one like myself."
    hk "That's amazing, Noburo! I'm sorry I doubted you!"
    noburo "Nah, it's all good! Even I was a little anxious when it started to look like primordial sludge!"
    hk "Wait! I thought you said it was supposed to be that color!"
    noburo "I mean, it was supposed to be more of a rich red, but I'm glad it all worked out!"
    hk "I'm glad it did too! Hahaha..."
    hkmonologue "I could've been poisoned by punch... ..."
    hkmonologue "I just played Russian Roulette with his punch..."
    hkmonologue "At least I'm almost done with the taste testing. Let's just hope the last dish won't try to kill me..."

    # GRIMALDI'S DISH BEST FOR LAST 
    hk "All right, Grimaldi. I have save the best dish for last!"
    grimaldi "And Grimaldi is very excited that lawyer friend did so!"
    grimaldi "Grimaldi presents to Hisako food from homeland: Pierogi with sauteed sauerkraut!"
    sfxText "{i}*chew chew munch munch*{/i}"
    hk "Oooo! This is so tasty, Grimaldi! The flavors melt on my tongue!!"
    grimaldi "Grimaldi is truly jubilant that friend enjoys food from the homeland!"
    grimaldi "Does Hisako think other will enjoy Grimaldi's cooking?"
    hk "They won't just enjoy it, but they'll absolutely love it!"
    grimaldi "Grimaldi is overflowing with joy!"

    # ENDING OF SCENE 5
    nobruo "Awesome!! We got through all of the dishes, making sure they were certified-delicious, and now they're ready to plate!"
    yashimata "Hisako, thank you so much once again for helping us out with our dishes! We seriously cannot thank you enough!"
    grimaldi "Grimaldi promises to return favor in future!"
    hk "Guys, it's no problem at all!"
    hk "You three spent a huge chunk of time making the food for everyone, so I should really be thanking you!"
    hk "Besides, friends help each other, no matter how big or small the problem is!"
    yashimata "We're all glad to have someone so tubular as our friend!"
    noburo "Having you as a fellow peer and friend is gonna make these school years the best time ever!"
    grimaldi "Grimaldi agrees with other friends and is happy to cherish friendship!"
    hk "And I am happy to have friends like you as well!"
    hk "Now, unless there's anything else you need me to help with, I'm gonna head back to my room and get ready for the party! Is that cool?"
    yashimata "Yeah, go on ahead! We're all good here!"
    grimaldi "See you at party, Hisako!"
    noburo "Smell you later, Hisako!"
    hk "Bye, now!"

    # END SCENE 5
    jump scene2_10
        
# SCENE 6 [WHITE WYVERN MANOR - DINING ROOM (MULTICHOICE OPTION 3)] --> HISAKO GOES TO THE DINING ROOM TO SEE HOW SHINZO, KICHI, AND RYOSEI ARE HOLDING UP.
# SHE'S HOPING THAT THE 3 BROS IN THE KITCHEN AREN'T CAUSING MAYHEM, BUT SEE WILL SOON DISCOVER THE OTHERS ARE IN MAYHEM THEMSELVES.
label scene2_6:
    hkmonologue "Okay...I am pretty sure that everything's fine in the dining room, but what happens if it isn't?"
    hkmonologue "There could be all sorts of pandemonium in there, making Kichi, Shinzo, and Ryosei's jobs and their lives harder than it has to be!"
    hkmonologue "Fingers crossed...Fingers crossed...Fingers crossed!"

    # HISAKO ENTERS THE DINING ROOM 
    hkmonologue "And...we're all good! Everything seems to be going smoothly doen here!"
    hkmonologue "The silverware has been polished, the plates set up on the tray in an ornate fashion..."
    hkmonologue "...and the glasses cleaned and rinsed: ready for whatever drinks go in them!"
    hkmonologue "Awesome! I guess the only think that needs to be done is wait for the food to finish cooking, plate it, then bring it down to the basement!"
    hkmonologue "Now it's time for me to find Kichi and ask her if she needs me help out!" 
    
    # START OF THE DEBATE
    kichi "...And that is how both of our {color=#efcc00}{b}Ultimates{/b}{/color} are different, while also sharing multiple similarities!"
    hkmonologue "Wait! Was that Kichi? I wonder what they're talking about..."
    kichi "Do you finally understand what the differences are?"
    shinzo "Not at t'all! It's all still so confusin', it feels like my head's on backwards!"
    ryosei "{i}Maybe your head really is on backwards...{/i}"
    shinzo "What'd you say, partner?"
    ryosei "I said: What parts are you still confused with?"
    shinzo "You said that an astrologist uses the planets, stars, an' a person's birth date information to make the predictions..."
    ryosei "Yes, what you said is true, so far."
    shinzo "And when it comes to the psychics, they rely more on th' mind and speak to dead people and stuff?"
    ryosei "No, those are spiritual mediums."
    shinzo "Then why do you use all those tools that she uses like cards and crystals an' all?"

    # DEBATE GETTING HEATED
    kichi "Like we've explained it four times, hun: psychics and astrologists use the same tools more or less for predictin' the future."
    shinzo "But then who has ESP or whatever it was?"
    ryosei "Like {i}*I*{/i} also said multiple times, my dear friend: I, as a psychic, have extrasensory perception."
    ryosei "This allows me to be more open to both the spiritual and supernatural aspects of this wonderful world."
    ryosei "I use divinatory items in order to make my connection with the Astral Plane stronger to gaze into the future more clearly."
    ryosei "Do you get it {i}*now*{/i}??"
    shinzo "Then if you have extra senses, what does she use?"
    kichi "Oh, bless your heart...None of this was written in the stars."
    shinzo "So if you couldn't foretell this, did your ESP detect this then?"
    ryosei "Why, I did not. I don't think even the Akashic record could either..."

    # HISAKO INTERRUPTS TO AVOID A CONFRONTATION 
    hkmonologue "Oh boy, I do not like where this is heading."
    hkmonologue "The last thing I need today is to see Ryosei try to strangle a fellow housemate."
    sfxText "{i}*knock knock knock*{/i}"
    ryosei "Huh? Who is over there? Speak now and reveal thyself!"
    hk "Hello!"
    ryosei "Hisako!"
    shinzo "How do ya do, lass?"
    kichi "Hisako, dumplin'! How's everything treating you 'round here?"
    hk "I'm feeling a lot better than I did earlier!"
    kichi "That's great to hear, darlin'!"
    shinzo "What you doin' around these parts for? Shouldn't you be taking it easy n' lying down?"
    hk "Since I was feeling better, I decided to come down here and help out!"
    ryosei "Although your thoughts of generosity and charity are appreciated by all of us, we've already finished all that can be at the moment."
    ryosei "And until The Three Musketeers in the kitchen finish their cookings, I forsee us being here for quite a time."
    kichi "You are welcome to stay and chat with us for the time bein', hun!"
    hk "Only if it's cool with all of you."
    ryosei "Absolutely."
    shinzo "By all means."
    hk "Thank you! Also! Sorry about interrupting your conversation earlier."
    kichi "Oh no. You're fine, hun! It wasn't anything important now."
    hk "What were you all talking about, if you don't mind me asking?"
    ryosei "{i}*sigh*{/i}"
    hkmonologue "Yep, I can understand how frustrated you are, Ryosei..."
    hk "Did I say something wrong?"
    ryosei "No...no you didn't. It's just complicated, Hisako."
    hk "The conversation?"
    ryosei "Indeed, my friend."
    ryosei "To make a long story short, Kichi and I have been trying to explain to The Malboro Man..."
    ryosei "how both of our {color=#efcc00}{b}Ultimates{/b}{/color}, although very similar, are actually quite different from one another."
    hk "Does he understand the differences?"
    kichi "That befuddled-lookin' face says it all, but why don't you tell her, Doc Holiday?"
    shinzo "I'm telling y'all: it still don't make any sense to me!"
    ryosei "Do we have to go through all of this a fifth time to you?"
    hk "I don't think that will be necessary, Ryosei! I think what Shinzo needs is an apology!"
    hk "Once he connects with something he's very well-acquainted with, then everything else will fall into place."
    ryosei "Well I hope so, not only for you, but for all of our sakes!"

    # ANALOGY TIME 
    hk "Don't worry! Just trust me!"
    ryosei "Alright then..."
    hk "Okay! So, Shinzo, you're still confused on what makes a psychic different from an astrologist, correct?"
    shinzo "Damn straight! All of the similarities and whatnot made me feel like I went and gone off the deep end!"
    ryosei "{i}Probably because you have{/i}."
    kichi "Ryosei! Shhhhhh."
    ryosei "Okay, okay."

    # ANALOGY
    hk "Think of it this way: Imagine a psychic and an astrologist like a sheriff and a deputy."
    hk "Both of them were there to enforce the law in the Old West, but whereas the shriff has more jurisdiction and say-so in certain matters..."
    hk "The deputies take orders from the sheriff."
    hk "While psychics and astrologists both predict futures, psychics may invoke the powers of astrology themselves!"
    hk "This, along with other divination practices, allows them to further their mind into the future unknown!"
    hk "Astrologists, however, are bound only to their own practice and cannot use other forms of divination to delve into the astral plane."
    shinzo "Uh huh..."
    hk "Finally to drive the point home: A sheriff can be a deputy; the deputy cannot be a former sheriff."
    hk "Therefore: A psychic can be an astrologist, but an astrologist cannot be a psychic! Does that make sense to you?"

    # REALIZATION 
    shinzo "... ..."
    shnzo "OHHHHHHHHHHH!! I get it now!"
    shinzo "Why didn't the two of y'all explain it like that earlier?"
    ryosei "{i}*slap*{/i} Even with my hundreds of readings today, none have predicted a future such as this..."
    kichi "Fate can be most cruel sometimes, hun. It truly can be."
    shinzo "Much obliged for the help, Hisako!"
    hk "No problem at all! Glad I could help!"
    shinzo "And my apologies to you two. I didn't mean to sound like such a dunce."
    kichi "No hard feelings, hun."
    ryosei "I suppose the universe is back in balance, so all is forgiven."
    ryosei "It would also be dishonorable and bad karma to harbor ill feelings to those who ask for forgiveness with sincerity."
    hk "Now that that's all said and done, all we need to do is wait for the food to finish cooking!"
    ryosei "Who knows how long that will take? It may be minutes, hours, days, or even..."
    sfxText "{i}*ding ding ding*{/i}"
    noburo "Food is ready!"
    ryosei "...Seconds. It will take seconds."
    noburo "Get ready to start plating, my dudes! Oh hey, Hisako! Glad to see you doing better! Are you helping us plate the food?"
    hk "Yes, I am!"
    noburo "Totally 'licious, bro! The more help, the better!!"
    noburo "Now, let's get to it! The party starts in less than an hour!"
    ryosei "With seven of us, I see us finishing this rather quickly."
    shinzo "I don't think my Third Eye is all that impressive in size, but my gut feeling agrees with ya!"
    kichi "Why don't we stop talking 'bout the size your Third Eye, and prepare the food. Hisako, hun, are you ready?"
    hk "Yeah! Let's do this!"

    # FADE TO BLACK, THEN REAPPEAR 

    # AFTER THEY FINISH PLATING AND ENDING SCENE 
    shinzo "All right! All of the food is set up, drinks poured out, and right before the top of th' hour too!"
    kichi "Hisako, dear, we wanted to thank you for your help, not only with the food prep, but also with our conversation earlier!"
    hk "There's no need to thank me, Kichi! I was just glad to have helped out before tensions boiled over!"
    kichi "If you hadn't come by the time you did, I just knew that Ryosei would'a blown a fuse tryin'a hold in all that frustration, and honestly,
    I don't blame him."
    hk "Neither do I. Even upon entering the dining room, I could just feel the energy surrounding Ryosei."
    kichi "Sounds like you're more in-tune with the supernatural than I thought you were!"
    hk "Really?"
    kichi "Indeed! However, I think it'd be best to hold off on this little chat and save it later for the party."
    kichi "You should take this time to freshen up before the party, hmm?"
    hk "You're right! I might as well while I have the time!"
    hk "Again, it was really nice helping you and the others out! See you at the party!"
    kichi "See you soon, Hisako!"

    # END SCENE 6
    jump scene2_10

# SCENE 7 [WHITE WYVERN MANOR - BAR (MULTICHOICE OPTION 4)] --> ALTHOUGH SHE KNOWS I TMIGHT BE A BAD IDEA, HISAKO DECIDES TO GO HELP 
# MATSUKO, NAGANORI, AND NARUMI DOWN AT THE BASEMENT BAR. WHAT WILL HAPPEN WHEN HER HAPPY AND FRIENDLY NATURE IS CHALLENGED BY THE 
# SILENCE AND COLDNESS EMANATING FROM THE OTHERS?    
label scene2_7:
        # HISAKO ENTERS THE BAR 
        hkmonologue "Wow, it's very quiet down here! no talking, no music, nothing at all. Is there even anybod down here?"

        # THE OTHERS AT THE BAR 
        naganori "... ..."
        matusko "... ..."
        narumi "... ..."
        hkmonologue "Nope, they're down here after all."
        hkmonologue "With this much silence, you could drop a pin and it would sound like glasses smashing on the floor!"
        naganori "You do knew we can all hear you, Hisako."
        hk "What!? How'd you know and how could you tell it was me?"
        naganori "Eizo is out of commission and Vladnot holed up in his room, you were the only logical answer left."
        matusko "In addition, your shoes were slapping against the tile. If you were trying to be sneaky, it wasn't working."   
        naganori "..."     
        narumi "..."
        hk "Was I really that loud?"
        matsuko "Yes. Yes, you were. And until you arrived, it was rather quite peaceful."
        hk "I'm...really sorry. I'll make sure not to bother you."
        hk "See you all at the party...I guess...." # EXIT HISAKO 

        # NARUMI CHIMES IN 
        matsuko "..."
        naganori "..."
        narumi "... ... Wait."
        hk "Narumi?"
        narumi "I have a few cases of glasses ad other bar supplies that need to be cleaned, and help would be greatly appreciated in the dishroom."
        hk "Are you sure?"
        narumi "Yes, I am sure, Hisako."
        matusko "Narumi, what are you doing?"
        narumi "Giving her something to do. Is there anything wrong with my decision?"
        matsuko "You know just as well as I do that we were doing just fine until she came strolling along."
        narumi "Do you want to go back there and do all the dirty work or rather her do it?"
        narumi "It doesn't negate the fact we still have things that need to be cleaned, prior to Hisako's arrival."
        matsuko "I still think it's a bad idea."
        hkmonologue "Me just being here has made tensions rise so much! Should I just leave? Ugh, I feel so guilty..."
        narumi "Naganori: your thoughts?"
        naganori "Hmmm...I think it would be best for HIsako to deal with cleaning the glassware while we finished up here behind the counter."
        matsuko "Now you too?"
        naganori "Matusko, you make it sound as if I betrayed you in some way."
        naganori "We could use the help, and Hisako is right before us wanting to do just that."
        naganori "And to be frank with you, the way you have been reacting to Hisako's presence is akin to that of a child throwing a tantrum in a public place."
        matusko "How dare you..."
        naganori "Irrational anger, outbursts, personal insultations."
        naganori "You have hit all three marks all because Hisako decided to come down here and visit."
        narumi "I stand by my decision. If it bothers you so much, you are welcome to leave until the party. Are we all in agreement?"
        naganori "Indeed."
        matusko "Hmph. Whatever"
        narumi "Good. Hisako: dishroom is behind the double doors, straight down, and on the first right."
        hk "Thank you very much for allowing me to stay! It really means a lot to me."
        narumi "...I mean, it's just washing dishes, but you're welcome."
        hk "I'll make sure those glasses are absolutely spotless!"
        matusko "You can't make them spotless if you keep on talking about and not actually going into the dishroom."
        naganori "There you go again with the juvenile quibs."
        hk "No, Matusko's right! I need to do more action and talk less! I'll see you guys in a few!" # EXIT HISAKO 
        naganori "I'm surprised she still has that Happy-Go-Lucky attitude and tenacity from earlier."
        naganori "If I were her, trying to maintain that peppiness would honestly tire me to the bone."
        matsuko "... ..."
        narumi "At least it saves me from doing the dishes myself again, and I'll take what I can get."
        narumi "I look forward to see how spotless those glasses will turn out to be."

        # FADE TO BLACK, THEN REAPPEAR 

        narumi "I'm impressed. You really put your heart into making those glasses shine like crystals. Thank you for your help, Hisako."
        hk "No...problem. Sorry, I'm just a little tired."
        naganori "It appears she put more than just \"heart\" into washing the glasses."
        naganori "I guess you could say that just by appearance alone, hmmm hmmm hmmm."
        narumi "On that note, since everything is pretty muh finished around here..."
        narumi "I'd recommend you go back to your room and get a new change of clothes before the party starts."
        narumi "You're drenched from head to toe in water. How's that even possible, I don't know."
        hk "Yeahhhh, that was kind of my first time woking in a dishroom."
        hk "I wanted to make sure I helped you out more than potentially being a detriment."
        narumi "I can tell you that you weren't a detriment. But, you should leave now before you continue another conversation."
        hk "You're right! I do tend to derail my own train of thought and completely forget what I was doing in the first place."
        narumi "You're doing it again."
        hk "Oops! I'll be leaving now. Thank you for letting me help you all out! I'll see you all in a little bit!"
        matsuko "..."
        naganori "Take care, Hisako."
        naurmi "Later."

        # END SCENE 7
        jump scene2_10

# SCENE 8 [WHITE WYVERN MANOR - RECREATION ROOM (MULTICHOICE OPTION 5)] --> HISAKO DECIDES TO PAY YUKAKO, YUI, AND NAYOKO A VISIT IN THE BASEMENT
# RECREATION ROOM NEAR THE BAR. HOW WILL THE INTERACTIONS GO?
label scene2_8:
    # JUMPING RIGHT INTO THE SCENE 
    yui "Come on, Yukako, you can't just leave me hanging like that!"
    yui "You gotta tell me more about yourself! The anticipation is killing me!"
    yukako "I don't know what you find so interesting about me."
    yui "Oh, nonsense! There's no need to be so modest here!"
    yukako "I assure you that I'm not being modest. All I know is that I am a normal person just like yourself."
    yui "Have you looked at yourself in the mirror?"
    yukako "I believe I did about..."
    yui "Your enigmatic personality, eyes that have seen events that could span many lifetimes..."
    yui "and behind every word, another door leading to a maze of endless mystery!"
    yukako "Are you really sure you can see all of that in me?"
    yui "Trust me! I'd never lie when it come to seeing the potential and inspiration in a muse!"
    nayoko "Oh my gosh, Yui!! Your {color=#efcc00}{b}Ultimate{/b}{/color} is so awesome!!"
    nayoko "How are you able to find so many qualities in a person just by looking at them?"
    yui "Hehehehehe...If it isn't possible to notice, I have been blessed by the gods of Olympus, Zeus himself, with such a gift!"
    nayoko "REALLY???"
    yui "Nah, I just made that up on the spot. What did you think? Cool, right?"
    nayoko "You made that story up that quickly??"
    yui "Yeah huh!"
    nayoko "That's amazing!!"
    yui "Hehehehehe!"

    # ENTER HISAKO 
    sfxText "{i}*knock knock knock*{/i}"
    yui "Huh? What was that?"
    hk "Hey guys!"
    nayoko "Is that who I think it is?"
    yui "It is!!"
    yukako "Hi...Hisako."
    $ multipleppl.name = "Yui & Nayoko" # NAME CHANGE 
    multipleppl "Hisako!"
    hk "How are you..."
    sfxText "{i}*scuttle scuttle shuffle shuffle*{/i}"
    hk "What the...!?"
    
    # YUI AND NAYOKO TALKING 
    nayoko "Hiiiiiiiiii! How are you feeling? You look a million time better!"
    yui "I know, right? She just looks absolutely stunning!"
    nayoko "However, there's a more pressing matter at the moment: Why has Hisako come down here?"
    yui "{i}*gasp{/i} Do you think she is here because she wanted to help us clean?"
    nayoko "Oh...My...Gosh...That would be so awesome!! However, we shouldn't assume, so we should ask instead!!"
    multipleppl "Are you here to help us, Hisako??"
    hk "Uh..."
    yukako "I am pretty sure that she has come down to help. Right, Hisako?"
    hk "...Right! Yes! Since I am feeling better, I thought I'd come down to see if you three needed any assistance cleaning up the recreation room!"
    hk "I mean, cleaning up an area as big as this can be quite daunting for only three people."
    nayoko "You're literally the best, Hisako!! Of course you can help, however, from the looks of it, I dont think there's much left... ... ..."
    hk "Nayoko, are you okay?"
    nayoko "What happened to all of our progress, Yui?"
    yui "I have no idea! I swear we were almost finished!"
    nayoko "Like didn't we already sweep over there? And set up the table in the corner? What is happening!?"
    yui "Do you think someone may have cast a spell on us, or even used time manipulation just to mess with us? Or maybe..."
    yukako "If I may interject..."
    hk "Yukako?"
    yukako "The reason...why the room isn't finished is becaused I have been doing most of the work."
    hkmonologue "Well that makes a lot more sense than time travel."
    yui "I thought we've been helping you this entire time!"
    yukako "In all honesty, not really...you both get distracted very easily."
    yukako "Since you saw me as...a muse, you have been asking me questions non-stop while Nayoko sits and watches."
    yui "So, we were the ones that were holding you back?"
    nayoko "And making you do all the work?"
    hkmonologue "Oh no..."
    multipleppl "WE'RE SO SORRY, YUKAKO!!"

    # APOLOGIZING AND RECONSILIATION 
    yukako "Ah! It's okay, I promise."
    yui "No, it's not! We've been working you unfairly!"
    yukako "Yui, Nayoko: please don't cry!"
    yukako "It's alright. I am not mad or sad or anything. Let's just focus on cleaning..."
    nayoko "We'll do anything to make up for doing this to you!!"
    yukako "...Um..."
    hkmonologue "Don't worry, Yukako, I got this!"
    hk "C'mon, guys! There's no need to be upset."
    hk "Yui: you were just very excited that Yukako holds a familiar, yet exiciting, source of inspiration for your stories!"
    hk "Sometimes, you just get a little too excited. You said so yourself earlier!"
    hk "Nayoko: it's totally okay to space out and have your head in the clouds sometimes. I completely understand! I've done it on the job sometimes myself!"
    hk "However, there does come a times when you need to try your best and concentrate on the task at hand."
    hk "And the same goes for you too, Yui!"
    yukako "...Hisako..."
    hk "You both have apologized to Yukako, and she has accepted your apology."
    hk "Instead of feeling down and being upset, let's put that energy into cleaning up this room before the party starts!"
    yui "...You're right, Hisako! If we both continue to sulk in our own pity, then the entire party would be a complete failure, and it would be our fault."
    yui "I promise I will do my best and stay on task!"
    nayoko "Same here! And if either one of us starts to get distracted, don't hesitate to call us out on it!"
    hk "Sounds good to me! How about you, Yukako?"
    yukako "Ah! Yes, all is good with me."
    hk "Alright then! Let's get to it! We only have an hour-and-a-half to get this room in tip-top shape!"

    # FADE TO BLACK, THEN REAPPEAR 

    hk "And that should do it!"
    nayoko "Yippee! We finished setting up the room!"
    yui "And just in the nick of time too!"
    yukako "I am glad that we were able to set up everything...without disrupting anything."
    hk "Same here! I honestly had some doubts at times."
    yukako "You...and me both!"
    yui "Yukako. Hisako. Yui and I just wanted to apologize once again for causing so much inconvenience earlier."
    nayoko "Not only that, but we also wanted to thank you both for all your help. Without you, Hisako, this party would've died before it even started."
    hk "You guys don't have to apologize! It was no problem lending my assistance. That's what I wanted to do in the first place anyway!"
    hk "Besides, I'm sure you three would've been able to finish the rec room by yourselves!"
    yukako "No, Hisako. If you hadn't intervened, I would've been the only one cleaning."
    yukako "Nayoko and Yui would've continued being distracted and all the work that everyone else is doing would've been for naught."
    yukako "You are the reason...why this party will go on!"
    hk "Yukako...Thank you! Thank you all for your kind words. I am glad that I was able to have a fun time and enjoy helping out my friends!"
    yukako "Hmmm...Glad to hear."
    nayoko "Yui, did she just call us..."
    yui "One of her friends? It's so exciting!!"
    nayoko "I know, right?"
    hk "Well, I'm gonna head back up to my room real quick and freshen up before the party!"
    yukako "You go do that. You deserve it."
    hk "I will see all of you soon! Bye now!"
    yukako "Goodbye, Hisako Kawahara."
    yui "See you later, Hisako!!"
    nayoko "Bye Bye!"

    # END SCENE 9
    jump scene2_10

# SCENE 9 [WHITE WYVERN MNAOR - MUSIC ROOM (MULTCHOICE CHOICE 6)] --> HISAKO DECIDES TO CHECK THE MUSIC ROOM WHERE AZUMI, FUJIKO, AND CHINO ARE AT.
# THERE SWILL TALK TO THE OTHERS ABOUT MUSIC RECOMMENDATIONS TO PLAY WHILE THE AKUDA BROTHERS ARE NOT DJ-ING DURING THE PARTY
label scene2_9:
    # JUMP RIGHT INTO THE SCENE 
    azumi "I dont know about these, Fujiko. I'm trying to imagine it, but I really can't see this playing at the party."
    fujiko "C'mon, are you sure, Azumi? These albums are pretty fire!"
    azumi "While I do agree that these albums are pretty good choices..."
    azumi "I don't think Metalcore or Heavy Metal in general will strike a chord with most partygoers in the same way it would with us."
    azumi "You know what I mean?"
    fujiko "Hmmm...I see what you did there with the \"chord\" pun!"
    azumi "Fujiko! You know I didn't intend for that to be a pun!"
    fujiko "I know, I know. But, yes, I do understand what you're getting at."
    fujiko "The only problem now is: what music do we choose? I mean, look at all these crates!"
    fujiko "There has to be at least a thousand records here! Hell, maybe even more!"
    azumi "I think the administration may have gone a little overboard with the records."
    azumi "It would be easier to find good music if we had an extra set of hands to help out."

    # ENTER HISAKO
    sfxText "{i}*knock knock knock*{/i}"
    azumi "Hmmm? Well look what the cat dragged in!"
    fujiko "Hisako!! Looking fresh to death, I see!"
    hk "Hey y'all! What are you up to here?"
    azumi "We are currently looking for songs to play at the party."
    hk "Huh? I thought the Akuda Brothers were in charge of the music."
    fujiko "Oh they are! Most of the time, that is."
    hk "What do you mean by \"most of the time\"?"
    azumi "You wouldn't expect them to entertain the entire time and not have a chance to enjoy the party themselves, right?"
    hk "Now that you mention it, that is a pretty good point you bring up."
    azumi "Exactly! So that got us thinking about what we could bring down to help out with that issue."
    fujiko "At first we though about bringing down the harpsichord, but Azumi said that it didn't jive with the party's atmosphere."
    azumi "So that's where our next idea came in: let's bring down some records that Naoki could use on his turntables!"
    fujiko "Which brings us to our current problem..."
    fujiko "There's literally thousands of records to comb through, and we don't have enough people for the job."
    azumi "Hisako, would you like help us out and find some awesome party jams?"
    hk "Absolutely! With the three of us, it shouldn't be too hard of a task to accomplish!"

    # CHINO JUMPSCARE!
    chino "N-Now that we have you as a fourth, we'll get it done in no time!"
    hk "GYAHHHHHHH!!!!!"
    chino "AHHHHHHHHHH!!"
    azumi "Hisako! Are you okay?"
    hk "Y-Yeah, I'm good..."
    hk "Hello again...Chino..."
    chino "Hi H-H-Hisako...I'm sorry if I scared you again."
    hk "No, it was my fault. I didn't notice you were in the room again."
    hk "I sincerely apologize that this keeps happening! Truly I am!"
    chino "It's okay! I p-promise I'll make sure I'm not acting like a such a wallflower."
    hk "And I promise to be actively looking out for you!"
    chino "T-Thank you, Hisako!"
    hk "No problem!"

    # BACK TO THE PROBLEM AT HAND 
    fujiko "Alright! Back to the problem at hand!"
    hk "Yes! Sorry about the interruption."
    azumi "All good here! Now then, the four of us need to use our heads collectively and make the best damn playlist!"
    hk "Let's do this!"
    fujiko "And we better make it quick too, or it's going to be ritual misery for all of us!"
    chino "G-Got it!"

    # FADE TO BLACK (NOT REAPPEAR HERE)
    hk "Oh man, this one is a must-have! Anything by ROTFL is an instant party classic!"
    chino "T-This one is pretty good! Whenever ON-POINT play, it actually makes me want to move off the wall and onto the dance floor!"
    fujiko "How could I forget this absolute banger? We're absolutely putting 4AY!8 in the playlist!"
    azumi "Now, a couple of song by The Red-Kidney Beans should finish this off!"
    fujiko "Alright! Let's head on over to the rec room, and hand these over to the Brothers!"

    # REAPPEAR HERE!!!
    hk "Wow! The rec room looks so inviting!"
    hk "And wait! When did the rec room connect to the bar?!"
    fujiko "Hold up. You didn't know that?"
    fujiko "How else did you think everyone was going to get a drink from the bar?"
    hk "I...don't...know...I guess I thought Narumi would bring some bar supplies over?"
    fujiko "I don't know if I agree with your reasoning, but I do agree that the rec room and bar combo looks pretty baller!"
    azumi "Okay, Hisako! One final thing left to do: could you take these over to Naoki for me?"
    hk "Yeah, I can do that, Azumi!"
    azumi "Thanks! I really appreciate it!"

    # CUTING CONVO SHORT 
    hk "Sorry to cut the conversation short, Fujiko..."
    fujiko "No worries. Imma go chat with some of the others here like that forensics chick or the storyteller! They seem fun to joke with!"
    hk "Okay then! See you around!"
    fujiko "See ya!" # EXIT FUJIKO HERE
    hkmonologue "Alrighty then, let me hand these off to the DJ and then we should be good!"
    sfxText "{i}*click clack click clack*{/i}"

    # VISITNG NAOKI 
    hk "Hey, Naoki!"
    naoki "Hi, Hisako! I'm glad to see you doing better!"
    hk "Thank you! I definitely feel a million times better than I did earlier."
    naoki "I'm really happy to hear that!"
    naoki "So, what's up? Did you need anything?"
    hk "Yes! Azumi, Fujiko, Chino, and myself have brought down some extra records from the music room!"
    hk "So, whenever you need to take a break from DJ-ing, you can pop one of these on and enjoy the party yourself without any hassle!"
    naoki "This is awesome! Thank you so much!"
    naoki "To be completely honest, Tetsu, Hiko, and I were so focused on bringing the equipment down that we completely forgot about background party music."
    naoki "This is such a big help! THank you so much once again!"
    hk "No problem! We're glad we could be of assistance!"
    hk "But, I'm going to take my leave and get freshened up before the party starts!"
    naoki "You go do that! Take care, Hisako and see you soon!"
    hk "See ya, Naoki, and good luck!"
    naoki "Thank you! We'll be doing our best!"

    # BACK TO AZUMI AND CHINO/ SCENE END 
    hkmonologue "And done! Now gotta back in with Azumi and Chino before heading up to my room!"
    hk "Okay, Azumi, the records have been handed off to Naoki!"
    azumi "That's wonderful!"
    azumi "Now, on behalf of me, Chino, and Fujiko, we would like to thank you for your help with the records!"
    azumi "I have no doubt that our choices will keep this party kickin'!"
    hk "Don't worry about it! I'm just glad I was able to help out and learn more about my friends through their tastes in music!"
    chino "I am glad to be considered your f-f-friend, Hisako!"
    azumi "And the same goes for me and I know it also the same for Fujiko as well!"
    hk "I'm really happy to hear!"
    azumi "Mmmm Hmmm!"
    hk "I apologize if it seems rude of me, but I'm going to head up to my room before the party starts and..."
    azumi "You're not being rude at all, Hisako! It's perfectly normal!"
    azumi "But, hey, don't be a stranger at the party!"
    hk "Don't worry! I won't! I gotta keep my promise to Chino somehow! But I'll be seeing you around!"
    azumi "Later, alligator!"
    chino "Goodbye. H-Hisako!"
    hk "Bye now!"

    # END SCENE 9
    jump scene2_10

# SCENE 10 [WHITE WYVERN MANOR - BASEMENT: REC ROOM/BAR] --> IT'S PARTY TIME AT THE WHITE WYVERN MANOR! THE COUNTDOWN TO THE EPIC CLIMAX
# TO THIS PROLOGUE AND BEGINNING OF THE HOPE'S PEAK UNIVERSITY KILLING GAME STARTS HERE! WATCH THE PARTY UNFOLD AS THE STUDENTS ENJOY THEIR 
# LAST MOMENTS OF FREEDOM BEFORE BEING FORCED INTRO A GAME FULL OF HOPE, BETRAYAL, AND DESPAIR: THIS IS DANGANRONPA: REAWAKENING
label scene2_10:
    # MASSIVE HISAKO MONOLOGUE INCOMING:
    # MONOLOGUE PART I
    hkmonologue "Shortly after everyone finished their assigned jobs, the party went into full swing!"
    hkmonologue "Looking around the room, I see not a frown in sight! Even Vladnot was out of his room and roaming about!"
    hkmonologue "All of my fellow housemates. My peers. My friends. All of them enjoying themselves and having fun!"
    hkmonologue "Well, almost everyone. There's still no sign of {color=#efcc00}{b}Eizo{/b}{/color} anywhere."
    hkmonologue "The poor kid. He really needs to take a break from that job and focus on his health."
    hkmonologue "I know that he would've enjoyed the party as well..."
    hkmonologue "But I'd rather him get the rest he needs and have fun when he's attentive and conscious."

    # MONOLOGUE PART II 
    hkmonologue "Near the DJ booth are the Akuda brothers."
    hkmonologue "Kazuhiko is continuing to hype up the party, while Tetsunori ups the ante, breaking out his best moveset!"
    hkmonologue "And behind the scenes, Naoki is tearing it up with the music!"
    hkmonologue "Making sure that each song flows into one antoerh in between transitiions, down to the last beat measure!"

    # MONOLOGUE PART III
    hkmonologue "Looking by the dance floor, Kichi, Azumi, and Fujiko are out there feeling the rhythm and soul through the music, 
    letting it take control of them!"
    hkmonologue "Shinzo is also there, but is awkardly doing a line dance, despartely trying to keep up with the beat of the music."
    hkmonologue "Hmm Hmm Hmmmm! At least he's trying, so I'll give him that!"

    # MONOLOGUE PART IV
    hkmonologue "Over at the bar, Yashimata and Noburo are in the middle of a drinking game with Narumi officiating the match overall!"
    hkmonologue "With Noburo being the {color=#efcc00}{b}Ultimate Greek Brother{/b}{/color} and all, I was under the impression he'd 
    dominate the competition..."
    hkmonologue "However, by the looks of it, Yashimata appears to be winning. And by a large margin too! You got this, Yashimata!"

    # MONOLOGUE PART V 
    hkmonologue "Sitting by the side tables is Ryosei, accompanied by Matsuko, Naganori, and Vladnot."
    hkmonologue "It doesn't look like they're talking, rather, they are relaxing in silence, having a drink."
    hkmonologue "Matsuko and Ryosei seem to enjoy hard liquor, judging by the number of shot glasses between the two of them."
    hkmonologue "Naganori, meanwhile, holds a single glass of wine in his hand as he looks off int the distance."
    hkmonologue "Vladot enjoys cocktails, more specifically ones that are red in color."
    hkmonologue "Either he's a real vampire or he takes the whole thing so seriously!"
    hkmonologue "I mean, he is the {color=#efcc00}{b}Ultimate Vampire{/b}{/color}, so I shouldn't be too surprised."

    # MONOLOGUE PART VI 
    hkmonologue "By the snack and punch table, Yui, similar to a busy bee, is moving around Grimaldi, completely enthralled."
    hkmonologue "If I had to guess: Yui has found a fountain of inspiration with Grimaldi."
    hkmonologue "Nayoko, on the other hand, is talking to.......Chino! Yes, she's talking to Chino."
    hkmonologue "Although I can't explicitly see Chino's face, the LEDs on her face show she is very happy someone is talking to her!"
    hkmonologue "I'm really happy for her!"

    # MONOLOGUE PART VII
    hkmonologue "Although I see most of my new friends, there's one I haven't spotted yet. I wonder where she is?"
    hkmonologue "Hmmmmm...Ah! There she is, but why is she way over there?"
    hkmonologue "Usually, I would say that Chino is the wallflower, but {color=#efcc00}{b}Yukako{/b}{/color} is the one being the wallflower!"
    hkmonologue "Does she want to be by herself? Does she want to be at the party?"
    hkmonologue "I hope I don't invade her personal space, but I'm just goig to pop by and make sure she's okay."

    # HISAKO TALKING WITH YUKAKO 
    hk "Hey, Yukako!"
    yukako "... ..."
    hk "Yukako?"
    yukako "...Hmmm..."
    hk "Hey, are you good?"
    yukako "Mmm? Ah!"
    hk "I'm so sorry!"
    yukako "No...You're okay. I was just startled...that's all."
    hk "Oh, okay..."
    yukako "..."
    hk "..."
    yukako "..." # NERVOUS 
    hkmonologue "Oh man, now I feel bad for making it awkward!"
    hkmonologue "This must be just as bad for her! I have to get this conversation rolling!"
    hk "So, how are you feeling? Enjoying the party?"
    yukako "It's good...I am glad to see everyone having fun."
    hk "But, you aren't over there with your peers. Why is that?"
    yukako "I'm just not that big of a social butterfly, or a party person...However, it is a nice change of scenery."
    hk "Scenery? What do you mean?"
    yukako "With a profession like mine, life isn't all that bright."
    yukako "More times than not...I've seen the end of peoples' lives more than I see their joys in life."
    yukako "Although...I am desensitized for the most part...I enjoy seeing the spark of life iginiting with passion in one's eyes..."
    yukako "rather than seeing it extinquished."
    hk "Oh, wow..."
    yukako "Do not feel bad for me. It was my decision to be a {color=#efcc00}{b}forensic scientist{/b}{/color}, just as it was yours 
    to be...a {color=#efcc00}{b}lawyer{/b}{/color}."
    hk "..."
    yukako "But, I do appreciate you asking how I feel. I do not...get that a lot."
    yukako "You are a nice person...to be around, {color=#efcc00}{b}Hisako Kawahara{/b}{/color}."
    hk "Thank you! I'm glad I get to be not only your peer, but also your friend/"
    yukako "I am glad...as well."
    hkmonologue "I'm really glad that she is okay and enjoying the party in her own way!"
    yukako "I do have a question for you, Hisako Kawahara: Why do you have two drinks in your hand? Do you plan on drinking both by yourself or...?"
    hk "Oh my gosh! I completely forgot that I brought these over! Here! This one's for you!"
    yukako "Thank you...Hisako..."
    hk "Did you really think that I had them both for myself?"
    yukako "Not...really. I wanted to feign ignorance...ust to see how you would react."
    hk "Ah!" # EMBARRASSED
    yukako "Your embarrassed reaction...is honestly quite refreshing, Hisako."
    yukako "Glad to become friends with you...and everyone else here. I look forward to the school year ahead of us."
    hkmonologue "Oh my gosh...Yukako is actually smiling. She finally broke not just a smirk, but an actual smile!"
    yukako "...Erm...Hisako?"
    hk "Huh!?"
    yukako "I was just asking if I was allowed to drink this now."
    hk "Oh! Um...not yet! Narumi told me that all of us have to wait until midnight to drink."
    yukako "I understand...At least it is not that long of a wait at all."
    hk "At least!"
    sfxText "{i}*tap tap boom*{/i}"
    hiko "Alright! Is this thing on?"
    hkmonologue "Looks like the {color=#efcc00}{b}Ultimate M.C.{/b}{/color} is going to be taking over this ceremony!"

    # KAZUHIKO MONOLOGUE         
    hiko "Okay, everyone!"
    hiko "We are currently two minutes away from the top of the hour, and together, we are going to ring in the new school year, the right way!"
    hiko "Each of you currently holds a drink, crafted by none other than the {color=#efcc00}{b}Ultimate Bartender{/b}{/color} herself!"
    hiko "This drink is officially called The I-V Phoenix."
    hiko "The \'IV,\' is short for \"Initium Vum\". This phrase translates to \"The Beginning of Life\"."
    hiko "Here we all stand, although as individuals, but also as a community."
    hiko "We all come from different backgrounds and different life experiences, but the one thing that connects us all together is that we are  
    {color=#efcc00}{b}Ultimates{/b}{/color}."
    hiko "{color=#efcc00}{b}Ultimates{/b}{/color} who have been given a second chance to get back on our feet and be like those who change our world 
    for the better!"
    hiko "To all of you, I just want to say one last thing before we all toast:"
    hiko "I look forward to spending my college years here, not only to become friends with you all..."
    hiko "...but also to learn something new that I can use to change my life for the better!"
    hiko "This one is to us! Our future!"
    hiko "Our new Beginning of Life! Our {color=#efcc00}{b}Reawakening{/b}{/color}!!! Cheers!"

    # CHEERS 
    $ multipleppl.name = "Everyone"
    multipleppl "Cheers!!"
    yukako "Cheers to you, Hisako Kawahara!"
    hk "And cheers to you, Yukako Maeno!"
    yukako "Hmm...I am surprised you remembered my last name."
    hk "well, I am a lawyer, so I gotta have a good memory, right?"
    yukako "I believe...you are indeed correct, Hisako."
    hk "Hahaha!"
    sfxText "{i}*sip sip sip*{/i}"

    # CLIMAX 
    hk "Oh, wow! Narumi really outdid herself with this one!"
    hk "The lemon juice really compliments the gin and orange liquor! What do you think about the drink, Yukako?"
    yukako "..."
    hk "Yukako, are you okay?"
    yukako "...This isn't good..."
    hk "What isn't good? Is something wrong?"
    yukako "Hisako, we need to leave immediately!"
    hk "Yukako, you're starting to scare me. Tell me what is the matter!"
    yukako "Look at the bar!"
    hk "What do you mean look at the bar? Everyone is just enjoying them...selves?"

    # EVERYONE HAS COLLAPSED/DRUGGED
    hk "What the...? Everyone's knocked out!"
    hk "Even Narumi is out cold...Were all of our drinks spiked??"
    yukako "It would appear so. That is why we need to leave the Manor and reach for help!"
    hk "How much time do we have before the effects kick in?"
    yukako "Since we were the last to drink, about 3 minutes, 5 at most!"
    hk "W-What about the others? Don't they need help?"
    yukako "Hisako! If we don't leave the manor and get help ourselves, we'll succumb to the same fate as everyone else!"
    yukako "So stop wasting time and let's go!"
    hk "...Ok...Let's go!"

    # TRANSITION TO LIBRARY HERE 
    hk "Alright! A minute and a half remaining! We'll be out of here in no time!"
    yukako "Hi...sa...ko..."
    sfxText "{i}*thud*{/i}"
    hk "Yukako! No!"
    yukako "Just...leave...me..."
    hk "No! I'm not leaving you!"
    hk "You and I are going to make it out of here and get help! GRRRRRR!"
    hk "Don't you...worry...I still have some strength left in me."
    hk "I still have a few minutes...before it kicks in..."

    # TRANSITION TO DINING AREA 
    hk "We're almost there, Yukako!"
    hk "You...hear me? Yu...Yukako?"
    sfxText "{i}*slam*{/i}" # RINGING IN EARS
    hk "...Get up...I can't get up..."
    hk "Yukako...Yukako, please wake up..."
    hk "Please forgive me...I'll be back soon..."
    hk "Come on...Come on..."
    hk "Please body! {i}*huff huff*{/i}"
    hk "I gotta keep moving..."
    hk "Move...Move!"

    # TRANSITION TO ATRIUM 
    hk "Almost...there..."
    hk "Door...in front of me..."
    hk "I will...get help..."
    hk "Save...everyone..."
    hk "Save...every...one..."
    sfxText "{i}*ka-thump*{/i}"
    hk "No...No..."
    hk "Please...body..."
    hk "Not...right now..."
    hk "I need...to save them..."
    hk "I need..."
    hk "I need to save...Yukako..."
    hk "...Umph..."
    sfxText "{i}*thud*{/i}"

    # HISAKO'S VISION STARTS TO FADE IN AND OUT HERE

    # ENTER HI-DORA SAN 
    dumbhead "Alright, Boss, the last one is down for the count!"
    hidora "That's great to hear, but she wouldn't have gotten this far if SOMEONE would've spiked their drinks more!"
    hidora "If she escaped, that would've ruined our ENTIRE PLAN!"
    dumbhead "Dawww, I'm sorry, Boss. I'll do better next time."
    hidora "Damn sure you will!"
    friendlyhead "Look on the bright side, Sir! The drink finally kicked in, she didn't escape, and most importantly, she didn't hurt herself!"
    hidora "Well, at least there is that."
    friendlyhead "Sir, what should we do with her?"
    hidora "First thing we need to do is make sure she doesn't remember any of this..."
    hidora "If she remembers anything at all, we're screwed...Hey!! Are you two even listening??"
    friendlyhead "Yes, Sir!"
    dumbhead "Uh...yes, Boss!"
    hidora "Okay then. After that, take her to her room."
    hidora "This is a rinse and repeat with the others. Got it?"
    friendlyhead "Absolutely, Sir!"
    dumbhead "Yes, Boss!"
    hidora "Good, now get to it!"
    friendlyhead "Okay! Let's get her ready for the mind wipe!"
    friendlyhead "Wait a sec, she's still awake? I thought the drink would've knocked her dead."
    dumbhead "Don't worry, I got this! A little bonk on the head doesn't hurt anyone."
    friendlyhead "Wait, don't do it!!"
    sfxText "{i}*SLAM*{/i}"

    # PROLOGUE: DO OR DIE - RUN FOR YOUR LIFE OR SAY GOODNIGHT [THE END]
