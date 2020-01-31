def show_instruction_1():
    print("\tSultan Emir, remembering the insult he suffered, challenged \
        \n\tcrusader Sir Robin the Not-Quite-So-Brave-as-Sir-Lancelot to \
        \n\ta duel. Take on the role of the bravely bold Sir Robin or \
        \n\tthe ruthless Emir and turn your opponent into the gloomy echo \
        \n\tof desert sands. \
        \n\n\tThere is a board of 9 squares on which this bloody battle will \
        \n\ttake place. The Crusader crosses (how could it be otherwise) \
        \n\tand the Sultan releases toxic water pipe rings. Players move \
        \n\tin turns by indicating the number of an empty field. \
        \n\n\tYou will win if you take three adjacent fields: \
        \n\thorizontally, vertically or diagonally.")


def show_instruction_2():
    print("\n\tYour exemplary triumph might look like this:")


def show_instruction_3():
    return input("\n\tPress any horse [with Enter] to continue ...")


def show_opening_annotation():
    print("\tAs the Crusader begins, I ask:\n")


def show_opening_question():
    return input("\tAre you bravely bold Sir Robin, rode forth from Camelot? ")


def show_player_cheer():
    print("\tHe was not in the least bit scared to be mashed into a pulp,\
        \n\tOr to have his eyes gouged out, and his elbows broken.\
        \n\tTo have his kneecaps split, and his body burned away,\
        \n\tAnd his limbs all hacked and mangled, brave Sir Robin!")


def show_next_move_ask():
    return input("\n\tIndicate the field of your\n\tnext attack: ")


# ENDINGS

def show_sultan_wins_ending():
    print("\n\tBrave Sir Robin ran away\
    \n\tBravely ran away away\
    \n\tWhen danger reared its ugly head\
    \n\tHe bravely turned his tail and fled\
    \n\tYes Brave Sir Robin turned about\
    \n\tAnd gallantly he chickened out\
    \n\tBravely taking to his feet\
    \n\tHe beat a very brave retreat\
    \n\tBravest of the brave Sir Robin")


def show_crusader_wins_ending():
    print("\n\tThe brave Sir Robin triumphs! The glory of European Civilization\
    \n\tspreads over the hot sands of the desert. Sultan kicked the bucket.\n")


def show_tie_ending():
    print("\n\tTIE!? This can't happen too often, right?\n")


# ERRORS

def show_error_illegal_move():
    print("\n\tThis field is already under siege. Try again, sir.\n")


def show_error_not_valid_type():
    print("\n\tMaybe too much wine last night ...\
        \n\tMy Lord, please enter a number in the range 1-9.\n")


def show_error_not_crusader():
    print("\n\tPacking it in and packing it up\
        \n\tAnd sneaking away and buggering off\
        \n\tAnd chickening out and pissing off home\
        \n\tYes, bravely he is throwing in the sponge\n")


def error_to_many_inputs():
    print("\n\tUPS! Too many wrong decisions, too many...\
        \n\tAnd now, we're done!\n")
