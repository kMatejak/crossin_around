from languages import polski as pl
from languages import english as en


def white_rows(rows):
    print("\n" * (rows - 1))


def instruction():
    """show game instruction"""
    print('''
     _____                   _       _    ___                            _ 
    /  __ \                 (_)     ( )  / _ \                          | |
    | /  \/_ __ ___  ___ ___ _ _ __ |/  / /_\ \_ __ ___  _   _ _ __   __| |
    | |   | '__/ _ \/ __/ __| | '_ \    |  _  | '__/ _ \| | | | '_ \ / _` |
    | \__/\ | | (_) \__ \__ \ | | | |   | | | | | | (_) | |_| | | | | (_| |
     \____/_|  \___/|___/___/_|_| |_|   \_| |_/_|  \___/ \__,_|_| |_|\__,_|
                                                                       
    ''')
    pl.show_instruction_1()
    print(
        '\n\t\t\t       |       |       ',
        '\n\t\t\t   7   |   8   |   9   ',
        '\n\t\t\t_______|_______|_______',
        '\n\t\t\t       |       |       ',
        '\n\t\t\t   4   |   5   |   6   ',
        '\n\t\t\t_______|_______|_______',
        '\n\t\t\t       |       |       ',
        '\n\t\t\t   1   |   2   |   3   ',
        '\n\t\t\t       |       |       ')
    pl.show_instruction_2()
    print(
        '\n\t\t\t       |       |       ',
        '\n\t\t\t   +   |       |   o   ',
        '\n\t\t\t_______|_______|_______',
        '\n\t\t\t       |       |       ',
        '\n\t\t\t       |   +   |   o   ',
        '\n\t\t\t_______|_______|_______',
        '\n\t\t\t       |       |       ',
        '\n\t\t\t       |       |   +   ',
        '\n\t\t\t       |       |       ')
    question = pl.show_instruction_3()
    return question


# GAME

def board_template_with_numbers():
    print(
        '\n\t\t\t       |       |       ',
        '\n\t\t\t   7   |   8   |   9   ',
        '\n\t\t\t_______|_______|_______',
        '\n\t\t\t       |       |       ',
        '\n\t\t\t   4   |   5   |   6   ',
        '\n\t\t\t_______|_______|_______',
        '\n\t\t\t       |       |       ',
        '\n\t\t\t   1   |   2   |   3   ',
        '\n\t\t\t       |       |       ')


def opening_question(counter):
    white_rows(70)
    if counter == 0:
        pl.show_opening_adnotation()
    return pl.show_opening_question()


def player_cheer():
    white_rows(30)
    pl.show_player_cheer()
    white_rows(3)


def next_move_ask():
    show = pl.show_next_move_ask()
    white_rows(70)
    return show


def current(board):
    white_rows(50)
    board_template_with_numbers()
    print('''
        \t\t       |       |      
        \t\t   {}   |   {}   |   {}
        \t\t_______|_______|_______
        \t\t       |       |       
        \t\t   {}   |   {}   |   {}
        \t\t_______|_______|_______
        \t\t       |       |       
        \t\t   {}   |   {}   |   {}
        \t\t       |       |        '''.format(board['7'], board['8'], board['9'], 
                                               board['4'], board['5'], board['6'], 
                                               board['1'], board['2'], board['3']))


# ENDINGS

def congrat(winner):
    if winner == 'o':
        sultan_wins_ending()
    elif winner == '+':
        crusader_wins_ending()
    elif winner == 'tie':
        tie_ending()


def sultan_wins_ending():
    white_rows(4)
    pl.show_sultan_wins_ending()
    white_rows(6)


def crusader_wins_ending():
    white_rows(4)
    pl.show_crusader_wins_ending()
    white_rows(6)


def tie_ending():
    white_rows(4)
    pl.show_tie_ending()
    white_rows(3)


# ERRORS

def error_illegal_move(): 
    pl.show_error_illegal_move()


def error_not_valid_type():
    pl.show_error_not_valid_type()


def error_not_crusader():
    white_rows(50)
    pl.show_error_not_crusader()
    white_rows(6)

def error_to_many_inputs():
    white_rows(50)
    pl.error_to_many_inputs()
    white_rows(6)
