from enum import IntEnum
from services.dmx.dmx import DmxFixture


class Channels(IntEnum):
    MODE = 0
    SPEED = 1
    DIMMER_RED_1 = 2
    DIMMER_GREEN_1 = 3
    DIMMER_BLUE_1 = 4
    DIMMER_RED_2 = 5
    DIMMER_GREEN_2 = 6
    DIMMER_BLUE_2 = 7
    DIMMER_RED_3 = 8
    DIMMER_GREEN_3 = 9
    DIMMER_BLUE_3 = 10


class StairvilleLedBar252Rgb(DmxFixture):
    def reset(self):
        self.set_mode(100, False)
        self.set_color_black(False)
        self.set_speed(0, False)
        self.submit()

    def set_mode(self, mode: int, submit=True):
        """
             0 -  40    Blackout
            41 -  80    3-Segment-Mode
            81 - 120    1-Segment-Mode
           121 - 160    Strobe-Effect
           161 - 200    Color-Change
           201 - 240    Color-Flow
           241 - 255    Color-Change
        """
        self.set_channel(Channels.MODE, mode, submit)

    def set_color_red(self, submit=True):
        self.set_color(255, 0, 0, submit)

    def set_color_green(self, submit=True):
        self.set_color(0, 255, 0, submit)

    def set_color_blue(self, submit=True):
        self.set_color(0, 0, 255, submit)

    def set_color_white(self, submit=True):
        self.set_color(255, 255, 255, submit)

    def set_color_black(self, submit=True):
        self.set_color(0, 0, 0, submit)

    def set_color(self, red, green, blue, submit=True):
        self.set_channel(Channels.DIMMER_RED_1, red, False)
        self.set_channel(Channels.DIMMER_GREEN_1, green, False)
        self.set_channel(Channels.DIMMER_BLUE_1, blue, False)
        if submit:
            self.submit()

    def set_speed(self, value: int, submit=True):
        self.set_channel(Channels.SPEED, value, submit)
