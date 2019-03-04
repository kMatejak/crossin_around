from display_in_console import show


def ask_yes_no(question):
    """
    Ask a question that you can answer 'yes' or 'no'
    """
    answer = False
    counter = 0
    
    while answer not in ('t', 'y', 'n', '', 'maciej jest spoko') and counter < 4:
        answer = input(question).lower()
        counter += 1
    
    return answer


def ask_number(question):
    """
    Ask about the number of the selected field
    """
    answer = False
    counter = 0

    while answer not in range(1, 10) and counter < 4:
        answer = int(input(question))
        counter += 1
    return answer


def create_empty_board():
    '''
    :return: dict
    '''
    new_board = {
        '1':' ',
        '2':' ',
        '3':' ',
        '4':' ',
        '5':' ',
        '6':' ',
        '7':' ',
        '8':' ',
        '9':' ',
    }
    return new_board 


def player_moves(turn, board):
    EMPTY = ' '
    move = input('Wskaż pole swojego najazdu: ')
    if move not in ['1','2','3','4','5','6','7','8','9']:
        show.error_not_valid_type()
        raise TypeError
    elif board[move] != EMPTY:
        show.error_illegal_move()
        raise TypeError
    else:
        board[move] = turn
        return board


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
    EMPTY = ' '
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
    
    if EMPTY not in board.values():
        return 'tie'
    
    return False
