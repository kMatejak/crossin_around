from languages import polski


def instruction():
    """show game instruction"""
    print('''
     _____                   _       _    ___                            _ 
    /  __ \                 (_)     ( )  / _ \                          | |
    | /  \/_ __ ___  ___ ___ _ _ __ |/  / /_\ \_ __ ___  _   _ _ __   __| |
    | |   | '__/ _ \/ __/ __| | '_ \    |  _  | '__/ _ \| | | | '_ \ / _` |
    | \__/\ | | (_) \__ \__ \ | | | |   | | | | | | (_) | |_| | | | | (_| |
     \____/_|  \___/|___/___/_|_| |_|   \_| |_/_|  \___/ \__,_|_| |_|\__,_|
                                                                       
    ''')
    print('\tSułtan Kefiratu pomny o zniewagę jakiej doznał, wyzwał na poje-\n',
        '\tdynek dzielnego Krzyżowca Ogórkomira. Wciel się w rolę waleczn-\n',
        '\tego Krzyżowca lub bezwględnego Sułtana i wgnieć swojego przeci-\n',
        '\twnika w piaski pustyni.\n\n',
        '\tDostępna jest plansza składająca się z 9 pól, na których rozeg-\n',
        '\tra się ta krwawa walka. Krzyżowiec krzyżuje (jakżeby inaczej),\n',
        '\ta Sułtan puszcza toksyczne kółka z fajki wodnej. Ruch odbywa\n',
        '\tsię na zmianę poprzez wskazanie numeru pustego pola.\n')
    print('\tZwyciężysz, o ile zajmiesz trzy sąsiadujące ze sobą pola:\n',
        '\tpoziomo, pionowo lub ukośnie.\n')
    print(
        '\t\t\t       |       |       \n',
        '\t\t\t   7   |   8   |   9   \n',
        '\t\t\t_______|_______|_______\n',
        '\t\t\t       |       |       \n',
        '\t\t\t   4   |   5   |   6   \n',
        '\t\t\t_______|_______|_______\n',
        '\t\t\t       |       |       \n',
        '\t\t\t   1   |   2   |   3   \n',
        '\t\t\t       |       |       \n')
    print('\tTwój przykładowy tryumf może wyglądać tak:\n')
    print(
        '\t\t\t       |       |       \n',
        '\t\t\t   +   |       |   o   \n',
        '\t\t\t_______|_______|_______\n',
        '\t\t\t       |       |       \n',
        '\t\t\t       |   +   |   o   \n',
        '\t\t\t_______|_______|_______\n',
        '\t\t\t       |       |       \n',
        '\t\t\t       |       |   +   \n',
        '\t\t\t       |       |       \n')
    n = input('\tDociśnij dowolnego konia [klawiszem Enter], aby kontynuować...')


def board_template_with_numbers():
    print(
        '\t\t\t       |       |       \n',
        '\t\t\t   7   |   8   |   9   \n',
        '\t\t\t_______|_______|_______\n',
        '\t\t\t       |       |       \n',
        '\t\t\t   4   |   5   |   6   \n',
        '\t\t\t_______|_______|_______\n',
        '\t\t\t       |       |       \n',
        '\t\t\t   1   |   2   |   3   \n',
        '\t\t\t       |       |       \n')


def player_cheer():
    white_rows(30)
    print('\t\tNAJEŻDŻAJ!!!')
    white_rows(3)


def white_rows(how_many_rows):
    rows = how_many_rows - 1
    print('\n'*rows)


def current(board):
    board_template_with_numbers()
    print('''
        \t\t       |       |      
        \t\t    {}  |   {}   |  {}  
        \t\t_______|_______|_______  
        \t\t       |       |         
        \t\t    {}  |   {}   |   {}  
        \t\t_______|_______|_______ 
        \t\t       |       |         
        \t\t    {}  |   {}   |   {}  
        \t\t       |       |        '''.format(board['7'], board['8'], board['9'], 
                                                board['4'], board['5'], board['6'], 
                                                board['1'], board['2'], board['3']))


def congrat(winner):
    if 'o':
        sultan_wins_ending()
    elif '+':
        crusader_wins_ending()
    elif 'TIE':
        tie_ending()


def sultan_wins_ending():
    print('\t\tPrzebiegły Sułtan docisnął parszywego Krzyżowca w piach. \
        \t\nNastępnie rzucił truchło biedaka swoim niebywale wyrośniętym skorpionom. Radości nie było końca!\n')


def crusader_wins_ending():
    print('\tKrzyżowiec tryumfuje! Chwała eurpejskiej cywilizacji \
        \troztacza się nad spalonymi poiaskami pustyni. Sułtan gryzie piach.\n')


def tie_ending():
    print('\tI wszystko to jak krew w piach! Dosłownie. Krzyżowiec \
        \t\nzagazowany toksycznymi oparami fajki wodnej padł twarzą w wydmę \
        \t\nstając się tym samym pokarmem dla okolicznych grzechotników. \
        \t\nA sam Sułtan jakkolwiek przebiegły, to teraz z nabiegłymi krwią \
        \t\noczyma, przeszedł kilka metrów do swojego wielbłąda zostawiając \
        \t\nza sobą karmazynową ścieżkę hańby. Padł na wznak - zakrzyżowany na śmierć.\n')


def error_illegal_move(): 
    print('To pole jest już oblegane. Spróbuj Waść ponownie.')


def error_not_valid_type():
    print('Może za dużo gorzałki wczorajszego wieczora... \nPanie, proszę wprowadzić cyfrę w zakresie 1-9.')
