from novation_launchpad_mini import launchpad_connection as connection


def reset_board():
    try:
        connection.reset_board()
    except:
        pass


def grid():
    try:
        connection.light_grid()
    except:
        pass


def box(shots, turn):
    try:
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
    except:
        pass
