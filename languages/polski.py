def show_instruction_1():
    show = print('\tSułtan Kefiratu pomny o zniewagę jakiej doznał, wyzwał na poje- \
        \n\tdynek dzielnego Krzyżowca Ogórkomira. Wciel się w rolę waleczn- \
        \n\tego Krzyżowca lub bezwględnego Sułtana i wgnieć swojego przeci-\
        \n\twnika w piaski pustyni.\
        \n\n\tDostępna jest plansza składająca się z 9 pól, na których rozeg-\
        \n\tra się ta krwawa walka. Krzyżowiec krzyżuje (jakżeby inaczej),\
        \n\ta Sułtan puszcza toksyczne kółka z fajki wodnej. Ruch odbywa\
        \n\tsię na zmianę poprzez wskazanie numeru pustego pola. \
        \n\n\tZwyciężysz, o ile zajmiesz trzy sąsiadujące ze sobą pola:\
        \n\tpoziomo, pionowo lub ukośnie.')
    return show


def show_instruction_2():
    show = print('\n\tTwój przykładowy tryumf może wyglądać tak:')
    return show


def show_instruction_3():
    show = print('\tDociśnij dowolnego konia [klawiszem Enter], aby kontynuować...')
    return show


def show_opening_question():
    show = print('\tCzy jesteś Krzyżowcem? ')
    return show


def show_player_cheer():
    show = print('\t\tNAJEŻDŻAJ!!!')
    return show


def show_next_move_ask():
    show = print('\n\tWskaż pole swojego najazdu: ')
    return show


def show_sultan_wins_ending():
    show = print('\n\tPrzebiegły Sułtan docisnął parszywego Krzyżowca w piach. \
        \n\tNastępnie rzucił truchło biedaka swoim niebywale wyrośniętym skorpionom. \
        Radości nie było końca!\n')
    return show


def show_crusader_wins_ending():
    show = print('\n\tKrzyżowiec tryumfuje! Chwała eurpejskiej cywilizacji \
        \n\troztacza się nad spalonymi poiaskami pustyni. Sułtan gryzie piach.\n')
    return show


def show_tie_ending():
    show = print('\n\tI wszystko to jak krew w piach! Dosłownie. Krzyżowiec \
        \n\tzagazowany toksycznymi oparami fajki wodnej padł twarzą w wydmę \
        \n\tstając się tym samym pokarmem dla okolicznych grzechotników. \
        \n\tA sam Sułtan jakkolwiek przebiegły, to teraz z nabiegłymi krwią \
        \n\toczyma, przeszedł kilka metrów do swojego wielbłąda zostawiając \
        \n\tza sobą karmazynową ścieżkę hańby. Padł na wznak - zakrzyżowany \
        \n\tna śmierć.\n')
    return show


def show_error_illegal_move():
    show = print('\n\tTo pole jest już oblegane. Spróbuj Waść ponownie.\n')
    return show


def show_error_not_valid_type():
    show = print('\n\tMoże za dużo gorzałki wczorajszego wieczora... \
        \nPanie, proszę wprowadzić cyfrę w zakresie 1-9.\n')
    return show


def show_not_crusader_error():
    show = print('\n\tMoże Krzyżowiec padł zanim stanął... do walki. \
        \nTrudno, rozgrywka sie nie odbędzie.\n')
    return show
