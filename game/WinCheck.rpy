if one == 2 and two == 2 and three == 2:  #2/1
    $ player2win = 2
    jump WIN
elif one == 1 and two == 1 and three == 1:  #1/1
    $ player1win = 1
    jump WIN
elif four == 2 and five == 2 and six == 2:  #2/2
    $ player2win = 2
    jump WIN
elif four == 1 and five == 1 and six == 1:  #1/2
    $ player1win = 1
    jump WIN
elif seven == 2 and eight == 2 and nine == 2:  #2/3
    $ player2win = 2
    jump WIN
elif seven == 1 and eight == 1 and nine == 1:  #1/3
    $ player1win = 1
    jump WIN
elif one == 2 and five == 2 and nine == 2:  #2/4
    $ player2win = 2
    jump WIN
elif one == 1 and five == 1 and nine == 1:  #1/4
    $ player1win = 1
    jump win
elif three == 2 and five == 2 and seven == 2:  #2/5
    $ player2win = 2
    jump WIN
elif three == 1 and five == 1 and seven == 1:  #1/5
    $ player1win = 1
    jump WIN
elif one == 2 and four == 2 and seven == 2:  #2/6
    $ player2win = 2
    jump WIN
elif one == 1 and four == 1 and seven == 1:  #1/6
    $ player1win = 1
    jump WIN
elif two == 2 and five == 2 and eight == 2:  #2/7
    $ player2win = 2
    jump WIN
elif two == 1 and five == 1 and eight == 1:  #1/7
    $ player1win = 1
    jump WIN
elif three == 2 and six == 2 and nine == 2:  #2/8
    $ player2win = 2
    jump WIN
elif three == 1 and six == 1 and nine == 1:  #1/8
    $ player1win = 1
    jump WIN
elif turn >= 9:
    jump WIN
else:
    jump PROD
