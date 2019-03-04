from data_manager import data_manager as data
from display_in_console import show
# from novation_launchpad_mini import show_on_launchpad as light

RED = 3
GREEN = 48


def game():
# INTRO
    # light.reset_board()
    n = 'cxfdks728%@&*^^'
    while n == 'cxfdks728%@&*^^':
        n = show.instruction()

# START GAME
    try:
        data.ask_yes_no()
    except:
        show.error_not_crusader()
        exit()
    
    turn = '+'
    board = data.create_empty_board()
    show.player_cheer()
    winner = data.check_winner(turn, board)

# PLAY GAME
    while not winner:
        show.current(board)
        board = data.player_moves(turn, board)
        winner = data.check_winner(turn, board)
        turn = data.next_(turn)

# END GAME
    show.current(board)
    show.congrat(winner)


if __name__ == '__main__':
    game()
