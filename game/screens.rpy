################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Image("gui/textbox/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign 2
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos 500
    xsize 1200
    ypos 75

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():
    #zorder 100  # Ensure it appears above most screens

    if quick_menu:
        imagemap:
            ground "gui/textbox/textbox_idle.png"
            hover "gui/textbox/textbox_hover.png"

            # Align the entire quick menu to the bottom center
            xpos 0.5
            ypos 1.0
            xanchor 0.5
            yanchor 1.0

            # Buttons for quick menu actions
            hotspot (1245, 767, 83, 84) action Preference("auto-forward", "toggle") hovered [ Play("sound" , "audio/hover.wav") ] # Back
            #hotspot (210, 1020, 150, 60) action ShowMenu('history')  # History
            hotspot (1353, 767, 87, 85) action Skip() alternate Skip(fast=True, confirm=True) hovered [ Play("sound" , "audio/hover.wav") ] # Skip
            #hotspot (530, 1020, 150, 60) action Preference("auto-forward", "toggle")  # Auto
            hotspot (1721, 940, 85, 85) action QuickSave()  hovered [ Play("sound" , "audio/hover.wav") ]
            hotspot (1724, 833, 81, 84) action Rollback() hovered [ Play("sound" , "audio/hover.wav") ] # Quick Save
            hotspot (1577, 767, 83, 85) action MainMenu() hovered [ Play("sound" , "audio/hover.wav") ] # Main Menu
            hotspot (1461, 764, 88, 88) action ShowMenu('preferences') hovered [ Play("sound" , "audio/hover.wav") ] # Preferences

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    fixed:
        style_prefix "navigation"

        #xpos gui.navigation_xpos
        #yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            # textbutton _("Start") action Start()
            imagebutton auto "gui/buttons/maglaro_%s.png" focus_mask True action Start() hovered [ Play("sound" , "audio/hover.wav") ]
        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        #textbutton _("Load") action ShowMenu("load")
        imagebutton auto "gui/buttons/load_%s.png" focus_mask True action ShowMenu("load") hovered [ Play("sound" , "audio/hover.wav") ]

        #textbutton _("Preferences") action ShowMenu("preferences")
        imagebutton auto "gui/buttons/opsyon_%s.png" focus_mask True action ShowMenu("preferences") hovered [ Play("sound" , "audio/hover.wav") ]

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        #textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            #textbutton _("Help") action ShowMenu("help")
            imagebutton auto "gui/buttons/gabay_%s.png" focus_mask True action ShowMenu("help") hovered [ Play("sound" , "audio/hover.wav") ]

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            #textbutton _("Quit") action Quit(confirm=not main_menu)
            imagebutton auto "gui/buttons/quit_%s.png" focus_mask True action Quit(confirm=not main_menu) hovered [ Play("sound" , "audio/hover.wav") ]


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

screen navigation2():
    
    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")

## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation2

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu
    style_prefix "about"
    imagemap:
        ground 'gui/abouthistory/menu_idle.png'
        idle 'gui/abouthistory/menu_idle.png'
        hover 'gui/abouthistory/menu_hover.png'
        selected_idle 'gui/abouthistory/menu_hover.png'
        selected_hover 'gui/abouthistory/menu_hover.png'
        cache False

        hotspot (85, 263, 233, 90) action ShowMenu('history')  hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (1584, 245, 239, 91) action ShowMenu('about') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (1584, 411, 242, 98) action ShowMenu('help') hovered [ Play("sound" , "audio/hover.wav") ]

        hotspot (75, 613, 246, 88) action ShowMenu('preferences') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (75, 483, 257, 91) action ShowMenu('load') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (82, 366, 265, 90) action ShowMenu('save') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (1584, 537, 254, 91) action MainMenu() hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (1601, 698, 229, 96) action Quit() hovered [ Play("sound" , "audio/hover.wav") ]

        hotspot (1448, 183, 64, 65) action Return() hovered [ Play("sound" , "audio/hover.wav") ]

    vbox:
        xpos 0.25
        ypos 0.23
        xmaximum 400
        text _("We do not claim ownership of most of the materials used in this app. All rights are reserved by their respective owners. This app is solely intended for research and educational purposes.\n ")


    vbox:
        xpos 0.55
        ypos 0.23
        xmaximum 400
        text _("Credits:\n-{a=https://incompetech.filmmusic.io/song/4371-skye-cuillin/}Skye Cuillin{/a} by Kevin MacLeod\nLicense: {a=https://filmmusic.io/standard-license/}https://filmmusic.io/standard-license{/a}")
        text _("\n-{a=https://incompetech.filmmusic.io/song/4467-teller-of-the-tales/}Teller of tales{/a} by Kevin MacLeod\nLicense: {a=https://filmmusic.io/standard-license/}https://filmmusic.io/standard-license{/a}")

        text _("\nBase template created by Skolaztika | Art by Lyra Oleta")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen load_save_slot:
    $ file_text = "% s\n  %s" % (FileTime(number, empty="Empty Slot"), FileSaveName(number))
    add FileScreenshot(number) xpos -1 ypos 0
    text file_text xpos 11 ypos -20 size 15  color "#000000"

screen load:

    tag menu

    imagemap:
        ground 'gui/SaveLoad/saveload_ground.png'
        idle 'gui/SaveLoad/saveload_idle.png'
        hover 'gui/SaveLoad/saveload_hover.png'
        selected_idle 'gui/SaveLoad/saveload_selected.png'
        selected_hover 'gui/SaveLoad/saveload_hover.png'
        cache False

        hotspot (458, 204, 47, 48) action FilePage(1) hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (531, 204, 48, 48) action FilePage(2) hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (606, 204, 45, 48) action FilePage(3) hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (679, 204, 47, 48) action FilePage(4) hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (753, 204, 47, 48) action FilePage(5) hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (827, 204, 47, 48) action FilePage(6) hovered [ Play("sound" , "audio/hover.wav") ]

        ## You might get confused but these one below are the save/load slots, those boxes.
        hotspot (468, 312, 393, 207) action FileAction(1) hovered [ Play("sound" , "audio/hover.wav") ]:
            use load_save_slot(number=1)
        hotspot (468, 620, 393, 207) action FileAction(2) hovered [ Play("sound" , "audio/hover.wav") ]:
            use load_save_slot(number=2)
        hotspot (1055, 312, 393, 207) action FileAction(3) hovered [ Play("sound" , "audio/hover.wav") ]:
            use load_save_slot(number=3)
        hotspot (1055, 620, 393, 207) action FileAction(4) hovered [ Play("sound" , "audio/hover.wav") ]:
            use load_save_slot(number=4)


        hotspot (85, 263, 233, 90) action ShowMenu('history') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (1584, 245, 239, 91) action ShowMenu('about') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (1584, 411, 242, 98) action ShowMenu('help') hovered [ Play("sound" , "audio/hover.wav") ]

        hotspot (75, 613, 246, 88) action ShowMenu('preferences') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (75, 483, 257, 91) action ShowMenu('load') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (82, 366, 265, 90) action ShowMenu('save') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (1584, 537, 254, 91) action MainMenu() hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (1601, 698, 229, 96) action Quit() hovered [ Play("sound" , "audio/hover.wav") ]


        hotspot (1448, 183, 64, 65) action Return() hovered [ Play("sound" , "audio/hover.wav") ]



screen save:

    tag menu

    imagemap:
        ground 'gui/SaveLoad/saveload_ground.png'
        idle 'gui/SaveLoad/saveload_idle.png'
        hover 'gui/SaveLoad/saveload_hover.png'
        selected_idle 'gui/SaveLoad/saveload_selected.png'
        selected_hover 'gui/SaveLoad/saveload_hover.png'
        cache False

        hotspot (458, 204, 47, 48) action FilePage(1) hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (531, 204, 48, 48) action FilePage(2) hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (606, 204, 45, 48) action FilePage(3) hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (679, 204, 47, 48) action FilePage(4) hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (753, 204, 47, 48) action FilePage(5) hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (827, 204, 47, 48) action FilePage(6) hovered [ Play("sound" , "audio/hover.wav") ]

        ## You might get confused but these one below are the save/load slots, those boxes.
        hotspot (468, 312, 393, 207) action FileAction(1) hovered [ Play("sound" , "audio/hover.wav") ]:
            use load_save_slot(number=1)
        hotspot (468, 620, 393, 207) action FileAction(2) hovered [ Play("sound" , "audio/hover.wav") ]:
            use load_save_slot(number=2)
        hotspot (1055, 312, 393, 207) action FileAction(3) hovered [ Play("sound" , "audio/hover.wav") ]:
            use load_save_slot(number=3)
        hotspot (1055, 620, 393, 207) action FileAction(4) hovered [ Play("sound" , "audio/hover.wav") ]:
            use load_save_slot(number=4)



        hotspot (85, 263, 233, 90) action ShowMenu('history') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (1584, 245, 239, 91) action ShowMenu('about') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (1584, 411, 242, 98) action ShowMenu('help') hovered [ Play("sound" , "audio/hover.wav") ]

        hotspot (75, 613, 246, 88) action ShowMenu('preferences') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (75, 483, 257, 91) action ShowMenu('load') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (82, 366, 265, 90) action ShowMenu('save') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (1584, 537, 254, 91) action MainMenu() hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (1601, 698, 229, 96) action Quit() hovered [ Play("sound" , "audio/hover.wav") ]

        hotspot (1448, 183, 64, 65) action Return() hovered [ Play("sound" , "audio/hover.wav") ]

init python:
    config.thumbnail_width = 393
    config.thumbnail_height = 207


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    imagemap:
        ground 'gui/Config/config_ground.png'
        idle 'gui/Config/config_idle.png'
        hover 'gui/Config/config_hover.png'
        selected_idle 'gui/Config/config_sidle.png'
        selected_hover 'gui/Config/config_shover.png'
        cache False

        ## DISPLAY
        hotspot (541, 274, 236, 66) action Preference('display', 'fullscreen') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (539, 346, 211, 78) action Preference('display', 'window') hovered [ Play("sound" , "audio/hover.wav") ]

        ## SKIP
        hotspot (544, 497, 257, 74) action Preference('skip', 'seen') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (545, 574, 149, 70) action Preference('skip', 'all') hovered [ Play("sound" , "audio/hover.wav") ]

        ## AFTER CHOICES
        hotspot (544, 712, 397, 76) action Preference('after choices', 'skip') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (544, 781, 132, 79) action Preference('after choices', 'stop') hovered [ Play("sound" , "audio/hover.wav") ]



        hotbar (1034, 273, 406, 73) value Preference('text speed') 
        hotbar (1026, 443, 422, 83) value Preference('music volume')
        hotbar (1032, 627, 408, 65) value Preference('sound volume') 
        hotbar (1036, 803, 410, 67) value Preference('auto-forward time') 


        hotspot (85, 263, 233, 90) action ShowMenu('history') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (1584, 245, 239, 91) action ShowMenu('about') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (1584, 411, 242, 98) action ShowMenu('help') hovered [ Play("sound" , "audio/hover.wav") ]

        hotspot (75, 613, 246, 88) action ShowMenu('preferences') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (75, 483, 257, 91) action ShowMenu('load') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (82, 366, 265, 90) action ShowMenu('save') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (1584, 537, 254, 91) action MainMenu() hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (1601, 698, 229, 96) action Quit() hovered [ Play("sound" , "audio/hover.wav") ]

        hotspot (1448, 183, 64, 65) action Return() hovered [ Play("sound" , "audio/hover.wav") ]



## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu
    #add "gui/abouthistory/menu_idle.png" xalign 0.5 yalign 0.5
    ## Avoid predicting this screen, as it can be very large.
    predict False
    style_prefix "history"
    imagemap:
        ground 'gui/abouthistory/menu_idle.png'
        idle 'gui/abouthistory/menu_idle.png'
        hover 'gui/abouthistory/menu_hover.png'
        selected_idle 'gui/abouthistory/menu_hover.png'
        selected_hover 'gui/abouthistory/menu_hover.png'
        cache False

        hotspot (85, 263, 233, 90) action ShowMenu('history')  hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (1584, 245, 239, 91) action ShowMenu('about') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (1584, 411, 242, 98) action ShowMenu('help') hovered [ Play("sound" , "audio/hover.wav") ]

        hotspot (75, 613, 246, 88) action ShowMenu('preferences') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (75, 483, 257, 91) action ShowMenu('load') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (82, 366, 265, 90) action ShowMenu('save') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (1584, 537, 254, 91) action MainMenu() hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (1601, 698, 229, 96) action Quit() hovered [ Play("sound" , "audio/hover.wav") ]

        hotspot (1448, 183, 64, 65) action Return() hovered [ Play("sound" , "audio/hover.wav") ]
    vbox:
        xalign 0.3
        ypos 250
        viewport id "vpgrid":
            yinitial 1.0
            #draggable True
            mousewheel True
            xmaximum 500
            ymaximum 620
            yfill True
            vbox:

                for h in _history_list:

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what:
                        substitute False

                    if h.who:
                        text "— " + h.who xalign 1.0 text_align 1.0
                    add "gui/abouthistory/divider.png" xalign 0.5
                if not _history_list:
                    label _("The dialogue history is empty.")






## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu
    imagemap:
        ground 'gui/abouthistory/menu_idle.png'
        idle 'gui/abouthistory/menu_idle.png'
        hover 'gui/abouthistory/menu_hover.png'
        selected_idle 'gui/abouthistory/menu_hover.png'
        selected_hover 'gui/abouthistory/menu_hover.png'
        cache False

        hotspot (85, 263, 233, 90) action ShowMenu('history') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (1584, 245, 239, 91) action ShowMenu('about') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (1584, 411, 242, 98) action ShowMenu('help') hovered [ Play("sound" , "audio/hover.wav") ]

        hotspot (75, 613, 246, 88) action ShowMenu('preferences') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (75, 483, 257, 91) action ShowMenu('load') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (82, 366, 265, 90) action ShowMenu('save') hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (1584, 537, 254, 91) action MainMenu() hovered [ Play("sound" , "audio/hover.wav") ]
        hotspot (1601, 698, 229, 96) action Quit() hovered [ Play("sound" , "audio/hover.wav") ]

        hotspot (1448, 183, 64, 65) action Return() hovered [ Play("sound" , "audio/hover.wav") ]
    style_prefix "help"
    default device = "keyboard"

    fixed:


        fixed:
            imagebutton auto "gui/HelpButtons/keyboard_%s.png" xpos 472 ypos 176 focus_mask True action SetScreenVariable("device", "keyboard")  hovered [ Play("sound" , "audio/hover.wav") ]
            imagebutton auto "gui/HelpButtons/mouse_%s.png" xpos 700 ypos 176 focus_mask True action SetScreenVariable("device", "mouse")  hovered [ Play("sound" , "audio/hover.wav") ]

            if GamepadExists():
                imagebutton auto "gui/HelpButtons/gamepad_%s.png" xpos 1022 ypos 176 focus_mask True action SetScreenVariable("device", "gamepad") hovered [ Play("sound" , "audio/hover.wav") ]

        if device == "keyboard":
            use keyboard_help
        elif device == "mouse":
            use mouse_help
        elif device == "gamepad":
            use gamepad_help



screen keyboard_help():
    vbox:
        xpos 0.22
        ypos 0.23
        xmaximum 450
        vbox:
            label _("Enter")
            text _("Advances dialogue and activates the interface.")
        vbox:
            label _("Space")
            text _("Advances dialogue without selecting choices.")
        vbox:
            label _("Escape")
            text _("Accesses the game menu.")
        vbox:
            label _("Ctrl")
            text _("Skips dialogue while held down.")
        vbox:
            label _("Tab")
            text _("Toggles dialogue skipping.")




    vbox:
        xpos 0.55
        ypos 0.23
        xmaximum 450
        vbox:
            label _("Page Up")
            text _("Rolls back to earlier dialogue.")
        vbox:
            label _("Page Down")
            text _("Rolls forward to later dialogue.")
        vbox:
            label "H"
            text _("Hides the user interface.")
        vbox:
            label "S"
            text _("Takes a screenshot.")
        vbox:
            label "V"
            text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():
    vbox:
        xpos 0.22
        ypos 0.23
        xmaximum 450
        vbox:
            label _("Left Click")
            text _("Advances dialogue and activates the interface.")
        vbox:
            label _("Middle Click")
            text _("Hides the user interface.")
        vbox:
            label _("Right Click")
            text _("Accesses the game menu.")
        vbox:
             label _("Mouse Wheel Up\nClick Rollback Side")
             text _("Rolls back to earlier dialogue.")
        vbox:
            label _("Mouse Wheel Down")
            text _("Rolls forward to later dialogue.")

screen gamepad_help():
    vbox:
        xpos 0.22
        ypos 0.23
        xmaximum 450
        vbox:
            label _("Right Trigger\nA/Bottom Button")
            text _("Advances dialogue and activates the interface.")
        vbox:
            label _("Left Trigger\nLeft Shoulder")
            text _("Rolls back to earlier dialogue.")
        vbox:
            label _("Right Shoulder")
            text _("Rolls forward to later dialogue.")
        vbox:
            label _("D-Pad, Sticks")
            text _("Navigate the interface.")
        vbox:
            label _("Start, Guide")
            text _("Accesses the game menu.")



    vbox:
        xpos 0.55
        ypos 0.23
        xmaximum 450
        vbox:
            label _("Y/Top Button")
            text _("Hides the user interface.")
        textbutton _("Calibrate") action GamepadCalibrate()


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size 11



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action  hovered [ Play("sound" , "audio/hover.wav") ]
                textbutton _("No") action no_action hovered [ Play("sound" , "audio/hover.wav") ]

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
