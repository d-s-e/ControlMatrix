#!/usr/bin/env python
import importlib
import logging
import pkgutil
import signal
from multiprocessing import Process
from threading import Event, Thread

import services as services_package
from control_matrix.queue import QueueSubscriber, QueuePublisher


logging.basicConfig(level=logging.INFO)
log = logging.getLogger('ControlMatrix')


class Subscription(Thread):
    def __init__(self, name, sub_port, handler):
        super().__init__()
        self.stop_flag = Event()
        self.name = name
        self.handler = handler
        self.socket = QueueSubscriber('', self.handle_message, sub_port, self.stop_flag)

    def handle_message(self, message):
        log.info(f' <-- {self.name : <10} | {message}')
        self.handler(message)

    def run(self):
        self.socket.start()


class ControlMatrix:
    def __init__(self):
        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)

        self.services_pkg = services_package
        self.services = {}
        self.threads = []
        self.processes = []

        self.queue = QueuePublisher()

    def load_services(self):
        for _, name, is_pkg in pkgutil.iter_modules(self.services_pkg.__path__, self.services_pkg.__name__ + '.'):
            module = importlib.import_module(f'{name}.main')
            try:
                service_cls = getattr(module, 'Service')
                self.services[name] = service_cls
                log.info(f'Loading {service_cls.name}')
            except AttributeError:
                pass

        for name, service in self.services.items():
            print(name, service)

    def run(self):
        self.threads = [
            Subscription(name, service.pub_port, self.forward_handler)
            for name, service in self.services.items() if service.is_enabled and service.pub_port
        ]

        self.processes = [
            Process(target=service, name=name)
            for name, service in self.services.items() if service.is_enabled
        ]

        for thread in self.threads:
            thread.start()

        for proc in self.processes:
            proc.start()

        for proc in self.processes:
            proc.join()

        for thread in self.threads:
            thread.join()

    def stop(self, *args):
        for thread in self.threads:
            thread.stop_flag.set()

    def forward_handler(self, message):
        log.info(f' --> master    | {message}')
        self.queue.send_raw(message)


if __name__ == '__main__':
    ctrl = ControlMatrix()
    ctrl.load_services()
    ctrl.run()
