import rtmidi


def midi_acces():
    midiout = rtmidi.MidiOut()
    for port_no in range(midiout.get_port_count()):
            port_name = midiout.get_port_name(port_no)
            if port_name.find('Launchpad Mini') > -1:
                midi_port = midiout.open_port(port_no)
    return midi_port
