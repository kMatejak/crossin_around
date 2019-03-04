from novation_launchpad_mini import launchpad_connection as connection


def reset_board():
    connection.reset_board()


def grid():
    connection.light_grid()


def box(shots, turn):
    if 'tie' in shots:
        connection.reset_board()
        connection.light_grid()
    else:
        for shot in shots:
            if turn == '+':
                color = 'red'
            elif turn == 'o':
                color = 'green'

            connection.light_box(shot, color)
