import zmq


PUB_URL = 'tcp://*:5556'
SUB_URL = 'tcp://localhost:5556'


class QueuePublisher:
    def __init__(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.socket.bind(PUB_URL)

    def send(self, category, message):
        self.socket.send_string(f'{category}/{message}')


class QueueSubscriber:
    def __init__(self, category, callback):
        self.category = category
        self.callback = callback
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect(SUB_URL)
        self.socket.setsockopt_string(zmq.SUBSCRIBE, self.category)

    def start(self):
        while True:
            message = self.socket.recv_string()
            self.callback(message)
