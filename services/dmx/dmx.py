from DMXEnttecPro import Controller


class DmxControl:
    def __init__(self):
        self.fixtures = {}
        self.dmx = Controller('/dev/ttyUSB0')

    def add_fixture(self, name, fixture, channel):
        self.fixtures[name] = fixture(channel, self.dmx)


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

    def set_mode(self, mode: int, submit=True):
        raise NotImplementedError

    def set_color(self, red, green, blue):
        raise NotImplementedError

    def set_shutter(self, level: int, submit=True):
        raise NotImplementedError

    def set_speed(self, level: int, submit=True):
        raise NotImplementedError
