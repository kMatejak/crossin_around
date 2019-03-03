import time 

import launchpad_connection as connection


def reset_board():
    reset = connection.midi_acces().send_message([0xB0, 00, 00])
    return reset


def get_grid_coordinates():
    grid_coordinates = [c for c in range(2, 115, 16)]
    for c in range(5, 118, 16):
        grid_coordinates.append(c)
    for c in range(32, 40):
        grid_coordinates.append(c)
    for c in range(80, 88):
        grid_coordinates.append(c)
    grid_coordinates.sort()
    return grid_coordinates


def show_grid(color=35, loc=0, hex=0x90):
    '''
    color
    3  is RED R3
    50 is YELLOW Y3
    48 is GREEN G3
    35 is ORANGE O4
    '''
    light_on_the_grid = connection.midi_acces().send_message
    grid = get_grid_coordinates()
    
    for coordinate in range(2, 115, 16) and \ 
        for loc in range(5, 118, 16) and
    for loc in range(32, 40) and
    for loc in range(80, 88): 
        light_on_the_grid([hex, loc, color])

    return light_up_grid


def get_position(number):

    positions = {
        '1': '96',
        '2': '99',
        '3': '102',
        '4': '48',
        '5': '51',
        '6': '54',
        '7': '0',
        '8': '3',
        '9': '6',}
    
    return int(positions.get(number))


def display_box(hex, loc, color):

    light_box = connection.midi_acces().send_message

    loc1 = loc + 1
    loc2 = loc + 16
    loc3 = loc + 17

    light_box([hex, loc, color])
    light_box([hex, loc1, color])
    light_box([hex, loc2, color])
    light_box([hex, loc3, color])

    return light_box
