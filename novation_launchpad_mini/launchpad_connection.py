import rtmidi


# PREPARE ACCES

def midi_acces():
    midiout = rtmidi.MidiOut()
    for port_no in range(midiout.get_port_count()):
            port_name = midiout.get_port_name(port_no)
            if port_name.find('Launchpad Mini') > -1:
                midi_port = midiout.open_port(port_no)
    return midi_port


# TURN OFF LIGHTS

def reset_board():
    midi_acces().send_message([0xB0, 00, 00])


# CALCULATE COORDINATES

def get_grid_coordinates():
    '''
    :returns: list
    '''
    grid_coordinates = [c for c in range(2, 115, 16)]
    for c in range(5, 118, 16):
        grid_coordinates.append(c)
    for c in range(32, 40):
        grid_coordinates.append(c)
    for c in range(80, 88):
        grid_coordinates.append(c)
    grid_coordinates.sort()
    return grid_coordinates


def get_shot_position(shot):
    positions = {
        '1': 96,
        '2': 99,
        '3': 102,
        '4': 48,
        '5': 51,
        '6': 54,
        '7': 0,
        '8': 3,
        '9': 6,
        }
    pos = positions.get(shot) 
    return pos


# TURN ON THE LIGHTS

def light_grid(color=50, loc=0, hex=0x90):
    '''
    color
    50 is YELLOW Y3
    '''
    light_on_the_grid = midi_acces().send_message
    grid = get_grid_coordinates()
    
    for loc in grid:
        light_on_the_grid([hex, loc, color])


def light_box(shot, color, hex=0x90):
    '''
    color
    3  is RED R3
    50 is YELLOW Y3
    48 is GREEN G3
    35 is ORANGE O4
    '''
    if color == 'red':
        color = 3
    elif color == 'green':
        color = 48
    
    light_box = midi_acces().send_message
    loc = get_shot_position(shot)
    
    loc1 = loc + 1
    loc2 = loc + 16
    loc3 = loc + 17
    
    light_box([hex, loc, color])
    light_box([hex, loc1, color])
    light_box([hex, loc2, color])
    light_box([hex, loc3, color])
