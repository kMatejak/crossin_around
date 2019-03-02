from data_manager import data_manager as data
from novation_launchpad_mini import show_on_launchpad as launchpad


def game():
# INSTRUCTION
    n = 'cxfdksuj'
    while n == 'cxfdksuj':
        n = show_instruction()
# START GAME
    great_white_space_printer()
    start_game()
    turn = X
    grid = new_grid()
    great_white_space_printer()
    print_player_prod()
    show_grid_template_with_numbers()
    show_grid(grid)

# PLAY GAME
    while not winner(grid):
        if turn == X:
            move = player_moves(grid)
            grid[move] = X
        else:
            move = player_moves(grid)
            grid[move] = O
        great_white_space_printer() 
        show_grid_template_with_numbers()
        show_grid(grid)
        turn = next_turn(turn)
        the_winner = winner(grid)

# END GAME
    congrat_winner(the_winner)


if __name__ = '__main__':
    main()
