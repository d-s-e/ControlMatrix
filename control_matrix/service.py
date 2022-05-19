import logging
import signal
from threading import Event, Thread

from control_matrix.queue import QueueSubscriber, QueuePublisher


log = logging.getLogger(__name__)


class SubMasterThread(Thread):
    def __init__(self, topic, handler):
        super().__init__()
        self.stop_flag = Event()
        self.topic = topic
        self.handler = handler
        self.socket = QueueSubscriber(self.topic, self.handler, stop_flag = self.stop_flag)

    def run(self):
        self.socket.start()


class ServiceBase:
    """Base class that each Service must inherit from"""

    name : str = ''
    topic : str = ''
    pub_port : str = ''
    is_enabled : bool = False
    commands : list = []

    def __init__(self, name: str, topic: str, commands: list = None, pub_port: str = None):
        signal.signal(signal.SIGINT, self.handle_shutdown)
        signal.signal(signal.SIGTERM, self.handle_shutdown)
        self.name = name
        self.topic = topic
        self.commands = commands
        self.pub_port = pub_port
        self.pub_socket = None
        self.queue = QueuePublisher(self.pub_port) if self.pub_port else None
        self.thread_sub_master = SubMasterThread(self.topic, self._message_handler)
        self.thread_sub_master.start()

    def _message_handler(self, message):
        topic, command, *options = message.split('/')
        match command:
            case 'config':
                self.handle_config(options)
            case 'shutdown':
                self.handle_shutdown()
            case _:
                self.handle_command(command, options)

    def handle_config(self, options):
        raise NotImplementedError

    def handle_shutdown(self, *args):
        self.thread_sub_master.stop_flag.set()
        self.thread_sub_master.join()
        exit()

    def handle_command(self, command, options):
        raise NotImplementedError
