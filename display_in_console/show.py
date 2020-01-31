from languages import english, polski


language = str()


def print_white_rows(rows):
    print("\n" * (rows - 1))


def print_available_languages(lang_files_names):
    print()
    for order, name in lang_files_names.items():
        print(f"  {order}. " + name)
    print()


def set_language_version():
    if language == "polski":
        return polski
    else:
        return english


def instruction():
    """show game instruction"""
    lang = set_language_version()
    print('''
     _____                   _       _    ___                            _ 
    /  __ \                 (_)     ( )  / _ \                          | |
    | /  \/_ __ ___  ___ ___ _ _ __ |/  / /_\ \_ __ ___  _   _ _ __   __| |
    | |   | '__/ _ \/ __/ __| | '_ \    |  _  | '__/ _ \| | | | '_ \ / _` |
    | \__/\ | | (_) \__ \__ \ | | | |   | | | | | | (_) | |_| | | | | (_| |
     \____/_|  \___/|___/___/_|_| |_|   \_| |_/_|  \___/ \__,_|_| |_|\__,_|
                                                                       
    ''')
    lang.show_instruction_1()
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
    lang.show_instruction_2()
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
    question = lang.show_instruction_3()
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
    lang = set_language_version()
    print_white_rows(70)
    if counter == 0:
        lang.show_opening_annotation()
    return lang.show_opening_question()


def player_cheer():
    lang = set_language_version()
    print_white_rows(50)
    lang.show_player_cheer()
    print_white_rows(3)


def next_move_ask():
    lang = set_language_version()
    show = lang.show_next_move_ask()
    print_white_rows(70)
    return show


def current(board, is_first_run=False):
    if is_first_run:
        player_cheer()
    else:
        print_white_rows(50)
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

def congratulation(winner):
    if winner == 'o':
        sultan_wins_ending()
    elif winner == '+':
        crusader_wins_ending()
    elif winner == 'tie':
        tie_ending()


def sultan_wins_ending():
    lang = set_language_version()
    print_white_rows(4)
    lang.show_sultan_wins_ending()
    print_white_rows(3)


def crusader_wins_ending():
    lang = set_language_version()
    print_white_rows(4)
    lang.show_crusader_wins_ending()
    print_white_rows(3)


def tie_ending():
    lang = set_language_version()
    print_white_rows(4)
    lang.show_tie_ending()
    print_white_rows(3)


# ERRORS

def error_illegal_move():
    lang = set_language_version()
    lang.show_error_illegal_move()


def error_not_valid_type():
    lang = set_language_version()
    lang.show_error_not_valid_type()


def error_not_crusader():
    lang = set_language_version()
    print_white_rows(70)
    lang.show_error_not_crusader()
    print_white_rows(3)


def error_to_many_inputs():
    lang = set_language_version()
    print_white_rows(70)
    lang.error_to_many_inputs()
    print_white_rows(3)
