def show_instruction_1():
    return '\tSułtan Kefiratu pomny o zniewagę jakiej doznał, wyzwał na poje- \
        \n\tdynek dzielnego Krzyżowca Ogórkomira. Wciel się w rolę waleczn- \
        \n\tego Krzyżowca lub bezwględnego Sułtana i wgnieć swojego przeci-\
        \n\twnika w piaski pustyni.\
        \n\n\tDostępna jest plansza składająca się z 9 pól, na których rozeg-\
        \n\tra się ta krwawa walka. Krzyżowiec krzyżuje (jakżeby inaczej),\
        \n\ta Sułtan puszcza toksyczne kółka z fajki wodnej. Ruch odbywa\
        \n\tsię na zmianę poprzez wskazanie numeru pustego pola. \
        \n\n\tZwyciężysz, o ile zajmiesz trzy sąsiadujące ze sobą pola:\
        \n\tpoziomo, pionowo lub ukośnie.'


def show_instruction_2():
    return '\n\tTwój przykładowy tryumf może wyglądać tak:'


def show_instruction_3():
    return '\tDociśnij dowolnego konia [klawiszem Enter], aby kontynuować...'


def show_opening_question():
    return '\tCzy jesteś Krzyżowcem? '


def show_player_cheer():
    return '\t\tNAJEŻDŻAJ!!!'


def show_next_move_ask():
    return '\n\tWskaż pole swojego najazdu: '


def show_sultan_wins_ending():
    return '\n\tPrzebiegły Sułtan docisnął parszywego Krzyżowca w piach. \
        \n\tNastępnie rzucił truchło biedaka swoim niebywale wyrośniętym skorpionom. \
        Radości nie było końca!\n'


def show_crusader_wins_ending():
    return '\n\tKrzyżowiec tryumfuje! Chwała eurpejskiej cywilizacji \
        \n\troztacza się nad spalonymi poiaskami pustyni. Sułtan gryzie piach.\n'

def show_tie_ending():
    return '\n\tI wszystko to jak krew w piach! Dosłownie. Krzyżowiec \
        \n\tzagazowany toksycznymi oparami fajki wodnej padł twarzą w wydmę \
        \n\tstając się tym samym pokarmem dla okolicznych grzechotników. \
        \n\tA sam Sułtan jakkolwiek przebiegły, to teraz z nabiegłymi krwią \
        \n\toczyma, przeszedł kilka metrów do swojego wielbłąda zostawiając \
        \n\tza sobą karmazynową ścieżkę hańby. Padł na wznak - zakrzyżowany \
        \n\tna śmierć.\n'

def show_error_illegal_move():
    return '\n\tTo pole jest już oblegane. Spróbuj Waść ponownie.\n'

def show_error_not_valid_type():
    return '\n\tMoże za dużo gorzałki wczorajszego wieczora... \
        \nPanie, proszę wprowadzić cyfrę w zakresie 1-9.\n'

def show_not_crusader_error():
    return '\n\tMoże Krzyżowiec padł zanim stanął... do walki. \
        \nTrudno, rozgrywka sie nie odbędzie.\n'