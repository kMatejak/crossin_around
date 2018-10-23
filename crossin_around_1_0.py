# GLOBAL VALUES
X = '+'
O = 'o'
EMPTY = ' '
TIE = 'TIE'
GRID_SIZE = 9

# PROGRAM
def display_instruct():
    """show game instruction"""
    print('''
     _____                   _       _    ___                            _ 
    /  __ \                 (_)     ( )  / _ \                          | |
    | /  \/_ __ ___  ___ ___ _ _ __ |/  / /_\ \_ __ ___  _   _ _ __   __| |
    | |   | '__/ _ \/ __/ __| | '_ \    |  _  | '__/ _ \| | | | '_ \ / _` |
    | \__/\ | | (_) \__ \__ \ | | | |   | | | | | | (_) | |_| | | | | (_| |
     \____/_|  \___/|___/___/_|_| |_|   \_| |_/_|  \___/ \__,_|_| |_|\__,_|
                                                                       
    ''')
    print('\tSułtan Kefiratu pomny o zniewagę jakiej doznał, wyzwał na poje-\n' \
    '\tdynek dzielnego Krzyżowca Ogórkomira. Wciel się w rolę waleczn-\n' \
    '\tego Krzyżowca lub bezwględnego Sułtana i wgnieć swojego przeci-\n' \
    '\twnika w piaski pustyni.\n\n' \
    '\tDostępna jest plansza składająca się z 9 pól, na których rozeg-\n' \
    '\tra się ta krwawa walka. Krzyżowiec krzyżuje (jakżeby inaczej),\n' \
    '\ta Sułtan puszcza toksyczne kółka z fajki wodnej. Ruch odbywa\n' \
    '\tsię na zmianę poprzez wskazanie współrzędnych pustego pola.\n')
    print('''\tZwyciężysz, o ile zajmiesz trzy sąsiadujące ze sobą pola: 
        poziomo, pionowo lub ukośnie. 

        Twój przykładowy tryumf może wyglądać tak

                 1       2       3
                     |       |
            1    +   |       |   o  
              _______|_______|_______
                     |       |
            2        |   +   |   o
              _______|_______|_______
                     |       |
            3        |       |   + 
                     |       |           
    ''')
    print(
    '{:>47}'.format('Gotowy?'), '\n\n', 
    '{:>31}'.format('NAJEŻDŻAJ!'), '\n\t', 
    '{:>10}'.format('\n\tDociśnij dowolnego konia [klawiszem Enter], aby kontynuować...'), '\n'
    )


def ask_yes_no(question):
    """Ask a question that you can answer 'yes' or 'no'"""
    response = None
    while response not in ('t', 'n'):
        response = input(question).lower()
    return response


def ask_number(question):
    """Ask about the coordinates of the selected field"""
    response = None
    while response not in shots:
        response = int(input(question))
    return response


def start_game():
    """Indicates the Crusader as the first player"""
    go_first = ask_yes_no('Czy jesteś Krzyżowcem? (t/n): ')
    if go_first == 't':
        print('\nPOCZYNAJ')
        crusader = X
    else:
        print('\nZapytam więc jeszcze raz... ')
        start_game()
    return crusader


def new_grid():
    """Create new game board"""
    grid = []
    for grid_size in range(GRID_SIZE):
        grid.append(EMPTY)
    return grid 


def show_grid(grid):
    grid_view = (f'''
                1        2       3
                     |       |
            1      {grid[0][0]} |   {grid[0][1]}   |   {grid[0][2]}  
              _______|_______|_______
                     |       |
            2    {grid[1][0]}   |   {grid[1][1]}   |   {grid[1][2]}
              _______|_______|_______
                     |       |
            3      {grid[2][0]} |   {grid[2][1]}   |   {grid[2][2]}  
                     |       |
        ''')
    print(grid_view) 


def legal_moves(grid):
    """Create list of legal moves"""
    moves = []
    for spam in shots:
        if grid[spam] == EMPTY:
            moves.append(spam)
    return moves


def winner(grid):
    '''Indicate the winner of the game'''
    WAYS_TO_WIN = (
        (7, 8, 9),
        (4, 5, 6),
        (1, 2, 3),
        (7, 4, 1),
        (8, 5, 2),
        (9, 6, 3),
        (7, 5, 3),
        (9, 5, 1))

    for row in WAYS_TO_WIN:
        if grid[0][0] == grid[0][1] == grid[0][2] != EMPTY:
            
            winner = grid[row[0]]
            return winner

        if EMPTY not in grid:
            return TIE

    return None 


def player_moves(grid, crusader):
    '''Do crusader move'''
    grid = grid[:]
    legal = legal_moves(grid)
    move = None
    while move not in legal:
        move = ask_number("Wskaż pole, które chcesz zająć: ")
        if move not in legal:
            print("\nTo pole jest już oblegane przez nieprzyjaciela.")
    print("Świetnie")
    return move


def next_turn(turn):
    '''Change the player'''
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, sultan, crusader):
    if the_winner != TIE:
        print(the_winner, 'jest zwycięzcą!\n')
    else:
        print('Remis!\n')

    if the_winner == sultan:
        print("Jak przewidywałem, Człowieku, jeszcze raz zostałem triumfatorem.  \n" \
              "Dowód na to, że komputery przewyższają ludzi pod każdym względem.")

    elif the_winner == crusader:
        print("No nie!  To niemożliwe!  Jakoś udało Ci się mnie zwieść, Człowieku. \n" \
              "Ale to się nigdy nie powtórzy!  Ja, komputer, przyrzekam Ci to!")

    elif the_winner == TIE:
        print("Miałeś mnóstwo szczęścia, Człowieku, i jakoś udało Ci się ze mną " \
              "zremisować. \nŚwiętuj ten dzień... bo to najlepszy wynik, jaki możesz " \
              "kiedykolwiek osiągnąć.")


def main():
    n = ' '
    while n == ' ':
        show_instruction()
        n = input()
    sultan, crusader = start_game()
    turn = X
    grid = new_grid()
    show_grid(grid)

    while not winner(grid):
        if turn == crusader:
            move = crusader_move(grid, crusader)
            grid[move] = crusader
        else:
            move = sultan_move(grid, sultan, crusader)
            grid[move] = sultan
        show_grid(grid)
        turn = next_turn(turn)

    the_winner = winner(grid)
    congrat_winner(the_winner, sultan, crusader)


# PROGRAM EXECUTE
main()