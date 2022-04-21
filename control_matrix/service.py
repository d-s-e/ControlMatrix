import logging

from threading import Thread

from control_matrix.queue import QueueSubscriber, QueuePublisher


log = logging.getLogger(__name__)


class ServiceBase:
    def __init__(self, name: str, topic: str, commands: list = None, pub_url: str = None):
        self.name = name
        self.topic = topic
        self.commands = commands
        self.pub_url = pub_url
        self.sub_socket = None
        self.pub_socket = None
        self.queue = QueuePublisher(self.pub_url) if self.pub_url else None
        self.thread_sub_master = Thread(target=self.subscribe_to_master)
        self.thread_sub_master.start()

    def subscribe_to_master(self):
        log.info(f'Subscribing {self.name} to topic "{self.topic}"')
        self.sub_socket = QueueSubscriber(self.topic, self._message_handler)
        self.sub_socket.start()

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

    def handle_shutdown(self):
        self.thread_sub_master.join()
        self.sub_socket.close()

    def handle_command(self, command, options):
        raise NotImplementedError
