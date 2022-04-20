#!/usr/bin/env python
from datetime import datetime
from control_matrix.queue import QueueSubscriber


class Monitor:
    @staticmethod
    def handle_message(message):
        topic, command, *options = message.split('/')
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'{current_time} | {topic : <10} | {command : <10} | {options}')


def main():
    print('Starting Bus Monitoring')

    monitor = Monitor()
    sub = QueueSubscriber('', monitor.handle_message)
    sub.start()


if __name__ == '__main__':
    main()
