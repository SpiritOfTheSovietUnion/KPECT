# Файл основа
label main_menu:
    return

#используемые фигуры
image x = Text("x", size=150)
image o = Text("o", size=150)

define chara = ".!."

#значения для заполнения игроками
define return_values = [
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
]

#шаблоны победы
define win_values = [
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    ((0, 0), (1, 1), (2, 2)),
    ((2, 0), (1, 1), (0, 2)),
]

#отображаемые фигуры
screen game():
    layer "master"
    frame:
        background Solid("#000")
        padding (25, 25)
        align (0.5, 0.5)
        vbox:
            spacing 10
            for s_row, r_row in zip(state, return_values):
                hbox:
                    spacing 10
                    for state_value, r_value in zip(s_row, r_row):
                        fixed:
                            fit_first True
                            imagebutton:
                                xysize (150, 150)
                                idle Solid("#0ff")
                                hover Solid("#ff0")
                                action Return(r_value)
                            if state_value == "x":
                                add "x" align (0.5, 0.5)
                            elif state_value == "o":
                                add "o" align (0.5, 0.5)
#основа
label start:
    hide black
    $chara = None
    $user_value = None
    menu:
        "Выбери кем ходишь"
        "По очереди":
            $chara = "x"
        "Быть Крестом":
            $chara = "x"
        "Быть полным Нулём":
            $chara = "o"

    $turn = 0
    
    #заполняются в соответствии со знаком
    $state = [
        [None] * 3,
        [None] * 3,
        [None] * 3,
    ]
    $renpy.watch("turn")
    $renpy.watch("state")

    #тело игры
    #до 9 ходов, с 5-го идет проверка на победный ход
    while turn < 9:
        $user_value = chara
        $turn += 1
        if chara == "x":
            $chara = "o"
        else:
            $chara = "x"
        if turn > 5:
            call check_win(state, chara)

        call screen game
        call process(*_return)
    call check_win
    return
    
#вывод текущей колонки хода, чистая проверка
label process(column, row):
    "[column], [row]"
    $state[column][row] = user_value
    return
    
#проверка на победный ход
label check_win(state, chara):
    $inside = []
    $outside = []
    $i = 0
    
    #в теории, должен сравнивать знак(chara) по текущим ходам с уже готовыми шаблонами победы
    #и в случае совпадения, выкидывать текущего пользователя на победный кат
    python:
        """for inside in win_values:
            for outside in inside:
                if state[inside[0], inside[1]] == chara:
                    i += 1
                    continue
                else:
                    i = 0
                    break
            if i == 3:
                renpy.jump("WIN")
        renpy.jump("WIN")"""

    return
    
#Переход на победный кат
label WIN:
    "Поздравляю, игрок за [chara] - ПАДЕБИЛ!!1!"
    return
