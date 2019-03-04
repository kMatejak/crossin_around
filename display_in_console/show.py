from languages import polski as pl
from languages import english as en


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
    input(question)


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


def opening_question():
    return pl.show_opening_question()


def player_cheer():
    white_rows(30)
    pl.show_player_cheer()
    white_rows(3)


def next_move_ask():
    return pl.show_next_move_ask()


def white_rows(how_many_rows):
    rows = how_many_rows - 1
    print('\n'*rows)


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


def congrat(winner):
    if winner == 'o':
        sultan_wins_ending()
    elif winner == '+':
        crusader_wins_ending()
    elif winner == 'tie':
        tie_ending()


def sultan_wins_ending():
    return pl.show_sultan_wins_ending()


def crusader_wins_ending():
    return pl.show_crusader_wins_ending()


def tie_ending():
    return pl.show_tie_ending()


def error_illegal_move(): 
    return pl.show_error_illegal_move()


def error_not_valid_type():
    return pl.show_error_not_valid_type()


def not_crusader_error():
    return pl.show_not_crusader_error()
