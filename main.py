from random import randint

def finish():
    global finish_game

    win_condition = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    ver2 = 0
    while(ver2 < 8):
        j = 0
        while(j < 2):
            i,win = 0,0
            while(i < 3):
                if states[win_condition[ver2][i]] == player[j]:
                    win += 1
                i += 1
            if win == 3:
                finish_game = True
                layout()
                print('Jogador {} ganhou o jogo'.format(player[j]))
                pass
            j += 1
        ver2 += 1

    if(finish_game == False):    
        ver = 0
        for state in states:
            if state != ' ':
                ver = ver + 1
            if ver == 9:
                print('Partida deu empate!')
                finish_game = True

def layout():
    print('{}|{}|{}'.format(states[0], states[1], states[2]))
    print('-------')
    print('{}|{}|{}'.format(states[3], states[4], states[5]))
    print('-------')
    print('{}|{}|{}'.format(states[6], states[7], states[8]))

def play():

    global states
    global finish_game
    global player
    states = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player = ['X','O']
    player_play = randint(0,1)

    finish_game = False
    while (finish_game == False):
        layout()
        choose_field = int(input("Jogador [{}]:  ".format(player[player_play])))
        
        if states[choose_field] != player[0] and states[choose_field] != player[1]:
            if player_play == 0:
                states[choose_field] = player[0]
                player_play = 1
            else:
                states[choose_field] = player[1] 
                player_play = 0
        finish()
play()
