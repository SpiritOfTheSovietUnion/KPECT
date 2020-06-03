# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define ii = Character('ИИ', color="#ffcccc", what_color="feee74")

define turn = 0

define player1win = 0
define player2win = 0

define one = 0
define two = 0
define tree = 0
define four = 0
define five = 0
define six = 0
define seven = 0
define eight = 0
define nine = 0

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:


    ii "Вы попали в Симмуляцию."

    ii "Располагайтесь удобнее, время первого теста!"

    ii "Вы уже готовы?"

label choose:

    menu:

        "Да, готов.":
            ii "Перемещаю.."
            jump starting
        "Ещё не готов.":

            ii "Жаль. Вы уверены?"

            ii "Обдумайте вопрос ещё раз"

            jump choose


label starting:

    ii "Самое времяя запустить матч против другого игрока"

    call screen KPECT

label minigame:

    if turn >= 5:
        call WinCheck

    else:
        jump PROD

label PROD:
    call screen KPECT
    jump PROM

label PROM:
#######################################
    if one == 2:
        show NULL:
            xpos 120, ypos 135
    elif one == 1:
        show IKS:
            xpos 120, ypos 135
    else:
        jump minigame
########################################
    if two == 2:
        show NULL:
            xpos 350, ypos 135
    elif two == 1:
        show IKS:
            xpos 350, ypos 135
    else:
        jump minigame
########################################
    if three == 2:
        show NULL:
            xpos 570, ypos 135
    elif three == 1:
        show IKS:
            xpos 570, ypos 135
    else:
        jump minigame
#######################################
    if four == 2:
        show NULL:
            xpos 120, ypos 385
    elif four == 1:
        show IKS:
            xpos 120, ypos 385
    else:
        jump minigame
########################################
    if five == 2:
        show NULL:
            xpos 350, ypos 385
    elif five == 1:
        show IKS:
            xpos 350, ypos 385
    else:
        jump minigame
########################################
    if six == 2:
        show NULL:
            xpos 570, ypos 385
    elif six == 1:
        show IKS:
            xpos 570, ypos 385
    else:
        jump minigame
########################################
    if seven == 2:
        show NULL:
            xpos 120, ypos 570
    elif seven == 1:
        show IKS:
            xpos 120, ypos 570
    else:
        jump minigame
########################################
    if eight == 2:
        show NULL:
            xpos 350, ypos 570
    elif eight == 1:
        show IKS:
            xpos 350, ypos 570
    else:
        jump minigame
########################################
    if seven == 2:
        show NULL:
            xpos 570, ypos 570
    elif seven == 1:
        show IKS:
            xpos 570, ypos 570
    else:
        jump minigame
########################################

label ONE:


    $ turn += 1
    jump minigame

label TWO:


    $ turn +=1
    jump minigame

label THREE:


    $ turn += 1
    jump minigame

label FOUR:


    $ turn += 1
    jump minigame

label FIVE:


    $ turn += 1
    jump minigame

label SIX:


    $ turn += 1
    jump minigame

label SEVEN:


    $ turn += 1
    jump minigame

label EIGHT:


    $ turn += 1
    jump minigame

label NINE:


    $ turn += 1
    jump minigame

label WinCheck:

    ii "..."
    ii "..."
    ii "..."

label WIN:
    if player2win == 2:
        ii "Второй игрок победил"
    elif player1win == 1:
        ii "Игрок, начинавший партию, победил"
    else:
        ii "Похоже, вы сыграли в ничью"

    jump END

label END:
