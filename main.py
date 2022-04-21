#!/usr/bin/env python
import logging
from multiprocessing import Process
from threading import Thread

from control_matrix.queue import QueueSubscriber, QueuePublisher

from services.dmx.main import Service as dmx
from services.midi.main import Service as midi
from services.twitch.main import Service as twitch


logging.basicConfig(level = logging.INFO)
log = logging.getLogger(__name__)


class Subscription:
    def __init__(self, name, sub_url, handler):
        self.name = name
        self.handler = handler
        self.socket = QueueSubscriber('', self.handle_message, sub_url)
        self.socket.start()

    def handle_message(self, message):
        log.info(f' <-- {self.name : <10} | {message}')
        self.handler(message)


class ControlMatrix:
    def __init__(self):
        self.queue = QueuePublisher()
        self.threads = [
            Thread(target=Subscription, args=('twitch', 'tcp://localhost:5561', self.forward_handler)),
            Thread(target=Subscription, args=('midi', 'tcp://localhost:5562', self.forward_handler))
        ]
        self.processes = [
            Process(target=dmx),
            Process(target=twitch),
            Process(target=midi),
        ]

    def run(self):
        for thread in self.threads:
            thread.start()

        for proc in self.processes:
            proc.start()

        for proc in self.processes:
            proc.join()

        for thread in self.threads:
            thread.join()

    def forward_handler(self, message):
        log.info(f' --> master    | {message}')
        self.queue.send_raw(message)


if __name__ == '__main__':
    ctrl = ControlMatrix()
    ctrl.run()
