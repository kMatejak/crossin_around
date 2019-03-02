X = '+'
O = 'o'
EMPTY = ' '
TIE = 'TIE'


def ask_yes_no(question):
    """Ask a question that you can answer 'yes' or 'no'"""
    response = None
    while response not in ('t', 'n', '', 'maciej jest spoko'):
        response = input(question).lower()
    return response


def ask_number(question):
    """Ask about the number of the selected field"""
    response = None
    while response not in SHOTS:
        response = int(input(question))
    return response


def create_new_empty_board():
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


def legal_moves(grid):
    """Create list of legal moves"""
    moves = []
    for field in SHOTS:
        if grid[field] == EMPTY:
            moves.append(field)
    return moves
