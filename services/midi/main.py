#!/usr/bin/env python
import signal
from control_matrix.queue import QueuePublisher
from control_matrix.config import midi as config
from services.midi.midi import MidiControl


MAPPING = {
    36: ('dmx', 'color/red'),
    38: ('dmx', 'color/green'),
    40: ('dmx', 'color/blue'),
    42: ('dmx', 'color/cyan'),
    44: ('dmx', 'color/magenta'),
    46: ('dmx', 'color/yellow'),
    48: ('dmx', 'color/pink'),
    50: ('dmx', 'color/white'),
    51: ('dmx', 'color/black'),
}


class MidiService:
    def __init__(self, port):
        signal.signal(signal.SIGINT, self.cleanup)
        signal.signal(signal.SIGTERM, self.cleanup)

        # self.queue = QueuePublisher()
        self.control = MidiControl(port, self.handle_message)

    def cleanup(self, *args):
        self.control.close_port()

    def handle_message(self, message):
        match message.type:
            case 'note_on':
                try:
                    cat, msg = MAPPING[message.note]
                    # self.queue.send(cat, msg)
                    print('MIDI:', cat, msg)
                except KeyError:
                    print('MIDI: unmapped key:', message.note)
            case 'control_change':
                print('MIDI: control:', f'{message.control} = {message.value}')
            case 'note_off':
                pass
            case _:
                print('MIDI: unmapped type:', message)


def main():
    print('Starting MIDI Service')
    port = config['in_port']
    midi = MidiService(port)
    signal.pause()


if __name__ == '__main__':
    main()
