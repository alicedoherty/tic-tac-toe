game_finished = False
counter = 'X'

# Elements in board not stored in same order they're printed (to allow for easier coordinate checking in
# check_coordinates(), see nice_board below.
board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_'],
]

# nice_board has elements in array in same position as they are printed i.e nice_board[0] is the top-left of board.
nice_board = [
    board[0][2], board[1][2], board[2][2],
    board[0][1], board[1][1], board[2][1],
    board[0][0], board[1][0], board[2][0],
]


def update_board():
    global nice_board
    nice_board = [
        board[0][2], board[1][2], board[2][2],
        board[0][1], board[1][1], board[2][1],
        board[0][0], board[1][0], board[2][0],
    ]


def print_board():
    print('---------')
    print('|', nice_board[0], nice_board[1], nice_board[2], '|')
    print('|', nice_board[3], nice_board[4], nice_board[5], '|')
    print('|', nice_board[6], nice_board[7], nice_board[8], '|')
    print('---------')


def check_coordinates():
    finished = False
    while not finished:
        x, y = input('Enter coordinates: ').split()
        if x.isdigit() and y.isdigit():
            x = int(x)
            y = int(y)
            if x < 1 or x > 3 or y < 1 or y > 3:
                print('Coordinates should be from 1 to 3!')
            else:
                if board[x - 1][y - 1] == 'X' or board[x - 1][y - 1] == 'O':
                    print('This cell is occupied! Choose another one!')
                else:
                    global counter
                    board[x - 1][y - 1] = counter
                    update_board()
                    print_board()
                    finished = True
                    if counter == 'X':
                        counter = 'O'
                    else:
                        counter = 'X'
        else:
            print('You should enter numbers!')


def check_win():
    global game_finished
    x_win = False
    o_win = False
    impossible = False
    draw = False

    # Check for horizontal win
    for i in range(3):
        if nice_board[0 + (i * 3)] == nice_board[1 + (i * 3)] == nice_board[2 + (i * 3)] and not nice_board[0 + (
                i * 3)] == '_':
            if nice_board[0 + (i * 3)] == 'X':
                x_win = True
            elif nice_board[0 + (i * 3)] == 'O':
                o_win = True

    # Check for vertical win
    for i in range(3):
        if nice_board[0 + i] == nice_board[3 + i] == nice_board[6 + i] and not nice_board[0 + i] == '_':
            if nice_board[0 + i] == 'X':
                x_win = True
            elif nice_board[0 + i] == 'O':
                o_win = True

    # Check for diagonal win
    if nice_board[0] == nice_board[4] == nice_board[8] and not nice_board[0] == '_':
        if nice_board[0] == 'X':
            x_win = True
        elif nice_board[0] == 'O':
            o_win = True
    if nice_board[2] == nice_board[4] == nice_board[6] and not nice_board[2] == '_':
        if nice_board[0] == 'X':
            x_win = True
        elif nice_board[0] == 'O':
            o_win = True

    # Check for a draw
    if nice_board.count('_') == 0 and not o_win and not x_win:
        draw = True

    # Check if game is finished
    if nice_board.count('_') != 0 and not o_win and not x_win:
        game_finished = False

    # Check if the play is impossible (not relevant for current game input method)
    x_count = nice_board.count('X')
    o_count = nice_board.count('O')
    if (abs(x_count - o_count) > 1) or (x_win and o_win):
        impossible = True

    if impossible:
        print('Impossible')
    elif x_win:
        print('X wins')
        game_finished = True
    elif o_win:
        print('O wins')
        game_finished = True
    elif draw:
        print('Draw')
        game_finished = True
    elif not game_finished:
        print('Game not finished')


print('''Coordinates are: 
(1,3) (2,3) (3,3)
(1,2) (2,2) (3,2)
(1,1) (2,1) (3,1)
''')

print_board()

while not game_finished:
    check_coordinates()
    check_win()
