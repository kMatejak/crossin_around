#import launchpad

# GLOBAL VALUES
X = '+'
O = 'o'
EMPTY = ' '
TIE = 'TIE'
GRID_SIZE = 10
SHOTS = [1,2,3,4,5,6,7,8,9]

# PROGRAM
def show_instruction():
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
    '\tsię na zmianę poprzez wskazanie numeru pustego pola.\n')
    print('''\tZwyciężysz, o ile zajmiesz trzy sąsiadujące ze sobą pola: 
        poziomo, pionowo lub ukośnie. 

                         |       |
                     7   |   8   |   9  
                  _______|_______|_______
                         |       |
                     4   |   5   |   6
                  _______|_______|_______
                         |       |
                     1   |   2   |   3 
                         |       |      

        Twój przykładowy tryumf może wyglądać tak 

                         |       |
                     +   |       |   o  
                  _______|_______|_______
                         |       |
                         |   +   |   o
                  _______|_______|_______
                         |       |
                         |       |   + 
                         |       |           
    ''')
    x = input('\tDociśnij dowolnego konia [klawiszem Enter], aby kontynuować...')


def show_grid_template_with_numbers():
    print('''
    


                         |       |
                     7   |   8   |   9  
                  _______|_______|_______
                         |       |
                     4   |   5   |   6
                  _______|_______|_______
                         |       |
                     1   |   2   |   3 
                         |       |      
    ''')


def ask_yes_no(question):
    """Ask a question that you can answer 'yes' or 'no'"""
    response = None
    while response not in ('t', 'n', '', 'maciej jest spoko'):
        response = input(question).lower()
    return response


def ask_number(question):
    """Ask about the number of the selected field"""
    response = None
    while response not in SHOTS:
        response = int(input(question))
    return response


def start_game():
    """Indicates the Crusader as the first player"""
    go_first = ask_yes_no('\t\tCzy jesteś Krzyżowcem? (t/n): ')
    if go_first == 't':
        pass
    elif go_first == 'maciej jest spoko':
        print('\n\t\tTak, Maciej jest naprawdę spoko ziomkiem. Nawet wtedy, gdy... \n\t\tNo dobrze, ale jeszcze raz:\n')
        start_game()
    elif go_first == '':
        print('\n\t\tDoprawdy, nie rozumiem twojego milczenia. \
        \n\t\tJeszcze raz:\n')
        start_game()
    else:
        print('\n\t\tPytam więc jeszcze raz...\n')
        start_game()
    return X


def new_grid():
    """Create new game board"""
    grid = []
    for grid_size in range(GRID_SIZE):
        grid.append(EMPTY)
    return grid 


def print_player_prod():
    print('\t\tNAJEŻDŻAJ!!!')


def great_white_space_printer():
    print('\n'*50)


def show_grid(grid):
    grid_view = (f''' 


                         |       |
                     {grid[7]}   |   {grid[8]}   |   {grid[9]}  
                  _______|_______|_______
                         |       |
                     {grid[4]}   |   {grid[5]}   |   {grid[6]}
                  _______|_______|_______
                         |       |
                     {grid[1]}   |   {grid[2]}   |   {grid[3]}  
                         |       |


    ''')
    print(grid_view) 


def legal_moves(grid):
    """Create list of legal moves"""
    moves = []
    for field in SHOTS:
        if grid[field] == EMPTY:
            moves.append(field)
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
        if grid[row[0]] == grid[row[1]] == grid[row[2]] != EMPTY:  
            winner = grid[row[0]]
            return winner

    if EMPTY not in grid[1:]:
        return TIE

    return None 


def player_moves(grid):
    '''Do crusader move'''
    grid = grid[:]
    legal = legal_moves(grid)
    move = None
    while move not in legal:
        move = ask_number("\t\tWskaż pole, \n\t\tktóre chcesz zająć: ")
        if move not in legal:
            print("\n\t\tTo pole jest już oblegane!")
    return move


def next_turn(turn):
    '''Change the player'''
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner):
    if the_winner == O:
        print('\t\tPrzebiegły Sułtan docisnął parszywego Krzyżowca w piach.'
	'\t\nNastępnie rzucił truchło biedaka swoim niebywale wyrośniętym skorpionom. Radości nie było końca!\n')

    elif the_winner == X:
        print('\tKrzyżowiec tryumfuje! Chwała eurpejskiej cywilizacji'  
        '\troztacza się nad spalonymi poiaskami pustyni. Sułtan gryzie piach.\n')

    else:
        print('\tI wszystko to jak krew w piach! Dosłownie. Krzyżowiec' 
        '\t\nzagazowany toksycznymi oparami fajki wodnej padł twarzą w wydmę' 
        '\t\nstając się tym samym pokarmem dla okolicznych grzechotników.' 
        '\t\nA sam Sułtan jakkolwiek przebiegły, to teraz z nabiegłymi krwią' 
        '\t\noczyma, przeszedł kilka metrów do swojego wielbłąda zostawiając' 
        '\t\nza sobą karmazynową ścieżkę hańby. Padł na wznak - zakrzyżowany na śmierć.\n')


def main():
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


# PROGRAM EXECUTE
main()
