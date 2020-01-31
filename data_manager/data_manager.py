import os

from display_in_console import show


def exit_game():
    print("Exit")
    print()
    exit()


def get_available_langs_from_filenames():
    langs = dict()
    i = 1
    for f_name in os.listdir("./languages/"):
        if f_name.endswith(".py"):
            langs.update({str(i): f_name[:-3]})
            i += 1
    return langs


def ask_language_version():
    langs = get_available_langs_from_filenames()
    show.print_available_languages(langs)
    inp = input("Choose your language by type a number:\n")
    if inp == "q":
        exit_game()
    elif inp not in langs.keys():
        inp = "1"
    return langs[inp]


def ask_yes_no():
    """
    Ask a question that you can answer 'yes' or 'no'
    """
    answer = str()
    counter = 0
    
    while answer not in ["t", "y", "tak", "yes", "aye", "african swallow"]:
        if answer == "q":
            exit_game()
        if counter == 3:
            raise TypeError
        answer = show.opening_question(counter).lower()
        counter += 1

    if answer == "african swallow":
        return "\t\nWhat is the airspeed velocity of an unladen swallow?"


def create_empty_board() -> dict:
    new_board = dict()
    for n in range(1, 10):
        new_board.update({str(n): " "})
    return new_board 


def player_moves(turn, board):
    empty = " "
    limit = 0

    while limit <= 2:
        shot = show.next_move_ask()

        if shot == "q":
            exit_game()

        elif limit == 2:
            show.error_to_many_inputs()
            exit()
    
        elif shot == "TIE fighter":
            board = {"1": "o", "2": "+", "3": "o", "4": "+", "5": "o", "6": "+", "7": "+", "8": "o", "9": "+"}
            move = [board, ['tie']]
            return move, turn

        elif shot == "EMPEROR":
            board = {"1": " ", "2": "+", "3": " ", "4": " ", "5": "+", "6": " ", "7": " ", "8": "+", "9": " "}
            move = [board, ['2', '5', '8']]
            turn = "+"
            return move, turn

        elif shot == "YODA":
            board = {"1": "o", "2": " ", "3": " ", "4": " ", "5": "o", "6": " ", "7": " ", "8": " ", "9": "o"}
            move = [board, ['1', '5', '9']]
            turn = "o"
            return move, turn

        elif shot not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            show.current(board)
            show.error_not_valid_type()
            limit += 1

        elif board[shot] != empty:
            show.current(board)
            show.error_illegal_move()
            limit += 1

        else:
            board[shot] = turn
            move = [board, shot]
            return move, turn


def next_(turn):
    if turn == "+":
        turn = "o"
    else:
        turn = "+"
    return turn


def check_winner(symbol, board):
    """
    takes symbol (string) and actual board (dict)
    :returns: string or False
    """
    empty = ' '
    winner_board = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["1", "4", "7"],
            ["2", "5", "8"],
            ["3", "6", "9"],
            ["1", "5", "9"],
            ["3", "5", "7"]
    ]
    for win_row in winner_board:
        check = 0
        for el in win_row:
            if board[el] == symbol:
                check += 1
                if check == 3:
                    return symbol
    
    if empty not in board.values():
        return "tie"
    
    return False
