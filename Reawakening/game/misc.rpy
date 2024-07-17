# BUTTON FOR INVESTIGATE, TALK, AND MOVE LIKE PHOENIX WRIGHT 
screen investigation(isPersonInRoom, canIMove):
    # BACKGROUND
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.50
        ypos 0.95            
        idle "investigation_background"
   
    # INVESTIGATE BUTTON
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.25
        ypos 0.85      
        idle "investigate_idle" action Play("sound", menu_click_sfx), Function(renpy.call, "investigate_room")
        hover "investigate_hover" hovered Play("sound", menu_hover_sfx)
                        

    # TALK BUTTON
    if(isPersonInRoom == 1):
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.50
            ypos 0.85      
            idle "talk_idle" action Play("sound", menu_click_sfx), Function(renpy.call, "talk_room")
            hover "talk_hover" hovered Play("sound", menu_hover_sfx)
                        

    # MOVE BUTTON 
    if(canIMove == 1):
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.75
            ypos 0.85      
            idle "move_idle" action Play("sound", menu_click_sfx), Function(renpy.call, "move_room")
            hover "move_hover" hovered Play("sound", menu_hover_sfx)
                        

    




    

# WHAT I WILL PROBABLY DO IS SOME SORT OF PHOENIX WRIGHT MOMENT WHERE THE PLAYER CAN MOVE THEIR CURSOR ACROSS THE SCREEN 
# IN ORDER TO FIND SOME HIDDEN GEMS ABOUT THE ROOM. ALSO HAVE A QUICK TUTORIAL MOMENT TO GET THE PLAYERS TO FAMILIARIZE THEMSELVES
# WITH SEARCHING AROUND 7-1-24 9:56PM

label investigate_room:  
    # SWITCH CASE
    if (sceneRoom == "prologue_hisakoRoom"):             
        # CALL SCREEN 
        call screen hisakoRoom()



    $ ui.interact()

label talk_room:
    $ ui.interact()

label move_room:
    $ ui.interact()



         