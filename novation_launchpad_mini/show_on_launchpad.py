import time 
import rtmidi


def midi_acces():
    mo = rtmidi.MidiOut()
    for port_no in range(mo.get_port_count()):
            port_name = mo.get_port_name(port_no)
            print("MIDI out:", port_name)
            if port_name.find('Launchpad Mini') > -1:
                midi_port = mo.open_port(port_no)
    return midi_port

# midi_acces().send_message([0xB0, 00, 00]) #reset


def display_grid(hex, key, color):
    light_grid = midi_acces().send_message
    for key in range(2, 115, 16):
        light_grid([hex, key, color])
    for key in range(5, 118, 16):
        light_grid([hex, key, color])
    for key in range(32, 40):
        light_grid([hex, key, color])
    for key in range(80, 88):
        light_grid([hex, key, color])
    return light_grid

display_grid(0x90, 0, 17)


def ask_number():
    response = input('input nr: ')
    return response 


def get_loc(num):
    pos_dict = {
        '1': '96',
        '2': '99',
        '3': '102',
        '4': '48',
        '5': '51',
        '6': '54',
        '7': '0',
        '8': '3',
        '9': '6',}
    loc = pos_dict.get(num)
    return int(loc)


def display_box(hex, loc, color):
    light_box = midi_acces().send_message
    loc1 = loc + 1
    loc2 = loc + 16
    loc3 = loc + 17
    light_box([hex, loc, color])
    light_box([hex, loc1, color])
    light_box([hex, loc2, color])
    light_box([hex, loc3, color])

    return light_box

# display_box(0x90, 0, 11)
# display_box(0x90, 51, 48)


response = ask_number()
print(response)
loc = get_loc(response)
print(loc)
color = 11
display_box(0x90, loc, color)
#display_box(0x90, 0, 11)
#display_box(0x90, 51, 48)