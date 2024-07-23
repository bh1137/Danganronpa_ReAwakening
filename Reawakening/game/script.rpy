# The game starts here.
label start:
    # 3D CAMERA PERSPECTIVE (VISUAL NOVEL DESIGN YOUTUBE)
    camera:
        perspective True
        
    # START THE GAME      
    # ATTEMPT TO JUMP PART 1 SCRIPT 
    jump scene2_4    
   
    label saveGamePrologueOne:
        # SAVE PROMPT FOR PART 1 (FOUND FROM https://lemmasoft.renai.us/forums/viewtopic.php?t=50298)
        call screen confirm("Do you want to save?", yes_action=[ShowMenu('save'), Return()], no_action=Return())  

        # ATTEMPT TO JUMP TO PART 2 SCRIPT
        jump scene2_1
  

    
    # CODING INFORMATION AND STATISTICS 
    # PART I --> TRANSCRIBING THE SCRIPT TO THE CODE [11/15/23 - 12/18/23]
    # PART II --> CODING MUSIC, SFX, AND BACKGROUNDS PART I [12/25/23 - 3/20/24]
    # PART III --> FIXING UP CHARACTER SPRITES AND FINISHING UP PROLOGUE PART I AND STARTING PROLOGUE PART II [5/6/2024 - 5/16/2024]
        
 

   
    # This ends the game.
    return


