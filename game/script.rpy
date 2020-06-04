# Вы можете расположить сценарий своей игры в этом файле.
label main_menu:
    return

image x = Text("x", size=150)
image o = Text("o", size=150)

define return_values = [
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
]

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
                            if state_value is True:
                                add "x" align (0.5, 0.5)
                            elif state_value is False:
                                add "o" align (0.5, 0.5)

label start:
    hide black
    menu:
        "Выбери кем ходишь"
        "По очереди":
            $user_value = None
        "xxxxxxxx":
            $user_value = True
        "oooooooo":
            $user_value = False

    $turn = 0
    # None -> empty, True -> x, False -> o
    $state = [
        [None] * 3,
        [None] * 3,
        [None] * 3,
    ]
    $renpy.watch("turn")
    $renpy.watch("state")

    while turn < 9:
        $turn += 1
        call screen game
        call process(*_return)
    call check_win
    return

label process(column, row):
    "[column], [row]"
    $state[column][row] = user_value
    return

label check_win():
    return
