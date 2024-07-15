# INVESTIGATION SCREENS FOR PROLOGUE 

# 1. PROLOGUE: HISAKO'S ROOM 
screen hisakoRoom():

    # MAG FOR THE SHOWER
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 350
        ypos 350         
        idle "mag_glass_idle" action Function(renpy.call, "shower_dialogue")
        hover "mag_glass_hover" hovered Play("sound", mag_hover_sfx)     

    # MAG FOR THE DESK
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 425
        ypos 950         
        idle "mag_glass_idle" action Function(renpy.call, "desk_dialogue")
        hover "mag_glass_hover" hovered Play("sound", mag_hover_sfx)      
        

    # MAG FOR THE INTERIOR
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 1500
        ypos 375         
        idle "mag_glass_idle" action Function(renpy.call, "interior_dialogue")
        hover "mag_glass_hover" hovered Play("sound", mag_hover_sfx)     
        