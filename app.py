from data_manager import data_manager as data
from display_in_console import show
from novation_launchpad_mini import show_on_launchpad as light

RED = 3
GREEN = 48
EMPTY = ' '


def game():
# INTRO
    n = 'cxfdks728uj!!pierogi'
    while n == 'cxfdks728uj!!pierogi':
        n = show.instruction()

# START GAME
    turn = '+'
    # winner = 
    board = data.create_empty_board()

    show.player_cheer()
    show.current(board)

# PLAY GAME
    while EMPTY in board:
        try:
            board = data.player_moves(turn, board)
        except:
            pass   
        show.current(board)
        #winner = data.winner(turn)
        turn = data.next_turn(turn)

# END GAME
    print('END')
    #show.congrat(winner)


if __name__ == '__main__':
    game()




# daj postawic znak sprawdzjac czy pole wolne
# zmien znak na inny i daj postawic w wolnym polu
# sprawdzaj caly czas czy ktos wygral
# wyswietl gratulacja dla zwuciezcy lub oglos remis