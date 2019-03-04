from data_manager import data_manager as data
from display_in_console import show
# from novation_launchpad_mini import show_on_launchpad as light

RED = 3
GREEN = 48
EMPTY = ' '


def game():
# INTRO
    # light.reset_board()
    n = 'cxfdks728uj!!pierogi'
    while n == 'cxfdks728uj!!pierogi':
        n = show.instruction()

# START GAME
    turn = '+'
    board = data.create_empty_board()
    try:
        data.ask_yes_no('Czy jesteś Krzyżowcem?')
    except:
        exit
    show.player_cheer()
    show.current(board)
    check_winner = data.check_winner(turn, board)

# PLAY GAME
    while not check_winner:
        try:
            board = data.player_moves(turn, board)
        except:
            pass
        show.current(board)
        check_winner = data.check_winner(turn, board)
        turn = data.next_(turn)

# END GAME
    show.congrat(check_winner)
    print('END')


if __name__ == '__main__':
    game()




# daj postawic znak sprawdzjac czy pole wolne
# zmien znak na inny i daj postawic w wolnym polu
# sprawdzaj caly czas czy ktos wygral
# wyswietl gratulacja dla zwuciezcy lub oglos remis