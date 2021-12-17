import random

def display_board(board):
    print ( "   |   |   ")
    print (" "+board[7]+" | "+board[8]+" | "+board[9]+"  ")
    print ("   |   |")
    print ("---|---|---")
    print ("   |   |")
    print (" "+board[4]+" | "+board[5]+" | "+board[6]+"  ")
    print ("   |   |")
    print ("---|---|---")
    print ("   |   |")
    print (" "+board[1]+" | "+board[2]+" | "+board[3]+"  ")
    print ("   |   |   ")


def player_input():
    marker1 = 'Wrong'
    while marker1 not in ['X','O']:
        marker1 = input("Escoge el simbolo que quieres ser: ").upper()
        if marker1 not in ['X','O']:
            print('Simbolo no valido, Escoge X o O ')
    if marker1 == 'X':
        marker2 = 'O'
    else:
        marker2 = 'X'
    return (marker1, marker2)

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[1] == mark and board[4] == mark and board[7] == mark) or 
    (board[2] == mark and board[5] == mark and board[8] == mark) or 
    (board[3] == mark and board[6] == mark and board[9] == mark) or 
    (board[1] == mark and board[5] == mark and board[9] == mark) or 
    (board[3] == mark and board[5] == mark and board[7] == mark))


def choose_first():
    orden = random.randint(1,2)
    if orden == 1:
        return 'Jugador 1 va primero'
    else:
        return 'Jugador 2 va primero'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(0,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Selecciona tu siguiente posicion: "))
    return position

def replay():
    reset = 'wrong'
    while reset not in ['Y','N']:
        reset = input("Desea volver al jugar, Y or N: ")
        if reset.upper() not in ['Y','N']:
            print('Seleccione Y o N')
    if reset == 'Y':
        return True
    else:
        return False

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    theboard = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn)
    
    play_game = input("Desea empezar el juego: Si o No ")
    if play_game.lower()[0] == 's':
        game_on = True
    else:
        game_on = False

    while game_on:
        #Player 1 Turn
        if turn == 'Jugador 1 va primero':
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard, player1_marker, position)
            
            if win_check(theboard,player1_marker):
                display_board(theboard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Jugador 2 va primero'

        else:
            # Player2's turn.
            
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard, player2_marker, position)

            if win_check(theboard, player2_marker):
                display_board(theboard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Jugador 1 va primero'

    if not replay():
        break