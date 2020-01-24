from display_in_console import show


def ask_language_version():
    pass


def ask_yes_no():
    """
    Ask a question that you can answer 'yes' or 'no'
    """
    answer = False
    counter = 0
    
    while answer not in ['t', 'y', 'tak', 'yes', 'maciej jest spoko']:
        if counter == 3:
            raise TypeError
        answer = show.opening_question(counter).lower()
        counter += 1
    
    return answer


def create_empty_board() -> dict:
    new_board = dict()
    for n in range(1, 10):
        new_board.update({n: " "})
    return new_board 


def player_moves(turn, board):
    empty = ' '
    limit = 0

    while limit <= 2:
        shot = show.next_move_ask()

        if limit == 2:
            show.error_to_many_inputs()
            exit()
    
        elif shot == 'TIE fighter':
            board = {'1':'o','2':'+','3':'o','4':'+','5':'o','6':'+','7':'+','8':'o','9':'+'}
            move = [board, ['tie']]
            return move

        elif shot == 'EMPEROR':
            board = {'1':' ','2':'+','3':' ','4':' ','5':'+','6':' ','7':' ','8':'+','9':' '}
            move = [board, ['2','5','8']]
            return move

        elif shot == 'YODA':
            board = {'1':'o','2':' ','3':' ','4':' ','5':'o','6':' ','7':' ','8':' ','9':'o'}
            move = [board, ['1','5','9']]
            return move

        elif shot not in ['1','2','3','4','5','6','7','8','9']:
            show.error_not_valid_type()
            limit += 1

        elif board[shot] != empty:
            show.error_illegal_move()
            limit += 1

        else:
            board[shot] = turn
            move = [board, shot]
            return move


def next_(turn):
    if turn == '+':
        turn = 'o'
    else:
        turn = '+'
    return turn


def check_winner(symbol, board):
    '''
    takes symbol (string) and actual board (dict)
    :returns: string or False 
    '''
    empty = ' '
    winner_board = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['1', '4', '7'],
        ['2', '5', '8'],
        ['3', '6', '9'],
        ['1', '5', '9'],
        ['3', '5', '7']
    ]
    for win_row in winner_board:
        check = 0
        for el in win_row:
            if board[el] == symbol:
                check += 1
                if check == 3:
                    return symbol
    
    if empty not in board.values():
        return 'tie'
    
    return False
