# INVESTIGATION LABEL PROMPTS FOR PROLOGUE 

# PROLOGUE: HISAKO'S ROOM 

# 1. SHOWER DIALOGUE
label shower_dialogue():
    hkmonologue "The detail is so immaculate and intricate! And the room is massive too!"
    hkmonologue "They were even able to add a glass shower on the second floor!"
    hkmonologue "How they were able to turn the luxury of a mansion into a one-bedroom apartment is totally astounding!"

    # SUBTRACT FROM MAG NUM AND TURN BOOLEAN TRUE
    if (isMagGlassOneSeen == "false"):
        $ isMagGlassOneSeen = "true"
        $ magGlassNum  = magGlassNum - 1

    # CHECK TO SEE IF MAG GLASS NUM IS AT 0 OR CAUSE THEM TO CONTINUE UI INTERACTION 
    if (magGlassNum == 0):
        jump scene2_3_Post_Investigation
    else:
        call screen hisakoRoom

# 2. DESK DIALOGUE
label desk_dialogue():
    hkmonologue "There's a small bookshelf near my work desk!"
    hkmonologue "{i}The Dark Underbelly: Unravelling the Complexities of Crime and Law{/i}!"
    hkmonologue "{i}Understanding the Criminal Mind{/i}!"
    hkmonologue "{i}The Lawyer's Pocket Dictionary for Law and Order{/i}!?"
    hkmonologue "All the books I've always wanted, but never had the chance to buy! This is amazing!!"
    hkmonologue "With the time I'll have, I'll be able to catch up on my backlog and learn more in the process!"

    # SUBTRACT FROM MAG NUM AND TURN BOOLEAN TRUE
    if (isMagGlassTwoSeen == "false"):
        $ isMagGlassTwoSeen = "true"
        $ magGlassNum  = magGlassNum - 1

    # CHECK TO SEE IF MAG GLASS NUM IS AT 0 OR CAUSE THEM TO CONTINUE UI INTERACTION 
    if (magGlassNum == 0):
        jump scene2_3_Post_Investigation
    else:
        call screen hisakoRoom

# 3. INTERIOR DIALOGUE
label interior_dialogue():
    hkmonologue "Marbled walls."
    hkmonologue "Mahogany staircase."
    hkmonologue "All accompanied by inported luxury furniture..."
    hkmonologue "There's no way I could have afforded any of this as a paralegal!"
    hkmonologue "I guess the Academy wants the best for its students, so that they can perform at their best."
    hkmonologue "I'm definitely going to make sure I take advantage of such commodities and comforts!"

    # SUBTRACT FROM MAG NUM AND TURN BOOLEAN TRUE
    if (isMagGlassThreeSeen == "false"):
        $ isMagGlassThreeSeen = "true"
        $ magGlassNum  = magGlassNum - 1

    # CHECK TO SEE IF MAG GLASS NUM IS AT 0 OR CAUSE THEM TO CONTINUE UI INTERACTION 
    if (magGlassNum == 0):
        jump scene2_3_Post_Investigation
    else:
        call screen hisakoRoom

# 4. BED DIALOGUE
label bed_dialogue():
    hkmonologue "A bed fit for a king...or a queen, as in my case!"
    hkmonologue "Get it? Because I'd be a queen if I were a ruler, and the bed...also queen-size?"
    hkmonologue "Heh Heh Heh...."
    hkmonologue "... ... ..."
    hkmonologue "That was such a corny ahh joke, Hisako."
    hkmonologue "You're so lucky that we're not trying out for {color=#efcc00}{b}Ultimate{/b}{/color} Comedian..."

    # SUBTRACT FROM MAG NUM AND TURN BOOLEAN TRUE
    if (isMagGlassFourSeen == "false"):
        $ isMagGlassFourSeen = "true"
        $ magGlassNum  = magGlassNum - 1

    # CHECK TO SEE IF MAG GLASS NUM IS AT 0 OR CAUSE THEM TO CONTINUE UI INTERACTION 
    if (magGlassNum == 0):
        jump scene2_3_Post_Investigation
    else:
        call screen hisakoRoom
    
