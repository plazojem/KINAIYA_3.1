# The script of the game goes in this file.
#Images go here
image a ="databaes.png"
image b ="kinaiya1.png"
# Declare characters used by this game. The color argument colorizes the
# name of the character.
label splashscreen:
    scene black
    pause 1.0 
    show a at top with fade
    pause 1.0
    hide a with dissolve

    scene black
    pause 1.0 
    show b at top with fade
    pause 1.0
    hide b with dissolve
    return
    

#Declare music
define audio.gamemusic = "audio/game_music.mp3"
define config.main_menu_music = "audio/main_menu.mp3"
define config.game_menu_music = "audio/main_menu.mp3"

#Define Characters:

#Story 1
define m = Character("Mila", image= "mila")
define s = Character("Shadow")
define c = Character("Chabs")
define n = Character("Nanay")
define t = Character("Matandang Aso")
define p1 = Character("Pusa 1")
define p2 = Character("Pusa 2")
define a1 = Character("Aso 1")
define a2 = Character("Aso 2")



#Story 2
define d = Character("Adrielle")
define j = Character("Lola Jiji")
define f = Character("Fiona")
define e = Character("Jane")
define k = Character("Kuya Gong")
define p1 = Character("Pusa 1")
define p2 = Character("Pusa 2")
define t = Character("Dot")

#Story 3
define i = Character("Isra")
define l = Character("Lala")
define b1 = Character("Batang Lalaki 1")
define b2 = Character("Batang Lalaki 2")    
define a = Character("Ahas")

#Declare image :

#Story 1:
image calm_mila:
    "storyonemila/calm_mila.png" 
    zoom 0.25
image curious_mila:
    "storyonemila/curious_mila.png"
    zoom 0.25
image happy_mila:
    "storyonemila/happy_mila.png"
    zoom 0.25
image scared_mila:
    "storyonemila/scared_mila.png"
    zoom 0.25
image mother_mila:
    "storyonemila/mother_mila.png"
    zoom 0.25
image mila_sitting:
    "storyonemila/mila_sitting.png"
    zoom 0.25
image mila_standing:
    "storyonemila/mila_standing.png"
    zoom 0.25
image standing_shadow:
    "storyonemila/standing_shadow.png"
    zoom 0.25
image sitting_shadow:
    "storyonemila/sitting_shadow.png"
    zoom 0.25
image galang_aso1:
    "storyonemila/galang_aso1.png"
    zoom 0.25
image galang_aso2:
    "storyonemila/galang_aso2.png"
    zoom 0.25
image galang_aso2:
    "storyonemila/galang_aso2.png"
    zoom 0.25
image chabs_sitting:
    "storyonemila/chabs_sitting.png"
    zoom 0.25
image chabs_standing:
    "storyonemila/chabs_standing.png"
    zoom 0.25



#Story 2:
image calm_adi:
    "storytwo/calm_adi.png" 
    zoom 0.25
image curious_adi:
    "storytwo/curious_adi.png"
    zoom 0.25
image happy_adi:
    "storytwo/happy_adi.png"
    zoom 0.25
image scared_adi:
    "storytwo/scared_adi.png"
    zoom 0.25
image happy_lolajiji:
    "storytwo/happy_lolajiji.png"
    zoom 0.25
image happy_kuyagong:
    "storytwo/happy_kuyagong.png"
    zoom 0.25
image calm_lolajiji:
    "storytwo/calm_lolajiji.png"
    zoom 0.25
image sad_lolajiji:
    "storytwo/sad_lolajiji.png"
    zoom 0.25
image kuya_gong:
    "storytwo/kuya_gong.png"
    zoom 0.25

#Story 3:
image Calm Isra:
    "story 3/Calm Isra.png"
    zoom 0.25
image Curious Isra:
    "story 3/Curious Isra.png"
    zoom 0.25
image Happy Isra:
    "story 3/Happy Isra.png"
    zoom 0.25
image Scared Isra:
    "story 3/Scared Isra.png"
    zoom 0.25
image Angry Ahas:
    "story 3/Angry Ahas.png"
    zoom 0.25
image Sad Ahas:
    "story 3/Sad Ahas.png"
    zoom 0.25
image Calm Ahas:
    "story 3/Calm Ahas.png"
    zoom 0.25
image Happy Batang Lalaki 1:
    "story 3/Happy Batang Lalaki 1.png"
    zoom 0.25
image Angry Batang Lalaki 1:
    "story 3/Angry Batang Lalaki 1.png"
    zoom 0.25
image Angry Batang Lalaki 2:
    "story 3/Angry Batang Lalaki 2.png"
    zoom 0.25
image Calm Batang Lalaki 1:
    "story 3/Calm Batang Lalaki 1.png"
    zoom 0.25
image Calm Batang Lalaki 2:
    "story 3/Calm Batang Lalaki 2.png"
    zoom 0.25
image Happy Batang Lalaki 2:
    "story 3/Calm Batang Lalaki 2.png"
    zoom 0.25
image Scared Batang Lalaki 1:
    "story 3/Scared Batang Lalaki 1.png"
    zoom 0.25
image Scared Batang Lalaki 2:
    "story 3/Scared Batang Lalaki 2.png"
    zoom 0.25
image Lala Sitting:
    "story 3/Lala Sitting.png"
    zoom 0.25
image Lala Standing:
    "story 3/Lala Standing.png"
    zoom 0.25

#Define Positioning
transform slightleft:
    xalign 0.25
    yalign 1.0

transform center:
    xalign 0.5
    yalign 1.0

transform slightright:
    xalign 0.75
    yalign 1.0

transform left:
    xalign 0.0
    yalign 1.0

transform right:
    xalign 1.0
    yalign 1.0

transform rightish:
    xalign 1.10
    yalign 1.0

transform rights:
    xalign 1.20
    yalign 1.0

# transform
transform darken:
    matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
    linear 0.5 matrixcolor TintMatrix("#4e4e4e") * SaturationMatrix(1.0)

transform lighten:
    linear 0.5 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)


# The game starts here.

label start:


    play music gamemusic volume 0.2
    
    $ quick_menu = False
    scene black
    pause 1.0 
    show splash1 at top with fade
    voice "title/title1.mp3"
    pause 
    hide splash1 with dissolve
    $ quick_menu = True
    stop voice

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg bedroom
    with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show curious_mila at center, lighten with dissolve 
    # These display lines of dialogue.

    voice "mila/mila_1.mp3"
    m "Hay, ang saya siguro maligo sa ulan..."


    voice "mila/mila_2.mp3"
    m "Mabuti pa ang mga aso, puwedeng lumabas kahit umuulan. Ang nanay ko, hindi man lang ako pinayagang maligo sa ulan."

    show scared_mila at center, lighten with dissolve
    voice "mila/mila_3.mp3"
    m "Ayy!"


    jump scene_2

label scene_2:

    scene bg house
    with dissolve

    show mila_sitting at left, lighten with dissolve 
    voice "mila/mila_4.mp3"
    m "H-Ha?! Anong nangyari? Bakit ako nasa labas?"

    voice "mila/mila_5.mp3"
    m "EHHHHH?! Bakit ako may apat na paa?!"

    show mila_sitting at left, darken  with dissolve
    show standing_shadow at right, lighten with dissolve
    voice "shadow/line1.mp3"
    s "Oh! Isa ka ring aso? Kamusta? Ako si Shadow!"

    show standing_shadow at right, darken with dissolve
    show chabs_sitting at center, lighten with dissolve
    voice "chabs/line1.mp3"
    c "Ako naman si Chabelitos, pero puwede mo akong tawaging Chabs!"

    show chabs_sitting at center, darken with dissolve
    show standing_shadow at right, lighten with dissolve
    voice "shadow/line2.mp3"
    s "Ikaw? Anong pangalan mo?"

    show standing_shadow at right, darken with dissolve
    show mila_sitting at left, lighten with dissolve
    voice "mila/mila_6.mp3"
    m "Ako? Aking... aking pangalan..."

    voice "mila/mila_7.mp3"
    m "H-Ha? Ano nga ulit ang pangalan ko?"

    show mila_sitting at left, darken with dissolve
    show chabs_sitting at center, lighten with dissolve
    voice "chabs/line2.mp3"
    c "Hala! Nakalimutan mo ang pangalan mo?"

    show chabs_sitting at center, darken with dissolve
    show standing_shadow at right, lighten with dissolve
    voice "shadow/line3.mp3"
    s "Ano kaya ang nangyari sa’yo?"

    show standing_shadow at right, darken with dissolve
    show chabs_sitting at center, lighten with dissolve
    voice "chabs/line3.mp3"
    c "Diba, Ikaw si Mila?"

    show chabs_sitting at center, darken with dissolve 
    show standing_shadow at right, lighten with dissolve 
    voice "shadow/line4.mp3"
    s "Tama, lagi mong tinatawag ang sarili mong 'Mila' sa harap namin!"

    show standing_shadow at right, darken with dissolve
    show mila_sitting at left, lighten with dissolve
    voice "mila/mila_8.mp3"
    m "Pangalan? Ano ba ‘yun?"

    show mila_sitting at left, darken with dissolve
    show standing_shadow at right, lighten with dissolve
    voice "shadow/line5.mp3"
    s "Aba! Hindi mo alam kung ano ang pangalan?"

    show standing_shadow at right, darken with dissolve
    show chabs_sitting at center, lighten with dissolve
    voice "chabs/line4.mp3"
    c "Hmmm… Mukhang kailangan nating ipaliwanag ito nang mabuti."

    show chabs_sitting at center, darken with dissolve
    show standing_shadow at right, lighten with dissolve
    voice "shadow/line6.mp3"
    s "Tama ka d’yan, Chabs! Simulan natin sa pinakauna—ano nga ba ang pangalan? Pero bago tayo magsimula ipakikilala ka muna namin sa aming mundo!"

    jump scene_3


label scene_3:

    scene bg road 
    with dissolve

    show mila_standing at left, lighten with dissolve
    voice "mila/mila_9.mp3"
    m "Ang ganda pala ng mundo ng mga aso! Napakaraming bagay dito—mga puno, bahay, at mga ibang aso!"

    show mila_standing at left, darken with dissolve
    show sitting_shadow at right, lighten with dissolve
    voice "shadow/line7.mp3"
    s "Tama ka, Mila! Napansin mo ba ang mga sinabi mo? 'Puno,' 'bahay,' at 'aso'—ang mga ito ay pangngalan!"

    show sitting_shadow at right, darken with dissolve
    show chabs_sitting at center, lighten with dissolve
    voice "chabs/line5.mp3"
    c "Ang pangngalan ay mga salitang ginagamit upang pangalanan ang tao, hayop, lugar, bagay, o pangyayari!"

    show chabs_sitting at center, darken with dissolve
    show sitting_shadow at right, lighten with dissolve
    voice "shadow/line8.mp3"
    s "Halimbawa, ang 'bato' ay isang bagay. Ang 'ilog' ay isang lugar. At tayo—mga 'aso'—ay mga hayop"

    show sitting_shadow at right, darken with dissolve
    show mila_standing at left, lighten with dissolve
    voice "mila/mila_10.mp3"
    m "Ah! Ibig sabihin, ang pangalan ko, 'Mila', ay isang pangngalan din?"

    show mila_standing at left, darken with dissolve
    show chabs_sitting at center, lighten with dissolve
    voice "chabs/line6.mp3"
    c "Tama! Ang pangalan ng isang tao, hayop, o lugar ay pangngalang pantangi!"

    hide mila_standing with dissolve
    hide sitting_shadow with dissolve
    jump prompt_1


label prompt_1:

    show chabs_sitting at center
    with dissolve

    voice "chabsprompt/q1.mp3"
    c "Ano ang pangngalan sa pangungusap na ito?\n'Si Mila ay naglalakad kasama sina Shadow at Chabs.'"
    
    menu:
        c "Ano ang pangngalan sa pangungusap na ito?\n'Si Mila ay naglalakad kasama sina Shadow at Chabs.'"
        "Naglalakad":
            voice "chabsprompt/w2.mp3"
            c "Hmm… ang 'naglalakad' ay hindi isang pangngalan. Ano kaya ang tamang sagot?"
            jump prompt_1

        "Mila, Shadow, Chabs":
            voice "chabsprompt/r1.mp3"
            c "Tama! Ang mga pangalang 'Mila,' 'Shadow,' at 'Chabs' ay pangngalan dahil ito ay pangalan ng mga tao o hayop!"
            jump scene_4

        "Kasama":
            voice "chabsprompt/w1.mp3"
            c "Hindi rin! Ang 'kasama' ay isang pang-ukol. Subukan ulit!"
            jump prompt_1
        
    

label scene_4:

    scene bg outside
    with dissolve

    show mila_standing at left with dissolve
    voice "mila/mila_11.mp3"
    m "Ang dami palang hayop dito sa labas... Dati, hindi ko sila napapansin!"

    show mila_standing at left, darken with dissolve
    show chabs_standing at right, lighten with dissolve
    voice "chabs/line7.mp3"
    c "Siyempre! Kapag aso ka, mas malapit ka sa kalikasan. Alam mo ba, marami kaming ugali na parang sa mga tao?"

    show chabs_standing at right, darken with dissolve
    show mila_standing at left, lighten with dissolve
    voice "mila/mila_12.mp3"
    m "Talaga? Tulad ng ano?"

    show mila_standing at left, darken with dissolve
    show sitting_shadow at center, lighten with dissolve
    voice "shadow/line9.mp3"
    s "Halimbawa, tulad ng tao, marunong din kaming rumespeto. May mga matatandang aso na dapat naming igalang."

    show sitting_shadow at center, darken with dissolve
    show mila_standing at left, lighten with dissolve
    voice "mila/mila_13.mp3"
    m "Parang pagsasabi ng 'po' at 'opo'?"

    show mila_standing at left, darken with dissolve
    show sitting_shadow at center, lighten with dissolve
    voice "shadow/line10.mp3"
    s "Ano iyon? Hindi namin alam 'yan."

    show sitting_shadow at center, darken with dissolve
    show mila_standing at left, lighten with dissolve
    voice "mila/mila_14.mp3"
    m "Sa mundo ng mga tao, natutunan namin ang paggamit ng 'po' at 'opo' bilang tanda ng paggalang, lalo na sa mga nakatatanda."

    show mila_standing at left, darken with dissolve
    show chabs_standing at right, lighten with dissolve
    voice "chabs/line8.mp3"
    c "Talaga? Paano ito ginagamit?"

    show chabs_standing at right, darken with dissolve
    show mila_standing at left, lighten with dissolve
    voice "mila/mila_15.mp3"
    m "Halimbawa, kapag kinakausap ko ang nanay ko, hindi ko lang sinasabi 'Salamat,' sinasabi ko rin, 'Salamat po!'"

    show mila_standing at left, darken with dissolve
    voice "tandang aso/line1.mp3"
    t "Ano itong naririnig ko tungkol sa 'po' at 'opo'?"

    show mila_standing at left, lighten with dissolve
    voice "mila/mila_16.mp3"
    m "Magandang araw po! Ipinapaliwanag ko lang po kung paano ito ginagamit bilang tanda ng paggalang."

    show mila_standing at left, darken with dissolve
    voice "tandang aso/line2.mp3"
    t "Hmm... Mukhang maganda 'yang kaugalian niyo. Sana matutunan din ng ibang aso rito."

    show mila_standing at left, darken with dissolve
    show sitting_shadow at center, lighten with dissolve
    voice "shadow/line11.mp3"
    s "Opo, susubukan po namin itong gamitin!"

    show sitting_shadow at center, darken with dissolve
    show chabs_standing at right, lighten with dissolve
    voice "chabs/line9.mp3"
    c "Tama po!"

    show chabs_standing at right, darken with dissolve
    show mila_standing at left, lighten with dissolve
    voice "mila/mila_17.mp3"
    m "Ayun! Ang paggamit ng 'po' at 'opo' ay nagdadagdag ng respeto sa ating pananalita."

    show mila_standing at left, darken with dissolve
    show chabs_standing at right, lighten with dissolve
    voice "chabs/line10.mp3"
    c "May mga paniniwala rin kami. Halimbawa, kapag kumakain kami, hindi dapat inaagaw ang pagkain ng iba!"

    show chabs_standing at right, darken with dissolve
    show mila_standing at left, lighten with dissolve
    voice "mila/mila_18.mp3"
    m "Ahh! May sarili rin pala kayong kultura!"

    voice "mila/mila_19.mp3"
    m "Shadow, Chabs, bakit parang may dalawang aso na nag-aaway?"

    show mila_standing at left, darken with dissolve
    show sitting_shadow at center, lighten with dissolve
    voice "shadow/line12.mp3"
    s "May ilang aso na hindi sumusunod sa aming paniniwala. Hindi namin gawi ang mag-away, pero minsan nangyayari ito."

    show sitting_shadow at center, darken with dissolve
    show chabs_standing at right, lighten with dissolve
    voice "chabs/line11.mp3"
    c "Tulad ng tao, may iba't ibang ugali rin ang aso. Ang ibang aso ay mabait, ang iba ay matulungin, at ang iba naman ay masayahin."

    show chabs_standing at right, darken with dissolve
    show sitting_shadow at center, lighten with dissolve
    voice "shadow/line13.mp3"
    s "Lahat ng bagay dito ay may pangalan. Mila, kaya mo bang pangalanan ang mga bagay na nakikita mo?" 

    hide chabs_standing with dissolve
    hide mila_standing with dissolve
    jump prompt_2

label prompt_2:

    voice "prompt evens/shadow_prompt2.mp3"
    s  "Alin sa mga ito ang pangngalan?"

    menu:
        s "Alin sa mga ito ang pangngalan?"
        "Masayahin":
            voice "prompt evens/shadow_wrong2A.mp3"
            m "Ang 'masayahin' ay isang pang-uri dahil ito ay naglalarawan ng isang katangian."
            jump prompt_2

        "Aso":
            voice "prompt evens/shadow_right2B.mp3"
            m "Tama! Ang 'aso' ay isang pangngalan dahil ito ay pangalan ng isang hayop!"
            jump scene_5

        "Mabilis":
            voice "prompt evens/shadow_wrong2C.mp3"
            m "Tama! Ang 'aso' ay isang pangngalan dahil ito ay pangalan ng isang hayop!"
            jump prompt_2


label scene_5:

    scene bg outside
    with dissolve

    show mila_standing at left, lighten with dissolve 
    voice "mila/mila_20.mp3"
    m "Ano ‘yun? Parang may kaguluhan..."

    show mila_standing at left, darken with dissolve
    show galang_aso1 at center, lighten with dissolve 
    voice "aso1/line1.mp3"
    a1 "Wala kayong puwang dito, mga pusa!"

    show galang_aso1 at center, darken with dissolve
    show galang_aso2 at right, lighten with dissolve 
    voice "aso2/line1.mp3"
    a2 "Tama! Dapat lang na umalis kayo!"

    show galang_aso2 at right, darken with dissolve
    voice "pusa 1/line1.mp3"
    p1 "W-Wala kaming ginagawang masama... naghahanap lang kami ng pagkain..."

    p2 "Hindi namin gustong manggulo..."

    show mila_standing at left, lighten with dissolve 
    voice "mila/mila_21.mp3"
    m "Teka lang! Hindi ito tama!"

    show mila_standing at left, darken with dissolve
    show galang_aso1 at center, lighten with dissolve
    voice "aso1/line2.mp3"
    a1 "Sino ka ba at bakit ka nakikialam?"

    show galang_aso1 at center, darken with dissolve
    show mila_standing at left, lighten with dissolve
    voice "mila/mila_22.mp3"
    m "Hindi natin gawi ang mang-api ng iba! Dapat natin silang igalang, kahit na iba sila sa atin."

    show mila_standing at left, darken with dissolve
    show galang_aso2 at right, lighten with dissolve
    voice "aso2/line2.mp3"
    a2 "Pero... hindi ba’t madalas tayong magtunggali?"

    show galang_aso2 at right, darken with dissolve
    show mila_standing at left, lighten with dissolve
    voice "mila/mila_23.mp3"
    m "Oo, pero hindi ibig sabihin na dapat natin silang apihin. Ang tunay na lakas ay nasa kabutihan, hindi sa pananakot."

    show mila_standing at left, darken with dissolve
    voice "pusa 1/line2.mp3"
    p1 "Salamat sa’yo! Kung hindi ka dumating, hindi namin alam ang gagawin."

    show mila_standing at left, lighten with dissolve
    voice "mila/mila_24.mp3"
    m "Walang anuman! Dapat nagtutulungan tayo."
    
    hide mila_standing with dissolve
    hide galang_aso1 with dissolve
    hide galang_aso2 with dissolve
    jump prompt_3


label prompt_3:

    show chabs_standing at center, with dissolve
    voice "chabsprompt/q2.mp3"
    c "Alin ang pangngalan sa pangungusap na ito?\n'Si Mila ay tumulong sa pusa.'"

    menu:
        c "Alin ang pangngalan sa pangungusap na ito?\n'Si Mila ay tumulong sa pusa.'"
        "Sa":
            voice "chabsprompt/3...mp3"
            c "Ang 'sa' ay isang pang-ukol. Subukan mong pumili ulit!"
            jump prompt_3

        "Tumulong":
            voice "chabsprompt/3..mp3"
            c "Ang 'tumulong' ay isang pandiwa. Ano kaya ang tamang sagot?"
            jump prompt_3

        "Mila, pusa":
            voice "chabsprompt/3....mp3"
            c "Tama! Ang 'Mila' at 'pusa' ay pangngalan dahil ito ay pangalan ng isang tao at hayop!"
            jump scene_6
        

    
        

label scene_6:

    scene bg room
    with dissolve

    show scared_mila at left, lighten with dissolve 
    voice "mila/mila_25.mp3"
    m "H-Ha? Nasaan ako?"

    show scared_mila at left, darken with dissolve
    show mother_mila at right, lighten with dissolve 
    voice "nanay/line1.mp3"
    n "Anak, gising ka na! Akala ko ay nawawala ka na!"

    show mother_mila at right, darken with dissolve
    hide scared_mila with dissolve
    show curious_mila at left, lighten with dissolve 
    voice "mila/mila_26.mp3"
    m "Panaginip lang ba ang lahat?"

    hide mother_mila with moveoutright
    voice "mila/mila_27.mp3"
    m "Shadow! Chabs! Nandito lang ba kayo?"

    show chabs_sitting at right, lighten with dissolve
    show sitting_shadow at center, lighten with dissolve
    show happy_mila at left, lighten with dissolve 
    voice "mila/mila_28.mp3"
    m "Buti naman! Akala ko nawala na kayo!"

    show curious_mila at left, with dissolve
    hide happy_mila with dissolve
    voice "mila/mila_29.mp3"
    m "Siguro... panaginip lang talaga. Pero natutunan ko ang halaga ng pangngalan—kung paanong hindi lang ito tungkol sa pangalan ng tao o hayop, kundi sa pagbibigay ng kahulugan sa mundo sa paligid natin."
    
    show happy_mila at left, with dissolve
    hide curious_mila with dissolve
    voice "mila/mila_30.mp3"
    m "Okay, okay! Tara na, maglaro tayo!"

    hide chabs_sitting with dissolve
    hide happy_mila with dissolve

    jump prompt_4

label prompt_4:

    show sitting_shadow at center, with move
    voice "prompt evens/shadow_prompt4.mp3"
    s "Ano ang ibig sabihin ng pangngalan?"

    menu:
        s "Ano ang ibig sabihin ng pangngalan?"
        "Pangalan ng tao, hayop, lugar, bagay, o pangyayari":
            voice "prompt evens/shadow_right4B.mp3"
            s "Tama! Ang pangngalan ay pangalan ng tao, hayop, lugar, bagay, o pangyayari!"
            jump prompt_5

        "Salitang nagsasaad ng kilos":
            voice "prompt evens/shadow_wrong4A.mp3"
            s "Hmm, hindi! Ang salitang nagsasaad ng kilos ay pandiwa. Subukan ulit!"
            jump prompt_4

        "Salitang naglalarawan ng kilos":
            voice "prompt evens/shadow_wrong4C.mp3"
            s "Hindi rin! Ang salitang naglalarawan ng kilos ay hindi ito. Ano kaya ang tamang sagot?"
            jump prompt_4


label prompt_5:
    hide sitting_shadow with dissolve

    show chabs_sitting at center, with dissolve
    voice "chabsprompt/q5.mp3"
    c "Dahil kilala mo na sina Mila, Shadow, at Chabs, ano naman ang kahulugan ng salitang 'Mila' na ginamit natin sa kwento?"

    menu:
        c "Dahil kilala mo na sina Mila, Shadow, at Chabs, ano naman ang kahulugan ng salitang 'Mila' na ginamit natin sa kwento?"
        "Pangalan ng hayop":
            voice "chabsprompt/5..mp3"
            c "Hindi! Ang 'Mila' ay hindi pangalan ng hayop."
            jump prompt_5

        "Pang-uri ng pag-uugali":
            voice "chabsprompt/5...mp3"
            c "Hindi rin! Ang 'Mila' ay hindi paglalarawan. Subukan ulit!"
            jump prompt_5

        "Pangalan ng tao":
            voice "chabsprompt/5....mp3"
            c "Tama! Ang 'Mila' ay isang pangngalan na pangalan ng tao!"
            jump prompt_6
        
    

label prompt_6:
    hide chabs_sitting with dissolve

    show standing_shadow at center, with dissolve
    voice "prompt evens/shadow_prompt6.mp3"
    s "Kung tinawag mo ang isang aso sa pangalang 'Shadow' o 'Chabs', ano ito?"

    menu:
        s "Kung tinawag mo ang isang aso sa pangalang 'Shadow' o 'Chabs', ano ito?"
        "Pangalan ng hayop":
            voice "prompt evens/shadow_right6A.mp3"
            s "Tama! Ang 'Shadow' at 'Chabs' ay pangngalan dahil ito ay pangalan ng hayop!"
            jump prompt_7

        "Salitang nagsasaad ng kilos":
            voice "prompt evens/shadow_wrong6B.mp3"
            s "Hindi! Ang salitang nagsasaad ng kilos ay pandiwa. Subukan mong muli!"
            jump prompt_6

        "Pang-uri":
            voice "prompt evens/shadow_wrong6C.mp3"
            s "Mali! Ang pang-uri ay naglalarawan, hindi pangalan."
            jump prompt_6
        
    

label prompt_7:
    hide standing_shadow with dissolve

    show chabs_standing at center, with dissolve
    voice "chabsprompt/q7.mp3"
    c "Alin sa mga sumusunod ang halimbawa ng pangngalan? Pumili ng tamang sagot: bato, ilog, o masayahin?"

    menu:
        c "Alin sa mga sumusunod ang halimbawa ng pangngalan? Pumili ng tamang sagot: bato, ilog, o masayahin?"
        "bato":
            voice "chabsprompt/q7...mp3"
            c "Tama! Ang bato at ilog ay mga pangngalan dahil sila ay pangalan ng bagay at lugar!"
            jump prompt_8

        "ilog":
            voice "chabsprompt/7...mp3"
            c "Tama! Ang bato at ilog ay mga pangngalan dahil sila ay pangalan ng bagay at lugar!"
            jump prompt_8

        "masayahin":
            voice "chabsprompt/7..mp3"
            c "Hindi! Ang 'masayahin' ay isang pang-uri. Subukan ulit!\n(Maaaring pumili din ng maling sagot kung piliin ang hindi parehong tamang halimbawa.) "
            jump prompt_7
        
    

label prompt_8:
    hide chabs_standing with dissolve

    show sitting_shadow at center, with dissolve
    voice "prompt evens/shadow_prompt8.mp3"
    s "Sa huli, ano naman ang ibig sabihin ng pangngalang pantangi?"

    menu:
        s "Sa huli, ano naman ang ibig sabihin ng pangngalang pantangi?"
        "Pangalan na ginagamit sa lahat ng bagay":
            voice "prompt evens/shadow_wrong8A.mp3"
            s "Hindi! Ang pangalang ginagamit sa lahat ay karaniwang pangngalan. Subukan ulit!"
            jump prompt_8

        "Pangalan na natatangi at tumutukoy sa isang partikular na tao, hayop, o lugar":
            voice "prompt evens/shadow_right8B.mp3"
            s "Tama! Ang pangalang pantangi ay natatangi at tumutukoy sa isang partikular na tao, hayop, o lugar!"
            jump story_1_ending

        "Salitang naglalarawan ng kilos":
            voice "prompt evens/shadow_prompt8C.mp3"
            s "Hindi rin! Ang salitang naglalarawan ng kilos ay hindi ito."
            jump prompt_8
        
    
label story_1_ending:
    show happy_mila at left, with moveinleft
    show chabs_sitting at right, with moveinright
    
    voice "mila/mila_31.mp3"
    m "Salamat sa pagsama sa aking paglalakbay! Sana ay may natutunan kayo sa ating aralin. Huwag kalimutan—ang pangngalan ay mahalaga sa ating wika at sa ating pagkatao. Hanggang sa muli!"

    jump story_2_splashscreen


label story_2_splashscreen:
    
    $ quick_menu = False
    scene black
    pause 1.0 
    show splash2 at top with fade
    voice "title/title2.mp3"
    pause 
    hide splash2 with dissolve
    $ quick_menu = True
    stop voice

    jump story_2


label story_2:

    scene bg living room
    with dissolve

    show happy_adi at left, with dissolve 
    voice "adrielle/line1.mp3"
    d "Magandang araw! Ako si Adrielle, at ito ang aking Lola Jiji. Nakatira kami sa isang masiglang bahay kasama ang aming mga alagang pusa."

    show happy_adi at left, darken with dissolve
    show happy_lolajiji at right, with dissolve 
    voice "lola/lola 1.mp3"
    j "Buti naman at napadalaw ka! Halika, ipapakilala kita sa aming mga alaga!"

    voice "cat/cat_meow.mp3"
    f "Meow!"

    voice "cat/cat_meow4.mp3"
    e "meow!"

    voice "lola/lola 2.mp3"
    j "ito sina Fiona at Jane! Si Fiona ay makinis at makulay, habang si Jane naman ay matapang at espesyal pati espesyal dahil isa siyang pirata!"

    show happy_lolajiji at right, darken with dissolve
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line2.mp3"
    d "Pirata? Haha! Totoo nga, Lola! Si Jane ay bulag sa isang mata kaya may suot siyang takip sa kanyang kaliwang mata, pero hindi iyon hadlang sa kanyang pagiging matalino at maliksi!"

    show happy_adi at left, darken with dissolve
    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 3.mp3"
    j "Tignan mo, ang c-cute nila! Si Jane ay kulay kahel at puti habang si Jane naman ay mayroong itim na balahibong bagay na bagay sa kanyang kulay dilaw na mata."

    show happy_lolajiji at right, darken with dissolve
    show happy_adi at left,lighten with dissolve
    voice "adrielle/line3.mp3"
    d "Hmm…kahel at puti? asul o dilaw? Lola, nakakahilo naman ang mga binibigkas mo salita, hindi po kita maintindihan…"

    show happy_adi at left, darken with dissolve
    show calm_lolajiji at right, lighten with dissolve
    voice "lola/lola 4.mp3"
    j "Ang binigkas kong mga salita ay mga kulay, Adi. Ang tawag sa mga salitang kulay ay “Pang-uri.”"

    show calm_lolajiji at right, darken with dissolve
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line4.mp3"
    d "Huh? Ano yun, Lola?"

    show happy_adi at left, darken with dissolve
    show calm_lolajiji at right, lighten with dissolve
    voice "lola/lola 5.mp3"
    j "Ang pang-uri ay mga salitang naglalarawan o nagbibigay-katangian sa isang tao, kilos, o hayop, kagaya nila Fiona at Jane."

    show calm_lolajiji at right, darken with dissolve
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line5.mp3"
    d "Ah! Pang-uri! Ayan ang itinuro sa amin ng aming guro noong nakaraang klase, Lola! Ngunit, nalilito parin ako kung ano ang mga salitang pandiwa, sobrang dami kasi, Lola…"

    show happy_adi at left, darken with dissolve
    show calm_lolajiji at right, lighten with dissolve
    voice "lola/lola 6.mp3"
    j "Dahil ang mga salitang pang-uri ay may iba’t ibang anyo, Adi."

    voice "cat/cat_meow2.mp3"
    f "Meow! Meow!"

    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 7.mp3"
    j "Subukan niyo, Adi! Tignan mo ang kulay nila Fiona at Jane. Alin sa sumusunod ang tamang paglalarawan ng kulay ng balahibo ni Fiona?"

    hide calm_lolajiji with dissolve
    hide happy_adi with dissolve

    jump prompt_9

label prompt_9:

    show happy_lolajiji at center, with move

    menu:
        
        j "Alin sa sumusunod ang tamang paglalarawan ng kulay ng balahibo ni Fiona?"
        "Kulay asul at puti":
            j "Maling sagot! Subukan muli! Ano nga ba ang kulay ng balahibo ni Fiona?"
            jump prompt_9

        "Kulay puti at kahel":
            j "Tama! Si Fiona ay may balahibong kulay kahel at puti!"
            jump scene2_2

        "Kulay itim at dilaw":

            j "Maling sagot! Subukan muli! Ano nga ba ang kulay ng balahibo ni Fiona?"
            jump prompt_9
        
    


label scene2_2:
    hide happy_lolajiji with dissolve

    show happy_adi at left, with dissolve
    voice "adrielle/line6.mp3"
    d "ahhh! Iyon pala ang tawag sa kulay ng balahibo ni Fiona. Puti, na kakulay ng mga ulap sa langit habang ang kahel ay kakulay ng mga dalandan."

    show happy_adi at left, darken with dissolve
    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 8.mp3"
    j "Tama, Adi! Oh, subukan niyo muli. Alin sa mga sumusunod ang tamang naglalarawan sa kulay ng balahibo ni Jane?"

    hide happy_adi with dissolve

    jump prompt_10

label prompt_10:

    show happy_lolajiji at center with move

    menu:
        j " Alin sa mga sumusunod ang tamang naglalarawan sa kulay ng balahibo ni Jane?"
        "Kulay itim":
            j "Tama! Si Jane ay may balahibong kulay itim."
            jump scene2_3

        "Kulay puti":
            j "Mhm. Subukan mong pagmasdan muli si Jane. Ano ang kanyang tunay na kulay?"
            jump prompt_10

        "Kulay kahel":
            j "Mhm. Subukan mong pagmasdan muli si Jane. Ano ang kanyang tunay na kulay?"
            jump prompt_10
        
    


label scene2_3:
    hide happy_lolajiji with dissolve

    show happy_adi at left, lighten with dissolve
    voice "adrielle/line7.mp3"
    d "Itim pala ang tawag sa kulay ng balahibo ni Jane! Kaya pala magaling siyang nakakapagtago tuwing gabi dahil ka-kulay niya halos ang langit, Lola."

    show happy_adi at left, darken with dissolve
    show calm_lolajiji at right, lighten with dissolve
    voice "lola/lola 9.mp3"
    j "Tama ka diyan, Adi. Ang mga ginamit natin mga salitang ay halimbawa ng mga Pang-uri na ipinapantukoy natin sa kulay ng mga bagay."

    show calm_lolajiji at right, darken with dissolve
    show curious_adi at left, lighten with dissolve
    voice "adrielle/line8.mp3"
    d "Ngunit, Lola, hindi lamang po riyan nagtatapos ang mga salitang pang-uri, hindi ba?"

    show curious_adi at left, darken with dissolve
    show calm_lolajiji at right, lighten with dissolve
    voice "lola/lola 10.mp3"
    j "Oo, Adi. Maaari pa itong maglarawan sa laki, bilang, hugis, ugali at iba pang katangian ng isang pangngalan."

    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 11.mp3"
    j "simula nang lumipat kayo rito, Adi, napansin kong napaka-ingay ng mga pusa tuwing umaga!"

    show happy_lolajiji at right, darken with dissolve
    show happy_adi at left, lighten with dissolve
    hide curious_adi with dissolve
    voice "adrielle/line9.mp3"
    d "Hehehe…dahil po kasi yan kay Kuya Gong, ang nagbebenta ng taho dito sa ating barangay."

    show happy_adi at left, darken with dissolve
    show calm_lolajiji at right, lighten with dissolve
    voice "lola/lola 12.mp3"
    j "Ay, nako apo…mukang inaabangan rin nila ang paborito mong taga-lako dahil paborito mo ang taho niya."

    show calm_lolajiji at right, darken with dissolve
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line10.mp3"
    d "Opo, Lola! Siguro gusto nilang lumabas dahil sila ay naghahanap ng pagkain."

    voice "cat/cat_meow2.mp3"
    f "Meow! Meow!"

    voice "cat/cat_meow4.mp3"
    e "Meow!"

    show happy_adi at left, darken with dissolve
    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 13.mp3"
    j "Pakinggan mo, Adi! Ang kanilang tinig ay malakas! Ano kaya ang ibig sabihin ng mga sigaw nila?"

    show happy_lolajiji at right, darken with dissolve
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line11.mp3"
    d "Subukan niyo naman, mga kaibigan! Paano niyo mailalarawan ang tunog nila Fiona at Jane?"
    
    hide happy_lolajiji with dissolve
    hide calm_lolajiji with dissolve

    jump prompt_11

label prompt_11:

    show happy_adi at center, with move
    voice "adrielle/choices1.mp3"
    d "Paano niyo mailalarawan ang tunog nila Fiona at Jane?"

    menu:
        d "Paano niyo mailalarawan ang tunog nila Fiona at Jane?"
        "Tahimik":
            voice "adrielle/adrielle_wrong1.mp3"
            d "Maling sagot! Subukan mong pakinggan muli ang tunog nila Fiona at Jane. Ano ang naririnig mo?"
            jump prompt_11

        "Malakas":
            voice "adrielle/right1.mp3"
            d "Tama! Ang kanilang tinig ay malakas!"
            jump scene2_4

        "Malalim":
            voice "adrielle/choices1.mp3"
            d "Maling sagot! Subukan mong pakinggan muli ang tunog nila Fiona at Jane. Ano ang naririnig mo?"
            jump prompt_11
        
    

label scene2_4:
    hide happy_adi with dissolve

    voice "cat/cat_meow3.mp3"
    f "Meow!"

    voice "cat/cat_meow2.mp3"
    e "Meow! Meow!"

    show happy_lolajiji at right, with dissolve 
    voice "lola/lola 14.mp3"
    j "oh, bumili ka na apo! Ang mga ingay ng mga pusa ay lumalakas at tumitinis. Baka hinihintay ka na ni Kuya Gong."

    show happy_lolajiji at right, darken with dissolve
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line12.mp3"
    d "Opo, Lola!"


    jump scene2_5


label scene2_5:

    scene bg roadside
    with dissolve

    show happy_kuyagong at center
    with dissolve
    voice "kuya/gong1.mp3"
    k "Magandang umaga, Adi! Bibili ka ba ng taho ngayong umaga?"


    show happy_adi at left, with dissolve
    show happy_kuyagong at right, with move 
    voice "adrielle/line13.mp3"
    d "Opo! Magiging kulang ang aking umaga kung hindi ko maiinom ang inyong taho, Kuya Gong."

    show happy_adi at left, darken with dissolve
    show happy_kuyagong at right, lighten with dissolve
    voice "kuya/gong2.mp3"  
    k "Oh siya, ano bang sukat ng baso ang bibilhin mo ngayong umaga, Adi?"

    show happy_kuyagong at right, darken with dissolve
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line14.mp3"
    d "Ano po bang mayroon kayo, Kuya?"

    show happy_adi at left, darken with dissolve
    show happy_kuyagong at right, lighten with dissolve
    voice "kuya/gong3.mp3"
    k "Mayroon akong tatlong sukat ng baso para sa iyong taho, Adi! May maliit, katamtaman, at malaking baso. Ano ang gusto mong bilhin?"

    p1 "Meow! Meow"

    show happy_kuyagong at center, darken with move
    show calm_lolajiji at right, darken with dissolve
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line15.mp3"
    d "Lola, Lola, tignan ninyo! May lalaking pusa rito sa labas! Tinatawag niya sina Fiona at Jane!"

    show happy_lolajiji at right, darken with dissolve
    hide calm_lolajiji with dissolve
    voice "adrielle/line16.mp3"
    d "Ang gusto kong sukat ng baso para sa aking taho ay malaki, Kuya Gong. Mga kaibigan, puwede niyo bang piliin kung alin sa mga basong ito ay may malaking sukat?"

    hide happy_lolajiji with dissolve
    hide happy_kuyagong with dissolve

label prompt_12:

    show happy_adi at center, with move




    show happy_adi at left, darken with dissolve
    show happy_kuyagong at center, lighten with dissolve
    voice "kuya/gong4.mp3"
    k "Ito na! Isang malaking baso para kay Adi na paborito ang binebenta kong taho."

    show happy_kuyagong at center, darken with dissolve
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line17.mp3"
    d "Maraming salamat po! Mhmmm! Hindi ko po talaga malilimutan ang lasa ng inyong taho, Kuya Gong!"

    show happy_adi at left, darken with dissolve
    show happy_kuyagong at center, lighten with dissolve
    voice "kuya/gong5.mp3"
    k "Haha! Salamat, Adi! Ang taho ko ay laging matamis at malinamnam! Kaya gustong-gusto ito ng maraming batang katulad mo."

    show happy_kuyagong at center, darken with dissolve
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line18.mp3"
    d "Kinikilig na ako dahil sa tamis nito, sadyang nakakapagbigay po ito ng enerhiya!"

    voice "cat/cat_meow2.mp3"
    f "Meow! Meow!"

    voice "cat/cat_meow2.mp3"
    e "Meow! Meow!"

    show happy_adi at left, darken with dissolve
    show happy_kuyagong at center, lighten with dissolve
    voice "kuya/gong6.mp3"
    k "Oh, mukhang gusto ring subukan ng iyong mga alaga ang aking taho! Oh siya, mauna na ako, Adi. Marami salamat sa pagbili!"

    show happy_kuyagong at center, darken with dissolve
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line19.mp3"
    d "Ingat po kayo, Kuya Gong. Salamat rin po!"   

    hide happy_kuyagong with dissolve

    voice "cat/cat_meow2.mp3"
    p1 "Meow! Meow!"

    voice "cat/cat_meow.mp3"
    f "Meow!"

    voice "adrielle/line20.mp3"
    d "Lola, Lola! Tingnan mo! May pusa na kamukhang-kamukha ni Fiona."

    show happy_adi at left, darken with dissolve
    show calm_lolajiji at right, lighten with dissolve
    hide happy_lolajiji with dissolve
    voice "lola/lola 15.mp3"
    j "Ay, sus! Yan ang mapagmahal na asawa ni Fiona, Adi."

    voice "cat/cat_meow 3.mp3"
    p1 "Meow!"

    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 16.mp3"
    j "Tingnan mo, Adi! Hindi lang siya basta dumalaw—nagbigay pa siya ng regalo kay Fiona! Talagang mapagmahal siyang asawa."

    show happy_lolajiji at right, darken with dissolve
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line21.mp3"
    d "Lola, paano mo nasabi na ang asawa ni Fiona ay mapagmahal?"

    show happy_adi at left, darken with dissolve
    show calm_lolajiji at right, lighten with dissolve
    hide happy_lolajiji with dissolve
    voice "lola/lola 17.mp3"
    j "Ang pagmamahal ay nakikita sa kilos, hindi lamang sa salita, Adi. Mga kaibigan, ano ba ang ginagawa ng asawa ni Fiona upang maging mapagmahal?"

    hide happy_adi with dissolve
    
    jump prompt_12

label prompt_12:

    show calm_lolajiji at center, with move

    menu:
        j "Mga kaibigan, ano ba ang ginagawa ng asawa ni Fiona upang maging mapagmahal?"
        "Nagdadala ng pagkain at nag-aalaga":
            j "Tama! Ang mapagmahal ay nangangahulugang maalaga at mabait, tulad ng pagbibigay ng pagkain at pagiging malambing kay Fiona!"
            jump scene2_6

        "Malakas":
            j ""
            jump prompt_12

        "Nang-aagaw ng pagkain":
            j "Maling sagot! Subukan mong pakinggan muli ang tunog nila Fiona at Jane. Ano ang naririnig mo?"
            jump prompt_12
        
    


label scene2_6:
    hide calm_lolajiji with dissolve

    show happy_adi at left, with dissolve
    voice "adrielle/line22.mp3"
    d "Ah! Kaya pala siya mapagmahal, Lola! Dahil hindi lang siya basta dumadalaw, ipinapakita rin niya ang kanyang pag-aalaga kay Fiona sa pamamagitan ng pagbibigay ng pagkain at pagiging malambing!"

    voice "adrielle/line23.mp3"
    d "Hala, Lola! Tignan mo, mayroon pang isang pusa!"

    voice "cat/cat_meow4.mp3"
    p1 "Niyawwww!"

    voice "cat/cat_meow3.mp3"
    p2 "Niyawwwww!"

    show happy_adi at left, darken with dissolve
    show sad_lolajiji at right, lighten with dissolve
    voice "lola/lola 18.mp3"
    j "Naku! Mukhang may labanang magaganap!"

    show sad_lolajiji at right, darken with dissolve
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line24.mp3"
    d "Lola, tignan mo si Jane! Parang ipinagtatanggol niya ang mag-asawa!"

    voice "cat/cat_growl.mp3"
    e "Hissss!"

    voice "adrielle/line25.mp3"
    d "Tingnan mo si Jane, La!—Kahit na may isang mata lamang siya, hindi siya natatakot humarap sa kalaban!"

    voice "cat/cat_angry.mp3"
    e "Hissss! Hissss!" 

    voice "cat/cat_meow.mp3"
    p2 "Meow…"

    voice "cat/cat_meow3.mp3"
    p1 "Meow!"

    voice "adrielle/line26.mp3"
    d "Grabe, Lola. Napaurong ang kalaban! Talagang hindi uurong si Jane kapag kailangan niyang ipagtanggol ang pamilya niya."

    show happy_adi at left, darken with dissolve
    show happy_lolajiji at right, lighten with dissolve
    hide sad_lolajiji with dissolve
    voice "lola/lola 19.mp3"
    j "Si Jane ay hindi lang basta pusa—isa siyang tunay na tagapagtanggol! Mga kaibigan, Ano sa tingin niyo ang nagpapakita na siya ay matapang?"

    hide happy_adi with dissolve

    jump prompt_13


label prompt_13:

    show happy_lolajiji at center, with move
    
    menu:
        j "Ano sa tingin niyo ang nagpapakita na siya ay matapang?"
        "Kung umalis papalayo ang isang hayop mula sa kanyang kalaban, hindi siya matapang! Subukan mong muli.":
            j "Tama! Ang mapagmahal ay nangangahulugang maalaga at mabait, tulad ng pagbibigay ng pagkain at pagiging malambing kay Fiona!"
            jump prompt_13

        "Tumayo sa harapan ni Fiona at hinarap ang kalaban":
            j "Tama! Ang matapang ay nangangahulugang hindi natatakot, tulad ni Jane na ipinagtanggol si Fiona!"
            jump scene2_7

        "Umakyat sa bubong at iniwan ang mag-asawa":
            j "Kung umalis papalayo ang isang hayop mula sa kanyang kalaban, hindi siya matapang! Subukan mong muli.?"
            jump prompt_13
        
    

label scene2_7:
    hide happy_lolajiji with dissolve   
    
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line27.mp3"
    d "Oo nga, Lola! Kahit mas malaki ang kalaban, hindi siya umatras. Talagang handa siyang ipagtanggol sina Fiona!"

    show happy_adi at left, darken with dissolve
    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 20.mp3"
    j "Tama ka, Adi! Ang pagiging matapang ay hindi lang tungkol sa pakikipaglaban, kundi tungkol din sa pagiging handang protektahan ang mahal mo, kahit nakakatakot ang sitwasyon."

    voice "cat/cat_meow.mp3"
    e "Meow…"

    show happy_lolajiji at right, darken with dissolve
    hide happy_adi with dissolve
    show scared_adi at left, lighten with dissolve
    voice "adrielle/line28.mp3"
    d "Ayos lang ba kayo, Fiona at Jane?"

    voice "cat/cat_meow2.mp3"
    f "Meow…meow…"

    show scared_adi at left, darken with dissolve
    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 21.mp3"
    j "Oh, saan ka naman kayo pupunta, Fiona at Jane?"

    jump scene2_8


label scene2_8: 

    scene bg backyard
    with dissolve

    voice "cat/cat_meow3.mp3"
    f "Meow!"

    show happy_adi at left, lighten with dissolve
    voice "adrielle/line29.mp3"
    d "Lola, Lola! Tingnan mo! May tatlong kuting na anak si Fiona dito!"

    show happy_adi at left, darken with dissolve
    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 22.mp3"
    j "Aba, ang gaganda nila, Adi! Mukhang malulusog at malilikot!"

    voice "cat/cat_meow.mp3"
    e "Meow!"

    show happy_lolajiji at right, darken with dissolve
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line30.mp3"
    d "Lola, pwede ba natin silang dalhin sa loob ng bahay? Para hindi sila ginawin sa labas!"

    show happy_adi at left, darken with dissolve
    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 23.mp3"
    j "Syempre naman, apo! Hindi natin sila pwedeng pabayaan dito. Halika, ilipat natin sila sa isang malambot na kumot sa loob."

    hide happy_adi with dissolve
    hide happy_lolajiji with dissolve

    scene bg living room
    with dissolve

    show curious_adi at left, lighten with dissolve
    voice "adrielle/line31.mp3"
    d "Lola, ano kaya ang magandang pangalan para sa kanila?"

    show curious_adi at left, darken with dissolve
    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 24.mp3"
    j "Hmm… Ano ba ang napapansin mo sa itsura at ugali nila?"

    show happy_lolajiji at right, darken with dissolve
    hide curious_adi with dissolve
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line32.mp3"
    d "Lola, ang isang ito, yung may itim at puting balahibo, parang kamukhang-kamukha ni Jane! Ngunit kanina pa siya takbo nang takbo!"

    show happy_adi at left, darken with dissolve
    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 25.mp3"
    j "Haha! Mukhang may isang pasaway sa grupo! Ano pa ang napapansin mo, Adi?"

    show happy_lolajiji at right, darken with dissolve
    show curious_adi at left, lighten with dissolve
    hide happy_adi with dissolve
    voice "adrielle/line34.mp3"
    d "Hmm…ano pong magandang ipangalan sa kanya, Lola?"

    show curious_adi at left, darken with dissolve
    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 26.mp3"
    j "Dahil ang balahibo niya ay katulad ni Fiona, mukhang bagay sa kanya ang pangalan na JJ."

    show happy_lolajiji at right, darken with dissolve
    show curious_adi at left, lighten with dissolve
    voice "adrielle/line35.mp3"
    d "JJ? Ano pong ibig sabihin nun?"

    show curious_adi at left, darken with dissolve
    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 27.mp3"
    j "Ang JJ ay nangangahulugan ng Jane Jr. Dahil kamukha niya si Jane, parang maliit na bersyon niya!"

    show happy_lolajiji at right, darken with dissolve
    show happy_adi at left, lighten with dissolve
    hide curious_adi with dissolve
    voice "adrielle/line36.mp3"
    d "Itong isa naman po ay mapagmahal katulad ng kanyang tatay. Tignan mo, Lola, kanina pa siya nakadikit kay Fiona! Parang gusto niya na lamang mahalin ang kanyang ina."

    show happy_adi at left, darken with dissolve
    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 28.mp3"
    j "Mukhang malambing siya, Adi! Paano naman ang kanyang itsura?"

    show happy_lolajiji at right, darken with dissolve
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line37.mp3"
    d "Hmm, ang kanyang balahibo ay katulad ng kanyang nanay."

    voice "adrielle/line38.mp3"
    d "Mukhang bagay po sa kanya ang pangalan na FJ! na nangangahulugang Fiona Jr., dahil katulad niya ang kanyang nanay!"

    show happy_adi at left, darken with dissolve
    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 29.mp3"
    j "At paano naman ‘yung isa pa? Paano mo naman ma-iiba ang kanyang ugali at itsura mula sa kanyang dalawang kapatid?"

    show happy_lolajiji at right, darken with dissolve
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line39.mp3"
    d "Hindi niya po kamukha kahit sino kina Fiona at Jane, Lola. Ang kanyang itsura ay puti at mayroong po siyang malaking tuldok sa kanyang ulo."

    show happy_adi at left, darken with dissolve
    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 30.mp3"
    j "Ano naman sa tingin mo ang bagay na pangalan sa kanya base sa kanyang itsura, Adi?"

    show happy_lolajiji at right, darken with dissolve
    show curious_adi at left, lighten with dissolve
    hide happy_adi with dissolve
    voice "adrielle/line40.mp3"
    d "Hmm… Dahil may malaking itim na tuldok sa ulo niya, parang bagay sa kanya ang pangalang…Dot!"

    show curious_adi at left, darken with dissolve
    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 31.mp3"
    j "Ikaw talaga, apo! Ngunit maliban sa kanyang kakaibang itsura ni Dot, Adi, ano pa ang napapansin mo sa kanya?"

    show happy_lolajiji at right, darken with dissolve
    show happy_adi at left, lighten with dissolve
    hide curious_adi with dissolve
    voice "adrielle/line41.mp3"
    d "Hindi po siya katulad ng dalawa na sobrang likot, Lola. Tahimik lamang po siya sa isang tabi."

    voice "adrielle/line42.mp3"
    d "Nakakalungkot naman, Lola…Baka hindi pa sanay sa atin at sa kanyang mga kapatid."

    show happy_adi at left, darken with dissolve
    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 32.mp3"
    j "Huwag kang mag-alala, Apo. Darating rin ang araw na masasanay siya sa atin, dahil tulad ng tao, iba-iba rin ang ugali ng mga pusa. Pero kahit magkakaiba sila, isang bagay ang sigurado—lahat sila ay bahagi na ng ating pamilya!"

    show happy_lolajiji at right, darken with dissolve
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line43.mp3"
    d "Tama, Lola! Mayroon na tayong tatlong bagong kuting na bagong miyembro ng ating pamilya! Sina JJ o Jane Jr, ang kakulay ni Jane; si FJ o Fiona Jr, ang kakulay ni Fiona; at si Dot, ang mayroong tuldok sa kanyang ulo! "

    show happy_adi at left, darken with dissolve
    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 33.mp3"
    j "Tama ka, Adi! At bilang kanilang pamilya, tungkulin nating alagaan at mahalin sila, anuman ang kanilang ugali."

    voice "cat/cat_meow4.mp3"
    t "Meow!"

    show happy_lolajiji at right, darken with dissolve
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line44.mp3"
    d "Aba, Lola! Mukhang unti-unti nang nasasanay si Dot sa atin!"

    show happy_adi at left, darken with dissolve
    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 34.mp3"
    j "Oo nga, Adi. Minsan, ang tiwala at pagmamahal ay dumarating sa tamang panahon."
    
    show happy_lolajiji at right, darken with dissolve
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line45.mp3"
    d "Hay, ang saya ng araw na ‘to, Lola! Ang dami nating natutunan at ang dami pang bago sa ating pamilya."

    show happy_adi at left, darken with dissolve
    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 35.mp3"
    j "Tama! Lagi nating tandaan—maliit man o malaki, tahimik man o makulit, lahat ay may natatanging halaga."

    show happy_lolajiji at right, darken with dissolve
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line46.mp3"
    d "Salamat sa pagsama sa amin, mga kaibigan! Hanggang sa susunod nating kwento, mga kaibigan! Salamat at ingat kayo palagi!"

    jump scene2_9


label scene2_9:

    scene bg backyard
    with dissolve

    show happy_adi at left, lighten with dissolve
    voice "adrielle/line47.mp3"
    d "Maraming salamat sa pagsama sa amin, mga kaibigan! Ang saya-saya namin ni Lola na ipakilala sa inyo sina Fiona, Jane, at ang kanilang mga kuting!"

    show happy_adi at left, darken with dissolve
    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 36.mp3"
    j "Ngayon, bago tayo magtapos, balikan natin ang mga natutunan natin tungkol sa pang-uri o mga salitang naglalarawan! Mga kaibigan, ano nga ba ulit ang ibig sabihin ng pang-uri?"

    hide happy_adi with dissolve
    show happy_lolajiji at center, with move

label prompt_14:
    
    menu:
        j "ano nga ba ulit ang ibig sabihin ng pang-uri?"
        "Salitang nagsasaad ng kilos":
            j "Hmm, hindi! Ang salitang nagsasaad ng kilos ay tinatawag na pandiwa. Subukan ulit!"
            jump prompt_14

        "Salitang naglalarawan ng katangian ng tao, hayop, bagay, o lugar":
            j "Tama! Ang pang-uri ay salitang naglalarawan ng katangian ng tao, hayop, bagay, o lugar, tulad ng 'makulit,' 'mahiyain,' at 'malambing!'"
            jump scene2_10

        "Pangalan ng tao, bagay, hayop, o lugar":
            j "Hindi rin! Ang pangalan ng tao, bagay, hayop, o lugar ay tinatawag na pangngalan. Ano kaya ang tamang sagot?"
            jump prompt_14
        
    

label scene2_10:
    hide happy_lolajiji with dissolve   

    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 37.mp3"
    j "Magaling! Natutunan natin kung paano naglalarawan ang pang-uri sa ating mga alagang pusa at sa mga bagay sa paligid natin. Ngayon, subukan nating isa pang halimbawa!"

    voice "lola/lola 38.mp3"
    j "Subukan nating alalahanin ang laki ng baso ng taho na binili ni Adi kanina mula kay Kuya Gong."
    
    show happy_lolajiji at right, darken with dissolve
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line49.mp3"
    d "Mga kaibigan, paano naman natin mailalarawan ang binili nating baso ng taho mula kay Kuya Gong na may pinakamaraming laman?"

    hide happy_lolajiji with dissolve
    show happy_adi at center, with move

    jump prompt_15

label prompt_15:
    menu:
        d "paano naman natin mailalarawan ang binili nating baso ng taho mula kay Kuya Gong na may pinakamaraming laman?"
        "maliit":
            d "Subukan muli! Ano ang tawag sa pinakamalaking sukat ng baso?"
            jump prompt_15

        "katamtaman":
            d "Subukan muli! Ano ang tawag sa pinakamalaking sukat ng baso?"
            jump scene2_11

        "malaki":
            d "Tama! Ang malaking baso ang may pinakamaraming na taho!"
            jump prompt_15
        
    

label scene2_11:
    hide happy_adi with dissolve

    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 39.mp3"
    j "Nako, apo! Paboritong-paborito mo talaga ang taho ni Kuya Gong, ano?"

    show happy_lolajiji at right, darken with dissolve
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line50.mp3"
    d "Opo, Lola! Sadyang kakaiba po talaga ang taho ni Kuya Gong dahil sa matamis nitong lasa. Ngunit hindi lamang po taho ang matamis kaninang umaga dahil sa pag-dalaw ng asawa ni Fiona!"

    show happy_adi at left, darken with dissolve
    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 40.mp3"
    j "Aba, Adi! Hindi lang siya basta dumadalaw—nagbigay pa siya ng regalo kay Fiona! Talagang mahal na mahal niya ang kanyang asawa."

    show happy_lolajiji at right, darken with dissolve
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line51.mp3"
    d "Mga kaibigan, ano kaya ang tamang paglalarawan sa asawa ni Fiona?"

    hide happy_lolajiji with dissolve
    show happy_adi at center, with move

    jump prompt_16

label prompt_16:

    menu:
        d "ano kaya ang tamang paglalarawan sa asawa ni Fiona?"
        "Malupit":
            d "Hmm, parang hindi naman siya malupit o masungit kay Fiona! Subukan mong pag-isipan ulit!"
            jump prompt_16

        "mapagmahal":
            d "Tama! Ang asawa ni Fiona ay mapagmahal dahil nagdadala siya ng pagkain at nagpapakita ng malasakit kay Fiona!"
            jump scene2_12

        "Masungit":
            d "Hmm, parang hindi naman siya malupit o masungit kay Fiona! Subukan mong pag-isipan ulit!"
            jump prompt_16
        
    

label scene2_12:
    hide happy_adi with dissolve

    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 41.mp3"
    j "Dahil sa pagmamahalan ni Fiona at ang kanyang asawa, nagbunga ito sa tatlo nilang anak na kuting. Nagdagdagan ang ating pamilya ng tatlong napaka-cute na kuting!"

    show happy_lolajiji at right, darken with dissolve
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line52.mp3"
    d "Opo, Lola! Sina Jane Jr. Fiona Jr., at si Dot! Ngunit napansin ko, Lola, si Dot ay hindi kasing likot ng kanyang mga kapatid at tahimik lamang sa isang tabi. Ano kaya ang tamang paglalarawan kay Dot?"

    hide happy_lolajiji with dissolve
    show happy_adi at center, with move
    jump prompt_17

label prompt_17:

    menu:
        d "Ano kaya ang tamang paglalarawan kay Dot?"
        "mahiyain":
            d "Tama! Si Dot ay mahiyain at mas gusto niyang magmasid muna bago makisalamuha!"
            jump prompt_17

        "malikot":
            d "Hmm, parang hindi siya mahilig tumakbo o mangulit. Ano kaya ang tamang sagot?"
            jump scene2_13

        "malambing":
            d "Hmm, parang hindi siya mahilig tumakbo o mangulit. Ano kaya ang tamang sagot?"
            jump prompt_17
        
    

label scene2_13:
    hide happy_adi with dissolve

    show happy_adi at left, lighten with dissolve
    voice "adrielle/line53.mp3"
    d "Hays…Ang saya, Lola! Ang dami nating natutunan ngayong araw! Sa pamamagitan ng pang-uri, mas naipapakita natin ang katangian ng mga bagay, hayop, at tao sa ating paligid"

    show happy_adi at left, darken with dissolve    
    show happy_lolajiji at right, lighten with dissolve
    voice "lola/lola 42.mp3"
    j "Tama, Adi! Bukod pa roon, natutunan din natin na bawat isa ay may kanya-kanyang katangian—maaaring makulit, malambing, mahiyain, o matapang—ngunit lahat ay may halaga at dapat nating pahalagahan."

    show happy_lolajiji at right, darken with dissolve
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line54.mp3"
    d "Opo, Lola. Tulad ng ating mga alagang pusa, ang pagmamahal at pag-aaruga ay hindi lang sa salita, kundi ipinapakita rin sa gawa. "

    voice "cat/cat_meow2.mp3"
    f "Meow! Meow!"

    show happy_adi at left, darken with dissolve
    show calm_lolajiji at right with dissolve
    hide happy_lolajiji with dissolve
    voice "lola/lola 43.mp3"
    j "Oh mukhang andito na ang paborito mong taho, Adi. Tayo na’t bumili!"

    show calm_lolajiji at right, darken with dissolve
    show happy_adi at left, lighten with dissolve
    voice "adrielle/line55.mp3"
    d "Mukhang dito na nagtatapos ang ating kwento, mga kaibigan. Muli, marami salamat sa pagsama sa amin ni Lola Jiji. Hanggang sa susunod nating kwento! Ingat!"


    jump story_3_splashscreen


label story_3_splashscreen:
    
    $ quick_menu = False
    scene black
    pause 1.0 
    show splash3 at top with fade
    voice "title/title3.mp3"
    pause 
    hide splash3 with dissolve
    $ quick_menu = True
    stop voice

    jump story_3


label story_3:

    scene bg backyard
    with dissolve

    show Happy Isra at left, lighten with dissolve
    voice "isra/isra_line1.mp3"
    i "Magandang umaga sa inyo, mga kaibigan! Ako nga pala si Isra, at ito naman ang aso kong si Lala. Siya ang aking mabait at makulit na aso!"    

    show Happy Isra at left, darken with dissolve
    show Lala Sitting at right, lighten with dissolve
    voice "lala/arf.mp3"
    l "Arf, arf!"

    show Lala Sitting at right, darken with dissolve
    show Happy Isra at left, lighten with dissolve
    voice "isra/isra_line2.mp3"
    i "Ngayong araw, kami ay pupunta sa palaruan ni Lala. Ang palaruan ay isang lugar kung saan puwede tayong magsaya, maglaro, at makakilala ng mga bagong kaibigan!"
    
    show Happy Isra at left, darken with dissolve
    show Lala Sitting at right, lighten with dissolve
    voice "lala/arf.mp3"
    l "Arf, arf!" 

    show Lala Sitting at right, darken with dissolve
    show Happy Isra at left, lighten with dissolve
    voice "isra/isra_line3.mp3"
    i "Mukhang gusto na ni Lala na pumunta tayo sa palaruan, tignan mo ang kanyang buntot—kumakawag ito nang masigla! Ano kaya sa tingin mo ang ginagawa ni Lala ngayon?"

    hide Lala Sitting with dissolve
    show Happy Isra at center, with move
    jump prompt_18

label prompt_18:
    menu:
        i "Ano kaya sa tingin mo ang ginagawa ni Lala ngayon?"
        "Kumakanta":
            i "Kumakanta"
            jump prompt_18

        "Kumakawag ang buntot":
            i "Tama! 'Kumakawag ang buntot' ang tamang sagot! Ang 'kumakawag' ay isang pandiwa o kilos na ginagawa ni Lala kapag siya ay masaya."
            jump scene3_2

        "Sumisipa ng bola":
            i " Subukan mo ulit! Ano ang ginagawa niya kapag masaya?"
            jump prompt_18


label scene3_2:

    scene bg backyard
    with dissolve

    hide Happy Isra with dissolve

    show Lala Sitting at right, lighten with dissolve
    voice "lala/arf.mp3"
    l "Arf, arf…?"

    show Lala Sitting at right, darken with dissolve
    show Calm Isra at left, lighten with dissolve
    voice "isra/isra_line4.mp3"
    i "Mukhang nalilito ka ata, Lala. Alam mo ba? Lahat ng ating ginagawa ay may pangngalan at ang tawag sa mga pangngalan na ito ay pandiwa. Ang pandiwa ay isang salitang nagpapakita ng kilos."
    voice "isra/isra_line5.mp3"
    i "Kagaya ng ating ginawa kanina, ang pandiwa ay ginamit natin upang tawagin ang “kilos” na ginawa ng buntot ni Lala."

    show Calm Isra at left, darken with dissolve
    show Lala Sitting at right, lighten with dissolve
    voice "lala/arf.mp3"
    l "Arf, arf!"

    show Lala Sitting at right, darken with dissolve
    show Happy Isra at left, lighten with dissolve
    hide Calm Isra with dissolve
    voice "isra/isra_line6.mp3"
    i "Tama, Lala! Ang iyong buntot ay kumakawag."

    voice "isra/isra_line7.mp3"
    i "Saktong sakto! Ngayon na natutunan natin kung ano ang pandiwa, ang pagpunta natin sa palaruan ay hindi na lamang basta laro! Dito, malalaman pa natin kung paano gamitin ang mga pandiwa kung paano tayo magsaya at maglaro. Tara! Halina't samahan niyo kami ni Lala sa palaruan!"

    jump scene3_3

label scene3_3:

    scene bg backyard
    with dissolve

    show Curious Isra at left, lighten with dissolve 
    voice "isra/isra_line8.mp3"
    i "Andito na tayo sa palaruan, Lala!"

    show Curious Isra at left, darken with dissolve
    show Lala Standing at right, lighten with dissolve
    voice "lala/arf.mp3"
    l "Arf, arf!"

    show Lala Standing at right, darken with dissolve
    show Happy Isra at left, lighten with dissolve
    hide Curious Isra with dissolve
    voice "isra/isra_line9.mp3"
    i "Dahil unang beses mo pa lamang na makapunta sa palaruan, laruin natin ang paborito naming laro ni Lala—ang batuhan-bola!"

    show Happy Isra at left, darken with dissolve
    hide Lala Standing with dissolve
    show Lala Sitting at right, lighten with dissolve
    voice "lala/arf.mp3"
    l "Arf, arf!"

    show Lala Sitting at right, darken with dissolve
    show Happy Isra at left, lighten with dissolve
    voice "isra/isra_line10.mp3"
    i "Bago natin laruin ang batong-bata, tuturuan muna kita kung paano laruin ito! Para makapaglaro tayo ng aming paboritong laro, kailangan natin ang aming mahiwagang pulang bola!"

    show Happy Isra at left, darken with dissolve
    hide Lala Sitting with dissolve
    show Lala Standing at right, lighten with dissolve
    voice "lala/arf.mp3"
    l "Arf, arf!"

    show Lala Standing at right, darken with dissolve
    show Happy Isra at left, lighten with dissolve
    voice "isra/isra_line11.mp3"
    i "Oh! Salamat Lala. Mukhang gustong-gusto na rin ni Lala na turuan ka! Ito ang aming mahiwagang pulang bola. Ito ay espesyal dahil ito ay may palatandaan ng pangalan namin ni Lala!"

    voice "isra/isra_line12.mp3"
    i "Upang maglaro ng batong-bata, una, kailangan natin ihagis ang bola upang hanapin ito ni Lala. Pero teka! Alin sa mga ito ang tamang kilos na ihahagis ko ang bola?"

    hide Lala Standing with dissolve
    show Happy Isra at center, with move

    jump prompt_19

label prompt_19:
    menu:
        i "Alin sa mga ito ang tamang kilos na ihahagis ko ang bola? "
        "Hawakan ito sa kamay":
            i "Kailangan natin itong ihagis para mahahanap ito ni Lala! Subukan mo ulit!"
            jump prompt_19

        "Ipagulong ito sa sahig":
            i "Hmm, hindi natin ipagugulong ang bola. Kailangan natin itong ihagis para mahahanap ito ni Lala! Subukan mo ulit!"
            jump prompt_19

        "Ihagis ito papalayo":
            i " Tama! 'Ihahagis' ang tamang sagot! Ang 'ihahagis' ay isang pandiwa dahil ito ay isang kilos na aking gagawin."
            jump scene3_4

label scene3_4:

    scene bg backyard
    with dissolve

    hide Happy Isra with dissolve
    
    show Curious Isra at left, lighten with dissolve
    voice "isra/isra_line13.mp3"
    i "Dahil unang beses mo pa lamang maglalaro nito, ikaw nag maghahagis ng bola! Handa ka na ba, Lala?"

    show Curious Isra at left, darken with dissolve
    show Lala Standing at right, lighten with dissolve
    voice "lala/arf.mp3"
    l "Arf! Arf!"

    show Lala Standing at right, darken with dissolve
    show Happy Isra at left, lighten with dissolve
    hide Curious Isra with dissolve
    voice "isra/isra_line14.mp3"
    i "Muli, ano ang gagagawin natin sa bola upang hanapin ito ni Lala?"

    hide Lala Standing with dissolve
    show Happy Isra at center, with move

    jump prompt_20

label prompt_20:
    menu:
        i "Muli, ano ang gagagawin natin sa bola upang hanapin ito ni Lala?"
        "Ihahagis":
            i "Tama! Ihahagis ko ang bola para madali mong makita at makuha!"
            jump scene3_5

        "Ibubulsa":
            i "Hmm, hindi natin ipagugulong ang bola. Kailangan natin itong ihagis para mahahanap ito ni Lala! Subukan mo ulit!"
            jump prompt_20

        "Ipapagulong":
            i "Hmm, hindi mo makikita at mahahabol ni Lala ang bola kung ganito ang gagawin mo. Kailangan natin itong ihagis para maghanap ka!"
            jump prompt_20
        


label scene3_5:
    hide Happy Isra with dissolve

    show Lala Standing at right, lighten with dissolve
    voice "lala/arf.mp3"
    l "Arf! Arf!"

    show Lala Standing at right, darken with dissolve
    show Happy Isra at left, lighten with dissolve
    voice "isra/isra_line15.mp3"
    i "Ngayong inihagis na natin ang bola, tayo naman ay magbibilang mula hanggang isa hanggang sampu upang bigyan ng oras si Lala na hanapin ang bola! Alam mo ba kung ano ang ating gagawin upang tayo ay makapagbilang?"

    hide Lala Standing with dissolve
    show Happy Isra at center, with move

    jump prompt_21

label prompt_21:
    menu:
        i "Alam mo ba kung ano ang ating gagawin upang tayo ay makapagbilang?"
        "Gamitin ang kamay":
            i "Tama! Magagamit natin ang ating kamay sa pagbibilang mula isa hanggang sampu. Handa ka na ba? Sabay tayong magbilang!"
            jump scene3_6

        "Tumalon ng sampung beses":
            i "Haha! Masaya ang tumalon, pero hindi ito ang tamang paraan ng pagbibilang! Subukan natin muli."
            jump prompt_21

        "Itikom ang bibig":
            i "Kapag itinikom natin ang ating bibig, hindi tayo makakapagbilang! Ano kaya ang tamang sagot?"
            jump prompt_21
        


label scene3_6:
    hide Happy Isra with dissolve

    show Happy Isra at left, lighten with dissolve
    show Lala Standing at right, darken with dissolve
    voice "isra/isra_line17.mp3"
    i "Apaka-galing mo magbilang! Lala, ibalik mo na ang bola!"

    hide Lala Standing with dissolve
    voice "isra/isra_18.mp3"
    i "Hala, hindi parin bumabalik si Lala. Siguro, nagtatago siya! Ano ang ibig sabihin ng salitang 'nagtatago'?"

    show Happy Isra at center, with move

    jump prompt_22

label prompt_22:
    menu:
        i "Ano ang ibig sabihin ng salitang 'nagtatago'?"
        "Nagpapakita sa harapan":
            i "Hmm, subukan mong isipin ulit! Kung nagtatago si Lala, makikita ko ba siya agad?"
            jump prompt_22

        "Hindi nagpapakita o nagkukubli":
            i "Magaling! Ang 'nagtatago' ay nangangahulugang hindi nagpapakita o nagkukubli. Isa itong pandiwa, dahil ito ay isang kilos na maaaring gawin ng isang tao o hayop!"
            jump scene3_7

        "Tumatalon nang mataas":
            i "Hmm, subukan mong isipin ulit! Kung nagtatago si Lala, makikita ko ba siya agad?"
            jump prompt_22
        

label scene3_7:
    hide Happy Isra with dissolve

    show Happy Isra at left, lighten with dissolve
    voice "isra/isra_21.mp3"
    i "Hay nako, Lala! Hindi pa nga tayo tapos ngunit iba na ang inilalaro mo! (masiglang tumawa) Tara, mga kaibigan! Hanapin natin si Lala."

    jump scene3_7


label scene3_7:

    scene bg backyard
    with dissolve

    show Scared Isra at left, lighten with dissolve
    voice "isra/isra_22.mp3"
    i "Lala! Lala! Kanina pa tayo naghahanap ngunit hindi parin natin nakikita si Lala. Nag-aalala na ako…"

    show Scared Isra at left, darken with dissolve
    voice "lala/arf.mp3"
    l "Arf, arf, arf!"  

    show Scared Isra at left, lighten with dissolve
    voice "isra/isra_23.mp3"
    i "Nako! Si Lala! Mukhang nangangailangan ng tulong ni Lala, mukhang narinig ko ang kanyang mga tahol doon!"

    hide Scared Isra with dissolve

    show Lala Sitting at left, darken with dissolve
    show Angry Batang Lalaki 2 at right, darken with dissolve
    show Angry Batang Lalaki 1 at slightright, lighten with dissolve
    voice "bl1/line1.mp3"
    b1 "Ang pangit mong aso! Umalis ka rito!"

    show Angry Batang Lalaki 1 at slightright, darken with dissolve
    show Angry Batang Lalaki 2 at right, lighten with dissolve
    voice "bl2/line1.mp3"
    b2 "Oo nga! Bakit nandito ’yan?"

    show Angry Batang Lalaki 2 at right, darken with dissolve
    show Lala Sitting at slightleft, darken with move
    show Calm Isra at left, lighten with dissolve
    voice "isra/isra_24.mp3"
    i "Huwag niyo siyang saktan! Aso ko siya at hindi siya masama! Nako, Lala…ano ang ginawa nila sa’yo.."

    show Calm Isra at left, darken with dissolve
    show Angry Batang Lalaki 1 at slightright, lighten with dissolve
    voice "bl1/line2.mp3"
    b1 "Anong sinaktan? Wala kaming ginawa sa kaniya dahil siya ang unang lumapit sa amin!"

    show Angry Batang Lalaki 1 at slightright, darken with dissolve
    show Angry Batang Lalaki 2 at right, lighten with dissolve
    voice "bl2/line2.mp3"
    b2 "Oo nga! Kami ang unang nakakuha ng pulang bola kaya amin na ito, ngunit napaka-kulit ng iyong aso."
    
    show Angry Batang Lalaki 2 at right, darken with dissolve
    show Curious Isra at left, lighten with dissolve
    hide Calm Isra with dissolve
    voice "isra/isra_25.mp3"
    i "Hindi niyo ba nakikita ang ginawa niyo sa aking aso? Mga kaibigan, ano ba ang kahulugan ng salitang 'saktan'?"

    hide Lala Sitting with dissolve
    hide Angry Batang Lalaki 1 with dissolve
    hide Angry Batang Lalaki 2 with dissolve
    show Curious Isra at center, with move

    jump prompt_23

label prompt_23:

    menu:
        i "ano ba ang kahulugan ng salitang 'saktan'?"
        "Alagaan at mahalin":
            i "Hmm, mukhang nagkamali ka. Ang 'saktan' ay isang kilos na hindi maganda. Subukan mong pumili ulit!"
            jump scene3_8

        "Bigyan ng laruan":
            i "Hmm, mukhang nagkamali ka. Ang 'saktan' ay isang kilos na hindi maganda. Subukan mong pumili ulit!"
            jump prompt_23

        "Pasakitan o gawan ng masama":
            i "Tama! Ang 'saktan' ay nangangahulugang pasakitan o gawan ng masama. Isa itong pandiwa, dahil ito ay isang kilos na maaaring gawin ng isang tao."
            jump prompt_23
        


label scene3_8:
    
    hide Curious Isra with dissolve

    show Calm Isra at left, darken with dissolve
    show Lala Sitting at slightleft, darken with dissolve
    show Angry Batang Lalaki 1 at slightright, lighten with dissolve
    show Angry Batang Lalaki 2 at right, darken with dissolve
    voice "bl1/line3.mp3"
    b1 "Hindi naman namin siya sinaktan, sadyang kinukuha lamang ng aso mo ang laruan namin!"

    show Angry Batang Lalaki 1 at slightright, darken with dissolve
    show Calm Isra at left, lighten with dissolve
    voice "isra/isra_28.mp3"
    i "Ang bolang iyan ay sa amin. Tignan mo, may palatandaan ang bola na yan, ang pangalan namin ni Lala!" 

    show Calm Isra at left, darken, with dissolve
    show Angry Batang Lalaki 2 at right, lighten with dissolve
    voice "bl2/line3.mp3"
    b2 "Nye-nye-nye-nye-nye! Subukan mo munang kuhanin mula sa amin, kung maaabot mo kami!"
    hide Angry Batang Lalaki 2 with moveoutright
    hide Angry Batang Lalaki 1 with moveoutright

    show Calm Isra at left, lighten with dissolve
    voice "isra/isra_29.mp3"
    i "Habuli natin sila, Lala! Hindi tama na kuhanin nila ang hindi naman sa kanila!"

    show Calm Isra at left, darken with dissolve
    show Lala Sitting at slightleft, lighten with dissolve
    voice "lala/arf.mp3"
    l "Arf! arf!"

    show Lala Sitting at slightleft, darken with dissolve
    voice "bl1/line4.mp3"
    b1 "Aaaaahhhh! Ahaaaaaass!"

    show Calm Isra at left, lighten with dissolve
    voice "isra/isra_30.mp3"
    i "Lala, mukhang andon ang mga kumuha ng ating bola! Tingnan natin kung anong nangyayari doon!"

    show Calm Isra at left, darken with dissolve
    show Lala Sitting at slightleft, lighten with dissolve
    voice "lala/arf.mp3"
    l "Arf, arf!"

    jump scene3_9


label scene3_9:

    scene bg backyard
    with dissolve

    show Angry Ahas at slightleft, darken with dissolve
    show Scared Batang Lalaki 2 at right, darken with dissolve
    show Scared Batang Lalaki 1 at slightright, lighten with dissolve
    voice "bl1/line5.mp3"
    b1 "Tulong! tulong! Hindi kami makababa ng puno, mayroong ahas!"

    show Scared Batang Lalaki 1 at slightright, darken with dissolve
    show Angry Ahas at slightleft, lighten with dissolve
    voice "ahas/line1.mp3"
    a "Ssss…hindi kayo makakababa! akyat-akyat kayo ng puno na hindi naman inyo! Ssss…!"

    show Angry Ahas at slightleft, darken with dissolve
    show Scared Batang Lalaki 2 at right, lighten with dissolve
    voice "bl2/line4.mp3"
    b2 "Lala, Lala, tulong! Puwede mo bang tabuyin ang ahas na iyan? Pangako, babalik namin ang bola!"

    show Scared Batang Lalaki 2 at right, darken with dissolve
    show Curious Isra at left, lighten with dissolve
    voice "isra/isra_31.mp3"
    i "Nako! Paano kaya matutulungan ni Lala ang mga bata na makababa sa puno? Tulong, mga kaibigan! Ano ang dapat gawin ni Lala upang mataboy ang ahas?"

    hide Angry Ahas with dissolve
    hide Scared Batang Lalaki 1 with dissolve
    hide Scared Batang Lalaki 2 with dissolve
    show Curious Isra at center with move

    jump prompt_24

label prompt_24:
    menu:
        i "Ano ang dapat gawin ni Lala upang mataboy ang ahas?"
        "Tahulan":
            i "Tama, Lala! Dapat mong tahulan ang ahas upang matakot ito at lumayo!"
            jump scene3_10

        "Yakapin":
            i "Hmm, hindi yata magandang yakapin ang ahas! Delikado ito, Lala! Ano kaya ang tamang gawin?"
            jump prompt_24

        "Tumakbo":
            i "Kung tatakbo tayo, paano natin matutulungan ang mga bata? Subukan natin ulit!"
            jump prompt_24
        


label scene3_10:
    hide Curious Isra with dissolve

    scene bg backyard
    with dissolve

    show Happy Isra at left, darken with dissolve
    show Lala Standing at slightleft, lighten with dissolve
    show Angry Ahas at right, lighten with dissolve
    voice "lala/arf.mp3"
    l "Arf! Arf!…"
    hide Angry Ahas with moveoutright

    hide Lala Standing with dissolve
    show Lala Sitting at slightleft, darken with dissolve
    show Happy Isra at left, lighten with dissolve
    voice "isra/isra_35.mp3"
    i "Wala na ang ahas, puwede na kayong bumababa!"

    show Happy Isra at left, darken with dissolve
    show Happy Batang Lalaki 1 at slightright, darken with dissolve
    show Happy Batang Lalaki 2 at right, lighten with dissolve
    voice "bl2/line5.mp3"
    b2 "Patawad sa ginawa namin sa inyo kanina, Isra at Lala. Salamat sa pagligtas ninyo sa amin!"

    show Happy Batang Lalaki 2 at right, darken with dissolve
    show Happy Isra at left, lighten with dissolve
    voice "isra/isra_36.mp3"
    i "Okay lang ‘yan, basta huwag niyo nang uulitin ang ginawa niyo kay Lala kasi nasasaktan at natatakot din ang mga hayop"
    
    show Happy Isra at left, darken with dissolve
    show Lala Sitting at slightleft, lighten with dissolve
    voice "lala/arf.mp3"
    l "Arf, arf, arf!"

    show Lala Sitting at slightleft, darken with dissolve
    show Happy Batang Lalaki 1 at slightright, lighten with dissolve
    voice "bl1/line6.mp3"
    b1 "Puwede ba kaming makipaglaro sa inyong dalawa upang makabawi?"

    show Happy Batang Lalaki 1 at slightright, darken with dissolve
    show Happy Isra at left, lighten with dissolve
    voice "isra/isra_37.mp3"
    i "Lala, gusto mo pa ba maglaro ng batong-bata?"    

    show Happy Isra at left, darken with dissolve
    show Lala Sitting at slightleft, lighten with dissolve
    voice "lala/arf.mp3"
    l "Arf, arf!"

    show Lala Sitting at slightleft, darken with dissolve
    show Happy Batang Lalaki 2 at right, lighten with dissolve
    voice "bl2/line6.mp3"
    b2 "Mukhang gusto pa ni Lala maglaro!"

    show Happy Batang Lalaki 2 at right, darken with dissolve
    show Happy Batang Lalaki 1 at slightright, lighten with dissolve
    voice "bl1/line7.mp3"
    b1 "Paunahan tayo bumalik sa palaruan, handa ka na ba, Lala?"

    show Happy Batang Lalaki 1 at slightright, darken with dissolve
    show Lala Sitting at slightleft, lighten with dissolve
    voice "lala/arf.mp3"
    l "Arf, arf!"

    show Lala Sitting at slightleft, darken with dissolve
    show Happy Batang Lalaki 2 at right, lighten with dissolve
    voice "bl2/line7.mp3"
    b2 "Hintayin mo kami, Lala!"

    show Happy Batang Lalaki 2 at right, darken with dissolve
    show Happy Isra at left, lighten with dissolve
    voice "isra/isra_38.mp3"
    i "Mukhang may bago nanamang mga kaibigan si Lala! Hanggang dito na lamang tayo maglalaro, mga kaibigan!"

    show Happy Isra at left, darken with dissolve
    show Happy Batang Lalaki 1 at slightright, lighten with dissolve
    voice "bl1/line8.mp3"
    b1 "Tara na, Isra!"

    show Happy Batang Lalaki 1 at slightright, darken with dissolve
    show Happy Isra at left, lighten with dissolve
    voice "isra/isra_39.mp3"
    i "Hanggang sa muli, paalam!"

    jump story_3_ending

label story_3_ending:

    scene bg backyard
    with dissolve

    show Happy Isra at left, lighten with dissolve
    show Lala Sitting at right, darken with dissolve
    voice "isra/isra_40.mp3"
    i "Salamat sa pakikisama sa amin ni Lala! Sana’y kayo ay nag-enjoy! Dahil dito natutunan natin kung ano ang mga salitang kilos o “pandiwa.” Ano nga ba muli ang pandiwa?"

    hide Lala Sitting with dissolve
    show Happy Isra at center, with move
    jump prompt_25

label prompt_25:

    menu:
        i "Ano nga ba muli ang pandiwa?"
        "Salitang nagsasaad ng kilos":
            i "Tama! Ang pandiwa ay salitang nagsasaad ng kilos o galaw, tulad ng ihagis, tumakbo, at tahulan! Ang galing mo!"
            jump scene3_11

        "Pangalan ng tao, lugar, o bagay":
            i "Hmm, hindi! Ang pangalan ng tao, lugar, o bagay ay tinatawag na pangngalan. Subukan ulit!"
            jump prompt_25

        "Salitang naglalarawan ng kulay o hugis":
            i "Hindi rin! Ang mga salitang naglalarawan ng kulay o hugis ay tinatawag na pang-uri. Ano kaya ang tamang sagot?"
            jump prompt_25

label scene3_11:

    hide Happy Isra with dissolve

    show Happy Isra at left, lighten with dissolve
    show Lala Sitting at right, darken with dissolve

    voice "isra/isra_44.mp3"
    i "Dahil kilala mo na si Lala at ang kanyang makulit na buntot, ano ang kahulugan ng salitang kumakawag, ang salita na ginamit natin sa kilos ng kanyang buntot? "

    hide Lala Sitting with dissolve
    show Happy Isra at center, with move

    jump prompt_26

label prompt_26:

    menu:
        i "ano ang kahulugan ng salitang kumakawag, ang salita na ginamit natin sa kilos ng kanyang buntot?"
        "Nananahimik sa isang sulok":
            i "Hindi! Ang isang bagay o hayop na nananahimik ay hindi gumagalaw. Subukan mong muli!"
            jump prompt_26

        "Sumisipa ng bola":
            i "Hindi! Ang taong o hayop na natutulog ay hindi kumikilos. Subukan mong muli!"
            jump prompt_26

        "Gumagalaw nang masigla":
            i  "Tama! Ang kumakawag ay kilos ng pagbibigay ng kasiyahan o sigla, tulad ng pagkilos ng buntot ng isang aso!"
            jump scene3_12
        

label scene3_12:

    hide Happy Isra with dissolve  

    show Happy Isra at left, lighten with dissolve
    show Lala Sitting at right, darken with dissolve

    voice "isra/isra_48.mp3"
    i "Kanina, tayo ay naglaro ng batong-bata, kung saan gumamit tayo ng bola at ito ay ating inihagis. Ano ang ibig sabihin ng 'Ihagis'?"

    hide Lala Sitting with dissolve
    show Happy Isra at center, with move

    jump prompt_27


label prompt_27:
    menu:
        i "Ano ang ibig sabihin ng 'ihagis'?"
        "Hawakan ito sa kamay":
            i "Hindi! Ang paghawak ay hindi nangangahulugang paghagis. Ano kaya ang tamang sagot?"
            jump prompt_27

        "Itapon ang isang bagay papalayo gamit ang kamay":
            i "Tama! Ang ihagis ay kilos ng pagtatapon o pagpapalipad ng isang bagay papalayo!"
            jump scene3_13

        "Itikom ang bibig":
            i "Hindi! Wala itong kinalaman sa bola. Subukan mong muli!"
            jump prompt_27
        


label scene3_13:

    hide Happy Isra with dissolve  

    show Happy Isra at left, lighten with dissolve
    show Lala Sitting at right, darken with dissolve

    voice "isra/isra_52.mp3"
    i "Pagkatapos natin i-bato ang bola at magbilang, biglang nawala si Lala! Akala natin siya ay nagtatago noon ngunit nasa panganib na pala ang ating kaibigang aso. Ano ang ibig sabihin ng 'nagtatago'?"

    hide Lala Sitting with dissolve
    show Happy Isra at center, with move

    jump prompt_28


label prompt_28:
    menu:
        i "Ano ang ibig sabihin ng salitang 'nagtatago'?"
        "Nagpapakita sa harapan":
            i "Hmm, subukan mong isipin ulit! Kung nagtatago si Lala, makikita ko ba siya agad?"
            jump prompt_28

        "Hindi nagpapakita o nagkukubli":
            i "Magaling! Ang 'nagtatago' ay nangangahulugang hindi nagpapakita o nagkukubli. Isa itong pandiwa, dahil ito ay isang kilos na maaaring gawin ng isang tao o hayop!"
            jump scene3_14

        "Tumatalon nang mataas":
            i "Hmm, subukan mong isipin ulit! Kung nagtatago si Lala, makikita ko ba siya agad?"
            jump prompt_28
        
    

label scene3_14:

    hide Happy Isra with dissolve  

    show Happy Isra at left, lighten with dissolve
    show Lala Sitting at right, darken with dissolve

    voice "isra/isra_53.mp3"
    i "Nang makita natin si Lala, siya pala ay inaapi na ng dalawang batang lalaki na kumuha ng kanyang bola! Hindi tama na saktan ang iba, lalo na kung wala naman silang ginagawang masama. Ano ang ibig sabihin ng 'saktan'?"

    hide Lala Sitting with dissolve
    show Happy Isra at center, with move

    jump prompt_29

label prompt_29:

    menu:
        i "Ano ang ibig sabihin ng 'saktan'?"
        "Alagaan at mahalin":
            i "Hindi! Ang pag-aalaga at pagmamahal ay kabaligtaran ng pananakit. Subukan mong muli!"
            jump prompt_29

        "Purihin at pasayahin":
            i "Hindi! Ang purihin at pasayahin ay kilos ng pagpapasaya, hindi pananakit!"
            jump prompt_29

        "Pasakitan o gawan ng masama":
            i "Tama! Ang saktan ay nangangahulugang pasakitan o gawan ng masama. Ito ay kilos na hindi dapat gawin!"
            jump scene3_15
        
    

label scene3_15:

    hide Happy Isra with dissolve  

    show Happy Isra at left, lighten with dissolve
    show Lala Sitting at right, darken with dissolve

    voice "isra/isra_57.mp3"
    i "Akala namin ni Lala na tuluyan na nilang nakuha ang aming bola, ngunit dahil sa isang ahas, kinailangan nila ng ating tulong! Buti na lang at nataboy ni Lala ang ahas matapos niya itong tahulan nang malakas! Ano ang kahulugan ng 'tahulan'?"

    hide Lala Sitting with dissolve
    show Happy Isra at center, with move

    jump prompt_30


label prompt_30:
    menu:
        i "Ano ang kahulugan ng 'tahulan'?"
        "Yakapin ng mahigpit":
            i "Hindi! Ang yakap ay nagpapakita ng pagmamahal, pero ang tahulan ay isang kilos na ginagamit sa babala!"
            jump prompt_30

        "Tumahol upang ipagtanggol o takutin ang iba":
            i "Tama! Ang tahulan ay kilos ng pagtahol upang magbigay babala o ipagtanggol ang sarili!"
            jump scene3_16

        "Paglaruan":
            i "Hindi! Ang paglalaro ay ibang kilos, subukan mong muli!"
            jump prompt_30

label scene3_16:

    hide Happy Isra with dissolve

    scene bg backyard
    with dissolve

    show Happy Isra at left, lighten with dissolve
    show Lala Sitting at right, darken with dissolve
    voice "isra/isra_60.mp3"
    i "Napakasama niyo talaga kasama, mga kabigan! Tapos na ang araw ng laro, pero bago tayo magtapos, nais ko lang ipaalala sa inyo ang mga natutunan natin!"

    voice "isra/isra_61.mp3"
    i "Una, natutunan natin kung ano ang pandiwa. Ang mga pandiwa ay mga salitang nagsasaad ng kilos, tulad ng 'kumakawag', 'ihagis', 'nagtatago', 'saktan', at 'tahulan'."

    show Happy Isra at left, darken with dissolve
    show Lala Sitting at right, lighten with dissolve
    voice "lala/arf.mp3"
    l "Arf, arf!"

    show Lala Sitting at right, darken with dissolve
    show Happy Isra at left, lighten with dissolve
    voice "isra/isra_62.mp3"
    i "At siyempre, natutunan din natin na mahalaga ang pagtulong sa mga kaibigan at mga hayop. Hindi tamang saktan ang iba, at ang pagtahol ni Lala sa ahas ay tumulong sa atin upang maprotektahan ang mga bata!"

    show Happy Isra at left, darken with dissolve
    show Lala Sitting at right, lighten with dissolve
    voice "lala/arf.mp3"
    l "Arf, arf!"

    show Lala Sitting at right, darken with dissolve
    show Happy Isra at left, lighten with dissolve
    voice "isra/isra_63.mp3"
    i "Salamat sa pagsama sa amin ni Lala sa araw na ito. Huwag kalimutan, laging maging mabait at magalang, at gamitin ang mga pandiwa sa tamang paraan. Hanggang sa muli, mga kaibigan! Paalam at mag-enjoy sa inyong araw!"

    show Happy Isra at left, darken with dissolve
    show Lala Sitting at right, lighten with dissolve
    voice "lala/arf.mp3"
    l "Arf, arf!"

    # This ends the game.

    return

