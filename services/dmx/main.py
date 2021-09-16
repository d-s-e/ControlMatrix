#!/usr/bin/env python
from control_matrix.queue import QueueSubscriber
from services.dmx.dmx import DmxControl
from services.dmx.fixtures.cameo_superfly_xs_5ch import CameoSuperflyXS
from services.dmx.fixtures.stairville_led_bar_252_rgb import StairvilleLedBar252Rgb


DELAY_IN_S = 1
SHUTTER = 5
ROTATION = 128


class DmxService:
    def __init__(self):
        self.control = DmxControl()
        self.control.add_fixture('bar', StairvilleLedBar252Rgb, 1)
        self.control.add_fixture('flower', CameoSuperflyXS, 22)
        self.control.fixtures['flower'].set_rotation(ROTATION)

    def execute_command(self, message):
        _, command, *options = message.split('/')
        print('DMX:', command, options)

        if command == 'color':
            color = options[0]
            if color == 'red':
                self.control.fixtures['bar'].set_color_red()
                self.control.fixtures['flower'].set_color_red()
            elif color == 'green':
                self.control.fixtures['bar'].set_color_green()
                self.control.fixtures['flower'].set_color_green()
            elif color == 'blue':
                self.control.fixtures['bar'].set_color_blue()
                self.control.fixtures['flower'].set_color_blue()
            elif color == 'white':
                self.control.fixtures['bar'].set_color_white()
                self.control.fixtures['flower'].set_color_white()


def main():
    print('Starting DMX Service')

    dmx = DmxService()
    sub = QueueSubscriber('dmx', dmx.execute_command)
    sub.start()


if __name__ == '__main__':
    main()
