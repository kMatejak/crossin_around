from data_manager import data_manager as data
from display_in_console import show
from novation_launchpad_mini import show_on_launchpad as lights


def game():
    # INTRO
    lights.reset_board()
    show.language = data.ask_language_version()
    n = 'cxfdks728%@&*^^'
    while n == 'cxfdks728%@&*^^':
        n = show.instruction()

    # START GAME
    try:
        data.ask_yes_no()
    except TypeError:
        show.error_not_crusader()
        exit()

    turn = '+'
    first_run = True
    board = data.create_empty_board()
    winner = data.check_winner(turn, board)

    # PLAY GAME
    while not winner:
        lights.grid()
        show.current(board, first_run)
        if first_run:
            first_run = False
        move, turn = data.player_moves(turn, board)
        board = move[0]
        shots = move[1]
        lights.box(shots, turn)
        winner = data.check_winner(turn, board)
        turn = data.next_(turn)

    # END GAME
    show.current(board)
    show.congratulation(winner)


if __name__ == '__main__':
    game()
