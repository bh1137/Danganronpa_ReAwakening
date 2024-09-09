# CALLBACKS 
init python:
    # TEXT SFX 
    def text_sfx(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "begin":
            renpy.sound.play("audio/sfx/text.ogg")
        elif event == "slow_done":
            renpy.sound.stop()

    # MAKING SFX CHANNEL 
    renpy.music.register_channel("sfx_channel", "sound")
    renpy.music.register_channel("character_voice", "sound")





# SONGS 
define lets_party = "audio/music/lets_party.mp3"
define beyond_the_funk = "audio/music/beyond_the_funk.mp3"
define watch_ur_behavior = "audio/music/watch_ur_behavior.mp3"
define new_fonky_step = "audio/music/new_fonky_step.mp3"
define fantastic_beat_remix = "audio/music/fantastic_beat_remix.mp3"
define high_school_snaps = "audio/music/high_school_snaps.mp3"
define laid_back = "audio/music/laid_back.mp3"
define transfixion  = "audio/music/transfixion/mp3"
define bell_pepper_beef = "audio/music/bell_pepper_beef.mp3"
define harpsichord_fuge = "audio/music/harpsichord_fuge.mp3"
define governor_minuet = "audio/music/governor_minuet.mp3"
define perdue2 = "audio/music/perdue_2.mp3"
define calm_seas = "audio/music/on_calm_sea.mp3"
define funkman = "audio/music/funkman.mp3"
define sundowner = "audio/music/sundowner.mp3"
define day_dreams = "audio/music/day_dreams.mp3"
define small_town_pluto = "audio/music/small_town_pluto.mp3"
define cubicat = "audio/music/cubicat.mp3"
define hot_pursuit = "audio/music/hot_pursuit_percussionless.mp3"
define boomerang = "audio/music/boomerang.mp3"
define hope_vs_despair ="audio/music/hope_vs_despair.mp3"
# SOUND EFFECTS 
define dizzy_sfx = "audio/sfx/dizzy.ogg"
define fireplace = "audio/sfx/crackle.ogg"
define running = "audio/sfx/run.ogg"
define school_bell = "audio/sfx/bell.ogg"
define exclamation = "audio/sfx/exclamation.ogg"
define card_intro_shine = "audio/sfx/card_intro.ogg"
define stern_sfx = "audio/sfx/stern.ogg"
define thunder_sfx = "audio/sfx/thunder.ogg"
define walking = "audio/sfx/walk.ogg"
define disappointment_sfx  = "audio/sfx/disappointed.ogg"
define faint_sfx = "audio/sfx/faint.ogg"
define fanfare_sfx = "audio/sfx/fanfare.ogg"
define double_walk_sfx = "audio/sfx/double_walk.ogg"
define damage_sfx = "audio/sfx/damage.ogg"
define ice_cube_sfx = "audio/sfx/ice_cube.ogg"
define mag_hover_sfx = "audio/sfx/mag_hover.ogg"
define mag_click_sfx = "audio/sfx/mag_click.ogg"
define menu_hover_sfx = "audio/sfx/menu_hover.ogg"
define menu_click_sfx = "audio/sfx/menu_click.ogg"
define knocking_sfx = "audio/sfx/knock.ogg"
define eating_sfx = "audio/sfx/eating.ogg"
define drinking_sfx = "audio/sfx/drinking_ajauk.ogg"
define shocked_sfx = "audio/sfx/shocked.ogg"
define hotel_bell = "audio/sfx/hotel_bell.ogg"
define scuttle_shuffle = "audio/sfx/shuffle.ogg"
define stunned = "audio/sfx/stunned.ogg"
define feedback = "audio/sfx/feedback.ogg"
define tinnitus = "audio/sfx/tinnitus.ogg"
define dark_guitar = "audio/sfx/dark_guitar.ogg"
define wind = "audio/sfx/wind.ogg"