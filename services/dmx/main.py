#!/usr/bin/env python
import logging
import signal

from control_matrix.service import ServiceBase

from services.dmx.dmx import DmxControl
from services.dmx.fixtures.cameo_superfly_xs_5ch import CameoSuperflyXS
from services.dmx.fixtures.stairville_led_bar_252_rgb import StairvilleLedBar252Rgb
from services.dmx.fixtures.stairville_afh_600 import StairvilleAFH600
from services.dmx.fixtures.eurolite_par56_rgb import EurolitePar65Rgb


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


DELAY_IN_S = 1
SHUTTER = 5
ROTATION = 128


class Service(ServiceBase):
    name = 'DMX Service'
    topic = 'dmx'
    pub_port = ''
    is_enabled = True
    commands = [
        'color'
    ]

    def __init__(self):
        from control_matrix.config import service_dmx as config
        self.config = config
        self.control = DmxControl()
        self.control.add_fixture('bar', StairvilleLedBar252Rgb, 1)
        self.control.add_fixture('flower', CameoSuperflyXS, 41)
        self.control.add_fixture('smoke', StairvilleAFH600, 501)
        self.control.add_fixture('par56', EurolitePar65Rgb, 51)
        self.control.fixtures['flower'].set_rotation(ROTATION)
        super().__init__(self.name, self.topic, self.commands, self.pub_port)

    def handle_config(self, options):
        log.info(f'config -> {options}')

    def handle_command(self, command, options):
        match command:
            case 'color':
                match options[0]:
                    case 'red':
                        self.control.fixtures['bar'].set_color_red()
                        self.control.fixtures['par56'].set_color_red()
                        self.control.fixtures['flower'].set_color_red()
                    case'green':
                        self.control.fixtures['bar'].set_color_green()
                        self.control.fixtures['par56'].set_color_green()
                        self.control.fixtures['flower'].set_color_green()
                    case 'blue':
                        self.control.fixtures['bar'].set_color_blue()
                        self.control.fixtures['par56'].set_color_blue()
                        self.control.fixtures['flower'].set_color_blue()
                    case 'cyan':
                        self.control.fixtures['bar'].set_color(0x00, 0xff, 0xff)
                        self.control.fixtures['par56'].set_color(0x00, 0xff, 0xff)
                        self.control.fixtures['flower'].set_color_black()
                    case 'magenta':
                        self.control.fixtures['bar'].set_color(0xff, 0x00, 0xff)
                        self.control.fixtures['par56'].set_color(0xff, 0x00, 0xff)
                        self.control.fixtures['flower'].set_color_black()
                    case 'yellow':
                        self.control.fixtures['bar'].set_color(0xff, 0xff, 0x00)
                        self.control.fixtures['par56'].set_color(0xff, 0xff, 0x00)
                        self.control.fixtures['flower'].set_color_black()
                    case 'pink':
                        self.control.fixtures['bar'].set_color(0xff, 0x14, 0x93)
                        self.control.fixtures['par56'].set_color(0xff, 0x14, 0x93)
                        self.control.fixtures['flower'].set_color_black()
                    case 'white':
                        self.control.fixtures['bar'].set_color_white()
                        self.control.fixtures['par56'].set_color_white()
                        self.control.fixtures['flower'].set_color_white()
                    case 'black':
                        self.control.fixtures['bar'].set_color_black()
                        self.control.fixtures['par56'].set_color_black()
                        self.control.fixtures['flower'].set_color_black()
                    case _:
                        log.info(f'unmapped color: {options[0]}')
            case 'smoke':
                match options[0]:
                    case 'toggle':
                        self.control.fixtures['smoke'].toggle_smoke()
                    case _:
                        log.info(f'unmapped smoke: {options[0]}')
            case _:
                log.info(f'unmapped command: {command} -> {options}')


def main():
    log.info('Starting DMX Service')
    Service()
    signal.pause()


if __name__ == '__main__':
    main()
