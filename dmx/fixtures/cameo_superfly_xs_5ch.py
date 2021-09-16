from enum import IntEnum
from dmx.dmx import DmxFixture


class Channels(IntEnum):
    MASTER_DIMMER = 0
    LED_COLOR = 1
    LED_STROBE = 2
    LED_ROTATION = 3
    STROBE_PROGRAMS = 4


class CameoSuperflyXS(DmxFixture):
    def __init__(self, channel):
        super().__init__(channel)

    def reset(self):
        self.set_channel(Channels.MASTER_DIMMER, 255)
        self.set_channel(Channels.LED_COLOR, 0)
        self.set_channel(Channels.LED_STROBE, 0)
        self.set_channel(Channels.LED_ROTATION, 0)
        self.set_channel(Channels.STROBE_PROGRAMS, 0)

    def set_color_red(self, submit=True):
        self.set_channel(Channels.LED_COLOR, 20, submit)

    def set_color_green(self, submit=True):
        self.set_channel(Channels.LED_COLOR, 35, submit)

    def set_color_blue(self, submit=True):
        self.set_channel(Channels.LED_COLOR, 50, submit)

    def set_color_white(self, submit=True):
        self.set_channel(Channels.LED_COLOR, 65, submit)

    def set_color_black(self, submit=True):
        self.set_channel(Channels.LED_COLOR, 0, submit)

    def set_shutter(self, value: int, submit=True):
        """
            0 -   5 No Function
            6 - 255 Strobe 1 Hz - 20 Hz
        """
        self.set_channel(Channels.LED_STROBE, value, submit)

    def set_rotation(self, value, submit=True):
        """
              0 - 5   No Function
              6 - 127 Motor indexing
            128 - 255 Motor rotation (slow - fast)
        """
        self.set_channel(Channels.LED_ROTATION, value, submit)
