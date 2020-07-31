from IPython.display import clear_output

# IPython.display only works for Jupyter notebook

def display_board(board):
    clear_output()  # Remember, this only works in jupyter!
    availableboard=['#','1','2','3','4','5','6','7','8','9']
    print('   Available        TIC-TAC-TOE\n'+
           '     Moves\n\n  '+
          board[7]+'  | '+board[8]+' |  '+board[9]+'        '+availableboard[7]+' | '+availableboard[8]+' | '+availableboard[9]+'\n  '+
          '-----------       -----------\n  '+
          board[4]+'  | '+board[5]+' |  '+board[6]+'        '+availableboard[4]+' | '+availableboard[5]+' | '+availableboard[6]+'\n  '+
          '-----------       -----------\n  '+
          board[1]+'  | '+board[2]+' |  '+board[3]+'        '+availableboard[1]+' | '+availableboard[2]+' | '+availableboard[3]+'\n')



def rules():
    ruleboard=['#','1','2','3','4','5','6','7','8','9']
    clear_output()  # Remember, this only works in jupyter!
    print('The corresponding numbers are representing the input postions.')
    print('To input at the particular position input the numeric number representing the position.\n')
    print('Example Board \n')
    print(' ' + ruleboard[7] + ' | ' + ruleboard[8] + ' | ' + ruleboard[9])
    print('-----------')
    print(' ' + ruleboard[4] + ' | ' + ruleboard[5] + ' | ' + ruleboard[6])
    print('-----------')
    print(' ' + ruleboard[1] + ' | ' + ruleboard[2] + ' | ' + ruleboard[3])

def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O' or marker == 'x' or marker == 'o' or marker == '0' ):
        marker = input('Do you want to be X or O? ')

    if marker.upper() == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

import random

def choose_first():
    if random.randint(0, 2) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):

    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    if num=='1':
        while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
            if turn == 'Player 1':
                position = int(input('Choose your next position: (1-9) '))
            else:
                position = random.randint(1, 10)
    else:
        while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
            if turn == 'Player 1':
                position = int(input('Player-1 choose your next position: (1-9) '))
            else:
                position = int(input('Player-2 choose your next position: (1-9) '))



    return position

def replay():

    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

print('Welcome to Tic Tac Toe!')

num=0

def playernumbers():
    global num
    till=True
    while till:
        num = input('How many players will play? 1 or 2: ')
        if num=='1':
            till=False
        elif num=='2':
            till=False


while True:

    rules()
    playernumbers()
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    if num=='1':
        if turn== 'Player 1':
            print('You will go first.')
        else:
            print('Computer will go first.')
    else:
        print(turn + ' will go first.')
    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations!, You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                if num=='1':
                    print('Computer has won!')
                else:
                    print('Congratulations! Player 2 has won the game.')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break

#end
