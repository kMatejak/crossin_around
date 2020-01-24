def show_instruction_1():
    print('\tSułtan Kefiratu pomny o zniewagę jakiej doznał, wyzwał na poje- \
        \n\tdynek dzielnego Krzyżowca Ogórkomira. Wciel się w rolę waleczn- \
        \n\tego Krzyżowca lub bezwględnego Sułtana i wgnieć swojego przeci-\
        \n\twnika w piaski pustyni.\
        \n\n\tDostępna jest plansza składająca się z 9 pól, na których rozeg-\
        \n\tra się ta krwawa walka. Krzyżowiec krzyżuje (jakżeby inaczej),\
        \n\ta Sułtan puszcza toksyczne kółka z fajki wodnej. Ruch odbywa\
        \n\tsię na zmianę poprzez wskazanie numeru pustego pola. \
        \n\n\tZwyciężysz, o ile zajmiesz trzy sąsiadujące ze sobą pola:\
        \n\tpoziomo, pionowo lub ukośnie.')


def show_instruction_2():
    print('\n\tTwój przykładowy tryumf może wyglądać tak:')


def show_instruction_3():
    return input('\n\tDociśnij dowolnego konia [klawiszem Enter], aby kontynuować...')


def show_opening_adnotation():
    print('\tJako, że zaczyna Krzyżowiec, pytam:\n')


def show_opening_question():
    return input('\tCzy jesteś Krzyżowcem? ')


def show_player_cheer():
    print('\t\tNAJEŻDŻAJ!!!')


def show_next_move_ask():
    return input('\n\tWskaż pole swojego \n\tnajazdu: ')


# ENDINGS

def show_sultan_wins_ending():
    print('\n\tPrzebiegły Sułtan docisnął parszywego Krzyżowca w piach. Następnie \
        \n\trzucił truchło biedaka swoim niebywale wyrośniętym skorpionom. \
        \n\tRadości nie było końca! 69 dziewic zatańczyło kankana.\n')


def show_crusader_wins_ending():
    print('\n\tKrzyżowiec tryumfuje! Chwała eurpejskiej cywilizacji \
        \n\troztacza się nad spalonymi piaskami pustyni. Sułtan gryzie piach.\n')


def show_tie_ending():
    print('\n\tI wszystko to jak krew w piach! Dosłownie. Krzyżowiec \
        \n\tzagazowany toksycznymi oparami fajki wodnej padł twarzą w wydmę \
        \n\tstając się tym samym pokarmem dla okolicznych grzechotników. \
        \n\n\tA sam Sułtan jakkolwiek przebiegły, to teraz z nabiegłymi krwią \
        \n\toczyma, przeszedł kilka metrów do swojego wielbłąda zostawiając \
        \n\tza sobą karmazynową ścieżkę hańby. Padł na wznak - zakrzyżowany \
        \n\tna śmierć.\n')


# ERRORS

def show_error_illegal_move():
    print('\n\tTo pole jest już oblegane. Spróbuj Waść ponownie.\n')


def show_error_not_valid_type():
    print('\n\tMoże za dużo gorzałki wczorajszego wieczora... \
        \n\tPanie, proszę wprowadzić cyfrę w zakresie 1-9.\n')


def show_error_not_crusader():
    print('\n\tMoże Krzyżowiec padł zanim stanął... do walki. \
        \n\tJako, że do tanga potrzeba dwojga (lub dwóch), \
        \n\tpotyczka nie odbędzie się. No, przykro mi.\n')


def error_to_many_inputs():
    print('\n\tI co? Mam tak powtarzać w koło Macieju do usranej... \
        \n\tNie, do czorta, kończymy zabawę! Tylko czekaj! \
        \n\n\tNa pustynię właśnie spadła okrutnie wielka kometa, \
        \n\ti nie ostał się choćby jeden żywy, obesrany pachoł.\
        \n\n\tZADOWOLONY!?\n')
