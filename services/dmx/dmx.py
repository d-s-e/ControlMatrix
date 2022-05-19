import signal
from DMXEnttecPro import Controller


class DmxControl:
    def __init__(self):
        signal.signal(signal.SIGINT, self.cleanup)
        signal.signal(signal.SIGTERM, self.cleanup)
        self.fixtures = {}
        self.dmx = Controller("/dev/ttyUSB0")

    def add_fixture(self, name, fixture, channel):
        self.fixtures[name] = fixture(channel, self.dmx)

    def cleanup(self, *args):
        if self.dmx:
            self.dmx.close()


class DmxFixture:
    def __init__(self, channel, controller):
        self.base_channel = channel
        self._controller = controller
        self.reset()

    def set_channel(self, offset, value, submit=True):
        self._controller.set_channel(self.base_channel + offset, value)
        if submit:
            self.submit()

    def submit(self):
        self._controller.submit()

    def reset(self):
        raise NotImplementedError


class DmxChaser:
    pass
