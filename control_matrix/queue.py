import zmq


MASTER_PUB_URL = 'tcp://*:5556'
MASTER_SUB_URL = 'tcp://localhost:5556'


class QueuePublisher:
    def __init__(self, pub_url=MASTER_PUB_URL):
        self.pub_url = pub_url
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.socket.bind(self.pub_url)

    def send(self, topic, message):
        self.socket.send_string(f'{topic}/{message}')

    def send_raw(self, message):
        self.socket.send_string(message)


class QueueSubscriber:
    def __init__(self, topic, callback, sub_url=MASTER_SUB_URL):
        self.topic = topic
        self.callback = callback
        self.sub_url = sub_url
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect(self.sub_url)
        self.socket.setsockopt_string(zmq.SUBSCRIBE, self.topic)

    def start(self):
        while True:
            message = self.socket.recv_string()
            self.callback(message)
