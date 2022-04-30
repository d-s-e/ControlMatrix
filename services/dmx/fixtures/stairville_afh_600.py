from enum import IntEnum
from services.dmx.dmx import DmxFixture


class Channels(IntEnum):
    CONTROL = 0


class StairvilleAFH600(DmxFixture):
    def __init__(self, channel, controller):
        self.is_smoking = False
        super().__init__(channel, controller)

    def reset(self):
        self.set_channel(Channels.CONTROL, 0)
        self.is_smoking = False

    def toggle_smoke(self):
        if self.is_smoking:
            self.set_channel(Channels.CONTROL, 0)
            self.is_smoking = False
        else:
            self.set_channel(Channels.CONTROL, 255)
            self.is_smoking = True

    def smoke_on(self):
        self.set_channel(Channels.CONTROL, 255)
        self.is_smoking = True

    def smoke_off(self):
        self.set_channel(Channels.CONTROL, 0)
        self.is_smoking = False
