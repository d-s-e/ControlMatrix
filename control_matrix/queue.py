import time
import zmq
from threading import Event


MASTER_PORT = '5556'
PUB_URL = 'tcp://*'
SUB_URL = 'tcp://localhost'


class QueuePublisher:
    def __init__(self, pub_port=MASTER_PORT):
        self.pub_url = f'{PUB_URL}:{pub_port}'
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.socket.bind(self.pub_url)

    def send(self, topic, message):
        self.socket.send_string(f'{topic}/{message}')

    def send_raw(self, message):
        self.socket.send_string(message)


class QueueSubscriber:
    def __init__(self, topic, callback, sub_port = MASTER_PORT, stop_flag: Event = None):
        self.stop_flag = stop_flag or Event()
        self.topic = topic
        self.callback = callback
        self.sub_url = f'{SUB_URL}:{sub_port}'
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect(self.sub_url)
        self.socket.setsockopt_string(zmq.SUBSCRIBE, self.topic)

    def start(self):
        while not self.stop_flag.is_set():
            try:
                message = self.socket.recv_string(zmq.NOBLOCK)
                self.callback(message)
            except zmq.Again:
                time.sleep(0.2)
