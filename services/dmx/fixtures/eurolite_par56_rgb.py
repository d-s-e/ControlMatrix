from enum import IntEnum
from services.dmx.dmx import DmxFixture


class Channels(IntEnum):
    DIMMER_RED = 0
    DIMMER_GREEN = 1
    DIMMER_BLUE = 2
    COLOR_MACRO = 3
    STROBE_SPEED = 4
    MODE = 5


class EurolitePar65Rgb(DmxFixture):
    def reset(self):
        self.set_mode(0, False)
        self.set_color_black(False)
        self.set_color_macro(0, False)
        self.set_strobe_speed(0, False)
        self.submit()

    def set_mode(self, mode: int, submit=True):
        """
          0 -  31    Dimmer
         32-   63    Decreasing Brightness
         64 -  95    Increasing Brightness
         96 - 127    Decreasing then increasing Brightness
        128 - 159    Auto color mix
        160 - 191    3 color flash
        192 - 223    7 color flash
        224 - 255    Sound control
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
        self.set_channel(Channels.DIMMER_RED, red, False)
        self.set_channel(Channels.DIMMER_GREEN, green, False)
        self.set_channel(Channels.DIMMER_BLUE, blue, False)
        if submit:
            self.submit()

    def set_color_macro(self, value: int, submit=True):
        self.set_channel(Channels.COLOR_MACRO, value, submit)

    def set_strobe_speed(self, value: int, submit=True):
        self.set_channel(Channels.STROBE_SPEED, value, submit)
