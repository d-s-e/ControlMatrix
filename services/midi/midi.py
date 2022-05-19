import logging
import mido


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


class MidiControl:
    def __init__(self, in_port, callback):
        self.in_port = in_port
        self.open_port()
        self.set_callback(callback)

    def set_callback(self, callback):
        self.in_port.callback = callback

    def clear_callback(self):
        self.in_port = None

    def open_port(self):
        self.in_port = mido.open_input(self.in_port)

    def close_port(self):
        self.in_port.close()

    @staticmethod
    def get_in_ports():
        return mido.get_input_names()
