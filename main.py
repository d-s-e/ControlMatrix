#!/usr/bin/env python
from multiprocessing import Process

from services.twitch.main import main as twitch
from services.dmx.main import main as dmx


if __name__ == '__main__':
    processes = [
        Process(target=dmx),
        Process(target=twitch),
    ]

    for proc in processes:
        proc.start()

    for proc in processes:
        proc.join()
