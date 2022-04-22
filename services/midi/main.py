#!/usr/bin/env python
import logging
import signal

from control_matrix.service import ServiceBase
from services.midi.midi import MidiControl


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


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


class Service(ServiceBase):
    name = 'MIDI Service'
    topic = 'midi'
    pub_port = '5562'
    is_enabled = True
    commands = []

    def __init__(self):
        from control_matrix.config import service_midi as config
        self.in_port = config['in_port']
        self.control = MidiControl(self.in_port, self.handle_midi_message)
        super().__init__(self.name, self.topic, self.commands, self.pub_port)

    def cleanup(self, *args):
        self.control.close_port()

    def handle_midi_message(self, message):
        match message.type:
            case 'note_on':
                try:
                    topic, msg = MAPPING[message.note]
                    self.queue.send(topic, msg)
                except KeyError:
                    log.info(f'unmapped key: {message.note}')
            case 'control_change':
                log.info(f'control change: {message.control} = {message.value}')
            case 'note_off':
                pass
            case _:
                log.info(f'unmapped type: {message}')

    def handle_config(self, options):
        log.info(f'config -> {options}')

    def handle_command(self, command, options):
        log.info(f'{command} -> {options}')


def main():
    log.info('Starting MIDI Service')
    Service()
    signal.pause()


if __name__ == '__main__':
    main()
