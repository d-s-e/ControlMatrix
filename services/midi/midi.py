import mido


class MidiControl:
    def __init__(self, port, callback):
        self.port = port
        self.open_port()
        self.set_callback(callback)

    def set_callback(self, callback):
        self._in_port.callback = callback

    def clear_callback(self):
        self._in_port = None

    def open_port(self):
        self._in_port = mido.open_input(self.port)

    def close_port(self):
        self._in_port.close()

    def get_in_ports(self):
        return mido.get_input_names()
