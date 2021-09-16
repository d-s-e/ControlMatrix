#!/usr/bin/env python
from control_matrix.queue import QueueSubscriber
from services.dmx.fixtures.cameo_superfly_xs_5ch import CameoSuperflyXS
from services.dmx.fixtures.stairville_led_bar_252_rgb import StairvilleLedBar252Rgb


DELAY_IN_S = 1
SHUTTER = 5
ROTATION = 128

COMMAND_COLOR = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
}

fixtures = {}


def main():
    print('Starting DMX Service')

    fixtures['bar'] = StairvilleLedBar252Rgb(1)
    fixtures['flower'] = CameoSuperflyXS(22)
    fixtures['flower'].set_rotation(ROTATION)

    sub = QueueSubscriber('dmx', execute_command)
    sub.start()


def execute_command(message):
    _, command, *options = message.split('/')
    print('DMX:', command, options)

    if command == 'color':
        fixtures['bar'].set_color(*COMMAND_COLOR[options[0]])


if __name__ == '__main__':
    main()
